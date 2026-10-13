---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TimeSeries/
title: BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::TimeSeries (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:14.427356+00:00
---

# BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::TimeSeries (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TimeSeries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::TimeSeries (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Cloud::Bigquery::Migration::V2::TimeSeries.

The metrics object for a SubTask.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #metric
    
    
    def metric() -> ::String

**Returns**

  * (::String) — Required. The name of the metric.

If the metric is not known by the service yet, it will be auto-created. 




### #metric=
    
    
    def metric=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the metric.

If the metric is not known by the service yet, it will be auto-created. 




**Returns**

  * (::String) — Required. The name of the metric.

If the metric is not known by the service yet, it will be auto-created. 




### #metric_kind
    
    
    def metric_kind() -> ::Google::Api::MetricDescriptor::MetricKind

**Returns**

  * ([::Google::Api::MetricDescriptor::MetricKind](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-MetricKind)) — Optional. The metric kind of the time series.

If present, it must be the same as the metric kind of the associated metric. If the associated metric's descriptor must be auto-created, then this field specifies the metric kind of the new descriptor and must be either `GAUGE` (the default) or `CUMULATIVE`. 




### #metric_kind=
    
    
    def metric_kind=(value) -> ::Google::Api::MetricDescriptor::MetricKind

**Parameter**

  * **value** ([::Google::Api::MetricDescriptor::MetricKind](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-MetricKind)) — Optional. The metric kind of the time series.

If present, it must be the same as the metric kind of the associated metric. If the associated metric's descriptor must be auto-created, then this field specifies the metric kind of the new descriptor and must be either `GAUGE` (the default) or `CUMULATIVE`. 




**Returns**

  * ([::Google::Api::MetricDescriptor::MetricKind](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-MetricKind)) — Optional. The metric kind of the time series.

If present, it must be the same as the metric kind of the associated metric. If the associated metric's descriptor must be auto-created, then this field specifies the metric kind of the new descriptor and must be either `GAUGE` (the default) or `CUMULATIVE`. 




### #points
    
    
    def points() -> ::Array<::Google::Cloud::Bigquery::Migration::V2::Point>

**Returns**

  * (::Array<[::Google::Cloud::Bigquery::Migration::V2::Point](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-Point)>) — Required. The data points of this time series. When listing time series, points are returned in reverse time order.

When creating a time series, this field must contain exactly one point and the point's type must be the same as the value type of the associated metric. If the associated metric's descriptor must be auto-created, then the value type of the descriptor is determined by the point's type, which must be `BOOL`, `INT64`, `DOUBLE`, or `DISTRIBUTION`. 




### #points=
    
    
    def points=(value) -> ::Array<::Google::Cloud::Bigquery::Migration::V2::Point>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Bigquery::Migration::V2::Point](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-Point)>) — Required. The data points of this time series. When listing time series, points are returned in reverse time order.

When creating a time series, this field must contain exactly one point and the point's type must be the same as the value type of the associated metric. If the associated metric's descriptor must be auto-created, then the value type of the descriptor is determined by the point's type, which must be `BOOL`, `INT64`, `DOUBLE`, or `DISTRIBUTION`. 




**Returns**

  * (::Array<[::Google::Cloud::Bigquery::Migration::V2::Point](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-Point)>) — Required. The data points of this time series. When listing time series, points are returned in reverse time order.

When creating a time series, this field must contain exactly one point and the point's type must be the same as the value type of the associated metric. If the associated metric's descriptor must be auto-created, then the value type of the descriptor is determined by the point's type, which must be `BOOL`, `INT64`, `DOUBLE`, or `DISTRIBUTION`. 




### #value_type
    
    
    def value_type() -> ::Google::Api::MetricDescriptor::ValueType

**Returns**

  * ([::Google::Api::MetricDescriptor::ValueType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-ValueType)) — Required. The value type of the time series. 



### #value_type=
    
    
    def value_type=(value) -> ::Google::Api::MetricDescriptor::ValueType

**Parameter**

  * **value** ([::Google::Api::MetricDescriptor::ValueType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-ValueType)) — Required. The value type of the time series. 



**Returns**

  * ([::Google::Api::MetricDescriptor::ValueType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-ValueType)) — Required. The value type of the time series. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
