---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationRunCachingSettings/
title: EvaluationRunCachingSettings \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:00:22.409356+00:00
---

# EvaluationRunCachingSettings  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationRunCachingSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  EvaluationRunCachingSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * EvaluationRunCachingSettings.EvaluationRunCachingMode



Settings for evaluation run caching.

JSON representation  
---  
      
    
    {
      "runCachingMode": enum ([EvaluationRunCachingSettings.EvaluationRunCachingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationRunCachingSettings#EvaluationRunCachingSettings.EvaluationRunCachingMode))
    }  
  
Fields  
---  
`runCachingMode` |  `enum (`[EvaluationRunCachingSettings.EvaluationRunCachingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationRunCachingSettings#EvaluationRunCachingSettings.EvaluationRunCachingMode)`)` Optional. The caching mode to use for the evaluation run. If not set, default to FORCE_RUN.  
  
## EvaluationRunCachingSettings.EvaluationRunCachingMode

The evaluation result caching behavior. Controls whether to return the last completed evaluation result (if existing) or to execute a new evaluation.

Enums  
---  
`EVALUATION_RUN_CACHING_MODE_UNSPECIFIED` | The run caching mode is unspecified.  
`FORCE_RUN` | Always execute a full live simulation regardless of whether changelogs exist.  
`SKIP_IF_UNCHANGED` | Skip execution and copy previous verified results if no dependencies have mutated, the evaluation channel/run method are the same.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
