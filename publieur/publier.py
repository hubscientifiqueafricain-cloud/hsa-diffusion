"""Robot de publication HSA. Lancé toutes les 15 minutes par GitHub Actions.

Pour chaque fichier de calendrier/posts/ au statut « prevu » dont l'heure est passée :
  - adapte le texte et choisit le bon format d'image pour chaque réseau ;
  - essaie les connecteurs dans l'ordre (API directe -> Metricool -> manuel) ;
  - écrit le résultat dans le fichier (statut, liens, plan B utilisé) ;
  - ouvre une alerte si un plan B ou une publication manuelle a été nécessaire.

  python publieur/publier.py            # publie pour de vrai
  python publieur/publier.py --essai    # montre ce qui serait fait, sans rien envoyer
"""
import os, sys, json, glob, datetime, pathlib, requests, yaml
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from textes import adapter
from connecteurs import CHAINES

RACINE = pathlib.Path(__file__).resolve().parent.parent
PAGES = os.getenv("PAGES_URL", "").rstrip("/")   # ex. https://compte.github.io/hsa-diffusion
FORMAT_PAR_RESEAU = {"instagram": "portrait_4x5", "facebook": "portrait_4x5", "tiktok": "story_9x16",
                     "youtube": "story_9x16", "pinterest": "pinterest_2x3", "x": "paysage_16x9"}

def maintenant():  # heure d'Abidjan = GMT
    return datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None).replace(microsecond=0)

def medias_pour(post, fichier, reseau):
    """Utilise la déclinaison au bon format si elle a été publiée sur GitHub Pages, sinon l'original."""
    medias = [m if m.startswith("http") else f"{PAGES}/{m}" for m in post.get("media") or []]
    fmt = (post.get("formats") or {}).get(reseau) or FORMAT_PAR_RESEAU.get(reseau)
    if PAGES and fmt and medias:
        url = f"{PAGES}/declinaisons/{pathlib.Path(fichier).stem}/{fmt}.jpg"
        try:
            if requests.head(url, timeout=15).status_code == 200:
                return [url] + medias[1:]
        except requests.RequestException:
            pass
    return medias

def alerter(titre, corps):
    tok, depot = os.getenv("GITHUB_TOKEN"), os.getenv("GITHUB_REPOSITORY")
    print(f"ALERTE : {titre}\n{corps}")
    if tok and depot:
        requests.post(f"https://api.github.com/repos/{depot}/issues", timeout=30,
                      headers={"Authorization": f"Bearer {tok}"},
                      json={"title": titre, "body": corps, "labels": ["diffusion"]})

def images_non_validees(post):
    """Contrôle visuel obligatoire : chaque image doit être marquée « ok » dans media/controle-visuel.json."""
    sys.path.insert(0, str(RACINE / "outils"))
    import controle_visuel as cv
    reg, manque = cv.charger(), []
    for m in post.get("media") or []:
        if not str(m).lower().split("?")[0].endswith((".jpg", ".jpeg", ".png", ".webp")):
            continue
        try:
            b = requests.get(m, timeout=60).content if str(m).startswith("http") else (RACINE / m).read_bytes()
        except Exception:
            manque.append(f"{m} (introuvable)"); continue
        if cv.verdict(reg, cv.empreinte_octets(b)) != "ok":
            manque.append(str(m))
    return manque

def traiter(fichier, essai=False):
    post = yaml.safe_load(open(fichier, encoding="utf-8"))
    if post.get("statut") != "prevu":
        return False
    if datetime.datetime.fromisoformat(str(post["quand"])) > maintenant():
        return False
    # Mode manuel : si aucun réseau du post n'a de connecteur automatique, le poste de publication s'en charge.
    if not any(c.dispo() and c.nom != "Manuel assisté" for r in post.get("reseaux", []) for c in CHAINES.get(r, [])):
        return False
    manque = images_non_validees(post)
    if manque:
        print(f"BLOQUÉ (contrôle visuel) {fichier} : {manque}")
        if not essai:
            post["statut"] = "a_verifier"
            yaml.safe_dump(post, open(fichier, "w", encoding="utf-8"), allow_unicode=True, sort_keys=False)
            alerter(f"Image non vérifiée : {pathlib.Path(fichier).name}",
                    "Publication bloquée : ces images n'ont pas passé le contrôle visuel obligatoire "
                    "(mains, membres, visages, texte dans l'image, logo) :\n\n- " + "\n- ".join(manque) +
                    "\n\nInspecte-les avec `python outils/controle_visuel.py planche ...`, refais celles qui ont un "
                    "défaut, puis `valider` et remets le statut à « prevu ».")
        return not essai
    return _publier(fichier, post, essai)

def _publier(fichier, post, essai):
    resultats = post.setdefault("resultats", {})
    secours = []
    for reseau in post.get("reseaux", []):
        if resultats.get(reseau, {}).get("statut") in ("publie", "manuel"):
            continue
        texte, medias = adapter(post, reseau), medias_pour(post, fichier, reseau)
        erreurs = []
        for i, c in enumerate(CHAINES.get(reseau, [])):
            if not c.dispo():
                continue
            if essai:
                print(f"[essai] {fichier} -> {reseau} via {c.nom} | {medias[:1]} | {texte[:60]!r}")
                break
            try:
                lien = c.publier(post, reseau, texte, medias)
                statut = "manuel" if lien == "MANUEL" else "publie"
                resultats[reseau] = {"statut": statut, "via": c.nom, "lien": lien,
                                     "quand": maintenant().isoformat(), **({"erreurs": erreurs} if erreurs else {})}
                if erreurs:
                    secours.append(f"- **{reseau}** : {c.nom}" + (f" (échecs avant : {'; '.join(erreurs)})" if erreurs else ""))
                break
            except Exception as e:
                erreurs.append(f"{c.nom}: {str(e)[:200]}")
        else:
            resultats[reseau] = {"statut": "echec", "erreurs": erreurs}
            secours.append(f"- **{reseau}** : ÉCHEC ({'; '.join(erreurs)})")
    if essai:
        return False
    etats = {r["statut"] for r in resultats.values()}
    post["statut"] = "echec" if etats == {"echec"} else ("manuel" if "manuel" in etats or "echec" in etats else "publie")
    yaml.safe_dump(post, open(fichier, "w", encoding="utf-8"), allow_unicode=True, sort_keys=False)
    if secours:
        alerter(f"Plan B utilisé : {pathlib.Path(fichier).name}",
                "La publication est partie, mais pas par le chemin habituel :\n\n" + "\n".join(secours) +
                "\n\nLes publications « manuel » sont prêtes à copier dans le tableau de bord.")
    return True

if __name__ == "__main__":
    essai = "--essai" in sys.argv
    n = sum(traiter(f, essai) for f in sorted(glob.glob(str(RACINE / "calendrier/posts/*.yaml"))))
    print(f"{n} publication(s) traitée(s)")
