import json,os,sys,glob
tag=sys.argv[1]; d=json.load(open(sys.argv[2])); size=int(sys.argv[3]) if len(sys.argv)>3 else 12
vt=json.load(open('out/videos-traitees.json'))
seen=set()
for f in glob.glob('verdicts/*.tsv'):
    seen|=set(l.split('\t')[0] for l in open(f))
ok=[(k,vt[k]['fichier']) for k in d if k in vt and vt[k].get('fichier') and k not in seen and not os.path.exists('out/fiches/'+vt[k]['fichier'])]
for i in range(0,len(ok),size):
    open(f'lots/{tag}_{i//size}','w').write(''.join(f"{k}\t{n}\n" for k,n in ok[i:i+size]))
print(len(ok), (len(ok)+size-1)//size)
