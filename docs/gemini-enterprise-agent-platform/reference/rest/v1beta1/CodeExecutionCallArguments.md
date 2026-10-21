---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/CodeExecutionCallArguments/
title: CodeExecutionCallArguments \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:26:50.863086+00:00
---

# CodeExecutionCallArguments  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/CodeExecutionCallArguments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  CodeExecutionCallArguments Stay organized with collections  Save and categorize content based on your preferences. 

The arguments to pass to the code execution.

Fields  
  
`language` `enum (`[Language](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/CodeExecutionCallArguments#Language)`)` Programming language of the `code`. | `code` `string` The code to be executed. | JSON representation  
---  
      
    
    {
      "language": enum ([Language](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/CodeExecutionCallArguments#Language)),
      "code": string
    }  
  
## Language

Supported programming languages for the generated code.

Enums  
---  
`LANGUAGE_UNSPECIFIED` | Unspecified language. This value should not be used.  
`PYTHON` | Python >= 3.10, with numpy and simpy available.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-01 UTC."],[],[]] 
