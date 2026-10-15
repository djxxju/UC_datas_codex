"""Verify original PGLIB bytes and inspect data; this does not solve UC models."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import argparse
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[1]
COMMIT = '39a7f38cf4703de92f0291f0c873c2e98c789301'


def inspect():
    tree = json.loads((ROOT / 'sources/pglib_upstream_tree.json').read_text('utf-8'))
    if tree.get('truncated') or tree['sha'] != COMMIT:
        raise ValueError('Official Git tree is incomplete or has the wrong version')
    base = ROOT / 'raw/pglib_uc' / COMMIT
    files, cases, errors = [], [], []
    for entry in tree['tree']:
        if entry['type'] != 'blob':
            continue
        path = base / entry['path']
        if not path.is_file():
            errors.append(f'Missing upstream file: {entry["path"]}')
            continue
        data = path.read_bytes()
        digest = hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()
        if digest != entry['sha'] or len(data) != entry['size']:
            errors.append(f'Original bytes differ: {entry["path"]}')
        files.append({'path': path.relative_to(ROOT).as_posix(), 'bytes': len(data),
                      'git_blob_sha': digest, 'sha256': hashlib.sha256(data).hexdigest()})
        if path.suffix != '.json':
            continue
        issues = []
        try:
            instance = json.loads(data, parse_constant=lambda value: (_ for _ in ()).throw(
                ValueError(f'Non-finite JSON constant: {value}')))
            periods = instance['time_periods']
            if not isinstance(periods, int) or periods <= 0:
                raise ValueError('Invalid time_periods')
            for field in ['demand', 'reserves']:
                values = instance[field]
                if len(values) != periods or any(not math.isfinite(v) or v < 0 for v in values):
                    issues.append(f'{field}: length, finite-value or sign error')
            thermal = instance['thermal_generators']
            renewable = instance['renewable_generators']
            for uid, unit in thermal.items():
                pmin, pmax = unit['power_output_minimum'], unit['power_output_maximum']
                if not 0 <= pmin <= pmax:
                    issues.append(f'{uid}: invalid output bounds')
                for field in ['time_up_minimum', 'time_down_minimum', 'ramp_up_limit',
                              'ramp_down_limit', 'ramp_startup_limit', 'ramp_shutdown_limit']:
                    if unit[field] < 0 or not math.isfinite(unit[field]):
                        issues.append(f'{uid}: invalid {field}')
                if unit['unit_on_t0'] not in [0, 1]:
                    issues.append(f'{uid}: invalid initial commitment')
                points = unit['piecewise_production']
                if not points or not unit['startup']:
                    issues.append(f'{uid}: missing cost or startup curve')
                if any(a['mw'] >= b['mw'] for a, b in zip(points, points[1:])):
                    issues.append(f'{uid}: unsorted production cost points')
            for uid, unit in renewable.items():
                lo, hi = unit['power_output_minimum'], unit['power_output_maximum']
                if len(lo) != periods or len(hi) != periods:
                    issues.append(f'{uid}: renewable time-series length')
                elif any(not (math.isfinite(a) and math.isfinite(b) and 0 <= a <= b)
                         for a, b in zip(lo, hi)):
                    issues.append(f'{uid}: renewable bounds')
            cases.append({'case_id': 'pglib_uc/' + path.relative_to(base).with_suffix('').as_posix(),
                          'source_id': 'pglib_uc', 'family': path.parent.name,
                          'path': path.relative_to(ROOT).as_posix(), 'time_periods': periods,
                          'time_step_hours': 1, 'thermal_generators': len(thermal),
                          'renewable_generators': len(renewable), 'network': False,
                          'inspection_status': 'passed' if not issues else 'issues_found',
                          'solve_status': 'not_run', 'issues': issues})
            errors.extend(f'{entry["path"]}: {issue}' for issue in issues)
        except (KeyError, ValueError, TypeError) as exc:
            errors.append(f'{entry["path"]}: {exc}')
    if len(cases) != 56:
        errors.append(f'Expected 56 JSON instances; inspected {len(cases)}')
    result = {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'upstream_commit': COMMIT, 'scope': 'original_bytes_and_basic_data_checks_only',
              'file_count': len(files), 'instance_count': len(cases),
              'families': dict(Counter(c['family'] for c in cases)),
              'time_periods': dict(Counter(c['time_periods'] for c in cases)),
              'errors': errors, 'files': files}
    (ROOT / 'reports').mkdir(exist_ok=True)
    (ROOT / 'reports/pglib_integrity.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (ROOT / 'catalog.json').write_text(
        json.dumps({'schema_version': 'catalog-0.1', 'instances': cases},
                   ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: value for key, value in result.items() if key != 'files'},
                     ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    raise SystemExit(inspect())
