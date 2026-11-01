"""Règles de diffusion HSA : quel contenu va sur quel réseau (décidées le 1er novembre 2026).

- LinkedIn : les publications (PDF et affiches des articles de vulgarisation) et HSA comme réseau
  dédié à la valorisation des résultats de la recherche (séries éducatives).
- Facebook : promotion de HSA, opportunités, écosystème, modèles inspirés (Yango, Canal+…).
- TikTok : les vidéos, la promotion de HSA et les modèles inspirés.
- YouTube : vidéos de présentation de HSA et micro-formations.
- WhatsApp : comme Facebook (promotion, opportunités, écosystème).

  python outils/regles.py   # réapplique les règles à tous les fichiers du calendrier et de la bibliothèque
"""
import glob, pathlib, yaml

SERIES_EDUCATIVES = {"Valorisation (novembre)", "Prépare 2027 (décembre)", "Carrière de chercheur (janvier)",
                     "Gagner de l'argent (février)", "Novembre, 1re version (30 jours)"}
PUBLICATIONS = {"Affiches des articles du blog", "PDF des articles de vulgarisation", "Couvertures des guides (LinkedIn)"}
PROMO = {"Semaine 2-8 nov. : pubs Pass", "Pubs « gagner de l'argent avec HSA »", "Pubs style application",
         "Pubs Pass HSA (douleurs)", "Pub Pass HSA", "Créas de l'écosystème HSA"}
OPPORTUNITES = {"Semaine 2-8 nov. : opportunités et événements", "Événements scientifiques"}
INSPIRES = {"Semaine 2-8 nov. : série bourses", "Semaine 2-8 nov. : série thèse", "Semaine 2-8 nov. : série arnaques",
            "Reels inspirés (Canal+, Wave, Yango, Startup Boost)"}

def reseaux(source, typ, actuels=None):
    video = typ == "video"
    if source == "Metricool (programmé)":
        return actuels
    if source in PUBLICATIONS:
        return ["linkedin"]
    if source in SERIES_EDUCATIVES:
        return ["linkedin", "facebook", "whatsapp"] + (["tiktok"] if video else [])
    if source in PROMO or source in INSPIRES:
        return ["facebook", "tiktok", "whatsapp"]
    if source in OPPORTUNITES:
        return ["facebook", "whatsapp"]
    if source == "Vidéos pub HSA":
        return ["youtube", "facebook", "tiktok", "whatsapp"]
    if source == "Prix de la valorisation 2026":
        return ["linkedin", "facebook", "whatsapp"]
    if source == "Couvertures des pages":
        return ["facebook", "linkedin"]
    return ["facebook", "whatsapp"]

if __name__ == "__main__":
    R = pathlib.Path(__file__).resolve().parent.parent
    n = 0
    for f in glob.glob(str(R / "calendrier/posts/*.yaml")) + glob.glob(str(R / "bibliotheque/**/*.yaml"), recursive=True):
        p = yaml.safe_load(open(f, encoding="utf-8"))
        nv = reseaux(p.get("source"), p.get("type"), p.get("reseaux"))
        if nv != p.get("reseaux"):
            p["reseaux"] = nv
            yaml.safe_dump(p, open(f, "w", encoding="utf-8"), allow_unicode=True, sort_keys=False, width=1000)
            n += 1
    print(f"{n} fichiers mis à jour")
