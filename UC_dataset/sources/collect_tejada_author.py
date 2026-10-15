"""Collect the author's published ZIPs, model, README and MIT notice via Git blobs.

This only downloads original bytes and records provenance; ZIPs are not opened.
The GitHub blob endpoint avoids raw-host/archive-host connectivity issues.
"""
from datetime import datetime, timezone
from pathlib import Path
import argparse
import base64
import hashlib
import json
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REPO = 'datejada/UC-data'
COMMIT = '1b417ece7ca61d41fca7302df6a0313f8236d611'
FILES = {
    'UC-Instances.zip': '7a2f0916d0628e66eb7cea5799ff0373f464a1a3',
    'UC-Instances-ResultsSummary.zip': '3ce815e2ba77e5b9c313509b066014997ff59731',
    'README.md': 'aac30686fb007679148e5053c459a701c115c06a',
    'LICENSE': '88f1f56e4f809a8d15e52cb761a6b79870b8f4a8',
    'StarGenLite_SCUC.gms': '8febf49d61a9d6d1ff8b24267345c81303afe990',
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--no-proxy', action='store_true')
    parser.add_argument('--archive-path', type=Path,
                        help='Copy originals from an already downloaded official repository ZIP; nested instance ZIPs stay unopened')
    args = parser.parse_args()
    opener = (urllib.request.build_opener(urllib.request.ProxyHandler({}))
              if args.no_proxy else urllib.request.build_opener())
    destination = ROOT / 'raw/tejada_author' / COMMIT
    destination.mkdir(parents=True, exist_ok=True)
    rows = []
    for name, blob in FILES.items():
        url = f'https://api.github.com/repos/{REPO}/git/blobs/{blob}'
        row = {'filename': name, 'url': url, 'upstream_git_blob_sha': blob,
               'commit': COMMIT, 'local_path': (destination / name).relative_to(ROOT).as_posix(),
               'collection_time_utc': datetime.now(timezone.utc).isoformat(),
               'content_validation': 'not_run', 'solve_status': 'not_run'}
        try:
            target = destination / name
            if target.exists():
                data = target.read_bytes()
                row['status'] = 'already_present'
            elif args.archive_path:
                with zipfile.ZipFile(args.archive_path) as archive:
                    data = archive.read(f'UC-data-{COMMIT}/{name}')
                target.write_bytes(data)
                row['status'] = 'copied_from_official_repository_archive'
                row['acquisition_method'] = 'outer_repository_archive_only; nested_instance_zips_unopened'
                row['source_archive'] = args.archive_path.as_posix()
            else:
                request = urllib.request.Request(url, headers={
                    'Accept': 'application/vnd.github+json', 'User-Agent': 'UC-dataset-collector/1.0'})
                with opener.open(request, timeout=25) as response:
                    payload = json.load(response)
                data = base64.b64decode(payload['content'])
                target.write_bytes(data)
                row['status'] = 'downloaded'
            row['bytes'] = len(data)
            row['sha256'] = hashlib.sha256(data).hexdigest()
        except Exception as exc:
            row.update(status='download_failed', error_type=type(exc).__name__, error=str(exc))
        print(name, row['status'], row.get('bytes', ''), row.get('error', ''), flush=True)
        rows.append(row)
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    receipt = ROOT / 'reports' / f'tejada_collection_{stamp}.json'
    receipt.write_text(json.dumps({'collection_only': True, 'instance_archives_extracted': False,
                                  'files': rows}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(receipt.relative_to(ROOT.parent).as_posix(), flush=True)
    return int(any(r['status'] == 'download_failed' for r in rows))


if __name__ == '__main__':
    raise SystemExit(main())
