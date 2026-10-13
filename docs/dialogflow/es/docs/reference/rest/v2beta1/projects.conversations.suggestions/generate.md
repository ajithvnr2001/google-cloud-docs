---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.suggestions/generate/
title: Method: projects.conversations.suggestions.generate \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:40.846212+00:00
---

# Method: projects.conversations.suggestions.generate  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.suggestions/generate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.conversations.suggestions.generate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Generates all the suggestions using generators configured in the conversation profile. A generator is used only if its trigger event is matched.

### HTTP request

`POST https://{endpoint}/v2beta1/{conversation=projects/*/conversations/*}/suggestions:generate`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`conversation` |  `string` Required. The conversation for which the suggestions are generated. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.The conversation must be created with a conversation profile which has generators configured in it to be able to get suggestions.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "latestMessage": string,
      "triggerEvents": [
        enum ([TriggerEvent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/TriggerEvent))
      ]
    }  
  
Fields  
---  
`latestMessage` |  `string` Optional. The name of the latest conversation message for which the request is triggered. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>`.  
`triggerEvents[]` |  `enum (`[TriggerEvent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/TriggerEvent)`)` Optional. A list of trigger events. Only generators configured in the conversationProfile whose triggerEvent is listed here will be triggered.  
  
### Response body

If successful, the response body contains an instance of `[GenerateSuggestionsResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/GenerateSuggestionsResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
