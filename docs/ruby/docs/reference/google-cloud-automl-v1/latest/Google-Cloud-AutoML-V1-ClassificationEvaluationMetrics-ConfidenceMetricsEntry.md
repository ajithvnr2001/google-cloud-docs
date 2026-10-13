---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ClassificationEvaluationMetrics-ConfidenceMetricsEntry/
title: Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfidenceMetricsEntry (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:25.156595+00:00
---

# Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfidenceMetricsEntry (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ClassificationEvaluationMetrics-ConfidenceMetricsEntry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfidenceMetricsEntry (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.1  0.4.8 

Reference documentation and code samples for the Cloud AutoML V1 API class Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfidenceMetricsEntry.

Metrics for a single confidence threshold.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #confidence_threshold
    
    
    def confidence_threshold() -> ::Float

**Returns**

  * (::Float) — Output only. Metrics are computed with an assumption that the model never returns predictions with score lower than this value. 



### #confidence_threshold=
    
    
    def confidence_threshold=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Output only. Metrics are computed with an assumption that the model never returns predictions with score lower than this value. 



**Returns**

  * (::Float) — Output only. Metrics are computed with an assumption that the model never returns predictions with score lower than this value. 



### #f1_score
    
    
    def f1_score() -> ::Float

**Returns**

  * (::Float) — Output only. The harmonic mean of recall and precision. 



### #f1_score=
    
    
    def f1_score=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Output only. The harmonic mean of recall and precision. 



**Returns**

  * (::Float) — Output only. The harmonic mean of recall and precision. 



### #f1_score_at1
    
    
    def f1_score_at1() -> ::Float

**Returns**

  * (::Float) — Output only. The harmonic mean of [recall_at1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ClassificationEvaluationMetrics-ConfidenceMetricsEntry#Google__Cloud__AutoML__V1__ClassificationEvaluationMetrics__ConfidenceMetricsEntry_recall_at1_instance_ "Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfidenceMetricsEntry#recall_at1 \(method\)") and [precision_at1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ClassificationEvaluationMetrics-ConfidenceMetricsEntry#Google__Cloud__AutoML__V1__ClassificationEvaluationMetrics__ConfidenceMetricsEntry_precision_at1_instance_ "Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfidenceMetricsEntry#precision_at1 \(method\)"). 



### #f1_score_at1=
    
    
    def f1_score_at1=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Output only. The harmonic mean of [recall_at1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ClassificationEvaluationMetrics-ConfidenceMetricsEntry#Google__Cloud__AutoML__V1__ClassificationEvaluationMetrics__ConfidenceMetricsEntry_recall_at1_instance_ "Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfidenceMetricsEntry#recall_at1 \(method\)") and [precision_at1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ClassificationEvaluationMetrics-ConfidenceMetricsEntry#Google__Cloud__AutoML__V1__ClassificationEvaluationMetrics__ConfidenceMetricsEntry_precision_at1_instance_ "Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfidenceMetricsEntry#precision_at1 \(method\)"). 



**Returns**

  * (::Float) — Output only. The harmonic mean of [recall_at1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ClassificationEvaluationMetrics-ConfidenceMetricsEntry#Google__Cloud__AutoML__V1__ClassificationEvaluationMetrics__ConfidenceMetricsEntry_recall_at1_instance_ "Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfidenceMetricsEntry#recall_at1 \(method\)") and [precision_at1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ClassificationEvaluationMetrics-ConfidenceMetricsEntry#Google__Cloud__AutoML__V1__ClassificationEvaluationMetrics__ConfidenceMetricsEntry_precision_at1_instance_ "Google::Cloud::AutoML::V1::ClassificationEvaluationMetrics::ConfidenceMetricsEntry#precision_at1 \(method\)"). 



### #false_negative_count
    
    
    def false_negative_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The number of ground truth labels that are not matched by a model created label. 



### #false_negative_count=
    
    
    def false_negative_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. The number of ground truth labels that are not matched by a model created label. 



**Returns**

  * (::Integer) — Output only. The number of ground truth labels that are not matched by a model created label. 



### #false_positive_count
    
    
    def false_positive_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The number of model created labels that do not match a ground truth label. 



### #false_positive_count=
    
    
    def false_positive_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. The number of model created labels that do not match a ground truth label. 



**Returns**

  * (::Integer) — Output only. The number of model created labels that do not match a ground truth label. 



### #false_positive_rate
    
    
    def false_positive_rate() -> ::Float

**Returns**

  * (::Float) — Output only. False Positive Rate for the given confidence threshold. 



### #false_positive_rate=
    
    
    def false_positive_rate=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Output only. False Positive Rate for the given confidence threshold. 



**Returns**

  * (::Float) — Output only. False Positive Rate for the given confidence threshold. 



### #false_positive_rate_at1
    
    
    def false_positive_rate_at1() -> ::Float

**Returns**

  * (::Float) — Output only. The False Positive Rate when only considering the label that has the highest prediction score and not below the confidence threshold for each example. 



### #false_positive_rate_at1=
    
    
    def false_positive_rate_at1=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Output only. The False Positive Rate when only considering the label that has the highest prediction score and not below the confidence threshold for each example. 



**Returns**

  * (::Float) — Output only. The False Positive Rate when only considering the label that has the highest prediction score and not below the confidence threshold for each example. 



### #position_threshold
    
    
    def position_threshold() -> ::Integer

**Returns**

  * (::Integer) — Output only. Metrics are computed with an assumption that the model always returns at most this many predictions (ordered by their score, descendingly), but they all still need to meet the confidence_threshold. 



### #position_threshold=
    
    
    def position_threshold=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. Metrics are computed with an assumption that the model always returns at most this many predictions (ordered by their score, descendingly), but they all still need to meet the confidence_threshold. 



**Returns**

  * (::Integer) — Output only. Metrics are computed with an assumption that the model always returns at most this many predictions (ordered by their score, descendingly), but they all still need to meet the confidence_threshold. 



### #precision
    
    
    def precision() -> ::Float

**Returns**

  * (::Float) — Output only. Precision for the given confidence threshold. 



### #precision=
    
    
    def precision=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Output only. Precision for the given confidence threshold. 



**Returns**

  * (::Float) — Output only. Precision for the given confidence threshold. 



### #precision_at1
    
    
    def precision_at1() -> ::Float

**Returns**

  * (::Float) — Output only. The precision when only considering the label that has the highest prediction score and not below the confidence threshold for each example. 



### #precision_at1=
    
    
    def precision_at1=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Output only. The precision when only considering the label that has the highest prediction score and not below the confidence threshold for each example. 



**Returns**

  * (::Float) — Output only. The precision when only considering the label that has the highest prediction score and not below the confidence threshold for each example. 



### #recall
    
    
    def recall() -> ::Float

**Returns**

  * (::Float) — Output only. Recall (True Positive Rate) for the given confidence threshold. 



### #recall=
    
    
    def recall=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Output only. Recall (True Positive Rate) for the given confidence threshold. 



**Returns**

  * (::Float) — Output only. Recall (True Positive Rate) for the given confidence threshold. 



### #recall_at1
    
    
    def recall_at1() -> ::Float

**Returns**

  * (::Float) — Output only. The Recall (True Positive Rate) when only considering the label that has the highest prediction score and not below the confidence threshold for each example. 



### #recall_at1=
    
    
    def recall_at1=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Output only. The Recall (True Positive Rate) when only considering the label that has the highest prediction score and not below the confidence threshold for each example. 



**Returns**

  * (::Float) — Output only. The Recall (True Positive Rate) when only considering the label that has the highest prediction score and not below the confidence threshold for each example. 



### #true_negative_count
    
    
    def true_negative_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The number of labels that were not created by the model, but if they would, they would not match a ground truth label. 



### #true_negative_count=
    
    
    def true_negative_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. The number of labels that were not created by the model, but if they would, they would not match a ground truth label. 



**Returns**

  * (::Integer) — Output only. The number of labels that were not created by the model, but if they would, they would not match a ground truth label. 



### #true_positive_count
    
    
    def true_positive_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The number of model created labels that match a ground truth label. 



### #true_positive_count=
    
    
    def true_positive_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. The number of model created labels that match a ground truth label. 



**Returns**

  * (::Integer) — Output only. The number of model created labels that match a ground truth label. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
