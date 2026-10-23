---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/express-mode/api-reference/
title: Gemini Enterprise Agent Platform in express mode REST API reference \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:45:37.935766+00:00
---

# Gemini Enterprise Agent Platform in express mode REST API reference  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/express-mode/api-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Gemini Enterprise Agent Platform in express mode REST API reference Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Gemini Enterprise Agent Platform in express mode lets you try a subset of Agent Platform features by using an express mode API key passed in the `x-goog-api-key` HTTP header (or the `key` query parameter). This document shows the REST resources available for Agent Platform in express mode.

Unlike the standard REST resource endpoints on Google Cloud, endpoints that are available when using Agent Platform in express mode use the global endpoint `aiplatform.googleapis.com` and don't include `projects` or `locations`. In the following REST resource paths, `{model}` uses the resource path format `publishers/google/models/MODEL_ID`:

  * **Standard Agent Platform endpoint format** : `https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/MODEL_ID:generateContent`
  * **Endpoint format for Agent Platform in express mode** : `https://aiplatform.googleapis.com/v1/publishers/google/models/MODEL_ID:generateContent`



## REST Resource: [v1.publishers.models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/express-mode/rest/v1/publishers.models)

Methods  
---  
`[countTokens](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/express-mode/rest/v1/publishers.models/countTokens)` |  `POST /v1/{endpoint}:countTokens`   
Perform a token counting.  
`[generateContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/express-mode/rest/v1/publishers.models/generateContent)` |  `POST /v1/{model}:generateContent`   
Generate content with multimodal inputs.  
`[streamGenerateContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/express-mode/rest/v1/publishers.models/streamGenerateContent)` |  `POST /v1/{model}:streamGenerateContent`   
Generate content with multimodal inputs with streaming support.  
  
## REST Resource: [v1beta1.publishers.models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/express-mode/rest/v1beta1/publishers.models)

Methods  
---  
`[countTokens](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/express-mode/rest/v1beta1/publishers.models/countTokens)` |  `POST /v1beta1/{endpoint}:countTokens`   
Perform a token counting.  
`[generateContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/express-mode/rest/v1beta1/publishers.models/generateContent)` |  `POST /v1beta1/{model}:generateContent`   
Generate content with multimodal inputs.  
`[streamGenerateContent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/express-mode/rest/v1beta1/publishers.models/streamGenerateContent)` |  `POST /v1beta1/{model}:streamGenerateContent`   
Generate content with multimodal inputs with streaming support.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
