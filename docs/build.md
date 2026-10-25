# Website and PDF builds

The website and downloadable PDF use the Markdown pages in `mkdocs.yml`, in its
navigation order. The PDF is a technical reference with linked sections, code,
tables, source references and page numbers. The catalogue uses landscape pages;
the API and guides use portrait pages. The overview's website link menu is
represented by the PDF's linked contents. There is no separate book manuscript.

## Install documentation dependencies

From the OpenGraf repository root, with Python 3.10 or newer:

```sh
python -m pip install -r docs/requirements.txt
```

PDF rendering also needs Pango/Harfbuzz and DejaVu Sans/DejaVu Sans Mono fonts.
On Ubuntu/Debian, install the native dependencies if they are absent:

```sh
sudo apt-get install libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz-subset0 fonts-dejavu-core
```

The [WeasyPrint installation reference](https://doc.courtbouillon.org/weasyprint/v66.0/first_steps.html)
has platform-specific instructions. Renderer and Markdown versions are pinned.
Native library or font updates can alter pagination; repeat the visual checks
after changing them. None of these dependencies is needed to run the Graf units.

## Build both formats

```sh
python3 tools/docs_build.py
```

The command first checks generated catalogue files and unit/example
correspondence. It then creates the PDF, copies it into the documentation's
download directory, builds MkDocs in strict mode and checks local links/assets
and HTML anchors. Any renderer warning or unresolved internal PDF link fails
the build.

| Output | Purpose |
| --- | --- |
| `output/pdf/open-graf-units.pdf` | Standalone PDF artifact |
| `output/docs/reference.html` | Intermediate combined HTML for diagnosis |
| `docs/downloads/open-graf-units.pdf` | Published PDF, copied into the generated site |
| `docs/downloads/build.json` | Documentation input fingerprint, PDF hash and page/navigation counts |
| `site/` | Generated static website, including the PDF download |

The PDF and manifest in `docs/downloads` are committed together. The other
generated outputs are ignored. The fingerprint covers all included Markdown,
the navigation, render styles, build/check tools and dependency declarations.
It deliberately excludes the generated PDF and manifest, avoiding a circular
hash dependency. The reference date is explicit in `mkdocs.yml`.
The build restarts its own process with `SOURCE_DATE_EPOCH` set to that date,
fixing embedded font timestamps without changing the caller's environment.
Repeated builds with the verified renderer, fonts and native libraries have
the same PDF bytes; changed fonts/libraries still require a visual review.

## Check an existing publication

```sh
python3 tools/docs_build.py --check
```

This checks the committed PDF's input fingerprint and file hash, then rebuilds
and checks the site. It does not silently regenerate an out-of-date PDF. Use
the normal build after editing documentation, styles or the build pipeline.
To build just the website for local editing, `mkdocs build --strict` also works;
the combined check remains the publication check.

Use `mkdocs serve` to preview the website locally. Deploy the contents of `site/`
to a static host when a hosting destination is selected. Building a site does
not configure GitHub Pages or another hosting service.

## Publication checks

The complete checkpoint is recorded in [validation](units/validation.md).
Before publishing updated reference files:

1. Run `graf test tests/units` and the auxiliary `graf test tests/testing`.
2. Run the six detailed examples plus [the quickstart](index.md#quickstart).
3. Run the catalogue and migration audits, using `--legacy-source` when the
   pinned historical commit is present locally.
4. Build both formats and run `tools/docs_build.py --check`.
5. Render PDF pages with Poppler (`pdftoppm`) and inspect code, table continuations,
   Unicode symbols, page headers/footers and long source links.
6. Open the website at desktop and narrow widths; check navigation, code/table
   scrolling, source links and the PDF download.

The automated PDF check verifies factory names, text safety margins, section
destinations and outlines. It
does not replace visual inspection. Local link checks do not claim that every
external bibliography URL will remain available. The numerical tests validate
units independently of the documentation renderer.
