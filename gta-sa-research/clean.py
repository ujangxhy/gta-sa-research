import re,sys,glob,os
def clean(p):
    t=open(p).read()
    t=re.sub(r'\[\[([^\]|]*\|)?([^\]]*)\]\]',r'\2',t)
    t=t.replace('\n',' ')
    parts=re.split(r'\{\{line',t)
    out=[]
    for b in parts[1:]:
        b=b.strip().rstrip('}').strip()
        bg=re.search(r'\|background\s*=\s*(.*?)(?=\|\w+\s*=|$)',b)
        nm=re.search(r'\|\s*name\s*=\s*(.*?)(?=\|dialogue\s*=|$)',b)
        dl=re.search(r'\|\s*dialogue\s*=\s*(.*)$',b)
        nm=re.sub(r'\|.*','',nm.group(1)).strip() if nm else '?'
        dl=dl.group(1).strip().rstrip('}') if dl else None
        if bg and dl: out.append('  (scene) '+bg.group(1).strip()[:260])
        if dl: out.append(f'{nm}: {dl}')
        elif bg: out.append('  (scene) '+bg.group(1).strip()[:260])
    return '\n'.join(out) if out else t[:1500]
for pat in sys.argv[1:]:
    for f in sorted(glob.glob('raw/'+pat)):
        print('\n########',os.path.basename(f))
        print(clean(f))
