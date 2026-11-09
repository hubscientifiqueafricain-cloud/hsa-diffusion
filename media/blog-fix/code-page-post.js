// Page Blog « Post » : bandeau « Revendiquer cette étude » affiché seulement sur les articles de la catégorie Publications.
// 9 nov. 2026 : remplace le module « wix-blog-frontend » (introuvable, bloquait la génération du code)
// par une lecture de la collection Blog/Posts à partir de l'adresse de l'article.
import wixData from 'wix-data';
import wixLocationFrontend from 'wix-location-frontend';

const CATEGORIES_PUBLICATIONS = ['6a7707de9f91b1775fd10739', '17116fd6-d91b-4eba-b407-1aa19ef064e5'];

async function articleCourant() {
  const morceaux = wixLocationFrontend.path || [];
  const slug = decodeURIComponent(morceaux[morceaux.length - 1] || '');
  if (!slug) return null;
  const res = await wixData.query('Blog/Posts').eq('slug', slug).limit(1).find();
  return res.items[0] || null;
}

$w.onReady(async function () {
  let p = null;
  try { p = await articleCourant(); } catch (e) { console.error(e); p = null; }
  const cats = (p && p.categories) || [];
  const estPublication = cats.some((c) => CATEGORIES_PUBLICATIONS.includes(c && (c._id || c.id || c)));
  if (!p || !estPublication) {
    $w('#section2').collapse();
    return;
  }
  $w('#html1').onMessage((ev) => {
    if (ev.data && ev.data.type === 'revendiquer') {
      wixLocationFrontend.to('/revendiquer-une-%C3%A9tude?article=' + encodeURIComponent(p._id));
    }
  });
});
