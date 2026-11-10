#!/usr/bin/env python3
"""
create_compliance_pages.py
Creates Impressum, Datenschutz (Privacy Policy), and AGB (Terms & Conditions) pages,
updates footers across all HTML pages to include compliances + LinkedIn,
and updates redirects and sitemaps for Alexander Jankowski's website.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSS_ADDITIONS = """
/* ==========================================================================
   COMPLIANCE PAGES & FOOTER COMPLIANCES
   ========================================================================== */

/* Footer Enhancements */
.footer-divider {
  width: 100%;
  height: 1px;
  background: rgba(255, 255, 255, 0.08);
  margin: 28px 0 20px 0;
}

.footer-compliance-links {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 12px;
}

@media (min-width: 768px) {
  .footer-compliance-links {
    justify-content: flex-start;
  }
}

.footer-compliance-links a {
  color: #888888 !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  text-decoration: none !important;
  transition: all 0.2s ease !important;
}

.footer-compliance-links a:hover {
  color: #60A5FA !important;
  text-decoration: underline !important;
}

.footer-social-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
}

@media (min-width: 768px) {
  .footer-social-wrap {
    justify-content: flex-end;
  }
}

.footer-linkedin-badge {
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
  background: rgba(59, 130, 246, 0.1) !important;
  border: 1px solid rgba(96, 165, 250, 0.35) !important;
  color: #60A5FA !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  letter-spacing: 0.4px !important;
  padding: 7px 16px !important;
  border-radius: 999px !important;
  text-decoration: none !important;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.footer-linkedin-badge svg {
  flex-shrink: 0;
}

.footer-linkedin-badge .ext-arrow {
  font-size: 14px;
  line-height: 1;
  transition: transform 0.2s ease;
}

.footer-linkedin-badge:hover {
  background: #2563EB !important;
  border-color: #2563EB !important;
  color: #FFFFFF !important;
  box-shadow: 0 0 18px rgba(59, 130, 246, 0.45) !important;
  transform: translateY(-1px);
}

.footer-linkedin-badge:hover .ext-arrow {
  transform: translate(2px, -2px);
}

/* Compliance Subpages Styling */
.compliance-hero {
  position: relative;
  padding-top: 150px;
  padding-bottom: 60px;
  background: radial-gradient(circle at 50% 10%, rgba(59, 130, 246, 0.12) 0%, rgba(0, 0, 0, 0) 65%), #000000;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

@media (min-width: 992px) {
  .compliance-hero {
    padding-top: 175px;
    padding-bottom: 75px;
  }
}

.compliance-title {
  font-family: 'zuume', sans-serif !important;
  font-weight: 700 !important;
  font-size: 46px !important;
  line-height: 1 !important;
  letter-spacing: 1.5px !important;
  text-transform: uppercase !important;
  color: #FFFFFF !important;
  margin-bottom: 16px !important;
}

@media (min-width: 768px) {
  .compliance-title {
    font-size: 68px !important;
  }
}

.compliance-subtitle {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  font-size: 16px !important;
  color: rgba(255, 255, 255, 0.7) !important;
  max-width: 680px;
  margin: 0 auto !important;
  line-height: 1.6 !important;
}

.compliance-content-wrap {
  padding: 50px 0 90px 0;
  background-color: #000000;
}

.compliance-nav-pills {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 45px;
}

.compliance-pill {
  font-family: 'zuume', sans-serif;
  font-size: 13px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.7);
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.15);
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  transition: all 0.25s ease;
}

.compliance-pill:hover,
.compliance-pill.active {
  background-color: #60A5FA;
  color: #000000;
  border-color: #60A5FA;
  font-weight: 700;
  box-shadow: 0 4px 16px rgba(59, 130, 246, 0.3);
}

.compliance-card {
  background: #091322;
  border: 1px solid rgba(59, 130, 246, 0.2);
  border-radius: 20px;
  padding: 32px 24px;
  margin-bottom: 28px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
}

@media (min-width: 768px) {
  .compliance-card {
    padding: 44px 40px;
  }
}

.compliance-sec-heading {
  font-family: 'zuume', sans-serif !important;
  font-weight: 700 !important;
  font-size: 26px !important;
  letter-spacing: 1px !important;
  text-transform: uppercase !important;
  color: #60A5FA !important;
  margin-bottom: 18px !important;
}

.compliance-sec-subheading {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  font-weight: 600 !important;
  font-size: 18px !important;
  color: #FFFFFF !important;
  margin-top: 22px !important;
  margin-bottom: 10px !important;
}

.compliance-card p,
.compliance-card li {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
  font-size: 15.5px !important;
  line-height: 1.75 !important;
  color: rgba(255, 255, 255, 0.82) !important;
  margin-bottom: 14px;
}

.compliance-card ul {
  padding-left: 22px;
  margin-bottom: 20px;
}

.compliance-card strong {
  color: #FFFFFF !important;
  font-weight: 600 !important;
}

.compliance-card a {
  color: #60A5FA !important;
  text-decoration: underline !important;
  transition: color 0.2s ease !important;
}

.compliance-card a:hover {
  color: #93C5FD !important;
}

.compliance-highlight-box {
  background: rgba(59, 130, 246, 0.08);
  border-left: 3px solid #3B82F6;
  border-radius: 0 12px 12px 0;
  padding: 18px 22px;
  margin: 22px 0;
}

.compliance-highlight-box p:last-child {
  margin-bottom: 0;
}

.back-to-home-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: #60A5FA;
  font-size: 14px;
  font-weight: 600;
  text-decoration: none;
  margin-bottom: 24px;
  transition: all 0.2s ease;
}

.back-to-home-link:hover {
  color: #FFFFFF;
  transform: translateX(-3px);
}
"""

def update_css():
    css_path = os.path.join(BASE_DIR, "css", "theme-navy.css")
    with open(css_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "COMPLIANCE PAGES & FOOTER COMPLIANCES" not in content:
        with open(css_path, "a", encoding="utf-8") as f:
            f.write("\n" + CSS_ADDITIONS + "\n")
        print("Updated theme-navy.css with compliance styles.")
    else:
        print("theme-navy.css already contains compliance styles.")

def get_compliance_template(title, meta_desc, canonical_url, active_page, hero_badge, hero_title, hero_subtitle, card_content):
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>{title}</title>
	<meta name="title" content="{title}">
	<meta name="description" content="{meta_desc}">
	<meta name="robots" content="index, follow">
	<link rel="canonical" href="{canonical_url}">

	<!-- Open Graph / Facebook -->
	<meta property="og:type" content="website">
	<meta property="og:url" content="{canonical_url}">
	<meta property="og:title" content="{title}">
	<meta property="og:description" content="{meta_desc}">
	<meta property="og:image" content="https://alexanderjankowski.com/images/og-image.jpg">

	<!-- Fonts -->
	<link rel="stylesheet" href="https://use.typekit.net/erm4jbe.css">
	<link href="css/bootstrap.min.css" rel="stylesheet">
	<link href="css/hamburgers.min.css" rel="stylesheet">
	<!-- Main Styles -->
	<link href="css/main.css" rel="stylesheet">
	<link href="css/theme-navy.css" rel="stylesheet">
	<!-- AOS Animations -->
	<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">

	<!-- Favicon & Touch Icons -->
	<link rel="icon" href="favicon.ico" sizes="any">
	<link rel="icon" type="image/svg+xml" href="images/favicon.svg">
	<link rel="icon" type="image/png" sizes="32x32" href="images/favicon-32x32.png">
	<link rel="icon" type="image/png" sizes="192x192" href="images/favicon-192x192.png">
	<link rel="apple-touch-icon" sizes="180x180" href="images/apple-touch-icon.png">

	<!-- Microsoft Clarity -->
	<script type="text/javascript">
	    (function(c,l,a,r,i,t,y){{
	        c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
	        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
	        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
	    }})(window, document, "clarity", "script", "z79a01yj7z");
	</script>
</head>

<body>

	<!-- Mobile Navigation Trigger -->
	<div id="menu-trigger" class="hamburger hamburger--collapse">
		<div class="hamburger-box">
			<div class="hamburger-inner"></div>
		</div>
	</div>

	<!-- Header Logo -->
	<div class="fw header">
		<a href="/"><img src="images/sb-logotype-wo.svg" class="logo" alt="Alexander Jankowski"></a>
	</div>

	<!-- Fullscreen Menu Wrap -->
	<div class="menu-wrap">
		<ul class="menu">
			<li><a href="/">Startseite</a></li>
			<li><a href="/#about">Über mich</a></li>
			<li><a href="/#timeline">Mein Weg</a></li>
			<li><a href="/#work">Vertrieb</a></li>
			<li><a href="insights.html">Insights</a></li>
			<li><a href="/#contact">Kontakt</a></li>
		</ul>
	</div>

	<!-- Compliance Hero Section -->
	<section class="compliance-hero text-center">
		<div class="container">
			<div data-aos="fade-up" data-aos-duration="1000">
				<span class="hero-badge">{hero_badge}</span>
				<h1 class="compliance-title">{hero_title}</h1>
				<p class="compliance-subtitle">{hero_subtitle}</p>
			</div>
		</div>
	</section>

	<!-- Compliance Content Section -->
	<section class="compliance-content-wrap">
		<div class="container">
			<!-- Navigation Tabs for Legal Pages -->
			<div class="compliance-nav-pills" data-aos="fade" data-aos-duration="1000">
				<a href="impressum.html" class="compliance-pill {'active' if active_page == 'impressum' else ''}">Impressum</a>
				<a href="datenschutz.html" class="compliance-pill {'active' if active_page == 'datenschutz' else ''}">Datenschutz</a>
				<a href="agb.html" class="compliance-pill {'active' if active_page == 'agb' else ''}">AGB &amp; Nutzungsbedingungen</a>
			</div>

			<div class="row justify-content-center">
				<div class="col-12 col-lg-10 col-xl-9">
					<div class="mb-3">
						<a href="/" class="back-to-home-link">
							<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
							<span>Zurück zur Startseite</span>
						</a>
					</div>

					{card_content}

					<div class="mt-4 pt-2 text-center">
						<a href="/" class="btn2" style="padding: 0 32px; height: 50px; line-height: 46px; display: inline-flex; align-items: center; gap: 10px; text-decoration: none;">
							<span>Zurück zur Startseite</span>
							<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
						</a>
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- Enhanced Site Footer -->
	<footer class="fw site-footer">
		<div class="container-fluid px-4 px-md-5">
			<!-- Top Row: Brand & Quicklinks -->
			<div class="row align-items-center gy-3">
				<div class="col-12 col-md-7 text-center text-md-start">
					<div class="footer-brand-title">ALEXANDER JANKOWSKI</div>
					<div class="footer-meta-info">
						<span>&copy; 2026 Alexander Jankowski</span>
						<span class="footer-dot">&bull;</span>
						<span>Berlin, Deutschland</span>
						<span class="footer-dot d-none d-sm-inline">&bull;</span>
						<span class="d-block d-sm-inline mt-1 mt-sm-0 text-white-50">Vertrieb &bull; Account Management &bull; Neukundengewinnung</span>
					</div>
				</div>
				<div class="col-12 col-md-5 text-center text-md-end">
					<p class="footer-motto mb-2">„Unterschiedliche Stationen. Eine Konstante: Menschen.“</p>
					<div class="footer-quicklinks">
						<a href="/">Startseite</a>
						<a href="/#about">Über mich</a>
						<a href="/#timeline">Mein Weg</a>
						<a href="/#work">Vertrieb</a>
						<a href="insights.html">Insights</a>
						<a href="/#contact">Kontakt</a>
					</div>
				</div>
			</div>

			<!-- Subtle Divider -->
			<div class="footer-divider"></div>

			<!-- Bottom Row: Legal Compliances & LinkedIn -->
			<div class="row align-items-center gy-3 footer-bottom-row">
				<div class="col-12 col-md-8 text-center text-md-start">
					<div class="footer-compliance-links">
						<a href="impressum.html" {'style="color:#60A5FA; font-weight:700;"' if active_page == 'impressum' else ''}>Impressum</a>
						<span class="footer-dot">&bull;</span>
						<a href="datenschutz.html" {'style="color:#60A5FA; font-weight:700;"' if active_page == 'datenschutz' else ''}>Datenschutz</a>
						<span class="footer-dot">&bull;</span>
						<a href="agb.html" {'style="color:#60A5FA; font-weight:700;"' if active_page == 'agb' else ''}>AGB &amp; Nutzungsbedingungen</a>
					</div>
				</div>
				<div class="col-12 col-md-4 text-center text-md-end">
					<div class="footer-social-wrap">
						<a href="https://www.linkedin.com/in/alexander-jankowski-320ab6447/" target="_blank" rel="noopener noreferrer" class="footer-linkedin-badge" aria-label="LinkedIn Profil von Alexander Jankowski">
							<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
							<span>LinkedIn</span>
							<span class="ext-arrow">&nearr;</span>
						</a>
					</div>
				</div>
			</div>
		</div>
	</footer>

	<script src="js/bootstrap.bundle.min.js"></script>
	<script type="text/javascript" src="https://code.jquery.com/jquery-1.11.0.min.js"></script>
	<script src="js/init.js"></script>
	<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
	<script>
		AOS.init();
	</script>
</body>
</html>"""

def build_impressum_page():
    card_content = """
	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">1. Angaben gemäß § 5 DDG</h2>
		<p>
			<strong>Diensteanbieter und Betreiber dieser Website:</strong><br>
			Alexander Jankowski<br>
			Standort: Berlin, Deutschland
		</p>
		
		<div class="compliance-highlight-box">
			<p><strong>Direkte Kontaktmöglichkeiten:</strong></p>
			<p>
				E-Mail: <a href="mailto:alexander@alexanderjankowski.com">alexander@alexanderjankowski.com</a><br>
				Web: <a href="https://alexanderjankowski.com/">https://alexanderjankowski.com/</a><br>
				Online-Terminkalender: <a href="https://calendly.com/aj-alexanderjankowski/get2know" target="_blank" rel="noopener noreferrer">calendly.com/aj-alexanderjankowski/get2know</a><br>
				LinkedIn: <a href="https://www.linkedin.com/in/alexander-jankowski-320ab6447/" target="_blank" rel="noopener noreferrer">linkedin.com/in/alexander-jankowski</a>
			</p>
			<p style="font-size: 13.5px; color: rgba(255, 255, 255, 0.65); margin-top: 8px;">
				<em>Hinweis:</em> Eine vollständige ladungsfähige Postanschrift wird gemäß den gesetzlichen Vorgaben zur Verfügung gestellt und kann jederzeit unter der oben genannten E-Mail-Adresse angefordert werden.
			</p>
		</div>

		<h3 class="compliance-sec-subheading">Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h3>
		<p>
			Alexander Jankowski<br>
			Berlin, Deutschland<br>
			E-Mail: <a href="mailto:alexander@alexanderjankowski.com">alexander@alexanderjankowski.com</a>
		</p>

		<h3 class="compliance-sec-subheading">Berufsbezeichnung &amp; Tätigkeitsfeld</h3>
		<p>
			Junior Account Manager, Vertriebsberatung &amp; Keynote Speaker.<br>
			Verliehen in der Bundesrepublik Deutschland.
		</p>
	</div>

	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">2. EU-Streitschlichtung &amp; Verbraucherstreitbeilegung</h2>
		<p>
			Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit, die Sie unter folgendem Link finden:<br>
			<a href="https://ec.europa.eu/consumers/odr/" target="_blank" rel="noopener noreferrer">https://ec.europa.eu/consumers/odr/</a>
		</p>
		<p>
			Unsere E-Mail-Adresse finden Sie oben im Impressum.
		</p>
		<p>
			<strong>Verbraucherstreitbeilegung / Universalschlichtungsstelle (§ 36 VSBG):</strong><br>
			Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.
		</p>
	</div>

	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">3. Haftung für Inhalte (§ 7 Abs. 1 DDG)</h2>
		<p>
			Als Diensteanbieter sind wir gemäß § 7 Abs. 1 DDG (Digitale-Dienste-Gesetz) für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 DDG sind wir als Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen.
		</p>
		<p>
			Verpflichtungen zur Entfernung oder Sperrung der Nutzung von Informationen nach den allgemeinen Gesetzen bleiben hiervon unberührt. Eine diesbezügliche Haftung ist jedoch erst ab dem Zeitpunkt der Kenntnis einer konkreten Rechtsverletzung möglich. Bei Bekanntwerden von entsprechenden Rechtsverletzungen werden wir diese Inhalte umgehend entfernen.
		</p>
	</div>

	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">4. Haftung für Links</h2>
		<p>
			Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben. Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich.
		</p>
		<p>
			Die verlinkten Seiten wurden zum Zeitpunkt der Verlinkung auf mögliche Rechtsverstöße überprüft. Rechtswidrige Inhalte waren zum Zeitpunkt der Verlinkung nicht erkennbar. Eine permanente inhaltliche Kontrolle der verlinkten Seiten ist jedoch ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Links umgehend entfernen.
		</p>
	</div>

	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">5. Urheberrecht (Copyright)</h2>
		<p>
			Die durch den Seitenbetreiber erstellten Inhalte, Texte, Fachartikel, Fotografien, Porträts und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der vorherigen schriftlichen Zustimmung von Alexander Jankowski bzw. des jeweiligen Rechteinhabers.
		</p>
		<p>
			Downloads und Kopien dieser Seite sind ausschließlich für den privaten, nicht kommerziellen Gebrauch gestattet. Soweit die Inhalte auf dieser Seite nicht vom Betreiber erstellt wurden, werden die Urheberrechte Dritter beachtet und entsprechend gekennzeichnet. Sollten Sie trotzdem auf eine Urheberrechtsverletzung aufmerksam werden, bitten wir um einen entsprechenden Hinweis. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Inhalte unverzüglich entfernen.
		</p>
	</div>
    """
    html = get_compliance_template(
        title="Impressum | Alexander Jankowski – Offizielle Webpräsenz",
        meta_desc="Impressum und rechtliche Anbieterkennzeichnung gemäß § 5 DDG und § 18 Abs. 2 MStV für alexanderjankowski.com von Alexander Jankowski, Berlin.",
        canonical_url="https://alexanderjankowski.com/impressum.html",
        active_page="impressum",
        hero_badge="RECHTLICHE HINWEISE &bull; DDG &amp; MStV",
        hero_title="IMPRESSUM",
        hero_subtitle="Angaben gemäß § 5 DDG (Digitale-Dienste-Gesetz, vormals § 5 TMG) sowie § 18 Abs. 2 MStV.",
        card_content=card_content
    )
    with open(os.path.join(BASE_DIR, "impressum.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Created impressum.html")

def build_datenschutz_page():
    card_content = """
	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">1. Datenschutz auf einen Blick</h2>
		<h3 class="compliance-sec-subheading">Allgemeine Hinweise</h3>
		<p>
			Die folgenden Hinweise geben einen einfachen Überblick darüber, was mit Ihren personenbezogenen Daten passiert, wenn Sie diese Website besuchen. Personenbezogene Daten sind alle Daten, mit denen Sie persönlich identifiziert werden können. Ausführliche Informationen zum Thema Datenschutz entnehmen Sie unserer nachfolgend aufgeführten Datenschutzerklärung.
		</p>
		
		<h3 class="compliance-sec-subheading">Datenerfassung auf dieser Website</h3>
		<p>
			<strong>Wer ist verantwortlich für die Datenerfassung auf dieser Website?</strong><br>
			Die Datenverarbeitung auf dieser Website erfolgt durch den Websitebetreiber:
		</p>
		<div class="compliance-highlight-box">
			<p>
				<strong>Alexander Jankowski</strong><br>
				Berlin, Deutschland<br>
				E-Mail: <a href="mailto:alexander@alexanderjankowski.com">alexander@alexanderjankowski.com</a><br>
				Website: <a href="https://alexanderjankowski.com/">https://alexanderjankowski.com/</a>
			</p>
		</div>

		<p>
			<strong>Wie erfassen wir Ihre Daten?</strong><br>
			Ihre Daten werden zum einen dadurch erhoben, dass Sie uns diese mitteilen. Hierbei kann es sich z. B. um Daten handeln, die Sie uns per E-Mail zusenden oder bei der Online-Terminbuchung über Calendly eingeben.<br>
			Andere Daten werden automatisch oder nach Ihrer Einwilligung beim Besuch der Website durch unsere IT-Systeme erfasst. Das sind vor allem technische Daten (z. B. Internetbrowser, Betriebssystem oder Uhrzeit des Seitenaufrufs).
		</p>

		<p>
			<strong>Wofür nutzen wir Ihre Daten?</strong><br>
			Ein Teil der Daten wird erhoben, um eine fehlerfreie und sichere Bereitstellung der Website zu gewährleisten. Andere Daten können zur Analyse Ihres Nutzerverhaltens und zur Optimierung der Benutzerfreundlichkeit verwendet werden.
		</p>

		<p>
			<strong>Welche Rechte haben Sie bezüglich Ihrer Daten?</strong><br>
			Sie haben jederzeit das Recht, unentgeltlich Auskunft über Herkunft, Empfänger und Zweck Ihrer gespeicherten personenbezogenen Daten zu erhalten. Sie haben außerdem ein Recht, die Berichtigung oder Löschung dieser Daten zu verlangen. Wenn Sie eine Einwilligung zur Datenverarbeitung erteilt haben, können Sie diese jederzeit für die Zukunft widerrufen. Zudem steht Ihnen ein Beschwerderecht bei der zuständigen Aufsichtsbehörde zu.
		</p>
	</div>

	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">2. Hosting &amp; Content Delivery Networks (Netlify)</h2>
		<p>
			Wir hosten unsere Website bei <strong>Netlify</strong>. Anbieter ist die Netlify, Inc., 44 Montgomery Street, Suite 300, San Francisco, CA 94104, USA (nachfolgend „Netlify“).
		</p>
		<p>
			Wenn Sie unsere Website besuchen, erfasst Netlify verschiedene Logdateien inklusive Ihrer IP-Adresse. Details entnehmen Sie der Datenschutzerklärung von Netlify: <a href="https://www.netlify.com/privacy/" target="_blank" rel="noopener noreferrer">https://www.netlify.com/privacy/</a>.
		</p>
		<p>
			Die Verwendung von Netlify erfolgt auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO. Wir haben ein berechtigtes Interesse an einer möglichst zuverlässigen, schnellen und sicheren Bereitstellung unserer Website. Die Datenübertragung in die USA wird auf die Standardvertragsklauseln (SCC) der EU-Kommission bzw. das EU-US Data Privacy Framework (DPF) gestützt.
		</p>
	</div>

	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">3. Allgemeine Hinweise &amp; Pflichtinformationen</h2>
		<h3 class="compliance-sec-subheading">SSL- bzw. TLS-Verschlüsselung</h3>
		<p>
			Diese Seite nutzt aus Sicherheitsgründen und zum Schutz der Übertragung vertraulicher Inhalte, wie zum Beispiel Anfragen, die Sie an uns als Seitenbetreiber senden, eine SSL- bzw. TLS-Verschlüsselung. Eine verschlüsselte Verbindung erkennen Sie daran, dass die Adresszeile des Browsers von „http://“ auf „https://“ wechselt und an dem Schloss-Symbol in Ihrer Browserzeile.
		</p>

		<h3 class="compliance-sec-subheading">Widerruf Ihrer Einwilligung zur Datenverarbeitung</h3>
		<p>
			Viele Datenverarbeitungsvorgänge sind nur mit Ihrer ausdrücklichen Einwilligung möglich. Sie können eine bereits erteilte Einwilligung jederzeit widerrufen. Die Rechtmäßigkeit der bis zum Widerruf erfolgten Datenverarbeitung bleibt vom Widerruf unberührt.
		</p>

		<h3 class="compliance-sec-subheading">Beschwerderecht bei der zuständigen Aufsichtsbehörde</h3>
		<p>
			Im Falle von Verstößen gegen die DSGVO steht den Betroffenen ein Beschwerderecht bei einer Aufsichtsbehörde, insbesondere in dem Mitgliedstaat ihres gewöhnlichen Aufenthaltsorts, ihres Arbeitsplatzes oder des Orts des mutmaßlichen Verstoßes zu. Zuständige Aufsichtsbehörde für Berlin ist:<br>
			<strong>Berliner Beauftragte für Datenschutz und Informationsfreiheit</strong><br>
			Alt-Moabit 59-61, 10555 Berlin<br>
			Website: <a href="https://www.datenschutz-berlin.de" target="_blank" rel="noopener noreferrer">www.datenschutz-berlin.de</a>
		</p>
	</div>

	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">4. Datenerfassung auf dieser Website</h2>
		<h3 class="compliance-sec-subheading">Kontaktaufnahme per E-Mail</h3>
		<p>
			Wenn Sie uns per E-Mail kontaktieren, wird Ihre Anfrage inklusive aller daraus hervorgehenden personenbezogenen Daten (Name, E-Mail-Adresse, Inhalt der Nachricht) zum Zwecke der Bearbeitung Ihres Anliegens bei uns gespeichert und verarbeitet. Diese Daten geben wir nicht ohne Ihre Einwilligung weiter.
		</p>
		<p>
			Die Verarbeitung dieser Daten erfolgt auf Grundlage von Art. 6 Abs. 1 lit. b DSGVO, sofern Ihre Anfrage mit der Erfüllung eines Vertrags zusammenhängt oder zur Durchführung vorvertraglicher Maßnahmen erforderlich ist. In allen übrigen Fällen beruht die Verarbeitung auf unserem berechtigten Interesse an der effektiven Bearbeitung der an uns gerichteten Anfragen (Art. 6 Abs. 1 lit. f DSGVO).
		</p>

		<h3 class="compliance-sec-subheading">Online-Terminbuchung über Calendly</h3>
		<p>
			Auf unserer Website bieten wir die Möglichkeit, über den externen Dienst <strong>Calendly</strong> Termine für ein persönliches 1:1 Kennenlerngespräch zu vereinbaren. Anbieter ist die Calendly LLC, 271 17th St NW, 10th Floor, Atlanta, GA 30363, USA.
		</p>
		<p>
			Wenn Sie über den bereitgestellten Link oder das Termin-Widget einen Termin buchen, werden die von Ihnen eingegebenen Daten (z. B. Name, E-Mail-Adresse, gewünschter Gesprächstermin und etwaige Anmerkungen) an Calendly übertragen und dort verarbeitet. Die Nutzung von Calendly erfolgt auf Grundlage von Art. 6 Abs. 1 lit. b DSGVO (Vertragsanbahnung bzw. Terminvereinbarung). Weitere Informationen finden Sie in der Datenschutzerklärung von Calendly: <a href="https://calendly.com/de/pages/privacy" target="_blank" rel="noopener noreferrer">https://calendly.com/de/pages/privacy</a>.
		</p>
	</div>

	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">5. Analyse-Tools &amp; Optimierung (Microsoft Clarity)</h2>
		<p>
			Diese Website nutzt <strong>Microsoft Clarity</strong>, einen Webanalysedienst der Microsoft Corporation, One Microsoft Way, Redmond, WA 98052, USA. Clarity ermöglicht es uns, das Nutzerverhalten (z. B. Mausbewegungen, Scroll-Tiefe, Klicks und Verweildauern) in aggregierter und anonymisierter Form nachzuvollziehen.
		</p>
		<p>
			Clarity maskiert sensible Daten automatisch vor der Aufzeichnung, sodass zu keinem Zeitpunkt vertrauliche persönliche Eingaben oder Passwörter erfasst werden. Die erfassten Informationen helfen uns, die Usability und Navigation der Website zu optimieren.
		</p>
		<p>
			Die Datenverarbeitung erfolgt auf Grundlage von Art. 6 Abs. 1 lit. f DSGVO (berechtigtes Interesse an der bedarfsgerechten Gestaltung, Fehlerbehebung und technischen Weiterentwicklung unserer Online-Präsenz). Weitere Informationen finden Sie unter: <a href="https://privacy.microsoft.com/de-de/privacystatement" target="_blank" rel="noopener noreferrer">https://privacy.microsoft.com/de-de/privacystatement</a>.
		</p>
	</div>

	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">6. Externe Schriftarten &amp; Bibliotheken</h2>
		<p>
			Diese Seite nutzt zur einheitlichen Darstellung von Schriftarten Webfonts von <strong>Adobe Typekit</strong>. Beim Aufruf einer Seite lädt Ihr Browser die benötigten Web-Fonts in ihren Browsercache, um Texte und Schriftarten korrekt anzuzeigen.
		</p>
		<p>
			Zu diesem Zweck muss der von Ihnen verwendete Browser Verbindung zu den Servern von Adobe aufnehmen. Hierdurch erlangt Adobe Kenntnis darüber, dass über Ihre IP-Adresse diese Website aufgerufen wurde. Die Nutzung von Adobe Typekit erfolgt im Interesse einer einheitlichen und ansprechenden Darstellung unserer Online-Angebote. Dies stellt ein berechtigtes Interesse im Sinne von Art. 6 Abs. 1 lit. f DSGVO dar.
		</p>
	</div>

	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">7. Social Media &amp; Externe Verlinkungen (LinkedIn)</h2>
		<p>
			Auf dieser Website finden Sie Verlinkungen zu unserem offiziellen Profil im beruflichen Netzwerk <strong>LinkedIn</strong> (LinkedIn Ireland Unlimited Company, Wilton Place, Dublin 2, Irland).
		</p>
		<p>
			Wir setzen keine automatischen Social-Media-Plugins ein, die bereits beim Laden der Website Nutzerdaten an Social-Media-Betreiber übertragen. Erst wenn Sie den Link zu LinkedIn aktiv anklicken, werden Sie auf die Plattform von LinkedIn weitergeleitet, wo die dortigen Datenschutzrichtlinien gelten: <a href="https://www.linkedin.com/legal/privacy-policy" target="_blank" rel="noopener noreferrer">https://www.linkedin.com/legal/privacy-policy</a>.
		</p>
	</div>
    """
    html = get_compliance_template(
        title="Datenschutzerklärung | Alexander Jankowski – DSGVO &amp; TDDDG",
        meta_desc="Datenschutzerklärung nach EU-DSGVO und TDDDG für alexanderjankowski.com. Umfassende Information über Erhebung, Zweck und Schutz personenbezogener Daten.",
        canonical_url="https://alexanderjankowski.com/datenschutz.html",
        active_page="datenschutz",
        hero_badge="DATENSCHUTZ &amp; DSGVO-KONFORMITÄT",
        hero_title="DATENSCHUTZERKLÄRUNG",
        hero_subtitle="Transparente Information über Art, Umfang und Zweck der Verarbeitung personenbezogener Daten nach EU-DSGVO &amp; TDDDG.",
        card_content=card_content
    )
    with open(os.path.join(BASE_DIR, "datenschutz.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Created datenschutz.html")

def build_agb_page():
    card_content = """
	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">1. Geltungsbereich &amp; Grundsätze</h2>
		<p>
			Diese Allgemeinen Geschäftsbedingungen und Nutzungsbedingungen (nachfolgend „AGB“) gelten für die Nutzung der Website <strong>alexanderjankowski.com</strong> sowie für sämtliche Anfragen, Buchungen von Vorträgen (Speaking Engagements), interaktiven Workshops und individuellen Beratungsleistungen im Bereich B2B-Vertrieb und Account Management durch Alexander Jankowski.
		</p>
		<p>
			Abweichende, entgegenstehende oder ergänzende Allgemeine Geschäftsbedingungen des Kunden oder Vertragspartners werden nur dann und insoweit Vertragsbestandteil, als Alexander Jankowski ihrer Geltung ausdrücklich schriftlich zugestimmt hat.
		</p>
	</div>

	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">2. Leistungsangebot &amp; Vertragsschluss</h2>
		<p>
			<strong>Nutzung der Website:</strong><br>
			Die Bereitstellung der Website und der Fachartikel („Insights“) erfolgt unentgeltlich und dient der beruflichen Information sowie dem professionellen Gedankenaustausch. Ein Rechtsanspruch auf permanente Verfügbarkeit oder bestimmte Inhalte besteht nicht.
		</p>
		<p>
			<strong>Vertragsschluss bei Speaking &amp; Beratung:</strong><br>
			Die Präsentation möglicher Themen auf dieser Website stellt kein rechtlich bindendes Angebot dar, sondern eine Aufforderung zur Kontaktaufnahme. Anfragen über das Kontaktformular, per E-Mail oder Calendly sind unverbindlich. Ein verbindlicher Vertrag über Vorträge oder Beratungsleistungen kommt erst durch ein individuelles schriftliches Angebot und dessen Annahme durch den Kunden zustande.
		</p>
	</div>

	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">3. Urheberrecht &amp; Geistiges Eigentum</h2>
		<p>
			Alle Inhalte dieser Website – insbesondere Texte, Fachbeiträge, Fallstudien, Zitate, Porträts, Businessfotografien, Gestaltungskonzepte und Logos – sind urheberrechtlich geschützt.
		</p>
		<p>
			Die Nutzung, Vervielfältigung oder Weitergabe zu kommerziellen Zwecken bedarf der ausdrücklichen vorherigen schriftlichen Zustimmung von Alexander Jankowski. Insbesondere ist das automatisierte Auslesen, Scraping oder Einlesen von Inhalten dieser Website zum Training von Künstlicher Intelligenz (KI) oder Machine-Learning-Modellen ohne gesonderte schriftliche Lizenzvereinbarung untersagt.
		</p>
	</div>

	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">4. Speaking Engagements, Workshops &amp; Honorare</h2>
		<p>
			Honorarhöhe, Reisekostenabrechnung, technische Anforderungen und Durchführungsmodalitäten für Vorträge oder Workshops werden im jeweiligen Einzelvertrag geregelt.
		</p>
		<p>
			<strong>Verhinderung &amp; Höhere Gewalt:</strong><br>
			Sollte Alexander Jankowski aus Gründen höherer Gewalt oder unverschuldeter Verhinderung (z. B. akute schwere Erkrankung oder gravierende Verkehrsstörungen) einen vereinbarten Termin nicht wahrnehmen können, wird er den Auftraggeber unverzüglich informieren. Die Parteien werden sich in diesem Fall um die Vereinbarung eines zeitnahen Ersatztermins bemühen. Weitergehende Schadensersatzansprüche sind in Fällen unverschuldeter Verhinderung ausgeschlossen.
		</p>
	</div>

	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">5. Haftung &amp; Gewährleistung</h2>
		<p>
			Die auf der Website veröffentlichten Fachbeiträge basieren auf praktischer Berufserfahrung und sorgfältiger Reflexion. Sie stellen jedoch keine Rechts-, Steuer- oder Anlageberatung dar. Für den konkreten wirtschaftlichen Erfolg einzelner Vertriebsmaßnahmen beim Kunden wird keine Gewähr übernommen.
		</p>
		<p>
			Alexander Jankowski haftet uneingeschränkt bei Vorsatz und grober Fahrlässigkeit sowie bei Verletzung des Lebens, des Körpers oder der Gesundheit nach den gesetzlichen Vorschriften.<br>
			Bei leichter Fahrlässigkeit haftet Alexander Jankowski nur bei der Verletzung wesentlicher Vertragspflichten (Kardinalpflichten). In diesem Fall ist die Haftung auf den bei Vertragsschluss typischerweise vorhersehbaren Schaden begrenzt.
		</p>
	</div>

	<div class="compliance-card" data-aos="fade-up" data-aos-duration="1000">
		<h2 class="compliance-sec-heading">6. Schlussbestimmungen &amp; Gerichtsstand</h2>
		<p>
			Es gilt das Recht der Bundesrepublik Deutschland unter Ausschluss des UN-Kaufrechts (CISG).
		</p>
		<p>
			Ist der Kunde Kaufmann, eine juristische Person des öffentlichen Rechts oder ein öffentlich-rechtliches Sondervermögen, ist der Gerichtsstand für alle Streitigkeiten aus oder im Zusammenhang mit Verträgen mit Alexander Jankowski <strong>Berlin</strong>.
		</p>
		<p>
			Sollten einzelne Bestimmungen dieser AGB ganz oder teilweise unwirksam sein oder werden, bleibt die Wirksamkeit der übrigen Bestimmungen hiervon unberührt.
		</p>
		<p style="font-size: 13.5px; color: rgba(255, 255, 255, 0.6); margin-top: 24px;">
			<em>Stand dieser Bedingungen: November 2026 &bull; Alexander Jankowski, Berlin</em>
		</p>
	</div>
    """
    html = get_compliance_template(
        title="AGB &amp; Nutzungsbedingungen | Alexander Jankowski",
        meta_desc="Allgemeine Geschäftsbedingungen und Nutzungsbedingungen für die Website und Leistungen von Alexander Jankowski (alexanderjankowski.com), Berlin.",
        canonical_url="https://alexanderjankowski.com/agb.html",
        active_page="agb",
        hero_badge="RECHTLICHE BEDINGUNGEN &bull; NUTZUNG &amp; BERATUNG",
        hero_title="ALLGEMEINE GESCHÄFTSBEDINGUNGEN",
        hero_subtitle="Bedingungen für die Nutzung von alexanderjankowski.com sowie Richtlinien für Speaking Engagements &amp; Beratung.",
        card_content=card_content
    )
    with open(os.path.join(BASE_DIR, "agb.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Created agb.html")

def update_page_footer(file_path, is_home=False):
    if not os.path.exists(file_path):
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Look for existing footer
    footer_pattern = r'<footer class="fw site-footer">.*?</footer>'
    
    # Construct home vs subpage navigation links
    if is_home:
        quicklinks_html = """<div class="footer-quicklinks">
						<a href="#home">Startseite</a>
						<a href="#about">Über mich</a>
						<a href="#timeline">Mein Weg</a>
						<a href="#work">Vertrieb</a>
						<a href="insights.html">Insights</a>
						<a href="#contact">Kontakt</a>
					</div>"""
    else:
        quicklinks_html = """<div class="footer-quicklinks">
						<a href="/">Startseite</a>
						<a href="/#about">Über mich</a>
						<a href="/#timeline">Mein Weg</a>
						<a href="/#work">Vertrieb</a>
						<a href="insights.html">Insights</a>
						<a href="/#contact">Kontakt</a>
					</div>"""

    new_footer = f"""<footer class="fw site-footer">
		<div class="container-fluid px-4 px-md-5">
			<!-- Top Row: Brand & Quicklinks -->
			<div class="row align-items-center gy-3">
				<div class="col-12 col-md-7 text-center text-md-start">
					<div class="footer-brand-title">ALEXANDER JANKOWSKI</div>
					<div class="footer-meta-info">
						<span>&copy; 2026 Alexander Jankowski</span>
						<span class="footer-dot">&bull;</span>
						<span>Berlin, Deutschland</span>
						<span class="footer-dot d-none d-sm-inline">&bull;</span>
						<span class="d-block d-sm-inline mt-1 mt-sm-0 text-white-50">Vertrieb &bull; Account Management &bull; Neukundengewinnung</span>
					</div>
				</div>
				<div class="col-12 col-md-5 text-center text-md-end">
					<p class="footer-motto mb-2">„Unterschiedliche Stationen. Eine Konstante: Menschen.“</p>
					{quicklinks_html}
				</div>
			</div>

			<!-- Subtle Divider -->
			<div class="footer-divider"></div>

			<!-- Bottom Row: Legal Compliances & LinkedIn -->
			<div class="row align-items-center gy-3 footer-bottom-row">
				<div class="col-12 col-md-8 text-center text-md-start">
					<div class="footer-compliance-links">
						<a href="impressum.html">Impressum</a>
						<span class="footer-dot">&bull;</span>
						<a href="datenschutz.html">Datenschutz</a>
						<span class="footer-dot">&bull;</span>
						<a href="agb.html">AGB &amp; Nutzungsbedingungen</a>
					</div>
				</div>
				<div class="col-12 col-md-4 text-center text-md-end">
					<div class="footer-social-wrap">
						<a href="https://www.linkedin.com/in/alexander-jankowski-320ab6447/" target="_blank" rel="noopener noreferrer" class="footer-linkedin-badge" aria-label="LinkedIn Profil von Alexander Jankowski">
							<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
							<span>LinkedIn</span>
							<span class="ext-arrow">&nearr;</span>
						</a>
					</div>
				</div>
			</div>
		</div>
	</footer>"""

    if re.search(footer_pattern, content, re.S):
        content = re.sub(footer_pattern, new_footer, content, flags=re.S)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated footer in {os.path.basename(file_path)}")
    else:
        print(f"Warning: Footer not matched in {os.path.basename(file_path)}")

def update_redirects():
    paths = [
        os.path.join(BASE_DIR, "_redirects"),
        os.path.join(BASE_DIR, "public", "_redirects")
    ]
    
    compliance_rules = """
# Legal Compliances (DDG, DSGVO, AGB)
/impressum      /impressum.html 200
/imprint        /impressum.html 301
/datenschutz    /datenschutz.html 200
/privacy        /datenschutz.html 301
/agb            /agb.html       200
/terms          /agb.html       301
/nutzungsbedingungen /agb.html  301
/conditions     /agb.html       301
"""

    for p in paths:
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                content = f.read()
            if "/impressum" not in content:
                # Insert before catch-all /* /index.html 200
                if "/*              /index.html     200" in content:
                    content = content.replace("/*              /index.html     200", compliance_rules.strip() + "\n\n/*              /index.html     200")
                elif "/*" in content:
                    idx = content.rfind("/*")
                    content = content[:idx] + compliance_rules.strip() + "\n\n" + content[idx:]
                else:
                    content += "\n" + compliance_rules
                with open(p, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated redirects in {p}")
            else:
                print(f"{p} already has compliance redirects.")

def update_sitemaps():
    paths = [
        os.path.join(BASE_DIR, "sitemap.xml"),
        os.path.join(BASE_DIR, "public", "sitemap.xml")
    ]

    sitemap_entries = """
  <!-- Legal Compliances -->
  <url>
    <loc>https://alexanderjankowski.com/impressum.html</loc>
    <lastmod>2026-11-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>

  <url>
    <loc>https://alexanderjankowski.com/datenschutz.html</loc>
    <lastmod>2026-11-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>

  <url>
    <loc>https://alexanderjankowski.com/agb.html</loc>
    <lastmod>2026-11-10</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
"""

    for p in paths:
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                content = f.read()
            if "impressum.html" not in content:
                content = content.replace("</urlset>", sitemap_entries.strip() + "\n\n</urlset>")
                with open(p, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated sitemap in {p}")
            else:
                print(f"{p} already has compliance sitemap entries.")

def main():
    print("--- Executing Compliance & Footer Updates ---")
    update_css()
    build_impressum_page()
    build_datenschutz_page()
    build_agb_page()
    
    # Update footers in all pages
    update_page_footer(os.path.join(BASE_DIR, "index.html"), is_home=True)
    update_page_footer(os.path.join(BASE_DIR, "insights.html"), is_home=False)
    update_page_footer(os.path.join(BASE_DIR, "variation-navy.html"), is_home=True)
    update_page_footer(os.path.join(BASE_DIR, "variation-teal.html"), is_home=True)
    
    update_redirects()
    update_sitemaps()
    print("--- All Compliance Updates Complete! ---")

if __name__ == "__main__":
    main()
