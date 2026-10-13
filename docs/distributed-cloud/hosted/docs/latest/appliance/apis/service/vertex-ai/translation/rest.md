---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/
title: Vertex AI Translation API \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:10.721139+00:00
---

# Vertex AI Translation API  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Vertex AI Translation API Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes the Vertex AI Translation API.

## Service: {TRANSLATION_GDC_ENDPOINT}

### Service endpoint

A service endpoint is a base URL that specifies the network address of an API service.

{TRANSLATION_GDC_ENDPOINT} is a service that might have multiple service endpoints. Its service endpoint is `https://{TRANSLATION_GDC_ENDPOINT}`. Replace `TRANSLATION_GDC_ENDPOINT` with the endpoint used to access the Vertex AI Translation API. For more information, see [View service statuses and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-api-status). 

All URIs on this page are relative to the {TRANSLATION_GDC_ENDPOINT} service endpoint.

## REST Resource: [v3.projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/v3/projects)

Methods  
---  
`[detectLanguage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/v3/projects/detectLanguage)` |  `POST /v3/{parent}:detectLanguage`   
Detects the language of text within a request.  
`[getSupportedLanguages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/v3/projects/getSupportedLanguages)` |  `GET /v3/{parent}:getSupportedLanguages`   
Returns a list of supported languages for translation.  
`[translateText](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rest/v3/projects/translateText)` |  `POST /v3/{parent}:translateText`   
Translates input text and returns translated text.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-11 UTC."],[],[]] 
