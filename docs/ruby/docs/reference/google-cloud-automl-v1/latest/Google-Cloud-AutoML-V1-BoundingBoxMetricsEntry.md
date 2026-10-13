---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-BoundingBoxMetricsEntry/
title: Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::BoundingBoxMetricsEntry (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:34.450917+00:00
---

# Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::BoundingBoxMetricsEntry (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-BoundingBoxMetricsEntry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::BoundingBoxMetricsEntry (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.1  0.4.8 

Reference documentation and code samples for the Cloud AutoML V1 API class Google::Cloud::AutoML::V1::BoundingBoxMetricsEntry.

Bounding box matching model metrics for a single intersection-over-union threshold and multiple label match confidence thresholds.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #confidence_metrics_entries
    
    
    def confidence_metrics_entries() -> ::Array<::Google::Cloud::AutoML::V1::BoundingBoxMetricsEntry::ConfidenceMetricsEntry>

**Returns**

  * (::Array<[::Google::Cloud::AutoML::V1::BoundingBoxMetricsEntry::ConfidenceMetricsEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-BoundingBoxMetricsEntry-ConfidenceMetricsEntry)>) — Output only. Metrics for each label-match confidence_threshold from 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99. Precision-recall curve is derived from them. 



### #confidence_metrics_entries=
    
    
    def confidence_metrics_entries=(value) -> ::Array<::Google::Cloud::AutoML::V1::BoundingBoxMetricsEntry::ConfidenceMetricsEntry>

**Parameter**

  * **value** (::Array<[::Google::Cloud::AutoML::V1::BoundingBoxMetricsEntry::ConfidenceMetricsEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-BoundingBoxMetricsEntry-ConfidenceMetricsEntry)>) — Output only. Metrics for each label-match confidence_threshold from 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99. Precision-recall curve is derived from them. 



**Returns**

  * (::Array<[::Google::Cloud::AutoML::V1::BoundingBoxMetricsEntry::ConfidenceMetricsEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-BoundingBoxMetricsEntry-ConfidenceMetricsEntry)>) — Output only. Metrics for each label-match confidence_threshold from 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99. Precision-recall curve is derived from them. 



### #iou_threshold
    
    
    def iou_threshold() -> ::Float

**Returns**

  * (::Float) — Output only. The intersection-over-union threshold value used to compute this metrics entry. 



### #iou_threshold=
    
    
    def iou_threshold=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Output only. The intersection-over-union threshold value used to compute this metrics entry. 



**Returns**

  * (::Float) — Output only. The intersection-over-union threshold value used to compute this metrics entry. 



### #mean_average_precision
    
    
    def mean_average_precision() -> ::Float

**Returns**

  * (::Float) — Output only. The mean average precision, most often close to au_prc. 



### #mean_average_precision=
    
    
    def mean_average_precision=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Output only. The mean average precision, most often close to au_prc. 



**Returns**

  * (::Float) — Output only. The mean average precision, most often close to au_prc. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
