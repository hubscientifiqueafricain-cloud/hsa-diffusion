# Gabarit PDF HSA (commun aux bases de connaissances YouTube)

Charte reprise des PDF du blog : brun #230e02, jaune #ffcc00, orange #e16a00, crème #fbf4ea, polices Bricolage Grotesque et Plus Jakarta Sans (embarquées dans fonts/), logo HSA allégé. Page de garde brune, corps en A4, encadré final avec la signature HSA et le bouton « Rejoins HSA » ajoutés automatiquement. Environ 30 Ko par page.

## Usage
    pip install markdown   # une fois
    # tout un dossier (même arborescence, liens .md réécrits en .pdf, ne refait que ce qui a changé)
    python3 md_vers_pdf.py <dossier-md> <dossier-pdf> --tag "Livre blanc HSA · Valorisation de la recherche"
    # un seul fichier
    python3 md_vers_pdf.py --fichier doc.md sortie.pdf --tag "..."

## Format Markdown attendu (livres blancs)
    ---
    sous_titre: une phrase affichée en chapeau sur la page de garde
    meta_description: 150 caractères max (SEO)
    mots_cles: 4 à 6 mots-clés
    ---
    # Titre du livre blanc
    ## Résumé
    ...
- Le premier `# Titre` devient le titre de la page de garde (il n'est pas répété dans le corps).
- Les lignes « HSA, le réseau social scientifique n°1… » et « Rejoins HSA : … » sont retirées du corps car l'encadré final les ajoute.
- Un fichier placé dans un dossier `livres-blancs/` porte l'étiquette « Livre blanc » sur la couverture.
