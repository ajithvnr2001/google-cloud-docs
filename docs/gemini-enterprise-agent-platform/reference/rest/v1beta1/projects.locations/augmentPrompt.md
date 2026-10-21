---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/augmentPrompt/
title: Method: locations.augmentPrompt \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:52:44.699386+00:00
---

# Method: locations.augmentPrompt  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/augmentPrompt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: locations.augmentPrompt Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.augmentPrompt

Given an input prompt, it returns augmented prompt from vertex rag store to guide LLM towards generating grounded responses.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{parent}:augmentPrompt`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the Location from which to augment prompt. The users must have permission to make a call in the project. Format: `projects/{project}/locations/{location}`.

### Request body

The request body contains data with the following structure: | Fields  
  
`contents[]` `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content)`)` Optional. Input content to augment, only text format is supported for now. | `model` `object (`[Model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/augmentPrompt#Model)`)` Optional. metadata of the backend deployed model. | `data_source` `Union type`  
  
The data source for retrieving contexts. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`vertexRagStore` `object (`[VertexRagStore](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiExample#VertexRagStore)`)` Optional. Retrieves contexts from the Vertex RagStore. End of mutually exclusive fields.

### Response body

Response message for locations.augmentPrompt. If successful, the response body contains data with the following structure: | Fields  
  
`augmentedPrompt[]` `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content)`)` Augmented prompt, only text format is supported for now. | `facts[]` `object (`[Fact](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Fact)`)` Retrieved facts from RAG data sources. | JSON representation  
---  
      
    
    {
      "augmentedPrompt": [
        {
          object ([Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content))
        }
      ],
      "facts": [
        {
          object ([Fact](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Fact))
        }
      ]
    }  
  
## Model

metadata of the backend deployed model.

Fields  
  
`model` `string` Optional. The model that the user will send the augmented prompt for content generation. | `modelVersion` `string` Optional. The model version of the backend deployed model. | JSON representation  
---  
      
    
    {
      "model": string,
      "modelVersion": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
