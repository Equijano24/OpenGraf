# Decimal and binary prefixes

`si-prefixes` contains the 24 BIPM prefixes from quetta to quecto.
`binary-prefixes` contains the 10 prefixes from kibi to quebi listed in BIPM
version 4.01 and IEC 80000-13:2025. SI prefixes always mean powers of ten;
binary prefixes mean powers of two. See [reviewed sources](sources.md).

## Use

```graf
// Save as examples/units/catalogue.graf, relative to the repository root.
import(units: graf {path: "../../src/units"});

quectograms$ = units.si-prefixes.quecto(units.grams);
quebibytes$ = units.binary-prefixes.quebi(units.bytes);

(units.meters(units.feet(3)).value(),
 units.liters(units.us-liquid-gallons(1)).value(),
 units.liters(units.imperial-gallons(1)).value(),
 units.bytes(units.kilobytes(1)).value(),
 units.bytes(units.kibibytes(1)).value(),
 units.kilograms(quectograms$(1)).value(),
 units.bits(quebibytes$(1)).value(),
 units.cubic-meters(units.cube(units.centimeters)(1)).value())
// => 0.9144 exactly, 3.785411784 exactly, 4.54609 exactly,
//    1000, 1024, 1/10^33, 10141204801825835211973625643008, 1/1000000
```

A prefix call accepts an eligible **factory** and returns a new factory. It
never prefixes a measurement or mutates its parent. Named catalogue factories
such as `kilometers`, `milligrams` and `kibibytes` use this same protocol.
Their definitions remain inheritable; measurements remain immutable.

| Operation | Result |
| --- | --- |
| `si-prefixes.kilo(meters)` | Length factory, scale 1000, symbol `km` |
| `si-prefixes.milli(grams)` | Mass factory, scale 1/10^6 kg, symbol `mg` |
| `binary-prefixes.kibi(bytes)` | Information factory, scale 8192 bit, symbol `KiB` |
| `binary-prefixes.kibi(bytes-per-second)` | Information-rate factory, 8192 bit/s |
| `square(centimeters)` | Area factory, scale 1/10^4 m², symbol `cm²` |
| `cube(centimeters)` | Volume factory, scale 1/10^6 m³, symbol `cm³` |

The API uses American English names (`meters`, `liters`) and international
scientific symbols. Symbol case matters: `mA` and `MA`, `kB` and `KiB`, differ.
Symbols are metadata; no automatic parsing of ambiguous symbols is introduced.

## Eligibility and powers

Decimal prefixing requires `prefixable: yes`; binary prefixing requires
`binary-prefixable: yes`, kind `information` or `information-rate`, and the
corresponding dimension vector. Both require positive scale, zero offset,
linear arithmetic and an empty `prefix-name`. The returned definition has
both eligibility flags set to `no` and records its prefix name and system.
Double prefixes, affine points, unfilled families and measurements are refused.

The kilogram already contains a prefix. Prefix `grams`, never `kilograms`:
`si-prefixes.milli(grams)` produces milligrams; `si-prefixes.milli(kilograms)`
is refused. Temperature **differences** may be prefixed when eligible; absolute
temperature factories, logarithmic values and gauge factories are ineligible;
see [special-unit rules](special.md).

A prefix on a length applies **before** its power. Use
`square(si-prefixes.centi(meters))` or `square(centimeters)`, and similarly `cube`.
The area and volume factories themselves are not prefixable. Thus this API
refuses `si-prefixes.centi(square-meters)` instead of silently interpreting it
as either 1/100 m² or 1/10000 m². `square` and `cube` accept complete, linear,
positive-scale length definitions with the length dimension vector.

## Prefix data

A prefix is an immutable instance of `prefix`, with `name`, `symbol`, `radix`,
`exponent`, `factor` and `source`. Applying the instance transforms a definition.
The factor is an exact integer or rational; it is not a binary64 approximation.

| Decimal prefix | Symbol | Exponent of 10 |
| --- | --- | --- |
| quetta | Q | 30 |
| ronna | R | 27 |
| yotta | Y | 24 |
| zetta | Z | 21 |
| exa | E | 18 |
| peta | P | 15 |
| tera | T | 12 |
| giga | G | 9 |
| mega | M | 6 |
| kilo | k | 3 |
| hecto | h | 2 |
| deca | da | 1 |
| deci | d | -1 |
| centi | c | -2 |
| milli | m | -3 |
| micro | µ | -6 |
| nano | n | -9 |
| pico | p | -12 |
| femto | f | -15 |
| atto | a | -18 |
| zepto | z | -21 |
| yocto | y | -24 |
| ronto | r | -27 |
| quecto | q | -30 |

| Binary prefix | Symbol | Exponent of 2 |
| --- | --- | --- |
| kibi | Ki | 10 |
| mebi | Mi | 20 |
| gibi | Gi | 30 |
| tebi | Ti | 40 |
| pebi | Pi | 50 |
| exbi | Ei | 60 |
| zebi | Zi | 70 |
| yobi | Yi | 80 |
| robi | Ri | 90 |
| quebi | Qi | 100 |

## Local extension and provenance

`prefix(name, symbol, radix, exponent, source)` constructs a local prefix.
Names and symbols must be nonempty, radix must be 2 or 10, and the exponent
must be an integer. The standard namespaces contain only the listed standard
entries; a locally defined prefix is the application's explicit convention.
No global registration occurs.

Prefixing inherits the original kind, dimensions, methods, `exact` flag,
`reference-edition` and `quantity(number)` construction override. It combines
source provenance and multiplies both scale and absolute `scale-uncertainty`
by the prefix factor. The parent definition remains unchanged.

`square` and `cube` create area/volume factories and propagate factor exactness,
source and edition. For measured length factors they record first-order standard
uncertainty as `2*s*u` or `3*s*s*u`. This metadata describes conversion-factor
uncertainty; OpenGraf does not provide general measurement uncertainty propagation.

## Numeric boundary

Prefix factors, powers of factory scales and coherent conversion multipliers/
divisors use Graf's explicit `exact-product` and `exact-quotient`. Exact rational
inputs remain exact even beyond Int64; a `float64` input retains Graf's usual
floating-point participation and integer normalization. Symbolic operands remain
symbolic. An exact unit factor does not make a user's approximate input exact.

Other arithmetic messages (`plus`, `times`, `over`, etc.) still follow Graf's
ordinary numeric promotion rules. For example, a later generic multiplication
of a large rational can produce `float64`. This does not affect the exact prefix
metadata or the coherent scale conversion path. See [angles](angles.md#precision-boundary)
and Graf's numeric reference.
