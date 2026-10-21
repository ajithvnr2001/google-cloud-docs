---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/
title: SendMessageConfiguration \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:43:07.206326+00:00
---

# SendMessageConfiguration  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  SendMessageConfiguration Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Configuration of a send message request.

JSON representation  
---  
      
    
    {
      "acceptedOutputModes": [
        string
      ],
      "pushNotification": {
        object ([PushNotificationConfig](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/PushNotificationConfig))
      },
      "historyLength": integer,
      "blocking": boolean
    }  
  
Fields  
---  
`acceptedOutputModes[]` |  `string` The output modes that the agent is expected to respond with.  
`pushNotification` |  `object (`[PushNotificationConfig](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/PushNotificationConfig)`)` A configuration of a webhook that can be used to receive updates  
`historyLength` |  `integer` The maximum number of messages to include in the history. if 0, the history will be unlimited.  
`blocking` |  `boolean` If true, the message will be blocking until the task is completed. If false, the message will be non-blocking and the task will be returned immediately. It is the caller's responsibility to check for any task updates.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
