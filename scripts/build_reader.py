#!/usr/bin/env python3
"""Build an offline single-file reader from canonical Markdown and PNGs.

Dependency: markdown-it-py (see requirements-docs.txt). No network or tracking.
"""
from __future__ import annotations
import base64
import html
import mimetypes
from pathlib import Path
import re
import sys
from urllib.parse import unquote,urlsplit
try:
    from markdown_it import MarkdownIt
except ImportError:
    raise SystemExit('Install reader dependency: python3 -m pip install -r requirements-docs.txt')
from doc_utils import digest_sources,markdown_files,slug
ROOT=Path(__file__).resolve().parents[1]
def doc_id(path:Path)->str:
    return 'doc-'+re.sub(r'[^a-z0-9-]','-',str(path.relative_to(ROOT)).lower())
def ordered_docs()->list[Path]:
    first=[ROOT/'README.md',ROOT/'READING-GUIDE.md']
    chapters=sorted((ROOT/'book').glob('*.md'))
    rest=[p for p in markdown_files(ROOT) if p not in first+chapters]
    # The full historical archive is included at the end, explicitly historical.
    return first+chapters+sorted(rest,key=lambda p:(p.parts[-2]=='archive',str(p)))
def render_doc(path:Path,available:set[Path])->str:
    parser=MarkdownIt('commonmark',{'html':True}).enable('table')
    text=path.read_text();tokens=parser.parse(text);prefix=doc_id(path);counts={}
    for index,token in enumerate(tokens):
        if token.type=='heading_open':
            label=tokens[index+1].content
            base=slug(label);count=counts.get(base,0);counts[base]=count+1
            token.attrSet('id',prefix+'-'+base+(f'-{count}' if count else ''))
        for child in token.children or []:
            if child.type=='image':
                src=child.attrGet('src') or '';parts=urlsplit(src)
                if not parts.scheme:
                    dest=(path.parent/unquote(parts.path)).resolve()
                    if dest.exists() and dest.suffix in ('.png','.svg','.jpg'):
                        mime=mimetypes.guess_type(dest.name)[0] or 'application/octet-stream'
                        child.attrSet('src',f'data:{mime};base64,'+base64.b64encode(dest.read_bytes()).decode())
            if child.type=='link_open':
                href=child.attrGet('href') or '';parts=urlsplit(href)
                if not parts.scheme and not parts.netloc:
                    dest=(path.parent/unquote(parts.path)).resolve() if parts.path else path.resolve()
                    if dest in available:
                        target=doc_id(dest)+(('-'+unquote(parts.fragment)) if parts.fragment else '')
                        child.attrSet('href','#'+target)
                    elif dest==ROOT/'index.html':child.attrSet('href','#top')
                    elif dest.is_file():
                        # Small source files remain inspectable even in the single HTML.
                        mime=mimetypes.guess_type(dest.name)[0] or 'text/plain'
                        child.attrSet('href',f'data:{mime};base64,'+base64.b64encode(dest.read_bytes()).decode())
                        child.attrSet('download',dest.name)
    rendered=parser.renderer.render(tokens,parser.options,{})
    rendered=re.sub(r'<a id="([^"]+)"',lambda m:f'<a id="{prefix}-{html.escape(m.group(1))}"',rendered)
    return rendered
CSS='''
:root{color-scheme:light;--ink:#203044;--muted:#52657a;--line:#dbe2e9;--accent:#234d78}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f6f8fa;color:var(--ink);font:18px/1.7 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
header,main,footer{max-width:920px;margin:auto;padding:28px}header{padding-top:48px}header h1{font-size:2.7rem;line-height:1.12;margin:.5em 0}header p{color:var(--muted)}
article{background:white;padding:34px;border:1px solid var(--line);border-radius:12px;margin:24px 0 44px;overflow-wrap:anywhere;scroll-margin-top:16px}
h1{font-size:2rem;line-height:1.2}h2{font-size:1.45rem;margin-top:1.8em;line-height:1.3}h3{font-size:1.13rem;margin-top:1.6em}h4{font-size:1rem}
a{color:var(--accent);text-decoration-thickness:1px;text-underline-offset:3px}a:hover{text-decoration-thickness:2px}img{display:block;max-width:100%;height:auto;margin:24px auto}pre{overflow-x:auto;background:#f3f5f8;padding:18px;border-radius:8px;font:14px/1.55 ui-monospace,Menlo,Consolas,monospace;white-space:pre}
code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.86em;background:#f0f3f6;padding:.13em .23em;border-radius:3px}pre code{background:transparent;padding:0;font-size:inherit}blockquote{margin:22px 0;padding:4px 20px;border-left:4px solid #6c86a3;background:#f5f8fb}table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%;font-size:.9em;line-height:1.55;margin:22px 0}td,th{border:1px solid var(--line);padding:11px 13px;min-width:130px;vertical-align:top;text-align:left}th{background:#eff3f7}hr{border:0;border-top:1px solid var(--line);margin:28px 0}
summary{cursor:pointer;font-weight:650}details{background:white;border:1px solid var(--line);border-radius:8px;padding:14px 18px;margin:14px 0}nav ul{padding-left:22px}nav li{margin:6px 0}.path{font:12px/1.5 ui-monospace,monospace;color:var(--muted);margin-bottom:22px}.back{font-size:14px}footer{font-size:14px;color:var(--muted)}
@media(max-width:600px){body{font-size:17px}header,main,footer{padding:16px}header{padding-top:24px}header h1{font-size:2.15rem}article{padding:20px 16px;margin:14px 0 28px;border-radius:8px}h1{font-size:1.7rem}h2{font-size:1.3rem}pre{font-size:12px;padding:12px}img{margin:16px auto}table{font-size:.82em}td,th{min-width:140px;padding:8px}}
@media print{body{background:white;font-size:11pt}header,main,footer{max-width:none;padding:0}article{border:0;padding:0;page-break-before:always}nav,.back{display:none}pre{white-space:pre-wrap}table{display:table}a{color:inherit}}
'''
def main()->int:
    docs=ordered_docs();available=set(docs)
    groups=[('Start here',[p for p in docs if p.parent==ROOT]),('The book',[p for p in docs if p.parent==ROOT/'book']),
      ('Examples',[p for p in docs if 'examples' in p.relative_to(ROOT).parts]),
      ('Research and sources',[p for p in docs if 'research' in p.relative_to(ROOT).parts]),
      ('Templates and experiments',[p for p in docs if set(p.relative_to(ROOT).parts)&{'templates','experiments'}]),
      ('Diagrams and historical archive',[p for p in docs if set(p.relative_to(ROOT).parts)&{'diagrams','archive'}])]
    toc=[]
    for label,paths in groups:
        links=[]
        for p in paths:
            title=next((line.lstrip('# ').strip() for line in p.read_text().splitlines() if line.startswith('# ')),p.stem)
            links.append(f'<li><a href="#{doc_id(p)}">{html.escape(title)}</a></li>')
        toc.append(f'<details{(" open" if label=="The book" else "")}><summary>{label}</summary><ul>'+''.join(links)+'</ul></details>')
    content=[]
    for path in docs:
        content.append(f'<article id="{doc_id(path)}"><div class="path">{html.escape(str(path.relative_to(ROOT)))}</div>'+render_doc(path,available)+'<p class="back"><a href="#top">Back to contents</a></p></article>')
    output='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'+f'<meta name="source-digest" content="{digest_sources(ROOT)}">'+ '<title>Beyond Code Generation — Research Book</title><style>'+CSS+'</style></head><body><header id="top"><p>SOFTWARE FACTORY RESEARCH · FIRST EDITION</p><h1>Beyond Code Generation</h1><p>Customer outcomes. Human judgment. Maintainable change.</p><p>By Sabir Moglad · AI-assisted research and synthesis · October 17, 2026</p><p>A complete offline reading edition. Proposals, source positions, and executed checks are distinguished throughout. No factory-effectiveness or customer trial is claimed.</p><nav aria-label="Book contents">'+''.join(toc)+'</nav></header><main>'+''.join(content)+'</main><footer>Generated from canonical Markdown. No external fonts, scripts, tracking, or assets. The source repository includes editable diagrams, tests, and publishing instructions.</footer></body></html>'
    (ROOT/'index.html').write_text(output)
    print(f'Built offline reader with {len(docs)} documents ({len(output.encode()):,} bytes).')
    return 0
if __name__=='__main__':raise SystemExit(main())
