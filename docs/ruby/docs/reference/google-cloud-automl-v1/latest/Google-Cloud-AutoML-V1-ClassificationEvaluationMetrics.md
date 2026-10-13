---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ClassificationEvaluationMetrics/
title: Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:47.071547+00:00
---

# Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ClassificationEvaluationMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.1  0.4.8 

Reference documentation and code samples for the Cloud AutoML V1 API class Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics.

Model evaluation metrics for classification problems. Note: For Video Classification this metrics only describe quality of the Video Classification predictions of "segment_classification" type.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #annotation_spec_id
    
    
    def annotation_spec_id() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. The annotation spec ids used for this evaluation. 



### #annotation_spec_id=
    
    
    def annotation_spec_id=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Output only. The annotation spec ids used for this evaluation. 



**Returns**

  * (::Array<::String>) — Output only. The annotation spec ids used for this evaluation. 



### #au_prc
    
    
    def au_prc() -> ::Float

**Returns**

  * (::Float) — Output only. The Area Under Precision-Recall Curve metric. Micro-averaged for the overall evaluation. 



### #au_prc=
    
    
    def au_prc=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Output only. The Area Under Precision-Recall Curve metric. Micro-averaged for the overall evaluation. 



**Returns**

  * (::Float) — Output only. The Area Under Precision-Recall Curve metric. Micro-averaged for the overall evaluation. 



### #au_roc
    
    
    def au_roc() -> ::Float

**Returns**

  * (::Float) — Output only. The Area Under Receiver Operating Characteristic curve metric. Micro-averaged for the overall evaluation. 



### #au_roc=
    
    
    def au_roc=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Output only. The Area Under Receiver Operating Characteristic curve metric. Micro-averaged for the overall evaluation. 



**Returns**

  * (::Float) — Output only. The Area Under Receiver Operating Characteristic curve metric. Micro-averaged for the overall evaluation. 



### #confidence_metrics_entry
    
    
    def confidence_metrics_entry() -> ::Array<::Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfidenceMetricsEntry>

**Returns**

  * (::Array<[::Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfidenceMetricsEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ClassificationEvaluationMetrics-ConfidenceMetricsEntry)>) — Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed. 



### #confidence_metrics_entry=
    
    
    def confidence_metrics_entry=(value) -> ::Array<::Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfidenceMetricsEntry>

**Parameter**

  * **value** (::Array<[::Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfidenceMetricsEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ClassificationEvaluationMetrics-ConfidenceMetricsEntry)>) — Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed. 



**Returns**

  * (::Array<[::Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfidenceMetricsEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ClassificationEvaluationMetrics-ConfidenceMetricsEntry)>) — Output only. Metrics for each confidence_threshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and position_threshold = INT32_MAX_VALUE. ROC and precision-recall curves, and other aggregated metrics are derived from them. The confidence metrics entries may also be supplied for additional values of position_threshold, but from these no aggregated metrics are computed. 



### #confusion_matrix
    
    
    def confusion_matrix() -> ::Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfusionMatrix

**Returns**

  * ([::Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfusionMatrix](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ClassificationEvaluationMetrics-ConfusionMatrix)) — Output only. Confusion matrix of the evaluation. Only set for MULTICLASS classification problems where number of labels is no more than 10. Only set for model level evaluation, not for evaluation per label. 



### #confusion_matrix=
    
    
    def confusion_matrix=(value) -> ::Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfusionMatrix

**Parameter**

  * **value** ([::Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfusionMatrix](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ClassificationEvaluationMetrics-ConfusionMatrix)) — Output only. Confusion matrix of the evaluation. Only set for MULTICLASS classification problems where number of labels is no more than 10. Only set for model level evaluation, not for evaluation per label. 



**Returns**

  * ([::Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfusionMatrix](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ClassificationEvaluationMetrics-ConfusionMatrix)) — Output only. Confusion matrix of the evaluation. Only set for MULTICLASS classification problems where number of labels is no more than 10. Only set for model level evaluation, not for evaluation per label. 



### #log_loss
    
    
    def log_loss() -> ::Float

**Returns**

  * (::Float) — Output only. The Log Loss metric. 



### #log_loss=
    
    
    def log_loss=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Output only. The Log Loss metric. 



**Returns**

  * (::Float) — Output only. The Log Loss metric. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
