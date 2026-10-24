# Testing with gunit

Open Graf uses `common.testing.gunit`, implemented in Graf's embedded library.
The runner and assertions require the corresponding changes on `Graf/develop`.
The replacement units catalogue remains pending.

## Define a suite

A suite is a box. Mark setup methods with `gunit.setup` and test methods with
`gunit.test`. Each test runs its setups first. All setups and tests must take no
arguments. Declare the receiver in the method head (`self$.reset`) when its body
uses `self$`. Use fields of that receiver for mutable test state and qualified
library paths inside methods. Graf methods do not implicitly capture unrelated
variables from a calling method. Quoted bodies follow Graf's normal binding rules.

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

report$ = common.testing.gunit.run(suite$);
(report$.passed, report$.failed)
```

The expected result is `2`, then `0`. `run` returns a report value; it does not
set a process exit code. The separate `graf test` CLI work is still pending.

## Assertions

| Assertion | Contract |
| --- | --- |
| `assert(condition)` | Condition must be `yes` |
| `assert-equals(expected, actual)` | Values must compare equal |
| `assert-not-equals(a, b)` | Values must compare unequal |
| `fail(message)` | Raise an assertion exception with that message |
| `assert-fails {expression}` | Evaluate the quoted expression once and require a failure |
| `assert-fails {exception-class, expression}` | Require a failure matching that exception class |

Use braces to defer an `assert-fails` body. A successful value, including `yes`
or an exception returned as data, is not a failure. An empty response stream
also does not satisfy `assert-fails`. A mixed stream satisfies it if at least one
failure matches. Successful assertions allow the next statement to run.

## Reports and failure handling

`report.passed` and `report.failed` count tests. `report.results` contains repeated
`item` labels. Each item contains `name`, `phase` (`"setup"` or `"test"`) and
`outcome`. A failed outcome has an inspectable `error`; a passed outcome collects
its successful responses under `values.item`.

Every setup and test invocation is guarded by Graf `try`. A failed setup skips
its test and counts that test once as failed. The runner then proceeds to the
next test and runs setups again. A failure among several test responses fails
the test once. An empty test response stream passes. .NET exceptions become Graf
exception values and are recorded through the same mechanism.

Setups provide state preparation; the runner does not automatically clone the
suite or roll back external effects. Reset mutable test state explicitly.

## Open Graf smoke check

Run `tests/testing/gunit-smoke.graf` with the updated Graf interpreter:

```sh
graf run tests/testing/gunit-smoke.graf
```

The expected result is `5`, then `0`. The smoke suite checks assertions, deferred
failures, class filtering, continued execution after failure and setup failure.
The command is `graf run` until the dedicated test CLI is implemented.

## Discovery rules

Gunit registers one method per label. It inspects the suite's own declarations,
newest first, then inheritance and instantiation parents breadth-first. Parents
at the same depth keep their declared order; shared ancestors are visited once.
The nearest/latest declaration claims a label before its marker is checked.
An unmarked override therefore removes an inherited test/setup, and changing a
mark from setup to test replaces that role. Use distinct labels for distinct
tests rather than overloading or accumulating them under the same name.

Discovery reads declarations as data. It never enters nested data, method
bodies or imported environments. Inherited methods receive the original suite
as their receiver. The additional smoke suite checks these boundaries:

```sh
graf run tests/testing/gunit-discovery-smoke.graf
```

Its expected result is `6`, then `0`.

## Compatibility and test scope

OpenGraf's existing components and tests were written for an older Graf version.
Only units are scheduled for rewriting in this project. Do not interpret checks
of gunit or the new units as validation of the other legacy sections.

When the dedicated test CLI is implemented, run the replacement units tests
under the explicit `tests/units` target. Do not default to the repository root
or all of `tests`: unrelated legacy tests are not expected to pass against
current Graf. The two contemporary suites in `tests/testing` are auxiliary
checks of gunit, not a migration of the legacy library.
