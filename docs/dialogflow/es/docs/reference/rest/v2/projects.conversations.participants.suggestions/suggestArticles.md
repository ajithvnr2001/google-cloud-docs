---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants.suggestions/suggestArticles/
title: Method: projects.conversations.participants.suggestions.suggestArticles \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:24.763396+00:00
---

# Method: projects.conversations.participants.suggestions.suggestArticles  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants.suggestions/suggestArticles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.conversations.participants.suggestions.suggestArticles Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Gets suggested articles for a participant based on specific historical messages.

### HTTP request

`POST https://{endpoint}/v2/{parent=projects/*/conversations/*/participants/*}/suggestions:suggestArticles`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the participant to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.suggestions.list`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "latestMessage": string,
      "contextSize": integer,
      "assistQueryParams": {
        object ([AssistQueryParameters](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/AssistQueryParameters))
      }
    }  
  
Fields  
---  
`latestMessage` |  `string` Optional. The name of the latest conversation message to compile suggestion for. If empty, it will be the latest message of the conversation.Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>`.  
`contextSize` |  `integer` Optional. Max number of messages prior to and including `[latestMessage](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants.suggestions/suggestArticles#body.request_body.FIELDS.latest_message)` to use as context when compiling the suggestion. By default 20 and at most 50.  
`assistQueryParams` |  `object (`[AssistQueryParameters](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/AssistQueryParameters)`)` Parameters for a human assist query.  
  
### Response body

If successful, the response body contains an instance of `[SuggestArticlesResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/SuggestArticlesResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
