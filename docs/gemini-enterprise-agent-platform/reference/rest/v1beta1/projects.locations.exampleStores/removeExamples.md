---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/removeExamples/
title: Method: exampleStores.removeExamples \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:59:44.417721+00:00
---

# Method: exampleStores.removeExamples  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/removeExamples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: exampleStores.removeExamples Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.exampleStores.removeExamples

Remove Examples from the Example Store.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{exampleStore}:removeExamples`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`exampleStore` `string` Required. The name of the ExampleStore resource that the examples should be removed from. Format: `projects/{project}/locations/{location}/exampleStores/{exampleStore}`

### Request body

The request body contains data with the following structure: | Fields  
  
`exampleIds[]` `string` Optional. Example IDs to remove. If both metadata filters and Example IDs are specified, the metadata filters will be applied to the specified examples in order to identify which should be removed. | `metadata_filter` `Union type`  
  
The metadata filters that will be used to select which examples should be removed. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`storedContentsExampleFilter` `object (`[StoredContentsExampleFilter](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/StoredContentsExampleFilter)`)` The metadata filters for StoredContentsExamples. End of mutually exclusive fields.

### Response body

Response message for `[ExampleStoreService.RemoveExamples](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/removeExamples#google.cloud.aiplatform.v1beta1.ExampleStoreService.RemoveExamples)`. If successful, the response body contains data with the following structure: | Fields  
  
`exampleIds[]` `string` The IDs for the removed examples. | JSON representation  
---  
      
    
    {
      "exampleIds": [
        string
      ]
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `exampleStore` resource:

  * `aiplatform.exampleStores.writeExample`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
