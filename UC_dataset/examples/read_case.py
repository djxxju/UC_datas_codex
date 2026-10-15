"""Read an unchanged PGLIB case using Python's standard library."""
from pathlib import Path
import argparse
import json

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / 'raw/pglib_uc/39a7f38cf4703de92f0291f0c873c2e98c789301/rts_gmlc/2020-01-27.json'
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('path', nargs='?', default=str(DEFAULT))
args = parser.parse_args()
path = Path(args.path)
case = json.loads(path.read_text(encoding='utf-8'))
print(json.dumps({'case': path.name, 'time_periods': case['time_periods'],
                  'thermal_generators': len(case['thermal_generators']),
                  'renewable_generators': len(case['renewable_generators']),
                  'demand_min_mw': min(case['demand']),
                  'demand_max_mw': max(case['demand']),
                  'status': 'read_only_not_solved'}, indent=2))
