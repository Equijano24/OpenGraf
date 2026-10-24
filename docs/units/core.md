# Unit core API

The core is implemented for current Graf on `develop`. It provides 25 families,
local unit definitions, integral dimensions, and immutable measurements.
Conversion, quantity arithmetic, trigonometry and the reviewed unit catalogue
are the following implementation steps; the complete target is in the
[design contract](design.md).

## Import and construct

Import the units directory explicitly. Paths are relative to the source file:

```graf
// Save as examples/units/core.graf, relative to the repository root.
import(units: graf {path: "../../src/units"});

meters$ = units.length.define("meter", "m", 1);
length$ = meters$(1.over(3));
changed$ = length$.with-value(2);

(length$.value(), changed$.value(), length$.symbol,
 length$.dimension.length, length$.compatible-with(changed$))
// => 1/3, 2, "m", 1, yes (one response per value)
```

Run `graf run examples/units/core.graf` from the repository root. The
[executable example](https://github.com/Equijano24/OpenGraf/blob/master/examples/units/core.graf)
uses this exact source. Importing all of `src` is unnecessary for units; the
other sections still use an older Graf API.

A bare number is already expressed in the target definition. Construction does
not apply `scale`: `inches$(5).value()` is 5, whatever the definition's scale.
The numeric constructor accepts `number?` and stores the supplied value without
rounding, promotion, conversion to floating point, or numeric decoration.
Integer, arbitrary-size integer, float64, rational and symbolic pi payloads are
covered by the executable tests. A number supplied by a host uses the same
`number?` protocol; the core adds no restrictions on numeric backends.

## Definitions and measurements

`unit` is a class. Each family is an heir of `unit`, a definition is an heir of
its family, and a numeric call makes an instance of that definition. `unit` and
an unfilled family are abstract: they cannot produce a measurement until a
complete definition supplies its metadata.

A measurement composes `amount` and `factory`; it inherits metadata and behavior.
It is a sealed composite instance. Its slots cannot be assigned, it cannot be
extended or instantiated, and wrapping its constructor with `mutable>>` is
refused. `.with-value(number)` makes a new measurement through the original
factory. It never constructs an heir of an existing measurement.

| Message | Implemented behavior |
| --- | --- |
| `family.define(id, symbol, scale)` | Local definition, not registered globally |
| `family.define(id, symbol, scale, prefixable, exact, source)` | Definition with explicit provenance and flags |
| `factory(number)` | Immutable measurement with the same numeric payload |
| `quantity.value()` | Displayed payload; also available as `quantity.amount` |
| `quantity.factory` | Explicit reference to the definition that constructed it |
| `quantity.with-value(number)` | New measurement in that same definition |
| `quantity.compatible-with(other)` | Same kind identifier and all eight dimension exponents |
| `unit.family(kind, dimension)` | Local family inheriting the receiver; copies dimension exponents |
| `dimension(L, M, T, I, Theta, N, J, info)` | Immutable composite of eight integer exponents |
| `dimension.same-as(other)` | Field-by-field comparison of exponents |

`compatible-with` accepts the kind/dimension protocol of a family, definition or
measurement. It checks eligibility; it does not convert or compare amounts.
Composite equality requires the same definition parent, amount and factory.
Equivalent measurements expressed in different definitions are not converted
by `equals`; conversion and numeric comparisons belong to step 6.

## Definition metadata

| Label | Meaning and default |
| --- | --- |
| `id` | Nonempty local identifier, supplied to `define` |
| `symbol` | Case-sensitive display symbol, supplied to `define` |
| `kind` | Semantic family identifier |
| `dimension` | Integral dimension value |
| `scale` | Positive real factor relative to the family's coherent unit |
| `offset` | Zero in this core; affine rules are pending |
| `prefixable` | Eligibility metadata, default `no`; prefix generation is pending |
| `exact` | Definition author's exactness claim, default `yes` |
| `source` | Provenance text, default `"user-defined"` |

Use exact rational factors when the definition is exact. The six-argument form
can mark a measured factor as inexact and name its source. No measurement
uncertainty model or automatic factor verification is implied by these fields.
The catalogue step will add reviewed definitions and their sources.

Nonpositive factors and empty identifiers fail through Graf predicate casts.
Non-numeric payloads, invalid flags, nonintegral dimensions and incomplete
instances fail through normal Graf pattern/instantiation checks. The core does
not depend on testing assertions to report invalid input.

## Dimensions and families

The fields, in constructor order, are:

| Field | Dimension |
| --- | --- |
| `length` | L |
| `mass` | M |
| `duration` | T; fixed durations, not calendar periods |
| `current` | I |
| `temperature` | Theta |
| `amount-of-substance` | N |
| `luminous-intensity` | J |
| `information` | info; an independent information dimension |

| Family | Dimension |
| --- | --- |
| `ratio`, `angle`, `solid-angle` | All exponents zero; three distinct kinds |
| `length` | L |
| `area` | L^2 |
| `volume` | L^3 |
| `mass` | M |
| `duration` | T |
| `current` | I |
| `temperature-point`, `temperature-difference` | Theta; two distinct kinds |
| `amount-of-substance` | N |
| `luminous-intensity` | J |
| `information` | info |
| `velocity` | L*T^-1 |
| `acceleration` | L*T^-2 |
| `frequency`, `radioactivity` | T^-1; two distinct kinds |
| `force` | L*M*T^-2 |
| `pressure` | L^-1*M*T^-2 |
| `energy`, `torque` | L^2*M*T^-2; two distinct kinds |
| `power` | L^2*M*T^-3 |
| `absorbed-dose`, `equivalent-dose` | L^2*T^-2; two distinct kinds |

Temperature and dose families establish distinct types here. Their domain
rules, temperature point/difference arithmetic, weighting models and other
special conversions are still pending. These family declarations are not a
completed catalogue of concrete physical units.

## Local extension

A local family needs a kind and a dimension, with no global registry:

```graf
rate$ = units.unit.family("example-data-rate",
    units.dimension(0, 0, -1, 0, 0, 0, 0, 1));
bits-per-second$ = rate$.define("example-bit-per-second", "bit/s", 1);
bits-per-second$(64).value()
// => 64
```

Use Graf inheritance to add behavior or refine metadata. An explicit
`override>>` replaces inherited metadata so a read does not return both values.
A factory must keep its numeric constructor contract and its metadata immutable;
custom behavior should create results through the definition. Mutating a custom
ancestor falls outside this immutable-definition protocol.

The files in `src/units/core` supply the shared base classes. Public unit files
mount that directory under an internal alias, so importing units directly or
through the library root reaches the same base `unit` and `dimension` classes.
No other legacy component is evaluated by the units examples or tests.

## Validation

Run `graf test tests/units` from the repository root. The suites cover all 25
families, payload preservation, immutable instances, exact factor metadata,
local extension, compatibility, provenance and invalid input. See the
[validation status](validation.md) for the verified counts and remaining work.
