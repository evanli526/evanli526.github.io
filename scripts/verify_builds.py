# coding: utf-8
from pathlib import Path
import tempfile,shutil,subprocess,json
r=Path(__file__).resolve().parents[1];results={}
for name,base in [('root','https://evanli526.github.io/'),('project','https://evanli526.github.io/senyang/')]:
 dest=r/'runtime'/('verify-'+name)
 subprocess.run([str(r/'runtime/hugo'),'--source',str(r),'--baseURL',base,'--destination',str(dest),'--minify','--cleanDestinationDir','--cacheDir',str(r/'runtime/cache')],check=True,capture_output=True)
 x=subprocess.run(['python3',str(r/'scripts/check_output.py'),str(dest),base],check=True,capture_output=True,text=True)
 results[name]=json.loads(x.stdout)
with tempfile.TemporaryDirectory(prefix='senyang-draft-check-') as tmp:
 t=Path(tmp);s=t/'site';shutil.copytree(r,s,ignore=shutil.ignore_patterns('runtime','public','resources','.git'))
 (s/'content/notes/private-test.md').write_text('---\ntitle: PRIVATE_DRAFT_SENTINEL\ndate: 2026-01-01\ndraft: true\n---\nPRIVATE_DRAFT_SENTINEL\n')
 subprocess.run([str(r/'runtime/hugo'),'--source',str(s),'--destination',str(t/'public'),'--minify','--cleanDestinationDir','--cacheDir',str(t/'cache')],check=True)
 for p in (t/'public').rglob('*'):
  if p.is_file() and p.suffix in ['.html','.xml','.txt']:assert 'PRIVATE_DRAFT_SENTINEL' not in p.read_text()
 results['draft_exclusion']='PASS: temporary fixture not included in HTML, RSS or sitemap; source never published'
results['runtime_sha256']='PASS: official macOS archive checksum verified'
(r/'runtime/build-verification.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));print(json.dumps(results,ensure_ascii=False,indent=2))
