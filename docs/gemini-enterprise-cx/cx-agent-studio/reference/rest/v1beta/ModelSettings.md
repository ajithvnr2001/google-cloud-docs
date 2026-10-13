---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ModelSettings/
title: ModelSettings \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:41.784703+00:00
---

# ModelSettings  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ModelSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  ModelSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ModelSettings.ThinkingLevel



Model settings contains various configurations for the LLM model.

JSON representation  
---  
      
    
    {
      "model": string,
      "thinkingLevel": enum ([ModelSettings.ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ModelSettings#ModelSettings.ThinkingLevel)),
      "temperature": number
    }  
  
Fields  
---  
`model` |  `string` Optional. The LLM model that the agent should use. If not set, the agent will inherit the model from its parent agent.  
`thinkingLevel` |  `enum (`[ModelSettings.ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ModelSettings#ModelSettings.ThinkingLevel)`)` Optional. The thinking level of the model.  
`temperature` |  `number` Optional. If set, this temperature will be used for the LLM model. Temperature controls the randomness of the model's responses. Lower temperatures produce responses that are more predictable. Higher temperatures produce responses that are more creative.  
  
## ModelSettings.ThinkingLevel

Thinking level configuration for the model.

Enums  
---  
`THINKING_LEVEL_UNSPECIFIED` | Thinking level is unspecified.  
`DEFAULT` | Default thinking level.  
`LOW` | Low thinking level.  
`MEDIUM` | Medium thinking level.  
`HIGH` | High thinking level.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
