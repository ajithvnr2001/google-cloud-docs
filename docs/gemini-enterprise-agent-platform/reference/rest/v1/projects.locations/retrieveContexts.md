---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations/retrieveContexts/
title: Method: locations.retrieveContexts \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:59:52.053155+00:00
---

# Method: locations.retrieveContexts  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations/retrieveContexts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: locations.retrieveContexts Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.retrieveContexts

Retrieves relevant contexts for a query.

### Endpoint

post  `https://{service-endpoint}/v1/{parent}:retrieveContexts`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the Location from which to retrieve RagContexts. The users must have permission to make a call in the project. Format: `projects/{project}/locations/{location}`.

### Request body

The request body contains data with the following structure: | Fields  
  
`query` `object (`[RagQuery](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RagQuery)`)` Required. Single RAG retrieve query. | `data_source` `Union type`  
  
Data Source to retrieve contexts. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`vertexRagStore` `object (`[VertexRagStore](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations/retrieveContexts#VertexRagStore)`)` The data source for Vertex RagStore. End of mutually exclusive fields.

### Response body

Response message for `[VertexRagService.RetrieveContexts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations/retrieveContexts#google.cloud.aiplatform.v1.VertexRagService.RetrieveContexts)`. If successful, the response body contains data with the following structure: | Fields  
  
`contexts` `object (`[RagContexts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RagContexts)`)` The contexts of the query. | JSON representation  
---  
      
    
    {
      "contexts": {
        object ([RagContexts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RagContexts))
      }
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.ragCorpora.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## VertexRagStore

The data source for Vertex RagStore.

Fields  
  
`ragResources[]` `object (`[RagResource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations/retrieveContexts#RagResource)`)` Optional. The representation of the rag source. It can be used to specify corpus only or ragfiles. Currently only support one corpus or multiple files from one corpus. In the future we may open up multiple corpora support. | `vectorDistanceThreshold  
**(deprecated)**` `number` This item is deprecated!Optional. Only return contexts with vector distance smaller than the threshold. | JSON representation  
---  
      
    
    {
      "ragResources": [
        {
          object ([RagResource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations/retrieveContexts#RagResource))
        }
      ],
      "vectorDistanceThreshold": number
    }  
  
## RagResource

The definition of the Rag resource.

Fields  
  
`ragCorpus` `string` Optional. RagCorpora resource name. Format: `projects/{project}/locations/{location}/ragCorpora/{ragCorpus}` | `ragFileIds[]` `string` Optional. ragFileId. The files should be in the same ragCorpus set in ragCorpus field. | JSON representation  
---  
      
    
    {
      "ragCorpus": string,
      "ragFileIds": [
        string
      ]
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
