---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/PredictionResult/
title: PredictionResult \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:13:35.086816+00:00
---

# PredictionResult  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/PredictionResult/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  PredictionResult Stay organized with collections  Save and categorize content based on your preferences. 

Represents a line of JSONL in the batch prediction output file.

Fields  
  
`prediction` `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` The prediction result. value is used here instead of Any so that JsonFormat does not append an extra "@type" field when we convert the proto to JSON and so we can represent array of objects. Do not set error if this is set. | `error` `object (`[Error](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/PredictionResult#Error)`)` The error result. Do not set prediction if this is set. | `input` `Union type`  
  
Some identifier from the input so that the prediction can be mapped back to the input instance. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`instance` `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` user's input instance. Struct is used here instead of Any so that JsonFormat does not append an extra "@type" field when we convert the proto to JSON. | `key` `string` Optional user-provided key from the input instance. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "prediction": value,
      "error": {
        object ([Error](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/PredictionResult#Error))
      },
    
      // input
      "instance": {
        object
      },
      "key": string
      // Union type
    }  
  
## Error

Fields  
  
`status` `enum (`[Code](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Code)`)` Error status. This will be serialized into the enum name e.g. "NOT_FOUND". | `message` `string` Error message with additional details. | JSON representation  
---  
      
    
    {
      "status": enum ([Code](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Code)),
      "message": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
