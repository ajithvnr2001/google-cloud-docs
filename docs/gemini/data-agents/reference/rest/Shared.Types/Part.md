---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Part/
title: Part \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:40.821709+00:00
---

# Part  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Part/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  Part Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * FilePart
    * JSON representation
  * DataPart
    * JSON representation



Part represents a container for a section of communication content. Parts can be purely textual, some sort of file (image, video, etc) or a structured data blob (i.e. JSON).

JSON representation  
---  
      
    
    {
      "metadata": {
        object
      },
    
      // Union field part can be only one of the following:
      "text": string,
      "file": {
        object ([FilePart](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Part#FilePart))
      },
      "data": {
        object ([DataPart](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Part#DataPart))
      }
      // End of list of possible types for union field part.
    }  
  
Fields  
---  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional metadata associated with this part.  
Union field `part`.`part` can be only one of the following:  
`text` |  `string`  
`file` |  `object (`[FilePart](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Part#FilePart)`)`  
`data` |  `object (`[DataPart](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Part#DataPart)`)`  
  
## FilePart

FilePart represents the different ways files can be provided. If files are small, directly feeding the bytes is supported via fileWithBytes. If the file is large, the agent should read the content as appropriate directly from the fileWithUri source.

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "name": string,
    
      // Union field file can be only one of the following:
      "fileWithUri": string,
      "fileWithBytes": string
      // End of list of possible types for union field file.
    }  
  
Fields  
---  
`mimeType` |  `string`  
`name` |  `string`  
Union field `file`.`file` can be only one of the following:  
`fileWithUri` |  `string`  
`fileWithBytes` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A base64-encoded string.  
  
## DataPart

DataPart represents a structured blob. This is most commonly a JSON payload.

JSON representation  
---  
      
    
    {
      "data": {
        object
      }
    }  
  
Fields  
---  
`data` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
