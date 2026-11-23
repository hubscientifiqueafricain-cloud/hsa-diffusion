import json, re, sys, os, unicodedata
src, out = sys.argv[1], sys.argv[2]
d = json.load(open(src))
over = {}
for extra in sys.argv[3:]:
    for k,v in json.load(open(extra)).items():
        if not v.get('err'): over[k]=v
d.update(over)
FR_ORIG = {'GOYEkXf0VC4'}  # mal étiquetée en, en réalité française
REGION = {}
for fn in ('regions.tsv','zones-extra.tsv'):
    fp=os.path.join(os.path.dirname(os.path.abspath(src)),fn)
    if os.path.exists(fp):
        for l in open(fp):
            if '\t' in l: k,r = l.rstrip('\n').split('\t')[:2]; REGION[k]=r
REJ=set()
fp=os.path.join(os.path.dirname(os.path.abspath(src)),'ecartees.tsv')
if os.path.exists(fp): REJ=set(l.split('\t')[0].strip() for l in open(fp))
d={k:v for k,v in d.items() if k not in REJ}
def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')[:60].strip('-')
def ts(t): return f"{t//3600}:{t%3600//60:02d}:{t%60:02d}" if t>=3600 else f"{t//60}:{t%60:02d}"
def paras(segs, step=45):
    outp, cur, start = [], [], None
    for s in segs:
        if start is None: start = s['t']
        cur.append(s['x'].strip())
        if s['t'] - start >= step:
            outp.append(f"[{ts(start)}] " + re.sub(r'\s+',' ',' '.join(cur))); cur, start = [], None
    if cur: outp.append(f"[{ts(start)}] " + re.sub(r'\s+',' ',' '.join(cur)))
    return '\n\n'.join(outp)
MOIS = 'janv. févr. mars avr. mai juin juil. août sept. oct. nov. déc.'.split()
def fdate(s):
    if not s: return ''
    y,m,dd = s[:10].split('-'); return f"{int(dd)} {MOIS[int(m)-1]} {y}"
os.makedirs(f"{out}/transcriptions", exist_ok=True)
rows, allfr = [], []
for k, r in d.items():
    if r.get('err') or not r.get('orig'): 
        rows.append((r.get('date',''), k, r, None, 0)); continue
    isfr = r['lang'].startswith('fr') or k in FR_ORIG
    fr = r['orig'] if isfr else (r['fr'] if isinstance(r.get('fr'), list) else None)
    name = slug(r['title']) + '.md'
    url = f"https://www.youtube.com/watch?v={k}"
    if isfr: kind = "Transcription automatique YouTube en français (texte brut, sans ponctuation, peut contenir des erreurs de reconnaissance vocale)"
    elif fr: kind = f"Langue d'origine : {r['lang']}. Version française : traduction automatique YouTube de la transcription {'officielle' if r['kind']=='manual' else 'automatique'}. Le texte original suit la version française."
    else: kind = f"Langue d'origine : {r['lang']}. Traduction française pas encore disponible (YouTube a limité les requêtes) : texte original seulement."
    body = [f"# {r['title']}", "", f"- Chaîne : {r['author']}", f"- Date : {fdate(r.get('date'))}", f"- Durée : {ts(r['secs'])}", f"- Zone : {REGION.get(k,'')}", f"- Lien : {url}", f"- {kind}", "", "---", "", "## Texte en français" if fr else "## Texte original", "", paras(fr or r['orig'])]
    if fr and not isfr:
        body += ["", "---", "", f"## Texte original ({r['lang']})", "", paras(r['orig'])]
    open(f"{out}/transcriptions/{name}", 'w').write('\n'.join(body)+'\n')
    w = sum(len(s['x'].split()) for s in (fr or r['orig']))
    rows.append((r.get('date',''), k, r, name, w))
    if fr: allfr.append(f"# {r['title']}\n\nSource : {r['author']}, {fdate(r.get('date'))}, {url}\n\n" + paras(fr))
rows.sort(key=lambda x: x[0] or '', reverse=True)

done=[x for x in rows if x[3]]
idx = ["# Index : valorisation des résultats de la recherche (YouTube, monde entier)", "",
  f"{len(done)} vidéos transcrites, de la plus récente à la plus ancienne. Toutes ont une version française (traduction automatique YouTube pour les vidéos en anglais, à relire avant citation). Les liens mènent aux vidéos originales.", "",
  "| Date | Zone | Vidéo | Chaîne | Mots | Fichier |", "|---|---|---|---|---|---|"]
for date,k,r,name,w in rows:
    t = r.get('title','').replace('|','-')
    f = f"[{name}](transcriptions/{name})" if name else "pas de transcription disponible"
    idx.append(f"| {fdate(date)} | {REGION.get(k,'')} | [{t}](https://www.youtube.com/watch?v={k}) | {r.get('author','')} | {w} | {f} |")
open(f"{out}/index.md",'w').write('\n'.join(idx)+'\n')
open(f"{out}/toutes-les-transcriptions-fr.md",'w').write("# Toutes les transcriptions en français : valorisation de la recherche\n\n" + '\n\n---\n\n'.join(allfr)+'\n')
json.dump({k:{'title':r.get('title'),'author':r.get('author'),'date':(r.get('date') or '')[:10]} for _,k,r,_,_ in rows}, open(f"{out}/videos-traitees.json",'w'), ensure_ascii=False, indent=1)
print(len(done), 'ok')
