---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-MetricDescriptorMetadata/
title: BigQuery Migration V2 API - Class Google::Api::MetricDescriptor::MetricDescriptorMetadata (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:13.027207+00:00
---

# BigQuery Migration V2 API - Class Google::Api::MetricDescriptor::MetricDescriptorMetadata (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-MetricDescriptorMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Api::MetricDescriptor::MetricDescriptorMetadata (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Api::MetricDescriptor::MetricDescriptorMetadata.

Additional annotations that can be used to guide the usage of a metric.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #ingest_delay
    
    
    def ingest_delay() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Duration)) — The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors. 



### #ingest_delay=
    
    
    def ingest_delay=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Duration)) — The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Duration)) — The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors. 



### #launch_stage
    
    
    def launch_stage() -> ::Google::Api::LaunchStage

**Returns**

  * ([::Google::Api::LaunchStage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-LaunchStage)) — Deprecated. Must use the [MetricDescriptor.launch_stage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor#Google__Api__MetricDescriptor_launch_stage_instance_ "Google::Api::MetricDescriptor#launch_stage \(method\)") instead. 



### #launch_stage=
    
    
    def launch_stage=(value) -> ::Google::Api::LaunchStage

**Parameter**

  * **value** ([::Google::Api::LaunchStage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-LaunchStage)) — Deprecated. Must use the [MetricDescriptor.launch_stage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor#Google__Api__MetricDescriptor_launch_stage_instance_ "Google::Api::MetricDescriptor#launch_stage \(method\)") instead. 



**Returns**

  * ([::Google::Api::LaunchStage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-LaunchStage)) — Deprecated. Must use the [MetricDescriptor.launch_stage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor#Google__Api__MetricDescriptor_launch_stage_instance_ "Google::Api::MetricDescriptor#launch_stage \(method\)") instead. 



### #sample_period
    
    
    def sample_period() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Duration)) — The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period. 



### #sample_period=
    
    
    def sample_period=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Duration)) — The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Duration)) — The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period. 



### #time_series_resource_hierarchy_level
    
    
    def time_series_resource_hierarchy_level() -> ::Array<::Google::Api::MetricDescriptor::MetricDescriptorMetadata::TimeSeriesResourceHierarchyLevel>

**Returns**

  * (::Array<[::Google::Api::MetricDescriptor::MetricDescriptorMetadata::TimeSeriesResourceHierarchyLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-MetricDescriptorMetadata-TimeSeriesResourceHierarchyLevel)>) — The scope of the timeseries data of the metric. 



### #time_series_resource_hierarchy_level=
    
    
    def time_series_resource_hierarchy_level=(value) -> ::Array<::Google::Api::MetricDescriptor::MetricDescriptorMetadata::TimeSeriesResourceHierarchyLevel>

**Parameter**

  * **value** (::Array<[::Google::Api::MetricDescriptor::MetricDescriptorMetadata::TimeSeriesResourceHierarchyLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-MetricDescriptorMetadata-TimeSeriesResourceHierarchyLevel)>) — The scope of the timeseries data of the metric. 



**Returns**

  * (::Array<[::Google::Api::MetricDescriptor::MetricDescriptorMetadata::TimeSeriesResourceHierarchyLevel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-MetricDescriptorMetadata-TimeSeriesResourceHierarchyLevel)>) — The scope of the timeseries data of the metric. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
