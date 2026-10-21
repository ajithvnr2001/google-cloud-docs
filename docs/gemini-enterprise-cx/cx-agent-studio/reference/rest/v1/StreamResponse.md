---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/StreamResponse/
title: StreamResponse \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:41.365507+00:00
---

# StreamResponse  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/StreamResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  StreamResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TaskStatusUpdateEvent
    * JSON representation
  * TaskArtifactUpdateEvent
    * JSON representation



A wrapper object used in streaming operations to encapsulate different types of response data.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "task": {
        object ([Task](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks#Task))
      },
      "message": {
        object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks#Message))
      },
      "statusUpdate": {
        object ([TaskStatusUpdateEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/StreamResponse#TaskStatusUpdateEvent))
      },
      "artifactUpdate": {
        object ([TaskArtifactUpdateEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/StreamResponse#TaskArtifactUpdateEvent))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The payload of the stream response. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`task` |  `object (`[Task](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks#Task)`)` A Task object containing the current state of the task.  
`message` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks#Message)`)` A Message object containing a message from the agent.  
`statusUpdate` |  `object (`[TaskStatusUpdateEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/StreamResponse#TaskStatusUpdateEvent)`)` An event indicating a task status update.  
`artifactUpdate` |  `object (`[TaskArtifactUpdateEvent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/StreamResponse#TaskArtifactUpdateEvent)`)` An event indicating a task artifact update.  
End of mutually exclusive fields.  
  
## TaskStatusUpdateEvent

An event sent by the agent to notify the client of a change in a task's status.

JSON representation  
---  
      
    
    {
      "taskId": string,
      "contextId": string,
      "status": {
        object ([TaskStatus](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks#TaskStatus))
      },
      "metadata": {
        object
      }
    }  
  
Fields  
---  
`taskId` |  `string` Required. The ID of the task that has changed.  
`contextId` |  `string` Required. The ID of the context that the task belongs to.  
`status` |  `object (`[TaskStatus](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks#TaskStatus)`)` Required. The new status of the task.  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Metadata associated with the task update.  
  
## TaskArtifactUpdateEvent

A task delta where an artifact has been generated.

JSON representation  
---  
      
    
    {
      "taskId": string,
      "contextId": string,
      "artifact": {
        object ([Artifact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks#Artifact))
      },
      "append": boolean,
      "lastChunk": boolean,
      "metadata": {
        object
      }
    }  
  
Fields  
---  
`taskId` |  `string` Required. The ID of the task for this artifact.  
`contextId` |  `string` Required. The ID of the context that this task belongs to.  
`artifact` |  `object (`[Artifact](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/tasks#Artifact)`)` Required. The artifact that was generated or updated.  
`append` |  `boolean` If true, the content of this artifact should be appended to a previously sent artifact with the same ID.  
`lastChunk` |  `boolean` If true, this is the final chunk of the artifact.  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Metadata associated with the artifact update.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
