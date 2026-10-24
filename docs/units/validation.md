# Validation and implementation status

This checkpoint records the replacement design. It does not claim completion or
validation of the new units catalogue. Existing unit sources and tests use the
legacy API.

## Prerequisites in Graf

Use `T-and-Q/Graf` on `develop`. Exception handling must obey these rules:

1. Each gunit setup/test is invoked inside Graf `try`.
2. .NET exceptions are converted by `TryCatch`, then offered to catch patterns
   as level-zero values.
3. A handler returns all its responses; an unmatched failure retains its level.
4. A caught exception can be stored in a failed-test report without being raised
   again merely by reading that report.
5. Handler-body failures propagate independently of dispatch misses.

The exception and label-modifier foundation has focused regression coverage in
Graf. The gunit runner now guards each method and supports deferred failure assertions.
Discovery now respects nearest/latest declarations and excludes nested data,
method bodies and imported environments; the `graf test` command now provides targeted execution and status codes.

## Work remaining before release

- [x] Verify per-test setup execution, guarded test invocation and continuing after failures.
      Suites reset mutable state through setup methods; the runner does not clone them.
- [x] Restrict discovery to the target's inheritance/instantiation lineage; never discover tests in
      nested data, method bodies or imported environments.
- [x] Deduplicate labels and preserve nearest/latest declaration selection, including unmarked replacements.
- [x] Verify lazy `assert-fails`, including class-filtered assertions and empty
      or multiple response streams.
- [x] Provide `graf test` for files/directories, filters, useful diagnostics and
      process exit codes for pass, failure and load error.
- [ ] Implement the numeric/conversion core and independent extension examples.
- [ ] Add the reviewed catalogue and its per-factory tests.
- [ ] Replace or explicitly migrate legacy unit entry points.
- [ ] Publish executable usage examples and the complete API reference.

## Unit regression matrix

| Concern | Required checks |
| --- | --- |
| Construction | Every factory accepts supported Graf numeric payloads and preserves numeric behavior |
| Conversion | Independent physical anchor and round trip for every unit; incompatible families/kinds refused |
| Arithmetic | Mixed addition retains left factory; scalar operations retain unit; compounds compose exponents |
| Angles | Exact special angles, symbolic pi conversions, precision overloads, undefined tangent/domain errors |
| Temperature | Freezing/boiling anchors, absolute-zero boundary, point/delta operations, affine multiplication refusal |
| Prefixes | All supported SI/binary exponents, byte/bit factors, square/cube scaling, no double prefix |
| Special cases | Decibel power/amplitude ratio domains, pH activity, explicit gauge reference and hardness basis |
| Extensibility | Local custom factory converts and participates in arithmetic without global registration |
| Errors | Unit failures become failed gunit rows; a failed setup prevents its test and the runner continues |

A round trip can pass when both directions share a wrong factor. Include
independent anchors such as the exact international inch of 0.0254 meters,
a liter of 0.001 cubic meters, and distinct U.S./Imperial gallon definitions.
Measured constants need tolerance-based tests with documented reference values.

## Specification checkpoint checks

The documentation builds successfully with MkDocs 1.6.1 in strict mode.
Graf's exception and gunit checkpoint passed its complete .NET test
suite: 1955 passed, 0 failed, 2 existing printed-form skips. These are Graf
engine results, not results for a replacement Open Graf units implementation.

The auxiliary `.graf` files now return suites for `graf test`. Their execution
and discovery cases total 11 tests. The documentation example defines 2 tests.
Runner, assertions and discovery are complete. The targeted test CLI is available; the units
implementation remains pending. The replacement units tests must be targeted explicitly
under `tests/units`; other legacy OpenGraf sections are not compatible test targets.

The discovery smoke suite defines 6 tests; Graf includes 13
discovery regressions alongside the 11 execution/assertion regressions.

The actual `graf test tests/testing` command passes all 11 auxiliary tests and
exits 0. Exit codes 1 (failed test), 2 (load/target/no matches) and 130
(cancellation) were also verified. Replacement units tests remain pending.
