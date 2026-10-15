"""Collect original UC files on a GitHub runner; never parse or solve case data.

The output is four Release assets plus attribution and byte-provenance records.
All payloads are downloaded into temporary runner storage, not the user's PC.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import tempfile
import time
import urllib.request
import zipfile


def fetch_file(row, destination):
    if Path(row['filename']).name != row['filename']:
        raise ValueError('Only original leaf filenames are allowed')
    target = destination / row['filename']
    last_error = None
    for attempt in range(3):
        try:
            request = urllib.request.Request(row['url'], headers={'User-Agent': 'UC-dataset-collector/1.0'})
            digest = hashlib.sha256()
            size = 0
            with urllib.request.urlopen(request, timeout=90) as response, target.open('wb') as stream:
                final_url = response.url
                last_modified = response.headers.get('Last-Modified')
                while chunk := response.read(1024 * 1024):
                    stream.write(chunk)
                    digest.update(chunk)
                    size += len(chunk)
            # Detect interrupted/error-page transfers only, not UC data validity.
            expected_size = row.get('upstream_size')
            if expected_size is not None and expected_size != size:
                raise ValueError(f'Transfer length differs from official file metadata: {size} != {expected_size}')
            record = dict(row, status='downloaded', bytes=size, sha256=digest.hexdigest(),
                          final_url=final_url, last_modified=last_modified,
                          collected_at_utc=datetime.now(timezone.utc).isoformat(),
                          parameter_validation='not_run', solve_status='not_run')
            print(f"Collected {row['filename']}: {size} bytes", flush=True)
            return record
        except Exception as exc:
            last_error = exc
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"Download failed: {row['filename']}: {last_error}")


def notice(source):
    return (f"# {source['title']}\n\n"
            f"Original source: {source['source_url']}\n\n"
            f"Version: {source.get('version')}; commit: {source.get('commit')}\n\n"
            f"License: {source['license']}\n{source['license_url']}\n\n"
            f"Citation / attribution: {source['citation']}\n\n"
            "Original file contents are unchanged. This mirror only adds source metadata and "
            "this notice around files when packaging is required. No UC parameters were checked, "
            "no format conversion was performed, and no solver was run. Author-published results "
            "are upstream reference material, not results reproduced by this project.\n")


def collect_source(source, output):
    with tempfile.TemporaryDirectory(prefix='uc-originals-') as temp:
        staging = Path(temp)
        with ThreadPoolExecutor(max_workers=3) as pool:
            files = list(pool.map(lambda row: fetch_file(row, staging), source['files']))
        asset = output / source['asset_name']
        if source['packaging'] == 'unchanged_archive':
            if len(files) != 1:
                raise ValueError('Unchanged archive source must contain one file')
            shutil.move(str(staging / files[0]['filename']), asset)
        else:
            (staging / 'SOURCE_NOTICE.md').write_text(notice(source), encoding='utf-8')
            (staging / 'SOURCE_METADATA.json').write_text(json.dumps(source, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            with zipfile.ZipFile(asset, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
                for path in sorted(staging.iterdir()):
                    archive.write(path, arcname=path.name)
        with asset.open('rb') as stream:
            sha256 = hashlib.file_digest(stream, 'sha256').hexdigest()
        return {'source_id': source['source_id'], 'source_url': source['source_url'],
                'asset_name': asset.name, 'asset_bytes': asset.stat().st_size, 'asset_sha256': sha256,
                'status': 'collected_and_packaged_for_release', 'original_files': files,
                'parameter_validation': 'not_run', 'solve_status': 'not_run'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding='utf-8'))
    args.output.mkdir(parents=True, exist_ok=True)
    receipts = []
    for source in manifest['sources']:
        receipts.append(collect_source(source, args.output))
    report = {'release_tag': manifest['release_tag'], 'collection_only': True,
              'source_count': len(receipts), 'original_file_count': sum(len(r['original_files']) for r in receipts),
              'sources': receipts}
    (args.output / 'collection_receipt.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    shutil.copyfile(args.manifest, args.output / 'source_manifest.json')
    (args.output / 'ATTRIBUTION.md').write_text('\n\n'.join(notice(s) for s in manifest['sources']), encoding='utf-8')
    print('Collection complete. Data validity and solver status remain untested.', flush=True)


if __name__ == '__main__':
    main()
