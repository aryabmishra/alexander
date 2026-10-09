#!/usr/bin/env python3
import os
import re

DIR = "/Users/aryabmishra/Downloads/Website Replicates/alexander-jankowski"

# -------------------------------------------------------------
# 1. Update index.html, variation-navy.html, variation-teal.html
# -------------------------------------------------------------
home_files = ["index.html", "variation-navy.html", "variation-teal.html"]

intro_replacement = """					<h2 style="font-size: clamp(32px, 3.8vw, 56px); line-height: 1.15; margin-bottom: 20px;">Vertrieb. Beziehungen. Vertrauen. Entwicklung.</h2>
					<p style="font-family: paralucent, sans-serif; font-size: clamp(17px, 1.25vw, 22px); line-height: 1.6; color: rgba(255, 255, 255, 0.82); margin-bottom: 30px; max-width: 580px;">Mein Weg führte mich von der Polizei über die Fitnessbranche bis in den Vertrieb. Was sich dabei nie verändert hat: mein Interesse an Menschen, Kommunikation und echten Beziehungen.</p>
					<a href="#timeline" class="btn">Mehr über meinen Weg</a>"""

speaker_replacement = """						<h2>MENSCHEN &amp; UNTERNEHMEN <br>ZUSAMMENBRINGEN</h2>
						<p>Langfristig möchte ich meine Erfahrung im Vertrieb mit meiner Stärke im Umgang mit Menschen verbinden und dort arbeiten, wo Beziehungen, Vertrauen und neue Möglichkeiten entstehen.</p>
						<p>Vertrieb bedeutet für mich nicht, möglichst viel zu reden. Es bedeutet, die richtigen Fragen zu stellen, zuzuhören, Zusammenhänge zu verstehen und herauszufinden, ob auf beiden Seiten echter Mehrwert entstehen kann.</p>
						<a href="#contact-form" class="btn2">Nachricht senden</a>"""

contact_subtext = "Mein Weg hat mich durch sehr unterschiedliche Bereiche geführt. Deshalb freue ich mich auf Gespräche mit Menschen aus Vertrieb, Fitness, Polizei und darüber hinaus."

news_slides_replacement = """							<a href="insights.html#article-1" class="swiper-slide news-block">
								<div class="news-thumb">
									<img src="images/news-1.jpg" alt="Was Polizeiarbeit über den Umgang mit Druck lehrt">
								</div>
								<div class="fw">
									<ul class="news-tags"><li>Polizei &amp; Haltung</li></ul>
									<h3>Was Polizeiarbeit über den Umgang mit Druck lehrt</h3>
								</div>
							</a>

							<a href="insights.html#article-2" class="swiper-slide news-block">
								<div class="news-thumb">
									<img src="images/news-5.jpg" alt="Warum Disziplin wichtiger sein kann als Motivation">
								</div>
								<div class="fw">
									<ul class="news-tags"><li>Fitness-Coaching</li></ul>
									<h3>Warum Disziplin wichtiger sein kann als Motivation</h3>
								</div>
							</a>

							<a href="insights.html#article-3" class="swiper-slide news-block">
								<div class="news-thumb">
									<img src="images/news-6.jpg" alt="Wann Menschen wirklich zuhören">
								</div>
								<div class="fw">
									<ul class="news-tags"><li>Kommunikation</li></ul>
									<h3>Wann Menschen wirklich zuhören</h3>
								</div>
							</a>

							<a href="insights.html#article-4" class="swiper-slide news-block">
								<div class="news-thumb">
									<img src="images/news-4.jpg" alt="Wann Vertrauen in Geschäftsbeziehungen entsteht">
								</div>
								<div class="fw">
									<ul class="news-tags"><li>Vertrieb &amp; Vertrauen</li></ul>
									<h3>Wann Vertrauen in Geschäftsbeziehungen entsteht</h3>
								</div>
							</a>"""

for filename in home_files:
    filepath = os.path.join(DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Meta updates
    content = re.sub(r'B2B Vertrieb &amp; Account Management Berlin', 'Vertrieb, Beziehungen &amp; Account Management', content)
    content = re.sub(r'B2B Vertriebsprofi und Account Manager aus Berlin', 'Vertriebsprofi und Account Manager aus Berlin', content)
    content = re.sub(r'bis in den B2B Vertrieb', 'bis in den Vertrieb', content)
    content = re.sub(r'B2B Vertrieb &amp; Account Management', 'Vertrieb &amp; Account Management', content)
    content = re.sub(r'"B2B Vertrieb, Account Management,', '"Vertrieb, Account Management,', content)

    # Intro Section replacement
    intro_pattern = r'<h2>Alexander Jankowski;.*?</h2>\s*<a href="#timeline" class="btn">Mehr über meinen Weg</a>'
    content = re.sub(intro_pattern, intro_replacement, content, flags=re.DOTALL)

    # Speaker / Vision Section replacement
    speaker_pattern = r'<h2>WIE ICH <br>VERTRIEB SEHE</h2>.*?<a href="#contact-form" class="btn2">Nachricht senden</a>'
    content = re.sub(speaker_pattern, speaker_replacement, content, flags=re.DOTALL)

    # Contact subtext replacement
    contact_pattern = r'<p class="connect-subtext">.*?</p>'
    content = re.sub(contact_pattern, f'<p class="connect-subtext">{contact_subtext}</p>', content, flags=re.DOTALL)

    # News slides replacement
    news_pattern = r'<div class="swiper-wrapper">\s*<a href="insights\.html#article-1".*?</a>\s*</div>'
    content = re.sub(news_pattern, f'<div class="swiper-wrapper">\n{news_slides_replacement}\n\t\t\t\t\t\t</div>', content, flags=re.DOTALL)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {filename}")

# -------------------------------------------------------------
# 2. Update insights.html
# -------------------------------------------------------------
insights_path = os.path.join(DIR, "insights.html")
with open(insights_path, "r", encoding="utf-8") as f:
    ins = f.read()

# Meta & Subtitle
ins = re.sub(r'B2B Vertrieb &amp; Account Management', 'Vertrieb, Kommunikation &amp; Haltung', ins)
ins = re.sub(r'B2B-Vertrieb, Neukundengewinnung, Account Management und Disziplin', 'Vertrieb, Kommunikation, Vertrauen und mentaler Disziplin', ins)
ins = re.sub(r'B2B-Vertrieb, Verhandlungsführung und mentaler Disziplin', 'Vertrieb, Kommunikation, Vertrauen und mentaler Disziplin', ins)
ins = re.sub(r'Leistungssport', 'Fitness-Coaching', ins)
ins = re.sub(r'High-Ticket-B2B-Verhandlungen', 'Verhandlungen', ins)
ins = re.sub(r'B2B-Kunden', 'Kunden', ins)
ins = re.sub(r'B2B Vertrieb &bull;', 'Vertrieb &bull;', ins)
ins = re.sub(r'B2B VERTRIEB', 'VERTRIEB', ins)

# Filter pills: 4 focused pills
filter_pills_replacement = """				<button class="filter-pill active" data-filter="all">Alle Artikel (4)</button>
				<button class="filter-pill" data-filter="polizei">Polizei &amp; Druck</button>
				<button class="filter-pill" data-filter="fitness">Fitness &amp; Disziplin</button>
				<button class="filter-pill" data-filter="kommunikation">Kommunikation</button>
				<button class="filter-pill" data-filter="vertrieb">Vertrieb &amp; Vertrauen</button>"""

filter_pattern = r'<div class="filter-wrap"[^>]*>.*?</div>'
ins = re.sub(filter_pattern, f'<div class="filter-wrap" data-aos="fade-up" data-aos-delay="200" data-aos-duration="1000">\n{filter_pills_replacement}\n\t\t\t</div>', ins, flags=re.DOTALL)

# Hero subtitle
hero_subtitle = """Reale Lektionen aus Polizei, Fitness-Coaching und Vertrieb. Über den Umgang mit Druck, verlässliche Routinen, aktives Zuhören und Vertrauen als echtes Fundament."""
ins = re.sub(r'<p class="insights-subtitle">.*?</p>', f'<p class="insights-subtitle">\n\t\t\t\t\t{hero_subtitle}\n\t\t\t\t</p>', ins, flags=re.DOTALL)

# Featured Spotlight card update
spotlight_replacement = """			<!-- Featured Spotlight Article -->
			<div data-aos="fade-up" data-aos-duration="1000">
				<a href="javascript:void(0)" class="featured-card-wrap" onclick="openInsightModal(1)">
					<div class="row g-0 align-items-center">
						<div class="col-lg-6">
							<div class="featured-thumb-container">
								<span class="featured-badge">Spotlight Insight</span>
								<img src="images/news-1.jpg" alt="Was Polizeiarbeit über den Umgang mit Druck lehrt">
							</div>
						</div>
						<div class="col-lg-6">
							<div class="featured-content">
								<div class="featured-meta">
									<span>Polizei &amp; Haltung</span> &bull; <span>5 Min. Lesezeit</span> &bull; <span>Autor: Alexander Jankowski</span>
								</div>
								<h2 class="featured-title">Was Polizeiarbeit über den Umgang mit Druck lehrt</h2>
								<p class="featured-excerpt">
									Ein Notruf geht ein. Keine Zeit zum Nachdenken, keine zweite Chance. Warum Druck seine Macht verliert, wenn man vorbereitet ist – im Einsatz genauso wie im Beruf.
								</p>
								<span class="btn2">Diesen Insight lesen &rarr;</span>
							</div>
						</div>
					</div>
				</a>
			</div>"""

featured_pattern = r'<!-- Featured Spotlight Article -->.*?</a>\s*</div>'
ins = re.sub(featured_pattern, spotlight_replacement, ins, flags=re.DOTALL)

# Grid of All Insights: Exactly 4 balanced cards in a 2x2 grid (col-12 col-md-6)
# Each card has identical structure, flex height, even layout
grid_replacement = """			<!-- Grid of All Insights (Even 2x2 Balanced Layout) -->
			<div class="row g-4" id="insights-grid">

				<!-- Article 1: Polizei -->
				<div class="col-12 col-md-6 insight-item" data-category="polizei">
					<div class="insight-card" onclick="openInsightModal(1)">
						<div class="insight-thumb">
							<img src="images/news-1.jpg" alt="Was Polizeiarbeit über den Umgang mit Druck lehrt">
						</div>
						<div class="insight-body">
							<div class="insight-tags">
								<span class="insight-tag">Polizei</span>
								<span class="insight-tag">Druck &amp; Haltung</span>
							</div>
							<h3 class="insight-card-title">Was Polizeiarbeit über den Umgang mit Druck lehrt</h3>
							<p class="insight-card-desc">
								Ein Notruf geht ein. Keine Zeit zum Nachdenken, keine zweite Chance. Warum Druck seine Macht verliert, wenn man vorbereitet ist – im Einsatz genauso wie im Job.
							</p>
							<div class="insight-footer-meta">
								<span>Alexander Jankowski</span>
								<span class="reading-time">5 Min. Lesezeit</span>
							</div>
						</div>
					</div>
				</div>

				<!-- Article 2: Fitness & Disziplin -->
				<div class="col-12 col-md-6 insight-item" data-category="fitness">
					<div class="insight-card" onclick="openInsightModal(2)">
						<div class="insight-thumb">
							<img src="images/news-5.jpg" alt="Warum Disziplin wichtiger sein kann als Motivation">
						</div>
						<div class="insight-body">
							<div class="insight-tags">
								<span class="insight-tag">Fitness-Coaching</span>
								<span class="insight-tag">Routinen</span>
							</div>
							<h3 class="insight-card-title">Warum Disziplin wichtiger sein kann als Motivation</h3>
							<p class="insight-card-desc">
								Motivation ist ein Gefühl, und Gefühle schwanken. Warum Disziplin genau dort ansetzt, wo Motivation endet – und wie feste Routinen Entscheidungen abnehmen.
							</p>
							<div class="insight-footer-meta">
								<span>Alexander Jankowski</span>
								<span class="reading-time">5 Min. Lesezeit</span>
							</div>
						</div>
					</div>
				</div>

				<!-- Article 3: Kommunikation -->
				<div class="col-12 col-md-6 insight-item" data-category="kommunikation">
					<div class="insight-card" onclick="openInsightModal(3)">
						<div class="insight-thumb">
							<img src="images/news-6.jpg" alt="Wann Menschen wirklich zuhören">
						</div>
						<div class="insight-body">
							<div class="insight-tags">
								<span class="insight-tag">Kommunikation</span>
								<span class="insight-tag">Relevanz</span>
							</div>
							<h3 class="insight-card-title">Wann Menschen wirklich zuhören</h3>
							<p class="insight-card-desc">
								Kennst du das? Dein Gegenüber nickt, ist aber gedanklich woanders. Warum Relevanz alles verändert und Zuhören immer bei dem anfängt, der spricht.
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
							<img src="images/news-4.jpg" alt="Wann Vertrauen in Geschäftsbeziehungen entsteht">
						</div>
						<div class="insight-body">
							<div class="insight-tags">
								<span class="insight-tag">Vertrieb</span>
								<span class="insight-tag">Vertrauen</span>
							</div>
							<h3 class="insight-card-title">Wann Vertrauen in Geschäftsbeziehungen entsteht</h3>
							<p class="insight-card-desc">
								Ein Kunde sagt Ja – nicht wegen des billigsten Preises, sondern aus Vertrauen. Auf welche drei Fragen es wirklich ankommt und warum Kleinigkeiten entscheiden.
							</p>
							<div class="insight-footer-meta">
								<span>Alexander Jankowski</span>
								<span class="reading-time">5 Min. Lesezeit</span>
							</div>
						</div>
					</div>
				</div>

			</div>"""

grid_pattern = r'<!-- Grid of All Insights -->.*?</div>\s*<!-- CTA Banner Section -->'
ins = re.sub(grid_pattern, f'{grid_replacement}\n\n\t\t\t<!-- CTA Banner Section -->', ins, flags=re.DOTALL)

# Bottom CTA Banner in insights.html
ins_cta_replacement = """			<!-- CTA Banner Section -->
			<div class="insights-cta-wrap" data-aos="fade-up" data-aos-duration="1000">
				<h2 class="insights-cta-title">LASSEN SIE UNS VERNETZEN</h2>
				<p class="insights-cta-subtitle">
					Mein Weg hat mich durch sehr unterschiedliche Bereiche geführt. Deshalb freue ich mich auf Gespräche mit Menschen aus Vertrieb, Fitness, Polizei und darüber hinaus.
				</p>
				<div class="btn-cta-group">
					<a href="https://www.linkedin.com/in/alexander-jankowski-03491242a/" target="_blank" rel="noopener noreferrer" class="btn2">
						Auf LinkedIn vernetzen &rarr;
					</a>
					<a href="/#contact" class="btn2">
						Direkte Nachricht senden
					</a>
				</div>
			</div>"""

ins_cta_pattern = r'<!-- CTA Banner Section -->.*?</div>\s*</div>\s*</main>'
ins = re.sub(ins_cta_pattern, f'{ins_cta_replacement}\n\t\t</div>\n\t</main>', ins, flags=re.DOTALL)

# Modal Articles Data: The exact texts provided by the user
articles_data_replacement = """		// Article Data for Rich Modal Experience (Directly from Alexander Jankowski)
		var articlesData = {
			1: {
				title: "Was Polizeiarbeit über den Umgang mit Druck lehrt",
				category: "POLIZEI & DRUCK",
				meta: "Oktober 2026 &bull; 5 Min. Lesezeit &bull; Autor: Alexander Jankowski",
				content: `
					<p>Ein Notruf geht ein. Keine Zeit zum Nachdenken, keine zweite Chance. Und trotzdem wird eine Entscheidung erwartet, und zwar die richtige. Wie schafft man das?</p>
					
					<p>Die ehrliche Antwort: nicht mit Talent. Unter Stress spielt unser Körper verrückt. Der Puls rast, der Blick wird eng, klares Denken wird schwer. Genau deshalb verlässt sich die Polizei nicht darauf, dass im Ernstfall schon die richtige Idee kommt. Abläufe werden trainiert, bis sie sitzen. Und sogar ruhiges, bewusstes Atmen gehört zur Ausbildung, weil es den Kopf wieder freimacht.</p>
					
					<blockquote>„Druck verschwindet nicht. Aber er verliert seine Macht, wenn man vorbereitet ist.“</blockquote>
					
					<p>Was ich daraus mitnehme? Druck verschwindet nicht. Aber er verliert seine Macht, wenn man vorbereitet ist. Wer seine Abläufe kennt und einmal kurz durchatmet, bevor er reagiert, bleibt ruhig, auch wenn es drumherum laut wird. Im Einsatz genauso wie im Job.</p>
				`
			},
			2: {
				title: "Warum Disziplin wichtiger sein kann als Motivation",
				category: "FITNESS-COACHING & ROUTINEN",
				meta: "Oktober 2026 &bull; 5 Min. Lesezeit &bull; Autor: Alexander Jankowski",
				content: `
					<p>Motivation ist ein Gefühl, und Gefühle schwanken. An manchen Tagen ist sie groß, an anderen kaum spürbar. Wer seine Ziele nur dann verfolgt, wenn er sich danach fühlt, macht seinen Fortschritt von der Tagesform abhängig. Disziplin setzt genau dort an, wo Motivation endet: Sie sorgt dafür, dass wir handeln, auch wenn die Lust fehlt.</p>

					<p>Disziplin bedeutet dabei nicht Härte gegen sich selbst, sondern das Schaffen verlässlicher Routinen. Kleine, feste Schritte, die unabhängig von der Stimmung umgesetzt werden, summieren sich über Wochen und Monate zu messbaren Ergebnissen. Motivation kann den Anfang erleichtern. Disziplin sorgt dafür, dass man dranbleibt.</p>

					<blockquote>„Disziplin bedeutet nicht Härte gegen sich selbst, sondern das Schaffen verlässlicher Routinen.“</blockquote>

					<p>Ich habe das selbst im Fitnessbereich erlebt, vor allem bei der Ernährung. Am Anfang war die Motivation hoch, doch sie hielt selten länger als ein paar Wochen. Nach einem stressigen Tag fiel die gesunde Mahlzeit schnell weg. Geändert hat sich das erst, als ich feste Routinen eingeführt habe: Mahlzeiten im Voraus planen und vorbereiten, zu ähnlichen Zeiten essen und die Entscheidung nicht jeden Tag neu treffen müssen. Heute muss ich mich dafür gar nicht mehr überwinden. Nicht, weil ich jeden Tag motiviert bin, sondern weil die Routine die Entscheidung für mich übernimmt.</p>
				`
			},
			3: {
				title: "Wann Menschen wirklich zuhören",
				category: "KOMMUNIKATION & RELEVANZ",
				meta: "Oktober 2026 &bull; 4 Min. Lesezeit &bull; Autor: Alexander Jankowski",
				content: `
					<p>Kennst du das? Du erzählst etwas, und dein Gegenüber nickt, aber du merkst genau, dass er gedanklich woanders ist. Das liegt nicht unbedingt an Desinteresse. Wir denken einfach schneller, als andere sprechen. Und die freie Zeit nutzt unser Kopf für eigene Gedanken oder dafür, schon mal die Antwort vorzubereiten.</p>

					<p>Was ändert das? Relevanz. Es gibt dazu ein schönes Beispiel aus der Psychologie, den sogenannten Cocktailparty-Effekt: Selbst in einem lauten Raum horchen wir sofort auf, wenn jemand unseren Namen sagt. Und Studien zeigen auch, dass wir uns Dinge viel besser merken, wenn sie etwas mit uns selbst zu tun haben.</p>

					<blockquote>„Menschen hören dann zu, wenn es um sie geht. Zuhören fängt also bei dem an, der spricht.“</blockquote>

					<p>Für mich heißt das: Menschen hören dann zu, wenn es um sie geht. Wenn ich also möchte, dass mir jemand wirklich zuhört, frage ich lieber nach, greife auf, was er gesagt hat, und rede über das, was für ihn wichtig ist. Nicht nur über das, was ich loswerden will. Zuhören fängt also bei dem an, der spricht.</p>
				`
			},
			4: {
				title: "Wann Vertrauen in Geschäftsbeziehungen entsteht",
				category: "VERTRIEB & BEZIEHUNGEN",
				meta: "Oktober 2026 &bull; 5 Min. Lesezeit &bull; Autor: Alexander Jankowski",
				content: `
					<p>Ein Kunde sagt Ja. Nicht weil mein Angebot das günstigste war. Sondern weil er mir vertraut hat. Aber wann genau passiert das eigentlich?</p>

					<p>Ganz ehrlich: selten im ersten Gespräch. Vertrauen lässt sich nicht einfordern, man verdient es sich. Und am Ende läuft es für mich auf drei Fragen hinaus, die sich jeder Kunde stellt, bewusst oder unbewusst: Kann der das wirklich? Meint der es gut mit mir? Und hält der, was er sagt?</p>

					<blockquote>„Vertrauen lässt sich nicht einfordern, man verdient es sich.“</blockquote>

					<p>Die Antwort darauf geben keine großen Versprechen, sondern Kleinigkeiten. Zurückrufen, wenn ich es gesagt habe. Ehrlich sein, auch wenn ich dann mal nichts verkaufe und mich wirklich für die Situation des anderen interessieren. Genau daran merken Menschen, ob sie sich auf jemanden verlassen können.</p>
				`
			}
		};"""

articles_data_pattern = r'// Article Data for Rich Modal Experience.*?var articlesData = \{.*?\n\t\t\};'
ins = re.sub(articles_data_pattern, articles_data_replacement, ins, flags=re.DOTALL)

with open(insights_path, "w", encoding="utf-8") as f:
    f.write(ins)
print("Updated insights.html")
