# Validation and implementation status

Steps 5–7 replace the legacy units with the [core](core.md),
[conversion/arithmetic](operations.md) and [angles/trigonometry](angles.md):
25 families, local definitions, immutable measurements, compound dimensions,
powers, roots, comparisons, `radians`, `degrees` and precision-controlled circular/
inverse functions. The reviewed catalogue and special-unit rules remain later
steps. The [11-step plan](../plan-de-trabajo.md) records seven completed steps
and step 8 next.

## Verified checkpoint

| Check | Result |
| --- | --- |
| `graf test tests/units` | 110 passed, 0 failed, 0 load errors; exit 0 |
| `graf test tests/testing` | 11 auxiliary gunit tests passed; exit 0 |
| Complete Graf .NET suite on `develop` | 1980 passed, 0 failed, 2 existing printed-form skips |
| Graf solution build | Successful; symbolic operand arithmetic/comparison fix included |
| `graf run examples/units/core.graf` | Original 1/3, replacement 2, symbol m, length exponent 1, compatible yes |
| `graf run examples/units/operations.graf` | 23/10, 200, 25/18, 5, 3, yes |
| `graf run examples/units/angles.graf` | Constructor, symbolic pi/6, 180, mixed sum, sine, exact 1/2, inverse 30 and atan2 135 |
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

`tests/units` is the replacement test target. The old `tests/units-test.graf`,
other tests and other library sections still target the obsolete API; they are
not evidence for or against the modern unit core. Importing the library root
in an import regression reads only the unit labels it uses.

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
| Construction | Core numeric constructor, payload preservation, family lineage, immutable instance behavior | Per-catalogue-factory construction |
| Dimensions and kinds | Eight integral fields; 25 family vectors; products, quotients, powers and integral roots | Further catalogue families |
| Conversion | Coherent/affine mappings, anchors, round trips, kind/dimension checks, compound classification | Per-catalogue-factory anchors |
| Arithmetic | Mixed addition/subtraction, scalars, compounds, powers, roots, comparisons and rounding | Special-unit operations |
| Angles | Radians/degrees, symbolic conversion, circular/inverse methods, precision, domains and extension | Further catalogue angles; native large-rational promotion decision |
| Temperature | Distinct kinds; generic arithmetic on points/offset values refused | Absolute-zero boundary and specialized point/delta arithmetic |
| Prefixes | Eligibility metadata | SI/binary exponents, byte/bit factors, square/cube scaling, no double prefix |
| Special cases | Distinct dose and radioactivity kinds | Logarithmic domains, pH activity, explicit reference/model conversions |
| Extensibility | Local factories/families, conversion/arithmetic, overridden `quantity`, provenance and metadata overrides | Prefix/model-specific extensions |
| Migration | Old unit implementation removed; new core reference and executable example | Full old-API migration guidance and replacement of old catalogue examples/tests |
| Documentation | Technical Markdown, API tables, site build | Complete catalogue, reviewed sources and final PDF verification |

Round trips alone cannot detect a shared wrong factor. Later catalogue tests
must include independent anchors such as the exact international inch, liter
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
