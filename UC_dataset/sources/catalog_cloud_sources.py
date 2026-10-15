"""Refresh public file metadata only; never download the case payloads locally."""
from pathlib import Path
import json
import urllib.request

HERE = Path(__file__).resolve().parent


def read_json(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'UC-dataset-catalog/1.0'})
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.load(response)


def main():
    md_url = 'https://data.mendeley.com/public-api/datasets/h7cnt32kys/files?folder_id=root&version=1'
    md = read_json(md_url)
    fg_url = 'https://api.figshare.com/v2/articles/8131529/versions/2'
    fg = read_json(fg_url)
    sources = [
        {'source_id': 'rts_gmlc', 'title': 'RTS-GMLC v0.2.3',
         'source_url': 'https://github.com/GridMod/RTS-GMLC/releases/tag/v0.2.3',
         'version': 'v0.2.3', 'commit': '3ece0d3725c844056132393ee252b3083dd4eab4',
         'license': 'Custom DATA USE DISCLAIMER AGREEMENT in upstream README',
         'license_url': 'https://github.com/GridMod/RTS-GMLC/blob/3ece0d3725c844056132393ee252b3083dd4eab4/README.md',
         'citation': 'Barrows et al., The IEEE Reliability Test System: A Proposed 2019 Update, DOI 10.1109/TPWRS.2019.2925557; preserve the complete upstream notice and DOE/NREL/ALLIANCE attribution.',
         'packaging': 'unchanged_archive', 'asset_name': 'RTS-GMLC-v0.2.3.zip',
         'files': [{'filename': 'RTS-GMLC-v0.2.3.zip', 'url': 'https://codeload.github.com/GridMod/RTS-GMLC/zip/3ece0d3725c844056132393ee252b3083dd4eab4'}]},
        {'source_id': 'tejada_uc_data', 'title': 'Tejada-Arango UC-data author repository',
         'source_url': 'https://github.com/datejada/UC-data',
         'version': None, 'commit': '1b417ece7ca61d41fca7302df6a0313f8236d611',
         'license': 'MIT repository license; original LICENSE included in archive',
         'license_url': 'https://github.com/datejada/UC-data/blob/1b417ece7ca61d41fca7302df6a0313f8236d611/LICENSE',
         'citation': 'D. A. Tejada-Arango, S. Lumbreras, P. Sanchez-Martin and A. Ramos; DOI 10.1109/TPWRS.2019.2962024. Copyright (c) 2018 Diego Alejandro Tejada Arango. Preserve original LICENSE and README.',
         'packaging': 'unchanged_archive', 'asset_name': 'Tejada-UC-data-1b417ece.zip',
         'files': [{'filename': 'Tejada-UC-data-1b417ece.zip', 'url': 'https://codeload.github.com/datejada/UC-data/zip/1b417ece7ca61d41fca7302df6a0313f8236d611'}]},
        {'source_id': 'stochastic_uc_solar', 'title': 'Stochastic UC data files',
         'source_url': 'https://data.mendeley.com/datasets/h7cnt32kys/1',
         'version': 1, 'doi': '10.17632/h7cnt32kys.1',
         'license': 'CC BY 4.0', 'license_url': 'https://creativecommons.org/licenses/by/4.0/',
         'citation': 'Doubleday, Kate; Hodge, Bri-Mathias; Lara, Jose Daniel (2022), Stochastic UC data files, Mendeley Data, V1, doi: 10.17632/h7cnt32kys.1.',
         'institutional_affiliations': ['National Renewable Energy Laboratory', 'University of California Berkeley', 'University of Colorado Boulder'],
         'model_scope': 'Research data for stochastic UC with high solar PV shares; original JSON and HDF5 files for HodgeLab/Unit_Commitment and NREL-SIIP/ExtremeSolarTexas.',
         'metadata_url': md_url, 'packaging': 'original_files_with_notice',
         'asset_name': 'Stochastic-UC-solar-h7cnt32kys-v1.zip',
         'files': [{'filename': f['filename'], 'url': f['content_details']['download_url'],
                    'upstream_file_id': f['id'], 'upstream_size': f['size'],
                    'upstream_sha256_as_reported': f['content_details'].get('sha256_hash')}
                   for f in md]},
        {'source_id': 'monash_capacity_uc', 'title': fg['title'],
         'source_url': fg['url_public_html'], 'version': 2, 'doi': fg['doi'],
         'license': fg['license']['name'], 'license_url': fg['license']['url'],
         'citation': 'Semini Wijekoon; Ariel Liebman; Simon Dunstall (2019), Data Set for Capacity Expansion Planning with Unit Commitment, Monash University, version 2, DOI 10.26180/5cdbde51bbb1b.',
         'model_scope': 'Six capacity-expansion cases with UC parameters, DC networks, storage candidates and chronological annual load/renewable profiles; retain the original XLSX files without conversion.',
         'metadata_url': fg_url, 'packaging': 'original_files_with_notice',
         'asset_name': 'Monash-capacity-expansion-UC-v2.zip',
         'files': [{'filename': f['name'], 'url': f['download_url'], 'upstream_file_id': f['id'],
                    'upstream_size': f['size'], 'upstream_md5_as_reported': f.get('computed_md5')}
                   for f in fg['files']]}
    ]
    manifest = {'created_date': '2026-10-15', 'repository': 'djxxju/UC_datas_codex',
                'release_tag': 'official-data-2026-10-15-batch04',
                'scope': 'Collect original files on GitHub-hosted runner and publish GitHub Release assets. No parameter validation, model conversion or solver execution.',
                'sources': sources}
    path = HERE / 'cloud_collection_2026-10-15.json'
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for source in sources:
        print(source['source_id'], len(source['files']), source['license'])


if __name__ == '__main__':
    main()
