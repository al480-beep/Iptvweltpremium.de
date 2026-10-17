"""Technical and on-page SEO audit of every HTML file: python3 tools/seo/audit_site.py [repo root]
Checks title/description/canonical/hreflang/OG/Twitter, sitemap, headings, ids, internal links, JSON-LD and FAQ visibility.
Noindex pages (404, checkout, impressum, datenschutz) are expected to show missing social tags."""
import os,re,json,sys,glob,html
from html.parser import HTMLParser
from collections import defaultdict,Counter
R=sys.argv[1] if len(sys.argv)>1 else os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'); os.chdir(R)
files=sorted(glob.glob('**/*.html',recursive=True))
files=[f for f in files if not f.startswith('.git')]
def url_of(f):
    if f=='index.html': return '/'
    if f.endswith('/index.html'): return '/'+f[:-10]
    return '/'+f[:-5]
sitemap=set(re.findall(r'<loc>https://iptvweltpremium.de([^<]*)</loc>',open('sitemap.xml').read()))
redir=open('_redirects').read()
urls={url_of(f) for f in files}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.heads=[]; s.cur=None; s.txt=[]; s.links=[]; s.ids=[]; s.in_script=False; s.scripts=[]; s.sbuf=''; s.stype=None; s.body=False; s.skip=0; s.ps=[]; s.inp=False; s.pbuf=''; s.headtags=[];s.in_head=True
    def handle_starttag(s,t,a):
        a=dict(a)
        if t=='body': s.in_head=False
        if s.in_head and t in('script','link'): s.headtags.append((t,a))
        if 'id' in a: s.ids.append(a['id'])
        if t in('h1','h2','h3','h4'): s.cur=[t,'']
        if t=='a' and a.get('href'): s.links.append(a['href'])
        if t=='script': s.in_script=True; s.stype=a.get('type'); s.sbuf=''
        if t in('style','noscript'): s.skip+=1
        if t=='p': s.inp=True; s.pbuf=''
    def handle_endtag(s,t):
        if s.cur and t==s.cur[0]: s.heads.append((s.cur[0],s.cur[1].strip())); s.cur=None
        if t=='script':
            s.in_script=False
            if s.stype=='application/ld+json': s.scripts.append(s.sbuf)
        if t in('style','noscript'): s.skip-=1
        if t=='p' and s.inp: s.ps.append(s.pbuf); s.inp=False
    def handle_data(s,d):
        if s.in_script: s.sbuf+=d; return
        if s.skip: return
        if s.cur: s.cur[1]+=d
        if s.inp: s.pbuf+=d
        if not s.in_head: s.txt.append(d)
res={}; titles=defaultdict(list); descs=defaultdict(list)
for f in files:
    h=open(f,encoding='utf-8').read(); u=url_of(f); p=P(); p.feed(h)
    iss=[]
    m=re.findall(r'<title>(.*?)</title>',h,re.S)
    t=html.unescape(m[0]) if m else ''
    if len(m)!=1: iss.append(f'title count {len(m)}')
    elif not (30<=len(t)<=65): iss.append(f'title len {len(t)}')
    titles[t].append(u)
    d=re.findall(r'<meta name="description" content="(.*?)"',h)
    dd=html.unescape(d[0]) if d else ''
    if len(d)!=1: iss.append(f'desc count {len(d)}')
    elif not (120<=len(dd)<=160): iss.append(f'desc len {len(dd)}')
    descs[dd].append(u)
    c=re.findall(r'<link rel="canonical" href="(.*?)"',h)
    noindex='noindex' in (re.findall(r'<meta name="robots" content="(.*?)"',h) or [''])[0]
    if len(c)!=1: iss.append('canonical count %d'%len(c))
    elif c[0]!='https://iptvweltpremium.de'+u: iss.append('canonical mismatch '+c[0])
    hl=re.findall(r'<link rel="alternate" hreflang="(.*?)" href="(.*?)"',h)
    if not hl: iss.append('no hreflang')
    for k in ['og:title','og:description','og:url','og:image','og:type']:
        if f'property="{k}"' not in h: iss.append('missing '+k)
    for k in ['twitter:card','twitter:title','twitter:description','twitter:image']:
        if f'name="{k}"' not in h: iss.append('missing '+k)
    if not noindex and u not in sitemap: iss.append('not in sitemap')
    if noindex and u in sitemap: iss.append('noindex in sitemap')
    h1=[x for x in p.heads if x[0]=='h1']
    if len(h1)!=1: iss.append(f'h1 count {len(h1)}')
    lvl=0
    for tg,_ in p.heads:
        n=int(tg[1])
        if lvl and n>lvl+1: iss.append(f'heading skip {lvl}->{n}'); break
        lvl=n
    if p.heads and p.heads[0][0]!='h1': iss.append('first heading '+p.heads[0][0])
    words=len(re.findall(r'\w+',' '.join(p.txt)))
    dup=[k for k,v in Counter(p.ids).items() if v>1]
    if dup: iss.append('dup ids '+','.join(dup))
    for l in p.links:
        if l.startswith(('http','mailto','tel','#','javascript')):continue
        path=l.split('#')[0].split('?')[0]
        if not path: continue
        if path.startswith('/assets') or path.startswith('/api'):
            if path.startswith('/assets') and not os.path.exists('.'+path): iss.append('dead asset '+path)
            continue
        if path not in urls and not re.search(r'^'+re.escape(path)+r'\s',redir,re.M): iss.append('dead link '+l)
    ext=[l for l in p.links if l.startswith('http') and 'iptvweltpremium' not in l]
    types=[]
    for s in p.scripts:
        try:
            j=json.loads(s)
        except Exception as e: iss.append('JSON-LD error '+str(e)); continue
        def walk(o):
            if isinstance(o,dict):
                if '@type' in o: types.append(o['@type'] if isinstance(o['@type'],str) else '/'.join(o['@type']))
                for v in o.values(): walk(v)
            elif isinstance(o,list):
                for v in o: walk(v)
        walk(j)
        # faq match
        def faqs(o):
            if isinstance(o,dict):
                if o.get('@type')=='FAQPage':
                    for q in o.get('mainEntity',[]):
                        qn=html.unescape(q['name'])
                        vis=html.unescape(re.sub('<[^>]+>','',h))
                        if qn not in vis.replace('\n',' ') and qn not in vis: iss.append('faq q not visible: '+qn[:40])
                for v in o.values(): faqs(v)
            elif isinstance(o,list):
                for v in o: faqs(v)
        faqs(j)
    bl=[t for t,a in p.headtags if t=='script' and 'src' in a and 'defer' not in a and 'async' not in a]
    if bl: iss.append('render-blocking script')
    fp=next((x for x in p.ps if len(x.strip())>60),'')
    res[u]=dict(f=f,iss=iss,words=words,types=sorted(set(types)),ext=len(ext),noindex=noindex,int=len([l for l in p.links if l.startswith('/') and not l.startswith('/assets')]),h1=h1[0][1] if h1 else '',fp=fp[:200],title=t)
for t,v in titles.items():
    if len(v)>1:
        for u in v: res[u]['iss'].append('dup title')
for t,v in descs.items():
    if len(v)>1:
        for u in v: res[u]['iss'].append('dup desc')
for u,r in res.items():
    if r['noindex'] or u in('/404','/checkout/'): pass
    print(f"{u:32} w={r['words']:5} int={r['int']:3} ext={r['ext']:2} ni={int(r['noindex'])} {','.join(r['types'])}")
    for i in r['iss']: print('    -',i)
for s in sitemap-urls: print('sitemap url without file',s)
