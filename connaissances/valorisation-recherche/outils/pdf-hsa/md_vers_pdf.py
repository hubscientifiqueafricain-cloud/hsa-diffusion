#!/usr/bin/env python3
"""Markdown -> PDF aux couleurs HSA (charte des PDF du blog : brun, jaune, orange, crème).

Usage :
  python3 md_vers_pdf.py <dossier-source> <dossier-pdf> [--tag "Base de connaissances · ..."] [--force] [--jobs 3]
    Convertit récursivement tous les .md de <dossier-source> en PDF dans <dossier-pdf>,
    même arborescence (fiches/x.md -> fiches/x.pdf). Les liens relatifs vers des .md
    sont réécrits vers les .pdf correspondants. Ne refait pas un PDF plus récent que sa source (sauf --force).
  python3 md_vers_pdf.py --fichier doc.md sortie.pdf [--tag ...]

Type de document deviné d'après le dossier (articles, fiches, transcriptions, cours, notes-hsa...)
ou le nom (guide, livre-blanc). Front matter optionnel (--- clé: valeur ---) : titre_seo,
meta_description, mots_cles. Signature HSA et lien ajoutés automatiquement en fin de document
(les lignes de signature déjà présentes dans le .md sont retirées pour éviter le doublon).
Nécessite : pip install markdown ; node + playwright (préinstallés dans le conteneur).
"""
import base64, html, json, os, re, subprocess, sys, tempfile
from pathlib import Path
import markdown

HERE = Path(__file__).resolve().parent
SITE = 'https://www.hubscientifiqueafricain.com'
SIGNATURE = 'HSA, le réseau social scientifique n°1 dédié à la valorisation des résultats de la recherche.'
TYPES = {'livres-blancs': 'Livre blanc', 'articles': 'Article', 'fiches': 'Fiche de lecture', 'transcriptions': 'Transcription en français',
         'cours': 'Cours', 'notes-hsa': 'Note HSA', 'masterclass': 'Masterclass', 'posts': 'Posts'}

def logo_uri():
    return 'data:image/png;base64,' + base64.b64encode((HERE / 'logo-hsa.png').read_bytes()).decode()

def front_matter(txt):
    meta = {}
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', txt, re.S)
    if m:
        for l in m.group(1).splitlines():
            if ':' in l:
                k, v = l.split(':', 1); meta[k.strip()] = v.strip()
        txt = txt[m.end():]
    return meta, txt

def doc_type(rel):
    parts = Path(rel).parts
    for p in parts[:-1]:
        if p in TYPES: return TYPES[p]
    n = parts[-1]
    if 'livre-blanc' in n: return 'Livre blanc'
    if 'guide' in n: return 'Guide'
    if 'index' in n: return 'Index'
    return 'Document'

def strip_signature(txt):
    lines = [l for l in txt.splitlines()
             if not re.search(r'réseau social scientifique n.?1', l) and not re.match(r'\s*\**\s*Rejoins HSA\s*:', l)]
    return '\n'.join(lines).rstrip()

def rewrite_links(htm):
    def fix(m):
        href = m.group(1)
        if re.match(r'^(https?:|mailto:|#)', href): return m.group(0)
        if href.endswith('/'): return 'href="#"'  # dossier : pas de cible PDF
        return 'href="' + re.sub(r'\.md(#.*)?$', r'.pdf\1', href) + '"'
    return re.sub(r'href="([^"]+)"', fix, htm)

def build_html(md_txt, rel, tag):
    meta, body = front_matter(md_txt)
    body = strip_signature(body)
    m = re.search(r'^#\s+(.+)$', body, re.M)
    title = m.group(1).strip() if m else Path(rel).stem.replace('-', ' ')
    if m: body = body[:m.start()] + body[m.end():]
    title = re.sub(r'^Fiche\s*:\s*', '', title)
    # chapeau : meta_description, sinon premier paragraphe court
    lead = meta.get('sous_titre') or meta.get('meta_description', '')
    if not lead:
        for para in re.split(r'\n\s*\n', body.strip()):
            p = para.strip()
            if p and not p.startswith(('#', '-', '|', '*', '>', '[')) and len(p) < 400:
                lead = re.sub(r'[*_`]', '', p); break
    # infos source (lignes "- Chaîne :", "- Date :", "- Source :")
    infos = []
    for k in ('Source', 'Chaîne', 'Date', 'Durée', 'Zone'):
        mm = re.search(rf'^-\s*{k}\s*:\s*(.+)$', body, re.M)
        if mm: infos.append((k, re.sub(r'https?://\S+', '', mm.group(1)).strip(' ,')))
    kind = doc_type(rel)
    htm = markdown.markdown(body, extensions=['tables', 'sane_lists'])
    htm = rewrite_links(htm)
    htm = re.sub(r'<a href="(https?://[^"]+)">\1</a>', lambda x: f'<a href="{x.group(1)}">{html.escape(x.group(1))}</a>', htm)
    logo = logo_uri()
    metas = ''.join(f'<div>{html.escape(k)}<b>{html.escape(v[:70])}</b></div>' for k, v in infos[:3])
    if meta.get('mots_cles'):
        metas += f'<div>Mots-clés<b>{html.escape(meta["mots_cles"][:70])}</b></div>'
    fonts = (HERE / 'fonts' / 'fonts.css').read_text().replace("url('", f"url('file://{HERE}/fonts/")
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(lead)}">
<style>{fonts}
@page {{ size:A4; margin:16mm 0 16mm; }}
@page :first {{ margin:0; }}
:root {{ --brun:#230e02; --or:#ffcc00; --orange:#e16a00; --creme:#fbf4ea; --sable:#f3e6d3; --txt:#2a1608; }}
* {{ box-sizing:border-box; }}
body {{ margin:0; font-family:'Plus Jakarta Sans',sans-serif; color:var(--txt); -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
.cover {{ width:210mm; height:297mm; background:var(--brun); color:#fff; position:relative; overflow:hidden; page-break-after:always; }}
.cover .top {{ padding:16mm 16mm 0; }}
.cover .top img {{ height:18mm; }}
.ray {{ position:absolute; right:-35mm; top:30mm; width:120mm; height:120mm; opacity:.08; border:16mm solid var(--or); border-radius:50%; }}
.ray2 {{ position:absolute; left:-25mm; bottom:40mm; width:70mm; height:70mm; opacity:.06; border:10mm solid var(--orange); border-radius:50%; }}
.cover .kind {{ display:inline-block; margin:62mm 16mm 0; background:var(--or); color:var(--brun); font-weight:700; font-size:9pt; letter-spacing:.18em; text-transform:uppercase; padding:2mm 4mm; border-radius:1.5mm; }}
.cover .tag {{ margin:5mm 16mm 0; font-size:9pt; font-weight:700; letter-spacing:.2em; text-transform:uppercase; color:var(--or); }}
.cover h1 {{ font-family:'Bricolage Grotesque',sans-serif; font-weight:800; font-size:28pt; line-height:1.1; margin:4mm 16mm 0; max-width:175mm; }}
.cover .bar {{ margin:7mm 16mm 0; width:40mm; height:2.5mm; background:var(--or); border-radius:2mm; }}
.cover .lead {{ margin:7mm 16mm 0; font-size:11.5pt; line-height:1.55; color:#e9dccb; max-width:170mm; }}
.cover .meta {{ position:absolute; left:16mm; right:16mm; bottom:26mm; display:flex; flex-wrap:wrap; gap:4mm 9mm; font-size:8.5pt; color:#d9c6b0; }}
.cover .meta b {{ color:#fff; display:block; font-size:9.5pt; font-weight:700; max-width:80mm; }}
.cover .band {{ position:absolute; left:0; right:0; bottom:0; height:13mm; background:var(--or); color:var(--brun); display:flex; align-items:center; justify-content:space-between; padding:0 16mm; font-weight:700; font-size:9.5pt; }}
.inner {{ padding:0 18mm; }}
.inner > h1, .inner > h2 {{ font-family:'Bricolage Grotesque',sans-serif; font-weight:800; color:var(--brun); font-size:15pt; margin:7mm 0 3mm; padding-bottom:1.5mm; border-bottom:.8mm solid var(--or); break-after:avoid; }}
h3 {{ font-family:'Bricolage Grotesque',sans-serif; font-weight:800; color:var(--orange); font-size:12pt; margin:5mm 0 2mm; break-after:avoid; }}
h4 {{ font-size:10.5pt; color:var(--brun); margin:4mm 0 1.5mm; }}
p {{ margin:0 0 2.6mm; font-size:10.3pt; line-height:1.62; text-align:justify; hyphens:auto; orphans:3; widows:3; }}
ul, ol {{ margin:0 0 3mm; padding-left:6mm; }}
li {{ font-size:10.3pt; line-height:1.55; margin-bottom:1.2mm; }}
li::marker {{ color:var(--orange); font-weight:700; }}
a {{ color:var(--orange); text-decoration:none; word-break:break-word; }}
strong {{ color:var(--brun); }}
blockquote {{ margin:4mm 0; background:var(--creme); border-left:1.6mm solid var(--or); border-radius:0 3mm 3mm 0; padding:3.5mm 5mm; }}
blockquote p {{ margin:0; font-style:italic; }}
hr {{ border:0; height:.5mm; background:var(--sable); margin:6mm 0; }}
table {{ border-collapse:collapse; width:100%; margin:3mm 0 5mm; font-size:8.6pt; }}
th {{ background:var(--brun); color:var(--or); text-align:left; padding:2mm; }}
td {{ border-bottom:.3mm solid var(--sable); padding:1.8mm 2mm; vertical-align:top; }}
tr:nth-child(even) td {{ background:var(--creme); }}
code {{ background:var(--creme); padding:.3mm 1.2mm; border-radius:1mm; font-size:9pt; }}
.about {{ break-inside:avoid; margin-top:9mm; background:var(--brun); color:#fff; border-radius:4mm; padding:6mm 7mm; }}
.about img {{ height:9mm; margin-bottom:3mm; }}
.about .sig {{ font-family:'Bricolage Grotesque',sans-serif; font-weight:800; font-size:13pt; color:var(--or); line-height:1.3; margin-bottom:2mm; }}
.about p {{ color:#e9dccb; font-size:9pt; text-align:left; margin-bottom:3mm; }}
.about a.btn {{ display:inline-block; background:var(--or); color:var(--brun); font-weight:700; font-size:10pt; padding:2.5mm 6mm; border-radius:10mm; }}
.about .url {{ margin-left:4mm; color:#fff; font-size:9pt; }}
</style></head><body>
<div class="cover"><div class="ray"></div><div class="ray2"></div>
  <div class="top"><img src="{logo}" alt="HSA"></div>
  <div class="kind">{html.escape(kind)}</div>
  <div class="tag">{html.escape(tag)}</div>
  <h1>{html.escape(title)}</h1>
  <div class="bar"></div>
  <div class="lead">{html.escape(lead)}</div>
  <div class="meta">{metas}</div>
  <div class="band"><span>Hub Scientifique Africain</span><span>hubscientifiqueafricain.com</span></div>
</div>
<div class="inner">
{htm}
<div class="about"><img src="{logo}" alt="HSA">
  <div class="sig">{SIGNATURE}</div>
  <p>Chercheurs, doctorants, innovateurs : HSA vous aide à rendre vos travaux visibles, à les protéger et à les transformer en impact.</p>
  <a class="btn" href="{SITE}">Rejoins HSA</a><span class="url">{SITE.replace('https://', '')}</span>
</div>
</div></body></html>"""

FOOTER = ('<div style="width:100%;font-size:7pt;font-family:sans-serif;color:#8a6d55;padding:0 18mm;display:flex;justify-content:space-between">'
          '<span>Hub Scientifique Africain · hubscientifiqueafricain.com</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')

def render(jobs, n=3):
    """jobs : liste de (html, pdf). Un seul Chromium, n pages en parallèle."""
    if not jobs: return []
    tmp = Path(tempfile.mkdtemp())
    lst = []
    for i, (h, out) in enumerate(jobs):
        f = tmp / f'{i}.html'; f.write_text(h, encoding='utf-8'); lst.append({'html': str(f), 'pdf': str(out)})
    jf = tmp / 'jobs.json'; jf.write_text(json.dumps({'jobs': lst, 'footer': FOOTER, 'n': n}))
    r = subprocess.run(['node', str(HERE / 'render_lot.js'), str(jf)], capture_output=True, text=True)
    if r.returncode: print(r.stderr[-2000:], file=sys.stderr)
    return [l for l in r.stdout.splitlines() if l.startswith('ERR')]

def main():
    a = sys.argv[1:]
    tag = 'Base de connaissances HSA'
    if '--tag' in a: i = a.index('--tag'); tag = a[i + 1]; del a[i:i + 2]
    force = '--force' in a; a = [x for x in a if x != '--force']
    n = 3
    if '--jobs' in a: i = a.index('--jobs'); n = int(a[i + 1]); del a[i:i + 2]
    if a[0] == '--fichier':
        src, out = Path(a[1]), Path(a[2])
        errs = render([(build_html(src.read_text(encoding='utf-8'), src.name, tag), out)], 1)
        print('ok' if not errs else errs); return
    src, dst = Path(a[0]), Path(a[1])
    jobs = []
    for md in sorted(src.rglob('*.md')):
        rel = md.relative_to(src)
        if any(p.startswith('.') or p == 'outils' for p in rel.parts): continue
        out = dst / rel.with_suffix('.pdf')
        if not force and out.exists() and out.stat().st_mtime >= md.stat().st_mtime: continue
        out.parent.mkdir(parents=True, exist_ok=True)
        jobs.append((build_html(md.read_text(encoding='utf-8'), str(rel), tag), out))
    print(len(jobs), 'PDF à produire', flush=True)
    for i in range(0, len(jobs), 60):
        errs = render(jobs[i:i + 60], n)
        print(f'{min(i + 60, len(jobs))}/{len(jobs)}', 'erreurs :', errs, flush=True)

if __name__ == '__main__':
    main()
