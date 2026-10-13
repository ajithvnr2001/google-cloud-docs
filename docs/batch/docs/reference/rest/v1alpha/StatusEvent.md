---
url: https://docs.cloud.google.com/batch/docs/reference/rest/v1alpha/StatusEvent/
title: StatusEvent \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:14:07.252710+00:00
---

# StatusEvent  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/reference/rest/v1alpha/StatusEvent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Reference ](https://docs.cloud.google.com/batch/docs/apis)



Send feedback 

#  StatusEvent Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TaskExecution
    * JSON representation



Status event.

JSON representation  
---  
      
    
    {
      "type": string,
      "description": string,
      "eventTime": string,
      "taskExecution": {
        object ([TaskExecution](https://docs.cloud.google.com/batch/docs/reference/rest/v1alpha/StatusEvent#TaskExecution))
      },
      "taskState": enum ([State](https://docs.cloud.google.com/batch/docs/reference/rest/v1alpha/State))
    }  
  
Fields  
---  
`type` |  `string` Type of the event.  
`description` |  `string` Description of the event.  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time this event occurred.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`taskExecution` |  `object (`[TaskExecution](https://docs.cloud.google.com/batch/docs/reference/rest/v1alpha/StatusEvent#TaskExecution)`)` Task Execution. This field is only defined for task-level status events where the task fails.  
`taskState` |  `enum (`[State](https://docs.cloud.google.com/batch/docs/reference/rest/v1alpha/State)`)` Task State. This field is only defined for task-level status events.  
  
## TaskExecution

This Task Execution field includes detail information for task execution procedures, based on StatusEvent types.

JSON representation  
---  
      
    
    {
      "exitCode": integer,
      "stderrSnippet": string
    }  
  
Fields  
---  
`exitCode` |  `integer` The exit code of a finished task.If the task succeeded, the exit code will be 0. If the task failed but not due to the following reasons, the exit code will be 50000.Otherwise, it can be from different sources: * Batch known failures: <https://cloud.google.com/batch/docs/troubleshooting#reserved-exit-codes>. * Batch runnable execution failures; you can rely on Batch logs to further diagnose: <https://cloud.google.com/batch/docs/analyze-job-using-logs>. If there are multiple runnables failures, Batch only exposes the first error.  
`stderrSnippet` |  `string` Optional. The tail end of any content written to standard error by the task execution. This field will be populated only when the execution failed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
