// Page « Profil » (espace membres) : bloc « Études vérifiées » sous le profil public.
// Liste les études du blog dont la revendication de ce membre est validée (RevendicationsEtudes, statut « validé… »).
import wixLocationFrontend from 'wix-location-frontend';
import { etudesDuProfil } from 'backend/hsaDashboard.web';
import { currentMember } from 'wix-members-frontend';

const BLOC = '#htmlEtudes';

$w.onReady(async function () {
  const bloc = $w(BLOC);
  // Adresse du profil : /profil/<slug>/profile (ou /profil/my/profile pour son propre profil).
  const morceaux = (wixLocationFrontend.path || []).map((s) => decodeURIComponent(s));
  let slug = morceaux.find((s) => !['profil', 'profile', 'my'].includes(s)) || '';
  if (!slug && morceaux.includes('my')) {
    const m = await currentMember.getMember().catch(() => null);
    slug = (m && m.profile && m.profile.slug) || '';
  }
  let items = [];
  try { items = slug ? (await etudesDuProfil(slug)) || [] : []; } catch (e) { console.error(e); }
  if (!items.length) {
    bloc.collapse();
    return;
  }
  const envoyer = () => bloc.postMessage({ type: 'etudes', items });
  bloc.onMessage((ev) => {
    const d = ev.data || {};
    if (d.type === 'pret') envoyer();
    if (d.type === 'ouvrir' && d.url) wixLocationFrontend.to(d.url);
  });
  envoyer();
});
