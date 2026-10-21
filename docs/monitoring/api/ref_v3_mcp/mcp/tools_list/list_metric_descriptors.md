---
url: https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors/
title: MCP Tools Reference: monitoring.googleapis.com \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:24.995130+00:00
---

# MCP Tools Reference: monitoring.googleapis.com  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  MCP Tools Reference: monitoring.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_metric_descriptors`

Use this as the primary tool to discover the types of metrics available in a Google Cloud project. This is a good first step to understanding what data is available for monitoring and building dashboards or alerts.

The following code sample shows how to use `curl` to call the `list_metric_descriptors` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://monitoring.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_metric_descriptors",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

The `ListMetricDescriptors` request.

### ListMetricDescriptorsRequest

JSON representation  
---  
      
    
    {
      "name": string,
      "filter": string,
      "pageSize": integer,
      "pageToken": string,
      "activeOnly": boolean
    }  
  
Fields  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
      
  
`filter` |  `string` Optional. If this field is empty, all custom and system-defined metric descriptors are returned. Otherwise, the [filter](https://cloud.google.com/monitoring/api/v3/filters) specifies which metric descriptors are to be returned. For example, the following filter matches all [custom metrics](https://cloud.google.com/monitoring/custom-metrics):
    
    
    metric.type = starts_with("custom.googleapis.com/")
      
  
`pageSize` |  `integer` Optional. A positive number that is the maximum number of results to return. The default and maximum value is 10,000. If a page_size <= 0 or > 10,000 is submitted, will instead return a maximum of 10,000 results.  
`pageToken` |  `string` Optional. If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
`activeOnly` |  `boolean` Optional. If true, only metrics and monitored resource types that have recent data (within roughly 25 hours) will be included in the response. - If a metric descriptor enumerates monitored resource types, only the monitored resource types for which the metric type has recent data will be included in the returned metric descriptor, and if none of them have recent data, the metric descriptor will not be returned. - If a metric descriptor does not enumerate the compatible monitored resource types, it will be returned only if the metric type has recent data for some monitored resource type. The returned descriptor will not enumerate any monitored resource types.  
  
## Output Schema

The `ListMetricDescriptors` response.

### ListMetricDescriptorsResponse

JSON representation  
---  
      
    
    {
      "metricDescriptors": [
        {
          object ([MetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.MetricDescriptor))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`metricDescriptors[]` |  `object (`[MetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.MetricDescriptor)`)` The metric descriptors that are available to the project and that match the value of `filter`, if present.  
`nextPageToken` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `page_token` in the next call to this method.  
  
### MetricDescriptor

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string,
      "labels": [
        {
          object ([LabelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.LabelDescriptor))
        }
      ],
      "metricKind": enum ([MetricKind](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.MetricKind)),
      "valueType": enum ([ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.ValueType)),
      "unit": string,
      "description": string,
      "displayName": string,
      "metadata": {
        object ([MetricDescriptorMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.MetricDescriptorMetadata))
      },
      "launchStage": enum ([LaunchStage](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.LaunchStage)),
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
      
  
`labels[]` |  `object (`[LabelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.LabelDescriptor)`)` The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.  
`metricKind` |  `enum (`[MetricKind](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.MetricKind)`)` Whether the metric records instantaneous values, changes to a value, etc. Some combinations of `metric_kind` and `value_type` might not be supported.  
`valueType` |  `enum (`[ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.ValueType)`)` Whether the measurement is an integer, a floating-point number, etc. Some combinations of `metric_kind` and `value_type` might not be supported.  
`unit` |  `string` The units in which the metric value is reported. It is only applicable if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values.Different systems might scale the values to be more easily displayed (so a value of `0.02kBy` _might_ be displayed as `20By`, and a value of `3523kBy` _might_ be displayed as `3.5MBy`). However, if the `unit` is `kBy`, then the value of the metric is always in thousands of bytes, no matter how it might be displayed.If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an `INT64 CUMULATIVE` metric whose `unit` is `s{CPU}` (or equivalently `1s{CPU}` or just `s`). If the job uses 12,005 CPU-seconds, then the value is written as `12005`.Alternatively, if you want a custom metric to record data in a more granular way, you can create a `DOUBLE CUMULATIVE` metric whose `unit` is `ks{CPU}`, and then write the value `12.005` (which is `12005/1000`), or use `Kis{CPU}` and write `11.723` (which is `12005/1024`).The supported units are a subset of [The Unified Code for Units of Measure](https://unitsofmeasure.org/ucum.html) standard:**Basic units (UNIT)**

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
`metadata` |  `object (`[MetricDescriptorMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.MetricDescriptorMetadata)`)` Optional. Metadata which can be used to guide usage of the metric.  
`launchStage` |  `enum (`[LaunchStage](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.LaunchStage)`)` Optional. The launch stage of the metric definition.  
`monitoredResourceTypes[]` |  `string` Read-only. If present, then a `[time series](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.TimeSeries)`, which is identified partially by a metric type and a `MonitoredResourceDescriptor`, that is associated with this metric type can only be associated with one of the monitored resource types listed here.  
  
### LabelDescriptor

JSON representation  
---  
      
    
    {
      "key": string,
      "valueType": enum ([ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.ValueType)),
      "description": string
    }  
  
Fields  
---  
`key` |  `string` The key for this label. The key must meet the following criteria:

  * Does not exceed 100 characters.
  * Matches the following regular expression: `[a-zA-Z][a-zA-Z0-9_]*`
    * The first character must be an upper- or lower-case letter.
    * The remaining characters must be letters, digits, or underscores.

  
`valueType` |  `enum (`[ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.ValueType)`)` The type of data that can be assigned to the label.  
`description` |  `string` A human-readable description for the label.  
  
### MetricDescriptorMetadata

JSON representation  
---  
      
    
    {
      "launchStage": enum ([LaunchStage](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.LaunchStage)),
      "samplePeriod": string,
      "ingestDelay": string,
      "timeSeriesResourceHierarchyLevel": [
        enum ([TimeSeriesResourceHierarchyLevel](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.TimeSeriesResourceHierarchyLevel))
      ]
    }  
  
Fields  
---  
`launchStage  
**(deprecated)**` |  `enum (`[LaunchStage](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.LaunchStage)`)` This item is deprecated!Deprecated. Must use the `MetricDescriptor.launch_stage` instead.  
`samplePeriod` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`ingestDelay` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`timeSeriesResourceHierarchyLevel[]` |  `enum (`[TimeSeriesResourceHierarchyLevel](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.TimeSeriesResourceHierarchyLevel)`)` The scope of the timeseries data of the metric.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### ValueType

Value types that can be used as label values.

Enums  
---  
`STRING` | A variable-length string, not to exceed 1,024 characters. This is the default value type.  
`BOOL` | Boolean; true or false.  
`INT64` | A 64-bit signed integer.  
  
### MetricKind

The kind of measurement. It describes how the data is reported. For information on setting the start time and end time based on the MetricKind, see `[TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.TimeInterval)`.

Enums  
---  
`METRIC_KIND_UNSPECIFIED` | Do not use this default value.  
`GAUGE` | An instantaneous measurement of a value.  
`DELTA` | The change in a value during a time interval.  
`CUMULATIVE` | A value accumulated over a time interval. Cumulative measurements in a time series should have the same start time and increasing end times, until an event resets the cumulative value to zero and sets a new start time for the following points.  
  
### ValueType

The value type of a metric.

Enums  
---  
`VALUE_TYPE_UNSPECIFIED` | Do not use this default value.  
`BOOL` | The value is a boolean. This value type can be used only if the metric kind is `GAUGE`.  
`INT64` | The value is a signed 64-bit integer.  
`DOUBLE` | The value is a double precision floating point number.  
`STRING` | The value is a text string. This value type can be used only if the metric kind is `GAUGE`.  
`DISTRIBUTION` | The value is a `[`Distribution`](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Distribution)`.  
`MONEY` | The value is money.  
  
### LaunchStage

The launch stage as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages).

Enums  
---  
`LAUNCH_STAGE_UNSPECIFIED` | Do not use this default value.  
`UNIMPLEMENTED` | The feature is not yet implemented. Users can not use it.  
`PRELAUNCH` | Prelaunch features are hidden from users and are only visible internally.  
`EARLY_ACCESS` | Early Access features are limited to a closed group of testers. To use these features, you must sign up in advance and sign a Trusted Tester agreement (which includes confidentiality provisions). These features may be unstable, changed in backward-incompatible ways, and are not guaranteed to be released.  
`ALPHA` | Alpha is a limited availability test for releases before they are cleared for widespread use. By Alpha, all significant design issues are resolved and we are in the process of verifying functionality. Alpha customers need to apply for access, agree to applicable terms, and have their projects allowlisted. Alpha releases don't have to be feature complete, no SLAs are provided, and there are no technical support obligations, but they will be far enough along that customers can actually use them in test environments or for limited-use tests -- just like they would in normal production cases.  
`BETA` | Beta is the point at which we are ready to open a release for any customer to use. There are no SLA or technical support obligations in a Beta release. Products will be complete from a feature perspective, but may have some open outstanding issues. Beta releases are suitable for limited production use cases.  
`GA` | GA features are open to all developers and are considered stable and fully qualified for production use.  
`DEPRECATED` | Deprecated features are scheduled to be shut down and removed. For more information, see the "Deprecation Policy" section of our [Terms of Service](https://cloud.google.com/terms/) and the [Google Cloud Platform Subject to the Deprecation Policy](https://cloud.google.com/terms/deprecation) documentation.  
  
### TimeSeriesResourceHierarchyLevel

The resource hierarchy level of the timeseries data of a metric.

Enums  
---  
`TIME_SERIES_RESOURCE_HIERARCHY_LEVEL_UNSPECIFIED` | Do not use this default value.  
`PROJECT` | Scopes a metric to a project.  
`ORGANIZATION` | Scopes a metric to an organization.  
`FOLDER` | Scopes a metric to a folder.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-04 UTC."],[],[]] 
