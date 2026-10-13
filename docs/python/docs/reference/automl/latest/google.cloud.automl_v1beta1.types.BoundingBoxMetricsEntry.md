---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BoundingBoxMetricsEntry
title: Class BoundingBoxMetricsEntry (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:43.647369+00:00
---

# Class BoundingBoxMetricsEntry (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BoundingBoxMetricsEntry

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BoundingBoxMetricsEntry (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    BoundingBoxMetricsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bounding box matching model metrics for a single intersection-over-union threshold and multiple label match confidence thresholds.

## Attributes  
  
---  
**Name** | **Description**  
`iou_threshold` |  `float`   
Output only. The intersection-over-union threshold value used to compute this metrics entry.   
`mean_average_precision` |  `float`   
Output only. The mean average precision, most often close to au_prc.   
`confidence_metrics_entries` |  `MutableSequence[[google.cloud.automl_v1beta1.types.BoundingBoxMetricsEntry.ConfidenceMetricsEntry](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.BoundingBoxMetricsEntry.ConfidenceMetricsEntry)]`   
Output only. Metrics for each label-match confidence_threshold from 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99. Precision-recall curve is derived from them.   
  
## Classes 

### ConfidenceMetricsEntry
    
    
    ConfidenceMetricsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Metrics for a single confidence threshold.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
