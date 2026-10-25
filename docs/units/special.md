# Temperature, logarithmic and contextual units

Step 9 implements these rules in Graf. Public modules are in `src/units`;
shared implementations are in `src/units/core`. The finite
`catalogue.definition` relation now includes **302 named factories**: the
290 entries in the [linear catalogue](catalogue.md) and these 12 definitions.
Context-dependent factories are constructed locally and are not registered globally.

| Factory | Quantity or convention | Mapping |
| --- | --- | --- |
| `kelvins` | Temperature point | K = value |
| `celsius` | Temperature point | K = value + 273.15 |
| `fahrenheit` | Temperature point | K = (value + 459.67) × 5/9 |
| `rankines` | Temperature point | K = value × 5/9 |
| `rankine-differences` | Temperature difference | ΔK = value × 5/9 |
| `power-decibels` | Power-ratio level | value = 10 log10(ratio) |
| `power-bels` | Power-ratio level | value = log10(ratio) |
| `power-nepers` | Power-ratio level | value = ln(ratio)/2 |
| `amplitude-decibels` | Amplitude-ratio level | value = 20 log10(ratio) |
| `amplitude-bels` | Amplitude-ratio level | value = 2 log10(ratio) |
| `amplitude-nepers` | Amplitude-ratio level | value = ln(ratio) |
| `ph` | Hydrogen-ion acidity | value = −log10(activity) |

Temperature factors and offsets are exact. The six logarithmic level factories
name the ratio convention explicitly. Their symbols alone do not choose it.
The logarithmic formulas are exact definitions; evaluations can be approximate.
[Sources](sources.md#special-unit-sources) distinguish definitions from physical models.

## Temperature points and differences

A point accepts a real Graf number and rejects a coherent temperature below
zero kelvin. Zero is included. The same validation applies to `quantity`,
conversion, `quantity-with-value`, arithmetic results and rounding.
A negative Celsius or Fahrenheit coordinate can be valid. These factories model
ordinary absolute temperature, not population-inversion negative-temperature models.

| Expression | Result |
| --- | --- |
| `celsius(fahrenheit(32))` | 0 °C point |
| `fahrenheit(212).minus(celsius(0))` | 180 Fahrenheit differences |
| `fahrenheit(32).plus(kelvin-differences(10))` | 50 °F point |
| `kelvins(0).minus(kelvin-differences(1))` | Failure: below absolute zero |
| `celsius(20).plus(celsius(10))` | Failure: point plus point |
| `celsius(20).times(2)` | Failure: point is not a linear quantity |

Point minus point returns a difference in the left point's paired difference
factory. Point plus/minus difference retains the left point's factory. Difference
plus point is refused; write point plus difference. Comparisons convert points
through kelvins. Points and differences do not convert directly to each other,
and a compound cannot be classified as a point.

`kelvin-differences`, `celsius-differences` and `fahrenheit-differences` remain in
the linear catalogue. Differences support linear arithmetic and eligible
prefixes. Absolute points, including kelvins with offset zero, cannot be prefixed.
`rankines` pairs with `rankine-differences`.

A custom point can use:

```graf
local$ = units.temperature-point.point-definition(
    "local-point", "u", 1, 273.15(0), units.celsius-differences, "local specification");
```

The scale must be positive and equal the paired difference's scale. That factory
must have temperature-difference kind and dimensions, with zero offset and linear
arithmetic. The shorter inherited `definition(id, symbol, scale)` uses offset
zero and constructs a matching local difference factory when needed.
Special families override base methods: use `all(units.quantity?)?` to check
the measurement protocol without requiring the base unit's exact method shape.

## Logarithmic ratios and precision

`power-decibels(20)` is a displayed logarithmic value. It is not a power quantity.
`.linear-ratio(precision)` returns its positive, dimensionless ratio.
`power-decibels.level(100)` constructs the inverse mapping. Ratios must be real
and strictly positive; zero does not create an infinite level. Logarithmic
payloads are real. pH is not restricted to the interval 0–14.

Conversions within one kind use `factory(quantity)`, or
`factory(quantity, precision)`. Power and amplitude conventions are separate
kinds. Direct conversion between them is refused. A physical relationship needs
an explicit model, even when particular level values happen to agree.

All logarithmic APIs default to **15 decimal places**. They delegate to
`common.math.log10`, `ln`, `exp` and Graf's precision-controlled `pow`.
Exact powers can remain exact. For other values, precision applies to the
underlying logarithm/exponential before the coefficient is applied; it is not
a promise of that many final significant digits. Conversion can involve two
rounded evaluations. Use explicit tolerance when checking a nonexact round trip.
A rounded inverse power that becomes zero is refused, not silently accepted as
a valid positive ratio. The [ordinary numeric promotion boundary](angles.md#precision-boundary)
still applies to later generic arithmetic.

Generic plus/minus, multiplication, division, powers and roots on logarithmic
quantities are refused. To combine signals, work on the appropriate linear
quantities using an explicit physical model. `.rounded(places)` explicitly rounds
the displayed level and retains its factory. Comparison within a kind compares
level coordinates; for pH, increasing the coordinate decreases activity.

`logarithmic-unit.logarithmic-definition(id, symbol, kind, logarithm, coefficient, source)`
constructs a local factory. `logarithm` is `"decimal"` or `"natural"` and the
coefficient must be a nonzero real. The `scale` field is not a substitute for
this nonlinear mapping. For unreferenced levels, `.coherent-value()` is the ratio.

## Referenced logarithmic levels

`logarithmic-reference(referenceQuantity, conventionFactory)` returns an
inheritable unit factory that retains both inputs. The reference must be a
positive linear quantity; the convention must be a power- or amplitude-level
factory. No reference pressure, impedance or reference power is guessed.

```graf
milliwatts$ = units.si-prefixes.milli(units.watts);
dbm$ = units.logarithmic-reference(milliwatts$(1), units.power-decibels);
dbw$ = units.logarithmic-reference(units.watts(1), units.power-decibels);
level$ = dbm$.level(units.watts(1));       // 30, with its 1 mW reference retained
dbw$(level$).value()                     // 0, referred to 1 W
units.watts(level$.linear-quantity()).value()  // 1 W
```

`dbm$(30)` also constructs a referenced measurement. Numeric `quantity` follows
the normal unit construction protocol. `factory(linearQuantity)` and
`.level(linearQuantity, precision)` take a physical quantity; the latter exposes
precision. `factory(referencedLevel, precision)` changes references and/or the
logarithmic convention. A reference and its value are immutable metadata on every
result, including rounded results.

Referenced power/amplitude kinds are distinct from unreferenced ratios.
Compatibility also checks the reference's physical kind and dimensions. Thus
level comparisons account for differing reference values, and a voltage level
cannot convert to a power level. `.linear-quantity(precision)` returns a physical
quantity in the reference's factory. Ordinary linear factories refuse direct
conversion from a logarithmic quantity.

Referenced levels are dimensionless; their reference retains the underlying
physical dimensions. Their internal coherent conversion coordinate is the
physical SI value, also available as `.physical-value(precision)`. This mapping
supports reference changes and comparisons, and is not permission to perform
linear dimensional arithmetic on a level.

`contextual.referenced-level(value, reference, convention, precision)` constructs
the same referenced measurement. `contextual.referenced-quantity(level, reference,
precision)` checks that a retained reference agrees with the supplied reference.
For an unreferenced ratio-level it explicitly applies the supplied reference.

## Amplitude-to-power models

`power-law(exponent, source)` is an immutable model for positive ratios:
`powerRatio = amplitudeRatio^exponent`. Its inverse uses the reciprocal exponent.
The exponent must be positive. Selecting exponent 2 is an explicit assumption;
it does not establish equal impedances for an application.

`contextual.power-level(amplitudeLevel, model, targetPowerFactory, precision)` and
`contextual.amplitude-level(powerLevel, model, targetAmplitudeFactory, precision)`
use `model.power-ratio(ratio, precision)` or `model.amplitude-ratio(ratio, precision)`.
Applications can supply their own model box for different impedances or other
physical relationships. Invalid/missing responses propagate as Graf failures.

## Gauge pressure

`gauge-pressure(referencePressure, displayPressureFactory)` constructs a local
factory. Both inputs must have pressure kind and dimensions and support linear
arithmetic. The reference is an explicit nonnegative absolute pressure.

A numeric call stores a gauge coordinate; `.coherent-value()` is
`gaugeCoordinate × scale + referencePressure`, in pascals. Negative gauge values
are allowed while the resulting absolute pressure remains nonnegative.
`.absolute-pressure(targetFactory)` returns a linear pressure quantity; its
default target is `pascals`. `factory(absolutePressure)` performs the inverse.
Conversion between gauge factories changes the reference explicitly and comparison
uses absolute pressure. Direct `pascals(gaugeQuantity)` is refused; use
`.absolute-pressure()`.

Gauge values retain the reference and their factory. Generic arithmetic and
prefixing are refused; supply the desired linear display factory when constructing
the gauge factory. No ambient atmospheric pressure is read.

## Activity and pH models

`ph.level(activity, precision)` takes dimensionless hydrogen-ion activity, never
a dimensionful concentration. The IUPAC definition uses a molality standard.
`activity-model(standard, coefficient, source)` implements the explicitly selected
model `activity = coefficient × value/standard`. Standard and value must have
the same kind and dimensions: molality or amount concentration. They are positive,
as is the coefficient. Molality and molarity do not convert implicitly.

`contextual.acidity(value, model, precision)` calls `model.activity(value)`, then
constructs `ph`. A concentration-based model is an explicit approximation or
application convention, not an automatic implementation of the molality definition.
The caller supplies the standard state, coefficient, provenance and any dependence
on temperature, composition or density. Custom model boxes can implement those
dependencies. This API does not calculate single-ion activity coefficients.

## Chemical-equivalent hardness

`equivalent-basis(name, molarMass, positiveIntegerCharge, source)` stores an
explicit equivalent basis, with equivalent mass `molarMass/charge`. Molar mass
must have the correct kind/dimensions and be positive. No atomic-weight or
valence table is selected automatically.

`basis.definition(id, symbol, scale)` creates a hardness unit with that basis.
Scale is relative to kg/m³ **as that basis**. A scale of `0.001(0)` corresponds
to mg/L. The basis remains on every measurement. Direct conversions or addition
across different bases are refused, even with equal dimensions.

`targetBasis.concentration(massConcentration, sourceBasis)` applies:

`target = source × targetEquivalentMass / sourceEquivalentMass`.

`targetBasis.concentration(hardnessQuantity)` reads the retained source basis.
The result is expressed in kg/m³ as the target basis and can be converted to a
factory created by that basis. Supplying a conflicting source basis is refused.
A plain mass concentration does not identify its chemical species. Hardness is
nonnegative. Same-basis linear arithmetic retains the factory and basis.
These definitions conservatively carry `exact: no`; a rational nominal molar
mass is not proof of physical exactness. General uncertainty propagation and a
complete speciation model are outside this API.

## Radiation weighting

`radiation-weighting(factor, source)` is an explicit positive, single-component
weighting model. `contextual.equivalent-dose(absorbedDose, model)` calls
`model.radiation-weight(absorbedDose)` and returns `sieverts` with value
`absorbed grays × factor`. Kind, dimensions and nonnegative absorbed dose are
checked. No direct gray-to-sievert factor is installed in the unit catalogue.

A custom model can inspect the supplied absorbed quantity. The application must
provide the radiation type, energy and tissue context as needed. This single
component API does not aggregate radiation fields, compute effective dose or
select clinical/protection recommendations.

## Executable example and tests

Run `graf run examples/units/special.graf` from the repository root. The example
below is the same source. The three special suites and the per-factory catalogue
checks run with `graf test tests/units`. Assertions collect actual responses so
an empty stream cannot pass a value check. Sequence integration checks use the
current `count`, `every`, `last` and `single` deferrevals.

```graf
import(units: graf {path: "../../src/units"});

milliwatts$ = units.si-prefixes.milli(units.watts);
dbm$ = units.logarithmic-reference(milliwatts$(1), units.power-decibels);
dbw$ = units.logarithmic-reference(units.watts(1), units.power-decibels);
level$ = dbm$.level(units.watts(1));
gauge$ = units.gauge-pressure(units.pascals(101325), units.bars);
activity$ = units.activity-model(units.moles-per-kilogram(1), 1, "explicit ideal molality model");
weighting$ = units.radiation-weighting(20, "single-component demonstration model");
// Synthetic molar masses illustrate the equation, not a physical constants table.
calcium$ = units.equivalent-basis("test-Ca", units.grams-per-mole(40), 2, "synthetic example");
carbonate$ = units.equivalent-basis("test-CaCO3", units.grams-per-mole(100), 2, "synthetic example");
hardness$ = carbonate$.definition("mg-per-liter-as-test-CaCO3", "mg/L as test-CaCO3", 0.001(0));

(units.kelvins(units.celsius(0)).value(),
 units.fahrenheit(212).minus(units.celsius(0)).value(),
 units.fahrenheit(32).plus(units.kelvin-differences(10)).value(),
 units.power-decibels(20).linear-ratio(),
 units.ph.level(0.0000001(0)).value(),
 level$.value(), dbw$(level$).value(), units.watts(level$.linear-quantity()).value(),
 gauge$(1).absolute-pressure().value(),
 units.contextual.acidity(units.moles-per-kilogram(0.0000001(0)), activity$).value(),
 units.contextual.equivalent-dose(units.grays(0.001(0)), weighting$).value(),
 hardness$(carbonate$.concentration(units.milligrams-per-liter(40), calcium$)).value())
// => 273.15, 180, 50, 100, 7, 30, 0, 1, 201325, 7, 0.02, 100
```
