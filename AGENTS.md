# Working on OpenGraf

Units under `src/units` target current `Graf/develop`. Other components and the
old `tests/units-test.graf` still target an older Graf. Validate rewritten units
with `graf test tests/units`; auxiliary gunit suites are in `tests/testing`.

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
