---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives
title: REST Resource: services.serviceLevelObjectives \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:16.788389+00:00
---

# REST Resource: services.serviceLevelObjectives  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  REST Resource: services.serviceLevelObjectives Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ServiceLevelObjective
    * JSON representation
  * ServiceLevelIndicator
    * JSON representation
  * BasicSli
    * JSON representation
  * AvailabilityCriteria
  * LatencyCriteria
    * JSON representation
  * RequestBasedSli
    * JSON representation
  * TimeSeriesRatio
    * JSON representation
  * DistributionCut
    * JSON representation
  * Range
    * JSON representation
  * WindowsBasedSli
    * JSON representation
  * PerformanceThreshold
    * JSON representation
  * MetricRange
    * JSON representation
  * CalendarPeriod
  * Methods



## Resource: ServiceLevelObjective

A Service-Level Objective (SLO) describes a level of desired good service. It consists of a service-level indicator (SLI), a performance goal, and a period over which the objective is to be evaluated against that goal. The SLO can use SLIs defined in a number of different manners. Typical SLOs might include "99% of requests in each rolling week have latency below 200 milliseconds" or "99.5% of requests in each calendar month return successfully."

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "serviceLevelIndicator": {
        object ([ServiceLevelIndicator](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#ServiceLevelIndicator))
      },
      "goal": number,
      "userLabels": {
        string: string,
        ...
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "rollingPeriod": string,
      "calendarPeriod": enum ([CalendarPeriod](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#CalendarPeriod))
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Resource name for this `ServiceLevelObjective`. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]/serviceLevelObjectives/[SLO_NAME]
      
  
`displayName` |  `string` Name used for UI elements listing this SLO.  
`serviceLevelIndicator` |  `object (`[ServiceLevelIndicator](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#ServiceLevelIndicator)`)` The definition of good service, used to measure and calculate the quality of the `Service`'s performance with respect to a single aspect of service quality.  
`goal` |  `number` The fraction of service that must be good in order for this objective to be met. `0 < goal <= 0.9999`.  
`userLabels` |  `map (key: string, value: string)` Labels which have been used to annotate the service-level objective. Label keys must start with a letter. Label keys and values may contain lowercase letters, numbers, underscores, and dashes. Label keys and values have a maximum length of 63 characters, and must be less than 128 bytes in size. Up to 64 label entries may be stored. For labels which do not have a semantic value, the empty string may be supplied for the label value.  
The time period over which the objective will be evaluated. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`rollingPeriod` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` A rolling time period, semantically "in the past `<rollingPeriod>`". Must be an integer multiple of 1 day no larger than 30 days.  
`calendarPeriod` |  `enum (`[CalendarPeriod](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#CalendarPeriod)`)` A calendar period, semantically "since the start of the current `<calendarPeriod>`". At this time, only `DAY`, `WEEK`, `FORTNIGHT`, and `MONTH` are supported.  
End of mutually exclusive fields.  
  
## ServiceLevelIndicator

A Service-Level Indicator (SLI) describes the "performance" of a service. For some services, the SLI is well-defined. In such cases, the SLI can be described easily by referencing the well-known SLI and providing the needed parameters. Alternatively, a "custom" SLI can be defined with a query to the underlying metric store. An SLI is defined to be `good_service / total_service` over any queried time interval. The value of performance always falls into the range `0 <= performance <= 1`. A custom SLI describes how to compute this ratio, whether this is by dividing values from a pair of time series, cutting a `Distribution` into good and bad counts, or counting time windows in which the service complies with a criterion. For separation of concerns, a single Service-Level Indicator measures performance for only one aspect of service quality, such as fraction of successful queries or fast-enough queries.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "basicSli": {
        object ([BasicSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#BasicSli))
      },
      "requestBased": {
        object ([RequestBasedSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#RequestBasedSli))
      },
      "windowsBased": {
        object ([WindowsBasedSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#WindowsBasedSli))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Service level indicators can be grouped by whether the "unit" of service being measured is based on counts of good requests or on counts of good time windows The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`basicSli` |  `object (`[BasicSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#BasicSli)`)` Basic SLI on a well-known service type.  
`requestBased` |  `object (`[RequestBasedSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#RequestBasedSli)`)` Request-based SLIs  
`windowsBased` |  `object (`[WindowsBasedSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#WindowsBasedSli)`)` Windows-based SLIs  
End of mutually exclusive fields.  
  
## BasicSli

An SLI measuring performance on a well-known service type. Performance will be computed on the basis of pre-defined metrics. The type of the `service_resource` determines the metrics to use and the `service_resource.labels` and `metricLabels` are used to construct a monitoring filter to filter that metric down to just the data relevant to this service.

JSON representation  
---  
      
    
    {
      "method": [
        string
      ],
      "location": [
        string
      ],
      "version": [
        string
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "availability": {
        object ([AvailabilityCriteria](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#AvailabilityCriteria))
      },
      "latency": {
        object ([LatencyCriteria](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#LatencyCriteria))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`method[]` |  `string` OPTIONAL: The set of RPCs to which this SLI is relevant. Telemetry from other methods will not be used to calculate performance for this SLI. If omitted, this SLI applies to all the Service's methods. For service types that don't support breaking down by method, setting this field will result in an error.  
`location[]` |  `string` OPTIONAL: The set of locations to which this SLI is relevant. Telemetry from other locations will not be used to calculate performance for this SLI. If omitted, this SLI applies to all locations in which the Service has activity. For service types that don't support breaking down by location, setting this field will result in an error.  
`version[]` |  `string` OPTIONAL: The set of API versions to which this SLI is relevant. Telemetry from other API versions will not be used to calculate performance for this SLI. If omitted, this SLI applies to all API versions. For service types that don't support breaking down by version, setting this field will result in an error.  
This SLI can be evaluated on the basis of availability or latency. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`availability` |  `object (`[AvailabilityCriteria](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#AvailabilityCriteria)`)` Good service is defined to be the count of requests made to this service that return successfully.  
`latency` |  `object (`[LatencyCriteria](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#LatencyCriteria)`)` Good service is defined to be the count of requests made to this service that are fast enough with respect to `latency.threshold`.  
End of mutually exclusive fields.  
  
## AvailabilityCriteria

This type has no fields.

Future parameters for the availability SLI.

## LatencyCriteria

Parameters for a latency threshold SLI.

JSON representation  
---  
      
    
    {
      "threshold": string
    }  
  
Fields  
---  
`threshold` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Good service is defined to be the count of requests made to this service that return in no more than `threshold`.  
  
## RequestBasedSli

Service Level Indicators for which atomic units of service are counted directly.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "goodTotalRatio": {
        object ([TimeSeriesRatio](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio))
      },
      "distributionCut": {
        object ([DistributionCut](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The means to compute a ratio of `good_service` to `total_service`. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`goodTotalRatio` |  `object (`[TimeSeriesRatio](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#TimeSeriesRatio)`)` `goodTotalRatio` is used when the ratio of `good_service` to `total_service` is computed from two `TimeSeries`.  
`distributionCut` |  `object (`[DistributionCut](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#DistributionCut)`)` `distributionCut` is used when `good_service` is a count of values aggregated in a `Distribution` that fall into a good range. The `total_service` is the total count of all values aggregated in the `Distribution`.  
End of mutually exclusive fields.  
  
## TimeSeriesRatio

A `TimeSeriesRatio` specifies two `TimeSeries` to use for computing the `good_service / total_service` ratio. The specified `TimeSeries` must have `ValueType = DOUBLE` or `ValueType = INT64` and must have `MetricKind = DELTA` or `MetricKind = CUMULATIVE`. The `TimeSeriesRatio` must specify exactly two of good, bad, and total, and the relationship `good_service + bad_service = total_service` will be assumed.

JSON representation  
---  
      
    
    {
      "goodServiceFilter": string,
      "badServiceFilter": string,
      "totalServiceFilter": string
    }  
  
Fields  
---  
`goodServiceFilter` |  `string` A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) specifying a `TimeSeries` quantifying good service provided. Must have `ValueType = DOUBLE` or `ValueType = INT64` and must have `MetricKind = DELTA` or `MetricKind = CUMULATIVE`.  
`badServiceFilter` |  `string` A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) specifying a `TimeSeries` quantifying bad service, either demanded service that was not provided or demanded service that was of inadequate quality. Must have `ValueType = DOUBLE` or `ValueType = INT64` and must have `MetricKind = DELTA` or `MetricKind = CUMULATIVE`.  
`totalServiceFilter` |  `string` A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) specifying a `TimeSeries` quantifying total demanded service. Must have `ValueType = DOUBLE` or `ValueType = INT64` and must have `MetricKind = DELTA` or `MetricKind = CUMULATIVE`.  
  
## DistributionCut

A `DistributionCut` defines a `TimeSeries` and thresholds used for measuring good service and total service. The `TimeSeries` must have `ValueType = DISTRIBUTION` and `MetricKind = DELTA` or `MetricKind = CUMULATIVE`. The computed `good_service` will be the estimated count of values in the `Distribution` that fall within the specified `min` and `max`.

JSON representation  
---  
      
    
    {
      "distributionFilter": string,
      "range": {
        object ([Range](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#Range))
      }
    }  
  
Fields  
---  
`distributionFilter` |  `string` A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) specifying a `TimeSeries` aggregating values. Must have `ValueType = DISTRIBUTION` and `MetricKind = DELTA` or `MetricKind = CUMULATIVE`.  
`range` |  `object (`[Range](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#Range)`)` Range of values considered "good." For a one-sided range, set one bound to an infinite value.  
  
## Range

Range of numerical values within `min` and `max`.

JSON representation  
---  
      
    
    {
      "min": number,
      "max": number
    }  
  
Fields  
---  
`min` |  `number` Range minimum.  
`max` |  `number` Range maximum.  
  
## WindowsBasedSli

A `WindowsBasedSli` defines `good_service` as the count of time windows for which the provided service was of good quality. Criteria for determining if service was good are embedded in the `window_criterion`.

JSON representation  
---  
      
    
    {
      "windowPeriod": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "goodBadMetricFilter": string,
      "goodTotalRatioThreshold": {
        object ([PerformanceThreshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#PerformanceThreshold))
      },
      "metricMeanInRange": {
        object ([MetricRange](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#MetricRange))
      },
      "metricSumInRange": {
        object ([MetricRange](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#MetricRange))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`windowPeriod` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Duration over which window quality is evaluated. Must be an integer fraction of a day and at least `60s`.  
The criterion to use for evaluating window goodness. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`goodBadMetricFilter` |  `string` A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) specifying a `TimeSeries` with `ValueType = BOOL`. The window is good if any `true` values appear in the window.  
`goodTotalRatioThreshold` |  `object (`[PerformanceThreshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#PerformanceThreshold)`)` A window is good if its `performance` is high enough.  
`metricMeanInRange` |  `object (`[MetricRange](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#MetricRange)`)` A window is good if the metric's value is in a good range, averaged across returned streams.  
`metricSumInRange` |  `object (`[MetricRange](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#MetricRange)`)` A window is good if the metric's value is in a good range, summed across returned streams.  
End of mutually exclusive fields.  
  
## PerformanceThreshold

A `PerformanceThreshold` is used when each window is good when that window has a sufficiently high `performance`.

JSON representation  
---  
      
    
    {
      "threshold": number,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "performance": {
        object ([RequestBasedSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#RequestBasedSli))
      },
      "basicSliPerformance": {
        object ([BasicSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#BasicSli))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`threshold` |  `number` If window `performance >= threshold`, the window is counted as good.  
The means, either a request-based SLI or a basic SLI, by which to compute performance over a window. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`performance` |  `object (`[RequestBasedSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#RequestBasedSli)`)` `RequestBasedSli` to evaluate to judge window quality.  
`basicSliPerformance` |  `object (`[BasicSli](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#BasicSli)`)` `BasicSli` to evaluate to judge window quality.  
End of mutually exclusive fields.  
  
## MetricRange

A `MetricRange` is used when each window is good when the value x of a single `TimeSeries` satisfies `range.min <= x <= range.max`. The provided `TimeSeries` must have `ValueType = INT64` or `ValueType = DOUBLE` and `MetricKind = GAUGE`.

JSON representation  
---  
      
    
    {
      "timeSeries": string,
      "range": {
        object ([Range](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#Range))
      }
    }  
  
Fields  
---  
`timeSeries` |  `string` A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) specifying the `TimeSeries` to use for evaluating window quality.  
`range` |  `object (`[Range](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives#Range)`)` Range of values considered "good." For a one-sided range, set one bound to an infinite value.  
  
## CalendarPeriod

A `CalendarPeriod` represents the abstract concept of a time period that has a canonical start. Grammatically, "the start of the current `CalendarPeriod`." All calendar times begin at midnight UTC.

Enums  
---  
`CALENDAR_PERIOD_UNSPECIFIED` | Undefined period, raises an error.  
`DAY` | A day.  
`WEEK` | A week. Weeks begin on Monday, following [ISO 8601](https://en.wikipedia.org/wiki/ISO_week_date).  
`FORTNIGHT` | A fortnight. The first calendar fortnight of the year begins at the start of week 1 according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_week_date).  
`MONTH` | A month.  
`QUARTER` | A quarter. Quarters start on dates 1-Jan, 1-Apr, 1-Jul, and 1-Oct of each year.  
`HALF` | A half-year. Half-years start on dates 1-Jan and 1-Jul.  
`YEAR` | A year.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/create)`

|  Create a `ServiceLevelObjective` for the given `Service`.  
  
### `[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/delete)`

|  Delete the given `ServiceLevelObjective`.  
  
### `[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/get)`

|  Get a `ServiceLevelObjective` by name.  
  
### `[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/list)`

|  List the `ServiceLevelObjective`s for the given `Service`.  
  
### `[patch](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/services.serviceLevelObjectives/patch)`

|  Update the given `ServiceLevelObjective`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-04 UTC."],[],[]] 
