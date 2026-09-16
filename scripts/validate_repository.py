"""Validate local links, structured files, Bash syntax, and PPTX package integrity.

Uses the standard library. YAML parsing is included when PyYAML is installed.
No external scanners or remote endpoints are executed.
"""
from pathlib import Path
import json
import re
import shutil
import subprocess
import sys
import tomllib
import urllib.parse
import xml.etree.ElementTree as ET
import zipfile

ROOT=Path(__file__).resolve().parents[1]
EXCLUDED={'.tools','.git','__pycache__','preview','generated'}

def files():
    # Prune excluded directories instead of opening locally installed dependencies.
    import os
    for parent,dirs,names in os.walk(ROOT):
        dirs[:]=[d for d in dirs if d not in EXCLUDED]
        for name in names:
            yield Path(parent)/name

def main():
    errors=[]
    checked=0
    yaml_count=0
    try:
        import yaml
    except ImportError:
        yaml=None
    bash_path=Path('C:/Program Files/Git/bin/bash.exe')
    bash=str(bash_path) if bash_path.exists() else shutil.which('bash')
    for p in files():
        rel=p.relative_to(ROOT).as_posix()
        try:
            if p.suffix=='.md':
                value=p.read_text(encoding='utf-8')
                # Code examples can contain demonstration placeholders that are not links.
                prose=re.sub(r'```.*?```','',value,flags=re.S)
                for match in re.finditer(r'\[[^\]]*\]\(([^\s)]+)\)',prose):
                    target=match.group(1).strip('<>')
                    if re.match(r'^[a-zA-Z]+:',target) or target.startswith('#'):
                        continue
                    path=urllib.parse.unquote(target.split('#')[0])
                    if path and not (p.parent/path).exists():
                        errors.append(f'{rel}: broken local link {target}')
            elif p.suffix in ('.json','.sarif'):
                json.loads(p.read_text(encoding='utf-8'))
            elif p.suffix=='.toml':
                tomllib.loads(p.read_text(encoding='utf-8'))
            elif p.suffix=='.xml':
                ET.parse(p)
            elif p.suffix in ('.yml','.yaml') and yaml:
                list(yaml.safe_load_all(p.read_text(encoding='utf-8')))
                yaml_count+=1
            elif p.suffix=='.sh' and bash:
                result=subprocess.run([bash,'-n',p.as_posix()],capture_output=True,text=True,timeout=15)
                if result.returncode: errors.append(f'{rel}: {result.stderr.strip()}')
            elif p.suffix=='.pptx':
                with zipfile.ZipFile(p) as z:
                    bad=z.testzip()
                    if bad: errors.append(f'{rel}: corrupt ZIP member {bad}')
                    for member in z.namelist():
                        if member.endswith(('.xml','.rels')): ET.fromstring(z.read(member))
            checked+=1
        except Exception as exc:
            errors.append(f'{rel}: {exc}')
    print(f'Inspected {checked} project files; parsed {yaml_count} YAML files.')
    if not yaml: print('NOTE: PyYAML unavailable; YAML parsing skipped.')
    if not bash: print('NOTE: Bash unavailable; shell syntax checks skipped.')
    for error in errors: print('ERROR:',error)
    if errors: return 1
    print('PASS: local file links, structured files, available shell syntax and PPTX XML/ZIP checks.')
    return 0

if __name__=='__main__': sys.exit(main())
