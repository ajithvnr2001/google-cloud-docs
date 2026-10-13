---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/ConditionEvaluation/
title: ConditionEvaluation \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:06.316202+00:00
---

# ConditionEvaluation  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/ConditionEvaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  ConditionEvaluation Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * EvaluationValue



The condition evaluation.

JSON representation  
---  
      
    
    {
      "evaluationValue": enum ([EvaluationValue](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/ConditionEvaluation#EvaluationValue))
    }  
  
Fields  
---  
`evaluationValue` |  `enum (`[EvaluationValue](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/ConditionEvaluation#EvaluationValue)`)` The evaluation result.  
  
## EvaluationValue

Value of this expression.

Enums  
---  
`EVALUATION_VALUE_UNSPECIFIED` | Reserved for future use.  
`TRUE` | The evaluation result is `true`.  
`FALSE` | The evaluation result is `false`.  
`CONDITIONAL` | The evaluation result is `conditional` when the condition expression contains variables that are either missing input values or have not been supported by Policy Analyzer yet.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-08 UTC."],[],[]] 
