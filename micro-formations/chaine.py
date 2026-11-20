"""Fabrique les éléments de personnalisation de la chaîne YouTube HSA.

  python micro-formations/chaine.py            # images + bande-annonce
  python micro-formations/chaine.py --images   # images seulement

Sorties dans media/chaine-youtube/ :
  photo-profil-800.png      photo de profil (800x800, s'affiche en rond)
  banniere-2560x1440.jpg    bannière (zone visible partout : 1546x423 au centre)
  filigrane-150.png         filigrane des vidéos (150x150, fond transparent)
  bande-annonce.mp4         bande-annonce pour les visiteurs non abonnés (+ miniature, .srt)
"""
import sys, pathlib
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import render
from render import font, logo, Y, BG, BG2, BLANC, GRIS

SORTIE = render.RACINE / "media" / "chaine-youtube"

def degrade(w, h, cx, cy, r):
    im = Image.new("RGB", (w, h), BG)
    halo = Image.new("L", (w, h), 0)
    ImageDraw.Draw(halo).ellipse((cx - r, cy - r, cx + r, cy + r), fill=255)
    halo = halo.filter(ImageFilter.GaussianBlur(r // 2))
    return Image.composite(Image.new("RGB", (w, h), BG2), im, halo)

def asterisque(hauteur):
    """La marque (astérisque jaune) seule, découpée dans le logo."""
    lg = render.LOGO
    a = lg.crop((0, 0, int(lg.width * 169 / 800), int(lg.height * 0.8)))  # sans la signature sous le logo
    a = a.crop(a.split()[3].getbbox())
    r = hauteur / a.height
    return a.resize((int(a.width * r), hauteur), Image.LANCZOS)

def photo_profil():
    im = degrade(800, 800, 400, 300, 420)
    lg = logo(600)
    im.paste(lg, ((800 - lg.width) // 2, (800 - lg.height) // 2 - 10), lg)
    im.save(SORTIE / "photo-profil-800.png")

def banniere():
    W, H = 2560, 1440
    im = degrade(W, H, 1900, 500, 900)
    d = ImageDraw.Draw(im)
    # filigrane décoratif, hors zone sûre
    for x, y, h, a in ((2150, 330, 780, 0.07), (90, 820, 520, 0.05)):
        m = asterisque(h); m.putalpha(m.split()[3].point(lambda v: int(v * a))); im.paste(m, (x, y), m)
    # zone visible sur tous les écrans : 1546 x 423, centrée
    x0, y0 = (W - 1546) // 2, (H - 423) // 2
    lg = logo(330)
    im.paste(lg, (x0 + 10, y0 + (423 - lg.height) // 2), lg)
    d.rectangle((x0 + 380, y0 + 70, x0 + 386, y0 + 353), fill=Y)
    tx = x0 + 430
    d.text((tx, y0 + 52), "Valorise ta recherche.", font=font("noir", 84), fill=BLANC)
    d.text((tx, y0 + 152), "1 question, 2 minutes.", font=font("noir", 84), fill=Y)
    f = font("xb", 34); t = "UNE MICRO-FORMATION CHAQUE JOUR · 17H30"; w = f.getlength(t)
    d.rounded_rectangle((tx, y0 + 285, tx + w + 60, y0 + 355), radius=35, fill=Y)
    d.text((tx + 30, y0 + 320), t, font=f, fill=BG, anchor="lm")
    d.text((W // 2, y0 + 423 + 120), "hubscientifiqueafricain.com", font=font("sb", 40), fill=GRIS, anchor="ma")
    im.save(SORTIE / "banniere-2560x1440.jpg", quality=92)
    # aperçu avec la zone sûre, pour vérifier
    ap = im.copy(); ImageDraw.Draw(ap).rectangle((x0, y0, x0 + 1546, y0 + 423), outline=(255, 0, 0), width=4)
    ap.resize((1280, 720)).save(SORTIE / "banniere-apercu-zone-sure.jpg", quality=80)

def filigrane():
    im = Image.new("RGBA", (150, 150), (0, 0, 0, 0))
    ImageDraw.Draw(im).ellipse((2, 2, 147, 147), fill=BG + (235,), outline=Y + (255,), width=5)
    m = asterisque(104)
    im.paste(m, ((150 - m.width) // 2 + 4, (150 - m.height) // 2), m)
    im.save(SORTIE / "filigrane-150.png")

BANDE_ANNONCE = {
    "n": 0, "slug": "bande-annonce", "etiquette": "BIENVENUE SUR LA CHAÎNE HSA",
    "q": "Ta recherche mérite mieux qu'un tiroir.",
    "miniature": "Ta recherche mérite mieux qu'un tiroir",
    "accroche": "Des mois de terrain, des nuits de rédaction, une soutenance… et ensuite ? Trop souvent, le mémoire ou la thèse finit dans un tiroir. Sur cette chaîne, on change ça.",
    "slides": [
        {"t": "Sur cette chaîne", "beats": [
            ["1 question, 2 minutes", "Chaque vidéo répond à une seule question sur la valorisation de la recherche, en deux minutes maximum."],
            ["Une vidéo chaque jour à 17h30", "Une nouvelle micro-formation chaque jour, à dix-sept heures trente."],
            ["Des réponses concrètes", "Des réponses concrètes : comment faire servir tes résultats, protéger ton travail, trouver des partenaires et en tirer des revenus."]]},
        {"t": "Pour qui ?", "beats": [
            ["Étudiants en master", "Pour les étudiants en master,"],
            ["Doctorants et docteurs", "les doctorants et les jeunes docteurs,"],
            ["Enseignants-chercheurs", "les enseignants-chercheurs,"],
            ["Toutes les disciplines", "et toutes les disciplines, des sciences de la vie aux sciences humaines."]]},
    ],
    "resume": "HSA, le Hub Scientifique Africain, t'aide à transformer ta recherche en impact, en revenus et en notoriété.",
}

def bande_annonce():
    render.SORTIE = SORTIE
    render.FOND = render.fond()
    outro = ("Abonne-toi et active la cloche pour ne manquer aucune micro-formation. Et si tu as une question sur ta recherche, "
             "pose-la en commentaire : on y répondra dans une prochaine vidéo.")
    mp4, fin = render.fabriquer(BANDE_ANNONCE, "Valoriser ta recherche · 1 question, 2 minutes", outro)
    for ext in (".mp4", ".srt", "-miniature.jpg"):
        (SORTIE / f"MF00-bande-annonce{ext}").replace(SORTIE / f"bande-annonce{ext}")
    print(f"bande-annonce.mp4  {fin:.0f} s")

if __name__ == "__main__":
    SORTIE.mkdir(parents=True, exist_ok=True)
    photo_profil(); banniere(); filigrane()
    if "--images" not in sys.argv:
        bande_annonce()
    print("ok :", ", ".join(sorted(p.name for p in SORTIE.iterdir())))
