---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.conversations/patch/
title: Method: projects.locations.collections.dataStores.conversations.patch \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:28.250806+00:00
---

# Method: projects.locations.collections.dataStores.conversations.patch  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.conversations/patch/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.collections.dataStores.conversations.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Updates a Conversation.

`[Conversation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.conversations#Conversation)` action type cannot be changed. If the `[Conversation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.conversations#Conversation)` to update does not exist, a NOT_FOUND error is returned.

### HTTP request

Choose an endpoint:

globalus

  
`PATCH https://discoveryengine.googleapis.com/v1/{conversation.name=projects/*/locations/*/collections/*/dataStores/*/conversations/*}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`conversation.name` |  `string` Immutable. Fully qualified name `projects/{project}/locations/global/collections/{collection}/dataStore/*/conversations/*` or `projects/{project}/locations/global/collections/{collection}/engines/*/conversations/*`.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Indicates which fields in the provided `[Conversation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.conversations#Conversation)` to update. The following are NOT supported:

  * `[Conversation.name](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.conversations#Conversation.FIELDS.name)`

If not set or empty, all supported fields are updated.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[Conversation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.conversations#Conversation)`.

### Response body

If successful, the response body contains an instance of `[Conversation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.conversations#Conversation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `discoveryengine.conversations.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
