import sys,urllib.parse,subprocess,json,re
def get(title):
    u="https://tcrf.net/api.php?"+urllib.parse.urlencode({"action":"parse","page":title,"prop":"wikitext","format":"json","redirects":"1"})
    o=subprocess.run(["curl","-s","-m","40","-A","Mozilla/5.0 (X11; Linux x86_64)","--compressed",u],capture_output=True,text=True).stdout
    try:
        d=json.loads(o)
        return d["parse"]["wikitext"]["*"]
    except Exception as e:
        return "ERR "+str(e)+" "+o[:300]
t=get(sys.argv[1])
open('raw/TCRF_'+re.sub(r'[^A-Za-z0-9]+','_',sys.argv[1])+'.txt','w').write(t)
print(len(t))
