"""Fetch selected ready-made UC.jl instances from the official versioned server.

Downloaded data stay local until their redistribution terms have been confirmed.
Default list contains small OR-LIB cases plus one day for common network systems.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import gzip
import hashlib
import json
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://axavier.org/UnitCommitment.jl/0.4/instances/'
DEFAULTS = ['or-lib/10_0_1_w', 'or-lib/20_0_1_w', 'or-lib/50_0_1_w',
            'matpower/case14/2017-01-01', 'matpower/case30/2017-01-01',
            'matpower/case57/2017-01-01', 'matpower/case118/2017-01-01',
            'matpower/case300/2017-01-01', 'matpower/case2383wp/2017-01-01',
            'tejada19/UC_24h_214g', 'tejada19/UC_168h_36g']


def download(names, no_proxy=False):
    destination = (ROOT / 'raw/unitcommitment_jl_0.4').resolve()
    results = []
    for name in names:
        target = (destination / (name + '.json.gz')).resolve()
        if not target.is_relative_to(destination) or '?' in name or '#' in name:
            raise ValueError(f'Invalid instance name: {name}')
        url = BASE + name + '.json.gz'
        try:
            if target.exists():
                data = target.read_bytes()
            else:
                opener = urllib.request.build_opener(urllib.request.ProxyHandler({})) if no_proxy else urllib.request.build_opener()
                with opener.open(url, timeout=45) as response:
                    data = response.read()
                json.loads(gzip.decompress(data))
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            instance = json.loads(gzip.decompress(data))
            row = {'name': name, 'url': url, 'status': 'downloaded_and_json_parsed',
                   'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                   'parameters': instance.get('Parameters'),
                   'redistribution_status': 'not_cleared', 'solve_status': 'not_run'}
        except Exception as exc:
            row = {'name': name, 'url': url, 'status': 'download_failed',
                   'error_type': type(exc).__name__}
        results.append(row)
        print(row['status'], name, flush=True)
    report = {'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'files': results}
    (ROOT / 'reports/ucjl_local_downloads.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return int(any(row['status'] == 'download_failed' for row in results))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('names', nargs='*', help='Official instance names without .json.gz')
    parser.add_argument('--no-proxy', action='store_true', help='Bypass the local proxy for this download process only')
    args = parser.parse_args()
    raise SystemExit(download(args.names or DEFAULTS, args.no_proxy))
