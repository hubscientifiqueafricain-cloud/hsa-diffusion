# Consignes de rédaction : base HSA « valorisation des résultats de la recherche »

Tout est en français correct, clair, sans jargon inutile. Public : chercheurs, doctorants, responsables de valorisation, décideurs, surtout en Afrique francophone (mais les sources viennent du monde entier).
Ne jamais inventer : chaque fait, chiffre, nom vient de la transcription. Les transcriptions sont automatiques (et traduites automatiquement pour les vidéos non francophones) : si un chiffre ou un nom propre paraît déformé, ne le reprends pas, ou signale-le « (à vérifier) ». Pas de tirets cadratins (—) ; utilise des virgules, deux-points ou parenthèses.

## 1. Tri : la vidéo est-elle dans le sujet ?
Sujet strict : valorisation des résultats de la recherche (transfert de technologie, bureaux de transfert/TTO/SATT, brevets et PI des chercheurs et universités, licences, spin-offs/start-ups issues de la recherche, partenariats recherche-industrie, financement de la maturation/preuve de concept, politiques publiques de valorisation, impact sociétal de la recherche, chercheurs-entrepreneurs).
Hors sujet : PI générale sans lien avec la recherche (droit des marques, contrefaçon), « spin-off » d'entreprise, « valorisation » du patrimoine/des déchets/d'une entreprise, cours de droit génériques, vidéos sans contenu (musique, teaser), transcription inutilisable.
Pour chaque vidéo hors sujet : n'écris rien d'autre, ajoute juste une ligne au fichier de verdicts (voir §4) avec `ecartee`.

## 2. Fiche de lecture : `fiches/<nom>.md`
`<nom>` = exactement le nom du fichier de transcription (même slug, même `.md`).
Format :
```
# Fiche : <titre de la vidéo, traduit en français si besoin>
- Source : <chaîne>, <date>, <lien YouTube>, <zone : pays ou région>
- Intervenant(s) : <noms et fonctions si identifiables ; sinon « non identifiés »>
- Pertinence : forte | moyenne – <une phrase>
- Idées clés :
  - <6 à 12 puces, phrases complètes, concrètes>
- Chiffres et faits cités :
  - [m:ss] <fait> (les horodatages viennent des repères [m:ss] de la transcription)
- Exemples et cas concrets : <...>
- Citations :
  - [m:ss] « <citation reformulée en français correct> » (<qui>)
- Réutilisation HSA : <2 ou 3 idées : module de cours, post, webinaire...>

Transcription complète : [../transcriptions/<nom>.md](../transcriptions/<nom>.md)
```

## 3. Article prêt à publier : `articles/<nom>.md`
Un article de blog original (pas un résumé plat) de 600 à 900 mots, qui tire de la vidéo une leçon utile pour un chercheur ou une université, surtout en Afrique.
Format :
```
---
titre_seo: <60 caractères max, avec le mot-clé principal>
meta_description: <150 caractères max, incitative>
mots_cles: <4 à 6 mots-clés séparés par des virgules>
---

# <Titre accrocheur>

<Chapeau de 2-3 phrases>

## <Intertitre 1>
...
## <Intertitre 2 ou 3>
...
## À retenir
- <3 à 5 puces actionnables>

*Source : « <titre de la vidéo> », <chaîne>, <date>, <lien YouTube>. Pour aller plus loin : [la fiche de lecture](../fiches/<nom>.md), [la transcription complète](../transcriptions/<nom>.md) et [le guide HSA de la valorisation](../guide-valorisation-recherche.md).*

**HSA, le réseau social scientifique n°1 dédié à la valorisation des résultats de la recherche.**
Rejoins HSA : https://www.hubscientifiqueafricain.com
```
Les deux dernières lignes (signature et appel à l'action) sont obligatoires, à l'identique.

## 4. Fichier de verdicts
Pour CHAQUE vidéo traitée, ajoute une ligne (TSV, séparateur tabulation) à ton fichier de verdicts :
`<id YouTube>\t<retenue|ecartee>\t<zone (pays ou région, en français)>\t<raison courte si écartée>`

## 5. Vérification avant de rendre
Relis chaque fichier : français correct, liens relatifs exacts (nom de fichier identique à la transcription), signature présente dans chaque article, aucun chiffre inventé. Réponds à la fin avec seulement : nombre de vidéos retenues, écartées, et fichiers écrits.
