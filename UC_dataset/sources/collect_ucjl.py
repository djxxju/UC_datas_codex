"""Collect official prebuilt UC.jl files without parsing or validating UC data.

Uses the existing official-documentation catalog. A family selection means all
cataloged names in that family; MATPOWER lists one day per system, not a year.
SHA-256 records identify saved bytes; they are not parameter/feasibility checks.
External data remain local; the public repository distributes links and code.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://axavier.org/UnitCommitment.jl/0.4/instances/'
DEST = ROOT / 'raw/unitcommitment_jl_0.4'


def collect_one(name, no_proxy):
    dest = DEST.resolve()
    target = (dest / (name + '.json.gz')).resolve()
    if not target.is_relative_to(dest) or any(c in name for c in ('?', '#', ':', '\\')):
        raise ValueError(f'Invalid catalog name: {name}')
    row = {'name': name, 'url': BASE + name + '.json.gz',
           'local_path': target.relative_to(ROOT).as_posix(),
           'collection_time_utc': datetime.now(timezone.utc).isoformat(),
           'data_validation': 'not_run_in_this_collection',
           'solve_status': 'not_run', 'redistribution_status': 'not_cleared'}
    try:
        if target.exists():
            data = target.read_bytes()
            row['status'] = 'already_present'
        else:
            opener = (urllib.request.build_opener(urllib.request.ProxyHandler({}))
                      if no_proxy else urllib.request.build_opener())
            with opener.open(row['url'], timeout=45) as response:
                data = response.read()
                row['final_url'] = response.url
                row['last_modified'] = response.headers.get('Last-Modified')
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_suffix(target.suffix + '.part')
            temporary.write_bytes(data)
            temporary.replace(target)
            row['status'] = 'downloaded'
        row['bytes'] = len(data)
        row['sha256'] = hashlib.sha256(data).hexdigest()
    except Exception as exc:
        row.update(status='download_failed', error_type=type(exc).__name__)
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('names', nargs='*', help='Official instance identifiers')
    parser.add_argument('--family', action='append', choices=['or-lib', 'tejada19', 'matpower', 'pglib-uc'])
    parser.add_argument('--no-proxy', action='store_true', help='Bypass proxy for this process only')
    args = parser.parse_args()
    catalog = json.loads((ROOT / 'sources/ucjl_available_instances.json').read_text(encoding='utf-8'))
    known = {r['name'] for r in catalog['instances']}
    if not args.names and not args.family:
        parser.error('Specify instance names or at least one --family.')
    if set(args.names) - known:
        parser.error('Name is absent from the pinned official-documentation catalog.')
    names = sorted(set(args.names) | {r['name'] for r in catalog['instances']
                                    if r['source_family'] in (args.family or [])})
    rows = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        for row in pool.map(lambda name: collect_one(name, args.no_proxy), names):
            rows.append(row)
            if len(rows) % 20 == 0 or len(rows) == len(names) or row['status'] == 'download_failed':
                print(f"{len(rows)}/{len(names)} {row['status']} {row['name']}", flush=True)
    # Append a new receipt for each collection; never overwrite earlier evidence.
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    receipt = ROOT / 'reports' / f'ucjl_collection_{stamp}.json'
    receipt.parent.mkdir(parents=True, exist_ok=True)
    report = {'collection_only': True, 'server_version': '0.4',
              'catalog_url': catalog['documentation_url'],
              'code_commit': catalog['code_commit'],
              'note': 'Raw-byte collection only. No gzip/JSON data parsing, parameter checks, modeling or solving.',
              'selected_count': len(rows),
              'downloaded_count': sum(r['status'] == 'downloaded' for r in rows),
              'already_present_count': sum(r['status'] == 'already_present' for r in rows),
              'failed_count': sum(r['status'] == 'download_failed' for r in rows),
              'files': rows}
    receipt.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(receipt.relative_to(ROOT.parent).as_posix(), flush=True)
    return int(report['failed_count'] > 0)


if __name__ == '__main__':
    raise SystemExit(main())
