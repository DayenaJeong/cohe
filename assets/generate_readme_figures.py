"""Generate README-only SVGs from fixed, already reported paper values.

No experiment inputs are read and no statistics are recomputed.
Run: python assets/generate_readme_figures.py
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parent
NAVY, BLUE, TEAL, AMBER, GRAY, RULE = '#243d57', '#27618f', '#10796f', '#995d20', '#596978', '#dce3e9'


def text(x, y, value, size=20, fill=NAVY, weight=None, anchor=None):
    attrs = f'x="{x}" y="{y}" font-size="{size}" fill="{fill}"'
    if weight: attrs += f' font-weight="{weight}"'
    if anchor: attrs += f' text-anchor="{anchor}"'
    return f'<text {attrs}>{escape(value)}</text>'


def line(x1, y1, x2, y2, color=RULE, width=1):
    return f'<path d="M{x1} {y1}H{x2}" stroke="{color}" stroke-width="{width}"/>' if y1 == y2 else f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="{width}"/>'


def svg(name, width, height, title, desc, body):
    xml = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">
  <title id="title">{escape(title)}</title>
  <desc id="description">{escape(desc)}</desc>
  <defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7" fill="{GRAY}"/></marker></defs>
  <rect width="{width}" height="{height}" fill="#fff"/>
  <g font-family="Arial, Helvetica, sans-serif">
    {''.join(body)}
  </g>
</svg>
'''
    (OUT / name).write_text(xml)


framework_desc = ('A proxy–target–protocol audit tuple feeds G1 Dependence, G2 Held-out prediction, and G3 Operational transfer in parallel, not as a sequential cascade. '
                  'The DINOv2 example has first-learning rho 0.4363 and held-out R squared 0.2126, yet 10% hard-only accuracy selection loses 14.87 percentage points versus Random. '
                  'First-learning and selection accuracy are distinct targets. The supported tier is Target-specific relation. '
                  'Joint evidence maps to one of six reporting tiers: Validated surrogate; Predictive validity only; Target-specific relation; Operational-only effect; Weak evidence; No reliable transfer. '
                  'An unmeasured gate is not a failed gate. G3 alone can support Operational-only effect.')

b = [text(32, 32, 'THE COHE AUDIT', 15, GRAY), text(32, 78, 'Prediction does not guarantee utility.', 34, NAVY, 600),
     text(32, 121, 'Audit tuple: Proxy + Target + Protocol', 20), text(1088, 121, 'Three separately evaluated gates', 17, GRAY, anchor='end'),
     '<path d="M560 135V155M182 155H938M182 155V183M560 155V183M938 155V183" fill="none" stroke="#9aa8b5" stroke-width="1.3"/>']
gates = [(32, BLUE, 'G1  Dependence', 'Does it align?', 'Rank association', 'ρ = 0.4363', 'First-learning target', ''),
         (410, TEAL, 'G2  Held-out prediction', 'Does it predict?', 'Held-out predictive power', 'R² = 0.2126', 'First-learning target', ''),
         (788, AMBER, 'G3  Operational transfer', 'Does it help?', 'Gain vs. matched baseline', '−14.87 pp', '10% hard-only accuracy', 'versus Random')]
for x, color, label, question, definition, metric, scope, second in gates:
    b += [line(x, 191, x + 300, 191, color, 3), text(x, 224, label, 21, color, 600), text(x, 263, question, 28, NAVY, 600), text(x, 292, definition, 18, GRAY),
          text(x, 370, metric, 39, color, 600), text(x, 403, scope, 20), text(x, 428, second, 17, GRAY)]
b += [text(32, 330, 'DINOv2 example · CIFAR-100', 16, GRAY),
      '<path d="M182 442V454H938V442M560 454V472" fill="none" stroke="#9aa8b5" stroke-width="1.3" marker-end="url(#arrow)"/>',
      text(32, 508, 'SUPPORTED REPORTING TIER', 16, GRAY), text(1088, 509, 'Target-specific relation', 27, NAVY, 600, 'end'),
      text(32, 545, 'G1/G2 concern first-learning; G3 tests accuracy selection. The tier reflects their joint evidence.', 17, GRAY)]
svg('cohe-framework.svg', 1120, 568, 'COHE: prediction does not guarantee utility', framework_desc, b)

b = [text(24, 32, 'THE COHE AUDIT', 15, GRAY), text(24, 76, 'Prediction does not', 31, NAVY, 600), text(24, 113, 'guarantee utility.', 31, NAVY, 600),
     text(24, 158, 'Audit tuple', 17, GRAY), text(24, 188, 'Proxy + Target + Protocol', 24),
     '<path d="M240 204V219H16V610" fill="none" stroke="#9aa8b5" stroke-width="1.3"/>', text(24, 250, 'DINOv2 example · CIFAR-100', 18, GRAY)]
for y, color, label, metric, scope in [(290, BLUE, 'G1  Dependence', 'ρ = 0.4363', 'First-learning target'), (435, TEAL, 'G2  Held-out prediction', 'R² = 0.2126', 'First-learning target'), (580, AMBER, 'G3  Operational transfer', '−14.87 pp', '10% hard-only accuracy vs. Random')]:
    b += [f'<path d="M16 {y+30}H40" fill="none" stroke="#9aa8b5" stroke-width="1.3" marker-end="url(#arrow)"/>',
          line(48, y-16, 456, y-16, color, 2), text(48, y+16, label, 23, color, 600), text(48, y+62, metric, 36, color, 600), text(48, y+94, scope, 21),
          line(456, y+30, 470, y+30, '#9aa8b5', 1.3)]
b += ['<path d="M470 320V710H240V733" fill="none" stroke="#9aa8b5" stroke-width="1.3" marker-end="url(#arrow)"/>',
      text(24, 766, 'SUPPORTED REPORTING TIER', 17, GRAY), text(24, 803, 'Target-specific relation', 29, NAVY, 600),
      text(24, 846, 'G1/G2: first-learning. G3: accuracy.', 21, GRAY), text(24, 877, 'Separate gates; combined evidence.', 21, GRAY)]
svg('cohe-framework-mobile.svg', 480, 904, 'COHE evidence gates: mobile teaser', framework_desc, b)

summary_desc = ('Four representative COHE audit settings, paper Table 6. Generative proxies: weak CE/margin dependence and prediction, multi-proxy CE R squared about 0.0002, no consistent protocol-stable transfer; No reliable transfer. '
                'DINOv2: first-learning rho 0.4363, R squared 0.2126; CIFAR-100/ResNet-18 10% hard-only accuracy selection loses 14.87 percentage points versus Random; Target-specific relation. '
                'Cross-architecture CE: rho 0.856–0.914, G2/G3 not evaluated; Weak evidence (G1 only). '
                'ImageNet-1K retrieval/triage positive control: rho 0.578, R squared 0.5637, top-10% recall 62.48%, enrichment 6.25 times; Validated surrogate for retrieval/triage only. '
                'Not evaluated is distinct from failed. DINOv2 first-learning and accuracy are distinct targets.')
b = [line(560, 16, 560, 569), line(32, 293, 1088, 293)]
b += [text(32, 43, 'Generative proxies → CE / margin', 25, NAVY, 600), text(32, 94, 'R² ≈ 0.0002', 36, TEAL, 600), text(32, 125, 'G2 · multi-proxy CE prediction', 18, GRAY),
      text(32, 166, 'G1  Weak dependence', 20, BLUE), text(32, 200, 'G3  No consistent protocol-stable transfer', 19, AMBER), text(32, 239, 'SUPPORTED TIER', 14, GRAY), text(32, 269, 'No reliable transfer', 24, NAVY, 600)]
b += [text(600, 43, 'DINOv2 → first-learning', 25, NAVY, 600), text(600, 94, 'ρ 0.4363', 32, BLUE, 600), text(856, 94, 'R² 0.2126', 32, TEAL, 600),
      text(600, 125, 'G1 · dependence', 18, GRAY), text(856, 125, 'G2 · prediction', 18, GRAY), text(600, 171, '−14.87 pp', 33, AMBER, 600), text(818, 171, 'G3 · 10% hard-only', 20, AMBER),
      text(600, 201, 'CIFAR-100 / ResNet-18 accuracy vs. Random', 18, GRAY), text(600, 239, 'SUPPORTED TIER', 14, GRAY), text(600, 269, 'Target-specific relation', 24, NAVY, 600)]
b += [text(32, 338, 'Cross-architecture CE ranking', 25, NAVY, 600), text(32, 389, 'ρ 0.856–0.914', 36, BLUE, 600), text(32, 420, 'G1 · rank association', 18, GRAY),
      text(32, 466, 'G2 / G3  Not evaluated', 22, GRAY), text(32, 514, 'SUPPORTED TIER', 14, GRAY), text(32, 544, 'Weak evidence', 24, NAVY, 600), text(239, 544, 'G1 only', 19, GRAY)]
b += [text(600, 338, 'ImageNet-1K retrieval / triage', 25, NAVY, 600), text(600, 389, 'ρ 0.578', 32, BLUE, 600), text(856, 389, 'R² 0.5637', 32, TEAL, 600),
      text(600, 420, 'G1 · dependence', 18, GRAY), text(856, 420, 'G2 · prediction', 18, GRAY), text(600, 466, '62.48% recall', 33, AMBER, 600), text(600, 496, 'G3 · top-10% budget; 6.25× enrichment', 18, GRAY),
      text(600, 531, 'SUPPORTED TIER', 14, GRAY), text(600, 561, 'Validated surrogate', 24, NAVY, 600), text(600, 589, 'for retrieval / triage only', 19, GRAY)]
b += [line(32, 611, 1088, 611), text(32, 641, 'Paper Table 6. DINOv2 G1/G2 concern first-learning; G3 concerns accuracy selection.', 18, GRAY)]
svg('cohe-results-summary.svg', 1120, 664, 'Four COHE audits: different levels of support', summary_desc, b)

b = []
for y in [301, 612, 884]: b.append(line(24, y, 456, y))
b += [text(24, 37, 'Generative proxies', 27, NAVY, 600), text(24, 67, '→ CE / margin', 21, GRAY), text(24, 116, 'R² ≈ 0.0002', 36, TEAL, 600), text(24, 146, 'G2 · multi-proxy CE prediction', 21, GRAY),
      text(24, 184, 'G1  Weak dependence', 22, BLUE), text(24, 218, 'G3  No consistent protocol-stable', 21, AMBER), text(60, 246, 'transfer under tested policies', 21, AMBER), text(24, 281, 'No reliable transfer', 25, NAVY, 600)]
b += [text(24, 341, 'DINOv2 → first-learning', 27, NAVY, 600), text(24, 393, 'ρ 0.4363', 34, BLUE, 600), text(252, 393, 'R² 0.2126', 34, TEAL, 600), text(24, 425, 'G1 · dependence', 20, GRAY), text(252, 425, 'G2 · prediction', 20, GRAY),
      text(24, 476, '−14.87 pp', 36, AMBER, 600), text(24, 510, 'G3 · 10% hard-only accuracy vs. Random', 21, AMBER), text(24, 543, 'CIFAR-100 / ResNet-18', 20, GRAY), text(24, 584, 'Target-specific relation', 25, NAVY, 600)]
b += [text(24, 652, 'Cross-architecture CE ranking', 26, NAVY, 600), text(24, 706, 'ρ 0.856–0.914', 36, BLUE, 600), text(24, 739, 'G1 · rank association', 21, GRAY), text(24, 782, 'G2 / G3  Not evaluated', 23, GRAY), text(24, 841, 'Weak evidence', 25, NAVY, 600), text(233, 841, 'G1 only', 21, GRAY)]
b += [text(24, 924, 'ImageNet-1K retrieval / triage', 26, NAVY, 600), text(24, 976, 'ρ 0.578', 34, BLUE, 600), text(252, 976, 'R² 0.5637', 34, TEAL, 600), text(24, 1008, 'G1 · dependence', 20, GRAY), text(252, 1008, 'G2 · prediction', 20, GRAY),
      text(24, 1060, '62.48% recall', 36, AMBER, 600), text(24, 1095, 'G3 · top-10% budget; 6.25× enrichment', 21, AMBER), text(24, 1140, 'Validated surrogate', 25, NAVY, 600), text(24, 1172, 'for retrieval / triage only', 22, GRAY),
      line(24, 1202, 456, 1202), text(24, 1235, 'Paper Table 6; declared settings only.', 20, GRAY), text(24, 1265, 'DINOv2: first-learning ≠ accuracy target.', 20, GRAY)]
svg('cohe-results-summary-mobile.svg', 480, 1290, 'Four COHE audits: mobile summary', summary_desc, b)

for name, label, width, color in [('homepage', 'Homepage', 108, TEAL), ('paper', 'Paper', 79, BLUE), ('code', 'Code', 76, NAVY), ('checkpoints', 'Checkpoints', 127, AMBER), ('bibtex', 'BibTeX', 87, '#586675')]:
    content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="30" viewBox="0 0 {width} 30" role="img" aria-labelledby="title description">
  <title id="title">{label}</title><desc id="description">COHE {label} resource link</desc>
  <rect width="{width}" height="30" rx="4" fill="{color}"/>
  <text x="{width/2}" y="19.5" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="600" fill="#fff">{label}</text>
</svg>
'''
    (OUT / f'badge-{name}.svg').write_text(content)
print('Generated four responsive research SVGs and five local resource badges.')
