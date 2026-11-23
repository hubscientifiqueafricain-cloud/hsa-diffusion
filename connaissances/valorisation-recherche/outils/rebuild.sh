#!/bin/bash
# Reconstruit la base avec tous les lots (+ traductions hors ligne) et les verdicts
cd /tmp/claude-0/-home-user/fa753fd5-3469-5b22-817f-79bcb2bc66b2/scratchpad
cat verdicts/*.tsv 2>/dev/null | awk -F'\t' '$2=="ecartee"' > ecartees.tsv
cat verdicts/*.tsv 2>/dev/null | awk -F'\t' '{print $1"\t"$3}' > zones-extra.tsv
FILES="dl/res2.json"
for f in $(ls dl/lot*.json | grep -v argos | sort); do FILES="$FILES $f"; a=${f%.json}-argos.json; [ -f $a ] && FILES="$FILES $a"; done
python3 -I build.py v1.json out $FILES
