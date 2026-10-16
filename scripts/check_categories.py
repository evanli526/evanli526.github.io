# coding: utf-8
"""Build isolated subject-category fixtures; nothing is added to public content."""
from pathlib import Path
import shutil,subprocess,json,re,hashlib
from html.parser import HTMLParser
r=Path(__file__).resolve().parents[1];work=r/'runtime/category-fixture';out=r/'runtime/category-output'
before={str(p.relative_to(r)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (r/'content').rglob('*.md')}
if work.exists():shutil.rmtree(work)
shutil.copytree(r,work,ignore=shutil.ignore_patterns('runtime','public','resources','.git'))
fixtures={'none':[],'one':['大模型'],'many':['大模型','数据结构与算法']}
for name,categories in fixtures.items():
 text='---\ntitle: "分类验收 '+name+'"\ndate: 2026-01-01\nslug: qa-'+name+'\ncategories: '+json.dumps(categories,ensure_ascii=False)+'\ndraft: false\n---\n\n仅用于本地分类布局验收。\n'
 (work/'content/notes'/('qa-'+name+'.md')).write_text(text)
reports={}
class Cards(HTMLParser):
 def __init__(self):super().__init__();self.cards=[];self.card=None;self.depth=0;self.in_categories=0;self.label=False
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='article' and a.get('class')=='entry':self.card={'categories':[],'text':'','classes':[]};self.depth=1
  elif self.card is not None:
   if t=='div':
    if a.get('class')=='entry-categories':self.in_categories=1
    elif self.in_categories:self.in_categories+=1
   if t=='a':self.label=a.get('class')=='category-link'
   self.card['classes'].append(a.get('class',''))
 def handle_data(self,s):
  if self.card is not None:
   self.card['text']+=s
   if self.label:self.card['categories'].append(s)
 def handle_endtag(self,t):
  if t=='a':self.label=False
  if t=='div' and self.in_categories:self.in_categories-=1
  if t=='article' and self.card is not None:self.cards.append(self.card);self.card=None
for name,base in [('root','https://evanli526.github.io/'),('project','https://evanli526.github.io/senyang/')]:
 dest=out/name
 subprocess.run([str(r/'runtime/hugo'),'--source',str(work),'--destination',str(dest),'--baseURL',base,'--cacheDir',str(r/'runtime/cache'),'--minify'],check=True,capture_output=True)
 subprocess.run(['python3',str(r/'scripts/check_output.py'),str(dest),base],check=True,capture_output=True)
 p=Cards();html=(dest/'index.html').read_text();p.feed(html)
 for label,expected in fixtures.items():
  card=next(c for c in p.cards if '分类验收 '+label in c['text']);assert card['categories']==expected,(label,card)
  assert ('entry-categories' in card['classes'])==bool(expected)
 for card in p.cards:assert '演示内容' not in re.sub(r'分类验收.*','',card['text']) or '（演示内容）' in card['text']
 assert not any(x in html for x in ['A PERSONAL SPACE','EVERYDAY','把想法记下来','一页一页','慢慢阅读','慢慢写','慢慢想','笔记与日常，慢慢记录。','留一点时间','在这里收集想法'])
 assert '轻身逐燕' in html and 'Utopia' in html
 for f in dest.rglob('*.html'):
  s=f.read_text();assert not re.search(r'<span>演示内容</span>',s)
 reports[name]={'none':'PASS','one':'PASS','many':'PASS','category_routes':'PASS','internal_links':'PASS','removed_template_copy':'PASS'}
assert all(hashlib.sha256((r/path).read_bytes()).hexdigest()==digest for path,digest in before.items())
reports['existing_markdown_and_slugs']='UNCHANGED by category fixtures';reports['fixtures']='runtime only, excluded from publication'
(r/'runtime/categories-verification.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2));print(json.dumps(reports,ensure_ascii=False,indent=2))
