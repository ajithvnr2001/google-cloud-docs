---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor/
title: BigQuery Migration V2 API - Class Google::Api::MetricDescriptor (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:27:57.480455+00:00
---

# BigQuery Migration V2 API - Class Google::Api::MetricDescriptor (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Api::MetricDescriptor (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Api::MetricDescriptor.

Defines a metric type and its schema. Once a metric descriptor is created, deleting or altering it stops data collection and makes the metric type's existing data unusable.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — A detailed description of the metric, which can be used in documentation. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — A detailed description of the metric, which can be used in documentation. 



**Returns**

  * (::String) — A detailed description of the metric, which can be used in documentation. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota. 



**Returns**

  * (::String) — A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota. 



### #labels
    
    
    def labels() -> ::Array<::Google::Api::LabelDescriptor>

**Returns**

  * (::Array<[::Google::Api::LabelDescriptor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-LabelDescriptor)>) — The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed. 



### #labels=
    
    
    def labels=(value) -> ::Array<::Google::Api::LabelDescriptor>

**Parameter**

  * **value** (::Array<[::Google::Api::LabelDescriptor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-LabelDescriptor)>) — The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed. 



**Returns**

  * (::Array<[::Google::Api::LabelDescriptor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-LabelDescriptor)>) — The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed. 



### #launch_stage
    
    
    def launch_stage() -> ::Google::Api::LaunchStage

**Returns**

  * ([::Google::Api::LaunchStage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-LaunchStage)) — Optional. The launch stage of the metric definition. 



### #launch_stage=
    
    
    def launch_stage=(value) -> ::Google::Api::LaunchStage

**Parameter**

  * **value** ([::Google::Api::LaunchStage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-LaunchStage)) — Optional. The launch stage of the metric definition. 



**Returns**

  * ([::Google::Api::LaunchStage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-LaunchStage)) — Optional. The launch stage of the metric definition. 



### #metadata
    
    
    def metadata() -> ::Google::Api::MetricDescriptor::MetricDescriptorMetadata

**Returns**

  * ([::Google::Api::MetricDescriptor::MetricDescriptorMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-MetricDescriptorMetadata)) — Optional. Metadata which can be used to guide usage of the metric. 



### #metadata=
    
    
    def metadata=(value) -> ::Google::Api::MetricDescriptor::MetricDescriptorMetadata

**Parameter**

  * **value** ([::Google::Api::MetricDescriptor::MetricDescriptorMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-MetricDescriptorMetadata)) — Optional. Metadata which can be used to guide usage of the metric. 



**Returns**

  * ([::Google::Api::MetricDescriptor::MetricDescriptorMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-MetricDescriptorMetadata)) — Optional. Metadata which can be used to guide usage of the metric. 



### #metric_kind
    
    
    def metric_kind() -> ::Google::Api::MetricDescriptor::MetricKind

**Returns**

  * ([::Google::Api::MetricDescriptor::MetricKind](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-MetricKind)) — Whether the metric records instantaneous values, changes to a value, etc. Some combinations of `metric_kind` and `value_type` might not be supported. 



### #metric_kind=
    
    
    def metric_kind=(value) -> ::Google::Api::MetricDescriptor::MetricKind

**Parameter**

  * **value** ([::Google::Api::MetricDescriptor::MetricKind](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-MetricKind)) — Whether the metric records instantaneous values, changes to a value, etc. Some combinations of `metric_kind` and `value_type` might not be supported. 



**Returns**

  * ([::Google::Api::MetricDescriptor::MetricKind](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-MetricKind)) — Whether the metric records instantaneous values, changes to a value, etc. Some combinations of `metric_kind` and `value_type` might not be supported. 



### #monitored_resource_types
    
    
    def monitored_resource_types() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Read-only. If present, then a [time series][google.monitoring.v3.TimeSeries], which is identified partially by a metric type and a [MonitoredResourceDescriptor][google.api.MonitoredResourceDescriptor], that is associated with this metric type can only be associated with one of the monitored resource types listed here. 



### #monitored_resource_types=
    
    
    def monitored_resource_types=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Read-only. If present, then a [time series][google.monitoring.v3.TimeSeries], which is identified partially by a metric type and a [MonitoredResourceDescriptor][google.api.MonitoredResourceDescriptor], that is associated with this metric type can only be associated with one of the monitored resource types listed here. 



**Returns**

  * (::Array<::String>) — Read-only. If present, then a [time series][google.monitoring.v3.TimeSeries], which is identified partially by a metric type and a [MonitoredResourceDescriptor][google.api.MonitoredResourceDescriptor], that is associated with this metric type can only be associated with one of the monitored resource types listed here. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The resource name of the metric descriptor. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The resource name of the metric descriptor. 



**Returns**

  * (::String) — The resource name of the metric descriptor. 



### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — 

The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name `custom.googleapis.com` or `external.googleapis.com`. Metric types should use a natural hierarchical grouping. For example:
        
        "custom.googleapis.com/invoice/paid/amount"
        "external.googleapis.com/prometheus/up"
        "appengine.googleapis.com/http/server/response_latencies"
        




### #type=
    
    
    def type=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name `custom.googleapis.com` or `external.googleapis.com`. Metric types should use a natural hierarchical grouping. For example:
        
        "custom.googleapis.com/invoice/paid/amount"
        "external.googleapis.com/prometheus/up"
        "appengine.googleapis.com/http/server/response_latencies"
        




**Returns**

  * (::String) — 

The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name `custom.googleapis.com` or `external.googleapis.com`. Metric types should use a natural hierarchical grouping. For example:
        
        "custom.googleapis.com/invoice/paid/amount"
        "external.googleapis.com/prometheus/up"
        "appengine.googleapis.com/http/server/response_latencies"
        




### #unit
    
    
    def unit() -> ::String

**Returns**

  * (::String) — 

The units in which the metric value is reported. It is only applicable if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values.

Different systems might scale the values to be more easily displayed (so a value of `0.02kBy` _might_ be displayed as `20By`, and a value of `3523kBy` _might_ be displayed as `3.5MBy`). However, if the `unit` is `kBy`, then the value of the metric is always in thousands of bytes, no matter how it might be displayed.

If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an `INT64 CUMULATIVE` metric whose `unit` is `s{CPU}` (or equivalently `1s{CPU}` or just `s`). If the job uses 12,005 CPU-seconds, then the value is written as `12005`.

Alternatively, if you want a custom metric to record data in a more granular way, you can create a `DOUBLE CUMULATIVE` metric whose `unit` is `ks{CPU}`, and then write the value `12.005` (which is `12005/1000`), or use `Kis{CPU}` and write `11.723` (which is `12005/1024`).

The supported units are a subset of [The Unified Code for Units of Measure](https://unitsofmeasure.org/ucum.html) standard:

**Basic units (UNIT)**

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

**Grammar**

The grammar also includes these connectors:

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



### #unit=
    
    
    def unit=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The units in which the metric value is reported. It is only applicable if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values.

Different systems might scale the values to be more easily displayed (so a value of `0.02kBy` _might_ be displayed as `20By`, and a value of `3523kBy` _might_ be displayed as `3.5MBy`). However, if the `unit` is `kBy`, then the value of the metric is always in thousands of bytes, no matter how it might be displayed.

If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an `INT64 CUMULATIVE` metric whose `unit` is `s{CPU}` (or equivalently `1s{CPU}` or just `s`). If the job uses 12,005 CPU-seconds, then the value is written as `12005`.

Alternatively, if you want a custom metric to record data in a more granular way, you can create a `DOUBLE CUMULATIVE` metric whose `unit` is `ks{CPU}`, and then write the value `12.005` (which is `12005/1000`), or use `Kis{CPU}` and write `11.723` (which is `12005/1024`).

The supported units are a subset of [The Unified Code for Units of Measure](https://unitsofmeasure.org/ucum.html) standard:

**Basic units (UNIT)**

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

**Grammar**

The grammar also includes these connectors:

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



**Returns**

  * (::String) — 

The units in which the metric value is reported. It is only applicable if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values.

Different systems might scale the values to be more easily displayed (so a value of `0.02kBy` _might_ be displayed as `20By`, and a value of `3523kBy` _might_ be displayed as `3.5MBy`). However, if the `unit` is `kBy`, then the value of the metric is always in thousands of bytes, no matter how it might be displayed.

If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an `INT64 CUMULATIVE` metric whose `unit` is `s{CPU}` (or equivalently `1s{CPU}` or just `s`). If the job uses 12,005 CPU-seconds, then the value is written as `12005`.

Alternatively, if you want a custom metric to record data in a more granular way, you can create a `DOUBLE CUMULATIVE` metric whose `unit` is `ks{CPU}`, and then write the value `12.005` (which is `12005/1000`), or use `Kis{CPU}` and write `11.723` (which is `12005/1024`).

The supported units are a subset of [The Unified Code for Units of Measure](https://unitsofmeasure.org/ucum.html) standard:

**Basic units (UNIT)**

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

**Grammar**

The grammar also includes these connectors:

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



### #value_type
    
    
    def value_type() -> ::Google::Api::MetricDescriptor::ValueType

**Returns**

  * ([::Google::Api::MetricDescriptor::ValueType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-ValueType)) — Whether the measurement is an integer, a floating-point number, etc. Some combinations of `metric_kind` and `value_type` might not be supported. 



### #value_type=
    
    
    def value_type=(value) -> ::Google::Api::MetricDescriptor::ValueType

**Parameter**

  * **value** ([::Google::Api::MetricDescriptor::ValueType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-ValueType)) — Whether the measurement is an integer, a floating-point number, etc. Some combinations of `metric_kind` and `value_type` might not be supported. 



**Returns**

  * ([::Google::Api::MetricDescriptor::ValueType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-MetricDescriptor-ValueType)) — Whether the measurement is an integer, a floating-point number, etc. Some combinations of `metric_kind` and `value_type` might not be supported. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
