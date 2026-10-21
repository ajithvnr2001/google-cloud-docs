---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-translation/
title: Learn about translation features \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:02.890909+00:00
---

# Learn about translation features  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-translation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Learn about translation features Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Translation is one of the three Vertex AI pre-trained APIs on Google Distributed Cloud (GDC) air-gapped. With the Vertex AI Translation service, any-to-any text translation is available for 105 languages.

Vertex AI Translation offers the following methods available in Distributed Cloud:

Method | Description  
---|---  
[`batchTranslateDocument`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-translate-docs#translate-in-batch) | Translate a large volume of document in asynchronous batch mode.  
[`detectLanguage`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-translation#detect-lang) | Get the name of the language you are translating.  
[`getOperation`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-translation#get-op) | Get the status of Vertex AI Translation operations.  
[`getSupportedLanguages`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-translation#get-supported-lang) | Return a list of languages supported by the Vertex AI Translation API. For the complete list of the supported languages, see [Supported languages for Vertex AI Translation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-translation-langs).  
[`listOperations`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-translation#list-op) | Obtain a list of operations that match a filter.  
[`translateDocument`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-translate-docs) | Translate documents in synchronous mode.  
[`translateText`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-translation#translate-text) | Translate input text from one language to another.  
  
To optionally define terms to translate, see [Create and use a glossary](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-glossary).

Before making translation requests, [set up a translation project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vai-set-up-translation). You can test the Vertex AI Translation API on Distributed Cloud by [translating text](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-translation) from one language to another.

## Considerations

When using the Vertex AI Translation API, particularly the `translateText` method, consider the following aspects:

  * The maximum input length of contents for translation is 1024 characters.
  * The `translateText` method doesn't support batching.
  * Types of characters and large portions of text affect translation quality. Therefore, if you experience translation issues, follow these steps:

    1. Remove all special and escape characters that might affect the processing of the request.
    2. Reduce the input size by splitting the contents into smaller sentences.
    3. Translate each of the smaller sentences again by sending them in separate requests to the endpoint.



For more information, see [`translateText`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects/translateText).

**Important:** Failure to follow these limiting considerations might result in error [`AITR2130 - TranslationServiceInternal`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-troubleshooting/vertex-ai-translation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
