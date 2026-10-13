---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/setSuggestionFeatureConfig/
title: Method: projects.conversationProfiles.setSuggestionFeatureConfig \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:22.344292+00:00
---

# Method: projects.conversationProfiles.setSuggestionFeatureConfig  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/setSuggestionFeatureConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.conversationProfiles.setSuggestionFeatureConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Adds or updates a suggestion feature in a conversation profile. If the conversation profile contains the type of suggestion feature for the participant role, it will update it. Otherwise it will insert the suggestion feature.

This method is a [long-running operation](https://cloud.google.com/dialogflow/es/docs/how/long-running-operations). The returned `Operation` type has the following method-specific fields:

  * `metadata`: `[SetSuggestionFeatureConfigOperationMetadata](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/SetSuggestionFeatureConfigOperationMetadata)`
  * `response`: `[ConversationProfile](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile)`



If a long running operation to add or update suggestion feature config for the same conversation profile, participant role and suggestion feature type exists, please cancel the existing long running operation before sending such request, otherwise the request will be rejected.

### HTTP request

`POST https://{endpoint}/v2/{conversationProfile=projects/*/conversationProfiles/*}:setSuggestionFeatureConfig`

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
      "suggestionFeatureConfig": {
        object ([SuggestionFeatureConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SuggestionFeatureConfig))
      }
    }  
  
Fields  
---  
`participantRole` |  `enum (`[Role](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants#Participant.Role)`)` Required. The participant role to add or update the suggestion feature config. Only HUMAN_AGENT or END_USER can be used.  
`suggestionFeatureConfig` |  `object (`[SuggestionFeatureConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SuggestionFeatureConfig)`)` Required. The suggestion feature config to add or update.  
  
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
