---
url: https://docs.cloud.google.com/translate/markup/
title: Translation API Markup \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:53.856667+00:00
---

# Translation API Markup  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/markup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback 

#  Translation API Markup Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Translation API is available to anyone wishing to integrate with the Cloud Translation API from their own site or application. Use of these APIs is governed by the [Terms of Service](https://cloud.google.com/terms). Among other things, these Terms require that you adhere to certain guidelines on how the resulting text must be displayed on your site. This document and [Attribution Requirements](https://docs.cloud.google.com/translate/attribution) are intended to help you meet these requirements.

If unaltered Cloud Translation API results are published and made searchable on the web, you are required to designate the translated text as machine translated content. For example, Google has quality guidelines about [automatically generated content](https://developers.google.com/search/docs/advanced/guidelines/auto-gen-content) and guidance about how to [prevent it from showing up in search results](https://developers.google.com/search/docs/advanced/crawling/control-what-you-share).

## For short snippets or sections within a HTML document

Wrap the translated text in a `<div lang="..."></div>` (for blocks) or `<span lang="..."></span>` (for inline fragments) and set the `lang=""` attribute to the appropriate language code formed as follows:

  * Use the following format to set `lang=""`: <language code of the language to which the text was translated>-x-mtfrom-<language code of original language>
  * For example, for French text that was machine translated from the original English text, the HTML tag should be: `<span lang="fr-x-mtfrom-en">Bonjour</span>` or `<div lang="fr-x-mtfrom-en"> Bonjour </div>`
  * If the source language or target language is unknown, use the “und” language specification to indicate undetermined language. For example, `<span lang="und-x-mtfrom-und"> … </span>` indicates undetermined source or target languages.

  * Alternatively, put a `lang=""` attribute around whatever element already wraps the translated text. For example, if the unaltered Cloud Translation API results are in a `<p>` paragraph, then put the `lang=""` on the `</p>` as in `<p lang="ar-x-mtfrom-jp">` for text translated from Japanese to Arabic).




## For entire documents or web page

For an entire page, when the original document is not available online or the URL of the original document is not yet known, put the lang="" attribute as described in the previous section on the <html> element:
    
    
    <DOCTYPE HTML>
      <html lang="en-x-mtfrom-fr">
        <head>
          <title>The Bee</title>
            ...
    

For the entire page, when the original document is available online, put a <link> element in the <head> of the HTML document, with the rel="" attribute set to "alternate machine-translated-from", the hreflang="" attribute set to the original language code, and href="" is set to the original page, as in:
    
    
    <DOCTYPE HTML>
      <html lang="en-x-mtfrom-fr">
        <head>
          <title>The Bee</title>
          <link rel="alternate machine-translated-from" hreflang="fr"
                href="http://fr.example.com/abeille.html">
        </head>
        <body>
            ...
    

The HTML code above specifies that this page is machine translated from French to English and the original French document is located at the fictitious `http://fr.example.com/abeille.html`.

For more information, language codes are described below:

  * [IANA language subtag registry](http://www.iana.org/assignments/language-subtag-registry)
  * [IETF language tag](http://en.wikipedia.org/wiki/IETF_language_tag)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
