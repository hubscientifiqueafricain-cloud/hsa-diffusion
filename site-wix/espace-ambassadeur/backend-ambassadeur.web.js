// Fichier backend Velo : backend/ambassadeur.web.js
// Renvoie au membre connecté son code ambassadeur, ses filleuls, ses gains, ses versements et son classement de la semaine.
import { Permissions, webMethod } from 'wix-web-module';
import { currentMember } from 'wix-members-backend';
import wixData from 'wix-data';

const SITE = 'https://www.hubscientifiqueafricain.com';
const OPTIONS = { suppressAuth: true };
const COMMISSION = 500;
const PAYES = ['Pass payé', 'versé'];
const TOP_BONUS = 10;

export const getMonEspace = webMethod(Permissions.SiteMember, async () => {
  const membre = await currentMember.getMember({ fieldsets: ['FULL'] });
  const email = (membre.loginEmail || '').toLowerCase();

  let res = await wixData.query('Ambassadeurs').eq('memberId', membre._id).find(OPTIONS);
  if (res.items.length === 0 && email) {
    res = await wixData.query('Ambassadeurs').eq('email', email).find(OPTIONS);
  }
  if (res.items.length === 0) {
    return { estAmbassadeur: false };
  }
  const amb = res.items[0];

  const filleuls = await wixData.query('Parrainages')
    .eq('codeAmbassadeur', amb.code)
    .descending('dateParrainage')
    .limit(1000)
    .find(OPTIONS);

  let gagne = 0;
  let verse = 0;
  const parVersement = {};
  const liste = filleuls.items.map((p) => {
    const paye = PAYES.includes(p.statut);
    const montant = paye ? (p.montant || COMMISSION) : 0;
    if (paye) gagne += montant;
    if (p.statut === 'versé') {
      verse += montant;
      const d = p.dateVersement || p._updatedDate;
      const cle = d ? new Date(d).toISOString().slice(0, 10) : 'inconnu';
      parVersement[cle] = (parVersement[cle] || 0) + montant;
    }
    return {
      nom: masquer(p.filleulNom),
      campus: p.campus || p.universite || '',
      statut: p.statut || 'inscrit',
      montant,
      prix: paye ? prixPaye(p) : 0,
      date: p.dateParrainage || p._createdDate
    };
  });

  const versements = Object.keys(parVersement)
    .filter((k) => k !== 'inconnu')
    .map((k) => ({ date: k, montant: parVersement[k] }));

  const classement = await classementSemaine(amb.code);

  return {
    estAmbassadeur: true,
    prenom: (membre.contactDetails && membre.contactDetails.firstName) || '',
    code: amb.code,
    lien: `${SITE}/chercheurs-premium?ref=${encodeURIComponent(amb.code)}`,
    nbFilleuls: liste.length,
    nbPayants: liste.filter((p) => PAYES.includes(p.statut)).length,
    totalGagne: gagne,
    totalVerse: verse,
    aVerser: gagne - verse,
    filleuls: liste,
    versements,
    rang: classement.rang,
    nbAmbassadeurs: classement.nbAmbassadeurs,
    top: TOP_BONUS,
    vuesTikTok: amb.vuesTikTok != null ? amb.vuesTikTok : null
  };
});

// Prix payé par l'étudiant : le champ de la collection s'il existe, sinon le tarif en vigueur à la date.
function prixPaye(p) {
  const v = p.prix || p.montantPaye || p.prixPass;
  if (v) return v;
  const d = new Date(p.dateParrainage || p._createdDate || Date.now());
  return d < new Date('2026-12-01T00:00:00Z') ? 2000 : 10000;
}

// Classement de la semaine (depuis lundi) au nombre de Pass payés
async function classementSemaine(monCode) {
  const lundi = new Date();
  lundi.setUTCHours(0, 0, 0, 0);
  lundi.setUTCDate(lundi.getUTCDate() - ((lundi.getUTCDay() + 6) % 7));
  const r = await wixData.query('Parrainages')
    .hasSome('statut', PAYES)
    .ge('dateParrainage', lundi)
    .limit(1000)
    .find(OPTIONS);
  const compte = {};
  r.items.forEach((p) => { compte[p.codeAmbassadeur] = (compte[p.codeAmbassadeur] || 0) + 1; });
  const nbAmbassadeurs = await wixData.query('Ambassadeurs').count(OPTIONS);
  const moi = compte[monCode] || 0;
  if (!moi) return { rang: null, nbAmbassadeurs };
  const devant = Object.values(compte).filter((n) => n > moi).length;
  return { rang: devant + 1, nbAmbassadeurs: Math.max(nbAmbassadeurs, Object.keys(compte).length) };
}

// Affiche « Awa K. » plutôt que le nom complet du filleul
function masquer(nom) {
  if (!nom) return 'Filleul';
  const parts = nom.trim().split(/\s+/);
  if (parts.length === 1) return parts[0];
  return `${parts[0]} ${parts[parts.length - 1].charAt(0).toUpperCase()}.`;
}
