import sys,os,re,subprocess
sys.path.insert(0,'/home/user/gta-sa-research')
from fetch import parse_wikitext
pages=open('pages.txt').read().split('\n')
for p in pages:
    p=p.strip()
    if not p: continue
    f='raw/'+re.sub(r'[^A-Za-z0-9]+','_',p)+'.txt'
    if os.path.exists(f) and os.path.getsize(f)>20: 
        print('cached',p); continue
    t=parse_wikitext(p)
    if t: open(f,'w').write(t); print('OK',p,len(t))
    else: print('MISS',p)
