"""Facebook (Page), Instagram (compte pro) et Threads via les API officielles de Meta.
Secrets : META_PAGE_TOKEN, META_PAGE_ID, IG_USER_ID, THREADS_TOKEN, THREADS_USER_ID."""
import os, time, requests

GRAPH = "https://graph.facebook.com/v20.0"

def _ok(r):
    j = r.json()
    if r.status_code >= 400 or "error" in j:
        raise RuntimeError(j.get("error", j))
    return j

class Facebook:
    nom = "API Facebook"
    def dispo(self): return bool(os.getenv("META_PAGE_TOKEN") and os.getenv("META_PAGE_ID"))
    def publier(self, post, reseau, texte, medias):
        pid, tok = os.environ["META_PAGE_ID"], os.environ["META_PAGE_TOKEN"]
        if medias:
            j = _ok(requests.post(f"{GRAPH}/{pid}/photos", data={"url": medias[0], "caption": texte, "access_token": tok}, timeout=60))
            return f"https://www.facebook.com/{j.get('post_id', j.get('id'))}"
        j = _ok(requests.post(f"{GRAPH}/{pid}/feed", data={"message": texte, "link": post.get("lien", ""), "access_token": tok}, timeout=60))
        return f"https://www.facebook.com/{j['id']}"

class Instagram:
    nom = "API Instagram"
    def dispo(self): return bool(os.getenv("META_PAGE_TOKEN") and os.getenv("IG_USER_ID"))
    def publier(self, post, reseau, texte, medias):
        if not medias: raise RuntimeError("Instagram exige une image ou une vidéo")
        ig, tok = os.environ["IG_USER_ID"], os.environ["META_PAGE_TOKEN"]
        c = _ok(requests.post(f"{GRAPH}/{ig}/media", data={"image_url": medias[0], "caption": texte, "access_token": tok}, timeout=60))
        time.sleep(5)
        j = _ok(requests.post(f"{GRAPH}/{ig}/media_publish", data={"creation_id": c["id"], "access_token": tok}, timeout=60))
        return f"instagram:{j['id']}"

class Threads:
    nom = "API Threads"
    def dispo(self): return bool(os.getenv("THREADS_TOKEN") and os.getenv("THREADS_USER_ID"))
    def publier(self, post, reseau, texte, medias):
        u, tok = os.environ["THREADS_USER_ID"], os.environ["THREADS_TOKEN"]
        d = {"text": texte, "access_token": tok, "media_type": "IMAGE" if medias else "TEXT"}
        if medias: d["image_url"] = medias[0]
        c = _ok(requests.post(f"https://graph.threads.net/v1.0/{u}/threads", data=d, timeout=60))
        time.sleep(5)
        j = _ok(requests.post(f"https://graph.threads.net/v1.0/{u}/threads_publish", data={"creation_id": c["id"], "access_token": tok}, timeout=60))
        return f"threads:{j['id']}"
