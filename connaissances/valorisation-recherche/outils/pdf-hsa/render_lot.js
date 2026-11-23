// node render_lot.js jobs.json  -> rend une liste de pages HTML en PDF avec un seul Chromium
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const { jobs, footer, n } = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const b = await chromium.launch();
  let k = 0;
  async function worker() {
    const pg = await b.newPage();
    while (k < jobs.length) {
      const j = jobs[k++];
      try {
        await pg.goto('file://' + j.html, { waitUntil: 'load' });
        await pg.evaluate(() => document.fonts.ready);
        await pg.pdf({ path: j.pdf, format: 'A4', printBackground: true, preferCSSPageSize: true,
          displayHeaderFooter: false });
        console.log('OK ' + j.pdf);
      } catch (e) { console.log('ERR ' + j.pdf + ' ' + e.message); }
    }
    await pg.close();
  }
  await Promise.all(Array.from({ length: n || 3 }, worker));
  await b.close();
})();
