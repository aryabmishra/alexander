#!/usr/bin/env python3
import os
import re

DIR = "/Users/aryabmishra/Downloads/Website Replicates/alexander-jankowski"

print("--- Updating Alexander Jankowski Website to Final Approved Copy & Visual Fixes ---")

# ==============================================================================
# 1. Update css/main.css
# ==============================================================================
main_css_path = os.path.join(DIR, "css/main.css")
with open(main_css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Fix 1: Speaker section overlay image positioning and tablet sizing
# Replace object-position: left bottom with center 18% so Alexander head/face is never cut off
css = css.replace(
    "-o-object-position: left bottom;\n     object-position: left bottom;",
    "-o-object-position: center 18%;\n     object-position: center 18%;"
)

# Custom additions for flawless responsive behavior & image framing
custom_fixes = """
/* --------------------------------------------------------------------------
   ALEXANDER JANKOWSKI - RESPONSIVE & IMAGE FRAMING FIXES (FINAL)
   -------------------------------------------------------------------------- */

/* 1. Floating Color Switcher Bar */
#color-switcher-bar {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 9999;
  background: rgba(13, 13, 13, 0.94);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 40px;
  padding: 6px 14px;
  display: flex;
  align-items: center;
  gap: 8px;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.85);
  transition: all 0.3s ease;
}

@media (max-width: 767px) {
  #color-switcher-bar {
    bottom: 14px !important;
    right: 14px !important;
    padding: 5px 10px !important;
    gap: 6px !important;
  }
  #color-switcher-bar .switcher-label {
    display: none;
  }
  #color-switcher-bar a {
    padding: 4px 8px !important;
    font-size: 10px !important;
  }
}

/* 2. Intro Section Cutout Image (Alexander) */
.intro-section .cutout {
  object-fit: contain;
  object-position: right bottom;
  filter: drop-shadow(0 15px 30px rgba(0,0,0,0.9));
}

/* 3. Timeline Center Gap on Tablet & Desktop (Prevents 2022/2026 overlapping images/text) */
@media (min-width: 768px) and (max-width: 1199px) {
  .timeline .tl-block .tl-half {
    width: 39% !important;
  }
  .timeline .tl-block h2 {
    font-size: 54px !important;
    padding: 10px 0 !important;
  }
  .timeline .tl-block .tl-half.tl-half-text {
    padding: 0 20px !important;
  }
}

@media (min-width: 1200px) {
  .timeline .tl-block .tl-half {
    width: 44% !important;
  }
  .timeline .tl-block h2 {
    font-size: 72px !important;
  }
}

/* 4. Transformation Photo (10 Weeks) - Never Cut Off, Never Collides */
.timeline .tl-block .tl-half img[src*="manchester-uni.jpg"] {
  object-fit: contain !important;
  background-color: #000000;
  padding-bottom: 8px;
  border-radius: 8px;
}

.timeline-wrap-mob .timeline-mob .timeline-item-mob img.timeline-img-mob[src*="manchester-uni.jpg"] {
  height: 250px !important;
  object-fit: contain !important;
  background-color: #000000 !important;
  margin-bottom: 12px !important;
  border-radius: 8px;
}

.timeline-wrap-mob .timeline-mob .timeline-item-mob h2 {
  margin-top: 14px !important;
  margin-bottom: 12px !important;
}

/* 5. Speaker Section Overlay Image on Tablet */
@media (min-width: 768px) and (max-width: 991px) {
  .speaker-section .speaker-overlay-img {
    width: 310px !important;
    height: 220px !important;
    left: 20px !important;
    top: 50% !important;
  }
}

/* 6. News & Insights Card Thumbnails - Complete Important Parts Visible */
.news-block .news-thumb {
  height: 230px !important;
  background-color: #0c0c0c;
}
@media (min-width: 992px) {
  .news-block .news-thumb {
    height: 260px !important;
  }
}
@media (min-width: 1400px) {
  .news-block .news-thumb {
    height: 300px !important;
  }
}

.news-block .news-thumb img[src*="news-1.jpg"],
.insight-thumb img[src*="news-1.jpg"],
.featured-thumb-container img[src*="news-1.jpg"] {
  object-position: center 15% !important;
}

.news-block .news-thumb img[src*="news-5.jpg"],
.insight-thumb img[src*="news-5.jpg"] {
  object-fit: contain !important;
  background-color: #050505 !important;
  padding: 8px 0 !important;
}

.news-block .news-thumb img[src*="news-6.jpg"],
.insight-thumb img[src*="news-6.jpg"] {
  object-position: center 25% !important;
}

.news-block .news-thumb img[src*="news-4.jpg"],
.insight-thumb img[src*="news-4.jpg"] {
  object-position: center 15% !important;
}
"""

if "ALEXANDER JANKOWSKI - RESPONSIVE & IMAGE FRAMING FIXES" not in css:
    css += "\n" + custom_fixes
    with open(main_css_path, "w", encoding="utf-8") as f:
        f.write(css)
    print("Updated css/main.css with responsive fixes.")
else:
    print("css/main.css already had custom fixes block.")

# ==============================================================================
# 2. Re-create / Update HTML files with final copy and color switchers
# ==============================================================================

COLOR_BAR_HTML_ORIGINAL = """
    <!-- Floating Color Palette Switcher for Alexander Review -->
    <div id="color-switcher-bar">
        <span class="switcher-label" style="font-family: 'zuume', sans-serif; font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: rgba(255, 255, 255, 0.6); margin-right: 4px; margin-left: 4px;">Farbe:</span>
        <a href="/" style="display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; border-radius: 30px; font-family: 'zuume', sans-serif; font-size: 11px; letter-spacing: 1px; text-decoration: none; text-transform: uppercase; transition: all 0.2s ease; background: #DBFF00; color: #000; font-weight: 700;">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: #DBFF00;"></span> Original
        </a>
        <a href="/variation-navy.html" style="display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; border-radius: 30px; font-family: 'zuume', sans-serif; font-size: 11px; letter-spacing: 1px; text-decoration: none; text-transform: uppercase; transition: all 0.2s ease; background: transparent; color: #fff; border: 1px solid rgba(255,255,255,0.2);">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: #3B82F6;"></span> Royal Navy
        </a>
        <a href="/variation-teal.html" style="display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; border-radius: 30px; font-family: 'zuume', sans-serif; font-size: 11px; letter-spacing: 1px; text-decoration: none; text-transform: uppercase; transition: all 0.2s ease; background: transparent; color: #fff; border: 1px solid rgba(255,255,255,0.2);">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: #00B4D8;"></span> Ocean Teal
        </a>
    </div>
"""

COLOR_BAR_HTML_NAVY = """
    <!-- Floating Color Palette Switcher for Alexander Review -->
    <div id="color-switcher-bar">
        <span class="switcher-label" style="font-family: 'zuume', sans-serif; font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: rgba(255, 255, 255, 0.6); margin-right: 4px; margin-left: 4px;">Farbe:</span>
        <a href="/" style="display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; border-radius: 30px; font-family: 'zuume', sans-serif; font-size: 11px; letter-spacing: 1px; text-decoration: none; text-transform: uppercase; transition: all 0.2s ease; background: transparent; color: #fff; border: 1px solid rgba(255,255,255,0.2);">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: #DBFF00;"></span> Original
        </a>
        <a href="/variation-navy.html" style="display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; border-radius: 30px; font-family: 'zuume', sans-serif; font-size: 11px; letter-spacing: 1px; text-decoration: none; text-transform: uppercase; transition: all 0.2s ease; background: #2563EB; color: #fff; font-weight: 700;">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: #3B82F6;"></span> Royal Navy
        </a>
        <a href="/variation-teal.html" style="display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; border-radius: 30px; font-family: 'zuume', sans-serif; font-size: 11px; letter-spacing: 1px; text-decoration: none; text-transform: uppercase; transition: all 0.2s ease; background: transparent; color: #fff; border: 1px solid rgba(255,255,255,0.2);">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: #00B4D8;"></span> Ocean Teal
        </a>
    </div>
"""

COLOR_BAR_HTML_TEAL = """
    <!-- Floating Color Palette Switcher for Alexander Review -->
    <div id="color-switcher-bar">
        <span class="switcher-label" style="font-family: 'zuume', sans-serif; font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: rgba(255, 255, 255, 0.6); margin-right: 4px; margin-left: 4px;">Farbe:</span>
        <a href="/" style="display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; border-radius: 30px; font-family: 'zuume', sans-serif; font-size: 11px; letter-spacing: 1px; text-decoration: none; text-transform: uppercase; transition: all 0.2s ease; background: transparent; color: #fff; border: 1px solid rgba(255,255,255,0.2);">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: #DBFF00;"></span> Original
        </a>
        <a href="/variation-navy.html" style="display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; border-radius: 30px; font-family: 'zuume', sans-serif; font-size: 11px; letter-spacing: 1px; text-decoration: none; text-transform: uppercase; transition: all 0.2s ease; background: transparent; color: #fff; border: 1px solid rgba(255,255,255,0.2);">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: #3B82F6;"></span> Royal Navy
        </a>
        <a href="/variation-teal.html" style="display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; border-radius: 30px; font-family: 'zuume', sans-serif; font-size: 11px; letter-spacing: 1px; text-decoration: none; text-transform: uppercase; transition: all 0.2s ease; background: #00B4D8; color: #000; font-weight: 700;">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: #00B4D8;"></span> Ocean Teal
        </a>
    </div>
"""

# Process index.html, variation-navy.html, variation-teal.html
files_to_update = [
    ("index.html", COLOR_BAR_HTML_ORIGINAL),
    ("variation-navy.html", COLOR_BAR_HTML_NAVY),
    ("variation-teal.html", COLOR_BAR_HTML_TEAL)
]

for filename, color_bar in files_to_update:
    path = os.path.join(DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Intro section copy
    content = re.sub(
        r'<div class="col-12 col-md-6" data-aos="fade" data-aos-duration="2500">\s*<h2[^>]*>.*?</h2>\s*<p[^>]*>.*?</p>\s*<a href="#timeline"[^>]*>.*?</a>',
        '''<div class="col-12 col-md-6" data-aos="fade" data-aos-duration="2500">
					<h2 style="font-size: clamp(32px, 3.8vw, 56px); line-height: 1.15; margin-bottom: 20px;">Vertrieb. Beziehungen. Vertrauen. Entwicklung.</h2>
					<p style="font-family: paralucent, sans-serif; font-size: clamp(17px, 1.25vw, 22px); line-height: 1.6; color: rgba(255, 255, 255, 0.82); margin-bottom: 30px; max-width: 580px;">Mein Weg f&uuml;hrte mich von der Polizei &uuml;ber die Fitnessbranche bis in den Vertrieb. Was sich dabei nie ver&auml;ndert hat: mein Interesse an Menschen, Kommunikation und echten Beziehungen.</p>
					<a href="#timeline" class="btn">Mehr &uuml;ber meinen Weg</a>''',
        content,
        flags=re.DOTALL
    )

    # Cutout image: Ensure it references images/alexander-cutout.png
    content = content.replace('src="images/steven-cutout1.png"', 'src="images/alexander-cutout.png"')

    # Desktop Timeline Stationen
    # 2018
    content = re.sub(
        r'<div class="tl-half tl-half-text">\s*<img src="images/timeline/timeline1\.jpg" class="blur-img">\s*<h3>FINANZDIENSTLEISTUNG</h3>\s*<h4 class="icon-loc">tecis Finanzdienstleistungen</h4>\s*<p>.*?</p>',
        '''<div class="tl-half tl-half-text">
						<img src="images/timeline/timeline1.jpg" class="blur-img">
						<h3>FINANZDIENSTLEISTUNG</h3>
						<h4 class="icon-loc">tecis Finanzdienstleistungen</h4>
						<p>Mein erster Kontakt mit Vertrieb begann fr&uuml;h. Bereits w&auml;hrend meines Polizeistudiums sammelte ich Erfahrungen darin, auf Menschen zuzugehen, zuzuh&ouml;ren, Bed&uuml;rfnisse zu verstehen und Vertrauen aufzubauen.</p>''',
        content,
        flags=re.DOTALL
    )

    # 2021
    content = re.sub(
        r'<div class="tl-half tl-half-text">\s*<img src="images/timeline/timeline3\.jpg" class="blur-img-small">\s*<h3>POLIZEIDIENST BERLIN</h3>\s*<h4 class="icon-loc">B\.A\. Polizei &amp; Sicherheitsmanagement \(HWR Berlin\)</h4>\s*<p>.*?</p>',
        '''<div class="tl-half tl-half-text">
						<img src="images/timeline/timeline3.jpg" class="blur-img-small">
						<h3>POLIZEIDIENST BERLIN</h3>
						<h4 class="icon-loc">B.A. Polizei &amp; Sicherheitsmanagement (HWR Berlin)</h4>
						<p>Die Polizei hat mir gezeigt, wie wichtig Ruhe, Verantwortung und klare Entscheidungen unter Druck sind. Sie hat meinen Blick auf Menschen ver&auml;ndert und mir beigebracht, auch in anspruchsvollen Situationen einen klaren Kopf zu behalten.</p>''',
        content,
        flags=re.DOTALL
    )

    # 2022
    content = re.sub(
        r'<div class="tl-half tl-half-text">\s*<img src="images/timeline/social-chain\.jpg" class="blur-img-small">\s*<h3>FITNESSBRANCHE</h3>\s*<h4 class="icon-loc">B\.A\. Fitness&ouml;konomie \(DHfPG\)</h4>\s*<p>.*?</p>',
        '''<div class="tl-half tl-half-text">
						<img src="images/timeline/social-chain.jpg" class="blur-img-small">
						<h3>FITNESSBRANCHE</h3>
						<h4 class="icon-loc">B.A. Fitness&ouml;konomie (DHfPG)</h4>
						<p>Im Fitness-Coaching habe ich gelernt, dass Wissen allein nicht ausreicht. Menschen brauchen Vertrauen, Motivation und jemanden, der ihnen wirklich zuh&ouml;rt. &Uuml;ber dreieinhalb Jahre entstanden daraus Erfahrungen und Beziehungen, die mich bis heute pr&auml;gen.</p>''',
        content,
        flags=re.DOTALL
    )

    # 2026
    content = re.sub(
        r'<div class="tl-half tl-half-text">\s*<img src="images/timeline/timeline4\.jpg" class="blur-img-small">\s*<h3>VERTRIEB &amp; ACCOUNT MANAGEMENT</h3>\s*<h4 class="icon-loc">Junior Account Manager &bull; 1&amp;1 Versatel</h4>\s*<p>.*?</p>',
        '''<div class="tl-half tl-half-text">
						<img src="images/timeline/timeline4.jpg" class="blur-img-small">
						<h3>VERTRIEB &amp; ACCOUNT MANAGEMENT</h3>
						<h4 class="icon-loc">Junior Account Manager &bull; 1&amp;1 Versatel</h4>
						<p>Der Vertrieb war f&uuml;r mich bewusst der n&auml;chste Schritt aus der Komfortzone. Kaltakquise, Ablehnung und t&auml;gliche Gespr&auml;che haben mir gezeigt, dass Entwicklung durch Handeln, Wiederholung und Lernen entsteht.</p>''',
        content,
        flags=re.DOTALL
    )

    # Mobile Timeline Stationen
    content = re.sub(
        r'<div class="swiper-slide timeline-item-mob timeline-first-item">.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>',
        '''<div class="swiper-slide timeline-item-mob timeline-first-item">
					<img src="images/timeline/timeline3.jpg" class="blur-img1">
					<img src="images/timeline/timeline1.jpg" class="timeline-img-mob">
					<h2>2018</h2>
					<div class="tl-mob-text-box">
						<h3>FINANZDIENSTLEISTUNG</h3>
						<h4 class="icon-loc">tecis Finanzdienstleistungen</h4>
						<p>Mein erster Kontakt mit Vertrieb begann fr&uuml;h. Bereits w&auml;hrend meines Polizeistudiums sammelte ich Erfahrungen darin, auf Menschen zuzugehen, zuzuh&ouml;ren, Bed&uuml;rfnisse zu verstehen und Vertrauen aufzubauen.</p>
					</div>
				</div>
				<div class="swiper-slide timeline-item-mob">
					<div class="tl-mob-text-box tl-mob-text-box-top">
						<h3>POLIZEIDIENST BERLIN</h3>
						<h4 class="icon-loc">B.A. Polizei &amp; Sicherheitsmanagement (HWR Berlin)</h4>
						<p>Die Polizei hat mir gezeigt, wie wichtig Ruhe, Verantwortung und klare Entscheidungen unter Druck sind. Sie hat meinen Blick auf Menschen ver&auml;ndert und mir beigebracht, auch in anspruchsvollen Situationen einen klaren Kopf zu behalten.</p>
					</div>
					<h2>2021</h2>
					<img src="images/timeline/timeline4.jpg" class="blur-img2">
					<img src="images/timeline/timeline2.jpg" class="timeline-img-mob">
				</div>
				<div class="swiper-slide timeline-item-mob">
					<img src="images/timeline/manchester-uni.jpg" class="timeline-img-mob">
					<img src="images/timeline/social-chain.jpg" class="blur-img1">
					<h2>2022</h2>
					<div class="tl-mob-text-box">
						<h3>FITNESSBRANCHE</h3>
						<h4 class="icon-loc">B.A. Fitness&ouml;konomie (DHfPG)</h4>
						<p>Im Fitness-Coaching habe ich gelernt, dass Wissen allein nicht ausreicht. Menschen brauchen Vertrauen, Motivation und jemanden, der ihnen wirklich zuh&ouml;rt. &Uuml;ber dreieinhalb Jahre entstanden daraus Erfahrungen und Beziehungen, die mich bis heute pr&auml;gen.</p>
					</div>
				</div>
				<div class="swiper-slide timeline-item-mob">
					<div class="tl-mob-text-box tl-mob-text-box-top">
						<h3>VERTRIEB &amp; ACCOUNT MANAGEMENT</h3>
						<h4 class="icon-loc">Junior Account Manager &bull; 1&amp;1 Versatel</h4>
						<p>Der Vertrieb war f&uuml;r mich bewusst der n&auml;chste Schritt aus der Komfortzone. Kaltakquise, Ablehnung und t&auml;gliche Gespr&auml;che haben mir gezeigt, dass Entwicklung durch Handeln, Wiederholung und Lernen entsteht.</p>
					</div>
					<a href="#about" class="btn2">Mehr &uuml;ber meinen Weg</a>
					<h2>2026</h2>
					<img src="images/timeline/wallpark.png" class="timeline-img-mob">
				</div>
			</div>
		</div>
	</div>''',
        content,
        flags=re.DOTALL
    )

    # Gedanken & Einblicke news slides
    news_slides_exact = """							<a href="insights.html#article-1" class="swiper-slide news-block">
								<div class="news-thumb">
									<img src="images/news-1.jpg" alt="Was Polizeiarbeit mich über Ruhe unter Druck gelehrt hat">
								</div>
								<div class="fw">
									<ul class="news-tags"><li>Polizei &amp; Haltung</li></ul>
									<h3>Was Polizeiarbeit mich &uuml;ber Ruhe unter Druck gelehrt hat</h3>
								</div>
							</a>

							<a href="insights.html#article-2" class="swiper-slide news-block">
								<div class="news-thumb">
									<img src="images/news-5.jpg" alt="Warum Menschenkenntnis im Coaching wichtiger ist als perfekte Theorie">
								</div>
								<div class="fw">
									<ul class="news-tags"><li>Fitness-Coaching</li></ul>
									<h3>Warum Menschenkenntnis im Coaching wichtiger ist als perfekte Theorie</h3>
								</div>
							</a>

							<a href="insights.html#article-3" class="swiper-slide news-block">
								<div class="news-thumb">
									<img src="images/news-6.jpg" alt="Warum Handeln oft wichtiger ist als Perfektion">
								</div>
								<div class="fw">
									<ul class="news-tags"><li>Mindset &amp; Disziplin</li></ul>
									<h3>Warum Handeln oft wichtiger ist als Perfektion</h3>
								</div>
							</a>

							<a href="insights.html#article-4" class="swiper-slide news-block">
								<div class="news-thumb">
									<img src="images/news-4.jpg" alt="Warum guter Vertrieb trotz aller Zahlen menschlich bleibt">
								</div>
								<div class="fw">
									<ul class="news-tags"><li>Vertrieb &amp; Vertrauen</li></ul>
									<h3>Warum guter Vertrieb trotz aller Zahlen menschlich bleibt</h3>
								</div>
							</a>"""

    content = re.sub(
        r'<div class="swiper swiper-news">\s*<div class="swiper-wrapper">.*?</div>\s*</div>',
        f'<div class="swiper swiper-news">\n\t\t\t\t\t\t<div class="swiper-wrapper">\n{news_slides_exact}\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>',
        content,
        flags=re.DOTALL
    )

    # Speaker / Future Positioning Section (MENSCHEN & UNTERNEHMEN ZUSAMMENBRINGEN)
    speaker_section_exact = """					<div class="col-12 col-md-6 offset-md-6 col-lg-5 offset-lg-7 text-center text-md-start" data-aos="fade" data-aos-duration="2000">
						<div style="font-family: 'zuume', sans-serif; font-size: 15px; letter-spacing: 2px; color: #DBFF00; text-transform: uppercase; margin-bottom: 10px;">Mein Werdegang</div>
						<h2>MENSCHEN &amp; UNTERNEHMEN <br>ZUSAMMENBRINGEN</h2>
						<p>Langfristig m&ouml;chte ich im Vertrieb dort arbeiten, wo Menschen und Unternehmen zusammenfinden. F&uuml;r mich geht es dabei nicht nur um Abschl&uuml;sse, sondern darum, zuzuh&ouml;ren, Vertrauen aufzubauen und herauszufinden, ob auf beiden Seiten echter Mehrwert entstehen kann.</p>
						<p>Gute Vorbereitung ist wichtig. Aber ich glaube nicht daran, auf den perfekten Moment zu warten. Entwicklung entsteht durch Handeln, Wiederholung und Lernen. Gerade im Vertrieb bedeutet das f&uuml;r mich: direkt und respektvoll kommunizieren, mit Ablehnung umgehen und aus jedem Gespr&auml;ch besser werden.</p>
						<a href="#contact-form" class="btn2">Nachricht senden</a>
					</div>"""

    content = re.sub(
        r'<div class="col-12 col-md-5 offset-md-7 col-lg-4 offset-lg-8 text-center text-md-start"[^>]*>.*?<a href="#contact-form"[^>]*>Nachricht senden</a>\s*</div>',
        speaker_section_exact,
        content,
        flags=re.DOTALL
    )

    # Contact section copy
    content = content.replace(
        "Mein Weg hat mich durch sehr unterschiedliche Bereiche geführt. Deshalb freue ich mich auf Gespräche mit Menschen aus Vertrieb, Fitness, Polizei und darüber hinaus.",
        "Mein Weg hat mich durch sehr unterschiedliche Bereiche gef&uuml;hrt. Deshalb freue ich mich auf Gespr&auml;che mit Menschen aus Vertrieb, Fitness, Polizei und dar&uuml;ber hinaus &ndash; &uuml;ber Entwicklung, Neuorientierung und neue M&ouml;glichkeiten."
    )
    content = content.replace(
        "Mein Weg hat mich durch sehr unterschiedliche Bereiche geführt. Deshalb freue ich mich auf Gespräche mit Menschen aus Vertrieb, Fitness, Polizei und darüber hinaus - über Entwicklung, Neuorientierung und neue Möglichkeiten.",
        "Mein Weg hat mich durch sehr unterschiedliche Bereiche gef&uuml;hrt. Deshalb freue ich mich auf Gespr&auml;che mit Menschen aus Vertrieb, Fitness, Polizei und dar&uuml;ber hinaus &ndash; &uuml;ber Entwicklung, Neuorientierung und neue M&ouml;glichkeiten."
    )

    # Ensure color switcher is present before </body>
    if 'id="color-switcher-bar"' not in content:
        content = content.replace("</body>", f"{color_bar}\n</body>")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {filename} successfully.")

# ==============================================================================
# 3. Update insights.html (Exact Copy, Balanced 2x2 Grid, Clean Image Framing)
# ==============================================================================
insights_path = os.path.join(DIR, "insights.html")
with open(insights_path, "r", encoding="utf-8") as f:
    ins = f.read()

# Make sure color switcher is in insights.html
if 'id="color-switcher-bar"' not in ins:
    ins = ins.replace("</body>", f"{COLOR_BAR_HTML_ORIGINAL}\n</body>")

# Replace articlesData and grid articles with the exact copy
articles_js = """
	const articlesData = {
		1: {
			title: "Was Polizeiarbeit mich über Ruhe unter Druck gelehrt hat",
			category: "Polizei & Haltung",
			date: "Oktober 2026",
			readTime: "5 Min. Lesezeit",
			author: "Alexander Jankowski",
			content: `
				<p>Ein Notruf geht ein. Keine Zeit zum Nachdenken, keine zweite Chance. Und trotzdem wird eine Entscheidung erwartet, und zwar die richtige. Wie schafft man das?</p>
				<p>Die ehrliche Antwort: nicht mit Talent. Unter Stress spielt unser Körper verrückt. Der Puls rast, der Blick wird eng, klares Denken wird schwer. Genau deshalb verlässt sich die Polizei nicht darauf, dass im Ernstfall schon die richtige Idee kommt. Abläufe werden trainiert, bis sie sitzen. Und sogar ruhiges, bewusstes Atmen gehört zur Ausbildung, weil es den Kopf wieder freimacht.</p>
				<blockquote>„Druck verschwindet nicht. Aber er verliert seine Macht, wenn man vorbereitet ist.“</blockquote>
				<p>Was ich daraus mitnehme? Druck verschwindet nicht. Aber er verliert seine Macht, wenn man vorbereitet ist. Wer seine Abläufe kennt und einmal kurz durchatmet, bevor er reagiert, bleibt ruhig, auch wenn es drumherum laut wird. Im Einsatz genauso wie im Beruf.</p>
			`
		},
		2: {
			title: "Warum Menschenkenntnis im Coaching wichtiger ist als perfekte Theorie",
			category: "Fitness-Coaching",
			date: "Oktober 2026",
			readTime: "5 Min. Lesezeit",
			author: "Alexander Jankowski",
			content: `
				<p>Im Coaching und Fitnessbereich glauben viele, der perfekte Trainings- oder Ernährungsplan sei der Schlüssel zum Erfolg. Doch die Praxis sieht völlig anders aus: Der beste Plan nützt nichts, wenn der Mensch ihn nicht umsetzt.</p>
				<p>Wissen allein verändert keine Gewohnheiten. Menschen brauchen Verständnis für ihre individuelle Situation, echte Motivation und jemanden, der ihnen auf Augenhöhe zuhört. Warum fällt die Umsetzung schwer? Welche Barrieren existieren im Alltag? Wann schlägt die Motivation in Frustration um?</p>
				<blockquote>„Theorie liefert die Struktur. Doch erst Empathie und Menschenkenntnis schaffen nachhaltige Veränderung.“</blockquote>
				<p>Über dreieinhalb Jahre im Coaching haben mir bewiesen: Wer Menschen nachhaltig voranbringen will, muss zuerst den Menschen verstehen – nicht nur die Theorie.</p>
			`
		},
		3: {
			title: "Warum Handeln oft wichtiger ist als Perfektion",
			category: "Mindset & Disziplin",
			date: "Oktober 2026",
			readTime: "4 Min. Lesezeit",
			author: "Alexander Jankowski",
			content: `
				<p>Wer auf den perfekten Moment wartet, wartet meistens für immer. Ob im Sport, bei der Polizei oder im Vertrieb: Perfektion existiert vor dem ersten Schritt nicht. Sie entsteht erst durch das Tun.</p>
				<p>Oft verbringen wir Tage damit, Pläne zu verfeinern, Vorwände zu analysieren und Risiken abzuwägen. Doch die wertvollsten Erkenntnisse gewinnen wir nie in der Vorbereitung, sondern in der direkten Praxis – im ersten Anruf, in der ersten echten Konfrontation, im ersten Versuch.</p>
				<blockquote>„Entwicklung entsteht durch Handeln, Wiederholung und Lernen. Nicht durch endloses Zögern.“</blockquote>
				<p>Handeln schlägt Zögern, jedes einzelne Mal. Wer bereit ist, unvollkommen zu starten, lernt schneller, passt sich schneller an und erzielt echte Ergebnisse.</p>
			`
		},
		4: {
			title: "Warum guter Vertrieb trotz aller Zahlen menschlich bleibt",
			category: "Vertrieb & Vertrauen",
			date: "Oktober 2026",
			readTime: "5 Min. Lesezeit",
			author: "Alexander Jankowski",
			content: `
				<p>Ein Kunde sagt Ja. Nicht weil mein Angebot das billigste war. Sondern weil er mir vertraut hat. Aber wann genau passiert das eigentlich?</p>
				<p>Ganz ehrlich: selten im ersten Gespräch. Vertrauen lässt sich nicht einfordern, man verdient es sich. Und am Ende läuft es auf drei fundamentale Fragen hinaus, die sich jeder Kunde stellt, bewusst oder unbewusst: Kann der das wirklich? Meint der es gut mit mir? Und hält der, was er sagt?</p>
				<blockquote>„Vertrauen entsteht nicht durch glänzende Präsentationen, sondern durch Verlässlichkeit im Detail.“</blockquote>
				<p>Die Antwort darauf geben keine großen Versprechen, sondern Kleinigkeiten. Zurückrufen, wenn man es zugesagt hat. Ehrlich sein, auch wenn man dann im Moment nichts verkauft, und sich aufrichtig für die Situation des Gegenübers interessieren. Genau daran merken Menschen, ob sie sich auf jemanden verlassen können.</p>
			`
		}
	};
"""

# Replace articlesData script in insights.html
ins = re.sub(r'const articlesData = \{.*?\};\n', articles_js, ins, flags=re.DOTALL)

# Replace filter buttons
filters_markup = """			<!-- Category Filters -->
			<div class="filter-wrap" data-aos="fade-up" data-aos-delay="200" data-aos-duration="1000">
				<button class="filter-pill active" data-filter="all">Alle Artikel (4)</button>
				<button class="filter-pill" data-filter="polizei">Polizei &amp; Haltung</button>
				<button class="filter-pill" data-filter="fitness">Fitness-Coaching</button>
				<button class="filter-pill" data-filter="mindset">Mindset &amp; Disziplin</button>
				<button class="filter-pill" data-filter="vertrieb">Vertrieb &amp; Vertrauen</button>
			</div>"""

ins = re.sub(r'<!-- Category Filters.*?</div>\s*</div>\s*</section>', filters_markup + '\n\t\t</div>\n\t</section>', ins, flags=re.DOTALL)

# Replace spotlight article
spotlight_markup = """						<!-- Featured Spotlight Article -->
			<div data-aos="fade-up" data-aos-duration="1000">
				<a href="javascript:void(0)" class="featured-card-wrap" onclick="openInsightModal(1)">
					<div class="row g-0 align-items-center">
						<div class="col-lg-6">
							<div class="featured-thumb-container">
								<span class="featured-badge">Spotlight Insight</span>
								<img src="images/news-1.jpg" alt="Was Polizeiarbeit mich über Ruhe unter Druck gelehrt hat">
							</div>
						</div>
						<div class="col-lg-6">
							<div class="featured-content">
								<div class="featured-meta">
									<span>Polizei &amp; Haltung</span> &bull; <span>5 Min. Lesezeit</span> &bull; <span>Autor: Alexander Jankowski</span>
								</div>
								<h2 class="featured-title">Was Polizeiarbeit mich &uuml;ber Ruhe unter Druck gelehrt hat</h2>
								<p class="featured-excerpt">
									Ein Notruf geht ein. Keine Zeit zum Nachdenken, keine zweite Chance. Warum Druck seine Macht verliert, wenn man vorbereitet ist – im Einsatz genauso wie im Beruf.
								</p>
								<span class="btn2">Diesen Insight lesen &rarr;</span>
							</div>
						</div>
					</div>
				</a>
			</div>"""

ins = re.sub(r'<!-- Featured Spotlight Article -->.*?</a>\s*</div>', spotlight_markup, ins, flags=re.DOTALL)

# Replace 2x2 grid
grid_markup = """						<!-- Grid of All Insights (Balanced 2x2 Layout) -->
			<div class="row g-4" id="insights-grid">

				<!-- Article 1: Polizei -->
				<div class="col-12 col-md-6 insight-item" data-category="polizei">
					<div class="insight-card" onclick="openInsightModal(1)">
						<div class="insight-thumb">
							<img src="images/news-1.jpg" alt="Was Polizeiarbeit mich über Ruhe unter Druck gelehrt hat">
						</div>
						<div class="insight-body">
							<div class="insight-tags">
								<span class="insight-tag">Polizei &amp; Haltung</span>
								<span class="insight-tag">Fokus</span>
							</div>
							<h3 class="insight-card-title">Was Polizeiarbeit mich &uuml;ber Ruhe unter Druck gelehrt hat</h3>
							<p class="insight-card-desc">
								Ein Notruf geht ein. Keine Zeit zum Nachdenken, keine zweite Chance. Warum Druck seine Macht verliert, wenn Abl&auml;ufe sitzen und man vorbereitet ist.
							</p>
							<div class="insight-footer-meta">
								<span>Alexander Jankowski</span>
								<span class="reading-time">5 Min. Lesezeit</span>
							</div>
						</div>
					</div>
				</div>

				<!-- Article 2: Fitness-Coaching -->
				<div class="col-12 col-md-6 insight-item" data-category="fitness">
					<div class="insight-card" onclick="openInsightModal(2)">
						<div class="insight-thumb">
							<img src="images/news-5.jpg" alt="Warum Menschenkenntnis im Coaching wichtiger ist als perfekte Theorie">
						</div>
						<div class="insight-body">
							<div class="insight-tags">
								<span class="insight-tag">Fitness-Coaching</span>
								<span class="insight-tag">Menschenkenntnis</span>
							</div>
							<h3 class="insight-card-title">Warum Menschenkenntnis im Coaching wichtiger ist als perfekte Theorie</h3>
							<p class="insight-card-desc">
								Wissen allein ver&auml;ndert keine Gewohnheiten. Menschen brauchen Verst&auml;ndnis f&uuml;r ihren Alltag, Motivation und jemanden, der ihnen auf Augenh&ouml;he zuh&ouml;rt.
							</p>
							<div class="insight-footer-meta">
								<span>Alexander Jankowski</span>
								<span class="reading-time">5 Min. Lesezeit</span>
							</div>
						</div>
					</div>
				</div>

				<!-- Article 3: Mindset & Disziplin -->
				<div class="col-12 col-md-6 insight-item" data-category="mindset">
					<div class="insight-card" onclick="openInsightModal(3)">
						<div class="insight-thumb">
							<img src="images/news-6.jpg" alt="Warum Handeln oft wichtiger ist als Perfektion">
						</div>
						<div class="insight-body">
							<div class="insight-tags">
								<span class="insight-tag">Mindset &amp; Disziplin</span>
								<span class="insight-tag">Handeln</span>
							</div>
							<h3 class="insight-card-title">Warum Handeln oft wichtiger ist als Perfektion</h3>
							<p class="insight-card-desc">
								Wer auf den perfekten Moment wartet, wartet meistens f&uuml;r immer. Warum Entwicklung nur durch Handeln, Wiederholung und direktes Feedback entsteht.
							</p>
							<div class="insight-footer-meta">
								<span>Alexander Jankowski</span>
								<span class="reading-time">4 Min. Lesezeit</span>
							</div>
						</div>
					</div>
				</div>

				<!-- Article 4: Vertrieb & Vertrauen -->
				<div class="col-12 col-md-6 insight-item" data-category="vertrieb">
					<div class="insight-card" onclick="openInsightModal(4)">
						<div class="insight-thumb">
							<img src="images/news-4.jpg" alt="Warum guter Vertrieb trotz aller Zahlen menschlich bleibt">
						</div>
						<div class="insight-body">
							<div class="insight-tags">
								<span class="insight-tag">Vertrieb &amp; Vertrauen</span>
								<span class="insight-tag">Beziehungen</span>
							</div>
							<h3 class="insight-card-title">Warum guter Vertrieb trotz aller Zahlen menschlich bleibt</h3>
							<p class="insight-card-desc">
								Ein Kunde sagt Ja aus Vertrauen, nicht wegen des billigsten Preises. Warum echte Verl&auml;sslichkeit und Ehrlichkeit im Detail den Unterschied machen.
							</p>
							<div class="insight-footer-meta">
								<span>Alexander Jankowski</span>
								<span class="reading-time">5 Min. Lesezeit</span>
							</div>
						</div>
					</div>
				</div>

			</div>"""

ins = re.sub(r'<!-- Grid of All Insights.*?</div>\s*</div>\s*<!-- Insights CTA / Banner -->', grid_markup + '\n\n\t\t\t<!-- Insights CTA / Banner -->', ins, flags=re.DOTALL)

with open(insights_path, "w", encoding="utf-8") as f:
    f.write(ins)
print("Updated insights.html successfully.")
