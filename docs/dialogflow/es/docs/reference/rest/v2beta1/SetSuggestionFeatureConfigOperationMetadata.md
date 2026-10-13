---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SetSuggestionFeatureConfigOperationMetadata/
title: SetSuggestionFeatureConfigOperationMetadata \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:17.686439+00:00
---

# SetSuggestionFeatureConfigOperationMetadata  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/SetSuggestionFeatureConfigOperationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  SetSuggestionFeatureConfigOperationMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Metadata for a [ConversationProfile.SetSuggestionFeatureConfig][] operation.

JSON representation  
---  
      
    
    {
      "conversationProfile": string,
      "participantRole": enum ([Role](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants#Participant.Role)),
      "suggestionFeatureType": enum ([Type](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles#ConversationProfile.Type)),
      "createTime": string
    }  
  
Fields  
---  
`conversationProfile` |  `string` The resource name of the conversation profile. Format: `projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>`  
`participantRole` |  `enum (`[Role](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants#Participant.Role)`)` Required. The participant role to add or update the suggestion feature config. Only HUMAN_AGENT or END_USER can be used.  
`suggestionFeatureType` |  `enum (`[Type](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles#ConversationProfile.Type)`)` Required. The type of the suggestion feature to add or update.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp whe the request was created. The time is measured on server side.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-21 UTC."],[],[]] 
