"""Construit media/catalogue.json : une entrée par affiche HSA, avec son URL publique.

Sources : blog-affiches/sauvegarde-couvertures-et-odd.tsv et blog-affiches/outils/targets.json
(dans les fichiers du projet HSA). Les affiches sont déjà hébergées publiquement par Wix
(static.wixstatic.com), donc utilisables tout de suite par Metricool, Instagram, etc.
"""
import csv, json, sys, pathlib

WIX = "https://static.wixstatic.com/media/"
BLOG = "https://www.hubscientifiqueafricain.com/post/"

def main(tsv, targets, sortie):
    meta = {t[0]: {"slug": t[2], "extrait": t[3], "date": t[5]} for t in json.load(open(targets, encoding="utf-8"))}
    cat = []
    for r in csv.DictReader(open(tsv, encoding="utf-8"), delimiter="\t"):
        m = meta.get(r["id"], {})
        cat.append({
            "id": r["id"],
            "titre": r["titre"],
            "odd": [int(x) for x in r["ODD"].split(",") if x.strip()],
            "date_article": m.get("date"),
            "lien_article": BLOG + m["slug"] if m.get("slug") else None,
            "extrait": m.get("extrait"),
            "affiche": WIX + r["nouvelle_affiche"],
        })
    cat.sort(key=lambda x: x["date_article"] or "", reverse=True)
    pathlib.Path(sortie).write_text(json.dumps(cat, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(cat)} affiches -> {sortie}")

if __name__ == "__main__":
    main(*sys.argv[1:4])
