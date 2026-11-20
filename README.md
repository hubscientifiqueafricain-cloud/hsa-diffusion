# HSA · outil de diffusion multi-réseaux

Outil maison du Hub Scientifique Africain pour planifier et diffuser ses contenus sur tous les
réseaux, dans tous les formats, avec un plan B automatique quand un canal bloque.

## Comment ça marche

1. **Médiathèque** : `media/catalogue.json` liste les 120 affiches du blog avec leur URL publique
   (hébergées par Wix) et le lien de l'article. Les déclinaisons de format sont publiées sur
   GitHub Pages (`site/declinaisons/`), donc elles aussi ont une URL publique.
2. **Calendrier** : un fichier YAML par publication dans `calendrier/posts/`
   (voir l'exemple). Statuts : `brouillon` → `prevu` → `publie` / `manuel` / `echec`.
3. **Formats** : chaque visuel est décliné en carré 1:1, portrait 4:5, story 9:16, paysage 16:9
   et Pinterest 2:3, sans rien couper (fond flou). Le bon format est choisi pour chaque réseau.
4. **Robot** : toutes les 15 minutes, GitHub Actions publie ce qui est dû. Pour chaque réseau, il
   essaie l'API directe, puis Metricool, puis la publication manuelle assistée, et ouvre une
   alerte (issue GitHub, reçue par e-mail) dès qu'un plan B a servi.
5. **Tableau de bord** : `https://<compte>.github.io/hsa-diffusion/` affiche le calendrier, l'état
   de chaque réseau et, pour les publications manuelles, le texte prêt à copier.

## Mise en route (une seule fois)

- Settings → Pages → Source : **GitHub Actions**.
- Settings → Secrets and variables → Actions : ajouter les clés des réseaux disponibles
  (aucune n'est obligatoire : un réseau sans clé passe directement au plan B).

| Secret | Réseau |
|---|---|
| `META_PAGE_TOKEN`, `META_PAGE_ID`, `IG_USER_ID` | Facebook, Instagram (app Meta) |
| `THREADS_TOKEN`, `THREADS_USER_ID` | Threads |
| `LINKEDIN_TOKEN`, `LINKEDIN_AUTEUR` | LinkedIn |
| `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CANAL` | Canal Telegram |
| `METRICOOL_TOKEN`, `METRICOOL_USER_ID` | Metricool (abonnement Advanced requis pour l'API) |

## Commandes utiles

```bash
pip install -r requirements.txt
python outils/generer_calendrier.py 2026-11-03 2      # brouillons à partir des affiches, 2 par jour
python publieur/publier.py --essai                    # simulation, rien n'est envoyé
python publieur/preparer.py                           # formats + tableau de bord en local
python outils/formats.py <image|URL> sortie/          # décliner un visuel à la main
```

## Micro-formations YouTube

Série « Valoriser ta recherche · 1 question, 2 minutes » : une question que les gens se posent sur
YouTube = une vidéo courte (16:9, voix off, sous-titres, miniature). Les scripts sont dans
`micro-formations/episodes.yaml`, les vidéos dans `media/micro-formations/`.

```bash
pip install edge-tts
python micro-formations/render.py            # refait les vidéos (ou : render.py 3 7 pour certains épisodes)
python micro-formations/calendrier.py 2026-11-03   # les place au calendrier, une par jour à 17h30
```

YouTube n'est pas encore relié à Metricool : tant que ce n'est pas fait, ces vidéos passent par le
poste de publication (titre, description, tags, miniature et sous-titres prêts à copier).

## Limites connues (imposées par les réseaux, pas par l'outil)

- Facebook/Instagram : rien ne passe par l'API tant que le contrôle de sécurité du compte Meta n'est pas levé.
- TikTok et YouTube : sans audit de l'application, les publications directes restent privées ; on passe par Metricool.
- LinkedIn page entreprise : nécessite l'accès « Community Management » (validation LinkedIn).
- Chaînes WhatsApp : aucune API ; publication manuelle assistée.
