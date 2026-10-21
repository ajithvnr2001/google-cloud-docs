---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RetrieveMemoriesResponse/
title: RetrieveMemoriesResponse \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:00:49.537282+00:00
---

# RetrieveMemoriesResponse  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RetrieveMemoriesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  RetrieveMemoriesResponse Stay organized with collections  Save and categorize content based on your preferences. 

Response message for `[MemoryBankService.RetrieveMemories](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.memories/retrieve#google.cloud.aiplatform.v1beta1.MemoryBankService.RetrieveMemories)`.

Fields  
  
`retrievedMemories[]` `object (`[RetrievedMemory](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RetrieveMemoriesResponse#RetrievedMemory)`)` The retrieved memories. | `nextPageToken` `string` A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages. This token is not set if similarity search was used for retrieval. | JSON representation  
---  
      
    
    {
      "retrievedMemories": [
        {
          object ([RetrievedMemory](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RetrieveMemoriesResponse#RetrievedMemory))
        }
      ],
      "nextPageToken": string
    }  
  
## RetrievedMemory

A retrieved memory.

Fields  
  
`memory` `object (`[Memory](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.memoryBanks.memories#Memory)`)` The retrieved Memory. | `distance` `number` The distance between the query and the retrieved Memory. Smaller values indicate more similar memories. This is only set if similarity search was used for retrieval. | JSON representation  
---  
      
    
    {
      "memory": {
        object ([Memory](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.memoryBanks.memories#Memory))
      },
      "distance": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
