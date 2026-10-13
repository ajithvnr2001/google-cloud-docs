---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-DistributionCut/
title: Cloud Monitoring V3 API - Class Google::Cloud::Monitoring::V3::DistributionCut (v1.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:35.651585+00:00
---

# Cloud Monitoring V3 API - Class Google::Cloud::Monitoring::V3::DistributionCut (v1.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-DistributionCut/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Monitoring V3 API - Class Google::Cloud::Monitoring::V3::DistributionCut (v1.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.1 (latest)  1.10.0  1.9.0  1.8.0  1.7.1  1.6.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.18.0  0.17.0  0.16.0  0.15.2  0.14.0  0.13.0  0.12.1  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1 

Reference documentation and code samples for the Cloud Monitoring V3 API class Google::Cloud::Monitoring::V3::DistributionCut.

A `DistributionCut` defines a `TimeSeries` and thresholds used for measuring good service and total service. The `TimeSeries` must have `ValueType = DISTRIBUTION` and `MetricKind = DELTA` or `MetricKind = CUMULATIVE`. The computed `good_service` will be the estimated count of values in the `Distribution` that fall within the specified `min` and `max`.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #distribution_filter
    
    
    def distribution_filter() -> ::String

**Returns**

  * (::String) — A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) specifying a `TimeSeries` aggregating values. Must have `ValueType = DISTRIBUTION` and `MetricKind = DELTA` or `MetricKind = CUMULATIVE`. 



### #distribution_filter=
    
    
    def distribution_filter=(value) -> ::String

**Parameter**

  * **value** (::String) — A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) specifying a `TimeSeries` aggregating values. Must have `ValueType = DISTRIBUTION` and `MetricKind = DELTA` or `MetricKind = CUMULATIVE`. 



**Returns**

  * (::String) — A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) specifying a `TimeSeries` aggregating values. Must have `ValueType = DISTRIBUTION` and `MetricKind = DELTA` or `MetricKind = CUMULATIVE`. 



### #range
    
    
    def range() -> ::Google::Cloud::Monitoring::V3::Range

**Returns**

  * ([::Google::Cloud::Monitoring::V3::Range](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-Range)) — Range of values considered "good." For a one-sided range, set one bound to an infinite value. 



### #range=
    
    
    def range=(value) -> ::Google::Cloud::Monitoring::V3::Range

**Parameter**

  * **value** ([::Google::Cloud::Monitoring::V3::Range](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-Range)) — Range of values considered "good." For a one-sided range, set one bound to an infinite value. 



**Returns**

  * ([::Google::Cloud::Monitoring::V3::Range](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-Range)) — Range of values considered "good." For a one-sided range, set one bound to an infinite value. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
