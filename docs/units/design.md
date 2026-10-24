# Units: design contract

Status: specification checkpoint. The replacement API is not implemented yet;
`src/units` still contains the legacy API.

## Object model

`unit` is the common base. Quantity families (`angle`, `length`, `area`, `volume`,
`mass`, and others) inherit from it. Concrete unit definitions inherit a family;
measurements are immutable instances composing a Graf `number` payload with a
reference to their defining factory. Numbers are neither subclassed nor mutated.
Decoration remains available for optional behavior such as formatting or tracing.

Factories accept a number in their own unit, or convert another compatible
quantity. `radians(20)` means twenty radians. `radians(degrees(30))` converts thirty
degrees to radians. `.value()` reads the displayed payload. Mixed addition and
subtraction preserve the left operand's factory.

## Dimensions and semantic kinds

Dimensions contain integer exponents for the seven SI base dimensions and
information. Multiplication/division combine dimensions; integer powers multiply
them. A root must leave integral exponents. A compound result is explicitly
classified by a named factory rather than inferred through a global registry.

Kinds retain distinctions that dimensions alone erase: angle versus ratio,
energy versus torque, frequency versus radioactivity, and absorbed versus
equivalent radiation dose. Direct conversions between those kinds are refused.
An application can classify a force-times-length compound as work or torque.

## Numeric and conversion protocol

Linear/affine conversions use `coherent = amount * scale + offset` and the inverse
mapping in the target factory. Exact decimal factors use rational numbers;
angular factors retain symbolic pi. Arithmetic delegates to the supplied numeric
backend, including its supported operations and explicit precision controls.

Angles implement `.sin()`, `.cos()`, and `.tan()` with a default precision and
explicit-precision overloads, delegating to `common.math` in radians. Inverse
trigonometric helpers return angle quantities. Logarithms operate on explicit
dimensionless ratios, not dimensionful values.

## Special quantity rules

- Temperature points and temperature differences are separate kinds. Point minus
  point produces a difference; point plus/minus difference produces a point.
  Point plus point and multiplication of affine points are refused. Absolute
  temperatures below zero kelvin are rejected.
- Decimal SI prefixes and binary information prefixes are separate APIs. A
  prefixed definition cannot be prefixed again. Prefix grams for kilogram units.
- Power and amplitude decibels use explicit linear-ratio conversions. Their
  physical relationship requires a model. pH uses activity, not automatic molarity.
- Gauge pressure requires an explicit reference pressure. Chemical hardness needs
  a specified equivalent basis. Gray-to-sievert conversion needs a weighting model.
- Fixed durations are distinct from calendar months and years.

## Extensibility

Definitions carry `id`, `symbol`, `kind`, `dimension`, `scale`, `offset`, prefix
eligibility, and exactness/source metadata. Measurements add `amount` and `factory`.
Users extend families through inheritance or a definition factory such as
`length.define("furlong", "fur", exactFactor)`. New dimensions/kinds compose the
same protocol; no mutable global registration is required.

## Validation and documentation

Every catalogue unit needs constructor and conversion tests through
`common.testing.gunit`. Independent physical anchors complement round trips;
round trips alone cannot detect wrong factors. Cover incompatible kinds,
compound arithmetic, symbolic angles, temperature boundaries, prefix rules,
logarithmic domains, and contextual conversions.

Gunit must invoke every setup and test through Graf's `try`. `TryCatch` converts
.NET exceptions to Graf failure results. Catch dispatch receives the exception
value with `ErrorLevel = 0`; a matching catch returns its body results and an
unmatched failure retains its original positive level. Stored caught exceptions
remain inspectable data. Test discovery must traverse only relevant lineage,
not method bodies, nested compositions, or imported environments.

Documentation is a technical reference with getting-started instructions, API
contracts, conversion conventions, a catalogue, extension guidance, and testing.
Markdown sources should support a documentation website and PDF rendering.
Gieck's handbook is a coverage reference, not the source of Open Graf's structure
or presentation. Check definitions against BIPM, NIST, and CODATA; identify
historical conventions, errors, and measured rather than exact constants.

## Public API contract

These examples specify the replacement API; they are not executable examples of
this checkpoint's legacy implementation.

```graf
meters(2).plus(centimeters(30)).value()     // 23/10, in meters
centimeters(meters(2)).value()             // 200
radians(degrees(180)).value()              // symbolic pi
radians(2.5).sin()                         // delegates to common.math
radians(2.5).sin(30)                       // explicit numeric precision
kilometers(10).over(hours(2))              // compound velocity
meters-per-second(kilometers(10).over(hours(2)))
```

An unadorned number passed to a factory is always measured in that factory's
unit. A bare scalar passed to addition/subtraction is refused; it has no unit.
Scalar multiplication/division retain the factory. Division by zero and numeric
domain failures use the numeric backend's Graf exceptions. No implicit rounding
or conversion to binary floating point occurs.

| Operation | Result contract |
| --- | --- |
| `factory(number)` | New immutable quantity in that unit |
| `factory(quantity)` | Convert compatible kind, or classify a compound with matching dimensions |
| `quantity.value()` | Original/display payload, still a Graf number |
| `quantity.coherent()` | Payload in the family's coherent unit |
| `quantity.plus(other)` / `.minus(other)` | Compatible kind, left factory retained |
| `quantity.times(number)` / `.over(number)` | Left factory retained |
| `quantity.times(quantity)` / `.over(quantity)` | Coherent compound and composed dimensions |
| `quantity.pow(integer)` | Compound with multiplied dimension exponents |
| `quantity.rounded(places)` | Explicit rounding of displayed payload |
| `angle.sin(precision)` / `.cos(precision)` / `.tan(precision)` | Dimensionless Graf number |
| `family.define(id, symbol, scale)` | Local inheritable factory; no registration side effects |

Factories and quantities share inheritance for method reuse, but a quantity's
`factory` reference is explicit. A result must be constructed through that
factory rather than by inheriting from an already measured instance. Unit
metadata is immutable and overridden explicitly so parent metadata does not
appear as extra answers.

## Representation and dispatch

A dimension value has fields for length, mass, duration, current, temperature,
amount of substance, luminous intensity, and information. Each field is an
integer exponent. An angle has zero exponents and a distinct kind. Dimensions
compare field by field; semantic kinds compare stable local identifiers.

A definition contains conversion metadata and methods, not a displayed amount.
Its numeric constructor creates an instance carrying `amount` and `factory`.
Its quantity constructor checks kind and dimensions, converts through coherent
values, then invokes the target numeric constructor. A compound has coherent
scale one, offset zero, and kind `compound`. Its dimensions are composed from the
operands and can be explicitly classified by a named factory.

This uses inheritance for families and factory extension, instantiation for
measurements, and composition for numeric payloads and dimensional metadata.
Decorating the numeric object would make conversions and arithmetic depend on
decoration order. Subclassing every numeric backend would duplicate numeric
behavior. Neither is part of the unit core.

Temperature points override addition/subtraction rules and reject compound
arithmetic. Logarithmic factories expose explicit ratio conversion rather than
pretending that their scale is a linear multiplier. Contextual conversions take
a reference or model as an argument and never consult hidden global state.

## Prefixes and naming

The catalogue uses unambiguous English factory names and scientific symbols as
metadata. Symbols are case sensitive. Do not resolve ambiguous `ton`, `gallon`,
`calorie`, or `year` names without naming their convention. Preserve existing
Spanish/English documentation independently of code names.

SI prefixes are decimal powers from quetta to quecto. Information uses separate
decimal and binary prefix factories. A prefix multiplies the unit's scale, keeps
the family/kind, and adds provenance. Prefixing an affine point or an already
prefixed definition is refused. Area and volume prefixes apply before the power:
a square centimeter is `(1/100)^2` square meters.

## Catalogue coverage plan

| Group | Families and conventions to cover |
| --- | --- |
| Geometry | Angle, solid angle, length, area, volume; metric, international foot/inch, nautical mile, liter; U.S. and Imperial volumes explicitly distinguished |
| Motion | Fixed duration, velocity, acceleration, angular velocity, frequency; calendar periods handled separately |
| Mechanics | Mass, force, pressure, energy, torque, power, momentum, density, specific volume, dynamic and kinematic viscosity |
| Thermal | Temperature points/differences, heat capacity, specific heat, thermal conductivity and expansion, heat flux |
| Electrical | Current, charge, potential, resistance/conductance, capacitance, inductance, magnetic flux/density/field, resistivity and conductivity |
| Light | Luminous intensity, luminous flux, illuminance and luminance; optical quantities retain their photometric/radiometric distinction |
| Chemistry | Amount, molar mass, concentration, activity-based pH; hardness names its equivalent basis |
| Radiation | Radioactivity, absorbed dose, equivalent dose and exposure; model-dependent weighting remains explicit |
| Information | Bits, bytes, decimal/binary multiples and transfer rate |
| Ratios | Dimensionless ratios, percentages, power/amplitude decibels with explicit domains |

A catalogue entry records definition source, convention, exactness, and any
validity restrictions. A measured constant includes its reference edition and
uncertainty information. Historical gravitational units name standard gravity
rather than using an unspecified local gravitational field.
