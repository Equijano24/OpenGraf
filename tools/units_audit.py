"""Check the published units inventory, migration ledger and executable documentation.

This checks source/test correspondence. Execution is a separate `graf test`
check; finding a test declaration is not evidence that the test passed.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEST = re.compile(r'common\.testing\.gunit\.test\s*>>\s*(?:self\$\.)?([\w-]+)\s*\(\s*\)')


def source_text(path: str) -> str:
    return (ROOT / path).read_text()


def normalized_source(source: str) -> str:
    return '\n'.join(line.strip() for line in source.splitlines()
                     if line.strip() and not line.strip().startswith('//'))


def units_audit(legacy_source: bool = False) -> dict:
    catalogue = json.loads(source_text('tools/units-catalogue.json'))
    migration = json.loads(source_text('tools/units-migration.json'))
    names = [row['name'] for row in catalogue['units'] + catalogue['special_units']]
    if len(names) != len(set(names)):
        raise ValueError('Duplicate published factory')
    cases = {}
    for path in sorted((ROOT / 'tests/units').rglob('*.graf')):
        labels = TEST.findall(path.read_text())
        if len(labels) != len(set(labels)):
            raise ValueError(f'Duplicate test label: {path.relative_to(ROOT)}')
        cases[path.relative_to(ROOT).as_posix()] = set(labels)
    for name in names:
        if not (ROOT / f'src/units/{name}.graf').is_file():
            raise ValueError(f'Missing public factory: {name}')
        matches = sum('verify-' + name in labels for path, labels in cases.items()
                      if path.startswith('tests/units/catalogue/'))
        if matches != 1:
            raise ValueError(f'Expected one catalogue construction case: {name}, found {matches}')
    legacy_names = [row['legacy'] for row in migration['legacy_units']]
    if len(legacy_names) != len(set(legacy_names)):
        raise ValueError('Duplicate historical mapping')
    legacy_test_names = [row['legacy'] for row in migration['legacy_tests']]
    if len(legacy_test_names) != len(set(legacy_test_names)):
        raise ValueError('Duplicate historical test mapping')
    for row in migration['legacy_units'] + migration['legacy_tests']:
        path, label = row['test'].split('::')
        if label not in cases.get(path, set()):
            raise ValueError(f'Missing migration case: {row["test"]}')
    for row in migration['legacy_units']:
        replacement = row['replacement']
        if not replacement.startswith('local:') and replacement not in names:
            raise ValueError(f'Unknown replacement: {replacement}')
        if replacement.startswith('local:') and row['decision'] != 'local-definition':
            raise ValueError(f'Local replacement lacks an explicit decision: {row["legacy"]}')
    for example in migration['examples']:
        code = normalized_source(source_text(example['file']))
        blocks = re.findall(r'```graf\n(.*?)```', source_text(example['document']), re.S)
        if not any(normalized_source(block) == code for block in blocks):
            raise ValueError(f'Executable example differs from its reference: {example["file"]}')
    forbidden = re.compile(r'\bopen\.units\b|\btest-fixture\b|\bassert\.(?:are-equal|is-true)\b')
    targets = list((ROOT / 'src/units').rglob('*.graf'))
    targets += list((ROOT / 'examples/units').rglob('*.graf'))
    targets += list((ROOT / 'tests/units').rglob('*.graf'))
    targets += [ROOT / 'tests/units-test.graf']
    for path in targets:
        if forbidden.search(normalized_source(path.read_text())):
            raise ValueError(f'Legacy runtime dependency in current units: {path.relative_to(ROOT)}')
    if legacy_source:
        expected = set()
        for module in ['distance', 'angle', 'weight', 'temperature', 'information-unit']:
            raw = subprocess.check_output(['git', 'show', migration['legacy_commit'] + ':src/units/' + module + '.graf'], cwd=ROOT)
            # Historical sources contain an old byte encoding; labels are ASCII.
            labels = re.findall(r'^\s*([\w-]+):\s*' + re.escape(module) + r'\(', raw.decode('latin1'), re.M)
            expected.update(module + '.' + label for label in labels)
        if expected != set(legacy_names):
            raise ValueError(f'Historical inventory differs: {expected.symmetric_difference(legacy_names)}')
        raw = subprocess.check_output(['git', 'show', migration['legacy_commit'] + ':tests/units-test.graf'], cwd=ROOT)
        labels = re.findall(r'test\("([^"]+)"\)', raw.decode('latin1'))
        if set(labels) != {row['legacy'] for row in migration['legacy_tests']}:
            raise ValueError('Historical test inventory differs')
    return dict(named_factories=len(names), catalogue_cases=len(names),
                unit_cases=sum(len(labels) for labels in cases.values()),
                legacy_factories=len(legacy_names), legacy_tests=len(migration['legacy_tests']),
                matched_examples=len(migration['examples']), legacy_source_checked=legacy_source)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--legacy-source', action='store_true', help='Also compare the ledger with the pinned historical git sources; needs that commit locally.')
    parser.add_argument('--json', action='store_true', help='Print the correspondence report as JSON.')
    args = parser.parse_args()
    try:
        report = units_audit(args.legacy_source)
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        raise SystemExit(str(error)) from error
    print(json.dumps(report, indent=2) if args.json else '; '.join(f'{key}: {value}' for key, value in report.items()))
