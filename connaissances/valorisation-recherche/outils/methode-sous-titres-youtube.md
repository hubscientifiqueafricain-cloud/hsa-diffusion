# Récupérer sous-titres + traduction française YouTube en masse (gratuit)

Constat : depuis le cloud, youtube-transcript-api et yt-dlp sont bloqués pour les sous-titres. La RECHERCHE yt-dlp marche depuis le cloud (`yt-dlp --flat-playlist --playlist-end 100 --print "%(id)s\t%(duration)s\t%(channel)s\t%(title)s" "https://www.youtube.com/results?search_query=..."`), pas les sous-titres.

Méthode qui marche : le navigateur intégré Claude sur le PC (outils `Claude_Browser__*`), sur une page `https://www.youtube.com/watch?v=...`.
L'URL `timedtext` a besoin d'un jeton `pot` lié à chaque vidéo : on le capte en interceptant la requête que fait le lecteur lui-même quand on active les sous-titres, puis on refait la requête avec `&fmt=json3` (original) et `&fmt=json3&tlang=fr` (traduction Google gratuite).

1. Ouvrir une vidéo YouTube dans le navigateur intégré, puis exécuter `grab.js` (même dossier) avec `javascript_tool`. Il définit `window.__grab(id)` et `window.__batch(ids)`.
2. Lancer `window.__batch(['id1','id2',...])` : résultats dans `window.__out` (objet id → {title, author, secs, date, lang, kind, orig:[{t,x}], fr:[{t,x}]}), progression dans `window.__prog`.
3. Exporter : `const b=new Blob([JSON.stringify(window.__out)]);const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='lot1.json';document.body.appendChild(a);a.click()` → le fichier arrive dans Téléchargements du PC (parfois d'abord en `.tmp`, attendre quelques secondes) → `device_stage_files` → `/mnt/user-data/uploads/Downloads/lot1.json` dans le conteneur.

Pièges :
- `tlang=fr` répond 429 après de nombreuses requêtes rapprochées : espacer, et relancer plus tard les vidéos en erreur (`fr` = 'ERR429').
- Vidéos multi-audio : elles ont des pistes doublées (de-DE, fr-FR) de mauvaise qualité ; `grab.js` choisit la piste originale (fr/en exacte) et traduit via tlang.
- Panneau du navigateur masqué : les `setTimeout` sont ralentis (jusqu'à 1 par minute). `grab.js` attend via MessageChannel et via des événements, pas via setTimeout.
