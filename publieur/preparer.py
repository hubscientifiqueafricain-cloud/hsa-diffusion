"""Génère les déclinaisons de format de chaque publication et le tableau de bord (site/)."""
import sys, glob, json, html, pathlib, yaml
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "outils"))
from formats import FORMATS, charger, decliner
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from textes import adapter

RACINE = pathlib.Path(__file__).resolve().parent.parent
SITE = RACINE / "site"
COULEURS = {"brouillon": "#888", "prevu": "#1f6feb", "publie": "#1a7f37", "manuel": "#bf8700", "echec": "#cf222e"}

def declinaisons(fichier, post):
    if not post.get("media"):
        return
    dossier = SITE / "declinaisons" / pathlib.Path(fichier).stem
    if dossier.exists() and len(list(dossier.glob("*.jpg"))) == len(FORMATS):
        return
    dossier.mkdir(parents=True, exist_ok=True)
    img = charger(post["media"][0])
    for f, t in FORMATS.items():
        decliner(img, t).save(dossier / f"{f}.jpg", quality=88, optimize=True)

def tableau(posts):
    lignes = []
    for f, p in posts:
        st = p.get("statut", "brouillon")
        res = p.get("resultats") or {}
        cases = []
        for r in p.get("reseaux", []):
            e = res.get(r, {})
            s = e.get("statut", st if st in ("brouillon", "prevu") else "prevu")
            lien = e.get("lien", "")
            lien_html = f' <a href="{html.escape(lien)}">↗</a>' if lien.startswith("http") else ""
            manuel = ""
            if s == "manuel":
                manuel = f'<details><summary>texte à copier</summary><pre>{html.escape(adapter(p, r))}</pre></details>'
            cases.append(f'<li><b style="color:{COULEURS.get(s, "#888")}">●</b> {r}{lien_html}{manuel}</li>')
        img = (p.get("media") or [""])[0]
        lignes.append(f'''<article><img src="{html.escape(img)}" alt="" loading="lazy">
<div><time>{html.escape(str(p.get("quand", "")))}</time> · <b style="color:{COULEURS.get(st)}">{st}</b>
<p>{html.escape((p.get("texte") or "")[:220])}</p><ul>{"".join(cases)}</ul>
<small>{html.escape(pathlib.Path(f).name)}</small></div></article>''')
    return f'''<!doctype html><html lang="fr"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>HSA · Diffusion</title><style>
body{{font-family:system-ui,sans-serif;max-width:900px;margin:auto;padding:16px;background:#fafafa;color:#222}}
article{{display:flex;gap:16px;background:#fff;border:1px solid #ddd;border-radius:10px;padding:12px;margin:12px 0}}
article img{{width:120px;height:120px;object-fit:cover;border-radius:6px}} ul{{list-style:none;padding:0}}
pre{{white-space:pre-wrap;background:#f3f3f3;padding:8px}} @media(max-width:600px){{article{{flex-direction:column}}}}
</style><h1>Hub Scientifique Africain · calendrier de diffusion</h1>
<p>● <span style="color:#1f6feb">prévu</span> ● <span style="color:#1a7f37">publié</span> ● <span style="color:#bf8700">à publier à la main</span> ● <span style="color:#cf222e">échec</span></p>
{"".join(lignes) or "<p>Aucune publication.</p>"}</html>'''

if __name__ == "__main__":
    posts = []
    for f in sorted(glob.glob(str(RACINE / "calendrier/posts/*.yaml")), reverse=True):
        p = yaml.safe_load(open(f, encoding="utf-8"))
        posts.append((f, p))
        if "--sans-images" not in sys.argv:
            declinaisons(f, p)
    SITE.mkdir(exist_ok=True)
    (SITE / "index.html").write_text(tableau(posts), encoding="utf-8")
    (SITE / "catalogue.json").write_text((RACINE / "media/catalogue.json").read_text(encoding="utf-8"), encoding="utf-8")
    print(f"site/ prêt ({len(posts)} publications)")
