---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/askContexts/
title: Method: locations.askContexts \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:42:57.354552+00:00
---

# Method: locations.askContexts  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/askContexts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: locations.askContexts Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.askContexts

Agentic Retrieval Ask API for RAG.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{parent}:askContexts`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the Location from which to retrieve RagContexts. The users must have permission to make a call in the project. Format: `projects/{project}/locations/{location}`.

### Request body

The request body contains data with the following structure: | Fields  
  
`query` `object (`[RagQuery](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagQuery)`)` Required. Single RAG retrieve query. | `tools[]` `object (`[Tool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiExample#Tool)`)` Optional. The tools to use for locations.askContexts.

### Response body

Response message for `[VertexRagService.AskContexts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/askContexts#google.cloud.aiplatform.v1beta1.VertexRagService.AskContexts)`. If successful, the response body contains data with the following structure: | Fields  
  
`response` `string` The Retrieval Response. | `contexts` `object (`[RagContexts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagContexts)`)` The contexts of the query. | JSON representation  
---  
      
    
    {
      "response": string,
      "contexts": {
        object ([RagContexts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagContexts))
      }
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
