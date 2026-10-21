---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.conversations/create/
title: Method: projects.locations.conversations.create \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:42:56.701735+00:00
---

# Method: projects.locations.conversations.create  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.conversations/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  Method: projects.locations.conversations.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Creates a new conversation to persist the conversation history. Each conversation will have multiple messages associated with it.

### HTTP request

`POST https://geminidataanalytics.googleapis.com/v1alpha/{parent=projects/*/locations/*}/conversations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for CreateConversationRequest. Format: `projects/{project}/locations/{location}`  
  
### Query parameters

Parameters  
---  
`conversationId` |  `string` Optional. The conversation id of the conversation to create. Must be unique within the parent. The allowed format is: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`. If not provided, the server will auto-generate a value for the id.  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.  
  
### Request body

The request body contains an instance of `[Conversation](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.conversations#Conversation)`.

### Response body

If successful, the response body contains a newly created instance of `[Conversation](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.conversations#Conversation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
