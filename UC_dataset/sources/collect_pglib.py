"""Fetch every original file at the pinned PGLIB-UC commit and verify Git blobs."""
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
import hashlib
import io
import json
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
COMMIT = '39a7f38cf4703de92f0291f0c873c2e98c789301'


def collect():
    tree = json.loads((ROOT / 'sources/pglib_upstream_tree.json').read_text('utf-8'))
    expected = {entry['path']: entry for entry in tree['tree'] if entry['type'] == 'blob'}
    if tree['sha'] != COMMIT or tree['truncated']:
        raise ValueError('Upstream tree is incomplete or has the wrong commit')
    destination = (ROOT / 'raw/pglib_uc' / COMMIT).resolve()
    url = f'https://codeload.github.com/power-grid-lib/pglib-uc/zip/{COMMIT}'
    request = urllib.request.Request(url, headers={'User-Agent': 'UC-dataset-collection'})
    with urllib.request.urlopen(request, timeout=60) as response:
        body = response.read()
    records = []
    with zipfile.ZipFile(io.BytesIO(body)) as archive:
        for member in archive.infolist():
            if member.is_dir():
                continue
            relative = PurePosixPath(*PurePosixPath(member.filename).parts[1:])
            if relative.as_posix() not in expected:
                raise ValueError(f'Unexpected archive entry: {relative}')
            target = destination.joinpath(*relative.parts).resolve()
            if not target.is_relative_to(destination):
                raise ValueError('Unsafe archive path')
            data = archive.read(member)
            git_sha = hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()
            entry = expected[relative.as_posix()]
            if git_sha != entry['sha'] or len(data) != entry['size']:
                raise ValueError(f'Upstream byte verification failed: {relative}')
            if target.exists() and target.read_bytes() != data:
                raise ValueError(f'Existing original differs: {target}')
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                target.write_bytes(data)
            records.append({'path': target.relative_to(ROOT).as_posix(),
                            'upstream_path': relative.as_posix(), 'bytes': len(data),
                            'git_blob_sha': git_sha, 'sha256': hashlib.sha256(data).hexdigest()})
    if len(records) != len(expected):
        raise ValueError('Archive file count differs from the official Git tree')
    result = {'source_id': 'pglib_uc', 'upstream_commit': COMMIT,
              'source_url': url, 'acquired_at_utc': datetime.now(timezone.utc).isoformat(),
              'archive_sha256': hashlib.sha256(body).hexdigest(),
              'archive_bytes': len(body), 'file_count': len(records), 'files': records}
    (ROOT / 'sources/pglib_acquisition.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'files': len(records), 'json_instances': sum(
        row['path'].endswith('.json') for row in records), 'archive_bytes': len(body)}))


if __name__ == '__main__':
    collect()
