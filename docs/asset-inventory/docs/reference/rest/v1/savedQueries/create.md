---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/create/
title: Method: savedQueries.create \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:05.470981+00:00
---

# Method: savedQueries.create  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: savedQueries.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates a saved query in a parent project/folder/organization.

### HTTP request

`POST https://cloudasset.googleapis.com/v1/{parent=*/*}/savedQueries`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the project/folder/organization where this savedQuery should be created in. It can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345").  
  
### Query parameters

Parameters  
---  
`savedQueryId` |  `string` Required. The ID to use for the saved query, which must be unique in the specified parent. It will become the final component of the saved query's resource name.This value should be 4-63 characters, and valid characters are `[a-z][0-9]-`.Notice that this field is required in the saved query creation, and the `name` field of the `savedQuery` will be ignored.  
  
### Request body

The request body contains an instance of `[SavedQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#SavedQuery)`.

### Response body

If successful, the response body contains a newly created instance of `[SavedQuery](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/savedQueries#SavedQuery)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
