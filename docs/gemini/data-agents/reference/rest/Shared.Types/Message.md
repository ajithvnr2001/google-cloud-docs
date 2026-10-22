---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/
title: Message \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:04.188483+00:00
---

# Message  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Message/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  Message Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Message is one unit of communication between client and server. It is associated with a context and optionally a task. Since the server is responsible for the context definition, it must always provide a contextId in its messages. The client can optionally provide the contextId if it knows the context to associate the message to. Similarly for taskId, except the server decides if a task is created and whether to include the taskId.

JSON representation  
---  
      
    
    {
      "messageId": string,
      "contextId": string,
      "taskId": string,
      "role": enum ([Role](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Role)),
      "content": [
        {
          object ([Part](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Part))
        }
      ],
      "metadata": {
        object
      },
      "extensions": [
        string
      ]
    }  
  
Fields  
---  
`messageId` |  `string` The unique identifier (e.g. UUID)of the message. This is required and created by the message creator.  
`contextId` |  `string` The context id of the message. This is optional and if set, the message will be associated with the given context.  
`taskId` |  `string` The task id of the message. This is optional and if set, the message will be associated with the given task.  
`role` |  `enum (`[Role](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Role)`)` A role for the message.  
`content[]` |  `object (`[Part](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Part)`)` protolint:disable REPEATED_FIELD_NAMES_PLURALIZED Content is the container of the message content.  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` protolint:enable REPEATED_FIELD_NAMES_PLURALIZED Any optional metadata to provide along with the message.  
`extensions[]` |  `string` The URIs of extensions that are present or contributed to this Message.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
