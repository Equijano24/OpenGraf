# Graf Open Library

A general purpose open source library for the Graf programming language.

See the [11-step plan and current progress](docs/plan-de-trabajo.md).

## Author

* **Esteban Quijano Vincenzi** - *Initial work* - [OpenGraf](https://github.com/OpenGraf)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Units replacement

The new core in `src/units` provides `unit`, dimensions, 25 quantity families,
local definitions and immutable measurements for current Graf. See the
[core API](docs/units/core.md) and [technical documentation](docs/index.md).
Conversions, arithmetic and the reviewed catalogue remain in the next steps.
Run `graf test tests/units` to check this section, or
`graf run examples/units/core.graf` to run the executable example.

## Testing foundation

See [Testing with gunit](docs/testing.md) for the runner, deferred assertions and
failure reports. The executable [gunit smoke suite](tests/testing/gunit-smoke.graf)
checks these prerequisites against the updated `Graf/develop` interpreter.
Run `graf test tests/testing` to execute both contemporary auxiliary suites.

## Compatibility

The existing library targets an older Graf version. This work rewrites units
for current Graf; other legacy sections are not expected to pass its tests.
See [test scope and discovery](docs/testing.md#compatibility-and-units-target).
