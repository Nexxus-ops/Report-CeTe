// Regenerate the report's SVG images locally; no data or sources are uploaded.
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const diagrams = path.resolve(__dirname, '../diagrams');
const config = JSON.parse(fs.readFileSync(path.join(diagrams, 'mermaid-config.json'), 'utf8'));
const mermaidBundle = path.join(path.dirname(require.resolve('mermaid')), 'mermaid.min.js');

(async () => {
  const channel = process.env.CETE_DIAGRAM_BROWSER || (process.platform === 'win32' ? 'msedge' : 'chromium');
  const browser = await chromium.launch({ channel, headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1600, height: 1200 } });
    await page.setContent('<!doctype html><html><head><meta charset="utf-8"></head><body></body></html>');
    await page.addScriptTag({ path: mermaidBundle });
    await page.evaluate(settings => mermaid.initialize(settings), config);
    const files = fs.readdirSync(diagrams).filter(file => file.endsWith('.mmd')).sort();
    for (const [index, file] of files.entries()) {
      const source = fs.readFileSync(path.join(diagrams, file), 'utf8');
      const svg = await page.evaluate(async ({ source, id }) => {
        await mermaid.parse(source);
        return (await mermaid.render(id, source)).svg;
      }, { source, id: `d${index}` });
      // An explicit white canvas preserves contrast in GitHub's dark theme.
      const opaque = svg.replace(/style="([^"]*)"/, (_, style) => `style="${style}; background-color: #FFFFFF;"`);
      fs.writeFileSync(path.join(diagrams, file.replace(/\.mmd$/, '.svg')), opaque);
      console.log(`Rendered ${file}`);
    }
    console.log(`PASS: ${files.length} diagrams parsed and rendered.`);
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
