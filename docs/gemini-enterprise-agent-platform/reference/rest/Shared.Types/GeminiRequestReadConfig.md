---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiRequestReadConfig/
title: GeminiRequestReadConfig \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:12:30.005063+00:00
---

# GeminiRequestReadConfig  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiRequestReadConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  GeminiRequestReadConfig Stay organized with collections  Save and categorize content based on your preferences. 

Configuration for how to read Gemini requests from a multimodal dataset.

Fields  
  
`read_config` `Union type`  
  
The read config for the dataset. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`templateConfig` `object (`[GeminiTemplateConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiRequestReadConfig#GeminiTemplateConfig)`)` Gemini request template with placeholders. | `assembledRequestColumnName` `string` Optional. column name in the dataset table that contains already fully assembled Gemini requests. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // read_config
      "templateConfig": {
        object ([GeminiTemplateConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiRequestReadConfig#GeminiTemplateConfig))
      },
      "assembledRequestColumnName": string
      // Union type
    }  
  
## GeminiTemplateConfig

Template configuration to create Gemini examples from a multimodal dataset.

Fields  
  
`geminiExample` `object (`[GeminiExample](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiExample)`)` Required. The template that will be used for assembling the request to use for downstream applications. | `fieldMapping` `map (key: string, value: string)` Required. Map of template parameters to the columns in the dataset table. | JSON representation  
---  
      
    
    {
      "geminiExample": {
        object ([GeminiExample](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiExample))
      },
      "fieldMapping": {
        string: string,
        ...
      }
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
