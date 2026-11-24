"""Traduction gratuite hors ligne (modèles Argos Translate via CTranslate2, traitement par lots).
Usage : python3 traduire.py entree.json sortie.json"""
import json, sys, re, os, glob
import ctranslate2, sentencepiece as spm
PK = os.path.expanduser('~/.local/share/argos-translate/packages/')
def load(f, t):
    d = [p for p in glob.glob(PK + '*') if os.path.basename(p) in (f'translate-{f}_{t}-1_9', f'{f}_{t}')][0]
    sp = glob.glob(d + '/sentencepiece.model')
    return ctranslate2.Translator(d + '/model', device='cpu', inter_threads=1, intra_threads=4), (spm.SentencePieceProcessor(model_file=sp[0]) if sp else None), d
MODELS = {}
def tr(texts, f, t):
    if (f, t) not in MODELS: MODELS[(f, t)] = load(f, t)
    m, sp, d = MODELS[(f, t)]
    if sp is None:  # modèle BPE (es) : on passe par argos
        import argostranslate.translate as T
        return [T.translate(x, f, t) for x in texts]
    toks = [sp.encode(x, out_type=str) for x in texts]
    res = m.translate_batch(toks, beam_size=2, max_batch_size=32, max_decoding_length=256)
    return [sp.decode_pieces(r.hypotheses[0]).replace('\u2581',' ').strip() for r in res]
def chunks(segs, n=28):
    """Découpe en morceaux d'environ n mots, chacun avec son horodatage."""
    out, cur, start = [], [], None
    for s in segs:
        if start is None: start = s['t']
        cur += s['x'].split()
        if len(cur) >= n: out.append((start, ' '.join(cur))); cur, start = [], None
    if cur: out.append((start, ' '.join(cur)))
    return out
if __name__ == '__main__':
    d = json.load(open(sys.argv[1]))
    out = json.load(open(sys.argv[2])) if os.path.exists(sys.argv[2]) else {}
    todo = [k for k, r in d.items() if k not in out and not r.get('err') and r.get('orig') and not r['lang'].startswith('fr') and not isinstance(r.get('fr'), list) and r['lang'][:2] in ('en', 'es', 'pt', 'ar')]
    print(len(todo), 'à traduire', flush=True)
    for k in todo:
        r = dict(d[k]); lang = r['lang'][:2]
        ch = chunks(r['orig']); xs = [x for _, x in ch]
        if lang != 'en': xs = tr(xs, lang, 'en')
        fr = tr(xs, 'en', 'fr')
        r['fr'] = [{'t': t, 'x': y} for (t, _), y in zip(ch, fr)]
        r['frsrc'] = 'traduction automatique hors ligne (modèle libre Argos Translate)'
        out[k] = r
        json.dump(out, open(sys.argv[2], 'w'))
        print('ok', k, len(xs), flush=True)
