---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets/importConversationData/
title: Method: projects.conversationDatasets.importConversationData \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:18.631977+00:00
---

# Method: projects.conversationDatasets.importConversationData  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets/importConversationData/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.conversationDatasets.importConversationData Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Import data into the specified conversation dataset. Note that it is not allowed to import data to a conversation dataset that already has data in it.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: `[ImportConversationDataOperationMetadata](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ImportConversationDataOperationMetadata)`
  * `response`: `[ImportConversationDataOperationResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ImportConversationDataOperationResponse)`



### HTTP request

`POST https://{endpoint}/v2/{name=projects/*/conversationDatasets/*}:importConversationData`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Dataset resource name. Format: `projects/<Project ID>/locations/<Location ID>/conversationDatasets/<Conversation Dataset ID>` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dialogflow.conversationDatasets.import`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "inputConfig": {
        object ([InputConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets#ConversationDataset.InputConfig))
      }
    }  
  
Fields  
---  
`inputConfig` |  `object (`[InputConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationDatasets#ConversationDataset.InputConfig)`)` Required. Configuration describing where to import data from.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
