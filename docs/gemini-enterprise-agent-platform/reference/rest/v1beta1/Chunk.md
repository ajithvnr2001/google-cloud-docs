---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Chunk/
title: Chunk \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:28:41.349217+00:00
---

# Chunk  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Chunk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Chunk Stay organized with collections  Save and categorize content based on your preferences. 

Container for bytes-encoded data such as video frame, audio sample, or a complete binary/text data.

Fields  
  
`mimeType` `string` Required. Mime type of the chunk data. See <https://www.iana.org/assignments/media-types/media-types.xhtml> for the full list. | `data` `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The data in the chunk.A base64-encoded string. | `metadata` `object (`[Metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Chunk#Metadata)`)` Optional. metadata that is associated with the data in the payload. | JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string,
      "metadata": {
        object ([Metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Chunk#Metadata))
      }
    }  
  
## Metadata

metadata for a chunk.

Fields  
  
`attributes` `map (key: string, value: string ([bytes](https://developers.google.com/discovery/v1/type-format) format))` Optional. Attributes attached to the data. The keys have semantic conventions and the consumers of the attributes should know how to deserialize the value bytes based on the keys. | JSON representation  
---  
      
    
    {
      "attributes": {
        string: string,
        ...
      }
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
