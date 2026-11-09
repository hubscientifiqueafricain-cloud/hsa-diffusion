// Code de page Wix (mode Dev) — v4, identique pour /gagner-argent-memoire-these et /ambassadeurs.
// L'élément « Intégrer HTML » de la page doit s'appeler #captureHtml.
// Nouveau en v2 : envoie les événements au Pixel Meta (via Wix > Marketing Integrations > Facebook Pixel)
//   - Lead             : quand le formulaire est envoyé
//   - InitiateCheckout : quand la personne clique sur « Payer » (page Pass Valoris)
//   - Contact          : quand la personne clique sur un bouton WhatsApp
// et enregistre le code de la pub (utm_content) dans la colonne « campagne » de LeadsPubs.
// Nouveaux champs : statutMemoire (statut du mémoire ou de la thèse) et codeInvitation (HSA-CESARDO26 par défaut).
// Depuis le 9 nov. : chaque page écrit dans sa propre liste CMS (CandidaturesAmbassadeurs ou InscriptionsValoris).
// Si l'écriture échoue, la fiche part dans LeadsPubs pour ne jamais perdre d'inscription.
// v4 (9 nov.) : le lien d'équipe ?equipe=HSA-PRENOM26 préremplit aussi le code d'invitation
// et l'enregistre dans le champ equipeCode de CandidaturesAmbassadeurs. ?code= marche toujours.
import wixData from 'wix-data';
import wixLocationFrontend from 'wix-location-frontend';
import wixWindowFrontend from 'wix-window-frontend';
import { contacts } from 'wix-crm-frontend';

function pixel(evenement, params) {
  try { wixWindowFrontend.trackEvent(evenement, params || {}); } catch (e) { console.error(e); }
}

$w.onReady(function () {
  const q = wixLocationFrontend.query || {};
  const campagne = [q.utm_source, q.utm_campaign, q.utm_content].filter(Boolean).join(' / ');

  // Code venu du lien : ?equipe= (lien d'équipe d'un ambassadeur) ou ?code= (lien d'ambassadeur).
  const nettoyer = (c) => String(c || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').trim().toUpperCase().replace(/[^A-Z0-9-]/g, '').slice(0, 30);
  const codeEquipe = nettoyer(q.equipe);
  const codeLien = codeEquipe || nettoyer(q.code);

  if (codeLien) {
    // Remplit le code d'invitation du formulaire.
    const envoyerCode = () => { try { $w('#captureHtml').postMessage({ type: 'hsa-code', code: codeLien }); } catch (e) { console.error(e); } };
    envoyerCode();
    setTimeout(envoyerCode, 1500);
    setTimeout(envoyerCode, 4000);
  }

  $w('#captureHtml').onMessage((event) => {
    const d = event.data || {};
    if (d.type === 'hsa-pret' && codeLien) {
      $w('#captureHtml').postMessage({ type: 'hsa-code', code: codeLien });
      return;
    }
    if (d.type === 'hsa-open') {
      wixLocationFrontend.to(d.url);
      return;
    }
    if (d.type === 'hsa-scroll') {
      wixWindowFrontend.scrollTo(0, d.offset || 0);
      return;
    }
    if (d.type === 'hsa-clic') {
      const lien = (d.lien || '').toLowerCase();
      if (lien.includes('payer')) {
        pixel('InitiateCheckout', { content_name: 'Pass Valoris', value: 2000, currency: 'XOF' });
      } else if (lien.includes('whatsapp') || lien.includes('confirmer')) {
        pixel('Contact', { content_name: d.source || '' });
      }
      return;
    }
    if (d.type !== 'hsa-lead') {
      return;
    }
    pixel('Lead', { content_name: d.source === 'ambassadeur' ? 'Candidature ambassadeur' : 'Pass Valoris', content_category: q.utm_content || '' });
    const fiche = {
      source: d.source,
      prenom: d.prenom,
      nom: d.nom,
      whatsapp: d.whatsapp,
      mobileMoney: d.mobilemoney,
      operateur: d.operateur,
      email: d.email,
      niveau: d.niveau,
      discipline: d.discipline,
      sujet: d.sujet,
      universite: d.universite,
      campus: d.campus,
      motivation: d.motivation,
      statutMemoire: d.statut,
      codeInvitation: d.code,
      campagne: campagne,
      statut: 'nouveau'
    };
    if (d.source === 'ambassadeur' && codeEquipe) {
      fiche.equipeCode = codeEquipe;
    }
    const liste = d.source === 'ambassadeur' ? 'CandidaturesAmbassadeurs' : 'InscriptionsValoris';
    wixData.insert(liste, fiche)
      .catch((error) => {
        console.error(error);
        return wixData.insert('LeadsPubs', fiche);
      })
      .catch((error) => console.error(error));
    contacts.appendOrCreateContact({
      name: { first: d.prenom || '', last: d.nom || '' },
      emails: d.email ? [{ email: d.email }] : [],
      phones: d.whatsapp ? [{ tag: 'MOBILE', countryCode: 'CI', phone: d.whatsapp }] : []
    }).catch((error) => console.error(error));
  });
});
