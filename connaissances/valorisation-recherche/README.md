# Base de connaissances HSA : valorisation des résultats de la recherche

Vidéos YouTube du monde entier (États-Unis, Europe, Afrique du Sud, Ghana, Bénin, Burkina Faso, Togo, Maroc, Côte d'Ivoire…) consacrées uniquement à la valorisation des résultats de la recherche : transfert de technologie, brevets, licences, spin-offs, partenariats avec l'industrie, politiques publiques.

## Ce que contient ce dossier

| Fichier | À quoi il sert |
|---|---|
| [guide-valorisation-recherche.md](guide-valorisation-recherche.md) | Le document exploitable : 12 fiches thématiques, une masterclass en 8 modules, 3 mini-cours, 10 posts prêts à publier, points de vigilance |
| [livre-blanc-valorisation-recherche-afrique.md](livre-blanc-valorisation-recherche-afrique.md) | Livre blanc HSA : constat, comparaison internationale, 10 leviers pour l'Afrique, recommandations par acteur |
| [fiches-par-video.md](fiches-par-video.md) | Une fiche de lecture par vidéo : idées clés, chiffres horodatés, cas concrets, citations |
| [index.md](index.md) | Liste de toutes les vidéos (date, zone, chaîne, lien, transcription) |
| [transcriptions/](transcriptions/) | Le texte intégral de chaque vidéo en français (et le texte original pour les vidéos en anglais) |
| [toutes-les-transcriptions-fr.md](toutes-les-transcriptions-fr.md) | Toutes les transcriptions françaises dans un seul fichier |
| `videos-traitees.json` | Registre des vidéos déjà traitées (utilisé par la veille) |
| [outils/veille.py](outils/veille.py) | Script de veille : liste les nouvelles vidéos candidates |

## Mise à jour continue

Une tâche planifiée tourne chaque semaine :

1. `python3 outils/veille.py > candidats.tsv` interroge YouTube avec 20 requêtes en français et en anglais (outil gratuit `yt-dlp`) et ne garde que les vidéos absentes de `videos-traitees.json` et de `outils/videos-ecartees.txt`.
2. Les candidats sont triés à la main : seules les vidéos qui traitent vraiment de valorisation de la recherche sont retenues ; les autres vont dans `outils/videos-ecartees.txt`.
3. Les sous-titres sont récupérés depuis un navigateur (YouTube bloque les serveurs cloud), puis traduits en français par la traduction automatique de YouTube.
4. La base est reconstruite (index, transcriptions), une fiche est rédigée pour chaque nouvelle vidéo, et le guide et le livre blanc sont enrichis si la vidéo apporte du nouveau.

## Fiabilité

Les transcriptions sont automatiques et les traductions aussi : chiffres et noms propres doivent être vérifiés dans la vidéo, au repère temporel indiqué, avant toute citation publique.
