# Open Graf technical documentation

Open Graf provides reusable components written in Graf. This documentation is
organized as an API and engineering reference.

The units replacement is currently specified, not released. The existing files
under `src/units` are legacy code and do not implement the API below.

- [Plan de trabajo y avance](plan-de-trabajo.md)
- [Testing with gunit](testing.md)
- [Units design and API contract](units/design.md)
- [Validation and implementation status](units/validation.md)
- [Sources and conversion policy](units/sources.md)

## Build the documentation

From the repository root:

```sh
python -m pip install -r docs/requirements.txt
mkdocs build --strict
```

`site/` contains the generated static website. For a PDF from the same Markdown
sources, install Pandoc and a LaTeX PDF engine, then run:

```sh
pandoc docs/index.md docs/testing.md docs/units/design.md docs/units/validation.md \
  docs/units/sources.md --standalone --toc -o open-graf-units.pdf
```

The PDF command is a rendering option, not an additional source of documentation.
