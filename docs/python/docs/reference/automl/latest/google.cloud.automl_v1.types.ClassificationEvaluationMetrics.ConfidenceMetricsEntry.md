---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ClassificationEvaluationMetrics.ConfidenceMetricsEntry
title: Class ConfidenceMetricsEntry (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:23.777817+00:00
---

# Class ConfidenceMetricsEntry (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ClassificationEvaluationMetrics.ConfidenceMetricsEntry

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ConfidenceMetricsEntry (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    ConfidenceMetricsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Metrics for a single confidence threshold.

## Attributes  
  
---  
**Name** | **Description**  
`confidence_threshold` |  `float`   
Output only. Metrics are computed with an assumption that the model never returns predictions with score lower than this value.   
`position_threshold` |  `int`   
Output only. Metrics are computed with an assumption that the model always returns at most this many predictions (ordered by their score, descendingly), but they all still need to meet the confidence_threshold.   
`recall` |  `float`   
Output only. Recall (True Positive Rate) for the given confidence threshold.   
`precision` |  `float`   
Output only. Precision for the given confidence threshold.   
`false_positive_rate` |  `float`   
Output only. False Positive Rate for the given confidence threshold.   
`f1_score` |  `float`   
Output only. The harmonic mean of recall and precision.   
`recall_at1` |  `float`   
Output only. The Recall (True Positive Rate) when only considering the label that has the highest prediction score and not below the confidence threshold for each example.   
`precision_at1` |  `float`   
Output only. The precision when only considering the label that has the highest prediction score and not below the confidence threshold for each example.   
`false_positive_rate_at1` |  `float`   
Output only. The False Positive Rate when only considering the label that has the highest prediction score and not below the confidence threshold for each example.   
`f1_score_at1` |  `float`   
Output only. The harmonic mean of recall_at1 and precision_at1.   
`true_positive_count` |  `int`   
Output only. The number of model created labels that match a ground truth label.   
`false_positive_count` |  `int`   
Output only. The number of model created labels that do not match a ground truth label.   
`false_negative_count` |  `int`   
Output only. The number of ground truth labels that are not matched by a model created label.   
`true_negative_count` |  `int`   
Output only. The number of labels that were not created by the model, but if they would, they would not match a ground truth label.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
