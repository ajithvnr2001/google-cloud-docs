---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores/list/
title: Method: projects.locations.collections.dataStores.list \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:02:43.403862+00:00
---

# Method: projects.locations.collections.dataStores.list  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores/list/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  Method: projects.locations.collections.dataStores.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Lists all the `[DataStore](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)`s associated with the project.

### HTTP request

Choose an endpoint:

globalus

  
`GET https://discoveryengine.googleapis.com/v1/{parent=projects/*/locations/*/collections/*}/dataStores`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collectionId}`.If the caller does not have permission to list `[DataStore](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)`s under this location, regardless of whether or not this data store exists, a PERMISSION_DENIED error is returned.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Maximum number of `[DataStore](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)`s to return. If unspecified, defaults to 10. The maximum allowed value is 50. Values above 50 will be coerced to 50.If this field is negative, an INVALID_ARGUMENT is returned.  
`pageToken` |  `string` A page token `[ListDataStoresResponse.next_page_token](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/ListDataStoresResponse#FIELDS.next_page_token)`, received from a previous `[DataStoreService.ListDataStores](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores/list#google.cloud.discoveryengine.v1.DataStoreService.ListDataStores)` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `[DataStoreService.ListDataStores](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores/list#google.cloud.discoveryengine.v1.DataStoreService.ListDataStores)` must match the call that provided the page token. Otherwise, an INVALID_ARGUMENT error is returned.  
`filter` |  `string` Filter by solution type . For example: `filter = 'solutionType:SOLUTION_TYPE_SEARCH'`  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListDataStoresResponse](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/ListDataStoresResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `discoveryengine.dataStores.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
