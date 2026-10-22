---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-translation/
title: Learn about translation features \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:37.701979+00:00
---

# Learn about translation features  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-translation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Learn about translation features Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Translation is one of the three Vertex AI pre-trained APIs on Google Distributed Cloud (GDC) air-gapped appliance. With the Vertex AI Translation service, you can translate text written in more than ten languages into English.

Vertex AI Translation offers the following methods available in GDC air-gapped appliance:

Method | Description  
---|---  
[`detectLanguage`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/quickstart-translation#detect-lang) | Get the name of the language you are translating.  
[`getSupportedLanguages`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/quickstart-translation#get-supported-lang) | Return a list of languages supported by the Vertex AI Translation API. For the complete list of the supported languages, see [Supported languages for Vertex AI Translation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vai-translation-langs).  
[`translateText`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/quickstart-translation#translate-text) | Translate input text from one language to another.  
  
Before making translation requests, [set up a translation project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vai-set-up-translation). You can test the Vertex AI Translation API on GDC air-gapped appliance by [translating text](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/quickstart-translation) from one language to another.

## Considerations

When using the Vertex AI Translation API, particularly the `translateText` method, consider the following aspects:

  * The maximum input length of contents for translation is 1024 characters.
  * You can translate up to 61,000 characters per minute, equivalent to 1,024 characters per second.
  * The `translateText` method doesn't support batching.
  * Types of characters and large portions of text affect translation quality. Therefore, if you experience translation issues, follow these steps:

    1. Remove all special and escape characters that might affect the processing of the request.
    2. Reduce the input size by splitting the contents into smaller sentences.
    3. Translate each of the smaller sentences again by sending them in separate requests to the endpoint.



Failure to follow these limiting considerations might result in errors.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
