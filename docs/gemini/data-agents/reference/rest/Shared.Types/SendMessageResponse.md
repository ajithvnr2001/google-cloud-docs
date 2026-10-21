---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageResponse/
title: SendMessageResponse \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:43:06.901110+00:00
---

# SendMessageResponse  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  SendMessageResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



////// Response Messages ///////////

JSON representation  
---  
      
    
    {
    
      // Union field payload can be only one of the following:
      "task": {
        object ([Task](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Task))
      },
      "message": {
        object ([Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message))
      }
      // End of list of possible types for union field payload.
    }  
  
Fields  
---  
Union field `payload`.`payload` can be only one of the following:  
`task` |  `object (`[Task](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Task)`)`  
`message` |  `object (`[Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message)`)`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
