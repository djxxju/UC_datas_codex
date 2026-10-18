"""Check packaged original bytes against a previously audited manifest, without parsing UC data."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile


def verify(manifest, output):
    receipt = json.loads((output / 'collection_receipt.json').read_text(encoding='utf-8'))
    expected_sources = {s['source_id']: s for s in manifest['sources']}
    actual_sources = {s['source_id']: s for s in receipt['sources']}
    if (len(expected_sources) != len(manifest['sources']) or
            len(actual_sources) != len(receipt['sources']) or
            expected_sources.keys() != actual_sources.keys()):
        raise ValueError('Source set differs from audited manifest')
    verified = 0
    for source_id, source in expected_sources.items():
        record = actual_sources[source_id]
        asset = output / source['asset_name']
        if record['asset_name'] != source['asset_name']:
            raise ValueError('Asset name differs from manifest')
        with asset.open('rb') as stream:
            digest = hashlib.file_digest(stream, 'sha256').hexdigest()
        if digest != record['asset_sha256'] or asset.stat().st_size != record['asset_bytes']:
            raise ValueError('Packaged asset differs from collection receipt')
        expected = {f['filename']: f for f in source['files']}
        actual = {f['filename']: f for f in record['original_files']}
        if (len(expected) != len(source['files']) or len(actual) != len(record['original_files']) or
                expected.keys() != actual.keys()):
            raise ValueError('Original file set differs from audited manifest')
        with zipfile.ZipFile(asset) as archive:
            names = archive.namelist()
            if len(names) != len(set(names)) or set(names) != set(expected) | {'SOURCE_NOTICE.md', 'SOURCE_METADATA.json'}:
                raise ValueError('Unexpected or missing archive members')
            for name, audited in expected.items():
                with archive.open(name) as stream:
                    digest = hashlib.file_digest(stream, 'sha256').hexdigest()
                size = archive.getinfo(name).file_size
                if digest != audited['expected_sha256'] or size != audited['upstream_size']:
                    raise ValueError(f'Original bytes differ from license-audited version: {source_id}/{name}')
                if actual[name]['sha256'] != digest or actual[name]['bytes'] != size:
                    raise ValueError(f'Original bytes differ from receipt: {source_id}/{name}')
                verified += 1
    return verified


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding='utf-8'))
    count = verify(manifest, args.output)
    print(f'Verified {count} original files against license-audited SHA-256 identities. No UC parameters inspected.')


if __name__ == '__main__':
    main()
