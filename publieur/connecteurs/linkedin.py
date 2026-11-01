"""LinkedIn (profil personnel, produit « Share on LinkedIn », ou page si l'accès entreprise est accordé).
Secrets : LINKEDIN_TOKEN, LINKEDIN_AUTEUR (urn:li:person:xxx ou urn:li:organization:xxx)."""
import os, requests

class LinkedIn:
    nom = "API LinkedIn"
    def dispo(self): return bool(os.getenv("LINKEDIN_TOKEN") and os.getenv("LINKEDIN_AUTEUR"))
    def publier(self, post, reseau, texte, medias):
        corps = {"author": os.environ["LINKEDIN_AUTEUR"], "commentary": texte, "visibility": "PUBLIC",
                 "distribution": {"feedDistribution": "MAIN_FEED", "targetEntities": [], "thirdPartyDistributionChannels": []},
                 "lifecycleState": "PUBLISHED", "isReshareDisabledByAuthor": False}
        if post.get("lien"):
            corps["content"] = {"article": {"source": post["lien"], "title": (post.get("texte") or "").split("\n")[0][:200]}}
        r = requests.post("https://api.linkedin.com/rest/posts", json=corps, timeout=60, headers={
            "Authorization": f"Bearer {os.environ['LINKEDIN_TOKEN']}", "LinkedIn-Version": "202501",
            "X-Restli-Protocol-Version": "2.0.0"})
        if r.status_code >= 300: raise RuntimeError(r.text)
        return "https://www.linkedin.com/feed/update/" + r.headers.get("x-restli-id", "")
