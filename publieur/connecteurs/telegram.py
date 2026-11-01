"""Canal Telegram via un bot. Secrets : TELEGRAM_BOT_TOKEN, TELEGRAM_CANAL (ex. @hsa_officiel)."""
import os, requests

class Telegram:
    nom = "Bot Telegram"
    def dispo(self): return bool(os.getenv("TELEGRAM_BOT_TOKEN") and os.getenv("TELEGRAM_CANAL"))
    def publier(self, post, reseau, texte, medias):
        base = f"https://api.telegram.org/bot{os.environ['TELEGRAM_BOT_TOKEN']}"
        canal = os.environ["TELEGRAM_CANAL"]
        if medias:
            r = requests.post(f"{base}/sendPhoto", data={"chat_id": canal, "photo": medias[0], "caption": texte}, timeout=60)
        else:
            r = requests.post(f"{base}/sendMessage", data={"chat_id": canal, "text": texte}, timeout=60)
        j = r.json()
        if not j.get("ok"): raise RuntimeError(j)
        return f"https://t.me/{canal.lstrip('@')}/{j['result']['message_id']}"
