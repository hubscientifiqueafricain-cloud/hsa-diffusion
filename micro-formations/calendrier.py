"""Ajoute les micro-formations au calendrier de diffusion (réseau YouTube).

  python micro-formations/calendrier.py 2026-11-03     # 1re vidéo ce jour-là, puis mardi et vendredi

Crée un fichier calendrier/posts/<date>-17h30-mf<NN>-<slug>.yaml par épisode, au statut « prevu ».
Le titre YouTube, la description, les tags, la miniature et les sous-titres sont dans le fichier.
"""
import sys, datetime, pathlib, yaml

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parent
LIEN = "https://www.hubscientifiqueafricain.com"
TAGS = ["valorisation de la recherche", "valoriser sa recherche", "thèse", "mémoire", "doctorat",
        "chercheur africain", "recherche scientifique", "HSA", "Hub Scientifique Africain", "micro-formation"]

def description(ep, d):
    points = []
    for s in ep["slides"]:
        points.append(f"▶ {s['t']}")
        points += [f"   • {b[0]}" for b in s["beats"]]
    return "\n".join([
        ep["accroche"], "",
        "Dans cette micro-formation :", *points, "",
        f"À retenir : {ep['resume']}", "",
        "💬 Tu as une question sur la valorisation de ta recherche ? Pose-la en commentaire : on y répondra dans une prochaine vidéo.",
        "🔔 Abonne-toi pour ne rien manquer de la série « " + d["serie"] + " ».", "",
        f"🌐 HSA, le Hub Scientifique Africain : {LIEN}", "",
        "#ValorisationDeLaRecherche #Doctorat #RechercheAfricaine",
    ])

def main():
    d = yaml.safe_load(open(ICI / "episodes.yaml", encoding="utf-8"))
    jour = datetime.date.fromisoformat(sys.argv[1] if len(sys.argv) > 1 else "2026-11-03")
    for ep in d["episodes"]:
        while jour.weekday() not in (1, 4):  # mardi, vendredi
            jour += datetime.timedelta(days=1)
        base = f"MF{ep['n']:02d}-{ep['slug']}"
        titre = f"{ep['q']} | Micro-formation HSA n°{ep['n']}"
        if len(titre) > 100:
            titre = ep["q"][:100]
        post = {
            "quand": f"{jour.isoformat()}T17:30:00",
            "statut": "prevu",
            "source": "Micro-formations YouTube",
            "titre": titre,
            "type": "video",
            "details": f"YouTube · vidéo 16:9 · épisode {ep['n']}/{len(d['episodes'])} · miniature et sous-titres (.srt) fournis",
            "reseaux": ["youtube"],
            "apercu": f"media/micro-formations/{base}-miniature.jpg",
            "media": [f"media/micro-formations/{base}.mp4",
                      f"media/micro-formations/{base}-miniature.jpg",
                      f"media/micro-formations/{base}.srt"],
            "youtube": {"titre": titre, "type": "video", "categorie": "EDUCATION", "pour_enfants": False,
                        "tags": TAGS, "miniature": f"media/micro-formations/{base}-miniature.jpg",
                        "sous_titres": f"media/micro-formations/{base}.srt"},
            "texte": description(ep, d),
            "question_youtube": ep["yt"],
        }
        nom = RACINE / "calendrier" / "posts" / f"{jour.isoformat()}-17h30-mf{ep['n']:02d}-{ep['slug']}.yaml"
        nom.write_text(yaml.safe_dump(post, allow_unicode=True, sort_keys=False, width=1000), encoding="utf-8")
        print(nom.name)
        jour += datetime.timedelta(days=1)

if __name__ == "__main__":
    main()
