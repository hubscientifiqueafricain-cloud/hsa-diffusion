"""Fabrique les vidéos de la série YouTube « Valoriser ta recherche · 1 question, 2 minutes ».

  python micro-formations/render.py            # toutes les vidéos
  python micro-formations/render.py 3 7        # seulement les épisodes 3 et 7

Pour chaque épisode de episodes.yaml : voix off (edge-tts), images 1920x1080 animées (Pillow),
sous-titres incrustés, montage ffmpeg, miniature YouTube 1280x720.
Sorties dans media/micro-formations/ (mp4 + miniature jpg + srt).
"""
import os, sys, asyncio, subprocess, pathlib, json
import yaml
from PIL import Image, ImageDraw, ImageFont, ImageFilter

try:  # derrière le proxy du conteneur cloud
    import certifi
    if os.path.exists("/root/.ccr/ca-bundle.crt"):
        certifi.where = lambda: "/root/.ccr/ca-bundle.crt"
except ImportError:
    pass

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parent
SORTIE = RACINE / "media" / "micro-formations"
TRAVAIL = pathlib.Path(os.getenv("MF_TRAVAIL", "/tmp/mf-travail"))
VOIX = os.getenv("MF_VOIX", "fr-FR-HenriNeural")

W, H, FPS = 1920, 1080, 25
BG, BG2 = (18, 9, 2), (46, 22, 3)
Y = (255, 203, 1)
BLANC = (247, 241, 232)
GRIS = (170, 152, 132)
CARTE = (34, 19, 7)
FD = "/usr/share/fonts/opentype/inter/"
def font(poids, taille):
    return ImageFont.truetype(FD + {"noir": "Inter-Black.otf", "xb": "Inter-ExtraBold.otf", "b": "Inter-Bold.otf",
                                    "sb": "Inter-SemiBold.otf", "m": "Inter-Medium.otf", "r": "Inter-Regular.otf"}[poids], taille)

LOGO = Image.open(ICI / "logo-hsa.png").convert("RGBA")
def logo(largeur):
    r = largeur / LOGO.width
    return LOGO.resize((int(LOGO.width * r), int(LOGO.height * r)), Image.LANCZOS)

def couper(texte, f, largeur):
    mots, lignes, cur = texte.split(), [], ""
    for m in mots:
        essai = (cur + " " + m).strip()
        if f.getlength(essai) <= largeur or not cur:
            cur = essai
        else:
            lignes.append(cur); cur = m
    if cur: lignes.append(cur)
    return lignes

# ---------------------------------------------------------------- fond
def fond():
    im = Image.new("RGB", (W, H), BG)
    halo = Image.new("L", (W, H), 0)
    ImageDraw.Draw(halo).ellipse((W - 900, -500, W + 500, 700), fill=255)
    halo = halo.filter(ImageFilter.GaussianBlur(260))
    im = Image.composite(Image.new("RGB", (W, H), BG2), im, halo)
    # astérisque HSA en filigrane
    marque = logo(1500).crop((0, 0, 330, 692 * 1500 // 1500))
    a = marque.split()[3].point(lambda v: v * 0.05)
    marque.putalpha(a)
    im.paste(marque, (W - 420, H - 620), marque)
    return im

FOND = None
def entete(im, n, serie):
    d = ImageDraw.Draw(im)
    lg = logo(200)
    im.paste(lg, (110, 70), lg)
    f = font("b", 26)
    txt = "BANDE-ANNONCE" if n == 0 else f"MICRO-FORMATION · ÉP. {n:02d}"
    w = f.getlength(txt)
    d.rounded_rectangle((W - 110 - w - 56, 78, W - 110, 136), radius=29, outline=Y, width=3)
    d.text((W - 110 - w - 28, 92), txt, font=f, fill=Y)

def carte_ligne(num, texte, largeur=1300, compact=False):
    """Une ligne qui apparaît : pastille + texte, sur une carte (compacte quand il y en a 4 ou plus)."""
    f = font("sb", 42 if compact else 52)
    pas = 54 if compact else 66
    lignes = couper(texte, f, largeur - 190)
    h = (36 if compact else 84) + pas * len(lignes)
    im = Image.new("RGBA", (largeur, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, largeur - 1, h - 1), radius=26, fill=CARTE + (255,), outline=(90, 62, 20, 255), width=2)
    d.ellipse((40, h // 2 - 34, 108, h // 2 + 34), fill=Y)
    if num:
        d.text((74, h // 2), str(num), font=font("xb", 36), fill=BG, anchor="mm")
    else:
        d.ellipse((64, h // 2 - 10, 84, h // 2 + 10), fill=BG)
    y = (h - pas * len(lignes)) // 2 - 4
    for l in lignes:
        d.text((146, y), l, font=f, fill=BLANC); y += pas
    return im

def sous_titre(im, texte):
    if not texte: return
    f = font("m", 36)
    lignes = couper(texte, f, 1500)[:3]
    h = 50 * len(lignes) + 36
    y0 = H - 40 - h
    voile = Image.new("RGBA", (W, h), (0, 0, 0, 0))
    ImageDraw.Draw(voile).rounded_rectangle(((W - 1600) // 2, 0, (W + 1600) // 2, h), radius=18, fill=(0, 0, 0, 170))
    im.paste(voile, (0, y0), voile)
    d = ImageDraw.Draw(im)
    y = y0 + 18
    for l in lignes:
        d.text((W // 2, y), l, font=f, fill=BLANC, anchor="ma"); y += 50

def barre(im, p):
    d = ImageDraw.Draw(im)
    d.rectangle((0, H - 10, W, H), fill=(40, 26, 10))
    d.rectangle((0, H - 10, int(W * p), H), fill=Y)

# ---------------------------------------------------------------- écrans
def ecran_question(ep, serie):
    im = FOND.copy(); entete(im, ep["n"], serie)
    d = ImageDraw.Draw(im)
    d.text((110, 300), ep.get("etiquette", "LA QUESTION"), font=font("xb", 40), fill=Y)
    f = font("noir", 96)
    y = 370
    for l in couper(ep["q"], f, 1650):
        d.text((110, y), l, font=f, fill=BLANC); y += 112
    d.text((110, y + 30), serie, font=font("m", 34), fill=GRIS)
    return im

def ecran_slide(ep, serie, titre):
    im = FOND.copy(); entete(im, ep["n"], serie)
    d = ImageDraw.Draw(im)
    f = font("noir", 76)
    d.text((110, 215), titre, font=f, fill=BLANC)
    d.rectangle((110, 318, 230, 328), fill=Y)
    return im

def ecran_resume(ep, serie):
    im = FOND.copy(); entete(im, ep["n"], serie)
    d = ImageDraw.Draw(im)
    d.text((110, 260), "À RETENIR", font=font("xb", 40), fill=Y)
    f = font("b", 72)
    y = 330
    for l in couper(ep["resume"], f, 1650):
        d.text((110, y), l, font=f, fill=BLANC); y += 92
    return im

# Zones laissées libres pour l'écran de fin YouTube (en pixels sur 1920x1080) :
# deux vidéos/playlists à droite, bouton S'abonner en bas à gauche.
ZONES_FIN = {"video_1": (1170, 150, 1810, 510), "video_2": (1170, 570, 1810, 930), "abonnement": (135, 610, 435, 910)}
DUREE_FIN = 16  # secondes à l'écran (YouTube : écran de fin de 5 à 20 s)

EPISODES = None
def episodes_suivants(n):
    """Les deux épisodes qui suivent n dans la série (on reboucle au début ; la bande-annonce, n = 0, mène aux épisodes 1 et 2)."""
    global EPISODES
    if EPISODES is None:
        EPISODES = yaml.safe_load(open(ICI / "episodes.yaml", encoding="utf-8"))["episodes"]
    nums = [e["n"] for e in EPISODES]
    i = nums.index(n) + 1 if n in nums else 0
    return [EPISODES[(i + k) % len(EPISODES)] for k in (0, 1)]

def capture(ep):
    """La miniature de l'épisode, fabriquée à la volée."""
    chemin = TRAVAIL / f"miniature-{ep['n']:02d}.jpg"
    miniature(ep, chemin)
    return Image.open(chemin).convert("RGB")

def ecran_fin(ep, serie):
    im = FOND.copy()
    d = ImageDraw.Draw(im)
    lg = logo(260)
    im.paste(lg, (110, 120), lg)
    d.text((110, 290), "Merci d'avoir regardé !", font=font("noir", 70), fill=BLANC)
    y = 385
    for l in couper("Pose ta question en commentaire : on y répond dans une prochaine vidéo.", font("m", 38), 900):
        d.text((110, y), l, font=font("m", 38), fill=GRIS); y += 50
    suivants = episodes_suivants(ep["n"])
    for nom, (x0, y0, x1, y1) in ZONES_FIN.items():
        if nom == "abonnement":
            d.ellipse((x0, y0, x1, y1), outline=Y, width=6)
            continue
        suivant = suivants[0 if nom == "video_1" else 1]
        d.text((x0, y0 - 44), "ÉPISODE SUIVANT" if nom == "video_1" else "ENSUITE", font=font("xb", 28), fill=Y)
        vignette = capture(suivant).resize((x1 - x0, y1 - y0), Image.LANCZOS)
        masque = Image.new("L", vignette.size, 0)
        ImageDraw.Draw(masque).rounded_rectangle((0, 0, vignette.width - 1, vignette.height - 1), radius=18, fill=255)
        im.paste(vignette, (x0, y0), masque)
        d.rounded_rectangle((x0, y0, x1, y1), radius=18, outline=(110, 80, 25), width=3)
    d.text((480, 700), "Abonne-toi", font=font("noir", 60), fill=Y)
    d.text((480, 780), "Une micro-formation", font=font("m", 36), fill=BLANC)
    d.text((480, 826), "chaque jour à 17h30", font=font("m", 36), fill=BLANC)
    d.text((110, 990), "hubscientifiqueafricain.com", font=font("sb", 34), fill=GRIS)
    return im

def miniature(ep, chemin):
    im = FOND.copy()
    d = ImageDraw.Draw(im)
    lg = logo(300); im.paste(lg, (110, 90), lg)
    f = font("xb", 46); t = "BANDE-ANNONCE" if ep['n'] == 0 else f"ÉP. {ep['n']:02d}"; w = f.getlength(t)
    d.rounded_rectangle((W - 110 - w - 70, 100, W - 110, 186), radius=43, fill=Y)
    d.text((W - 110 - w - 35, 143), t, font=f, fill=BG, anchor="lm")
    q = ep.get("miniature") or ep["q"]
    taille = 150
    while True:
        f = font("noir", taille); lignes = couper(q, f, 1700)
        if len(lignes) * taille * 1.12 <= 640 or taille <= 90: break
        taille -= 6
    y = 290 + (640 - len(lignes) * int(taille * 1.12)) // 2
    for i, l in enumerate(lignes):
        d.text((110, y), l, font=f, fill=Y if i == len(lignes) - 1 else BLANC); y += int(taille * 1.12)
    d.rectangle((0, H - 80, W, H), fill=Y)
    d.text((110, H - 40), "VALORISER TA RECHERCHE · 1 QUESTION, 2 MINUTES", font=font("xb", 38), fill=BG, anchor="lm")
    im.resize((1280, 720), Image.LANCZOS).save(chemin, quality=92)

# ---------------------------------------------------------------- voix
async def dire(texte, mp3):
    import edge_tts
    if mp3.exists() and mp3.with_suffix(".txt").exists() and mp3.with_suffix(".txt").read_text() == texte + VOIX:
        return
    await edge_tts.Communicate(texte, VOIX, rate="-3%").save(str(mp3))
    mp3.with_suffix(".txt").write_text(texte + VOIX)

def duree(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)]).strip())

def srt_temps(t):
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

# ---------------------------------------------------------------- montage
def fabriquer(ep, serie, outro):
    dos = TRAVAIL / f"ep{ep['n']:02d}"; dos.mkdir(parents=True, exist_ok=True)
    # 1. la liste des répliques, dans l'ordre
    repliques = [("question", None, ep["accroche"])]
    for si, s in enumerate(ep["slides"]):
        for bi, (ecran, voix) in enumerate(s["beats"]):
            repliques.append(("slide", (si, bi), voix))
    repliques += [("resume", None, ep["resume"]), ("fin", None, outro)]
    async def tout():
        for i, (_, _, txt) in enumerate(repliques):
            await dire(txt, dos / f"r{i:02d}.mp3")
    asyncio.run(tout())
    # 2. la ligne de temps
    t, tl = 0.6, []
    prec = None
    for i, (kind, ref, txt) in enumerate(repliques):
        nouvel_ecran = kind != "slide" or ref[1] == 0 or prec != "slide"
        if nouvel_ecran and i: t += 0.5
        d = duree(dos / f"r{i:02d}.mp3")
        tl.append({"kind": kind, "ref": ref, "txt": txt, "a": t, "b": t + d, "i": i})
        t += d + 0.35
        prec = kind
    fin = max(t + 1.2, tl[-1]["a"] - 0.5 + DUREE_FIN)
    # 3. la bande-son
    entrees, filtres = [], []
    for k, r in enumerate(tl):
        entrees += ["-i", str(dos / f"r{r['i']:02d}.mp3")]
        ms = int(r["a"] * 1000)
        filtres.append(f"[{k}:a]aresample=44100,adelay={ms}|{ms}[a{k}]")
    filtres.append("".join(f"[a{k}]" for k in range(len(tl))) + f"amix=inputs={len(tl)}:normalize=0,apad,atrim=0:{fin:.2f},loudnorm=I=-16:TP=-1.5[out]")
    subprocess.run(["ffmpeg", "-y", "-v", "error"] + entrees + ["-filter_complex", ";".join(filtres), "-map", "[out]", "-ac", "2", str(dos / "voix.wav")], check=True)
    # 4. sous-titres (srt à téléverser sur YouTube)
    srt = []
    for k, r in enumerate(tl, 1):
        srt.append(f"{k}\n{srt_temps(r['a'])} --> {srt_temps(r['b'])}\n{r['txt']}\n")
    # 5. les écrans de base (mis en cache) et les cartes
    cartes = {}
    for si, s in enumerate(ep["slides"]):
        numerote = len(s["beats"]) > 1 and all(b[0][:2].strip(". ").isdigit() for b in s["beats"])
        for bi, (ecran, _) in enumerate(s["beats"]):
            texte = ecran.split(". ", 1)[1] if numerote and ". " in ecran else ecran
            cartes[(si, bi)] = carte_ligne(bi + 1 if numerote else None, texte, compact=len(s["beats"]) >= 4)
    bases = {"question": ecran_question(ep, serie), "resume": ecran_resume(ep, serie), "fin": ecran_fin(ep, serie)}
    def base_slide(si, jusqua):
        cle = ("slide", si, jusqua)
        if cle not in bases:
            im = ecran_slide(ep, serie, ep["slides"][si]["t"])
            for bi in range(jusqua):
                c = cartes[(si, bi)]; im.paste(c, (110, y_carte(si, bi)), c)
            bases[cle] = im
        return bases[cle]
    def y_carte(si, bi):
        compact = len(ep["slides"][si]["beats"]) >= 4
        y = 370
        for k in range(bi): y += cartes[(si, k)].height + (14 if compact else 22)
        return y
    # 6. les images, envoyées directement à ffmpeg
    mp4 = SORTIE / f"MF{ep['n']:02d}-{ep['slug']}.mp4"
    ff = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-i", str(dos / "voix.wav"), "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                           "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", "-shortest", str(mp4)], stdin=subprocess.PIPE)
    n_images = int(fin * FPS)
    k = 0
    for f in range(n_images):
        ts = f / FPS
        while k + 1 < len(tl) and ts >= tl[k + 1]["a"] - 0.5: k += 1
        r = tl[k]
        if r["kind"] == "slide":
            si, bi = r["ref"]
            im = base_slide(si, bi).copy()
            c = cartes[(si, bi)]
            p = min(1.0, max(0.0, (ts - (r["a"] - 0.3)) / 0.45))
            p = 1 - (1 - p) ** 3
            if p > 0:
                c2 = c.copy(); c2.putalpha(c.split()[3].point(lambda v: int(v * p)))
                im.paste(c2, (110, y_carte(si, bi) + int(40 * (1 - p))), c2)
        else:
            im = bases[r["kind"]].copy()
            # fondu d'entrée de chaque nouvel écran
            p = min(1.0, max(0.0, (ts - (r["a"] - 0.5)) / 0.4))
            if p < 1:
                im = Image.blend(FOND, im, p)
        if r["a"] - 0.05 <= ts <= r["b"] + 0.3 and r["kind"] != "fin":
            sous_titre(im, r["txt"])
        barre(im, ts / fin)
        ff.stdin.write(im.tobytes())
    ff.stdin.close(); ff.wait()
    (SORTIE / f"MF{ep['n']:02d}-{ep['slug']}.srt").write_text("\n".join(srt), encoding="utf-8")
    miniature(ep, SORTIE / f"MF{ep['n']:02d}-{ep['slug']}-miniature.jpg")
    return mp4, fin

def main():
    global FOND
    d = yaml.safe_load(open(ICI / "episodes.yaml", encoding="utf-8"))
    SORTIE.mkdir(parents=True, exist_ok=True); TRAVAIL.mkdir(parents=True, exist_ok=True)
    FOND = fond()
    choix = {int(a) for a in sys.argv[1:]}
    for ep in d["episodes"]:
        if choix and ep["n"] not in choix: continue
        mp4, fin = fabriquer(ep, d["serie"], d["outro"])
        print(f"{mp4.name}  {fin:.0f} s")

if __name__ == "__main__":
    main()
