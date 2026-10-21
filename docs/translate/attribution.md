---
url: https://docs.cloud.google.com/translate/attribution/
title: Attribution Requirements \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:13.957062+00:00
---

# Attribution Requirements  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/attribution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback 

#  Attribution Requirements Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Translation is available to anyone wishing to perform integration between Google Translate and their own site or application.

Use of these APIs is governed by the [Terms of Service](https://cloud.google.com/terms). Among other things, these Terms require that you adhere to certain guidelines on how lay out, Google attribution, and branding must be handled on your site. This document and the [HTML Markup Requirements](https://docs.cloud.google.com/translate/markup) are intended to help you meet these requirements.

These branding guidelines may change from time to time, and without prior notice from Google. Your continued use of the Cloud Translation API is contingent upon your adherence to the current branding guidelines. If you are uncomfortable with any of these branding guidelines, discontinue your use of the API, and [contact us](https://cloud.google.com/contact) with your concerns.

## Overview

The purpose of Cloud Translation is to help make content accessible to users in their own language. Therefore, there are certain attribution and linking requirements. **The following basic principles govern your use of Cloud Translation:**

  * Adherence to these guidelines is required before using the Cloud Translation API from your website or application.
  * Whenever you display translation results from Google Translate directly to users, you **must** make it clear to users that they are viewing automatic translations from Google Translate using the appropriate text or brand elements.
  * Applications using the Cloud Translation API must state in the application description and help documentation that Google Translate is used to power translation within the application and provide links to the Cloud Translation site.
  * If unaltered translation results are displayed on web pages that can be indexed by search engines, you are required to designate the translated text as machine translated content using the [HTML markup reference](https://docs.cloud.google.com/translate/markup).



## Naming

To help us ensure a consistent end user experience and accurate expectation of Google Translate features, you must abide by certain naming conventions.

When creating a product utilizing the Cloud Translation API, the name of the product cannot use Google, Google Translate, or other Google Brand Features in the name of the software. If, for marketing or other strategic reasons, it would be valuable to reference Google Translate, it may be permissible for the developer to use, for example, the phrase "Acme Plugin for Google Translate." This should be the exception, and not the rule. However, never use, for example, "Google Translate AcmeOPAC Plugin." You may not state or otherwise imply any affiliation with Google or Google Translate.

It may occasionally be necessary to refer to Google Translate or features provided through the API (e.g., in documentation, headers, buttons). When doing so, you must only use approved terminology:

  * **Google Translate service** : Use only the term "Google Translate" to refer to the service made available through these APIs and at URLs such as <http://translate.google.com>. Do not modify this word mark, for example, through hyphenation, combination abbreviation, or acronym such as: Google-Translate, GT, GoogTrans, GTrans, etc.
  * **Cloud Translation API** : Use only the term "Cloud Translation API" to refer to the set of developer-facing features described within the [Cloud Translation API Documentation](https://docs.cloud.google.com/translate/docs). Refer to specific APIs and tools using the terminology from this site.



If you wish to refer to Cloud Translation features in a language other than English, you must do so using the same terminology as the [Google Translate Site](http://translate.google.com), which is available in over 50 languages.

For more questions about other uses of Google Brand Features, see <http://www.google.com/permissions/guidelines.html>

## Attribution and logos

In addition to following Google's general [Brand Features guidelines](http://www.google.com/permissions/guidelines.html), you are also required to adopt certain branding elements when using the Cloud Translation API. These forms of attribution are used in order to maintain consistency and preserve the Google brand identity.

The following basic principles govern use of the Google name and logo in conjunction with the Cloud Translation API:

  * **Google attribution is required.**
  * The Google name and logo should be associated with Google Translate only.
  * The Google logo may never appear next to or on the same page with the logos of competing web or other search services. There are no exceptions to this rule.
  * The "powered by Google Translate" graphic must always be displayed adjacent any translation results.
  * You shall display all intellectual property rights legends and notices (e.g., copyright notices) as instructed by Google.



### Translation results

Your application may display, in response to a user's action, translation results obtained from the Cloud Translation API. Whenever you display such information, you must include attribution to Google using one of the badges below. Attribution badges on web pages must link to <http://translate.google.com>. You can [download a zip file of the badges here](https://docs.cloud.google.com/static/translate/images/google-translate-attribution.zip).

The version of the attribution using the full-color Google logo is preferred, but depending on your application or website's layout and color-scheme, you must use one of these visual attribution styles:

  
![text attribution](https://docs.cloud.google.com/static/translate/images/text-attribution.png)  


The samples below show attributions within a mobile application:

  
![attribution sample](https://docs.cloud.google.com/static/translate/images/mobile-attribution-sample.png)  


### Translation buttons

#### Mobile apps

The button or user action that triggers a translation should be clearly labeled 'Translate with Google.'

  
![mobile action attribution](https://docs.cloud.google.com/static/translate/images/mobile-action-attribution.png)  


#### Desktop and web

Using the Cloud Translation API, it is possible to issue a call to Google Translate directly from your site. The buttons or links you use in conjunction to these features must include proper attribution to Google.

  
![translation buttons](https://docs.cloud.google.com/static/translate/images/translation-buttons.png)  


## Additional branding requirements

  * You must also adhere to the Google-wide [Guidelines for Third Party Use of Google Brand Features](http://www.google.com/permissions/guidelines.html)
  * Use of the buttons, stickers, and branding elements described in this document is governed by the [Cloud Translation API Terms of Service](https://cloud.google.com/terms)
  * Do not change any of the Google marks in any way. Do not remove, obstruct, distort, or alter any element of a Google Translate trademark. This includes modifying the Google word marks, for example, through hyphenation, combination abbreviation, or acronym such as: Google Translate, GT, GoogTrans, etc.
  * Make sure the button, sticker, or other branding element is full and clearly visible, never altered or partially covered.
  * Do not use the buttons, stickers, or other branding elements in ways that (1) imply an association with or endorsement of any other product, service, event, sponsorship, or organization; (2) can be reasonably interpreted to suggest editorial content was authored by Google; or (3) represent the views or opinions of Google personnel without prior written permission from Google. All of the previously mentioned usages must be approved via written permission.
  * Do not adopt marks, logos, slogans, or designs that are confusingly similar to the Google trademarks or imitate Google's trade dress, including the look and feel of Google Translate web design properties, Google Translate brand packaging, distinctive color combinations, typography, graphic designs, product icons, or imagery associated with Google Translate.
  * Do not register Google trademarks as second-level domain names or incorporate Google trademarks into your own product name, service names, trademarks, logos, or company names.
  * Never display a Google trademark in a manner that is misleading, unfair, defamatory, infringing, libelous, disparaging, obscene, or otherwise objectionable to Google.
  * Never display a Google Translate trademark on any web site or user interface that contains or displays adult content, promotes gambling, promotes violence, contains hate speech, involves the sale of tobacco or alcohol to persons under 21 years of age, violates other applicable laws or regulations or is otherwise objectionable.



## Disclaimer

If you display the results of the Translation API to your end users without modification, you must make the following disclaimer available on your web site or within your app:

> THIS SERVICE MAY CONTAIN TRANSLATIONS POWERED BY GOOGLE. GOOGLE DISCLAIMS ALL WARRANTIES RELATED TO THE TRANSLATIONS, EXPRESS OR IMPLIED, INCLUDING ANY WARRANTIES OF ACCURACY, RELIABILITY, AND ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 

If you are using the Translation API to make the content of a website available in more languages, you might also include an additional disclaimer:

> The <company name> website has been translated for your convenience using translation software powered by Google Translate. Reasonable efforts have been made to provide an accurate translation, however, no automated translation is perfect nor is it intended to replace human translators. Translations are provided as a service to users of the <company name> website, and are provided "as is." No warranty of any kind, either expressed or implied, is made as to the accuracy, reliability, or correctness of any translations made from <source language> into any other language. Some content (such as images, videos, Flash, etc.) may not be accurately translated due to the limitations of the translation software.

> The official text is the <source language> version of the website. Any discrepancies or differences created in the translation are not binding and have no legal effect for compliance or enforcement purposes. If any questions arise related to the accuracy of the information contained in the translated website, refer to the <source language> version of the website which is the official version.

Note that this example is for illustrative purposes only. We encourage you to consult your legal advisor about any additional disclaimers.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
