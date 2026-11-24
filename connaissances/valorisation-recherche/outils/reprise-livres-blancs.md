# Reprise de la production des livres blancs (en pause depuis le 24/11, 14 h UTC, à la demande de l'utilisateur)

- Fait : 636 livres blancs vérifiés (Markdown dans ../livres-blancs-md/, PDF dans ../pdf/livres-blancs/, aussi sur GitHub branche claude/project-thread-4w7h03).
- Reste : les thèmes de catalogue.tsv qui n'ont pas de fichier OK.
- Pour reprendre : copier ce dossier dans un espace de travail, remettre les .md déjà faits dans lb/livres-blancs/, supprimer ceux que checklb.sh marque KO (inachevés), puis `python3 retrieve.py catalogue.tsv sources-par-theme.json` (déjà fait), `python3 mklb.py 6` et lancer des rédacteurs avec prompt-lb.txt, 3 lots par rédacteur, 5 à 8 en parallèle. Rendu : renderok.sh.
- Prévoir les limites d'usage : environ 200 livres blancs par fenêtre de 5 heures avec 8 rédacteurs.
- Reste à faire aussi : encadrés d'exemples pour les n° 1 à 518 ; corriger quelques mots_cles de plus de 70 caractères.
