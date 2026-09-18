import json,urllib.parse,subprocess,sys,os,re
API="https://gta.fandom.com/api.php"
def call(params):
    q=urllib.parse.urlencode(params)
    out=subprocess.run(["curl","-s","-m","30","-A","Mozilla/5.0 (research)","--compressed",API+"?"+q],capture_output=True,text=True).stdout
    try: return json.loads(out)
    except Exception as e: return {"err":str(e),"raw":out[:400]}
def parse_wikitext(title):
    d=call({"action":"parse","page":title,"prop":"wikitext","format":"json","redirects":"1"})
    if "parse" in d: return d["parse"]["wikitext"]["*"]
    return None
def search(term,limit=12):
    d=call({"action":"query","list":"search","srsearch":term,"format":"json","srlimit":limit})
    return [(r["title"],re.sub("<[^>]*>","",r["snippet"])) for r in d.get("query",{}).get("search",[])]
if __name__=="__main__":
    mode=sys.argv[1]
    if mode=="page":
        t=parse_wikitext(sys.argv[2])
        print(t if t else "NOT FOUND")
    elif mode=="search":
        for a,b in search(sys.argv[2]): print("::",a,"|",b[:120])
