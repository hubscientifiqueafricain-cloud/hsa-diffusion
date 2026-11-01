"""Importe dans l'outil toutes les publications et créas HSA présentes dans les fichiers du projet.

  python outils/importer_tout.py /mnt/project-files

- 4 packs de 60 posts (novembre v2, décembre, janvier, février) -> calendrier/posts/
- semaine Facebook du 2 au 8 novembre (diffusion-growth) + événements -> calendrier/posts/
- posts Metricool programmés (metricool.json, exporté à part) -> calendrier/posts/
- 120 affiches du blog + séries de pubs -> bibliotheque/ (créas prêtes, sans date)
Les créas sont copiées (et les images allégées) dans media/.
"""
import sys, re, json, shutil, unicodedata, datetime, pathlib, yaml
from PIL import Image

PF = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "/mnt/project-files")
R = pathlib.Path(__file__).resolve().parent.parent
POSTS, BIB, MEDIA = R / "calendrier/posts", R / "bibliotheque", R / "media"
AUJ = datetime.date(2026, 11, 1)
MOIS = {m: i for i, m in enumerate("janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split(), 1)}
RESEAUX = {"carrousel": ["facebook", "instagram", "linkedin", "tiktok", "whatsapp"],
           "video": ["facebook", "instagram", "tiktok", "youtube", "linkedin", "whatsapp"],
           "image": ["facebook", "instagram", "linkedin", "whatsapp"],
           "texte": ["facebook", "linkedin", "whatsapp"]}

def slug(t, n=45):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")[:n].strip("-")

def media(src, dest_rel):
    """Copie une créa dans media/ (images JPEG allégées) et renvoie son chemin relatif."""
    src, dest = pathlib.Path(src), MEDIA / dest_rel
    if not src.exists():
        return None
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        if src.suffix.lower() in (".jpg", ".jpeg", ".png") and src.stat().st_size > 250_000:
            dest = dest.with_suffix(".jpg")
            im = Image.open(src).convert("RGB")
            if im.width > 1080:
                im = im.resize((1080, round(im.height * 1080 / im.width)), Image.LANCZOS)
            im.save(dest, quality=82, optimize=True, progressive=True)
        else:
            shutil.copy2(src, dest)
    elif src.suffix.lower() == ".png" and src.stat().st_size > 250_000:
        dest = dest.with_suffix(".jpg")
    return str(dest.relative_to(R))

def ecrire(dossier, nom, post):
    dossier.mkdir(parents=True, exist_ok=True)
    yaml.safe_dump(post, open(dossier / nom, "w", encoding="utf-8"), allow_unicode=True, sort_keys=False, width=1000)

# ---------- 1. Les 4 packs de 60 posts ----------
PACKS = [("contenu-valorisation-v2", "textes-60-posts-v2.md", "Valorisation (novembre)", {11: 2026, 12: 2026}),
         ("contenu-valorisation-decembre", "textes-60-posts-decembre.md", "Prépare 2027 (décembre)", {12: 2026}),
         ("contenu-carriere-janvier", "textes-60-posts-janvier.md", "Carrière de chercheur (janvier)", {1: 2027}),
         ("contenu-argent-fevrier", "textes-60-posts-fevrier.md", "Gagner de l'argent (février)", {2: 2027, 3: 2027})]

def packs():
    n = 0
    for dossier, fichier, serie, annees in PACKS:
        base = PF / dossier
        texte = (base / fichier).read_text(encoding="utf-8")
        cle = dossier.split("-")[-1]
        for jour in re.split(r"\n(?=## Jour )", texte)[1:]:
            m = re.match(r"## Jour (\d+) · \w+ (\d+)(?:er)? (\w+)", jour)
            date = datetime.date(annees[MOIS[m.group(3)]], MOIS[m.group(3)], int(m.group(2)))
            for bloc in re.split(r"\n(?=### )", jour)[1:]:
                t = re.match(r"### (\d+)h(\d+) · (.+)", bloc)
                if not t:
                    continue
                heure, titre = f"{t.group(1).zfill(2)}:{t.group(2)}", t.group(3).strip()
                meta = bloc.split("\n")[2].strip()
                crea = re.search(r"Créa : `([^`]+)`", bloc).group(1)
                stem = re.sub(r"\.(pdf|mp4).*", "", crea).strip()
                fb = re.search(r"\*\*Facebook\*\*\n(.*?)(?=\n\*\*LinkedIn\*\*|\Z)", bloc, re.S).group(1).strip()
                li = re.search(r"\*\*LinkedIn\*\*\n(.*?)(?=\n---|\Z)", bloc, re.S).group(1).strip()
                if ".mp4" in crea:
                    typ = "video"
                    medias = [media(base / "videos" / f"{stem}.mp4", f"{cle}/{stem}.mp4")]
                    apercu = media(base / "videos" / f"{stem}-apercu.jpg", f"{cle}/{stem}-apercu.jpg")
                else:
                    typ = "carrousel"
                    imgs = sorted((base / "carrousels" / stem).glob(f"{stem}-*.jpg"), key=lambda p: int(p.stem.rsplit("-", 1)[1]))
                    medias = [media(p, f"{cle}/{stem}/{p.name}") for p in imgs]
                    apercu = medias[0] if medias else None
                post = {"quand": f"{date}T{heure}:00", "statut": "prevu", "source": serie, "titre": titre,
                        "type": typ, "details": meta, "reseaux": RESEAUX[typ], "apercu": apercu,
                        "media": [x for x in medias if x], "texte": fb, "textes": {"linkedin": li}}
                ecrire(POSTS, f"{date}-{heure.replace(':', 'h')}-{cle}-{slug(titre)}.yaml", post)
                n += 1
    return n

# ---------- 2. Semaine Facebook 2-8 novembre + événements ----------
def semaine():
    dg = PF / "diffusion-growth/outils"
    programmes = json.load(open(dg / "facebook-programmes.json"))
    lots = [("facebook-remplacement-08h-02-06nov.json", "Semaine 2-8 nov. : pubs Pass"),
            ("facebook-pubs-extra-02-08-novembre.json", "Semaine 2-8 nov. : pubs Pass"),
            ("facebook-semaine-02-08-novembre.json", "Semaine 2-8 nov. : opportunités et événements"),
            ("facebook-serie-canalplus-02-04nov.json", "Semaine 2-8 nov. : série bourses"),
            ("facebook-serie-startupboost-04-06nov.json", "Semaine 2-8 nov. : série thèse"),
            ("facebook-serie-wave-06-08nov.json", "Semaine 2-8 nov. : série arnaques"),
            ("facebook-serie-yango-31oct-06nov.json", "Semaine 2-8 nov. : série bourses")]
    vus, n = set(), 0
    for f, serie in lots:
        for p in json.load(open(dg / f)):
            d, h = p["date"], p["heure"]
            date = datetime.datetime.strptime(d, "%d/%m/%Y").date()
            if date < AUJ or (d, h, p["texte"][:40]) in vus:
                continue
            if f == "facebook-semaine-02-08-novembre.json" and h == "08:00" and date.day <= 6 and date.month == 11:
                continue  # remplacé par les pubs Pass de 8 h
            vus.add((d, h, p["texte"][:40]))
            ms = [media(m, "semaine-nov/" + pathlib.Path(m).name) for m in p.get("medias") or []]
            ms = [x for x in ms if x]
            typ = "carrousel" if len(ms) > 1 else ("video" if ms and ms[0].endswith(".mp4") else ("image" if ms else "texte"))
            post = {"quand": f"{date}T{h}:00", "statut": "prevu", "source": serie, "titre": p.get("format", ""),
                    "type": typ, "reseaux": RESEAUX[typ], "apercu": ms[0] if ms and not ms[0].endswith(".mp4") else None,
                    "media": ms, "texte": p["texte"]}
            if p.get("commentaire"):
                post["premier_commentaire"] = p["commentaire"]
            if f"{d} {h}" in programmes:
                post["deja_programme"] = {"facebook": "Déjà programmé directement sur Facebook"}
            ecrire(POSTS, f"{date}-{h.replace(':', 'h')}-semaine-{slug(post['titre'] or p['texte'], 30)}.yaml", post)
            n += 1
    return n

# ---------- 3. Posts Metricool programmés ----------
def metricool():
    f = R / "outils/metricool.json"
    if not f.exists():
        return 0
    n = 0
    for p in json.load(open(f, encoding="utf-8")):
        if p.get("draft"):
            continue  # brouillons = pubs Pass déjà importées depuis la semaine Facebook
        q = p["publicationDate"]["dateTime"]
        rs = [x["network"] for x in p["providers"]]
        typ = "video" if any(m.endswith(".mp4") for m in p.get("media", [])) else ("image" if p.get("media") else "texte")
        post = {"quand": q, "statut": "prevu", "source": "Metricool (programmé)", "titre": p["text"].split("\n")[0][:80],
                "type": typ, "reseaux": rs + ["whatsapp"], "apercu": None if typ == "video" else (p.get("media") or [None])[0],
                "media": p.get("media", []), "texte": p["text"],
                "deja_programme": {r: "Programmé dans Metricool" for r in rs}}
        if p.get("firstCommentText"):
            post["premier_commentaire"] = p["firstCommentText"]
        ecrire(POSTS, f"{q[:10]}-{q[11:16].replace(':', 'h')}-metricool-{slug(post['titre'], 30)}.yaml", post)
        n += 1
    return n

# ---------- 4. Bibliothèque : affiches et pubs prêtes ----------
def bibliotheque():
    n = 0
    for a in json.load(open(R / "media/catalogue.json", encoding="utf-8")):
        tags = " ".join(f"#ODD{o}" for o in a["odd"])
        post = {"statut": "brouillon", "source": "Affiches des articles du blog", "titre": a["titre"], "type": "image",
                "reseaux": RESEAUX["image"], "apercu": a["affiche"], "media": [a["affiche"]], "lien": a["lien_article"],
                "texte": f"{a['titre']}\n\nUne recherche africaine à découvrir sur le Hub Scientifique Africain 👇",
                "hashtags": ["HSA", "RechercheAfricaine"] + [f"ODD{o}" for o in a["odd"]]}
        ecrire(BIB / "affiches", f"{a['date_article']}-{slug(a['titre'])}.yaml", post)
        n += 1
    rs = PF / "reseaux-sociaux-hsa"
    index = {p.name: p for p in rs.rglob("*") if p.suffix.lower() in (".jpg", ".png")}
    series = [("pubs-gagner-argent-avec-hsa/textes-des-60-pubs.md", "Pubs « gagner de l'argent avec HSA »"),
              ("pubs-style-app-chariow/textes-des-60-creas.md", "Pubs style application"),
              ("serie-pubs-pass-douleurs/textes-des-8-pubs.md", "Pubs Pass HSA (douleurs)")]
    for f, serie in series:
        dossier = pathlib.Path(f).parent
        for i, bloc in enumerate(re.split(r"\n(?=## \d)", (rs / f).read_text(encoding="utf-8"))[1:], 1):
            titre = bloc.split("\n")[0].lstrip("# ").strip()
            img = re.search(r"([\w-]+-feed-1080x1350)\.(?:jpg|png)", bloc)
            if not img:
                cands = sorted(p for p in (rs / dossier / "fil-4x5").glob(f"*-{i:02d}-*")) if (rs / dossier / "fil-4x5").exists() else []
                src = cands[0] if cands else None
            else:
                src = index.get(img.group(1) + ".jpg") or index.get(img.group(1) + ".png")
            corps = re.sub(r"^.*?(Texte principal\s*:?\**\s*\n|\*\*Image :\*\*.*?\n)", "", bloc, count=1, flags=re.S)
            corps = re.sub(r"^(Image|Accroche|Titre|Bouton).*$", "", corps, flags=re.M)
            corps = re.sub(r"\n---\s*$", "", corps).strip().replace("**", "")
            m = media(src, f"pubs/{dossier.name}/{src.name}") if src else None
            post = {"statut": "brouillon", "source": serie, "titre": titre, "type": "image" if m else "texte",
                    "reseaux": RESEAUX["image" if m else "texte"], "apercu": m, "media": [m] if m else [], "texte": corps}
            ecrire(BIB / slug(serie, 30), f"{i:02d}-{slug(titre, 40)}.yaml", post)
            n += 1
    return n

if __name__ == "__main__":
    print("packs", packs())
    print("semaine", semaine())
    print("metricool", metricool())
    print("bibliotheque", bibliotheque())
