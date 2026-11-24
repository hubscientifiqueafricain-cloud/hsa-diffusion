# Consignes : livres blancs HSA « valorisation des résultats de la recherche »

Tu écris des livres blancs en français pour HSA (Hub Scientifique Africain). Chaque livre blanc traite UN thème précis (titre, public et angle donnés), et s'appuie sur des vidéos YouTube déjà analysées (fiches de lecture fournies). Public : celui indiqué, avec une attention particulière au contexte africain.

## Règles de fond
- Le livre blanc est un document ORIGINAL signé HSA, écrit avec la voix d'expert de HSA. Il s'inspire du contenu des vidéos (idées, méthodes, retours d'expérience, bonnes pratiques) mais NE MENTIONNE JAMAIS les vidéos, YouTube, les intervenants, les chaînes ni les conférences. Pas de citation entre guillemets attribuée à une personne, pas de liste de sources, pas de « selon un expert », pas de « dans une vidéo ».
- Reformule entièrement avec tes mots : aucune phrase recopiée ou quasi traduite d'une transcription.
- Tu peux évoquer des dispositifs, institutions et politiques publics et connus (OAPI, OMPI, Bayh-Dole, SATT, PCT, agences nationales, programmes de l'UE...) quand c'est utile, de façon factuelle et générale.
- Chiffres : n'utilise que des ordres de grandeur prudents ou des données publiques bien établies ; pas de chiffre précis tiré d'une seule vidéo, pas de chiffre « (à vérifier) ». Aucun fait inventé.
- Exemples : présente-les comme des cas types (« une université ouest-africaine qui... », « une jeune spin-off en biotechnologie... ») sans nommer de personne ni d'entreprise privée tirée des vidéos.
- Nourris chaque livre blanc d'au moins 3 fiches pertinentes (jusqu'à 8). Ignore les fiches hors thème.
- Points de droit à respecter : un brevet OAPI couvre les 17 États membres de l'OAPI, pas le monde ; ne jamais conseiller de compter sur un délai de grâce (protéger avant de publier).
- Français clair et concret, phrases complètes, pas de tirets cadratins (—), pas de jargon gratuit. Ton professionnel et engageant.

## Format du fichier Markdown (2 500 à 3 500 mots)
```
---
sous_titre: <une phrase qui dit ce que le lecteur va gagner>
meta_description: <150 caractères max, avec le mot-clé principal>
mots_cles: <4 à 6 mots-clés>
---

# <Titre>

## Résumé
<5 à 7 lignes : enjeu, idées clés, ce que propose le document>

## 1. Le constat
## 2. Ce que montrent les expériences
<cas types et modèles d'ici et d'ailleurs ; au moins un encadré `> À retenir : ...`>
## 3. Méthode pas à pas
<étapes numérotées, concrètes, actionnables>
## 4. Erreurs à éviter
<liste>
## 5. Application au contexte africain
<pays, institutions et dispositifs publics africains pertinents ; adaptation réaliste>
## 6. Plan d'action
<tableau Markdown : Étape | Qui | Quand | Résultat attendu>

## Conclusion
<5 à 8 lignes, mobilisatrices>
```
Ne mets PAS de signature HSA ni d'appel à l'action : la mise en page PDF les ajoute automatiquement.

## Vérification avant de rendre
Pour chaque fichier : longueur (wc -w entre 2 500 et 3 800), Résumé + 6 sections + Conclusion présents, AUCUNE mention de vidéo, YouTube, intervenant, chaîne, lien (grep -iE 'vid[eé]o|youtube|http|intervenant|conférencier' doit être vide), pas de tiret cadratin.
