#!/usr/bin/env python3
"""Génère le badge officiel et les visuels « Bienvenue » des campus ambassadeurs HSA.

Pour chaque ambassadeur du fichier JSON, crée dans le dossier de sortie :
  - <numero>-badge.png            le badge seul (fond transparent, haute définition, imprimable)
  - <numero>-bienvenue-4x5.png    le post Facebook / Instagram / LinkedIn (1080 x 1350)
  - <numero>-bienvenue-9x16.png   la story / le statut WhatsApp (1080 x 1920)
  - <numero>-legende.txt          le texte du post, prêt à copier

Usage :
  python3 generer.py exemple.json -o sortie/
  python3 generer.py ambassadeurs.json -o sortie/ --seulement HSA-CI-004

Champs attendus par ambassadeur (voir exemple.json) :
  prenom, nom, genre (F ou H), universite, ville, pays, niveau (facultatif),
  numero (ex. HSA-CI-001), code (code promo), photo (chemin local, URL https
  ou valeur « wix:image://… » copiée depuis le CMS Wix), cadrage (facultatif,
  ex. "50% 30%" pour remonter le visage dans le rond).
"""
import argparse
import base64
import io
import json
import mimetypes
import re
import subprocess
import sys
import tempfile
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

import qrcode
from PIL import Image, ImageOps

ICI = Path(__file__).resolve().parent
ANNEE = "2026-2027"
SITE = "https://www.hubscientifiqueafricain.com"


def data_uri(octets: bytes, mime: str) -> str:
    return f"data:{mime};base64," + base64.b64encode(octets).decode()


def url_wix(valeur: str) -> str:
    """wix:image://v1/<id>/<nom>#... -> https://static.wixstatic.com/media/<id>"""
    m = re.match(r"wix:image://v1/([^/#]+)", valeur)
    return f"https://static.wixstatic.com/media/{m.group(1)}" if m else valeur


def charger_photo(source: str, base: Path) -> str:
    source = url_wix(source.strip())
    if source.startswith("http"):
        req = urllib.request.Request(source, headers={"User-Agent": "hsa-badges"})
        octets = urllib.request.urlopen(req, timeout=30).read()
    else:
        chemin = Path(source)
        if not chemin.is_absolute():
            chemin = base / chemin
        octets = chemin.read_bytes()
    # Redresse (EXIF), recadre en carré centré, réduit : photos de téléphone souvent énormes.
    im = ImageOps.exif_transpose(Image.open(io.BytesIO(octets))).convert("RGB")
    # Portrait : on garde le haut (le visage), avec une petite marge ; paysage : on centre.
    cote = min(im.size)
    x = (im.width - cote) // 2
    y = min(im.height - cote, int(im.height * 0.06)) if im.height > im.width else 0
    im = im.crop((x, y, x + cote, y + cote))
    im = im.resize((900, 900), Image.LANCZOS)
    tampon = io.BytesIO()
    im.save(tampon, "JPEG", quality=92)
    return data_uri(tampon.getvalue(), "image/jpeg")


def qr_uri(code: str) -> str:
    cible = f"{SITE}/tarifs?" + urllib.parse.urlencode(
        {"utm_source": "badge", "utm_campaign": "ambassadeurs", "utm_content": code})
    q = qrcode.QRCode(border=0, box_size=10, error_correction=qrcode.constants.ERROR_CORRECT_M)
    q.add_data(cible)
    img = q.make_image(fill_color="#1f0d03", back_color="white")
    tampon = io.BytesIO()
    img.save(tampon, "PNG")
    return data_uri(tampon.getvalue(), "image/png")


def taille(texte: str, maxi: int, largeur: int, ratio: float) -> int:
    return int(min(maxi, largeur / max(1, ratio * len(texte))))


def nom_fichier(texte: str) -> str:
    t = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9-]+", "-", t).strip("-")


def a_univ(nom: str) -> str:
    """« à l'Université… », « à la Faculté… », « à ESATIC »."""
    premier = nom.split()[0].lower() if nom.split() else ""
    if premier[:1] in "aeiouyhéèêâîôû" and premier[:1]:
        return "à l'"
    if premier in ("faculté", "haute", "grande"):
        return "à la "
    return "à "


def valeurs(a: dict, base: Path) -> dict:
    f = str(a.get("genre", "H")).strip().upper().startswith("F")
    prenom = a["prenom"].strip()
    nom = a["nom"].strip()
    role = "Campus Ambassadrice" if f else "Campus Ambassadeur"
    lieu = ", ".join(x for x in [a.get("ville", "").strip(), a.get("pays", "").strip()] if x)
    titre_nom = f"{prenom} {nom}"
    nouveau = "nouvelle ambassadrice" if f else "nouvel ambassadeur"
    plus_long = max(["Bienvenue à notre", nouveau, titre_nom], key=len)
    niveau = a.get("niveau", "").strip()
    return {
        "logo": data_uri((ICI / "assets/logo-blanc.png").read_bytes(), "image/png"),
        "photo": charger_photo(a["photo"], base),
        "qr": qr_uri(a["code"]),
        "cadrage": a.get("cadrage", "50% 35%"),
        "prenom": prenom,
        "nom": nom,
        "taille_prenom": taille(prenom, 50, 460, 0.6),
        "taille_nom": taille(nom, 30, 460, 0.68),
        "universite": a["universite"].strip(),
        "a_univ": a_univ(a["universite"].strip()),
        "lieu": lieu,
        "lieu_phrase": f" ({lieu})" if lieu else "",
        "bloc_niveau": f'<div class="niveau">{niveau}</div>' if niveau else "",
        "numero": a["numero"].strip(),
        "code": a["code"].strip(),
        "annee": a.get("annee", ANNEE),
        "role_titre": role,
        "role_majuscules": role.upper(),
        "article": "notre",
        "nouveau_role": nouveau,
        "pastille": "NOUVELLE AMBASSADRICE" if f else "NOUVEL AMBASSADEUR",
        "il_elle": "Elle" if f else "Il",
        "taille_titre_post": taille(plus_long, 92, 900, 0.56),
        "taille_titre_story": taille(plus_long, 100, 930, 0.56),
    }


def legende(v: dict) -> str:
    f = v["il_elle"] == "Elle"
    autour = "d'elle" if f else "de lui"
    return (
        f"🎉 Bienvenue à {v['prenom']} {v['nom']}, {v['nouveau_role']} HSA !\n\n"
        f"{v['il_elle']} représente le Hub Scientifique Africain {v['a_univ']}{v['universite']}"
        f"{v['lieu_phrase']} pour l'année {v['annee']}. "
        f"{'Elle' if f else 'Il'} fera connaître HSA sur son campus, accompagnera les étudiants "
        f"et les jeunes chercheurs, et animera la communauté HSA autour {autour}.\n\n"
        f"🎓 Tu es {v['a_univ']}{v['universite']} ? Prends ton Pass HSA avec son code {v['code']}.\n\n"
        f"👉 Toi aussi, représente HSA dans ton université : {SITE}/ambassadeurs\n\n"
        f"#HSA #HubScientifiqueAfricain #CampusAmbassadeur #RechercheAfricaine"
    )


FORMATS = [
    ("seul", "badge", 540, 856, 3, True),
    ("post", "bienvenue-4x5", 1080, 1350, 1, False),
    ("story", "bienvenue-9x16", 1080, 1920, 1, False),
]


def generer(a: dict, base: Path, sortie: Path) -> list:
    v = valeurs(a, base)
    gabarit = (ICI / "gabarit.html").read_text(encoding="utf-8")
    prefixe = nom_fichier(v["numero"]) + "-" + nom_fichier(f"{v['prenom']}-{v['nom']}").lower()
    faits = []
    with tempfile.TemporaryDirectory() as tmp:
        for fmt, suffixe, w, h, echelle, transparent in FORMATS:
            html = gabarit
            for cle, val in {**v, "format": fmt}.items():
                html = html.replace("{{" + cle + "}}", str(val))
            page = Path(tmp) / f"{fmt}.html"
            page.write_text(html, encoding="utf-8")
            png = sortie / f"{prefixe}-{suffixe}.png"
            subprocess.run(["node", str(ICI / "rendu.js"), str(page), str(png), str(w), str(h),
                            str(echelle), "transparent" if transparent else ""], check=True)
            faits.append(png)
    txt = sortie / f"{prefixe}-legende.txt"
    txt.write_text(legende(v) + "\n", encoding="utf-8")
    faits.append(txt)
    return faits


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("fichier", help="JSON : un ambassadeur ou une liste d'ambassadeurs")
    p.add_argument("-o", "--sortie", default="sortie", help="dossier de sortie")
    p.add_argument("--seulement", help="ne générer que ce numéro de badge")
    args = p.parse_args()

    source = Path(args.fichier).resolve()
    donnees = json.loads(source.read_text(encoding="utf-8"))
    if isinstance(donnees, dict):
        donnees = [donnees]
    sortie = Path(args.sortie)
    sortie.mkdir(parents=True, exist_ok=True)

    manquants = ("prenom", "nom", "universite", "numero", "code", "photo")
    for a in donnees:
        if args.seulement and a.get("numero") != args.seulement:
            continue
        vides = [k for k in manquants if not str(a.get(k, "")).strip()]
        if vides:
            print(f"⚠ {a.get('prenom', '?')} {a.get('nom', '')} : champs manquants {', '.join(vides)}, ignoré",
                  file=sys.stderr)
            continue
        for f in generer(a, source.parent, sortie):
            print("✓", f)


if __name__ == "__main__":
    main()
