import re,sys,glob,os
sys.path.insert(0,'/home/user/gta-sa-research')
exec(open('/home/user/gta-sa-research/clean.py').read().split('for pat')[0])
for f in sys.argv[1:]:
    print('\n########',os.path.basename(f))
    print(clean(f))
