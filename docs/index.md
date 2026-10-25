# Open Graf technical documentation

Open Graf provides reusable components written in Graf. This documentation is
organized as an API and engineering reference.

The new unit core is implemented under `src/units`: dimensions, 87 original families,
local definitions, immutable measurements, conversion, arithmetic, dimensions,
powers, roots, comparisons, `radians`, `degrees` and circular/inverse
trigonometry with explicit precision. The [catalogue](units/catalogue.md) contains 290 factories and the
[prefix API](units/prefixes.md) implements all 24 SI and 10 binary prefixes.
[Special units](units/special.md) add 12 named factories, for 302 in total,
plus locally constructed reference/model-dependent quantities. Other library
sections still target an older Graf version.

## Quickstart

Use current `Graf/develop` with the `graf` CLI on your path. In an OpenGraf
checkout, save or run `examples/units/quickstart.graf`:

```graf
import(units: graf {path: "../../src/units"});

(units.meters(2).plus(units.centimeters(30)).value(),
 units.radians(units.degrees(30)).value(),
 units.radians(2.5).sin())
// => 23/10, symbolic pi/6, approximately 0.598472144103956
```

Run `graf run examples/units/quickstart.graf` from the repository root.
Imports are relative to the source file. A numeric call uses that factory's
unit; passing a quantity converts it. Read [the core API](units/core.md) for
definitions and extension, or [migration](units/migration.md) for historical code.

## Reference navigation

- [Download the PDF](downloads/open-graf-units.pdf)
- [Website/PDF build and publication checks](build.md)
- [Plan de trabajo y avance](plan-de-trabajo.md)
- [Testing with gunit](testing.md)
- [Naming conventions and API migration](naming.md)
- [Unit core API and executable example](units/core.md)
- [Conversion and arithmetic](units/operations.md)
- [Angles and trigonometry](units/angles.md)
- [Temperature, logarithmic and contextual units](units/special.md)
- [Migration from historical units](units/migration.md)
- [Catalogue](units/catalogue.md)
- [Decimal and binary prefixes](units/prefixes.md)
- [Units design and API contract](units/design.md)
- [Validation and implementation status](units/validation.md)
- [Sources and conversion policy](units/sources.md)

## Build the documentation

From the repository root:

```sh
python -m pip install -r docs/requirements.txt
python3 tools/docs_build.py
python3 tools/docs_build.py --check
```

The [build reference](build.md) lists native dependencies, outputs and visual checks.
