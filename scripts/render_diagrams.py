#!/usr/bin/env python3
"""Render canonical JSON graphs to editable Mermaid/DOT and static SVG/PNG.

Requires Graphviz's `dot` binary. No network requests or external images.
"""
from __future__ import annotations
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import textwrap

ROOT = Path(__file__).resolve().parents[1]
PALETTE = {
    'human': ('#e9effb', '#355484'),
    'contract': ('#eeeafa', '#6c5599'),
    'work': ('#f2f4f7', '#596678'),
    'evidence': ('#e5f2ed', '#337361'),
    'warning': ('#fff0df', '#a56b26'),
}
def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()
def validate(graph: dict) -> None:
    ids = [node['id'] for node in graph['nodes']]
    if len(ids) != len(set(ids)) or any(not re.fullmatch(r'[A-Za-z][A-Za-z0-9_]*', id_) for id_ in ids):
        raise ValueError('Diagram node IDs must be unique safe identifiers')
    if any(edge['from'] not in ids or edge['to'] not in ids for edge in graph['edges']):
        raise ValueError('Diagram edge references an unknown node')
def mermaid(graph: dict) -> str:
    lines = ['%% Generated from ' + graph['id'] + '.json; edit the JSON source.', 'flowchart TD']
    for node in graph['nodes']:
        label = html.escape(node['label'].replace('\n', '<br/>'), quote=True).replace('&lt;br/&gt;', '<br/>')
        lines.append(f'    {node["id"]}["{label}"]')
    for edge in graph['edges']:
        label = html.escape(edge.get('label',''), quote=True)
        lines.append(f'    {edge["from"]} -->' + (f'|"{label}"|' if label else '') + f' {edge["to"]}')
    return '\n'.join(lines) + '\n'
def dot(graph: dict) -> str:
    q = lambda text: json.dumps(text,ensure_ascii=False)
    wrap = lambda text, width: '\n'.join(textwrap.fill(line,width=width,break_long_words=False) for line in text.split('\n'))
    lines = ['digraph G {', 'graph [rankdir=TB, bgcolor="white", pad="0.3", nodesep="0.28", ranksep="0.46", splines=polyline, dpi=144];',
      'node [shape=box, style="rounded,filled", fontname="DejaVu Sans", fontsize=16, group="main", margin="0.18,0.16", penwidth=1.4];',
      'edge [fontname="DejaVu Sans", fontsize=11, color="#788495", fontcolor="#445166", arrowsize=0.7];',
      f'labelloc=t; label={q(wrap(graph["title"],34))}; fontname="DejaVu Sans"; fontsize=21; fontcolor="#182b42";']
    for node in graph['nodes']:
        fill, border = PALETTE[node['kind']]
        lines.append(f'{node["id"]} [label={q(wrap(node["label"],30))}, fillcolor="{fill}", color="{border}", fontcolor="#17283c"];')
    for first, second in zip(graph['nodes'],graph['nodes'][1:]):
        lines.append(f'{first["id"]} -> {second["id"]} [style=invis, weight=100];')
    for edge in graph['edges']:
        lines.append(f'{edge["from"]} -> {edge["to"]} [constraint=false, label={q(wrap(edge.get("label",""),18))}];')
    return '\n'.join(lines+['}'])+'\n'
def main() -> int:
    binary=shutil.which('dot')
    if not binary:
        print('Graphviz is required: install its dot command, then rerun.',file=sys.stderr);return 1
    out=ROOT/'diagrams/rendered';out.mkdir(parents=True,exist_ok=True)
    manifest=[]
    for path in sorted((ROOT/'diagrams/source').glob('*.json')):
        graph=json.loads(path.read_text());validate(graph)
        path.with_suffix('.mmd').write_text(mermaid(graph))
        path.with_suffix('.dot').write_text(dot(graph))
        outputs=[path.with_suffix('.mmd'),path.with_suffix('.dot')]
        for ext in ('svg','png'):
            dest=out/f'{path.stem}.{ext}'
            subprocess.run([binary,f'-T{ext}',str(path.with_suffix('.dot')),'-o',str(dest)],check=True,timeout=30)
            if ext=='svg':
                text=dest.read_text()
                pos=text.index('>',text.index('<svg'))+1
                text=text[:pos]+f'\n<title>{html.escape(graph["title"])}</title><desc>{html.escape(graph["caption"])}</desc>\n'+text[pos:]
                dest.write_text(text)
            outputs.append(dest)
        manifest.append({'id':graph['id'],'source':str(path.relative_to(ROOT)),'source_sha256':sha(path),
          'outputs':{str(p.relative_to(ROOT)):sha(p) for p in outputs}})
    (ROOT/'diagrams/manifest.json').write_text(json.dumps({'generator':'scripts/render_diagrams.py',
        'canonical':'JSON source','rendering':'Graphviz dot; Mermaid exported, not rendered by mmdc',
        'diagrams':manifest},indent=2)+'\n')
    print(f'Rendered {len(manifest)} diagrams to SVG/PNG with Mermaid/DOT exports.')
    return 0
if __name__=='__main__':raise SystemExit(main())
