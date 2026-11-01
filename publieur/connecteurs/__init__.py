"""Un connecteur = une façon de publier. Chaque connecteur expose :
   dispo() -> bool   (les clés nécessaires sont-elles configurées ?)
   publier(post, reseau, texte, medias) -> str  (lien ou identifiant du post publié)
et lève une exception en cas d'échec, ce qui déclenche le plan B suivant.
"""
from . import meta, telegram, linkedin, metricool, manuel

# Ordre d'essai par réseau : API directe d'abord, puis Metricool, puis publication manuelle assistée.
CHAINES = {
    "facebook":  [meta.Facebook(), metricool.Metricool("facebook"), manuel.Manuel()],
    "instagram": [meta.Instagram(), metricool.Metricool("instagram"), manuel.Manuel()],
    "threads":   [meta.Threads(), metricool.Metricool("threads"), manuel.Manuel()],
    "tiktok":    [metricool.Metricool("tiktok"), manuel.Manuel()],
    "youtube":   [metricool.Metricool("youtube"), manuel.Manuel()],
    "linkedin":  [linkedin.LinkedIn(), metricool.Metricool("linkedin"), manuel.Manuel()],
    "x":         [metricool.Metricool("twitter"), manuel.Manuel()],
    "pinterest": [metricool.Metricool("pinterest"), manuel.Manuel()],
    "telegram":  [telegram.Telegram(), manuel.Manuel()],
    "whatsapp":  [manuel.Manuel()],   # pas d'API pour les Chaînes WhatsApp
}
