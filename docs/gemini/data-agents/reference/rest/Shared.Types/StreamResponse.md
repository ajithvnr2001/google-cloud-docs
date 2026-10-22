---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/StreamResponse/
title: StreamResponse \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:33.013302+00:00
---

# StreamResponse  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/StreamResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  StreamResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TaskStatusUpdateEvent
    * JSON representation
  * TaskArtifactUpdateEvent
    * JSON representation



The stream response for a message. The stream should be one of the following sequences: If the response is a message, the stream should contain one, and only one, message and then close If the response is a task lifecycle, the first response should be a Task object followed by zero or more TaskStatusUpdateEvents and TaskArtifactUpdateEvents. The stream should complete when the Task if in an interrupted or terminal state. A stream that ends before these conditions are met are

JSON representation  
---  
      
    
    {
    
      // Union field payload can be only one of the following:
      "task": {
        object ([Task](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Task))
      },
      "message": {
        object ([Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message))
      },
      "statusUpdate": {
        object ([TaskStatusUpdateEvent](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/StreamResponse#TaskStatusUpdateEvent))
      },
      "artifactUpdate": {
        object ([TaskArtifactUpdateEvent](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/StreamResponse#TaskArtifactUpdateEvent))
      }
      // End of list of possible types for union field payload.
    }  
  
Fields  
---  
Union field `payload`.`payload` can be only one of the following:  
`task` |  `object (`[Task](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Task)`)`  
`message` |  `object (`[Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message)`)`  
`statusUpdate` |  `object (`[TaskStatusUpdateEvent](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/StreamResponse#TaskStatusUpdateEvent)`)`  
`artifactUpdate` |  `object (`[TaskArtifactUpdateEvent](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/StreamResponse#TaskArtifactUpdateEvent)`)`  
  
## TaskStatusUpdateEvent

TaskStatusUpdateEvent is a delta even on a task indicating that a task has changed.

JSON representation  
---  
      
    
    {
      "taskId": string,
      "contextId": string,
      "status": {
        object ([TaskStatus](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/TaskStatus))
      },
      "final": boolean,
      "metadata": {
        object
      }
    }  
  
Fields  
---  
`taskId` |  `string` The id of the task that is changed  
`contextId` |  `string` The id of the context that the task belongs to  
`status` |  `object (`[TaskStatus](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/TaskStatus)`)` The new status of the task.  
`final` |  `boolean` Whether this is the last status update expected for this task.  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional metadata to associate with the task update.  
  
## TaskArtifactUpdateEvent

TaskArtifactUpdateEvent represents a task delta where an artifact has been generated.

JSON representation  
---  
      
    
    {
      "taskId": string,
      "contextId": string,
      "artifact": {
        object ([Artifact](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Artifact))
      },
      "append": boolean,
      "lastChunk": boolean,
      "metadata": {
        object
      }
    }  
  
Fields  
---  
`taskId` |  `string` The id of the task for this artifact  
`contextId` |  `string` The id of the context that this task belongs too  
`artifact` |  `object (`[Artifact](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Artifact)`)` The artifact itself  
`append` |  `boolean` Whether this should be appended to a prior one produced  
`lastChunk` |  `boolean` Whether this represents the last part of an artifact  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional metadata associated with the artifact update.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
