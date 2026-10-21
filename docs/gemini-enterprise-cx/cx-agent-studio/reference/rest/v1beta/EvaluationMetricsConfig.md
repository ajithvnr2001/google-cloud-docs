---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig/
title: EvaluationMetricsConfig \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:59:21.255387+00:00
---

# EvaluationMetricsConfig  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  EvaluationMetricsConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * EvaluationMetricsConfig.GoldenMetricsConfig
    * JSON representation
  * EvaluationMetricsConfig.ToolCorrectnessMetricsConfig
    * JSON representation
  * EvaluationMetricsConfig.ScenarioMetricsConfig
    * JSON representation
  * EvaluationMetricsConfig.UserGoalMetMetricsConfig
    * JSON representation
  * EvaluationMetricsConfig.ExpectationsMetMetricsConfig
    * JSON representation



Configures the metrics for an evaluation.

JSON representation  
---  
      
    
    {
      "goldenMetricsConfig": {
        object ([EvaluationMetricsConfig.GoldenMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig#EvaluationMetricsConfig.GoldenMetricsConfig))
      },
      "scenarioMetricsConfig": {
        object ([EvaluationMetricsConfig.ScenarioMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig#EvaluationMetricsConfig.ScenarioMetricsConfig))
      }
    }  
  
Fields  
---  
`goldenMetricsConfig` |  `object (`[EvaluationMetricsConfig.GoldenMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig#EvaluationMetricsConfig.GoldenMetricsConfig)`)` Optional. Configuration for the golden metrics for the evaluation.  
`scenarioMetricsConfig` |  `object (`[EvaluationMetricsConfig.ScenarioMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig#EvaluationMetricsConfig.ScenarioMetricsConfig)`)` Optional. Configuration for the scenario metrics for the evaluation.  
  
## EvaluationMetricsConfig.GoldenMetricsConfig

Configuration for the golden metrics for the evaluation.

JSON representation  
---  
      
    
    {
      "semanticSimilarityMetricsConfig": {
        object ([EvaluationMetricsConfig.SemanticSimilarityMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig.SemanticSimilarityMetricsConfig))
      },
      "toolCorrectnessMetricsConfig": {
        object ([EvaluationMetricsConfig.ToolCorrectnessMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig#EvaluationMetricsConfig.ToolCorrectnessMetricsConfig))
      },
      "stepToolCorrectnessMetricsConfig": {
        object ([EvaluationMetricsConfig.ToolCorrectnessMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig#EvaluationMetricsConfig.ToolCorrectnessMetricsConfig))
      }
    }  
  
Fields  
---  
`semanticSimilarityMetricsConfig` |  `object (`[EvaluationMetricsConfig.SemanticSimilarityMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig.SemanticSimilarityMetricsConfig)`)` Optional. Global configuration for semantic similarity metrics.  
`toolCorrectnessMetricsConfig` |  `object (`[EvaluationMetricsConfig.ToolCorrectnessMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig#EvaluationMetricsConfig.ToolCorrectnessMetricsConfig)`)` Optional. Configuration for turn level tool correctness metrics.  
`stepToolCorrectnessMetricsConfig` |  `object (`[EvaluationMetricsConfig.ToolCorrectnessMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig#EvaluationMetricsConfig.ToolCorrectnessMetricsConfig)`)` Optional. Configuration for step level tool correctness metrics.  
  
## EvaluationMetricsConfig.ToolCorrectnessMetricsConfig

Configuration for correctness metrics for the evaluation. To disable the metric, set the message but do not set the `enableToolCorrectnessMetrics` field to true (or explicitly set it to false). To unset the configuration and fallback to the default behavior, omit the message entirely.

JSON representation  
---  
      
    
    {
      "enableToolCorrectnessMetrics": boolean
    }  
  
Fields  
---  
`enableToolCorrectnessMetrics` |  `boolean` Optional. Whether to calculate tool correctness metrics for the evaluation.  
  
## EvaluationMetricsConfig.ScenarioMetricsConfig

Configuration for the scenario metrics for the evaluation.

JSON representation  
---  
      
    
    {
      "userGoalMetMetricsConfig": {
        object ([EvaluationMetricsConfig.UserGoalMetMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig#EvaluationMetricsConfig.UserGoalMetMetricsConfig))
      },
      "expectationsMetMetricsConfig": {
        object ([EvaluationMetricsConfig.ExpectationsMetMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig#EvaluationMetricsConfig.ExpectationsMetMetricsConfig))
      }
    }  
  
Fields  
---  
`userGoalMetMetricsConfig` |  `object (`[EvaluationMetricsConfig.UserGoalMetMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig#EvaluationMetricsConfig.UserGoalMetMetricsConfig)`)` Optional. Configuration for user goal met metrics.  
`expectationsMetMetricsConfig` |  `object (`[EvaluationMetricsConfig.ExpectationsMetMetricsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig#EvaluationMetricsConfig.ExpectationsMetMetricsConfig)`)` Optional. Configuration for expectation level metrics.  
  
## EvaluationMetricsConfig.UserGoalMetMetricsConfig

Configuration for the user goal met metrics for the evaluation. To disable the metric, set the message but do not set the `enableUserGoalMetMetrics` field to true (or explicitly set it to false). To unset the configuration and fallback to the default behavior, omit the message entirely.

JSON representation  
---  
      
    
    {
      "enableUserGoalMetMetrics": boolean
    }  
  
Fields  
---  
`enableUserGoalMetMetrics` |  `boolean` Optional. Whether to calculate the user goal met metrics for the evaluation.  
  
## EvaluationMetricsConfig.ExpectationsMetMetricsConfig

Configuration for the expectation level metrics for the evaluation. To disable the metric, set the message but do not set the `enableExpectationsMetMetrics` field to true (or explicitly set it to false). To unset the configuration and fallback to the default behavior, omit the message entirely.

JSON representation  
---  
      
    
    {
      "enableExpectationsMetMetrics": boolean
    }  
  
Fields  
---  
`enableExpectationsMetMetrics` |  `boolean` Optional. Whether to calculate the expectation level metrics for the evaluation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
