// Rend une page HTML en PNG avec Chromium (Playwright).
// Usage : node rendu.js <page.html> <sortie.png> <largeur> <hauteur> <echelle> [transparent]
const { chromium } = require("playwright");

(async () => {
  const [page_html, sortie, w, h, echelle, transparent] = process.argv.slice(2);
  const navigateur = await chromium.launch();
  const page = await navigateur.newPage({
    viewport: { width: +w, height: +h },
    deviceScaleFactor: +echelle,
  });
  await page.goto("file://" + page_html);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(150);
  await page.screenshot({ path: sortie, omitBackground: transparent === "transparent" });
  await navigateur.close();
})();
