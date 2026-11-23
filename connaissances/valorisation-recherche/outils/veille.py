#!/usr/bin/env python3
"""Veille YouTube : repère les vidéos sur la valorisation des résultats de la recherche, pas encore traitées.
Usage : python3 -I veille.py <dossier-base> [profondeur=20] [mode=date|pertinence|les2]
  profondeur : nombre de résultats lus par requête (20 pour la veille courante, 100+ pour constituer la base)
  mode : tri par date (nouveautés), par pertinence (fonds historique) ou les deux
Nécessite yt-dlp (gratuit) ; la recherche fonctionne depuis le cloud.
Sortie : TSV id, durée, chaîne, titre, requête — candidats à trier avant traitement."""
import json, subprocess, sys, os, urllib.parse
from concurrent.futures import ThreadPoolExecutor
base = sys.argv[1]
depth = int(sys.argv[2]) if len(sys.argv) > 2 else 20
mode = sys.argv[3] if len(sys.argv) > 3 else 'date'
done = set(json.load(open(os.path.join(base, 'videos-traitees.json'))))
rej_path = os.path.join(base, 'outils', 'videos-ecartees.txt')
rejected = set(l.split('\t')[0].strip() for l in open(rej_path)) if os.path.exists(rej_path) else set()
REQ = [
 # anglais
 "technology transfer university", "research commercialization university", "university spinout",
 "academic entrepreneurship spin-off", "university patent licensing", "tech transfer office",
 "Bayh-Dole", "knowledge transfer partnership research", "lab to market deep tech university",
 "research commercialization Africa", "technology transfer Africa university", "AUTM technology transfer",
 "intellectual property university researchers", "commercializing research startup founder scientist",
 "research impact industry collaboration university", "proof of concept fund university",
 "technology transfer Nigeria", "technology transfer Kenya", "technology transfer South Africa university",
 "research commercialisation Ghana", "innovation research Ethiopia university commercialization",
 "WIPO technology transfer", "university innovation ecosystem spin-off India",
 # français
 "valorisation de la recherche", "valorisation des résultats de la recherche", "transfert de technologie recherche",
 "SATT valorisation", "start-up issue de la recherche", "brevet chercheur université",
 "valorisation recherche Côte d'Ivoire", "valorisation recherche Afrique", "propriété intellectuelle université Afrique",
 "valorisation recherche Sénégal", "valorisation recherche Cameroun", "valorisation recherche Bénin",
 "valorisation recherche Burkina Faso", "valorisation recherche Maroc", "valorisation recherche Tunisie",
 "valorisation recherche Algérie", "valorisation recherche Québec", "chercheur entrepreneur deeptech",
 "maturation projet de recherche", "OAPI brevet innovation chercheurs", "innovation universitaire incubateur",
 # espagnol, portugais, arabe
 "transferencia de tecnología universidad", "valorización de la investigación", "spin-off universitaria",
 "transferência de tecnologia universidade", "valorização da pesquisa", "inovação universidade patente",
 "نقل التكنولوجيا الجامعة", "تثمين البحث العلمي",
]
SORT = {'date': ['sp=CAI%3D&'], 'pertinence': [''], 'les2': ['sp=CAI%3D&', '']}[mode]
def run(args):
    q, sp = args
    url = "https://www.youtube.com/results?" + sp + "search_query=" + urllib.parse.quote_plus(q)
    out = subprocess.run(["yt-dlp", "--flat-playlist", "--playlist-end", str(depth), "--print",
                          "%(id)s\t%(duration)s\t%(channel)s\t%(title)s", url], capture_output=True, text=True).stdout
    return q, out
seen = {}
with ThreadPoolExecutor(6) as ex:
    for q, out in ex.map(run, [(q, sp) for q in REQ for sp in SORT]):
        for line in out.splitlines():
            p = line.split('\t')
            if len(p) < 4 or p[0] in done or p[0] in rejected or p[0] in seen: continue
            try: dur = float(p[1])
            except ValueError: dur = 0
            if dur and dur < 120: continue   # trop court (Shorts, bandes-annonces)
            seen[p[0]] = (p[0], p[1], p[2], p[3], q)
for v in seen.values(): print('\t'.join(v))
