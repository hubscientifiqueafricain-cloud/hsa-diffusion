"""Plan B : programmation via Metricool (marque HSA, blogId 7539292).
L'API Metricool demande un abonnement Advanced. Secrets : METRICOOL_TOKEN, METRICOOL_USER_ID.
Sans abonnement, Claude peut programmer les mêmes posts via le connecteur Metricool (voir README)."""
import os, datetime, requests

BLOG_ID = os.getenv("METRICOOL_BLOG_ID", "7539292")
RESEAUX_BRANCHES = set((os.getenv("METRICOOL_RESEAUX") or "facebook,tiktok").split(","))

class Metricool:
    def __init__(self, reseau): self.reseau, self.nom = reseau, f"Metricool ({reseau})"
    def dispo(self):
        return bool(os.getenv("METRICOOL_TOKEN") and os.getenv("METRICOOL_USER_ID")) and self.reseau in RESEAUX_BRANCHES
    def publier(self, post, reseau, texte, medias):
        quand = (datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None) + datetime.timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%S")
        info = {"text": texte, "providers": [{"network": self.reseau}], "media": medias, "autoPublish": True,
                "publicationDate": {"dateTime": quand, "timezone": "Africa/Abidjan"}, "draft": False,
                "shortener": False, "descendants": [], "smartLinkData": {"ids": []}}
        if self.reseau == "facebook": info["facebookData"] = {"type": "POST"}
        if self.reseau == "instagram": info["instagramData"] = {"type": "POST"}
        if self.reseau == "youtube":
            yt = post.get("youtube") or {}
            info["youtubeData"] = {"title": (yt.get("titre") or post.get("titre") or texte)[:100],
                                   "type": yt.get("type", "video"),
                                   "privacy": "public", "madeForKids": bool(yt.get("pour_enfants", False)),
                                   "tags": yt.get("tags", []), "category": yt.get("categorie", "EDUCATION")}
            info["media"] = [m for m in medias if m.lower().endswith((".mp4", ".mov"))][:1]
        if self.reseau == "tiktok": info["tiktokData"] = {"privacyOption": "PUBLIC_TO_EVERYONE", "title": texte[:90]}
        r = requests.post("https://app.metricool.com/api/v2/scheduler/posts", json=info, timeout=60,
                          params={"blogId": BLOG_ID, "userId": os.environ["METRICOOL_USER_ID"]},
                          headers={"X-Mc-Auth": os.environ["METRICOOL_TOKEN"]})
        if r.status_code >= 300: raise RuntimeError(r.text[:500])
        return f"metricool:{r.json().get('data', {}).get('id', 'programmé')}"
