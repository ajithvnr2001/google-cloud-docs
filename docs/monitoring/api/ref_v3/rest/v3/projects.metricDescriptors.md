---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors
title: REST Resource: projects.metricDescriptors \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:12.208955+00:00
---

# REST Resource: projects.metricDescriptors  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  REST Resource: projects.metricDescriptors Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MetricDescriptor
    * JSON representation
  * MetricKind
  * ValueType
  * MetricDescriptorMetadata
    * JSON representation
  * TimeSeriesResourceHierarchyLevel
  * Methods



## Resource: MetricDescriptor

Defines a metric type and its schema. Once a metric descriptor is created, deleting or altering it stops data collection and makes the metric type's existing data unusable.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string,
      "labels": [
        {
          object ([LabelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LabelDescriptor))
        }
      ],
      "metricKind": enum ([MetricKind](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind)),
      "valueType": enum ([ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#ValueType)),
      "unit": string,
      "description": string,
      "displayName": string,
      "metadata": {
        object ([MetricDescriptorMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptorMetadata))
      },
      "launchStage": enum ([LaunchStage](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LaunchStage)),
      "monitoredResourceTypes": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` The resource name of the metric descriptor.  
`type` |  `string` The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name `custom.googleapis.com` or `external.googleapis.com`. Metric types should use a natural hierarchical grouping. For example:
    
    
    "custom.googleapis.com/invoice/paid/amount"
    "external.googleapis.com/prometheus/up"
    "appengine.googleapis.com/http/server/response_latencies"
      
  
`labels[]` |  `object (`[LabelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LabelDescriptor)`)` The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.  
`metricKind` |  `enum (`[MetricKind](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind)`)` Whether the metric records instantaneous values, changes to a value, etc. Some combinations of `metricKind` and `valueType` might not be supported.  
`valueType` |  `enum (`[ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#ValueType)`)` Whether the measurement is an integer, a floating-point number, etc. Some combinations of `metricKind` and `valueType` might not be supported.  
`unit` |  `string` The units in which the metric value is reported. It is only applicable if the `valueType` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values.Different systems might scale the values to be more easily displayed (so a value of `0.02kBy` _might_ be displayed as `20By`, and a value of `3523kBy` _might_ be displayed as `3.5MBy`). However, if the `unit` is `kBy`, then the value of the metric is always in thousands of bytes, no matter how it might be displayed.If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an `INT64 CUMULATIVE` metric whose `unit` is `s{CPU}` (or equivalently `1s{CPU}` or just `s`). If the job uses 12,005 CPU-seconds, then the value is written as `12005`.Alternatively, if you want a custom metric to record data in a more granular way, you can create a `DOUBLE CUMULATIVE` metric whose `unit` is `ks{CPU}`, and then write the value `12.005` (which is `12005/1000`), or use `Kis{CPU}` and write `11.723` (which is `12005/1024`).The supported units are a subset of [The Unified Code for Units of Measure](https://unitsofmeasure.org/ucum.html) standard:**Basic units (UNIT)**

  * `bit` bit
  * `By` byte
  * `s` second
  * `min` minute
  * `h` hour
  * `d` day
  * `1` dimensionless

**Prefixes (PREFIX)**

  * `k` kilo (10^3)
  * `M` mega (10^6)
  * `G` giga (10^9)
  * `T` tera (10^12)
  * `P` peta (10^15)
  * `E` exa (10^18)
  * `Z` zetta (10^21)
  * `Y` yotta (10^24)
  * `m` milli (10^-3)
  * `u` micro (10^-6)
  * `n` nano (10^-9)
  * `p` pico (10^-12)
  * `f` femto (10^-15)
  * `a` atto (10^-18)
  * `z` zepto (10^-21)
  * `y` yocto (10^-24)
  * `Ki` kibi (2^10)
  * `Mi` mebi (2^20)
  * `Gi` gibi (2^30)
  * `Ti` tebi (2^40)
  * `Pi` pebi (2^50)

**Grammar** The grammar also includes these connectors:

  * `/` division or ratio (as an infix operator). For examples, `kBy/{email}` or `MiBy/10ms` (although you should almost never have `/s` in a metric `unit`; rates should always be computed at query time from the underlying cumulative or delta value).
  * `.` multiplication or composition (as an infix operator). For examples, `GBy.d` or `k{watt}.h`.

The grammar for a unit is as follows:
    
    
    Expression = Component { "." Component } { "/" Component } ;
    
    Component = ( [ PREFIX ] UNIT | "%" ) [ Annotation ]
              | Annotation
              | "1"
              ;
    
    Annotation = "{" NAME "}" ;
    

Notes:

  * `Annotation` is just a comment if it follows a `UNIT`. If the annotation is used alone, then the unit is equivalent to `1`. For examples, `{request}/s == 1/s`, `By{transmitted}/s == By/s`.
  * `NAME` is a sequence of non-blank printable ASCII characters not containing `{` or `}`.
  * `1` represents a unitary [dimensionless unit](https://en.wikipedia.org/wiki/Dimensionless_quantity) of 1, such as in `1/s`. It is typically used when none of the basic units are appropriate. For example, "new users per day" can be represented as `1/d` or `{new-users}/d` (and a metric value `5` would mean "5 new users). Alternatively, "thousands of page views per day" would be represented as `1000/d` or `k1/d` or `k{page_views}/d` (and a metric value of `5.3` would mean "5300 page views per day").
  * `%` represents dimensionless value of 1/100, and annotates values giving a percentage (so the metric values are typically in the range of 0..100, and a metric value `3` means "3 percent").
  * `10^2.%` indicates a metric contains a ratio, typically in the range 0..1, that will be multiplied by 100 and displayed as a percentage (so a metric value `0.03` means "3 percent").

  
`description` |  `string` A detailed description of the metric, which can be used in documentation.  
`displayName` |  `string` A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota.  
`metadata` |  `object (`[MetricDescriptorMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptorMetadata)`)` Optional. Metadata which can be used to guide usage of the metric.  
`launchStage` |  `enum (`[LaunchStage](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LaunchStage)`)` Optional. The launch stage of the metric definition.  
`monitoredResourceTypes[]` |  `string` Read-only. If present, then a `[time series](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries)`, which is identified partially by a metric type and a `[MonitoredResourceDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors#MonitoredResourceDescriptor)`, that is associated with this metric type can only be associated with one of the monitored resource types listed here.  
  
## MetricKind

The kind of measurement. It describes how the data is reported. For information on setting the start time and end time based on the MetricKind, see `[TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes#TimeInterval)`.

Enums  
---  
`METRIC_KIND_UNSPECIFIED` | Do not use this default value.  
`GAUGE` | An instantaneous measurement of a value.  
`DELTA` | The change in a value during a time interval.  
`CUMULATIVE` | A value accumulated over a time interval. Cumulative measurements in a time series should have the same start time and increasing end times, until an event resets the cumulative value to zero and sets a new start time for the following points.  
  
## ValueType

The value type of a metric.

Enums  
---  
`VALUE_TYPE_UNSPECIFIED` | Do not use this default value.  
`BOOL` | The value is a boolean. This value type can be used only if the metric kind is `GAUGE`.  
`INT64` | The value is a signed 64-bit integer.  
`DOUBLE` | The value is a double precision floating point number.  
`STRING` | The value is a text string. This value type can be used only if the metric kind is `GAUGE`.  
`DISTRIBUTION` | The value is a `[`Distribution`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Distribution)`.  
  
## MetricDescriptorMetadata

Additional annotations that can be used to guide the usage of a metric.

JSON representation  
---  
      
    
    {
      "launchStage": enum ([LaunchStage](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LaunchStage)),
      "samplePeriod": string,
      "ingestDelay": string,
      "timeSeriesResourceHierarchyLevel": [
        enum ([TimeSeriesResourceHierarchyLevel](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#TimeSeriesResourceHierarchyLevel))
      ]
    }  
  
Fields  
---  
`launchStage  
**(deprecated)**` |  `enum (`[LaunchStage](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/LaunchStage)`)` This item is deprecated!Deprecated. Must use the `[MetricDescriptor.launch_stage](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor.FIELDS.launch_stage)` instead.  
`samplePeriod` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period.  
`ingestDelay` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors.  
`timeSeriesResourceHierarchyLevel[]` |  `enum (`[TimeSeriesResourceHierarchyLevel](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#TimeSeriesResourceHierarchyLevel)`)` The scope of the timeseries data of the metric.  
  
## TimeSeriesResourceHierarchyLevel

The resource hierarchy level of the timeseries data of a metric.

Enums  
---  
`TIME_SERIES_RESOURCE_HIERARCHY_LEVEL_UNSPECIFIED` | Do not use this default value.  
`PROJECT` | Scopes a metric to a project.  
`ORGANIZATION` | Scopes a metric to an organization.  
`FOLDER` | Scopes a metric to a folder.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/create)`

|  Creates a new metric descriptor.  
  
### `[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/delete)`

|  Deletes a metric descriptor.  
  
### `[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/get)`

|  Gets a single metric descriptor.  
  
### `[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/list)`

|  Lists metric descriptors that match a filter.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
