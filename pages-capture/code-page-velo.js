// Code de page Wix (mode Dev) — identique pour /gagner-argent-memoire et /ambassadeurs.
// L'élément « Intégrer HTML » de la page doit s'appeler #captureHtml.
// Les inscriptions arrivent dans la collection CMS « Leads des pubs » (LeadsPubs)
// et dans les Contacts Wix (avec le numéro WhatsApp).
import wixData from 'wix-data';
import wixLocationFrontend from 'wix-location-frontend';
import wixWindowFrontend from 'wix-window-frontend';
import { contacts } from 'wix-crm-frontend';

$w.onReady(function () {
  const q = wixLocationFrontend.query || {};
  const campagne = [q.utm_source, q.utm_campaign, q.utm_content].filter(Boolean).join(' / ');

  $w('#captureHtml').onMessage((event) => {
    const d = event.data || {};
    if (d.type === 'hsa-open') {
      wixLocationFrontend.to(d.url);
      return;
    }
    if (d.type === 'hsa-scroll') {
      wixWindowFrontend.scrollTo(0, d.offset || 0);
      return;
    }
    if (d.type !== 'hsa-lead') {
      return;
    }
    wixData.insert('LeadsPubs', {
      source: d.source,
      prenom: d.prenom,
      nom: d.nom,
      whatsapp: d.whatsapp,
      email: d.email,
      niveau: d.niveau,
      discipline: d.discipline,
      sujet: d.sujet,
      universite: d.universite,
      campus: d.campus,
      motivation: d.motivation,
      campagne: campagne,
      statut: 'nouveau'
    }).catch((error) => console.error(error));
    contacts.appendOrCreateContact({
      name: { first: d.prenom || '', last: d.nom || '' },
      emails: d.email ? [{ email: d.email }] : [],
      phones: d.whatsapp ? [{ tag: 'MOBILE', countryCode: 'CI', phone: d.whatsapp }] : []
    }).catch((error) => console.error(error));
  });
});
