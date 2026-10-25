# Migration from historical units

The replacement targets current `Graf/develop`. It changes imports, extension
protocols, several names and some semantics. It does not provide automatic
backward-compatible aliases. The original implementation is pinned at
[OpenGraf `1397b974`](https://github.com/Equijano24/OpenGraf/tree/1397b974816c00fe8d535db8f566d90523d412bf/src/units),
just before the unit rewrite. The machine-readable
[`tools/units-migration.json`](https://github.com/Equijano24/OpenGraf/blob/master/tools/units-migration.json)
accounts for all **31 historical factories and four historical test cases**.

## Imports and test execution

Replace `with {open.units, open.units.distance, ...}` and the old repository
setup with an explicit import. Paths are relative to the importing file:

```graf
import(units: graf {path: "../../src/units"});
units.meters(units.kilometers(1)).value()
```

This is the path used by `examples/units/*.graf`. Factories are direct members of
`units`; `length`, `mass` and the other families are extension bases, not folders
containing their old factories. An import of the entire library is unnecessary.

Run the modern targets from the OpenGraf repository root:

```sh
graf test tests/units
graf test tests/testing
graf test tests/units-test.graf
```

The retained `tests/units-test.graf` file forwards to
`tests/units/legacy-cases.graf`, which expresses its original four cases in gunit.
The directory target already includes those cases once. The single-file command
is a focused migration check, not another set to add to the directory count.

`setup.graf`, `run-tests.graf` and `run-tests.bat` belong to the old library/test
runner. They are not used to validate current units. Other legacy library
sections and tests remain outside this migration; scanning all of `tests` is
not the supported units command.

| Historical test | Modern case in `legacy-cases.graf` |
| --- | --- |
| `Distance Conversions` | `verify-distance-conversions` |
| `Distance Arithmetic` | `verify-distance-arithmetic` |
| `Temperature Conversions` | `verify-temperature-conversions` |
| `Comparable` | `verify-closed-interval-comparison` |

Use `common.testing.gunit.test>> verify-name(): (...)` rather than
`test-fixture` / `test("name")`. `assert.are-equal` becomes
`common.testing.gunit.assert-equals`; `assert.is-true` becomes `assert`.
Collect expected and actual values in tuples when asserting a required response:
an empty stream must fail the assertion instead of skipping it. The
[testing reference](../testing.md) documents deferred failures and discovery.

## Family and factory names

| Historical family | Current family | Important distinction |
| --- | --- | --- |
| `distance` | `length` | Named factories now live directly under `units`. |
| `weight` | `mass` | Grams, kilograms and avoirdupois pounds measure mass. Force is separate. |
| `information-unit` | `information` | Coherent coordinate is bits; prefixes state decimal/binary intent. |
| `temperature` | `temperature-point` / `temperature-difference` | Absolute points and intervals have different arithmetic. |
| `angle` | `angle` | Radians/degrees are direct factories; conversion retains symbolic pi. |
| `unit` | `unit` | Measurements now compose a number with an explicit factory and dimensions. |

The following table covers every historical factory. `units.` is omitted from
modern names. Preserved spellings can still have changed behavior as described
below; this is not a promise to reproduce old defects.

| Historical module | Historical names | Current replacements |
| --- | --- | --- |
| `distance` | `kilometers`, `meters`, `centimeters` | Same names |
| `distance` | `milimeters` | `millimeters` |
| `distance` | `miles`, `yards`, `feet`, `inches`, `micrometers` | Same names; international definitions and corrected micro symbol |
| `angle` | `radians`, `degrees` | Same names; numeric inputs are in the selected unit; degree conversion corrected |
| `weight` | `kilograms`, `grams`, `pounds` | Same names, in family `mass` |
| `weight` | `ounces` | `avoirdupois-ounces`; `troy-ounces` is a different explicit convention |
| `temperature` | `celsius`, `fahrenheit` | Same names, representing points |
| `temperature` | `kelvin` | `kelvins`, representing points |
| `information-unit` | `bits`, `bytes` | Same names |
| `information-unit` | `kilobytes`, `megabytes`, `gigabytes`, `terabytes` | `kibibytes`, `mebibytes`, `gibibytes`, `tebibytes` to retain old binary magnitudes |
| `information-unit` | `petabytes`, `exabytes`, `zettabytes`, `yottabytes` | `pebibytes`, `exbibytes`, `zebibytes`, `yobibytes` to retain old binary magnitudes |
| `information-unit` | `brontobytes`, `geopbytes` | `robibytes` (2^90 bytes), `quebibytes` (2^100 bytes) |
| `information-unit` | `saganbytes` | Explicit local 2^110-byte definition; no standard catalogue alias |

The historical byte-prefix factories used 1024 powers under decimal-looking
names. Current `kilobytes` means 1000 bytes, whereas `kibibytes` means 1024.
Choose which intent to preserve before changing a name. Correct symbols are
`kB` / `KiB`, `MB` / `MiB`, and so on. The historical `MG`, `BB`, `OB` and `SB`
spellings are not installed as unit aliases. The largest old scale can be
reconstructed locally with `prefix("legacy-sagan", "legacy-SB", 2, 110, source)`
applied to `bytes`; the source must identify it as a local historical convention.
See the [prefix reference](prefixes.md) and its primary sources.

## Definitions, extension and payloads

| Historical API | Current replacement |
| --- | --- |
| `distance(rate, suffix)` | `length.definition(id, symbol, coherentScale)` |
| `unit(fromCallable, toCallable, suffix)` | A family definition with explicit conversion metadata or overridden conversion methods |
| `internal-constructor(type, referenceValue)` | Override `factory.quantity(number)` when construction needs validation; return an immutable measurement with `amount` and `factory` |
| `reference-value` | `.coherent-value()` for calculations; not an automatic stored-data migration |
| `sufix` | `.symbol` metadata |
| `.value()` | Same name, now the stored/display numeric payload |
| `.to(text)` | Explicit Graf string template over `.value()` and `.symbol` |
| `compared-to` | Same numeric comparison protocol, with kind/dimension checks |
| `comparable(q).between(a, b)` | `q.gte(a).and(q.lte(b))`; use `gt` / `lt` for open endpoints |

The generic linear/affine mapping is `coherent = value × scale + offset`.
Exact scale literals use forms such as `0.01(0)` or `1.exact-quotient(100)`.
A plain `0.01` is a Graf floating value. Constructing a unit preserves the supplied
number's type; it does not silently turn every payload into a rational or float.

Functions now name their results. The provisional names introduced during the
rewrite (`make`, `define`, `with-value`, etc.) are separately mapped in
[naming conventions](../naming.md). They were not the historical unit API.
The current [core](core.md), [operation](operations.md) and [special](special.md)
references define the extension protocols. A custom conversion must provide
both directions consistently and declare kinds, dimensions and linear-arithmetic
eligibility. A nonlinear mapping is not made linear by giving it a scale field.

Formatting belongs to the presentation boundary. For example, a float payload
can be rendered with `"{0:.2f} {1}"(q.value(), q.symbol)`. This returns a string,
not a changed measurement. Formatting support depends on the numeric type and
specifier supported by Graf; an unsupported specifier/type is a Graf format
failure. Do not force a rational or symbolic payload into a float merely to
implement a measurement constructor.

## Stored values and coherent references

Historical `reference-value` was relative to each old family's implicit basis.
The bases are now explicit and consistent:

| Family | Historical reference | Current coherent coordinate |
| --- | --- | --- |
| Length | meters | meters |
| Mass | grams | kilograms |
| Information | bytes | bits |
| Temperature points | degrees Celsius | kelvins |
| Angles | radians, with a defective degree delegate | radians, with symbolic conversion |

When importing stored data, first identify whether it holds a displayed payload
or an old reference value, and retain the original unit and convention. Reconstruct
a displayed payload through its new factory. For an old reference value, construct
the old coherent unit explicitly (`grams`, `bytes`, `celsius`, etc.), then convert
to the desired factory. Do not copy that number into a new `.amount` field.
The mapping cannot infer the missing unit or repair a value produced by the old
degree bug without original input data.

`radians(20)` is twenty radians; `radians(degrees(20))` performs degree conversion.
The historical degree delegates ignored their arguments and used a short decimal
pi approximation. Those results are not reproduced by the replacement.

## Arithmetic and error changes

Mixed plus/minus for linear units retains the left factory. Scalar times/over
also retains it. Quantity times/over now produces a coherent compound with
composed dimensions; a named factory classifies that compound explicitly.
Kinds with equal dimensions can still be incompatible (energy/torque, for example).
A bare number cannot be added to a measurement. Division by zero remains a Graf
numeric error, and unsupported backend operations propagate their Graf failure.

Temperature conversion uses points, with a lower boundary at zero kelvin.
Point minus point yields an interval. Point plus/minus interval yields a point;
point plus point and point multiplication/division are refused. Replace an old
linear Celsius calculation only after deciding whether its operands are points
or intervals. Logarithmic, gauge, chemical-equivalent and dose-weighted conversions
need the explicit references/models documented in [special units](special.md).

Measurements are immutable instances. Replace an amount through
`.quantity-with-value(number)`; do not assign `.amount`, extend a measured
instance, or alter a definition's scale after using it.

## Validation and coverage

`python3 tools/units_audit.py --legacy-source` verifies that the ledger covers all
factories and tests in the pinned historical sources, all 302 published factories
have a dedicated catalogue test, every referenced migration case exists, and all
seven documentation examples match their executable source. It needs that commit
in local git history. Without `--legacy-source`, the same current-tree checks run
without accessing historical git objects. This is a correspondence check, not
execution or a proof of numerical correctness.

Run `python3 tools/units_catalogue.py --check` to detect drift in generated
sources/reference/tests. Execute `graf test tests/units` for numerical, operation,
extension and failure checks; independent anchors complement catalogue round trips.
The [validation matrix](validation.md) identifies the tests for each contract.
A complete checkout of `Graf/develop` is separately checked with
`dotnet test Graf.Testing/Graf.Testing.csproj`. No unrelated legacy suite is
silently included in these totals.

## Executable migration example

Run `graf run examples/units/migration.graf`. This example preserves old binary
magnitudes where requested and uses current spelling, arithmetic and formatting.

```graf
// Current replacements for the historical units API; no legacy setup is loaded.
import(units: graf {path: "../../src/units"});

length$ = units.kilometers(1).plus(units.meters(2000));
interval$ = units.celsius(20).minus(units.celsius(10));
furlongs$ = units.length.definition("local-furlong", "fur", 201.168(0));
legacy-large$ = units.prefix("legacy-sagan", "legacy-SB", 2, 110,
    "explicit legacy 2^110 byte convention, not an IEC prefix")(units.bytes);
display$ = units.meters(2.5);
formatted$ = "{0:.2f} {1}"(display$.value(), display$.symbol);
inside$ = units.meters(2000).gte(units.kilometers(1)).and(units.meters(2000).lte(units.kilometers(3)));

(length$.value(),
 units.meters(units.millimeters(1)).value(),
 units.grams(units.avoirdupois-ounces(1)).value(),
 units.bytes(units.kibibytes(1)).value(), units.bytes(units.kilobytes(1)).value(),
 units.bytes(legacy-large$(1)).value(),
 units.degrees(units.radians(pi)).value(),
 units.celsius(units.fahrenheit(32)).value(), interval$.value(),
 units.meters(furlongs$(2)).value(), formatted$, inside$)
// => 3, 0.001, 28.349523125, 1024, 1000, 1298074214633706907132624082305024,
//    180, 0, 10, 402.336, "2.50 m", yes
```
