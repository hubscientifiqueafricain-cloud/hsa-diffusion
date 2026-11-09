"""Contrôle visuel obligatoire avant toute publication HSA (règle du 9 novembre 2026).

Aucune image ne part sur un réseau, le blog ou une publicité sans avoir été regardée en détail :
mains et doigts (nombre, fusion), membres, visages, texte dans l'image (lisible, en bon français,
pas de charabia), billets ou documents inventés, logo HSA correct. Une image défectueuse est
refaite, jamais publiée.

Le registre media/controle-visuel.json garde, pour chaque image (par empreinte SHA-256), le
verdict « ok » ou « refuse », la date et une note. Le robot de publication (publieur/publier.py)
refuse de publier un post dont une image n'est pas marquée « ok ».

  python outils/controle_visuel.py planche IMAGES...          # planche + zooms à inspecter
  python outils/controle_visuel.py valider IMAGES... --note "mains et texte vérifiés"
  python outils/controle_visuel.py refuser IMAGES... --note "trois mains"
  python outils/controle_visuel.py manquants                  # images des posts à venir non validées
"""
import sys, json, glob, hashlib, datetime, pathlib, argparse

RACINE = pathlib.Path(__file__).resolve().parent.parent
REGISTRE = RACINE / "media/controle-visuel.json"
POINTS = ["mains et doigts (5 par main, pas de main en trop ni fusionnée)", "bras, jambes, corps entiers",
          "visages", "texte dans l'image : lisible et en bon français, sinon aucun texte",
          "pas de faux billets, faux documents ou panneaux inventés", "logo HSA et icônes ODD corrects"]


def empreinte_octets(b):
    return hashlib.sha256(b).hexdigest()


def empreinte(chemin):
    return empreinte_octets(pathlib.Path(chemin).read_bytes())


def charger():
    if REGISTRE.exists():
        return json.loads(REGISTRE.read_text(encoding="utf-8"))
    return {}


def enregistrer(reg):
    REGISTRE.write_text(json.dumps(reg, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")


def verdict(reg, h):
    return (reg.get(h) or {}).get("verdict")


def marquer(images, v, note):
    reg = charger()
    jour = datetime.date.today().isoformat()
    for img in images:
        rel = str(pathlib.Path(img).resolve().relative_to(RACINE)) if str(pathlib.Path(img).resolve()).startswith(str(RACINE)) else str(img)
        reg[empreinte(img)] = {"verdict": v, "date": jour, "note": note, "fichier": rel}
    enregistrer(reg)
    print(f"{len(images)} image(s) marquée(s) « {v} »")


def planche(images, sortie):
    """Une planche par image : l'image entière + ses 4 quarts agrandis, pour regarder les détails."""
    from PIL import Image, ImageDraw
    out = pathlib.Path(sortie)
    out.mkdir(parents=True, exist_ok=True)
    for img in images:
        im = Image.open(img).convert("RGB")
        w, h = im.size
        cell = 700
        sh = Image.new("RGB", (cell * 3, cell * 2), "white")
        sh.paste(im.resize((cell, int(cell * h / w)) if w >= h else (int(cell * w / h), cell)), (0, 0))
        quarts = [(0, 0, w // 2, h // 2), (w // 2, 0, w, h // 2), (0, h // 2, w // 2, h), (w // 2, h // 2, w, h)]
        pos = [(cell, 0), (cell * 2, 0), (cell, cell), (cell * 2, cell)]
        for q, p in zip(quarts, pos):
            sh.paste(im.crop(q).resize((cell, cell)), p)
        d = ImageDraw.Draw(sh)
        d.text((10, cell + 10), "À vérifier :\n- " + "\n- ".join(POINTS), fill="black")
        sh.save(out / (pathlib.Path(img).stem + "-controle.jpg"), quality=88)
    print(f"Planches dans {out}/ : regarde chaque zoom avant de valider.")


def medias_a_venir():
    import yaml
    maintenant = datetime.datetime.now().isoformat()
    for f in sorted(glob.glob(str(RACINE / "calendrier/posts/*.yaml"))):
        p = yaml.safe_load(open(f, encoding="utf-8"))
        if p.get("statut") not in ("prevu", "brouillon") or str(p.get("quand", "")) < maintenant[:19]:
            continue
        for m in p.get("media") or []:
            if not str(m).startswith("http") and str(m).lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                yield f, RACINE / m


def manquants():
    reg = charger()
    n = 0
    for f, m in medias_a_venir():
        if not m.exists():
            print(f"INTROUVABLE  {m}  ({pathlib.Path(f).name})"); n += 1
        elif verdict(reg, empreinte(m)) != "ok":
            print(f"À VÉRIFIER   {m.relative_to(RACINE)}  ({pathlib.Path(f).name})"); n += 1
    print(f"{n} image(s) à vérifier avant publication")
    return n


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("action", choices=["planche", "valider", "refuser", "manquants"])
    ap.add_argument("images", nargs="*")
    ap.add_argument("--note", default="")
    ap.add_argument("--sortie", default="controle-visuel")
    a = ap.parse_args()
    if a.action == "planche":
        planche(a.images, a.sortie)
    elif a.action in ("valider", "refuser"):
        if not a.note:
            sys.exit("Ajoute --note pour dire ce qui a été vérifié (ou le défaut trouvé).")
        marquer(a.images, "ok" if a.action == "valider" else "refuse", a.note)
    else:
        sys.exit(1 if manquants() else 0)
