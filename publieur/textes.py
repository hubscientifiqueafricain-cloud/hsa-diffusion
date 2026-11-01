"""Adapte le texte commun à chaque réseau (longueur, lien, hashtags)."""
LIMITES = {"x": 280, "telegram": 1024, "threads": 500, "instagram": 2200, "tiktok": 2200,
           "linkedin": 3000, "facebook": 5000, "whatsapp": 4000, "pinterest": 500}
LIEN_NON_CLIQUABLE = {"instagram", "tiktok"}

def adapter(post, reseau):
    perso = (post.get("textes") or {}).get(reseau)
    if perso:
        return perso.strip()
    texte = (post.get("texte") or "").strip()
    tags = " ".join("#" + h.lstrip("#") for h in post.get("hashtags") or [])
    lien = post.get("lien")
    if lien:
        lien_txt = "🔗 Lien dans la bio" if reseau in LIEN_NON_CLIQUABLE else lien
    else:
        lien_txt = ""
    lim = LIMITES.get(reseau, 5000)
    morceaux = [texte, lien_txt, tags]
    complet = "\n\n".join(m for m in morceaux if m)
    if len(complet) <= lim:
        return complet
    # trop long : on garde le lien, on raccourcit le texte, on retire les hashtags
    reste = lim - len(lien_txt) - 4
    court = texte if len(texte) <= reste else texte[: reste - 1].rsplit(" ", 1)[0] + "…"
    return "\n\n".join(m for m in [court, lien_txt] if m)
