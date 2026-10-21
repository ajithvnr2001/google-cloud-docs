---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TextSentimentEvaluationMetrics/
title: TextSentimentEvaluationMetrics \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:28:19.657861+00:00
---

# TextSentimentEvaluationMetrics  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TextSentimentEvaluationMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  TextSentimentEvaluationMetrics Stay organized with collections  Save and categorize content based on your preferences. 

Model evaluation metrics for text sentiment problems.

Fields  
  
`confusionMatrix` `object (`[ConfusionMatrix](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ConfusionMatrix)`)` Confusion matrix of the evaluation. Only set for ModelEvaluations, not for ModelEvaluationSlices. | `precision` `number` Precision. | `recall` `number` Recall. | `f1Score` `number` The harmonic mean of recall and precision. | `meanAbsoluteError` `number` Mean absolute error. Only set for ModelEvaluations, not for ModelEvaluationSlices. | `meanSquaredError` `number` Mean squared error. Only set for ModelEvaluations, not for ModelEvaluationSlices. | `linearKappa` `number` Linear weighted kappa. Only set for ModelEvaluations, not for ModelEvaluationSlices. | `quadraticKappa` `number` Quadratic weighted kappa. Only set for ModelEvaluations, not for ModelEvaluationSlices. | JSON representation  
---  
      
    
    {
      "confusionMatrix": {
        object ([ConfusionMatrix](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ConfusionMatrix))
      },
      "precision": number,
      "recall": number,
      "f1Score": number,
      "meanAbsoluteError": number,
      "meanSquaredError": number,
      "linearKappa": number,
      "quadraticKappa": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
