---
url: https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchHypernyms/create/
title: Method: projects.locations.corpora.searchHypernyms.create \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:21:28.009642+00:00
---

# Method: projects.locations.corpora.searchHypernyms.create  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchHypernyms/create/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/vision-ai/docs/reference/rest)



Send feedback 

#  Method: projects.locations.corpora.searchHypernyms.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Creates a SearchHypernym inside a corpus.

### HTTP request

`POST https://visionai.googleapis.com/v1/{parent=projects/*/locations/*/corpora/*}/searchHypernyms`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where this SearchHypernym will be created. projects/{project_number}/locations/{location}/corpora/{corpus}  
  
### Query parameters

Parameters  
---  
`searchHypernymId` |  `string` Optional. The search hypernym id. If omitted, a random UUID will be generated.  
  
### Request body

The request body contains an instance of `[SearchHypernym](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchHypernyms#SearchHypernym)`.

### Response body

If successful, the response body contains a newly created instance of `[SearchHypernym](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchHypernyms#SearchHypernym)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
