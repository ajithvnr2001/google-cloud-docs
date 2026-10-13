---
url: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.MetricDescriptor.MetricDescriptorMetadata
title: Google API Common Protos Client - Class MetricDescriptorMetadata (4.14.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:32.026028+00:00
---

# Google API Common Protos Client - Class MetricDescriptorMetadata (4.14.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.MetricDescriptor.MetricDescriptorMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Common Protos Client - Class MetricDescriptorMetadata (4.14.3) Stay organized with collections  Save and categorize content based on your preferences. 

4.14.3 (latest)  4.14.1  4.13.0  4.12.5  4.11.0  4.10.0  4.9.0  4.8.3 

Reference documentation and code samples for the Google API Common Protos Client class MetricDescriptorMetadata.

Additional annotations that can be used to guide the usage of a metric.

Generated from protobuf message `google.api.MetricDescriptor.MetricDescriptorMetadata`

## Namespace

Google \ Api \ MetricDescriptor

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ launch_stage` |  `int`   
Deprecated. Must use the [MetricDescriptor.launch_stage](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.MetricDescriptor#_Google_Api_MetricDescriptor__getLaunchStage__) instead.  
`↳ sample_period` |  `[Google\Protobuf\Duration](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Duration.html)`   
The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period.  
`↳ ingest_delay` |  `[Google\Protobuf\Duration](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Duration.html)`   
The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors.  
`↳ time_series_resource_hierarchy_level` |  `int[]`   
The scope of the timeseries data of the metric.  
  
### getLaunchStage

Deprecated. Must use the [MetricDescriptor.launch_stage](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.MetricDescriptor#_Google_Api_MetricDescriptor__getLaunchStage__) instead.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [LaunchStage](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.LaunchStage).  
  
### setLaunchStage

Deprecated. Must use the [MetricDescriptor.launch_stage](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.MetricDescriptor#_Google_Api_MetricDescriptor__getLaunchStage__) instead.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [LaunchStage](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.LaunchStage).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSamplePeriod

The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\Duration](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Duration.html)|null` |   
  
### hasSamplePeriod

### clearSamplePeriod

### setSamplePeriod

The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Protobuf\Duration](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Duration.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getIngestDelay

The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\Duration](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Duration.html)|null` |   
  
### hasIngestDelay

### clearIngestDelay

### setIngestDelay

The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Protobuf\Duration](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Duration.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTimeSeriesResourceHierarchyLevel

The scope of the timeseries data of the metric.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField.html)<int>` |   
  
### setTimeSeriesResourceHierarchyLevel

The scope of the timeseries data of the metric.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
