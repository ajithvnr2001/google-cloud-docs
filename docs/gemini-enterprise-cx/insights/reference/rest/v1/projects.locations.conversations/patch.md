---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/patch/
title: Method: projects.locations.conversations.patch \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:46:07.238763+00:00
---

# Method: projects.locations.conversations.patch  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Method: projects.locations.conversations.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Updates a conversation.

### HTTP request

`PATCH https://{endpoint}/v1/{conversation.name=projects/*/locations/*/conversations/*}`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`conversation.name` |  `string` Immutable. The resource name of the conversation. Format: projects/{project}/locations/{location}/conversations/{conversation}  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` The list of fields to be updated. All possible fields can be updated by passing `*`, or a subset of the following updateable fields can be provided:

  * `agentId`
  * `languageCode`
  * `labels`
  * `metadata`
  * `qualityMetadata`
  * `callMetadata`
  * `startTime`
  * `expireTime` or `ttl`
  * `dataSource.gcs_source.audio_uri` or `dataSource.dialogflow_source.audio_uri`

This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`allowMissing` |  `boolean` Optional. Defaults to false. If set to true, and the conversation is not found, a new conversation will be created. In this situation, `updateMask` is ignored.  
  
### Request body

The request body contains an instance of `[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation)`.

### Response body

If successful, the response body contains an instance of `[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires **one of** the following [IAM](https://cloud.google.com/iam/docs) permissions on the `name` resource, depending on the resource type:

  * `contactcenterinsights.authorizedConversations.update`
  * `contactcenterinsights.conversations.update`
  * `contactcenterinsights.datasetConversations.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
