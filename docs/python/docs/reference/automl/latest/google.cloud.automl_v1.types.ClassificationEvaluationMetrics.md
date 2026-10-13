---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ClassificationEvaluationMetrics
title: Class ClassificationEvaluationMetrics (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:23.906854+00:00
---

# Class ClassificationEvaluationMetrics (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ClassificationEvaluationMetrics

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ClassificationEvaluationMetrics (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    ClassificationEvaluationMetrics(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Model evaluation metrics for classification problems. Note: For Video Classification this metrics only describe quality of the Video Classification predictions of "segment_classification" type.

## Attributes  
  
---  
**Name** | **Description**  
`au_prc` |  `float`   
Output only. The Area Under Precision-Recall Curve metric. Micro-averaged for the overall evaluation.   
`au_roc` |  `float`   
Output only. The Area Under Receiver Operating Characteristic curve metric. Micro-averaged for the overall evaluation.   
`log_loss` |  `float`   
Output only. The Log Loss metric.   
`confidence_metrics_entry` |  `MutableSequence[[google.cloud.automl_v1.types.ClassificationEvaluationMetrics.ConfidenceMetricsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ClassificationEvaluationMetrics.ConfidenceMetricsEntry)]`   
Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed.   
`confusion_matrix` |  `[google.cloud.automl_v1.types.ClassificationEvaluationMetrics.ConfusionMatrix](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ClassificationEvaluationMetrics.ConfusionMatrix)`   
Output only. Confusion matrix of the evaluation. Only set for MULTICLASS classification problems where number of labels is no more than 10. Only set for model level evaluation, not for evaluation per label.   
`annotation_spec_id` |  `MutableSequence[str]`   
Output only. The annotation spec ids used for this evaluation.   
  
## Classes 

### ConfidenceMetricsEntry
    
    
    ConfidenceMetricsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Metrics for a single confidence threshold.

### ConfusionMatrix
    
    
    ConfusionMatrix(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Confusion matrix of the model running the classification.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
