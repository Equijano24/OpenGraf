# Graf Open Library

A general purpose open source library for the Graf programming language.

See the [11-step plan and current progress](docs/plan-de-trabajo.md).

## Author

* **Esteban Quijano Vincenzi** - *Initial work* - [OpenGraf](https://github.com/OpenGraf)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Units replacement

The new units API is at the specification stage. The existing `src/units` files
are legacy code. See the [technical documentation](docs/index.md) for the agreed
object model, conversion rules, validation matrix and implementation status.

## Testing foundation

See [Testing with gunit](docs/testing.md) for the runner, deferred assertions and
failure reports. The executable [gunit smoke suite](tests/testing/gunit-smoke.graf)
checks these prerequisites against the updated `Graf/develop` interpreter.
Run `graf test tests/testing` to execute both contemporary auxiliary suites.

## Compatibility

The existing library targets an older Graf version. This work rewrites units
for current Graf; other legacy sections are not expected to pass its tests.
See [test scope and discovery](docs/testing.md#compatibility-and-test-scope).
