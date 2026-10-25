# Working on OpenGraf

Units under `src/units` target current `Graf/develop`. Other components still
target an older Graf. Validate rewritten units with `graf test tests/units`;
auxiliary gunit suites are in `tests/testing`. The retained `tests/units-test.graf`
now forwards to four migrated cases already included in `tests/units`.
Check source/example correspondence with `python3 tools/units_audit.py`; add
`--legacy-source` to verify the migration ledger against its pinned git sources.

## Naming

- Classes use nouns or adjective+noun phrases that state what they are.
- Functions and methods that return data name their result. Prefer `quantity`,
  `definition` and `test-report` to `make`, `define` and `run`.
- Procedures that return void or no data use action verbs.
- Boolean labels/methods may start with `is`. Logical predicates may follow
  Prolog-like relational naming.
- Standard gunit `assert*` names are an explicit exception. Established Graf
  mathematical operators keep the shared numeric protocol.
- Test procedures use verification verbs. Arbitrary fixture labels used to test
  discovery, overrides or dispatch are test data, not application API names.

Update callers, examples and technical documentation together when changing an
API name. See `docs/naming.md` for the audited naming changes and migration map.
