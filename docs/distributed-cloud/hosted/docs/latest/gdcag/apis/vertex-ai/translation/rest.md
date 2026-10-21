---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/
title: Vertex AI Translation API \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:44.912467+00:00
---

# Vertex AI Translation API  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Vertex AI Translation API Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes the Vertex AI Translation API.

## Service: {TRANSLATION_GDC_ENDPOINT}

### Service endpoint

A service endpoint is a base URL that specifies the network address of an API service.

{TRANSLATION_GDC_ENDPOINT} is a service that might have multiple service endpoints. Its service endpoint is `https://{TRANSLATION_GDC_ENDPOINT}`. Replace `TRANSLATION_GDC_ENDPOINT` with the endpoint used to access the Vertex AI Translation API. For more information, see [View service statuses and endpoints](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-api-status). 

All URIs on this page are relative to the {TRANSLATION_GDC_ENDPOINT} service endpoint.

## REST Resource: [v3.projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects)

Methods  
---  
`[batchTranslateDocument](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/batchTranslateDocument)` |  `POST /v3/{parent}:batchTranslateDocument`   
Translates a large volume of document in asynchronous batch mode.  
`[detectLanguage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects/detectLanguage)` |  `POST /v3/{parent}:detectLanguage`   
Detects the language of text within a request.  
`[getSupportedLanguages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects/getSupportedLanguages)` |  `GET /v3/{parent}:getSupportedLanguages`   
Returns a list of supported languages for translation.  
`[translateDocument](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/translateDocument)` |  `POST /v3/{parent}:translateDocument`   
Translates documents in synchronous mode.  
`[translateText](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects/translateText)` |  `POST /v3/{parent}:translateText`   
Translates input text and returns translated text.  
  
## REST Resource: [v3.projects.glossaries](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries)

Methods  
---  
`[create](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries/create)` |  `POST /v3/{parent}/glossaries`   
Creates a glossary and returns the long-running operation.  
`[delete](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries/delete)` |  `DELETE /v3/{name}`   
Deletes a glossary if the glossary hasn't been created.  
`[get](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries/get)` |  `GET /v3/{name}`   
Gets a glossary.  
`[list](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.glossaries/list)` |  `GET /v3/{parent}/glossaries`   
Lists glossaries in a project.  
  
## REST Resource: [v3.projects.operations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.operations/cancel)` |  `POST https://{TRANSLATION_GDC_ENDPOINT}/v3/{name}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.operations/delete)` |  `DELETE https://{TRANSLATION_GDC_ENDPOINT}/v3/{name}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.operations/get)` |  `GET /v3/{name}`   
Gets the state of a long-running operation.  
`[list](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.operations/list)` |  `GET /v3/{name}/operations`  
Lists operations that match the specified filter in the request.  
`[wait](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.operations/wait)` |  `POST https://{TRANSLATION_GDC_ENDPOINT}/v3/{name}:wait`  
Waits until the specified long-running operation is done or reaches at most a specified timeout, returning the latest state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-10 UTC."],[],[]] 
