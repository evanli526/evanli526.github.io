# coding: utf-8
"""Check only generated public output; no credentials or source drafts are read."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote,urljoin
import re,sys,json
out=Path(sys.argv[1]).resolve();base=sys.argv[2];site=urlsplit(base);prefix=site.path.rstrip('/')
errors=[];checked=0
class Links(HTMLParser):
 def handle_starttag(self,t,a):
  for k,v in a:
   if k in ('href','src') and v: self.links.append(v)
 def __init__(self):super().__init__();self.links=[]
for p in out.rglob('*'):
 if not p.is_file():continue
 if p.suffix in ['.html','.xml','.css','.js','.txt']:
  s=p.read_text()
  if re.search(r'localhost|127\.0\.0\.1|PRIVATE_DRAFT_SENTINEL|BEGIN (?:OPENSSH |RSA )?PRIVATE KEY|HALO_DB_PASSWORD|pat_id_rsa|\.database-password|/Users/',s):errors.append(f'private/local pattern: {p.relative_to(out)}')
 if p.suffix=='.html':
  parser=Links();parser.feed(s)
  for v in parser.links:
   absolute=urlsplit(urljoin(base+str(p.relative_to(out)),v))
   if absolute.netloc and absolute.netloc!=site.netloc:continue
   path=unquote(absolute.path)
   if prefix and not (path==prefix or path.startswith(prefix+'/')):errors.append(f'basepath escape: {v}');continue
   path=path[len(prefix):].lstrip('/')
   target=out/path
   if target.is_dir():target=target/'index.html'
   if not target.exists():errors.append(f'broken {p.relative_to(out)} -> {v}')
   checked+=1
 for name in ['data','.database-password','.env']:
  if name in p.relative_to(out).parts:errors.append(f'forbidden path: {p}')
article=(out/'notes/markdown-demo/index.html').read_text()
for marker in ['<math','<table','<pre','waterside.jpg','TableOfContents']:
 if marker not in article:errors.append('missing renderer '+marker)
assert not errors,'\n'.join(errors)
print(json.dumps({'output':str(out.name),'base_url':base,'internal_links_checked':checked,'private_or_local_patterns':'PASS','markdown_math_code_table_image_toc':'PASS','broken_links':0},ensure_ascii=False))
