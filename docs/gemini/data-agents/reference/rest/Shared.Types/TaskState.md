---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/TaskState/
title: TaskState \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:17.116222+00:00
---

# TaskState  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/TaskState/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  TaskState Stay organized with collections  Save and categorize content based on your preferences. 

The set of states a Task can be in.

Enums  
---  
`TASK_STATE_UNSPECIFIED` |   
`TASK_STATE_SUBMITTED` | Represents the status that acknowledges a task is created  
`TASK_STATE_WORKING` | Represents the status that a task is actively being processed  
`TASK_STATE_COMPLETED` | Represents the status a task is finished. This is a terminal state  
`TASK_STATE_FAILED` | Represents the status a task is done but failed. This is a terminal state  
`TASK_STATE_CANCELLED` | Represents the status a task was cancelled before it finished. This is a terminal state.  
`TASK_STATE_INPUT_REQUIRED` | Represents the status that the task requires information to complete. This is an interrupted state.  
`TASK_STATE_REJECTED` | Represents the status that the agent has decided to not perform the task. This may be done during initial task creation or later once an agent has determined it can't or won't proceed. This is a terminal state.  
`TASK_STATE_AUTH_REQUIRED` | Represents the state that some authentication is needed from the upstream client. Authentication is expected to come out-of-band thus this is not an interrupted or terminal state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
