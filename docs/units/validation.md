# Validation and implementation status

Step 5 replaces the legacy unit sources with the [new core](core.md): `unit`,
eight integral dimension exponents, 25 families, local definitions and immutable
measurements. Conversion, arithmetic, the reviewed catalogue and special-unit
rules are not implemented yet. The [11-step plan](../plan-de-trabajo.md) records
five completed steps and step 6 next.

## Verified checkpoint

| Check | Result |
| --- | --- |
| `graf test tests/units` | 45 passed, 0 failed, 0 load errors; exit 0 |
| `graf test tests/testing` | 11 auxiliary gunit tests passed; exit 0 |
| Complete Graf .NET suite on `develop` | 1955 passed, 0 failed, 2 existing printed-form skips |
| Graf solution build | Successful; no engine changes required for this step |
| `graf run examples/units/core.graf` | Original 1/3, replacement 2, symbol m, length exponent 1, compatible yes |
| `mkdocs build --strict` | Successful |

The unit suites cover each family with an independent expected dimension
vector, numeric payload kinds, explicit factory references, composite equality,
immutable slots, refusal to extend or reopen a measurement, invalid payloads,
exact/inexact metadata, inherited overrides, local custom families, compatibility
and imports through aliases or the library root. A family copies mutable
input dimensions rather than retaining changeable exponent fields.

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

Graf has 11 gunit execution/assertion regressions, 13 discovery regressions and
9 command regressions. OpenGraf's auxiliary suites add 11 Graf-language checks.
The CLI's pass/fail/load/no-match/cancellation codes were verified in step 4.

## Remaining validation matrix

| Concern | Implemented now | Still required |
| --- | --- | --- |
| Construction | Core numeric constructor, payload preservation, family lineage, immutable instance behavior | Per-catalogue-factory construction |
| Dimensions and kinds | Eight integral fields; 25 family vectors; incompatible semantic kinds | Composed exponents, powers and roots |
| Conversion | Compatibility check and factor metadata | Independent physical anchors, round trips, incompatible conversion failures |
| Arithmetic | Replacement payload through the original factory | Mixed addition, scalar operations, compounds, comparisons |
| Angles | Distinct angle family; symbolic pi accepted as payload | Trig functions, symbolic conversions and precision overloads |
| Temperature | Distinct point and difference kinds | Absolute-zero boundary, point/delta arithmetic, affine restrictions |
| Prefixes | Eligibility metadata | SI/binary exponents, byte/bit factors, square/cube scaling, no double prefix |
| Special cases | Distinct dose and radioactivity kinds | Logarithmic domains, pH activity, explicit reference/model conversions |
| Extensibility | Local factories/families, provenance, inheritance and metadata overrides | Conversion and arithmetic with user definitions |
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
| `angle.graf` | Angle family; concrete angular definitions and methods follow later |
| `distance.graf` | `length.graf` |
| `weight.graf` | `mass.graf`; force is a distinct family |
| `information-unit.graf` | `information.graf` |
| `temperature.graf` | `temperature-point.graf` and `temperature-difference.graf` |

These names deliberately replace the obsolete unit API. The current checkpoint
provides a stable foundation rather than claiming that the old catalogue now
works with the modern interpreter.
