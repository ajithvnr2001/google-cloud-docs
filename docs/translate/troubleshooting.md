---
url: https://docs.cloud.google.com/translate/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:53.473771+00:00
---

# Troubleshooting  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback 

#  Troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

How do I tell Cloud Translation - Advanced to _not_ translate something?
    

You can use the following HTML tags:

  * `<span translate="no"> </span>`
  * `<span class="notranslate"> </span>`



This functionality requires the source text to be submitted in HTML (`mimeType` must be `text/html`). You can't selectively ignore segments when you send content as `text/plain`.

Why was a `style` attribute added to the translated text with `text-align` and `direction` CSS properties?
    

This occurs when you include HTML with the requested text to be translated, and you are translating from a right-to-left to a left-to-right language, or from a left-to-right to a right-to-left language. The translation includes the HTML `style` attribute with the `text-align` and `direction` CSS properties to ensure that the translated text is oriented in the proper direction. For example, translating `<h2>Sample text</h2>` from English to Hebrew returns the following JSON: 
    
    
    {
      "data": {
        "translations": [
          {
            "translatedText": "\u003ch2 style=\";text-align:right;direction:rtl\"\u003e טקסט לדוגמה (דברים) \u003c/h2\u003e"
          }
        ]
      }
    }

I get an `HTTP 403` error when I call the API.
    

You might have an issue with your billing account (such as an expired credit card), or you might be exceeding your daily billable total or the number of characters per minute quota. You receive the `Daily Limit Exceeded` error if you exceeded the daily limit or the `User Rate Limit Exceeded` error if you exceeded the characters per minute quota.

To view the billing status of your project, see [Verify the billing status of your projects](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled) in the Cloud Billing documentation.

To view or change usage quotas for your project, visit the [Quotas page](https://console.cloud.google.com/iam-admin/quotas?service=translate.googleapis.com) in the Google Cloud console.

I sometimes get `HTTP 500 (Internal Errors)` response from the API
    This could happen if you submit text without the source language specified. If Google cannot determine the source language given the text (usually because the text is too short), we will return a 500. This situation can be fixed by specifying the source language explicitly.
Can I specify multiple target languages in one request?
    You can supply up to ten target languages in a [batch request](https://docs.cloud.google.com/translate/docs/advanced/batch-translation). If you aren't making a batch request, you can only specify a single target language with your request.
Is it possible to get multiple translations of a word?
    No. This feature is only available via the web interface at [translate.google.com](http://translate.google.com)
For native PDF document translations, the output includes translated text overlaid on the source text.
    Cloud Translation isn't removing the underlying text, which results in shadow text. For more information, see [Translate documents](https://docs.cloud.google.com/translate/docs/advanced/translate-documents#overlaid). 
For scanned PDF document translations, translations don't work for pages where the source text isn't oriented horizontally.
    If text isn't horizontal, Cloud Translation cannot correctly parse the text to translate. You can enable automatic rotation so that text is oriented correctly before translation. For more information, see [Translate documents](https://docs.cloud.google.com/translate/docs/advanced/translate-documents#orientation). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
