# Validation and implementation status

Steps 5–9 implement the [core](core.md), [conversion/arithmetic](operations.md),
[angles](angles.md), [catalogue](catalogue.md), [prefixes](prefixes.md) and
[special units](special.md):
87 original families, 302 named factories, all 24 SI and 10 binary prefixes, immutable
measurements and explicit local extension. Absolute temperatures, logarithmic
units and reference/model conversions are implemented in step 9. The [plan](../plan-de-trabajo.md)
records nine completed steps and step 10 next.

## Verified checkpoint

| Check | Result |
| --- | --- |
| `graf test tests/units` | 489 passed, 0 failed, 0 load errors; exit 0 |
| `graf test tests/testing` | 11 auxiliary gunit tests passed; exit 0 |
| Complete Graf .NET suite on `develop` | 2076 passed, 0 failed, 2 existing printed-form skips |
| Graf solution build | Successful; symbolic operands and explicit exact-factor arithmetic included |
| `graf run examples/units/core.graf` | Original 1/3, replacement 2, symbol m, length exponent 1, compatible yes |
| `graf run examples/units/operations.graf` | 23/10, 200, 25/18, 5, 3, yes |
| `graf run examples/units/angles.graf` | Constructor, symbolic pi/6, 180, mixed sum, sine, exact 1/2, inverse 30 and atan2 135 |
| `graf run examples/units/catalogue.graf` | Exact international foot, U.S./Imperial gallons, decimal/binary byte, quecto gram, quebi byte and cubic centimeter anchors |
| `python3 tools/units_catalogue.py --check` | Generated sources/reference/integration tests match reviewed data; no stale generated definitions |
| `graf run examples/units/special.graf` | Temperature, logarithmic/reference, gauge, activity, hardness and radiation anchors |
| Host BigComplex payload check | Identity retained through construction, coherent mapping, conversion and replacement |
| `mkdocs build --strict` | Successful |

The unit suites cover each family with an independent expected dimension
vector, numeric payload kinds, explicit factory references, composite equality,
immutable slots, refusal to extend or reopen a measurement, invalid payloads,
exact/inexact metadata, inherited overrides, local custom families, compatibility
and imports through aliases or the library root. A family copies mutable
input dimensions rather than retaining changeable exponent fields.

The 32 operation regressions check independent conversion anchors, round trips,
left-factory retention, custom `quantity` validation, scalar and compound arithmetic,
all eight exponent operations, exact and precision-controlled roots, explicit
classification, numeric failures and incompatible kinds. Actual values are
collected in tuples so empty streams fail assertions instead of skipping them.

The 33 angular checks cover independent degree/radian anchors, mixed arithmetic,
kind boundaries, metadata overrides, aliases/root imports, six circular functions,
seven inverses, principal ranges, axes/quadrants, explicit/default precision,
30-digit rational reference values, periodic inputs, domains, immutability and
custom angular factories including overridden construction. Tuples check response
cardinality. The 23 new Graf regression cases cover symbolic operands on either
side, exact cancellation and all comparison messages. Exact rational reference
literals use `a.b(0)` to avoid invoking Graf's large-component promotion when
constructing an expected value.

The precision boundary in [angles](angles.md#precision-boundary) is explicit:
`common.math` results retain their backend type, but subsequent generic numeric
arithmetic still follows Graf's existing rational-to-float promotion rule.

Step 8 adds 327 checks: one integration test for each of the 290 catalogue
factories, 17 independent physical-anchor groups, five defining-equation groups,
12 prefix behavior groups, two explicit reference tables covering every prefix,
and a shared-import check. Generated integration cases check construction,
factory identity, family/dimension shape, coherent mapping and round trips;
hand-maintained anchors/equations catch a wrong factor or vector that a generated
round trip alone cannot detect. Prefix tests cover extreme exact factors,
byte/bit scaling, powers, kilogram rules, double-prefix refusal, affine and
non-information refusal, custom construction, immutable data, source/uncertainty
metadata and all 34 standard factors. The native exact-factor API has 11
additional regression cases.

`tests/units` is the replacement test target. The old `tests/units-test.graf`,
other tests and other library sections still target the obsolete API; they are
not evidence for or against the modern unit core. Importing the library root
in an import regression reads only the unit labels it uses.

## Step 9 validation

The 52 additional checks cover 12 special-factory construction/immutability cases,
nine temperature groups, 12 logarithmic groups and 19 contextual/model groups.
They check fixed temperature anchors and boundaries, left difference factories,
real domains, nonexact log precision/tolerance, all six power/amplitude conventions,
pH activity outside 0–14, reference retention and changes, gauge pressure,
explicit activity standards, basis-preserving hardness and custom radiation models.
Negative tests reject missing models, wrong kinds/dimensions, conflicting references,
nonpositive ratios/standards/weights and mutation. Assertions check response
cardinality. Current sequence deferrevals are exercised on unit results.

Graf was synchronized to `develop` commit `7da35b5fba689dee011ea5e41667d8b6dbd14359`
before implementation. Its full suite has **2076 passed, zero failed and two
existing omissions**, including the newly added deferrevals and expression-map
cases. Step 9 requires no engine change. The host BigComplex check listed above
is the retained step 8 result, not a new host-backend test in this step.

## Graf prerequisites

Use `T-and-Q/Graf` on `develop`. The completed testing foundation ensures:

1. Each gunit setup/test is invoked inside Graf `try`.
2. .NET exceptions pass through `TryCatch`, then catch dispatch receives a
   level-zero exception value.
3. Matching handlers return their responses; unmatched failures retain their level.
4. Reading a stored caught exception does not raise it again.
5. Handler-body failures propagate independently of dispatch misses.
6. Discovery selects nearest/latest declarations and skips nested data, method
   bodies and imported environments.
7. `graf test` supports explicit targets, filters, diagnostics and exit codes.
8. `assert-fails` evaluates quoted code in the caller context, including local
   variables and receiver; side effects execute once. A successful local
   expression cannot pass by losing its binding and raising an unrelated error.

Graf has 13 gunit execution/assertion regressions, 13 discovery regressions and
9 command regressions. OpenGraf's auxiliary suites add 11 Graf-language checks.
The CLI's pass/fail/load/no-match/cancellation codes were verified in step 4.

## Remaining validation matrix

| Concern | Implemented now | Still required |
| --- | --- | --- |
| Construction | Core and special constructors, payload/domain validation, retained references and immutable values | Further application-specific factories |
| Dimensions and kinds | Eight integral fields; 87 family vectors; products, quotients, powers and integral roots | Application-specific extensions |
| Conversion | Linear, affine, logarithmic and reference mappings; independent model anchors; kind/dimension checks | Further application models |
| Arithmetic | Linear operations, special point/difference rules, reference-aware comparisons and rounding | Further application-specific rules |
| Angles | Radians/degrees, symbolic conversion, circular/inverse methods, precision, domains and extension | Further catalogue angles; native large-rational promotion decision |
| Temperature | Four point scales, four difference scales, exact offsets, absolute-zero boundaries and point/difference operations | Population-inversion models are outside the ordinary point API |
| Prefixes | All SI/binary factors, powers, double-prefix refusal and special-unit exclusions | Application-specific eligibility |
| Special cases | Logarithmic domains, retained references, gauge pressure, pH activity, equivalent-basis hardness and explicit radiation weighting | Full speciation, uncertainty propagation and radiation-field aggregation are outside these APIs |
| Extensibility | Local factories, overridden construction, custom ratio/activity/radiation models and explicit equivalent bases | More application-specific models |
| Migration | Old unit implementation removed; new core reference and executable example | Full old-API migration guidance and replacement of old catalogue examples/tests |
| Documentation | Technical Markdown, 302-factory inventory, special/prefix references, reviewed sources and site build | Full migration guidance and final PDF verification |

Round trips alone cannot detect a shared wrong factor. The catalogue tests
include independent anchors such as the exact international inch, liter
and separately named U.S./Imperial gallons. Measured constants require documented
reference editions, uncertainty information and tolerance-based tests.

## Unit source migration

| Legacy file | Replacement |
| --- | --- |
| `unit.graf` | Public entry point to the new core class |
| `angle.graf` | Shared angular family with circular/inverse methods; public `radians.graf` and `degrees.graf` definitions |
| `distance.graf` | `length.graf` |
| `weight.graf` | `mass.graf`; force is a distinct family |
| `information-unit.graf` | `information.graf` |
| `temperature.graf` | `temperature-point.graf` and `temperature-difference.graf` |

These names deliberately replace the obsolete unit API. The current checkpoint
provides a stable foundation rather than claiming that the old catalogue now
works with the modern interpreter.
