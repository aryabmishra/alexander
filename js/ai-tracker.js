/**
 * AI Search & Answer Engine Visibility Tracker (AEO Analytics)
 * Captures referrals and citations from ChatGPT, Perplexity, Claude, Copilot, and Gemini
 * Attribution passed to Calendly and analytics platforms.
 */
(function() {
  'use strict';

  var AI_ENGINES = [
    { name: 'ChatGPT', regex: /chatgpt\.com|chat\.openai\.com/i },
    { name: 'Perplexity', regex: /perplexity\.ai/i },
    { name: 'Claude', regex: /claude\.ai/i },
    { name: 'Microsoft Copilot', regex: /copilot\.microsoft\.com|bing\.com\/chat/i },
    { name: 'Google Gemini', regex: /gemini\.google\.com/i },
    { name: 'You.com', regex: /you\.com/i }
  ];

  function detectAISource() {
    var ref = document.referrer || '';
    for (var i = 0; i < AI_ENGINES.length; i++) {
      if (AI_ENGINES[i].regex.test(ref)) {
        return AI_ENGINES[i].name;
      }
    }
    // Check URL parameters for explicit AI UTM tags
    var params = new URLSearchParams(window.location.search);
    var utmSource = params.get('utm_source') || '';
    var utmMedium = params.get('utm_medium') || '';
    if (/chatgpt|perplexity|claude|copilot|gemini|ai_search|llm/i.test(utmSource + utmMedium)) {
      return utmSource || 'AI Search';
    }
    return null;
  }

  var aiSource = detectAISource();
  if (aiSource) {
    try {
      sessionStorage.setItem('aj_ai_citation_source', aiSource);
      sessionStorage.setItem('aj_ai_citation_landing', window.location.pathname);
      console.log('[AEO Visibility] Visitor arrived from AI Answer Engine:', aiSource);
    } catch(e) {}

    // Enhance Calendly links with AI referral attribution
    document.addEventListener('DOMContentLoaded', function() {
      var calendlyLinks = document.querySelectorAll('a[href*="calendly.com"]');
      calendlyLinks.forEach(function(link) {
        try {
          var url = new URL(link.href);
          url.searchParams.set('utm_source', 'ai_search_' + aiSource.toLowerCase().replace(/[^a-z0-9]/g, ''));
          url.searchParams.set('utm_medium', 'aeo_citation');
          url.searchParams.set('utm_campaign', 'alexanderjankowski_aeo');
          link.href = url.toString();
        } catch(err) {}
      });
    });

    // Dispatch custom event for Google Analytics / Tag Manager
    if (window.dataLayer && Array.isArray(window.dataLayer)) {
      window.dataLayer.push({
        event: 'ai_citation_visit',
        ai_engine: aiSource,
        landing_page: window.location.pathname
      });
    }
  }
})();
