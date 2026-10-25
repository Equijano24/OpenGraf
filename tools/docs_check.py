"""Validate local website targets and the published PDF's source fingerprint."""
from __future__ import annotations

import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class PageLinks(HTMLParser):
    """IDs and local resource references in one generated HTML page."""

    def __init__(self, text: str):
        super().__init__()
        self.ids = set()
        self.links = []
        self.feed(text)

    def handle_starttag(self, tag: str, attrs: list):
        values = dict(attrs)
        if values.get('id'):
            self.ids.add(values['id'])
        for name in ('href', 'src'):
            if values.get(name):
                self.links.append(values[name])


def site_report(site: Path) -> dict:
    pages = {path.resolve(): PageLinks(path.read_text()) for path in site.rglob('*.html')}
    links = 0
    for path, page in pages.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            if url.path.startswith('/'):
                target = (site / unquote(url.path).lstrip('/')).resolve()
            else:
                target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if target.is_dir():
                target = target / 'index.html'
            if not target.is_relative_to(site.resolve()) or not target.is_file():
                raise ValueError(f'Broken local target in {path.name}: {link}')
            fragment = unquote(url.fragment)
            if fragment and target in pages and fragment not in pages[target].ids:
                raise ValueError(f'Broken local anchor in {path.name}: {link}')
            links += 1
    if not pages:
        raise ValueError('The generated site has no HTML pages')
    return dict(html_pages=len(pages), local_links=links)


def pdf_report(path: Path, anchors: set[str], factories: list[str]) -> dict:
    import pdfplumber
    from pypdf import PdfReader

    reader = PdfReader(path)
    if len(reader.pages) < 2 or not reader.outline:
        raise ValueError('The reference PDF lacks pages or navigation outlines')
    names = set(reader.named_destinations)
    missing = anchors - names
    if missing:
        raise ValueError(f'Missing PDF section destinations: {sorted(missing)}')
    text = '\n'.join(page.extract_text() or '' for page in reader.pages)
    for word in ['Unit catalogue', 'Migration from historical units', 'Sources and conversion policy', 'quebibytes', 'Gieck']:
        if word not in text:
            raise ValueError(f'Missing PDF reference content: {word}')
    if '\ufffd' in text:
        raise ValueError('The PDF contains replacement glyphs')
    compact = ''.join(text.split())
    missing_factories = [name for name in factories if name not in compact]
    if missing_factories:
        raise ValueError(f'Missing PDF catalogue factories: {missing_factories}')
    with pdfplumber.open(path) as pdf:
        for index, page in enumerate(pdf.pages, 1):
            if any(c['x0'] < 26 or c['x1'] > page.width - 26 or c['top'] < 15 or c['bottom'] > page.height - 15 for c in page.chars):
                raise ValueError(f'Text exceeds the PDF page safety margin: {index}')
    return dict(pages=len(reader.pages), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest(), destinations=len(names),
                catalogue_factories=len(factories))


def published_manifest(root: Path, source_hash: str) -> dict:
    folder = root / 'docs/downloads'
    manifest = json.loads((folder / 'build.json').read_text())
    if manifest['source_sha256'] != source_hash:
        raise ValueError('Published PDF is stale: rebuild after changing its sources')
    if manifest['pdf']['sha256'] != hashlib.sha256((folder / 'open-graf-units.pdf').read_bytes()).hexdigest():
        raise ValueError('Published PDF differs from its build manifest')
    return manifest
