"""Construit le poste de publication (site/) : données de tous les posts + médias + page web."""
import sys, glob, json, shutil, pathlib, yaml
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from textes import adapter

R = pathlib.Path(__file__).resolve().parent.parent
SITE = R / "site"

def charger(motif, rubrique):
    out = []
    for f in sorted(glob.glob(str(R / motif), recursive=True)):
        p = yaml.safe_load(open(f, encoding="utf-8"))
        rel = str(pathlib.Path(f).relative_to(R))
        out.append({
            "id": pathlib.Path(f).stem, "fichier": rel, "rubrique": rubrique,
            "quand": str(p.get("quand") or ""), "statut": p.get("statut"), "source": p.get("source", ""),
            "titre": p.get("titre", ""), "type": p.get("type", ""), "details": p.get("details", ""),
            "apercu": p.get("apercu"), "media": p.get("media") or [],
            "premier_commentaire": p.get("premier_commentaire"), "deja": p.get("deja_programme") or {},
            "resultats": p.get("resultats") or {},
            "textes": {r: adapter(p, r) for r in p.get("reseaux", [])},
        })
    return out

if __name__ == "__main__":
    SITE.mkdir(exist_ok=True)
    posts = charger("calendrier/posts/*.yaml", "calendrier") + charger("bibliotheque/**/*.yaml", "bibliotheque")
    (SITE / "donnees.json").write_text(json.dumps(posts, ensure_ascii=False), encoding="utf-8")
    shutil.copy2(R / "publieur/poste.html", SITE / "index.html")
    if "--sans-medias" not in sys.argv:
        if (SITE / "media").exists():
            shutil.rmtree(SITE / "media")
        shutil.copytree(R / "media", SITE / "media")
    print(f"site/ prêt : {len(posts)} posts")
