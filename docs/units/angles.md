# Angles and trigonometry

Step 7 provides the public factories `radians` and `degrees`, conversions with
symbolic pi, six circular functions and seven inverse functions. These use the
shared `angle` family and Graf's `common.math` implementation.

## Import and use

```graf
// Save as examples/units/angles.graf, relative to the repository root.
import(units: graf {path: "../../src/units"});

(units.radians(20).value(),
 units.radians(units.degrees(30)).value(),
 units.degrees(units.radians(pi)).value(),
 units.radians(20).plus(units.degrees(15)).value().round(6),
 units.radians(2.5).sin(),
 units.degrees(30).sin(0),
 units.degrees.asin(1.over(2)).value(),
 units.degrees.atan2(1, -1).value())
// => 20, symbolic pi/6, 180, 20 + 261799/1000000,
//    149618036025989/250000000000000, 1/2, 30, 135
```

Run `graf run examples/units/angles.graf` from the repository root. A numeric
argument is in the factory's own unit: `radians(20)` is twenty radians,
`degrees(20)` is twenty degrees. A quantity argument requests conversion.
There is no implicit interpretation of a bare number as degrees.

## Definitions and source files

| Public entry | Shared implementation | Symbol | Coherent scale | Prefix eligibility |
| --- | --- | --- | --- | --- |
| `src/units/angle.graf` | `src/units/core/angle.graf` | Family | Radians are coherent | Per definition |
| `src/units/radians.graf` | `src/units/core/radians.graf` | `rad` | 1 | Yes |
| `src/units/degrees.graf` | `src/units/core/degrees.graf` | `°` | pi/180 | No |

Both scales are exact; pi is a symbolic Graf number. Metadata records BIPM's SI
Brochure, ninth edition, version 4.01, Tables 4 and 8. See [sources](sources.md).
Prefix eligibility is metadata; the prefix API belongs to step 8.

Each definition inherits `angle`, which inherits `unit`. Measurements are
immutable instances with their original number and an explicit `factory`
reference. All eight dimension exponents are zero, but the kind is `angle`.
Ratios and solid angles remain distinct kinds and are not implicitly converted.
Aliases and imports from the library root share the same core definitions.

Mixed sums/subtractions and scalar operations retain the left factory. Angles
can also use the [common conversion and arithmetic API](operations.md).
`equals` compares representation; `.equal-to` compares compatible numeric
values. Symbolic pi expressions can have different trees but the same value.

## Circular functions

| Message on an angular measurement | Result |
| --- | --- |
| `.sin(precision)` | Sine |
| `.cos(precision)` | Cosine |
| `.tan(precision)` | Tangent |
| `.cot(precision)` | Cotangent |
| `.sec(precision)` | Secant |
| `.csc(precision)` | Cosecant |

Every message converts to coherent radians and delegates to the corresponding
`common.math` function. The result is a dimensionless Graf number, with no unit
wrapper. Precision is optional and defaults to 15 decimal places. It is an
integer parameter on each call; no global setting changes.

Exact special values remain exact, including at precision zero:
`degrees(30).sin(0)` is 1/2 and `degrees(90).sin()` is the integer 1.
Nonexact values are the rational approximations supplied by `common.math`,
which can retain more digits than binary64. A request for 30 places is passed
through unchanged. Numeric domain and available-precision errors propagate as
Graf exceptions; tangent at 90 degrees is undefined.

Payloads are not normalized modulo a turn. `degrees(360000030).sin()` is 1/2
and its stored value remains 360000030. Nonangular quantities have no circular
methods. The numeric constructor accepts Graf numbers; circular functions
require the real operands supported by `common.math`.

## Inverse functions

Invoke inverse functions on a concrete factory, with dimensionless real numbers:

| Factory message | Principal range in radians |
| --- | --- |
| `.asin(ratio, precision)` | [-pi/2, pi/2] |
| `.acos(ratio, precision)` | [0, pi] |
| `.atan(ratio, precision)` | (-pi/2, pi/2) |
| `.acot(ratio, precision)` | (0, pi) |
| `.asec(ratio, precision)` | [0, pi], excluding pi/2 |
| `.acsc(ratio, precision)` | [-pi/2, pi/2], excluding 0 |
| `.atan2(y, x, precision)` | [-pi, pi]; negative x axis is pi |

The factory converts the radian result of `common.math` to its own unit and
constructs a new immutable measurement through `quantity(number)`.
`degrees.asin(0.5).value()` is 30; `radians.asin(1).value()` is symbolic pi/2.
`atan2` takes y before x and refuses the origin. The inverse domains and
principal ranges are those of Graf; asin/acos require [-1, 1], and asec/acsc
require an absolute input of at least 1.

The same optional precision defaults to 15 and measures the numeric calculation
in radians **before** conversion to the target unit. A nonexact inverse in degrees
can therefore have a symbolic payload containing a rational divided by pi.
Use `.rounded(places)` to round the displayed unit explicitly; the inverse's
precision argument is not a promise of that many displayed degree decimals.
An angular measurement is not a dimensionless ratio argument. An abstract family
or an already constructed measurement is not an inverse factory.

## Local angular definitions

```graf
turns$ = units.angle.definition("local-turn", "turn", pi.times(2));
turns$(1.over(4)).sin()             // 1
turns$.asin(1).value()              // 1/4
units.degrees(turns$(1.over(4))).value() // 90
```

Definitions inherit the same circular and inverse methods without registration.
Overrides of `quantity(number)` remain the construction protocol for inverse
results. Source, exactness, prefix flags and offsets have typed defaults in the
base unit so overriding metadata does not remove unit/family membership.

## Precision boundary

OpenGraf stores constructor payloads and forwards `common.math` results without
an extra float conversion. Subsequent arithmetic follows Graf's numeric promotion
rules. Graf currently can promote a rational with components beyond Int64 to
`float64`, even without a float operand. Thus an arbitrary-precision sine result
is rational, but later `.times(1)` can lose digits. This existing engine behavior
is not redefined by units; see the precision question recorded in Graf's
`Open-Work-Checklist`. Exact circular anchors and symbolic angular conversion do
not require that promotion. Complex numeric payload construction remains supported;
complex circular-function support depends on Graf and is not added here.
