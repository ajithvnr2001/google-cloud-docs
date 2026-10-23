---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/upsertExamples/
title: Method: exampleStores.upsertExamples \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:56:30.018112+00:00
---

# Method: exampleStores.upsertExamples  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/upsertExamples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: exampleStores.upsertExamples Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.exampleStores.upsertExamples

Create or update Examples in the Example Store.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{exampleStore}:upsertExamples`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`exampleStore` `string` Required. The name of the ExampleStore resource that examples are added to or updated in. Format: `projects/{project}/locations/{location}/exampleStores/{exampleStore}`

### Request body

The request body contains data with the following structure: | Fields  
  
`examples[]` `object (`[Example](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Example)`)` Required. A list of examples to be created/updated. | `overwrite` `boolean` Optional. A flag indicating whether an example can be overwritten if it already exists. If False (default) and the example already exists, the example will not be updated. This does not affect behavior if the example does not exist already.

### Response body

Response message for `[ExampleStoreService.UpsertExamples](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/upsertExamples#google.cloud.aiplatform.v1beta1.ExampleStoreService.UpsertExamples)`. If successful, the response body contains data with the following structure: | Fields  
  
`results[]` `object (`[UpsertResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/upsertExamples#UpsertResult)`)` A list of results for creating/updating. It's either a successfully created/updated example or a status with an error message. | JSON representation  
---  
      
    
    {
      "results": [
        {
          object ([UpsertResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/upsertExamples#UpsertResult))
        }
      ]
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `exampleStore` resource:

  * `aiplatform.exampleStores.writeExample`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## UpsertResult

The result for creating/updating a single example.

Fields  
  
`result` `Union type`  
  
The outcome of creating/updating a single example. It's either the example that was successfully created/updated or a status with an error message. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`example` `object (`[Example](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Example)`)` The example created/updated successfully. | `status` `object (`[Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` The error message of the example that was not created/updated successfully. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // result
      "example": {
        object ([Example](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Example))
      },
      "status": {
        object ([Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Status))
      }
      // Union type
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
