---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/TaskStatus/
title: TaskStatus \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:16:18.114985+00:00
---

# TaskStatus  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/TaskStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  TaskStatus Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TaskState



A container for the status of a task

JSON representation  
---  
      
    
    {
      "state": enum ([TaskState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/TaskStatus#TaskState)),
      "message": {
        object (Message)
      },
      "timestamp": string
    }  
  
Fields  
---  
`state` |  `enum (`[TaskState](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/TaskStatus#TaskState)`)` Required. The current state of this task.  
`message` |  `object (`Message`)` A message associated with the status.  
`timestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` ISO 8601 Timestamp when the status was recorded. Example: "2023-10-27T10:00:00Z"Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## TaskState

Defines the possible lifecycle states of a `Task`.

Enums  
---  
`TASK_STATE_UNSPECIFIED` | The task is in an unknown or indeterminate state.  
`TASK_STATE_SUBMITTED` | Indicates that a task has been successfully submitted and acknowledged.  
`TASK_STATE_WORKING` | Indicates that a task is actively being processed by the agent.  
`TASK_STATE_COMPLETED` | Indicates that a task has finished successfully. This is a terminal state.  
`TASK_STATE_FAILED` | Indicates that a task has finished with an error. This is a terminal state.  
`TASK_STATE_CANCELED` | Indicates that a task was canceled before completion. This is a terminal state.  
`TASK_STATE_INPUT_REQUIRED` | Indicates that the agent requires additional user input to proceed. This is an interrupted state.  
`TASK_STATE_REJECTED` | Indicates that the agent has decided to not perform the task. This may be done during initial task creation or later once an agent has determined it can't or won't proceed. This is a terminal state.  
`TASK_STATE_AUTH_REQUIRED` | Indicates that authentication is required to proceed. This is an interrupted state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
