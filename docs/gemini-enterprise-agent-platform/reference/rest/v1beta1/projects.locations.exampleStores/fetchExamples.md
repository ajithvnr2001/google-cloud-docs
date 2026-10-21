---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/fetchExamples/
title: Method: exampleStores.fetchExamples \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:19:18.452850+00:00
---

# Method: exampleStores.fetchExamples  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/fetchExamples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: exampleStores.fetchExamples Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.exampleStores.fetchExamples

Get Examples from the Example Store.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{exampleStore}:fetchExamples`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`exampleStore` `string` Required. The name of the ExampleStore resource that the examples should be fetched from. Format: `projects/{project}/locations/{location}/exampleStores/{exampleStore}`

### Request body

The request body contains data with the following structure: | Fields  
  
`pageSize` `integer` Optional. The maximum number of examples to return. The service may return fewer than this value. If unspecified, at most 100 examples will be returned. | `pageToken` `string` Optional. The `[nextPageToken](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/fetchExamples#body.FetchExamplesResponse.FIELDS.next_page_token)` value returned from a previous list [ExampleStoreService.FetchExamplesResponse][] call. | `exampleIds[]` `string` Optional. Example IDs to fetch. If both metadata filters and Example IDs are specified, then both id and metadata filtering will be applied. | `metadata_filter` `Union type`  
  
The example type-specific filters to be applied to the fetch operation. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`storedContentsExampleFilter` `object (`[StoredContentsExampleFilter](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/StoredContentsExampleFilter)`)` The metadata filters for StoredContentsExamples. End of mutually exclusive fields.

### Response body

Response message for `[ExampleStoreService.FetchExamples](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/fetchExamples#google.cloud.aiplatform.v1beta1.ExampleStoreService.FetchExamples)`. If successful, the response body contains data with the following structure: | Fields  
  
`examples[]` `object (`[Example](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Example)`)` The examples in the Example Store that satisfy the metadata filters. | `nextPageToken` `string` A token, which can be sent as `[FetchExamplesRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/fetchExamples#body.request_body.FIELDS.page_token)` to retrieve the next page. Absence of this field indicates there are no subsequent pages. | JSON representation  
---  
      
    
    {
      "examples": [
        {
          object ([Example](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Example))
        }
      ],
      "nextPageToken": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
