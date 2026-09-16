"""Refresh or verify the distributable file inventory (excluding itself and caches)."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
EXCLUDED={'.git','.tools','__pycache__','.venv','node_modules'}

def inventory():
    result=[]
    for parent,dirs,names in os.walk(ROOT):
        dirs[:]=[d for d in dirs if d not in EXCLUDED]
        for name in names:
            path=Path(parent)/name
            rel=path.relative_to(ROOT).as_posix()
            if rel=='MANIFEST.json' or rel.startswith(('reports/generated/','presentation/preview/')):
                continue
            raw=path.read_bytes()
            result.append(dict(path=rel,sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw)))
    return sorted(result,key=lambda item:item['path'])

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',action='store_true',help='Replace MANIFEST.json with the current inventory')
    args=parser.parse_args()
    current=inventory()
    target=ROOT/'MANIFEST.json'
    if args.write:
        target.write_text(json.dumps(current,indent=2)+'\n',encoding='utf-8')
        print(f'Wrote hashes and sizes for {len(current)} distributable files.')
        return 0
    expected=json.loads(target.read_text(encoding='utf-8'))
    if expected!=current:
        print('Manifest differs. Review changes, then run with --write.')
        return 1
    print(f'PASS: hashes and sizes match for {len(current)} distributable files.')
    return 0

if __name__=='__main__': sys.exit(main())
