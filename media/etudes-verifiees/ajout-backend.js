
// ---- Études revendiquées (ajout du 9 nov. 2026) ----
// Une revendication de la collection RevendicationsEtudes compte dès que son statut commence par « valid »
// (validé, validée…). Rien n'est copié : si le statut change, l'étude disparaît du profil et le badge aussi.
const estEtudeValidee = (s) => /^valid/i.test(String(s || '').trim());

async function revendicationsValidees(champ, valeur) {
  const r = await wixData.query('RevendicationsEtudes').eq(champ, valeur).limit(100).find(OPTS);
  return r.items.filter((it) => estEtudeValidee(it.statut));
}

async function profilPublic(memberId) {
  return safe(async () => {
    const r = await wixData.query('Members/PublicData').eq('_id', memberId).limit(1).find(OPTS);
    const p = r.items[0];
    return p && p.slug ? SITE + '/profile/' + p.slug + '/profile' : null;
  }, null);
}

// Badge de l'article : auteurs vérifiés d'une étude (visible par tous).
export const auteursVerifies = webMethod(Permissions.Anyone, async (postId) => {
  if (!postId) return [];
  return safe(async () => {
    const vals = await revendicationsValidees('postId', String(postId));
    return Promise.all(vals.map(async (v) => ({ nom: v.nom || 'Auteur vérifié', profil: await profilPublic(v.memberId) })));
  }, []);
});

// Études validées d'un membre, sous forme de cartes d'article (même format que « Mes articles »).
async function etudesRevendiquees(memberId) {
  return safe(async () => {
    const vals = await revendicationsValidees('memberId', memberId);
    const ids = [...new Set(vals.map((v) => v.postId).filter(Boolean))];
    if (!ids.length) return [];
    const r = await wixData.query('Blog/Posts').hasSome('_id', ids).limit(100).find(OPTS);
    return r.items.map((p) => Object.assign(postCard(p), { revendiquee: true }));
  }, []);
}

// Études validées d'un membre à partir de l'adresse de son profil public (/profile/<slug>/...).
export const etudesDuProfil = webMethod(Permissions.Anyone, async (slug) => {
  if (!slug) return [];
  return safe(async () => {
    const r = await wixData.query('Members/PublicData').eq('slug', String(slug)).limit(1).find(OPTS);
    const m = r.items[0];
    return m ? etudesRevendiquees(m._id) : [];
  }, []);
});
