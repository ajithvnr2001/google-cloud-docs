---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores/list/
title: Method: metadataStores.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:12:01.130863+00:00
---

# Method: metadataStores.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: metadataStores.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.metadataStores.list

Lists MetadataStores for a Location.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{parent}/metadataStores`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The Location whose MetadataStores should be listed. Format: `projects/{project}/locations/{location}`

### Query parameters

| `pageSize` `integer` The maximum number of metadata Stores to return. The service may return fewer. Must be in range 1-100, inclusive. Defaults to 100. | `pageToken` `string` A page token, received from a previous `[MetadataService.ListMetadataStores](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores/list#google.cloud.aiplatform.v1beta1.MetadataService.ListMetadataStores)` call. Provide this to retrieve the subsequent page.When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with INVALID_ARGUMENT error.)

### Request body

The request body must be empty.

### Response body

Response message for `[MetadataService.ListMetadataStores](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores/list#google.cloud.aiplatform.v1beta1.MetadataService.ListMetadataStores)`. If successful, the response body contains data with the following structure: | Fields  
  
`metadataStores[]` `object (`[MetadataStore](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores#MetadataStore)`)` The MetadataStores found for the Location. | `nextPageToken` `string` A token, which can be sent as `[ListMetadataStoresRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores/list#body.QUERY_PARAMETERS.page_token)` to retrieve the next page. If this field is not populated, there are no subsequent pages. | JSON representation  
---  
      
    
    {
      "metadataStores": [
        {
          object ([MetadataStore](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores#MetadataStore))
        }
      ],
      "nextPageToken": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
