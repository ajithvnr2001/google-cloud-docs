---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ImportIntentsResponse/
title: ImportIntentsResponse \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:33.185820+00:00
---

# ImportIntentsResponse  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ImportIntentsResponse/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  ImportIntentsResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ConflictingResources
    * JSON representation



The response message for `[Intents.ImportIntents](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/import#google.cloud.dialogflow.cx.v3.Intents.ImportIntents)`.

JSON representation  
---  
      
    
    {
      "intents": [
        string
      ],
      "conflictingResources": {
        object ([ConflictingResources](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ImportIntentsResponse#ConflictingResources))
      }
    }  
  
Fields  
---  
`intents[]` |  `string` The unique identifier of the imported intents. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>`.  
`conflictingResources` |  `object (`[ConflictingResources](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ImportIntentsResponse#ConflictingResources)`)` Info which resources have conflicts when [REPORT_CONFLICT][ImportIntentsResponse.REPORT_CONFLICT] mergeOption is set in ImportIntentsRequest.  
  
## ConflictingResources

Conflicting resources detected during the import process. Only filled when [REPORT_CONFLICT][ImportIntentsResponse.REPORT_CONFLICT] is set in the request and there are conflicts in the display names.

JSON representation  
---  
      
    
    {
      "intentDisplayNames": [
        string
      ],
      "entityDisplayNames": [
        string
      ]
    }  
  
Fields  
---  
`intentDisplayNames[]` |  `string` Display names of conflicting intents.  
`entityDisplayNames[]` |  `string` Display names of conflicting entities.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
