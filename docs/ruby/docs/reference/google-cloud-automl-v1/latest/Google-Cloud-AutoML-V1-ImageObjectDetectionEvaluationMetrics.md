---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ImageObjectDetectionEvaluationMetrics/
title: Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::ImageObjectDetectionEvaluationMetrics (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:43:50.782593+00:00
---

# Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::ImageObjectDetectionEvaluationMetrics (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ImageObjectDetectionEvaluationMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::ImageObjectDetectionEvaluationMetrics (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.1  0.4.8 

Reference documentation and code samples for the Cloud AutoML V1 API class Google::Cloud::AutoML::V1::ImageObjectDetectionEvaluationMetrics.

Model evaluation metrics for image object detection problems. Evaluates prediction quality of labeled bounding boxes.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #bounding_box_mean_average_precision
    
    
    def bounding_box_mean_average_precision() -> ::Float

**Returns**

  * (::Float) — Output only. The single metric for bounding boxes evaluation: the mean_average_precision averaged over all bounding_box_metrics_entries. 



### #bounding_box_mean_average_precision=
    
    
    def bounding_box_mean_average_precision=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Output only. The single metric for bounding boxes evaluation: the mean_average_precision averaged over all bounding_box_metrics_entries. 



**Returns**

  * (::Float) — Output only. The single metric for bounding boxes evaluation: the mean_average_precision averaged over all bounding_box_metrics_entries. 



### #bounding_box_metrics_entries
    
    
    def bounding_box_metrics_entries() -> ::Array<::Google::Cloud::AutoML::V1::BoundingBoxMetricsEntry>

**Returns**

  * (::Array<[::Google::Cloud::AutoML::V1::BoundingBoxMetricsEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-BoundingBoxMetricsEntry)>) — Output only. The bounding boxes match metrics for each Intersection-over-union threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and each label confidence threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 pair. 



### #bounding_box_metrics_entries=
    
    
    def bounding_box_metrics_entries=(value) -> ::Array<::Google::Cloud::AutoML::V1::BoundingBoxMetricsEntry>

**Parameter**

  * **value** (::Array<[::Google::Cloud::AutoML::V1::BoundingBoxMetricsEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-BoundingBoxMetricsEntry)>) — Output only. The bounding boxes match metrics for each Intersection-over-union threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and each label confidence threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 pair. 



**Returns**

  * (::Array<[::Google::Cloud::AutoML::V1::BoundingBoxMetricsEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-BoundingBoxMetricsEntry)>) — Output only. The bounding boxes match metrics for each Intersection-over-union threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and each label confidence threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 pair. 



### #evaluated_bounding_box_count
    
    
    def evaluated_bounding_box_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The total number of bounding boxes (i.e. summed over all images) the ground truth used to create this evaluation had. 



### #evaluated_bounding_box_count=
    
    
    def evaluated_bounding_box_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. The total number of bounding boxes (i.e. summed over all images) the ground truth used to create this evaluation had. 



**Returns**

  * (::Integer) — Output only. The total number of bounding boxes (i.e. summed over all images) the ground truth used to create this evaluation had. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
