---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/a2a.projects.locations.dataAgents.v1.message/stream/
title: Method: a2a.projects.locations.dataAgents.v1.message.stream \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:01.954587+00:00
---

# Method: a2a.projects.locations.dataAgents.v1.message.stream  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/a2a.projects.locations.dataAgents.v1.message/stream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  Method: a2a.projects.locations.dataAgents.v1.message.stream Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes



message.stream is a streaming call that will return a stream of task update events until the Task is in an interrupted or terminal state.

### HTTP request

`POST https://geminidataanalytics.googleapis.com/v1/a2a/{tenant=projects/*/locations/*/dataAgents/*}/v1/message:stream`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`tenant` |  `string` Optional tenant, provided as a path parameter. Experimental, might still change for 1.0 release.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "message": {
        object ([Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message))
      },
      "configuration": {
        object ([SendMessageConfiguration](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration))
      },
      "metadata": {
        object
      }
    }  
  
Fields  
---  
`message` |  `object (`[Message](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message)`)` Required. The message to send to the agent.  
`configuration` |  `object (`[SendMessageConfiguration](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/SendMessageConfiguration)`)` Configuration for the send request.  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional metadata for the request.  
  
### Response body

If successful, the response body contains a stream of `[StreamResponse](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/StreamResponse)` instances.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
