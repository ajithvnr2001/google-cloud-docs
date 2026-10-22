---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/TaskStatus/
title: TaskStatus \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:02.773283+00:00
---

# TaskStatus  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/TaskStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  TaskStatus Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



A container for the status of a task

JSON representation  
---  
      
    
    {
      "state": enum ([TaskState](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/TaskState)),
      "message": {
        object ([Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message))
      },
      "timestamp": string
    }  
  
Fields  
---  
`state` |  `enum (`[TaskState](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/TaskState)`)` The current state of this task  
`message` |  `object (`[Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message)`)` A message associated with the status.  
`timestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the status was recorded. Example: "2023-10-27T10:00:00Z"Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
