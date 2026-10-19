#!/usr/bin/env python3
"""Optional in-memory Chromium inspection; no navigation to external resources.

Install requirements-visual-check.txt and supply a Chromium binary with
CHROMIUM_PATH, or have chromium/chromium-browser on PATH. Outputs evidence under
experiments/results/evidence. This is not a test of ChatGPT or iOS rendering.
"""
from __future__ import annotations
import json
import os
from pathlib import Path
import shutil
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    raise SystemExit('Install optional requirements-visual-check.txt first.')
ROOT=Path(__file__).resolve().parents[1]
def main()->int:
    binary=os.environ.get('CHROMIUM_PATH') or shutil.which('chromium') or shutil.which('chromium-browser')
    if not binary:raise SystemExit('Set CHROMIUM_PATH to a Chromium browser binary.')
    output=ROOT/'experiments/results/evidence';output.mkdir(parents=True,exist_ok=True)
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path=binary,headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
        page=browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1)
        requests=[];errors=[]
        page.on('request',lambda r:requests.append(r.url) if r.url.startswith(('http://','https://')) else None)
        page.on('pageerror',lambda e:errors.append(str(e)))
        # Loading already-owned HTML avoids dependence on local file URL policies.
        page.set_content((ROOT/'index.html').read_text(),wait_until='load',timeout=30000)
        page.screenshot(path=str(output/'reader-mobile.png'),full_page=False)
        result=page.evaluate('''() => ({
          viewportWidth:innerWidth, documentWidth:document.documentElement.scrollWidth,
          missingImages:[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.alt),
          duplicateIds:[...document.querySelectorAll('[id]')].map(e=>e.id).filter((id,i,all)=>all.indexOf(id)!==i),
          missingAnchors:[...document.querySelectorAll('a[href^="#"]')].map(a=>a.getAttribute('href').slice(1)).filter(id=>id&&!document.getElementById(id)),
          imageCount:document.images.length, articles:document.querySelectorAll('article').length
        })''')
        page.locator('#doc-book-09-make-clear-and-human-understanding-md').evaluate('(e) => e.scrollIntoView()')
        page.screenshot(path=str(output/'reader-chapter-mobile.png'),full_page=False)
        result['externalRequests']=requests;result['pageErrors']=errors
        result['method']='HTML loaded in memory, 390x844 Chromium viewport; no file URL navigation or GitHub/iOS validation'
        (output/'browser-check.json').write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps(result,indent=2));browser.close()
    invalid=bool(result['missingImages'] or result['duplicateIds'] or result['missingAnchors'] or requests or errors or result['documentWidth']>result['viewportWidth'])
    return int(invalid)
if __name__=='__main__':raise SystemExit(main())
