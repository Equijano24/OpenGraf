"""Build the website and paginated PDF from the MkDocs navigation and Markdown."""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import logging
import os
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit

import markdown
import yaml

from docs_check import pdf_report, site_report, published_manifest

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = 'https://github.com/Equijano24/OpenGraf/blob/master/'


class RenderDiagnostics(logging.Handler):
    """Rendering warnings/errors that must not disappear in a published build."""

    def __init__(self):
        super().__init__(logging.WARNING)
        self.messages = []

    def emit(self, record):
        self.messages.append(record.getMessage())


def navigation(items: list) -> list[tuple[str, str]]:
    result = []
    for item in items:
        for label, value in item.items():
            result.extend(navigation(value) if isinstance(value, list) else [(label, value)])
    return result


def document_id(path: str) -> str:
    return 'doc-' + path.removesuffix('.md').replace('/', '-')


def source_hash(documents: list) -> str:
    digest = hashlib.sha256()
    inputs = [path for _, path in documents]
    files = ['mkdocs.yml', 'docs/requirements.txt', 'tools/docs_build.py', 'tools/docs_check.py']
    files += ['docs/' + path for path in inputs]
    files += ['docs/assets/pdf.css', 'docs/assets/reference.css']
    for name in sorted(files):
        digest.update(name.encode() + b'\0' + (ROOT / name).read_bytes() + b'\0')
    return digest.hexdigest()


def reference_html(documents: list, date: str, fingerprint: str) -> tuple[str, set]:
    sections = {}
    anchor_maps = {}
    for _, path in documents:
        parser = markdown.Markdown(extensions=['tables', 'fenced_code', 'toc', 'sane_lists'], output_format='xhtml5')
        body = ET.fromstring('<section>' + parser.convert((ROOT / 'docs' / path).read_text()) + '</section>')
        if path == 'index.md':
            # The PDF's linked contents represents the website's overview link menu.
            navigation_block = False
            for child in list(body):
                if child.tag == 'h2':
                    navigation_block = child.get('id') == 'reference-navigation'
                if navigation_block:
                    body.remove(child)
        body.set('id', document_id(path))
        body.set('class', 'document ' + ('catalogue' if path == 'units/catalogue.md' else ''))
        body.set('lang', 'es' if path == 'plan-de-trabajo.md' else 'en')
        mapping = {}
        for element in body.iter():
            if element.get('id') and element is not body:
                original = element.get('id')
                mapping[original] = document_id(path) + '--' + original
                element.set('id', mapping[original])
            # Printed prose uses ordinary hyphens without changing source anchor IDs.
            if element.text:
                element.text = element.text.translate({0x2011: '-', 0x2013: '-', 0x2014: '-'})
            if element.tail:
                element.tail = element.tail.translate({0x2011: '-', 0x2013: '-', 0x2014: '-'})
        sections[path] = body
        anchor_maps[path] = mapping
        if path == 'units/catalogue.md':
            columns = ET.Element('colgroup')
            for width in (25, 17, 8, 25, 25):
                ET.SubElement(columns, 'col', {'style': f'width: {width}%'})
            body.find('.//table').insert(0, columns)
    for path, body in sections.items():
        for element in body.iter('a'):
            url = urlsplit(element.get('href', ''))
            if url.scheme or url.netloc:
                continue
            resolved = ((ROOT / 'docs' / path).parent / unquote(url.path)).resolve() if url.path else (ROOT / 'docs' / path).resolve()
            relative = resolved.relative_to(ROOT / 'docs').as_posix()
            if relative in sections:
                fragment = unquote(url.fragment)
                if fragment and fragment not in anchor_maps[relative]:
                    raise ValueError(f'Unknown documentation anchor: {path}: {element.get("href")}')
                target = anchor_maps[relative][fragment] if fragment else document_id(relative)
                element.set('href', '#' + target)
            elif relative.startswith('downloads/'):
                element.set('href', REPOSITORY + 'docs/' + relative)
            else:
                raise ValueError(f'Unresolved documentation link: {path}: {element.get("href")}')
    contents = '<nav class="contents"><h1>Reference contents</h1><p>Technical documentation • ' + html.escape(date) + '</p><ol>'
    contents += ''.join('<li><a href="#' + document_id(path) + '">' + html.escape(label) + '</a></li>' for label, path in documents)
    contents += '</ol></nav>'
    head = '<!doctype html><html lang="en"><head><meta charset="utf-8"/><title>Open Graf - Units technical reference</title>'
    head += '<meta name="author" content="Esteban Quijano Vincenzi"/>'
    head += '<meta name="dcterms.created" content="' + date + 'T00:00:00Z"/>'
    head += '<meta name="description" content="Units API, catalogue, migration, sources and validation. Source fingerprint: ' + fingerprint + '"/>'
    head += '</head><body>'
    return head + contents + ''.join(ET.tostring(body, encoding='unicode', method='html') for body in sections.values()) + '</body></html>', {document_id(path) for _, path in documents}


def pdf_publication(documents: list, date: str, fingerprint: str) -> dict:
    from weasyprint import CSS, HTML, default_url_fetcher

    def local_resource(url: str, *args, **kwargs):
        if urlsplit(url).scheme not in ('file', 'data', ''):
            raise ValueError('The reference renderer only reads local resources: ' + url)
        return default_url_fetcher(url, *args, **kwargs)

    text, anchors = reference_html(documents, date, fingerprint)
    intermediate = ROOT / 'output/docs'
    intermediate.mkdir(parents=True, exist_ok=True)
    (intermediate / 'reference.html').write_text(text)
    target = ROOT / 'output/pdf/open-graf-units.pdf'
    target.parent.mkdir(parents=True, exist_ok=True)
    diagnostics = RenderDiagnostics()
    logger = logging.getLogger('weasyprint')
    logger.addHandler(diagnostics)
    try:
        HTML(string=text, base_url=str(ROOT / 'docs'), url_fetcher=local_resource).write_pdf(
            target, stylesheets=[CSS(filename=ROOT / 'docs/assets/pdf.css')], pdf_identifier=fingerprint)
    finally:
        logger.removeHandler(diagnostics)
    if diagnostics.messages:
        raise ValueError('PDF renderer diagnostics: ' + '; '.join(diagnostics.messages))
    catalogue = json.loads((ROOT / 'tools/units-catalogue.json').read_text())
    factories = [row['name'] for row in catalogue['units'] + catalogue['special_units']]
    report = pdf_report(target, anchors, factories)
    folder = ROOT / 'docs/downloads'
    folder.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(target, folder / target.name)
    manifest = dict(reference_date=date, source_sha256=fingerprint, source_documents=len(documents), pdf=report)
    (folder / 'build.json').write_text(json.dumps(manifest, indent=2) + '\n')
    return manifest


def site_publication() -> dict:
    subprocess.run([sys.executable, '-m', 'mkdocs', 'build', '--strict', '-f', str(ROOT / 'mkdocs.yml')], check=True)
    return site_report(ROOT / 'site')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check the published PDF fingerprint and rebuild/validate the website without rendering a new PDF.')
    args = parser.parse_args()
    config = yaml.safe_load((ROOT / 'mkdocs.yml').read_text())
    epoch = str(int(datetime.fromisoformat(str(config['extra']['reference_date'])).replace(tzinfo=timezone.utc).timestamp()))
    if os.environ.get('SOURCE_DATE_EPOCH') != epoch:
        # FontTools reads this standard build input when embedding font timestamps.
        # Relaunch only this build process; the invoking shell is unchanged.
        os.execve(sys.executable, [sys.executable, str(Path(__file__).resolve()), *sys.argv[1:]],
                  {**os.environ, 'SOURCE_DATE_EPOCH': epoch})
    documents = navigation(config['nav'])
    fingerprint = source_hash(documents)
    try:
        for tool, arguments in [('units_catalogue.py', ['--check']), ('units_audit.py', [])]:
            subprocess.run([sys.executable, str(ROOT / 'tools' / tool), *arguments], check=True, capture_output=True)
        manifest = published_manifest(ROOT, fingerprint) if args.check else pdf_publication(documents, str(config['extra']['reference_date']), fingerprint)
        print(json.dumps(dict(pdf=manifest, site=site_publication()), indent=2))
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        raise SystemExit(str(error)) from error
