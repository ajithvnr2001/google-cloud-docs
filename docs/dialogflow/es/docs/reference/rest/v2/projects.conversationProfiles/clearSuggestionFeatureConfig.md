---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/clearSuggestionFeatureConfig/
title: Method: projects.conversationProfiles.clearSuggestionFeatureConfig \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:21.210929+00:00
---

# Method: projects.conversationProfiles.clearSuggestionFeatureConfig  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/clearSuggestionFeatureConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.conversationProfiles.clearSuggestionFeatureConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Clears a suggestion feature from a conversation profile for the given participant role.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: `[ClearSuggestionFeatureConfigOperationMetadata](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ClearSuggestionFeatureConfigOperationMetadata)`
  * `response`: `[ConversationProfile](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile)`



### HTTP request

`POST https://{endpoint}/v2/{conversationProfile=projects/*/conversationProfiles/*}:clearSuggestionFeatureConfig`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`conversationProfile` |  `string` Required. The Conversation Profile to add or update the suggestion feature config. Format: `projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "participantRole": enum ([Role](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants#Participant.Role)),
      "suggestionFeatureType": enum ([Type](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.Type))
    }  
  
Fields  
---  
`participantRole` |  `enum (`[Role](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants#Participant.Role)`)` Required. The participant role to remove the suggestion feature config. Only HUMAN_AGENT or END_USER can be used.  
`suggestionFeatureType` |  `enum (`[Type](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.Type)`)` Required. The type of the suggestion feature to remove.  
  
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
