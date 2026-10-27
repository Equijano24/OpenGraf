# Conversion and arithmetic

Step 6 adds operations to the [unit core](core.md). These examples define local
factories explicitly. Step 8 provides a reviewed [catalogue](catalogue.md) and
[decimal/binary prefixes](prefixes.md) alongside these extension examples.

## Executable example

Save this source as `examples/units/operations.graf` and run
`graf run examples/units/operations.graf` from the repository root:

```graf
import(units: graf {path: "../../src/units"});

meters$ = units.length.definition("meter", "m", 1);
centimeters$ = units.length.definition("centimeter", "cm", 1.over(100));
kilometers$ = units.length.definition("kilometer", "km", 1000);
hours$ = units.duration.definition("hour", "h", 3600);
meters-per-second$ = units.velocity.definition("meter-per-second", "m/s", 1);
kilometers-per-hour$ = units.velocity.definition("kilometer-per-hour", "km/h", 5.over(18));
square-meters$ = units.area.definition("square-meter", "m2", 1);

length$ = meters$(2).plus(centimeters$(30));
speed$ = kilometers$(10).over(hours$(2));
side$ = meters$(square-meters$(9).root(2));

(length$.value(), centimeters$(meters$(2)).value(),
 meters-per-second$(speed$).value(), kilometers-per-hour$(speed$).value(),
 side$.value(), meters$(2).equal-to(centimeters$(200)))
```

The six responses are `23/10`, `200`, `25/18`, `5`, `3`, and `yes`. Graf may
print fractions as mixed numbers. The
[example source](https://github.com/Equijano24/OpenGraf/blob/master/examples/units/operations.graf)
is tested with the current interpreter.

## Conversion

`factory(number)` interprets the number in that definition's unit.
`factory(quantity)` converts a compatible measurement, preserving the target
factory and leaving the input unchanged. The mapping is:

- To coherent value: `amount * scale + offset`.
- From coherent value: `(coherent - offset) / scale`.

`quantity.coherent-value()` returns a number, not another quantity. Identity mappings
skip multiplication by one and addition of zero, retaining the payload and its
numeric backend. Exact rational factors remain rational; no automatic rounding
or conversion to binary floating point is introduced by the unit layer.

Named measurements must have the same kind identifier and all eight dimension
exponents. Equal dimensions alone do not permit energy-to-torque,
frequency-to-radioactivity, angle-to-ratio or absorbed-to-equivalent dose
conversion. A custom family follows the same rules as a built-in family.

An unclassified compound can be converted explicitly to a named definition with
matching dimensions. For example, force times length can be classified as work
or torque. After classification, the result is a named measurement and retains
that kind; subsequent direct work-to-torque conversion is refused.

## Operations

| Message | Result |
| --- | --- |
| `a.plus(b)` / `a.minus(b)` | Compatible kinds and dimensions; result in `a.factory` |
| `a.times(number)` / `a.over(number)` | Displayed payload scaled; `a.factory` retained |
| `a.times(quantity)` | Coherent compound; dimension exponents added |
| `a.over(quantity)` | Coherent compound; dimension exponents subtracted |
| `a.pow(integer)` | Coherent compound; exponents multiplied by the power |
| `a.root(integer)` | Coherent compound; each exponent divided by the degree |
| `a.root(integer, precision)` | Same dimension rule, explicit numeric root precision |
| `a.rounded(places)` | Explicit rounding of displayed payload; factory retained |
| `a.compared-to(b)` | Numeric backend's -1, 0 or 1 after compatible conversion |
| `a.equal-to(b)` | Numeric equality after compatible conversion |
| `a.lt(b)` / `a.lte(b)` / `a.gt(b)` / `a.gte(b)` | Numeric ordering after compatible conversion |

Addition and subtraction require a quantity on the right; a bare number has no
unit. A compound must be classified before adding it to a named measurement.
For example, an area compound is not added directly to square meters, even
though its dimensions match. Two compounds with the same dimensions can be
added directly; they share the compound kind and coherent scale.

Products and quotients do not consult a global registry or infer a physical
kind. Each compound owns an immutable local definition with kind `compound`,
scale one, offset zero and an empty symbol. `.is-compound()` identifies the
classification protocol. A dimensionless quotient remains a quantity until
explicitly classified as a ratio or read with `.value()`.

`.pow(0)` follows Graf's numeric behavior and returns a dimensionless compound.
Negative integer powers and negative root degrees are allowed when the numeric
backend supports them. A root degree cannot be zero, and every resulting
dimension exponent must be an integer. A square root of a length therefore
fails; a square root of an area can produce a length compound.

Roots delegate to the numeric backend with a default precision of 15 decimal
places, or the explicit precision supplied. Exact roots stay exact. Non-exact
roots use that precision. Negative even roots, division by zero and unsupported
numeric operations keep the backend's Graf failure behavior. This does not add
complex arithmetic that the underlying Graf numeric backend lacks.

`equals(a, b)` still compares composite representation. It performs no unit
conversion. Use `.equal-to` to compare compatible physical measurements. Numeric
equality is not an approximate tolerance test.

## Local definitions and factory construction

A family created by `unit.family(kind, dimension)` participates in conversion,
arithmetic and comparison without registration. A definition can be extended
with Graf inheritance; use `override>>` when replacing metadata so reads remain
single-valued. Arithmetic retains the actual left factory, including inherited
methods and refinements.

Every numeric constructor, compatible conversion and replacement payload passes
through `factory.quantity(number)`. Its default implementation creates a composite
instance with `amount` and the explicit `factory` reference. Extensions that
validate or specialize construction should override `quantity` while keeping that
contract. Operations returning a named quantity use its factory's `quantity`;
compound operations use a fresh coherent compound definition.

A conversion into the same factory returns the stored reading. It does not
evaluate the scale. Exact scales and offsets, including temperature points and
gauge pressures, stay exact rationals or symbolic factors. An exact factor `a`
multiplies an existing absolute error by `abs(a)`. The public default precision
is 15 decimal places. A precision argument that a caller supplies is the one
the calculation uses.

`coherent-value-of(number)` and `display-value-of(number)` implement the numeric mapping.
`is-convertible-from(quantity)` reports conversion eligibility; it includes explicit
compound classification. `compatible-with` remains the stricter same-kind and
same-dimension check used by addition and comparisons.

## Affine values and temperature

Addition/subtraction operates on displayed readings after converting the right
operand to the left unit. Scalar multiplication/division operates on the displayed
number. These operations also support offset, logarithmic and referenced units.
When factories are identical, the right number is used directly, avoiding needless
conversion and logarithmic rounding. The factory's `quantity` protocol validates
each result and preserves its metadata.

Dimensional quantity products/quotients, powers and roots require both
`linear-arithmetic: yes` and offset zero. Temperature points, logarithmic levels
and gauge readings set `linear-arithmetic: no`. Temperature differences retain
linear dimensional arithmetic.

[Special units](special.md) implement point/difference arithmetic and absolute-zero
validation. Point plus point retains the left point factory; point minus point
produces a difference. Point plus/minus difference retains the point factory.
Reading arithmetic is distinct from a physical model: adding levels does not
automatically calculate combined signal power, and adding temperatures does not
calculate the equilibrium temperature of a mixture.

## Reading arithmetic example

Save as `examples/units/reading-arithmetic.graf` and run
`graf run examples/units/reading-arithmetic.graf`:

```graf
import(units: graf {path: "../../src/units"});

mw$ = units.si-prefixes.milli(units.watts);
dbm$ = units.logarithmic-reference(mw$(1), units.power-decibels);
dbw$ = units.logarithmic-reference(units.watts(1), units.power-decibels);
gauge$ = units.gauge-pressure(units.pascals(100000), units.bars);

(units.celsius(20).plus(units.celsius(10)).value(),
 units.celsius(20).plus(units.fahrenheit(50)).value(),
 units.celsius(20).times(2).value(),
 units.celsius-differences(10).plus(units.fahrenheit(32)).value(),
 units.power-decibels(20).plus(units.power-bels(1)).value(),
 units.ph(2).plus(units.ph(3)).value(),
 gauge$(1).plus(gauge$(1)).value(), dbm$(20).plus(dbw$(0)).value())
// => 30, 30, 40, 50, 30, 5, 2, 50
```

## Tests

Run `graf test tests/units`. The operation suites compare exact expected values,
factory identities, dimension vectors and expected failures. Value assertions
collect the actual response in a tuple, so an empty stream cannot accidentally
skip an assertion. The suites include independent conversion anchors, compatible
round trips, local family/factory extensions, negative and zero operands,
composed dimensions, roots, precision, and distinct kinds with equal dimensions.
