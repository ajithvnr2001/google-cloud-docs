---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RagChunk/
title: RagChunk \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:29:02.548048+00:00
---

# RagChunk  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RagChunk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  RagChunk Stay organized with collections  Save and categorize content based on your preferences. 

A RagChunk includes the content of a chunk of a RagFile, and associated metadata.

Fields  
  
`text` `string` The content of the chunk. | `fileId` `string` The id of the file that the chunk belongs to. | `chunkId` `string` The id of the chunk. | `pageSpan` `object (`[PageSpan](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RagChunk#PageSpan)`)` If populated, represents where the chunk starts and ends in the document. | JSON representation  
---  
      
    
    {
      "text": string,
      "fileId": string,
      "chunkId": string,
      "pageSpan": {
        object ([PageSpan](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RagChunk#PageSpan))
      }
    }  
  
## PageSpan

Represents where the chunk starts and ends in the document.

Fields  
  
`firstPage` `integer` Page where chunk starts in the document. Inclusive. 1-indexed. | `lastPage` `integer` Page where chunk ends in the document. Inclusive. 1-indexed. | JSON representation  
---  
      
    
    {
      "firstPage": integer,
      "lastPage": integer
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-02 UTC."],[],[]] 
