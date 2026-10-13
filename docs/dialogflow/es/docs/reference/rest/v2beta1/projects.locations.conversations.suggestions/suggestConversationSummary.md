---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.conversations.suggestions/suggestConversationSummary/
title: Method: projects.locations.conversations.suggestions.suggestConversationSummary \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:05.221757+00:00
---

# Method: projects.locations.conversations.suggestions.suggestConversationSummary  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.conversations.suggestions/suggestConversationSummary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.locations.conversations.suggestions.suggestConversationSummary Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Suggest summary for a conversation based on specific historical messages. The range of the messages to be used for summary can be specified in the request.

### HTTP request

`POST https://{endpoint}/v2beta1/{conversation=projects/*/locations/*/conversations/*}/suggestions:suggestConversationSummary`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`conversation` |  `string` Required. The conversation to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "latestMessage": string,
      "contextSize": integer,
      "assistQueryParams": {
        object ([AssistQueryParameters](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/AssistQueryParameters))
      }
    }  
  
Fields  
---  
`latestMessage` |  `string` Optional. The name of the latest conversation message used as context for compiling suggestion. If empty, the latest message of the conversation will be used.Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>`.  
`contextSize` |  `integer` Optional. Max number of messages prior to and including [latestMessage] to use as context when compiling the suggestion. By default 500 and at most 1000.  
`assistQueryParams` |  `object (`[AssistQueryParameters](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/AssistQueryParameters)`)` Optional. Parameters for a human assist query. Only used for POC/demo purpose.  
  
### Response body

If successful, the response body contains an instance of `[SuggestConversationSummaryResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SuggestConversationSummaryResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
