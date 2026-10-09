import os
import re

BASE_DIR = "/Users/aryabmishra/Downloads/Website Replicates/alexander-jankowski"

CALENDLY_URL = "https://calendly.com/aj-alexanderjankowski/get2know"

schedule_card_html = f'''						<div class="contact-card text-center" id="contact-form">
							<div class="contact-card-header text-center">
								<span class="contact-card-badge">CALENDLY &bull; 1:1 CALL</span>
								<h3 class="contact-card-title">Kennenlerngespräch vereinbaren</h3>
								<p class="contact-card-desc" style="max-width: 580px; margin: 0 auto 28px auto;">
									Buchen Sie direkt einen persönlichen 1:1 Kennenlern-Termin in meinem Kalender. Ich freue mich auf den direkten Austausch mit Ihnen.
								</p>
							</div>
							<div class="d-flex flex-wrap justify-content-center align-items-center gap-3">
								<a href="{CALENDLY_URL}" target="_blank" rel="noopener noreferrer" class="btn-submit-contact" style="text-decoration: none;">
									<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
										<rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
										<line x1="16" y1="2" x2="16" y2="6"></line>
										<line x1="8" y1="2" x2="8" y2="6"></line>
										<line x1="3" y1="10" x2="21" y2="10"></line>
									</svg>
									<span>Schedule a Call</span>
									<svg class="btn-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
								</a>
								<a href="https://www.linkedin.com/in/alexander-jankowski-03491242a/" target="_blank" rel="noopener noreferrer" class="btn2" style="padding: 0 32px; height: 52px; line-height: 48px; display: inline-flex; align-items: center; gap: 10px; text-decoration: none;">
									<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
									<span>LinkedIn</span>
								</a>
							</div>
						</div>'''

footer_social_call_html = f'''			<li class="social-item">
				<a href="{CALENDLY_URL}" target="_blank" rel="noopener noreferrer" class="social-link" aria-label="Schedule a Call">
					<div class="social-link-content">
						<svg class="social-icon" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
						<span class="social-title">SCHEDULE A CALL</span>
						<span class="social-subtitle">Calendly &bull; 1:1 Kennenlernen</span>
					</div>
				</a>
			</li>'''

# 1. Update index.html
index_file = os.path.join(BASE_DIR, "index.html")
with open(index_file, "r", encoding="utf-8") as f:
    idx = f.read()

# Update speaker CTA button
idx = idx.replace(
    '<a href="#contact-form" class="btn2">Nachricht senden</a>',
    f'<a href="{CALENDLY_URL}" target="_blank" rel="noopener noreferrer" class="btn2">Schedule a Call &rarr;</a>'
)

# Replace the contact-form block and LinkedIn wrapper
old_contact_block_pattern = r'<div class="connect-linkedin-wrap">.*?<div class="contact-card text-start" id="contact-form">.*?</div>\s*</div>\s*</div>\s*</div>'
idx = re.sub(
    r'<div class="connect-linkedin-wrap">.*?</div>\s*<div class="contact-card text-start" id="contact-form">.*?</div>\s*</div>\s*</div>\s*</div>',
    schedule_card_html + '\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>',
    idx,
    flags=re.DOTALL
)

# Replace footer social item
old_footer_social_pattern = r'<li class="social-item">\s*<a href="#contact-form"[^>]*>.*?</a>\s*</li>'
idx = re.sub(old_footer_social_pattern, footer_social_call_html, idx, flags=re.DOTALL)

with open(index_file, "w", encoding="utf-8") as f:
    f.write(idx)
print("Updated index.html with Schedule a Call Calendly button")

# 2. Update insights.html footer social item
insights_file = os.path.join(BASE_DIR, "insights.html")
with open(insights_file, "r", encoding="utf-8") as f:
    ins = f.read()

old_insights_footer_social_pattern = r'<li class="social-item">\s*<a href="/#contact-form"[^>]*>.*?</a>\s*</li>'
ins = re.sub(old_insights_footer_social_pattern, footer_social_call_html, ins, flags=re.DOTALL)

with open(insights_file, "w", encoding="utf-8") as f:
    f.write(ins)
print("Updated insights.html footer with Schedule a Call")

# 3. Update variation files for consistency
for var_file in ["variation-navy.html", "variation-teal.html"]:
    var_path = os.path.join(BASE_DIR, var_file)
    if os.path.exists(var_path):
        with open(var_path, "r", encoding="utf-8") as f:
            v_content = f.read()
        v_content = v_content.replace(
            '<a href="#contact-form" class="btn2">Nachricht senden</a>',
            f'<a href="{CALENDLY_URL}" target="_blank" rel="noopener noreferrer" class="btn2">Schedule a Call &rarr;</a>'
        )
        v_content = re.sub(
            r'<div class="connect-linkedin-wrap">.*?</div>\s*<div class="contact-card text-start" id="contact-form">.*?</div>\s*</div>\s*</div>\s*</div>',
            schedule_card_html + '\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>',
            v_content,
            flags=re.DOTALL
        )
        v_content = re.sub(old_footer_social_pattern, footer_social_call_html, v_content, flags=re.DOTALL)
        with open(var_path, "w", encoding="utf-8") as f:
            f.write(v_content)
        print(f"Updated {var_file} with Schedule a Call")
