---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.conversations/list/
title: Method: projects.locations.dataStores.conversations.list \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:34.225478+00:00
---

# Method: projects.locations.dataStores.conversations.list  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.conversations/list/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  Method: projects.locations.dataStores.conversations.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Lists all Conversations by their parent `[DataStore](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.collections.dataStores#DataStore)`.

### HTTP request

Choose an endpoint:

globalus

  
`GET https://discoveryengine.googleapis.com/v1beta/{parent=projects/*/locations/*/dataStores/*}/conversations`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The data store resource name. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStoreId}`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Maximum number of results to return. If unspecified, defaults to 50. Max allowed value is 1000.  
`pageToken` |  `string` A page token, received from a previous `conversations.list` call. Provide this to retrieve the subsequent page.  
`filter` |  `string` A filter to apply on the list results. The supported features are: userPseudoId, state.Example: "userPseudoId = some_id"  
`orderBy` |  `string` A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: * `updateTime` * `createTime` * `conversation_name`Example: "updateTime desc" "createTime"  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListConversationsResponse](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/ListConversationsResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `discoveryengine.conversations.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
