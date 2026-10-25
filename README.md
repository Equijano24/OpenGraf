# Graf Open Library

A general purpose open source library for the Graf programming language.

See the [11-step plan and current progress](docs/plan-de-trabajo.md), and the
[naming conventions and API migration](docs/naming.md).

## Author

* **Esteban Quijano Vincenzi** - *Initial work* - [OpenGraf](https://github.com/OpenGraf)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Units replacement

The new core in `src/units` provides `unit`, dimensions, 87 quantity families,
local definitions and immutable measurements for current Graf. See the
[core API](docs/units/core.md) and [technical documentation](docs/index.md).
[Conversion and arithmetic](docs/units/operations.md) are implemented, including
compound dimensions, powers, roots, comparisons and local extensions.
[Angles and trigonometry](docs/units/angles.md) provide `radians`, `degrees`,
symbolic conversion, circular/inverse functions and precision parameters.
The reviewed [catalogue](docs/units/catalogue.md) has 290 factories, including
meters, kilometers, feet and SI/engineering units. The [prefix API](docs/units/prefixes.md)
provides all 24 SI and 10 binary prefixes. [Special units](docs/units/special.md)
add temperature points, logarithmic ratios, retained references, gauge pressure
and explicit activity, chemical-equivalent and radiation models. There are
302 named factories in the complete catalogue.
Run `graf test tests/units` to check this section, or
`graf run examples/units/operations.graf` to run the arithmetic example, or
`graf run examples/units/angles.graf` for angles, or
`graf run examples/units/catalogue.graf` for catalogue units and prefixes, or
`graf run examples/units/special.graf` for the special rules.

## Testing foundation

See [Testing with gunit](docs/testing.md) for the runner, deferred assertions and
failure reports. The executable [gunit smoke suite](tests/testing/gunit-smoke.graf)
checks these prerequisites against the updated `Graf/develop` interpreter.
Run `graf test tests/testing` to execute both contemporary auxiliary suites.

## Compatibility

The existing library targets an older Graf version. This work rewrites units
for current Graf; other legacy sections are not expected to pass its tests.
See [test scope and discovery](docs/testing.md#compatibility-and-units-target).
