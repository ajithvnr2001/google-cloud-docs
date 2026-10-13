---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextSentimentEvaluationMetrics
title: Class TextSentimentEvaluationMetrics (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:35.277885+00:00
---

# Class TextSentimentEvaluationMetrics (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextSentimentEvaluationMetrics

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TextSentimentEvaluationMetrics (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    TextSentimentEvaluationMetrics(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Model evaluation metrics for text sentiment problems.

## Attributes  
  
---  
**Name** | **Description**  
`precision` |  `float`   
Output only. Precision.   
`recall` |  `float`   
Output only. Recall.   
`f1_score` |  `float`   
Output only. The harmonic mean of recall and precision.   
`mean_absolute_error` |  `float`   
Output only. Mean absolute error. Only set for the overall model evaluation, not for evaluation of a single annotation spec.   
`mean_squared_error` |  `float`   
Output only. Mean squared error. Only set for the overall model evaluation, not for evaluation of a single annotation spec.   
`linear_kappa` |  `float`   
Output only. Linear weighted kappa. Only set for the overall model evaluation, not for evaluation of a single annotation spec.   
`quadratic_kappa` |  `float`   
Output only. Quadratic weighted kappa. Only set for the overall model evaluation, not for evaluation of a single annotation spec.   
`confusion_matrix` |  `[google.cloud.automl_v1.types.ClassificationEvaluationMetrics.ConfusionMatrix](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ClassificationEvaluationMetrics.ConfusionMatrix)`   
Output only. Confusion matrix of the evaluation. Only set for the overall model evaluation, not for evaluation of a single annotation spec.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
