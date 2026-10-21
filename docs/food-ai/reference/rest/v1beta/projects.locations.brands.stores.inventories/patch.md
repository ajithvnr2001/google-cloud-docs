---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.inventories/patch/
title: Method: projects.locations.brands.stores.inventories.patch \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:50:25.094595+00:00
---

# Method: projects.locations.brands.stores.inventories.patch  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.inventories/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  Method: projects.locations.brands.stores.inventories.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Updates the specified inventory.

### HTTP request

`PATCH https://foodorderingaiagent.googleapis.com/v1beta/{inventory.name=projects/*/locations/*/brands/*/stores/*/inventories/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`inventory.name` |  `string` Identifier. The resource name of the inventory. Format: projects/{project}/locations/{location}/brands/{brand}/stores/{store}/inventories/{inventory}  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. The list of fields to updateThis is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`allowMissing` |  `boolean` Optional. If set to true, and the inventory is not found, a new inventory will be created. In this situation, `updateMask` is ignored.  
  
### Request body

The request body contains an instance of `[Inventory](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.inventories#Inventory)`.

### Response body

If successful, the response body contains an instance of `[Inventory](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.inventories#Inventory)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-09 UTC."],[],[]] 
