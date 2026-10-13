---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ListSessionEntityTypesResponse/
title: ListSessionEntityTypesResponse \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:34.490293+00:00
---

# ListSessionEntityTypesResponse  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ListSessionEntityTypesResponse/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  ListSessionEntityTypesResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The response message for `[SessionEntityTypes.ListSessionEntityTypes](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions.entityTypes/list#google.cloud.dialogflow.cx.v3.SessionEntityTypes.ListSessionEntityTypes)`.

JSON representation  
---  
      
    
    {
      "sessionEntityTypes": [
        {
          object ([SessionEntityType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions.entityTypes#SessionEntityType))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`sessionEntityTypes[]` |  `object (`[SessionEntityType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions.entityTypes#SessionEntityType)`)` The list of session entity types. There will be a maximum number of items returned based on the pageSize field in the request.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
