---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ListConversationProfilesResponse/
title: ListConversationProfilesResponse \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:30:32.914194+00:00
---

# ListConversationProfilesResponse  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ListConversationProfilesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  ListConversationProfilesResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The response message for `[ConversationProfiles.ListConversationProfiles](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/list#google.cloud.dialogflow.v2.ConversationProfiles.ListConversationProfiles)`.

JSON representation  
---  
      
    
    {
      "conversationProfiles": [
        {
          object ([ConversationProfile](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`conversationProfiles[]` |  `object (`[ConversationProfile](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile)`)` The list of project conversation profiles. There is a maximum number of items returned based on the pageSize field in the request.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
