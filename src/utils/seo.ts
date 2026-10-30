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
