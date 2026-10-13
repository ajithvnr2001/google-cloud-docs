---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas/list/
title: Method: ragDataSchemas.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:38.664435+00:00
---

# Method: ragDataSchemas.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: ragDataSchemas.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.ragCorpora.ragDataSchemas.list

Lists RagDataSchemas in a Location.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{parent}/ragDataSchemas`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the RagCorpus from which to list the RagDataSchemas. Format: `projects/{project}/locations/{location}/ragCorpora/{ragCorpus}`

### Query parameters

| `pageSize` `integer` Optional. The standard list page size. The maximum value is 100. If not specified, a default value of 100 will be used. | `pageToken` `string` Optional. The standard list page token. Typically obtained via `[ListRagDataSchemasResponse.next_page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas/list#body.ListRagDataSchemasResponse.FIELDS.next_page_token)` of the previous `[VertexRagDataService.ListRagDataSchemas](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas/list#google.cloud.aiplatform.v1beta1.VertexRagDataService.ListRagDataSchemas)` call.

### Request body

The request body must be empty.

### Response body

Response message for `[VertexRagDataService.ListRagDataSchemas](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas/list#google.cloud.aiplatform.v1beta1.VertexRagDataService.ListRagDataSchemas)`. If successful, the response body contains data with the following structure: | Fields  
  
`ragDataSchemas[]` `object (`[RagDataSchema](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas#RagDataSchema)`)` List of RagDataSchemas in the requested page. | `nextPageToken` `string` A token to retrieve the next page of results. Pass to `[ListRagDataSchemasRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas/list#body.QUERY_PARAMETERS.page_token)` to obtain that page. | JSON representation  
---  
      
    
    {
      "ragDataSchemas": [
        {
          object ([RagDataSchema](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragDataSchemas#RagDataSchema))
        }
      ],
      "nextPageToken": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
