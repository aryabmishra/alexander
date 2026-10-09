import os
import re

BASE_DIR = "/Users/aryabmishra/Downloads/Website Replicates/alexander-jankowski"

# 1. Update css/theme-navy.css
theme_css_path = os.path.join(BASE_DIR, "css", "theme-navy.css")
with open(theme_css_path, "r", encoding="utf-8") as f:
    theme_css = f.read()

insights_css_additions = """
/* ==========================================================================
   INSIGHTS & ARTICLE COMPONENTS
   ========================================================================== */
.insights-hero {
  background: radial-gradient(circle at 50% 10%, rgba(59, 130, 246, 0.15) 0%, rgba(0, 0, 0, 0) 60%), #000000 !important;
}

.hero-badge {
  color: #60A5FA !important;
  background-color: rgba(59, 130, 246, 0.15) !important;
  border: 1px solid #3B82F6 !important;
}

.filter-pill:hover,
.filter-pill.active {
  background-color: #2563EB !important;
  color: #FFFFFF !important;
  border-color: #3B82F6 !important;
  box-shadow: 0 4px 18px rgba(59, 130, 246, 0.35) !important;
}

.featured-card-wrap:hover {
  border-color: #3B82F6 !important;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.8), 0 0 25px rgba(59, 130, 246, 0.2) !important;
}

.featured-badge {
  background: #2563EB !important;
  color: #FFFFFF !important;
}

.featured-meta {
  color: #60A5FA !important;
}

.featured-card-wrap:hover .featured-title {
  color: #60A5FA !important;
}

.insight-card:hover {
  border-color: #3B82F6 !important;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7), 0 0 20px rgba(59, 130, 246, 0.2) !important;
}

.insight-thumb::before {
  background-color: #2563EB !important;
}

.insight-card:hover .insight-tag {
  border-color: #3B82F6 !important;
  color: #60A5FA !important;
}

.insight-card:hover .insight-card-title {
  color: #60A5FA !important;
}

.insight-footer-meta .reading-time {
  color: #60A5FA !important;
}

.modal-article-title {
  color: #60A5FA !important;
}

.modal-body blockquote {
  border-left-color: #3B82F6 !important;
}

::selection {
  background-color: #2563EB !important;
  color: #FFFFFF !important;
}

::-moz-selection {
  background-color: #2563EB !important;
  color: #FFFFFF !important;
}
"""

if "INSIGHTS & ARTICLE COMPONENTS" not in theme_css:
    theme_css += "\n" + insights_css_additions
    with open(theme_css_path, "w", encoding="utf-8") as f:
        f.write(theme_css)
    print("Updated css/theme-navy.css with insights components")

# 2. Update index.html
index_path = os.path.join(BASE_DIR, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    idx = f.read()

# Add theme-navy.css link if not present
if '<link href="css/theme-navy.css" rel="stylesheet">' not in idx:
    idx = idx.replace(
        '<link href="css/main.css" rel="stylesheet">',
        '<link href="css/main.css" rel="stylesheet">\n\t<link href="css/theme-navy.css" rel="stylesheet">'
    )

# Replace SVG paths
idx = idx.replace('images/text-animations/steven.svg', 'images/text-animations/steven-navy.svg')
idx = idx.replace('images/text-animations/bartlett.svg', 'images/text-animations/bartlett-navy.svg')
idx = idx.replace('images/pattern.svg', 'images/pattern-navy.svg')
idx = idx.replace('images/pattern2.svg', 'images/pattern2-navy.svg')
idx = idx.replace('images/arrow-right-bc1.svg', 'images/arrow-right-navy.svg')
idx = idx.replace('images/pattern-crop-left.svg', 'images/pattern-crop-left-navy.svg')
idx = idx.replace('images/pattern-crop-right.svg', 'images/pattern-crop-right-navy.svg')

# Fix inline style Mein Werdegang
idx = re.sub(
    r'(<div style="[^"]*color:\s*)#DBFF00([^"]*">Mein Werdegang</div>)',
    r'\g<1>#60A5FA\g<2>',
    idx
)

# Fix checkmark stroke in contact feedback
idx = idx.replace('stroke="#DBFF00"', 'stroke="#3B82F6"')

# Remove #color-switcher-bar
idx = re.sub(r'\s*<!-- Floating Color Palette Switcher for Alexander Review -->\s*<div id="color-switcher-bar">.*?</div>', '', idx, flags=re.DOTALL)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx)
print("Updated index.html to Royal Navy")

# 3. Update insights.html
insights_path = os.path.join(BASE_DIR, "insights.html")
with open(insights_path, "r", encoding="utf-8") as f:
    ins = f.read()

# Add theme-navy.css link if not present
if '<link href="css/theme-navy.css" rel="stylesheet">' not in ins:
    ins = ins.replace(
        '<link href="css/main.css" rel="stylesheet">',
        '<link href="css/main.css" rel="stylesheet">\n\t<link href="css/theme-navy.css" rel="stylesheet">'
    )

# Replace inline style colors in insights.html
ins = ins.replace('rgba(219, 255, 0, 0.08)', 'rgba(59, 130, 246, 0.12)')
ins = ins.replace('rgba(219, 255, 0, 0.12)', 'rgba(59, 130, 246, 0.15)')
ins = ins.replace('rgba(219, 255, 0, 0.15)', 'rgba(59, 130, 246, 0.2)')
ins = ins.replace('rgba(219, 255, 0, 0.25)', 'rgba(59, 130, 246, 0.35)')
ins = ins.replace('rgba(219, 255, 0, 0.3)', 'rgba(59, 130, 246, 0.35)')

# Specific color rules in insights.html
ins = re.sub(r'color:\s*#DBFF00', 'color: #60A5FA', ins)
ins = re.sub(r'border:\s*1px solid #DBFF00', 'border: 1px solid #3B82F6', ins)
ins = re.sub(r'border-color:\s*#DBFF00', 'border-color: #3B82F6', ins)
ins = re.sub(r'background:\s*#DBFF00', 'background: #2563EB', ins)
ins = re.sub(r'background-color:\s*#DBFF00', 'background-color: #2563EB', ins)
ins = re.sub(r'border-left:\s*3px solid #DBFF00', 'border-left: 3px solid #3B82F6', ins)
ins = re.sub(r'border-left-color:\s*#DBFF00', 'border-left-color: #3B82F6', ins)

# In filter pills and badges, make text white on active pill background
ins = ins.replace('.filter-pill:hover,\n\t\t.filter-pill.active {\n\t\t\tbackground-color: #2563EB;\n\t\t\tcolor: #000000;',
                  '.filter-pill:hover,\n\t\t.filter-pill.active {\n\t\t\tbackground-color: #2563EB;\n\t\t\tcolor: #ffffff;')
ins = ins.replace('.featured-badge {\n\t\t\tposition: absolute;\n\t\t\ttop: 20px;\n\t\t\tleft: 20px;\n\t\t\tbackground: #2563EB;\n\t\t\tcolor: #000000;',
                  '.featured-badge {\n\t\t\tposition: absolute;\n\t\t\ttop: 20px;\n\t\t\tleft: 20px;\n\t\t\tbackground: #2563EB;\n\t\t\tcolor: #ffffff;')

# Remove #color-switcher-bar
ins = re.sub(r'\s*<!-- Floating Color Palette Switcher for Alexander Review -->\s*<div id="color-switcher-bar">.*?</div>', '', ins, flags=re.DOTALL)

with open(insights_path, "w", encoding="utf-8") as f:
    f.write(ins)
print("Updated insights.html to Royal Navy")

# 4. Also fix variation-navy.html eyebrow and switcher
var_navy_path = os.path.join(BASE_DIR, "variation-navy.html")
if os.path.exists(var_navy_path):
    with open(var_navy_path, "r", encoding="utf-8") as f:
        v_navy = f.read()
    v_navy = re.sub(
        r'(<div style="[^"]*color:\s*)#DBFF00([^"]*">Mein Werdegang</div>)',
        r'\g<1>#60A5FA\g<2>',
        v_navy
    )
    v_navy = re.sub(r'\s*<!-- Floating Color Palette Switcher for Alexander Review -->\s*<div id="color-switcher-bar">.*?</div>', '', v_navy, flags=re.DOTALL)
    with open(var_navy_path, "w", encoding="utf-8") as f:
        f.write(v_navy)
    print("Updated variation-navy.html")
