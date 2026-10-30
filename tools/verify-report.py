"""Verify report integrity without dependencies, network, secrets or data writes."""
from pathlib import Path
import argparse
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--api-root', type=Path)
args = parser.parse_args()
errors = []
def check(condition, message):
    if not condition:
        errors.append(message)
def text(path): return path.read_text(encoding='utf-8')
def slug(value):
    value = re.sub(r'<[^>]*>', '', value).lower()
    return ''.join(c for c in value if c.isalnum() or c in ' _-').replace(' ', '-')
def headings(content):
    return [slug(m[1]) for m in re.finditer(r'^#{1,6} (.+)$', content, re.M)]
def no_fences(content): return re.sub(r'^```[^\n]*\n.*?^```\s*$', '', content, flags=re.M|re.S)

chapters = ['01-Chapter-1-Presentation.md', '02-Chapter-2.md', '03-Chapter-3.md', '04-Chapter-4.md', '05-Chapter-5.md', '06-Conclusions.md']
report = text(ROOT/'README.md')
for chapter in chapters:
    check(text(ROOT/chapter).strip() in report, f'Chapter differs from README: {chapter}')

c3 = text(ROOT/'03-Chapter-3.md')
catalogue = c3[:c3.index('## 3.2.')]
expected = {f'US{n:02}' for n in range(1,43)} | {f'TS{n:02}' for n in range(1,36)}
ids = re.findall(r'^\| \*\*((?:US|TS)\d+)\*\* \|', catalogue, re.M)
check(set(ids)==expected and len(ids)==77, 'Story catalogue has missing or duplicate IDs')
epics = re.findall(r'^\| \*\*(EPIC-\d+)\*\* \|', catalogue, re.M)
check(len(epics)==10 and len(set(epics))==10, 'Expected ten unique epics')
backlog = re.findall(r'^\| (\d+) \| ((?:US|TS)\d+) \| (US|TS) \| (.*?) \| (.*?) \| (.*?) \| (.*?) \|$', c3[c3.index('## 3.3.'):], re.M)
check(len(backlog)==77 and {b[1] for b in backlog}==expected, 'Backlog has missing or duplicate IDs')
check([int(b[0]) for b in backlog]==list(range(1,78)), 'Backlog priority order is not consecutive')
check(sum(int(b[5]) for b in backlog if b[2]=='US')==139, 'US estimates do not sum to 139 SP')

for file in ROOT.rglob('*.md'):
    if '.git' in file.parts: continue
    content = text(file)
    check(len(re.findall(r'^```', content, re.M))%2==0, f'Unbalanced code fences: {file.relative_to(ROOT)}')
    clean = no_fences(content)
    lines = clean.splitlines()
    # A blank line breaks a GFM table; every pipe block must have its own header.
    i=0
    while i<len(lines):
        if not lines[i].lstrip().startswith('|'):
            i+=1; continue
        block=[]
        while i<len(lines) and lines[i].lstrip().startswith('|'):
            block.append(lines[i]); i+=1
        check(len(block)>=2 and bool(re.fullmatch(r'\s*\|(?:\s*:?-+:?\s*\|)+\s*', block[1])), f'Orphan table rows: {file.relative_to(ROOT)}: {block[0][:60]}')
        counts=[len(re.split(r'(?<!\\)\|', row))-2 for row in block]
        check(len(set(counts))==1, f'Table column mismatch: {file.relative_to(ROOT)}: {block[0][:60]}')
    check(not re.search(r'^#!\[', clean, re.M), f'Malformed image heading: {file.relative_to(ROOT)}')
    links=re.findall(r'\]\(([^)]+)\)',clean)+re.findall(r'(?:src|href)="([^"]+)"',clean)
    for link in links:
        if re.match(r'^(?:https?:|mailto:|data:)',link): continue
        from urllib.parse import unquote
        path,sep,anchor=unquote(link).partition('#')
        target=(file.parent/path).resolve() if path else file
        check(target.exists(), f'Missing local target: {file.relative_to(ROOT)} -> {link}')
        if target.exists() and anchor and target.suffix=='.md':
            targets=headings(text(target))+re.findall(r'<a id="([^"]+)"',text(target))
            check(anchor in targets, f'Missing anchor: {file.relative_to(ROOT)} -> {link}')

sources=list((ROOT/'diagrams').glob('*.mmd'))
check(len(sources)==21, 'Expected 21 editable diagram sources')
for source in sources:
    image=source.with_suffix('.svg')
    check(image.exists(), f'Missing SVG: {source.name}')
    if not image.exists(): continue
    try:
        svg=ET.fromstring(text(image))
        check(svg.tag.endswith('svg') and 'viewBox' in svg.attrib, f'Invalid SVG root: {image.name}')
        check(not any(n.tag.endswith('script') for n in svg.iter()), f'Script embedded in SVG: {image.name}')
    except ET.ParseError as exc:
        errors.append(f'Invalid SVG XML: {image.name}: {exc}')

dictionary=text(ROOT/'AV2/diccionario-datos.md')
tables=re.findall(r'<summary><strong>([^<]+)</strong>', dictionary)
check(len(tables)==35 and len(set(tables))==35, 'Dictionary must describe 35 distinct tables')
if args.api_root:
    sql=text(args.api_root/'schema.sql')
    physical={t:re.findall(r'^    "([^"]+)"',body,re.M) for t,body in re.findall(r'CREATE TABLE public\."([^"]+)" \((.*?)\n\);',sql,re.S)}
    check(set(tables)==set(physical), 'Dictionary table names differ from API SQL')
    for table,columns in physical.items():
        block=dictionary.split(f'<summary><strong>{table}</strong>',1)[-1].split('</details>',1)[0]
        actual=re.findall(r'^\| `([^`]+)` \|',block,re.M)
        check(actual==columns, f'Dictionary columns differ: {table}')
    relations=re.findall(r'ALTER TABLE ONLY public\."([^"]+)"\s+ADD CONSTRAINT "[^"]+" FOREIGN KEY \(([^)]+)\) REFERENCES public\."([^"]+)"\(([^)]+)\)',sql,re.S)
    full=text(ROOT/'diagrams/er-complete.mmd')
    actual=re.findall(r'^\s+(\w+) \|\|--o[|{] (\w+) : "([^"]+)"',full,re.M)
    wanted=[(pri,dep,re.findall(r'"([^"]+)"',cols)[-1]) for dep,cols,pri,refs in relations]
    check(sorted(actual)==sorted(wanted), 'Complete ER relationships differ from API SQL')
    check(sum(map(len,physical.values()))==182, 'Review the documented 182-column count')

if errors:
    print('\n'.join('FAIL '+e for e in errors))
    sys.exit(1)
print('PASS: chapters synchronized; 10 epics; 42 US; 35 TS; 77 backlog entries; 139 SP; tables, links, 21 SVG/source pairs and 35 dictionary tables valid.' + (' API SQL matched.' if args.api_root else ''))
