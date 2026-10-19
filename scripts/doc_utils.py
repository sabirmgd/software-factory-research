"""Small shared utilities for this repository's explicit Markdown conventions."""
from __future__ import annotations
import hashlib
import re
from pathlib import Path

EXCLUDED = {'.git', '.build', '__pycache__', '.venv', 'node_modules'}
def markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob('*.md') if not any(x in EXCLUDED for x in p.relative_to(root).parts))
def strip_fences(text: str) -> str:
    lines=[]; fence=None
    for line in text.splitlines():
        match=re.match(r'^\s*(`{3,}|~{3,})',line)
        if match:
            run=match.group(1)
            if fence is None:fence=run
            elif run[0]==fence[0] and len(run)>=len(fence):fence=None
            lines.append('');continue
        lines.append('' if fence else line)
    return '\n'.join(lines)
def slug(text: str) -> str:
    text=re.sub(r'<[^>]*>', '', text)
    text=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',text)
    text=re.sub(r'[^\w\s-]','',text.lower(),flags=re.UNICODE)
    return re.sub(r'\s','-',text.strip())
def anchors(text: str) -> set[str]:
    clean=strip_fences(text);result=set(re.findall(r'<a\s+id=["\']([^"\']+)["\']',clean));counts={}
    for match in re.finditer(r'^#{1,6}\s+(.+?)\s*#*\s*$',clean,re.MULTILINE):
        base=slug(match.group(1));count=counts.get(base,0)
        result.add(base+(f'-{count}' if count else ''));counts[base]=count+1
    return result
LINK_RE=re.compile(r'!?\[([^\]]*)\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"\n]*")?\)')
def digest_sources(root:Path)->str:
    """All distributable inputs, including downloadable evidence and source files.

    Generated index.html and local caches are deliberately excluded.
    """
    files=[p for p in root.rglob('*') if p.is_file() and p.name != 'index.html'
           and not any(x in EXCLUDED for x in p.relative_to(root).parts)]
    hasher=hashlib.sha256()
    for p in sorted(files):
        hasher.update(str(p.relative_to(root)).encode());hasher.update(b'\0');hasher.update(p.read_bytes());hasher.update(b'\0')
    return hasher.hexdigest()
