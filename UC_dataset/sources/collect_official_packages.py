"""Download the original official archives listed in official_packages.json.

Only save bytes and provenance. Do not extract, parse, validate or solve cases.
Archives stay outside Git; published manifests link to their official hosts.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'raw/official_packages'


def collect_one(item, no_proxy):
    dest = DEST.resolve()
    target = (dest / item['filename']).resolve()
    if not target.is_relative_to(dest):
        raise ValueError('Archive path must stay inside collection directory')
    row = dict(item, local_path=target.relative_to(ROOT).as_posix(),
               collection_time_utc=datetime.now(timezone.utc).isoformat(),
               content_validation='not_run', solve_status='not_run')
    try:
        if not target.exists():
            opener = (urllib.request.build_opener(urllib.request.ProxyHandler({}))
                      if no_proxy else urllib.request.build_opener())
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_suffix(target.suffix + '.part')
            request = urllib.request.Request(item['url'], headers={'User-Agent': 'UC-dataset-collector/1.0'})
            with opener.open(request, timeout=60) as response, temporary.open('wb') as out:
                row['final_url'] = response.url
                row['last_modified'] = response.headers.get('Last-Modified')
                while chunk := response.read(1024 * 1024):
                    out.write(chunk)
            temporary.replace(target)
            row['status'] = 'downloaded'
        else:
            row['status'] = 'already_present'
        with target.open('rb') as stream:
            row['sha256'] = hashlib.file_digest(stream, 'sha256').hexdigest()
        row['bytes'] = target.stat().st_size
    except Exception as exc:
        row.update(status='download_failed', error_type=type(exc).__name__)
    print(item['id'], row['status'], row.get('bytes', ''), flush=True)
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ids', nargs='*', help='Package IDs; omitted means all manifest entries')
    parser.add_argument('--no-proxy', action='store_true', help='Bypass proxy for this process only')
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'sources/official_packages.json').read_text(encoding='utf-8'))
    known = {p['id'] for p in manifest['packages']}
    if set(args.ids) - known:
        parser.error('Unknown package ID')
    selected = [p for p in manifest['packages'] if not args.ids or p['id'] in args.ids]
    with ThreadPoolExecutor(max_workers=3) as pool:
        rows = list(pool.map(lambda p: collect_one(p, args.no_proxy), selected))
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    receipt = ROOT / 'reports' / f'official_package_collection_{stamp}.json'
    receipt.parent.mkdir(parents=True, exist_ok=True)
    report = {'collection_only': True, 'archives_extracted': False,
              'selected_count': len(rows),
              'failed_count': sum(r['status'] == 'download_failed' for r in rows), 'files': rows}
    receipt.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(receipt.relative_to(ROOT.parent).as_posix(), flush=True)
    return int(report['failed_count'] > 0)


if __name__ == '__main__':
    raise SystemExit(main())
