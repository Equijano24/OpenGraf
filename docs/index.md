# Open Graf technical documentation

Open Graf provides reusable components written in Graf. This documentation is
organized as an API and engineering reference.

The new unit core is implemented under `src/units`: dimensions, 87 families,
local definitions, immutable measurements, conversion, arithmetic, dimensions,
powers, roots, comparisons, `radians`, `degrees` and circular/inverse
trigonometry with explicit precision. The [catalogue](units/catalogue.md) contains 290 factories and the
[prefix API](units/prefixes.md) implements all 24 SI and 10 binary prefixes.
Special-unit rules remain in step 9. Other library sections still target an
older Graf version.

- [Plan de trabajo y avance](plan-de-trabajo.md)
- [Testing with gunit](testing.md)
- [Naming conventions and API migration](naming.md)
- [Unit core API and executable example](units/core.md)
- [Conversion and arithmetic](units/operations.md)
- [Angles and trigonometry](units/angles.md)
- [Catalogue](units/catalogue.md)
- [Decimal and binary prefixes](units/prefixes.md)
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
pandoc docs/index.md docs/testing.md docs/units/core.md docs/units/operations.md docs/units/angles.md docs/units/catalogue.md docs/units/prefixes.md docs/units/design.md docs/units/validation.md \
  docs/units/sources.md --standalone --toc -o open-graf-units.pdf
```

The PDF command is a rendering option, not an additional source of documentation.
