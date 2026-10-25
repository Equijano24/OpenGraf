# Naming conventions and review

Classes use nouns or adjective+noun phrases that describe what they are.
Value-returning methods name their result. A procedure that returns void or no
data uses an action verb. An empty result set from a data query does not make
the query a procedure. Boolean methods/labels may start with `is`; logical
predicates may use Prolog-style relations. Standard gunit `assert*` names are
an explicit exception.

This review covers the units implementation, gunit foundation, SDK test command,
engine helpers added for those features, their fixtures, examples and technical
references. It does not migrate unrelated legacy OpenGraf components or rename
all pre-existing Graf APIs. The review was completed before step 7; its naming
conventions also apply to the angular API. The current checkpoint is recorded
in the [eleven-step plan](plan-de-trabajo.md).

## Unit API migration

The table below covers provisional names introduced during the rewrite's early
steps. The [historical migration guide](units/migration.md) covers the original
31-factory API, including its imports, coherent references and semantic changes.

| Previous name | Current name | Result |
| --- | --- | --- |
| `make(number)` | `quantity(number)` | Immutable quantity; factory construction extension point |
| `define(id, symbol, scale, ...)` | `definition(id, symbol, scale, ...)` | Local unit definition |
| `with-value(number)` | `quantity-with-value(number)` | New quantity through the original factory |
| `coherent()` | `coherent-value()` | Coherent numeric payload |
| `to-coherent(number)` | `coherent-value-of(number)` | Numeric payload mapped to coherent units |
| `from-coherent(number)` | `display-value-of(number)` | Numeric payload mapped to the definition's displayed unit |
| `can-convert-from(quantity)` | `is-convertible-from(quantity)` | Conversion eligibility |

Constructor calls such as `meters$(2)` and `meters$(otherQuantity)` keep their
meaning. Overrides of the construction extension point now override `quantity`.
This is a naming change; conversion factors, dimensions, numeric behavior,
immutability and exception handling are preserved.

## Gunit and SDK migration

| Previous name | Current name |
| --- | --- |
| `gunit.run(suite)` | `gunit.test-report(suite)` |
| `gunit.run-filtered(suite, prefix, filter)` | `gunit.filtered-test-report(suite, prefix, filter)` |
| Gunit type `passed` / `failed` | `passed-outcome` / `failed-outcome` |
| Gunit queries `own` / `marked` | `own-marked-compositions` / `marked-compositions` |
| Gunit Boolean query `known` | `is-known` |
| SDK `Graf.TestStaticAsync(...)` | `Graf.TestSummaryAsync(...)` |

The report count fields remain `passed` and `failed`. The CLI remains
`graf test <PATH> [--filter <TEXT>]`, with the same output and exit codes.
Test procedure names now start with verification verbs; suite contents and
assertions are unchanged.

In C#, the added failure assertion is named `FailureAssertion`. The unconditional
failure deferreval exposed by the gunit work is `AssertionFailureDeferreval`.
Their public Graf labels remain `assert-fails` and `fail`. `TestCommand`,
`TestSummary`, test classes and quantity-family names already use nouns.
New label-result helpers use `LabelResult...` and `LabelValue...` instead of
`ResolveLabel...`; SDK helpers name their returned summaries or diagnostics.

## Preserved protocols

The mathematical messages `plus`, `minus`, `times`, `over`, `pow`, `root`,
`rounded`, `compared-to` and relational comparisons preserve Graf's established
numeric protocol and the requested units API. `require-linear` remains a verb:
it validates the precondition and returns a statement response. `assert*` names
retain testing conventions. Required external overrides such as Spectre's
`ExecuteAsync` keep their framework contract names. Deliberately arbitrary
fixture labels used in discovery/dispatch tests are test inputs.

No aliases with the retired action names are added. Callers and examples in
these repositories use the current names.
