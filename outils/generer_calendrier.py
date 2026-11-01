"""Crée des brouillons de publications à partir du catalogue des affiches.

  python outils/generer_calendrier.py 2026-11-03 2 [nombre]
  -> à partir du 3 novembre, 2 publications par jour (9 h et 17 h, heure d'Abidjan).
Les fichiers sont créés au statut « brouillon » : relisez-les puis passez-les à « prevu ».
"""
import sys, json, datetime, pathlib, re, unicodedata, yaml

RACINE = pathlib.Path(__file__).resolve().parent.parent
HEURES = ["09:00", "17:00", "12:30", "20:00"]
TAGS_ODD = {3: "Santé", 4: "Éducation", 5: "ÉgalitéFemmesHommes", 6: "Eau", 13: "Climat", 15: "Environnement", 2: "Agriculture"}

def slug(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:50]

def main(debut, par_jour=2, nombre=None):
    cat = json.load(open(RACINE / "media/catalogue.json", encoding="utf-8"))
    deja = {yaml.safe_load(open(f, encoding="utf-8")).get("source") for f in (RACINE / "calendrier/posts").glob("*.yaml")}
    a_faire = [c for c in cat if c["id"] not in deja][: int(nombre) if nombre else None]
    jour, n = datetime.date.fromisoformat(debut), 0
    for i, c in enumerate(a_faire):
        j = jour + datetime.timedelta(days=i // int(par_jour))
        h = HEURES[i % int(par_jour)]
        tags = ["HSA", "RechercheAfricaine", "CôteDIvoire"] + [TAGS_ODD[o] for o in c["odd"] if o in TAGS_ODD] + [f"ODD{o}" for o in c["odd"]]
        post = {"quand": f"{j}T{h}:00", "statut": "brouillon", "source": c["id"],
                "reseaux": ["facebook", "instagram", "tiktok", "linkedin", "telegram", "whatsapp"],
                "media": [c["affiche"]], "lien": c["lien_article"],
                "texte": f"{c['titre']}\n\nUne recherche ivoirienne à découvrir sur le Hub Scientifique Africain 👇",
                "hashtags": list(dict.fromkeys(tags))}
        f = RACINE / "calendrier/posts" / f"{j}-{h.replace(':', 'h')}-{slug(c['titre'])}.yaml"
        yaml.safe_dump(post, open(f, "w", encoding="utf-8"), allow_unicode=True, sort_keys=False)
        n += 1
    print(f"{n} brouillon(s) créé(s)")

if __name__ == "__main__":
    main(*sys.argv[1:4])
