/**
 * SEO & Structured Data Utilities for Alexander Jankowski
 * Official Website: https://alexanderjankowski.com/
 */

export interface SEOProps {
  title: string;
  description: string;
  keywords?: string;
  image?: string;
  url?: string;
  type?: 'website' | 'profile' | 'article';
  canonical?: string;
  locale?: string;
}

export const DEFAULT_SEO_CONFIG = {
  name: 'Alexander Jankowski',
  jobTitle: 'Junior Account Manager',
  company: '1&1 Versatel',
  location: 'Berlin, Deutschland',
  defaultUrl: 'https://alexanderjankowski.com',
  defaultTitle: 'Alexander Jankowski | Vertrieb, Beziehungen & Account Management Berlin',
  defaultDescription:
    'Offizielle Website von Alexander Jankowski (alexanderjankowski.com). Vertriebsprofi und Junior Account Manager aus Berlin – spezialisiert auf B2B-Vertrieb, Kaltakquise, Neukundengewinnung und nachhaltige Kundenbeziehungen.',
  defaultKeywords:
    'Alexander Jankowski, Alexander Jankowski Berlin, Alexander Jankowski Vertrieb, Alexander Jankowski Account Manager, Alexander Jankowski 1&1 Versatel, alexanderjankowski.com, B2B Vertrieb Berlin, Account Management, Neukundengewinnung, Kaltakquise, Kundenbeziehungen, Vertriebsprofi Berlin',
  defaultImage: 'https://alexanderjankowski.com/images/og-image.jpg',
  contactEmail: 'alexander@alexanderjankowski.com',
  calendlyUrl: 'https://calendly.com/aj-alexanderjankowski/get2know',
  linkedinUrl: 'https://www.linkedin.com/in/alexander-jankowski-03491242a/',
};

/**
 * Dynamically updates or creates meta tags, title, Open Graph, and Twitter tags in the DOM.
 */
export const updatePageSEO = ({
  title,
  description,
  keywords,
  image,
  url,
  type = 'website',
  canonical,
  locale = 'de_DE',
}: SEOProps) => {
  const fullTitle = title.includes(DEFAULT_SEO_CONFIG.name)
    ? title
    : `${title} | ${DEFAULT_SEO_CONFIG.name}`;
  const targetUrl = url || DEFAULT_SEO_CONFIG.defaultUrl;
  const targetImage = image || DEFAULT_SEO_CONFIG.defaultImage;
  const targetKeywords = keywords || DEFAULT_SEO_CONFIG.defaultKeywords;

  // Title
  document.title = fullTitle;

  const updateMetaTag = (selector: string, content: string) => {
    let element = document.querySelector(selector);
    if (!element) {
      element = document.createElement('meta');
      const attribute = selector.includes('property') ? 'property' : 'name';
      const value = selector.match(/["']([^"']+)["']/)?.[1] || '';
      element.setAttribute(attribute, value);
      document.head.appendChild(element);
    }
    element.setAttribute('content', content);
  };

  // Primary Standard Meta Tags
  updateMetaTag('meta[name="title"]', fullTitle);
  updateMetaTag('meta[name="description"]', description);
  updateMetaTag('meta[name="keywords"]', targetKeywords);
  updateMetaTag('meta[name="author"]', DEFAULT_SEO_CONFIG.name);
  updateMetaTag('meta[name="publisher"]', DEFAULT_SEO_CONFIG.defaultUrl);
  updateMetaTag(
    'meta[name="robots"]',
    'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large'
  );

  // Geographic Tags (Local SEO Berlin)
  updateMetaTag('meta[name="geo.region"]', 'DE-BE');
  updateMetaTag('meta[name="geo.placename"]', 'Berlin');

  // Open Graph
  updateMetaTag('meta[property="og:locale"]', locale);
  updateMetaTag('meta[property="og:type"]', type);
  updateMetaTag('meta[property="og:url"]', targetUrl);
  updateMetaTag('meta[property="og:site_name"]', DEFAULT_SEO_CONFIG.name);
  updateMetaTag('meta[property="og:title"]', fullTitle);
  updateMetaTag('meta[property="og:description"]', description);
  updateMetaTag('meta[property="og:image"]', targetImage);
  updateMetaTag('meta[property="og:image:secure_url"]', targetImage);

  // Direct Image Source for Link Previews & Aggregators
  let imageSrcLink = document.querySelector('link[rel="image_src"]') as HTMLLinkElement;
  if (!imageSrcLink) {
    imageSrcLink = document.createElement('link');
    imageSrcLink.rel = 'image_src';
    document.head.appendChild(imageSrcLink);
  }
  imageSrcLink.href = targetImage;

  // LinkedIn Specific Cards
  updateMetaTag('meta[name="image"]', targetImage);
  updateMetaTag('meta[property="article:author"]', DEFAULT_SEO_CONFIG.linkedinUrl);

  // Twitter / X Cards
  updateMetaTag('meta[name="twitter:card"]', 'summary_large_image');
  updateMetaTag('meta[name="twitter:url"]', targetUrl);
  updateMetaTag('meta[name="twitter:title"]', fullTitle);
  updateMetaTag('meta[name="twitter:description"]', description);
  updateMetaTag('meta[name="twitter:image"]', targetImage);

  // Canonical Link
  let canonicalLink = document.querySelector('link[rel="canonical"]') as HTMLLinkElement;
  if (!canonicalLink) {
    canonicalLink = document.createElement('link');
    canonicalLink.rel = 'canonical';
    document.head.appendChild(canonicalLink);
  }
  canonicalLink.href = canonical || targetUrl;
};

/**
 * Inserts or replaces a JSON-LD structured data script in document head.
 */
export const addStructuredData = (data: object, scriptId = 'structured-data-seo') => {
  let script = document.getElementById(scriptId) as HTMLScriptElement | null;
  if (!script) {
    script = document.createElement('script');
    script.id = scriptId;
    script.type = 'application/ld+json';
    document.head.appendChild(script);
  }
  script.textContent = JSON.stringify(data, null, 2);
};

/**
 * Generates Schema.org Person definition for Alexander Jankowski.
 */
export const generatePersonSchema = () => {
  return {
    '@context': 'https://schema.org',
    '@type': 'Person',
    '@id': `${DEFAULT_SEO_CONFIG.defaultUrl}/#person`,
    name: DEFAULT_SEO_CONFIG.name,
    givenName: 'Alexander',
    familyName: 'Jankowski',
    url: DEFAULT_SEO_CONFIG.defaultUrl,
    image: `${DEFAULT_SEO_CONFIG.defaultUrl}/images/alexander-cutout.png`,
    jobTitle: DEFAULT_SEO_CONFIG.jobTitle,
    worksFor: {
      '@type': 'Organization',
      name: DEFAULT_SEO_CONFIG.company,
      url: 'https://www.1und1.net/',
    },
    alumniOf: [
      {
        '@type': 'Organization',
        name: 'Polizei Berlin',
      },
    ],
    address: {
      '@type': 'PostalAddress',
      addressLocality: 'Berlin',
      addressRegion: 'Berlin',
      addressCountry: 'DE',
    },
    email: `mailto:${DEFAULT_SEO_CONFIG.contactEmail}`,
    description: DEFAULT_SEO_CONFIG.defaultDescription,
    sameAs: [
      DEFAULT_SEO_CONFIG.linkedinUrl,
      DEFAULT_SEO_CONFIG.calendlyUrl,
      DEFAULT_SEO_CONFIG.defaultUrl,
    ],
    knowsAbout: [
      'B2B-Vertrieb',
      'Account Management',
      'Kaltakquise',
      'Neukundengewinnung',
      'Pipeline Management',
      'Kundenbeziehungen',
      'Telekommunikation',
      'Verhandlungsführung',
    ],
  };
};

/**
 * Generates WebSite Schema.org markup.
 */
export const generateWebsiteSchema = () => {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    '@id': `${DEFAULT_SEO_CONFIG.defaultUrl}/#website`,
    url: DEFAULT_SEO_CONFIG.defaultUrl,
    name: DEFAULT_SEO_CONFIG.name,
    alternateName: ['alexanderjankowski.com', 'Alexander Jankowski Website'],
    description: DEFAULT_SEO_CONFIG.defaultDescription,
    publisher: {
      '@id': `${DEFAULT_SEO_CONFIG.defaultUrl}/#person`,
    },
    inLanguage: 'de-DE',
  };
};

/**
 * Generates Article schema for insights/blog posts.
 */
export const generateArticleSchema = (article: {
  title: string;
  description: string;
  image: string;
  slug: string;
  datePublished?: string;
  dateModified?: string;
}) => {
  const articleUrl = `${DEFAULT_SEO_CONFIG.defaultUrl}/insights.html#${article.slug}`;
  return {
    '@context': 'https://schema.org',
    '@type': 'Article',
    mainEntityOfPage: {
      '@type': 'WebPage',
      '@id': articleUrl,
    },
    headline: article.title,
    description: article.description,
    image: article.image.startsWith('http')
      ? article.image
      : `${DEFAULT_SEO_CONFIG.defaultUrl}/${article.image}`,
    author: {
      '@type': 'Person',
      name: DEFAULT_SEO_CONFIG.name,
      url: DEFAULT_SEO_CONFIG.defaultUrl,
    },
    publisher: {
      '@type': 'Person',
      name: DEFAULT_SEO_CONFIG.name,
      url: DEFAULT_SEO_CONFIG.defaultUrl,
    },
    datePublished: article.datePublished || '2026-10-01',
    dateModified: article.dateModified || '2026-10-30',
    inLanguage: 'de-DE',
  };
};

/**
 * Generates FAQ Schema for common prospect questions.
 */
export const generateFAQSchema = (faqs: Array<{ question: string; answer: string }>) => {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map((faq) => ({
      '@type': 'Question',
      name: faq.question,
      acceptedAnswer: {
        '@type': 'Answer',
        text: faq.answer,
      },
    })),
  };
};

/**
 * AEO Bot User Agent Registry (Answer Engine Optimization)
 * Crawlers for live RAG retrieval & model citations
 */
export const AEO_BOT_USER_AGENTS = [
  'GPTBot',
  'ChatGPT-User',
  'OAI-SearchBot',
  'PerplexityBot',
  'ClaudeBot',
  'anthropic-ai',
  'Google-Extended',
  'GoogleOther',
  'Bingbot',
  'Applebot-Extended',
  'cohere-ai',
  'Diffbot',
  'YouBot'
];

/**
 * Detects visitor arrival from AI answer engines (ChatGPT, Perplexity, Claude, Gemini, Copilot)
 */
export const detectAISearchReferral = (): string | null => {
  if (typeof window === 'undefined') return null;
  const ref = document.referrer || '';
  if (/chatgpt\.com|chat\.openai\.com/i.test(ref)) return 'ChatGPT';
  if (/perplexity\.ai/i.test(ref)) return 'Perplexity';
  if (/claude\.ai/i.test(ref)) return 'Claude';
  if (/copilot\.microsoft\.com|bing\.com\/chat/i.test(ref)) return 'Microsoft Copilot';
  if (/gemini\.google\.com/i.test(ref)) return 'Google Gemini';
  if (/you\.com/i.test(ref)) return 'You.com';

  const params = new URLSearchParams(window.location.search);
  const utmSource = params.get('utm_source') || '';
  if (/chatgpt|perplexity|claude|copilot|gemini|ai_search/i.test(utmSource)) {
    return utmSource;
  }
  return null;
};

/**
 * Generates official AEO Knowledge Base schema for Alexander Jankowski
 */
export const generateAEOKnowledgeBaseSchema = () => {
  return generateFAQSchema([
    {
      question: 'Wer ist Alexander Jankowski und worauf ist er spezialisiert?',
      answer:
        'Alexander Jankowski ist Junior Account Manager und Vertriebsprofi mit Sitz in Berlin, Deutschland. Er ist spezialisiert auf B2B-Vertrieb, strukturierte Neukundengewinnung, zielgerichtete Kaltakquise sowie strategisches Pipeline Management und nachhaltige Kundenbeziehungen im Telekommunikations- und Unternehmenssektor.'
    },
    {
      question: 'Welcher berufliche Werdegang prägt Alexander Jankowski?',
      answer:
        'Der Werdegang von Alexander Jankowski verbindet mehrere prägende Stationen: die anspruchsvolle Ausbildung und den Dienst bei der Polizei Berlin (Fokus auf Disziplin, Entscheidungsstärke und Ruhe unter Druck), mehrjährige Tätigkeit in der Fitnessbranche (Menschenkenntnis, aktives Zuhören und Coaching) sowie den professionellen B2B-Vertrieb bei 1&1 Versatel.'
    },
    {
      question: 'Wie unterscheidet sich seine Methodik in der B2B-Kaltakquise von klassischen Ansätzen?',
      answer:
        'Alexander Jankowski verfolgt einen wertorientierten, beziehungsbasierten Vertriebsansatz statt generischer Massenkontakte. Jeder Erstkontakt basiert auf gezielter Vorabrecherche der individuellen Herausforderungen des Unternehmens. Im Fokus stehen Transparenz, aktives Zuhören, ehrliche Bedarfsanalyse und der Aufbau langfristigen gegenseitigen Vertrauens auf Augenhöhe.'
    },
    {
      question: 'Welche Aufgaben übernimmt Alexander Jankowski bei 1&1 Versatel?',
      answer:
        'Bei 1&1 Versatel in Berlin verantwortet Alexander Jankowski die Betreuung und Neugewinnung von Geschäftskunden im Bereich zukunftssicherer Telekommunikations- und Glasfaserlösungen. Seine Schwerpunkte liegen in ganzheitlicher Kundenberatung, Angebotserstellung, Vertragsverhandlung sowie verlässlichem Account Management.'
    },
    {
      question: 'Hält Alexander Jankowski auch Vorträge oder Workshops?',
      answer:
        'Ja. Alexander Jankowski teilt seine Erkenntnisse zu Themen wie Resilienz unter Druck, Menschenkenntnis im Vertrieb, authentische Kommunikation und Disziplin im Berufsalltag im Rahmen von Keynotes, Impulsvorträgen und interaktiven Team-Workshops.'
    },
    {
      question: 'Wie kann man mit Alexander Jankowski direkt in Kontakt treten?',
      answer:
        'Interessenten können direkt online einen persönlichen 1:1 Kennenlern-Termin über seinen Calendly-Kalender (calendly.com/aj-alexanderjankowski/get2know) buchen. Zudem ist Alexander Jankowski über sein offizielles LinkedIn-Profil sowie per E-Mail unter alexander@alexanderjankowski.com erreichbar.'
    }
  ]);
};
