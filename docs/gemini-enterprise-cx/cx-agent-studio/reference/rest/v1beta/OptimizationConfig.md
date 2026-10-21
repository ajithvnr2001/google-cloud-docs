---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/OptimizationConfig/
title: OptimizationConfig \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:20:45.656859+00:00
---

# OptimizationConfig  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/OptimizationConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  OptimizationConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * OptimizationConfig.OptimizationStatus



Configuration for running the optimization step after the evaluation run.

JSON representation  
---  
      
    
    {
      "generateLossReport": boolean,
      "assistantSession": string,
      "reportSummary": string,
      "shouldSuggestFix": boolean,
      "status": enum ([OptimizationConfig.OptimizationStatus](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/OptimizationConfig#OptimizationConfig.OptimizationStatus)),
      "errorMessage": string,
      "lossReport": {
        object
      }
    }  
  
Fields  
---  
`generateLossReport` |  `boolean` Optional. Whether to generate a loss report.  
`assistantSession` |  `string` Output only. The assistant session to use for the optimization based on this evaluation run. Format: `projects/{project}/locations/{location}/apps/{app}/assistantSessions/{assistantSession}`  
`reportSummary` |  `string` Output only. The summary of the loss report.  
`shouldSuggestFix` |  `boolean` Output only. Whether to suggest a fix for the losses.  
`status` |  `enum (`[OptimizationConfig.OptimizationStatus](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/OptimizationConfig#OptimizationConfig.OptimizationStatus)`)` Output only. The status of the optimization run.  
`errorMessage` |  `string` Output only. The error message if the optimization run failed.  
`lossReport` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. The generated loss report.  
  
## OptimizationConfig.OptimizationStatus

The status of the optimization run.

Enums  
---  
`OPTIMIZATION_STATUS_UNSPECIFIED` | Optimization status is not specified.  
`RUNNING` | Optimization is running.  
`COMPLETED` | Optimization has completed.  
`ERROR` | Optimization failed due to an internal error.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
