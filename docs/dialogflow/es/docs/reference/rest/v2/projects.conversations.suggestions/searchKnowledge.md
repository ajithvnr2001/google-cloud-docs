---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.suggestions/searchKnowledge/
title: Method: projects.conversations.suggestions.searchKnowledge \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:25.524282+00:00
---

# Method: projects.conversations.suggestions.searchKnowledge  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.suggestions/searchKnowledge/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.conversations.suggestions.searchKnowledge Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Get answers for the given query based on knowledge documents.

### HTTP request

`POST https://{endpoint}/v2/{conversation=projects/*/conversations/*}/suggestions:searchKnowledge`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`conversation` |  `string` Optional. The conversation (between human agent and end user) where the search request is triggered. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "parent": string,
      "query": {
        object ([TextInput](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/TextInput))
      },
      "conversationProfile": string,
      "sessionId": string,
      "latestMessage": string,
      "querySource": enum ([QuerySource](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/QuerySource)),
      "endUserMetadata": {
        object
      },
      "searchConfig": {
        object ([SearchConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/SearchConfig))
      },
      "exactSearch": boolean
    }  
  
Fields  
---  
`parent` |  `string` Required. The parent resource contains the conversation profile Format: 'projects/' or `projects/<Project ID>/locations/<Location ID>`.  
`query` |  `object (`[TextInput](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/TextInput)`)` Required. The natural language text query for knowledge search.  
`conversationProfile` |  `string` Required. The conversation profile used to configure the search. Format: `projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>`.  
`sessionId` |  `string` Required. The ID of the search session. The sessionId can be combined with Dialogflow V3 Agent ID retrieved from conversation profile or on its own to identify a search session. The search history of the same session will impact the search result. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length must not exceed 36 characters.  
`latestMessage` |  `string` Optional. The name of the latest conversation message when the request is triggered. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>`.  
`querySource` |  `enum (`[QuerySource](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/QuerySource)`)` Optional. The source of the query in the request.  
`endUserMetadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Information about the end-user to improve the relevance and accuracy of generative answers.This will be interpreted and used by a language model, so, for good results, the data should be self-descriptive, and in a simple structure.Example:
    
    
    {
      "subscription plan": "Business Premium Plus",
      "devices owned": [
        {"model": "Google Pixel 7"},
        {"model": "Google Pixel Tablet"}
      ]
    }
      
  
`searchConfig` |  `object (`[SearchConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/SearchConfig)`)` Optional. Configuration specific to search queries with data stores.  
`exactSearch` |  `boolean` Optional. Whether to search the query exactly without query rewrite.  
  
### Response body

If successful, the response body contains an instance of `[SearchKnowledgeResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/SearchKnowledgeResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
