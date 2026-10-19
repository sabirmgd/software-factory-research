#!/usr/bin/env python3
"""Offline integrity checks, not fact checking or a full Markdown specification."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
from doc_utils import LINK_RE, anchors, digest_sources, markdown_files, strip_fences

ROOT=Path(__file__).resolve().parents[1]
def check_links(path:Path,root:Path)->list[str]:
    failures=[]
    for match in LINK_RE.finditer(strip_fences(path.read_text())):
        target=match.group(2).strip('<>');parts=urlsplit(target)
        if parts.scheme or parts.netloc:continue
        relative=unquote(parts.path)
        if relative.startswith('/'):
            failures.append(f'{path.relative_to(root)}: root-absolute link unsupported: {target}');continue
        dest=(path.parent/relative).resolve() if relative else path.resolve()
        try:dest.relative_to(root.resolve())
        except ValueError:
            failures.append(f'{path.relative_to(root)}: link escapes repository: {target}');continue
        if not dest.exists():
            failures.append(f'{path.relative_to(root)}: missing target {target}');continue
        if parts.fragment and dest.suffix=='.md' and unquote(parts.fragment) not in anchors(dest.read_text()):
            failures.append(f'{path.relative_to(root)}: missing anchor {target}')
    return failures

def validate(root:Path, check_reader:bool=True)->tuple[list[str],dict]:
    failures=[];docs=markdown_files(root)
    for path in docs:
        failures.extend(check_links(path,root))
        if not path.read_text().strip():failures.append(f'Empty document: {path.relative_to(root)}')
        # Deliberately narrow secret checks; not a replacement for a production scanner.
        if re.search(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{36,}',path.read_text()):
            failures.append(f'Possible credential material in {path.relative_to(root)}; inspect without printing it')
    for path in root.rglob('*.json'):
        if any(x in {'.git','.build','node_modules'} for x in path.parts):continue
        try:json.loads(path.read_text())
        except (ValueError,UnicodeError) as error:failures.append(f'Invalid JSON: {path.relative_to(root)}: {error}')
    chapters=sorted((root/'book').glob('*.md'))
    if len(chapters)!=13:failures.append(f'Expected 13 chapters, found {len(chapters)}')
    for chapter in chapters:
        if len(chapter.read_text().split())<600:failures.append(f'Chapter too short for this edition: {chapter.name}')
    try:
        sources=json.loads((root/'research/sources/manifest.json').read_text())
        ids=[s['id'] for s in sources]
        if len(ids)!=len(set(ids)):failures.append('Duplicate source IDs')
        ledger=anchors((root/'research/sources/index.md').read_text())
        for source in sources:
            if source['id'].lower() not in ledger:failures.append(f'Missing ledger anchor for {source["id"]}')
            if not source['url'].startswith('https://'):failures.append(f'Unexpected source URL: {source["id"]}')
        manifest=json.loads((root/'diagrams/manifest.json').read_text())
        for diagram in manifest['diagrams']:
            expected={diagram['source']:diagram['source_sha256'],**diagram['outputs']}
            for relative,sha in expected.items():
                p=root/relative
                if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=sha:
                    failures.append(f'Stale or missing diagram artifact: {relative}')
    except (OSError,ValueError,KeyError) as error:
        failures.append(f'Invalid or incomplete manifest: {error}')
    if check_reader:
        reader=root/'index.html'
        if not reader.exists():failures.append('Missing offline reader: run scripts/build_reader.py')
        elif f'name="source-digest" content="{digest_sources(root)}"' not in reader.read_text():
            failures.append('Offline reader is stale: run scripts/build_reader.py')
    return failures,{'markdown_documents':len(docs),'chapters':len(chapters),
        'chapter_words':sum(len(p.read_text().split()) for p in chapters),
        'json_diagrams':len(list((root/'diagrams/source').glob('*.json')))}

def main()->int:
    errors,stats=validate(ROOT,'--skip-reader' not in sys.argv)
    if errors:
        for e in errors:print('FAIL:',e,file=sys.stderr)
        return 1
    print('PASS: offline documentation integrity; '+json.dumps(stats,sort_keys=True))
    print('Scope: local links/anchors, chapter completeness, source-ledger shape, diagram hashes, reader freshness. No remote link or factual validation.')
    return 0
if __name__=='__main__':raise SystemExit(main())
