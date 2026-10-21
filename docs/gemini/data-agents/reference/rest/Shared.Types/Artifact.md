---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Artifact/
title: Artifact \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:56:57.188457+00:00
---

# Artifact  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Artifact/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  Artifact Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Artifacts are the container for task completed results. These are similar to Messages but are intended to be the product of a task, as opposed to point-to-point communication.

JSON representation  
---  
      
    
    {
      "artifactId": string,
      "name": string,
      "description": string,
      "parts": [
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
`artifactId` |  `string` Unique identifier (e.g. UUID) for the artifact. It must be at least unique within a task.  
`name` |  `string` A human readable name for the artifact.  
`description` |  `string` A human readable description of the artifact, optional.  
`parts[]` |  `object (`[Part](https://docs.cloud.google.com/gemini/data-agents/reference/rest/Shared.Types/Part)`)` The content of the artifact.  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional metadata included with the artifact.  
`extensions[]` |  `string` The URIs of extensions that are present or contributed to this Artifact.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
