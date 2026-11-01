"""Décline un visuel dans tous les formats des réseaux sociaux.

  python outils/formats.py <image ou URL> <dossier_sortie>

Produit : carre_1x1 (1080x1080), portrait_4x5 (1080x1350), story_9x16 (1080x1920),
paysage_16x9 (1200x675) et pinterest_2x3 (1000x1500). L'image n'est jamais coupée :
elle est centrée sur un fond flou tiré d'elle-même, comme le font les applications mobiles.
"""
import io, sys, pathlib, urllib.request
from PIL import Image, ImageFilter

FORMATS = {
    "carre_1x1": (1080, 1080),       # Facebook, Instagram, LinkedIn, X, Threads
    "portrait_4x5": (1080, 1350),    # fil Instagram / Facebook (meilleure visibilité)
    "story_9x16": (1080, 1920),      # Stories, Reels, TikTok, Shorts, statut WhatsApp
    "paysage_16x9": (1200, 675),     # X, LinkedIn lien, miniature YouTube
    "pinterest_2x3": (1000, 1500),   # Pinterest
}

def charger(src):
    if src.startswith("http"):
        return Image.open(io.BytesIO(urllib.request.urlopen(src).read())).convert("RGB")
    return Image.open(src).convert("RGB")

def decliner(img, taille):
    W, H = taille
    fond = img.copy()
    r = max(W / fond.width, H / fond.height)
    fond = fond.resize((round(fond.width * r), round(fond.height * r)))
    g, h = (fond.width - W) // 2, (fond.height - H) // 2
    fond = fond.crop((g, h, g + W, h + H)).filter(ImageFilter.GaussianBlur(40))
    fond = Image.blend(fond, Image.new("RGB", (W, H), (20, 20, 20)), 0.35)
    r = min(W / img.width, H / img.height)
    devant = img.resize((round(img.width * r), round(img.height * r)), Image.LANCZOS)
    fond.paste(devant, ((W - devant.width) // 2, (H - devant.height) // 2))
    return fond

def main(src, sortie, nom=None):
    img = charger(src)
    out = pathlib.Path(sortie); out.mkdir(parents=True, exist_ok=True)
    nom = nom or pathlib.Path(src.split("?")[0]).stem.replace("~", "_")
    chemins = {}
    for f, t in FORMATS.items():
        p = out / f"{nom}_{f}.jpg"
        decliner(img, t).save(p, quality=88, optimize=True)
        chemins[f] = str(p)
    return chemins

if __name__ == "__main__":
    print(main(*sys.argv[1:4]))
