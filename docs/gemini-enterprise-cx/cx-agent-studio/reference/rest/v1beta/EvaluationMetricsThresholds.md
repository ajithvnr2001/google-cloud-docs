---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds/
title: EvaluationMetricsThresholds \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:47:55.830030+00:00
---

# EvaluationMetricsThresholds  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  EvaluationMetricsThresholds Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds
    * JSON representation
  * EvaluationMetricsThresholds.ToolMatchingSettings
    * JSON representation
  * EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior



Threshold settings for metrics in an Evaluation.

JSON representation  
---  
      
    
    {
      "goldenEvaluationMetricsThresholds": {
        object ([EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds#EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds))
      },
      "hallucinationMetricBehavior": enum ([EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds.HallucinationMetricBehavior)),
      "goldenHallucinationMetricBehavior": enum ([EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds.HallucinationMetricBehavior)),
      "scenarioHallucinationMetricBehavior": enum ([EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds.HallucinationMetricBehavior))
    }  
  
Fields  
---  
`goldenEvaluationMetricsThresholds` |  `object (`[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds#EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds)`)` Optional. The golden evaluation metrics thresholds.  
`hallucinationMetricBehavior  
**(deprecated)**` |  `enum (`[EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds.HallucinationMetricBehavior)`)` This item is deprecated!Optional. Deprecated: Use `goldenHallucinationMetricBehavior` instead. The hallucination metric behavior is currently used for golden evaluations.  
`goldenHallucinationMetricBehavior` |  `enum (`[EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds.HallucinationMetricBehavior)`)` Optional. The hallucination metric behavior for golden evaluations.  
`scenarioHallucinationMetricBehavior` |  `enum (`[EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds.HallucinationMetricBehavior)`)` Optional. The hallucination metric behavior for scenario evaluations.  
  
## EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds

Settings for golden evaluations.

JSON representation  
---  
      
    
    {
      "turnLevelMetricsThresholds": {
        object ([EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds))
      },
      "expectationLevelMetricsThresholds": {
        object ([EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds))
      },
      "toolMatchingSettings": {
        object ([EvaluationMetricsThresholds.ToolMatchingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds#EvaluationMetricsThresholds.ToolMatchingSettings))
      }
    }  
  
Fields  
---  
`turnLevelMetricsThresholds` |  `object (`[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds)`)` Optional. The turn level metrics thresholds.  
`expectationLevelMetricsThresholds` |  `object (`[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds)`)` Optional. The expectation level metrics thresholds.  
`toolMatchingSettings` |  `object (`[EvaluationMetricsThresholds.ToolMatchingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds#EvaluationMetricsThresholds.ToolMatchingSettings)`)` Optional. The tool matching settings. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.  
  
## EvaluationMetricsThresholds.ToolMatchingSettings

Settings for matching tool calls.

JSON representation  
---  
      
    
    {
      "extraToolCallBehavior": enum ([EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds#EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior))
    }  
  
Fields  
---  
`extraToolCallBehavior` |  `enum (`[EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsThresholds#EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior)`)` Optional. Behavior for extra tool calls. Defaults to FAIL.  
  
## EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior

Defines the behavior when an extra tool call is encountered. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.

Enums  
---  
`EXTRA_TOOL_CALL_BEHAVIOR_UNSPECIFIED` | Unspecified behavior. Defaults to FAIL.  
`FAIL` | Fail the evaluation if an extra tool call is encountered.  
`ALLOW` | Allow the extra tool call.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
