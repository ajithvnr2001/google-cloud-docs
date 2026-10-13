---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/patch/
title: Method: projects.agent.intents.patch \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:10.572190+00:00
---

# Method: projects.agent.intents.patch  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.agent.intents.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Updates the specified intent.

Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).

### HTTP request

`PATCH https://{endpoint}/v2/{intent.name=projects/*/agent/intents/*}`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`intent.name` |  `string` Optional. The unique identifier of this intent. Required for `[Intents.UpdateIntent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/patch#google.cloud.dialogflow.v2.Intents.UpdateIntent)` and `[Intents.BatchUpdateIntents](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents/batchUpdate#google.cloud.dialogflow.v2.Intents.BatchUpdateIntents)` methods. Format: `projects/<Project ID>/agent/intents/<Intent ID>`.  
  
### Query parameters

Parameters  
---  
`languageCode` |  `string` Optional. The language used to access language-specific data. If not specified, the agent's default language is used. For more information, see [Multilingual intent and entity data](https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity).  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. The mask to control which fields get updated.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`intentView` |  `enum (`[IntentView](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/IntentView)`)` Optional. The resource view to apply to the returned intent.  
  
### Request body

The request body contains an instance of `[Intent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent)`.

### Response body

If successful, the response body contains an instance of `[Intent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.intents#Intent)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
