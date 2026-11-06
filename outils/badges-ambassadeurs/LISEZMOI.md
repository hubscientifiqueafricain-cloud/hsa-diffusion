# Badge officiel des campus ambassadeurs HSA

Génère, pour chaque ambassadeur validé :

| Fichier | Usage |
|---|---|
| `…-badge.png` | Le badge seul, fond transparent, 1620 × 2568 px (format carte 54 × 86 mm, imprimable). À envoyer à l'ambassadeur pour son profil, son statut, son CV. |
| `…-bienvenue-4x5.png` | Post « Bienvenue à notre nouvel ambassadeur » 1080 × 1350 (Facebook, Instagram, LinkedIn). |
| `…-bienvenue-9x16.png` | Story / statut WhatsApp 1080 × 1920. |
| `…-legende.txt` | Le texte du post, prêt à copier. |

Le style reprend la créa badge de la pub ambassadeurs (brun HSA, jaune, crème).
Tout s'adapte au genre (ambassadeur / ambassadrice) et aux noms ou universités longs.

## Générer

```bash
pip install -r requirements.txt qrcode
python3 outils/badges-ambassadeurs/generer.py outils/badges-ambassadeurs/exemple.json -o sortie/
```

Il faut Node et Playwright (Chromium) pour le rendu, et les polices Inter Display et JetBrains Mono.

Le fichier JSON contient un ambassadeur ou une liste (voir `exemple.json`) :

| Champ | Exemple | Obligatoire |
|---|---|---|
| `prenom`, `nom` | Aïcha, Koné | oui |
| `genre` | `F` ou `H` | non (H par défaut) |
| `universite` | Université Félix Houphouët-Boigny | oui |
| `ville`, `pays` | Abidjan, Côte d'Ivoire | conseillé |
| `niveau` | Master 1 · Biologie | non |
| `numero` | HSA-CI-001 | oui |
| `code` | HSA-AICHA26 (le code promo du CMS) | oui |
| `photo` | chemin local, URL, ou valeur `wix:image://…` du CMS | oui |
| `cadrage` | `50% 30%` pour remonter le visage dans le rond | non |

Le QR code du badge mène à la page Tarifs avec le suivi `utm_source=badge&utm_content=<code>`,
pour voir dans les statistiques les visites venues des badges de chaque ambassadeur.

## Numérotation

`HSA-<pays>-<rang>` : code pays à deux lettres puis rang de validation dans ce pays,
sur trois chiffres. HSA-CI-001, HSA-CI-002, HSA-SN-001, HSA-CM-001…
Un numéro attribué ne se réutilise jamais, même si l'ambassadeur quitte le programme.

## La photo : demandée à la validation, pas à la candidature

Le formulaire de candidature reste court (pas de photo). La photo est demandée
seulement aux candidats retenus, dans le message WhatsApp de validation
(modèle dans `message-validation.txt`). Consignes données à l'ambassadeur :
photo récente, visage de face et bien éclairé, fond clair et uni, sans filtre ni lunettes de soleil,
cadrée de la tête aux épaules.

Ensuite, dans le CMS Wix, collection **Ambassadeurs HSA** : déposer la photo dans le champ
« Photo du badge » et compléter prénom, genre, université, ville, pays, niveau et numéro de badge.
Ces champs se recopient depuis la candidature (collection Leads des pubs : `prenom`, `universite`,
`campus`, `niveau`).

## Circuit complet

1. Candidature validée : statut `actif` et code promo créés dans la collection Ambassadeurs.
2. Message WhatsApp de validation, avec la demande de photo.
3. Photo reçue : déposée dans le CMS, fiche complétée.
4. Génération du badge et des visuels, relecture (orthographe du nom, université).
5. Envoi du badge à l'ambassadeur, puis publication du post « Bienvenue » sur Facebook,
   Instagram, LinkedIn et en statut WhatsApp, en le taguant.
