# Testing with gunit

Open Graf uses `common.testing.gunit` from the updated `Graf/develop` interpreter.
The replacement units have 506 targeted tests covering all 302 named factories,
the core, conversion/arithmetic, dimensions, local extensions and special rules.
The [migration guide](units/migration.md) accounts for all 31 historical factories
and the four original unit test cases.

## Command

```sh
graf test tests/testing
graf test tests/testing/gunit-smoke.graf --filter class-filter
```

The auxiliary directory contains 11 cases: 5 execution/assertion cases and 6
discovery cases. The filtered command selects one. Results are plain `PASS`,
`FAIL` and `LOAD` lines followed by a summary.

A path is required. A directory scans `.graf` files recursively in ordinal path
order, excluding hidden entries, links and other file types. No files outside
that target are scanned. Each file loads in its own engine with its source
directory; imports are explicit and relative to that file, and are not shared
between files. The CLI's existing naming-convention options apply.

`--filter` is a case-sensitive literal substring of `relative/file.graf::test`.
A file with several returned values uses IDs such as `cases.graf#2::test`.
The filter selects methods before they or their setups execute. File bodies
still load; a filter does not avoid loading incompatible source files.

| Exit code | Meaning |
| --- | --- |
| `0` | At least one selected test, all passed, no load errors |
| `1` | A test/setup failed, with no load errors |
| `2` | Invalid target, load/report errors, or no matched tests |
| `130` | Cancelled with Ctrl+C |

A load error takes precedence over failed tests and does not stop the other
files from loading. An empty target or filter cannot produce a passing check.

## Suite file format

A file must return its suite box, or a stream of suite boxes. Do not call
`gunit.test-report` or return report counts in a file intended for `graf test`:

```graf
suite$ = (mutable>> box {
    count: 0,
    common.testing.gunit.setup>> self$.reset(): self$.count := 0,
    common.testing.gunit.test>> self$.increments(): (
        self$.count := self$.count.plus(1);
        common.testing.gunit.assert-equals(1, self$.count)
    ),
    common.testing.gunit.test>> rejects-missing-label():
        common.testing.gunit.assert-fails {missing}
});
suite$
```

Saving this as `cases.graf` and running `graf test cases.graf` reports two passes
and exits zero. Mark setup/test methods with `gunit.setup` / `gunit.test`. They
must take no arguments. Declare the receiver in the head when using `self$`.
Use receiver fields for mutable state and qualified library paths inside
methods. Graf methods do not implicitly capture unrelated caller variables;
quoted bodies follow the language's normal binding rules.

## Assertions

Here `gunit` abbreviates `common.testing.gunit`:

| Assertion | Contract |
| --- | --- |
| `assert(condition)` | Condition must be `yes` |
| `assert-equals(expected, actual)` | Values must compare equal |
| `assert-not-equals(a, b)` | Values must compare unequal |
| `fail(message)` | Raise an assertion exception with that message |
| `assert-fails {expression}` | Evaluate the quoted expression once and require a failure |
| `assert-fails {exception-class, expression}` | Require a failure matching that class |

Braces defer the body. A successful value, including `yes` or an exception
returned as data, is not a failure; neither is an empty response stream. A mixed
stream satisfies `assert-fails` if at least one failure matches. Successful
assertions allow later statements to run.

## Execution and reports

Each setup/test is invoked inside Graf `try`. A failed setup skips that test,
counts it once as failed, and later tests run their setups again. Several failed
responses from one test still count as one failed test. A test with no responses
passes. .NET exceptions become Graf exception data through the same mechanism.
Setups reset mutable state explicitly; the runner does not clone suites or roll
back side effects.

For manual use, `gunit.test-report(suite)` returns a report. `passed` and `failed` count
tests; `results.item` rows have `name`, `phase` (`"setup"` / `"test"`) and
`outcome`. Failed outcomes contain an inspectable `error`; passed outcomes
collect responses in `values.item`. The CLI uses `gunit.filtered-test-report` and reads
these reports, without duplicating discovery or the per-method try boundary.

`assert-fails` is a native deferreval that runs its quoted body in the caller's
context. Test-local variables and the receiver remain available, and body side
effects run once. This prevents unrelated variable errors from making broad
negative assertions pass. Every setup/test still runs through Graf `try`.

## Discovery

One method is registered per label. Own declarations are inspected newest
first, followed by inheritance/instantiation parents breadth-first. Parent ties
keep declared order; shared ancestors are visited once. The nearest/latest
declaration claims its label before its marker is checked. An unmarked override
therefore removes an inherited test/setup; changing a marker replaces that role.
Use distinct labels rather than overloading or accumulating tests under one name.

Discovery inspects declarations as data. It does not enter nested data, method
bodies or imported environments. Inherited methods use the original suite as
receiver. `gunit-discovery-smoke.graf` checks these boundaries.

## Compatibility and units target

The other OpenGraf components and tests were written for an older Graf. Only
units are being rewritten. Passing gunit checks does not validate those legacy
sections. The new unit core has its own targeted suites.

Run `graf test tests/units` for the replacement core. Import the
rewritten unit sources explicitly. Do not target the repository root or all of
`tests`: unrelated legacy sources are not expected to load or pass on current
Graf. `tests/testing` contains contemporary auxiliary gunit checks, not a
migration of the legacy library. The retained `tests/units-test.graf` also works with current Graf: it forwards
to four migrated cases already included in `tests/units`, so do not add those
four to the directory total. The other old test files and the old setup/runner
remain outside this target. Value assertions collect their actual response in
a tuple, so empty streams fail comparison instead of skipping an assertion.
`python3 tools/units_audit.py --legacy-source` checks inventory, migration and
example correspondence; it does not replace execution of the tests.
