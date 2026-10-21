---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies
title: REST Resource: projects.alertPolicies \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:42:55.259131+00:00
---

# REST Resource: projects.alertPolicies  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  REST Resource: projects.alertPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AlertPolicy
    * JSON representation
  * Documentation
    * JSON representation
  * Link
    * JSON representation
  * Condition
    * JSON representation
  * MetricThreshold
    * JSON representation
  * Aggregation
    * JSON representation
  * Aligner
  * Reducer
  * ForecastOptions
    * JSON representation
  * ComparisonType
  * Trigger
    * JSON representation
  * EvaluationMissingData
  * MetricAbsence
    * JSON representation
  * LogMatch
    * JSON representation
  * MonitoringQueryLanguageCondition
    * JSON representation
  * PrometheusQueryLanguageCondition
    * JSON representation
  * SqlCondition
    * JSON representation
  * Minutes
    * JSON representation
  * Hourly
    * JSON representation
  * Daily
    * JSON representation
  * TimeOfDay
    * JSON representation
  * RowCountTest
    * JSON representation
  * BooleanTest
    * JSON representation
  * ConditionCombinerType
  * AlertStrategy
    * JSON representation
  * NotificationRateLimit
    * JSON representation
  * NotificationPrompt
  * NotificationChannelStrategy
    * JSON representation
  * Methods



## Resource: AlertPolicy

A description of the conditions under which some aspect of your system is considered to be "unhealthy" and the ways to notify people or services about this state. For an overview of alerting policies, see [Introduction to Alerting](https://cloud.google.com/monitoring/alerts/).

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "documentation": {
        object ([Documentation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Documentation))
      },
      "userLabels": {
        string: string,
        ...
      },
      "conditions": [
        {
          object ([Condition](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Condition))
        }
      ],
      "combiner": enum ([ConditionCombinerType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#ConditionCombinerType)),
      "enabled": boolean,
      "validity": {
        object ([Status](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/Status))
      },
      "notificationChannels": [
        string
      ],
      "creationRecord": {
        object ([MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/MutationRecord))
      },
      "mutationRecord": {
        object ([MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/MutationRecord))
      },
      "alertStrategy": {
        object ([AlertStrategy](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertStrategy))
      },
      "severity": enum ([Severity](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/Severity))
    }  
  
Fields  
---  
`name` |  `string` Identifier. Required if the policy exists. The resource name for this policy. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[ALERT_POLICY_ID]
    

`[ALERT_POLICY_ID]` is assigned by Cloud Monitoring when the policy is created. When calling the `[alertPolicies.create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create#google.monitoring.v3.AlertPolicyService.CreateAlertPolicy)` method, do not include the `name` field in the alerting policy passed as part of the request.  
`displayName` |  `string` A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion, don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode characters.The convention for the displayName of a PrometheusQueryLanguageCondition is "{rule group name}/{alert name}", where the {rule group name} and {alert name} should be taken from the corresponding Prometheus configuration file. This convention is not enforced. In any case the displayName is not a unique key of the AlertPolicy.  
`documentation` |  `object (`[Documentation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Documentation)`)` Documentation that is included with notifications and incidents related to this policy. Best practice is for the documentation to include information to help responders understand, mitigate, escalate, and correct the underlying problems detected by the alerting policy. Notification channels that have limited capacity might not show this documentation.  
`userLabels` |  `map (key: string, value: string)` User-supplied key/value data to be used for organizing and identifying the `AlertPolicy` objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.Note that Prometheus {alert name} is a [valid Prometheus label names](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels), whereas Prometheus {rule group} is an unrestricted UTF-8 string. This means that they cannot be stored as-is in user labels, because they may contain characters that are not allowed in user-label values.  
`conditions[]` |  `object (`[Condition](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Condition)`)` A list of conditions for the policy. The conditions are combined by AND or OR according to the `combiner` field. If the combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions. If `conditionTimeSeriesQueryLanguage` is present, it must be the only `condition`. If `conditionMonitoringQueryLanguage` is present, it must be the only `condition`.  
`combiner` |  `enum (`[ConditionCombinerType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#ConditionCombinerType)`)` How to combine the results of multiple conditions to determine if an incident should be opened. If `conditionTimeSeriesQueryLanguage` is present, this must be `COMBINE_UNSPECIFIED`.  
`enabled` |  `boolean` Whether or not the policy is enabled. On write, the default interpretation if unset is that the policy is enabled. On read, clients should not make any assumption about the state if it has not been populated. The field should always be populated on List and Get operations, unless a field projection has been specified that strips it out.  
`validity` |  `object (`[Status](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/Status)`)` Read-only description of how the alerting policy is invalid. This field is only set when the alerting policy is invalid. An invalid alerting policy will not generate incidents.  
`notificationChannels[]` |  `string` Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when new violations occur on an already opened incident. Each element of this array corresponds to the `name` field in each of the `[`NotificationChannel`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels#NotificationChannel)` objects that are returned from the `[`notificationChannels.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/list#google.monitoring.v3.NotificationChannelService.ListNotificationChannels)` method. The format of the entries in this field is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID]
      
  
`creationRecord` |  `object (`[MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/MutationRecord)`)` A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be ignored.  
`mutationRecord` |  `object (`[MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/MutationRecord)`)` A read-only record of the most recent change to the alerting policy. If provided in a call to create or update, this field will be ignored.  
`alertStrategy` |  `object (`[AlertStrategy](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertStrategy)`)` Control over how this alerting policy's notification channels are notified.  
`severity` |  `enum (`[Severity](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/Severity)`)` Optional. The severity of an alerting policy indicates how important incidents generated by that policy are. The severity level will be displayed on the Incident detail page and in notifications.  
  
## Documentation

Documentation that is included in the notifications and incidents pertaining to this policy.

JSON representation  
---  
      
    
    {
      "content": string,
      "mimeType": string,
      "subject": string,
      "links": [
        {
          object ([Link](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Link))
        }
      ]
    }  
  
Fields  
---  
`content` |  `string` The body of the documentation, interpreted according to `mimeType`. The content may not exceed 8,192 Unicode characters and may not exceed more than 10,240 bytes when encoded in UTF-8 format, whichever is smaller. This text can be [templatized by using variables](https://cloud.google.com/monitoring/alerts/doc-variables#doc-vars).  
`mimeType` |  `string` The format of the `content` field. Presently, only the value `"text/markdown"` is supported. See [Markdown](https://en.wikipedia.org/wiki/Markdown) for more information.  
`subject` |  `string` Optional. The subject line of the notification. The subject line may not exceed 10,240 bytes. In notifications generated by this policy, the contents of the subject line after variable expansion will be truncated to 255 bytes or shorter at the latest UTF-8 character boundary. The 255-byte limit is recommended by [this thread](https://stackoverflow.com/questions/1592291/what-is-the-email-subject-length-limit). It is both the limit imposed by some third-party ticketing products and it is common to define textual fields in databases as VARCHAR(255).The contents of the subject line can be [templatized by using variables](https://cloud.google.com/monitoring/alerts/doc-variables#doc-vars). If this field is missing or empty, a default subject line will be generated.  
`links[]` |  `object (`[Link](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Link)`)` Optional. Links to content such as playbooks, repositories, and other resources. This field can contain up to 3 entries.  
  
## Link

Links to content such as playbooks, repositories, and other resources.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "url": string
    }  
  
Fields  
---  
`displayName` |  `string` A short display name for the link. The display name must not be empty or exceed 63 characters. Example: "playbook".  
`url` |  `string` The url of a webpage. A url can be templatized by using variables in the path or the query parameters. The total length of a URL should not exceed 2083 characters before and after variable expansion. Example: "https://my_domain.com/playbook?name=${resource.name}"  
  
## Condition

A condition is a true/false test that determines when an alerting policy should open an incident. If a condition evaluates to true, it signifies that something is wrong.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "conditionThreshold": {
        object ([MetricThreshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MetricThreshold))
      },
      "conditionAbsent": {
        object ([MetricAbsence](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MetricAbsence))
      },
      "conditionMatchedLog": {
        object ([LogMatch](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#LogMatch))
      },
      "conditionMonitoringQueryLanguage": {
        object ([MonitoringQueryLanguageCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MonitoringQueryLanguageCondition))
      },
      "conditionPrometheusQueryLanguage": {
        object ([PrometheusQueryLanguageCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#PrometheusQueryLanguageCondition))
      },
      "conditionSql": {
        object ([SqlCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#SqlCondition))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Required if the condition exists. The unique resource name for this condition. Its format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[POLICY_ID]/conditions/[CONDITION_ID]
    

`[CONDITION_ID]` is assigned by Cloud Monitoring when the condition is created as part of a new or updated alerting policy.When calling the `[alertPolicies.create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create#google.monitoring.v3.AlertPolicyService.CreateAlertPolicy)` method, do not include the `name` field in the conditions of the requested alerting policy. Cloud Monitoring creates the condition identifiers and includes them in the new policy.When calling the `[alertPolicies.update](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/patch#google.monitoring.v3.AlertPolicyService.UpdateAlertPolicy)` method to update a policy, including a condition `name` causes the existing condition to be updated. Conditions without names are added to the updated policy. Existing conditions are deleted if they are not updated.Best practice is to preserve `[CONDITION_ID]` if you make only small changes, such as those to condition thresholds, durations, or trigger values. Otherwise, treat the change as a new condition and let the existing condition be deleted.  
`displayName` |  `string` A short name or phrase used to identify the condition in dashboards, notifications, and incidents. To avoid confusion, don't use the same display name for multiple conditions in the same policy.  
Only one of the following condition types will be specified. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`conditionThreshold` |  `object (`[MetricThreshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MetricThreshold)`)` A condition that compares a time series against a threshold.  
`conditionAbsent` |  `object (`[MetricAbsence](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MetricAbsence)`)` A condition that checks that a time series continues to receive new data points.  
`conditionMatchedLog` |  `object (`[LogMatch](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#LogMatch)`)` A condition that checks for log messages matching given constraints. If set, no other conditions can be present.  
`conditionMonitoringQueryLanguage` |  `object (`[MonitoringQueryLanguageCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#MonitoringQueryLanguageCondition)`)` A condition that uses the Monitoring Query Language to define alerts.  
`conditionPrometheusQueryLanguage` |  `object (`[PrometheusQueryLanguageCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#PrometheusQueryLanguageCondition)`)` A condition that uses the Prometheus query language to define alerts.  
`conditionSql` |  `object (`[SqlCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#SqlCondition)`)` A condition that periodically evaluates a SQL query result.  
End of mutually exclusive fields.  
  
## MetricThreshold

A condition type that compares a collection of time series against a threshold.

JSON representation  
---  
      
    
    {
      "filter": string,
      "aggregations": [
        {
          object ([Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Aggregation))
        }
      ],
      "denominatorFilter": string,
      "denominatorAggregations": [
        {
          object ([Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Aggregation))
        }
      ],
      "forecastOptions": {
        object ([ForecastOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#ForecastOptions))
      },
      "comparison": enum ([ComparisonType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#ComparisonType)),
      "thresholdValue": number,
      "duration": string,
      "trigger": {
        object ([Trigger](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Trigger))
      },
      "evaluationMissingData": enum ([EvaluationMissingData](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#EvaluationMissingData))
    }  
  
Fields  
---  
`filter` |  `string` Required. A [filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the [`timeSeries.list` request](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) (that call is useful to verify the time series that will be retrieved / processed). The filter must specify the metric type and the resource type. Optionally, it can specify resource labels and metric labels. This field must not exceed 2048 Unicode characters in length.  
`aggregations[]` |  `object (`[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Aggregation)`)` Specifies the alignment of data points in individual time series as well as how to combine the retrieved time series together (such as when aggregating multiple streams on each resource to a single stream for each resource or when aggregating streams across all members of a group of resources). Multiple aggregations are applied in the order specified.This field is similar to the one in the [`timeSeries.list` request](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list). It is advisable to use the `timeSeries.list` method when debugging this field.  
`denominatorFilter` |  `string` A [filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies a time series that should be used as the denominator of a ratio that will be compared with the threshold. If a `denominatorFilter` is specified, the time series specified by the `filter` field will be used as the numerator.The filter must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length.  
`denominatorAggregations[]` |  `object (`[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Aggregation)`)` Specifies the alignment of data points in individual time series selected by `denominatorFilter` as well as how to combine the retrieved time series together (such as when aggregating multiple streams on each resource to a single stream for each resource or when aggregating streams across all members of a group of resources).When computing ratios, the `aggregations` and `denominatorAggregations` fields must use the same alignment period and produce time series that have the same periodicity and labels.  
`forecastOptions` |  `object (`[ForecastOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#ForecastOptions)`)` When this field is present, the `MetricThreshold` condition forecasts whether the time series is predicted to violate the threshold within the `forecastHorizon`. When this field is not set, the `MetricThreshold` tests the current value of the timeseries against the threshold.  
`comparison` |  `enum (`[ComparisonType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#ComparisonType)`)` The comparison to apply between the time series (indicated by `filter` and `aggregation`) and the threshold (indicated by `thresholdValue`). The comparison is applied on each time series, with the time series on the left-hand side and the threshold on the right-hand side.Only `COMPARISON_LT` and `COMPARISON_GT` are supported currently.  
`thresholdValue` |  `number` A value against which to compare the time series.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the `aggregations` field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly.  
`trigger` |  `object (`[Trigger](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Trigger)`)` The number/percent of time series for which the comparison must hold in order for the condition to trigger. If unspecified, then the condition will trigger if the comparison is true for any of the time series that have been identified by `filter` and `aggregations`, or by the ratio, if `denominatorFilter` and `denominatorAggregations` are specified.  
`evaluationMissingData` |  `enum (`[EvaluationMissingData](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#EvaluationMissingData)`)` A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. To use this control, the value of the `duration` field must be greater than or equal to 60 seconds.  
  
## Aggregation

Describes how to combine multiple time series to provide a different view of the data. Aggregation of time series is done in two steps. First, each time series in the set is _aligned_ to the same time interval boundaries, then the set of time series is optionally _reduced_ in number.

Alignment consists of applying the `perSeriesAligner` operation to each time series after its data has been divided into regular `alignmentPeriod` time intervals. This process takes _all_ of the data points in an alignment period, applies a mathematical transformation such as averaging, minimum, maximum, delta, etc., and converts them into a single data point per period.

Reduction is when the aligned and transformed time series can optionally be combined, reducing the number of time series through similar mathematical transformations. Reduction involves applying a `crossSeriesReducer` to all the time series, optionally sorting the time series into subsets with `groupByFields`, and applying the reducer to each subset.

The raw time series data can contain a huge amount of information from multiple sources. Alignment and reduction transforms this mass of data into a more manageable and representative collection of data, for example "the 95% latency across the average of all tasks in a cluster". This representative data can be more easily graphed and comprehended, and the individual time series data is still available for later drilldown. For more details, see [Filtering and aggregation](https://cloud.google.com/monitoring/api/v3/aggregation).

JSON representation  
---  
      
    
    {
      "alignmentPeriod": string,
      "perSeriesAligner": enum ([Aligner](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Aligner)),
      "crossSeriesReducer": enum ([Reducer](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Reducer)),
      "groupByFields": [
        string
      ]
    }  
  
Fields  
---  
`alignmentPeriod` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The `alignmentPeriod` specifies a time interval, in seconds, that is used to divide the data in all the `[time series](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries)` into consistent blocks of time. This will be done before the per-series aligner can be applied to the data.The value must be at least 60 seconds. If a per-series aligner other than `ALIGN_NONE` is specified, this field is required or an error is returned. If no per-series aligner is specified, or the aligner `ALIGN_NONE` is specified, then this field is ignored.The maximum value of the `alignmentPeriod` is 104 weeks (2 years) for charts, and 90,000 seconds (25 hours) for alerting policies.  
`perSeriesAligner` |  `enum (`[Aligner](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Aligner)`)` An `Aligner` describes how to bring the data points in a single time series into temporal alignment. Except for `ALIGN_NONE`, all alignments cause all the data points in an `alignmentPeriod` to be mathematically grouped together, resulting in a single data point for each `alignmentPeriod` with end timestamp at the end of the period.Not all alignment operations may be applied to all time series. The valid choices depend on the `metricKind` and `valueType` of the original time series. Alignment can change the `metricKind` or the `valueType` of the time series.Time series data must be aligned in order to perform cross-time series reduction. If `crossSeriesReducer` is specified, then `perSeriesAligner` must be specified and not equal to `ALIGN_NONE` and `alignmentPeriod` must be specified; otherwise, an error is returned.  
`crossSeriesReducer` |  `enum (`[Reducer](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Reducer)`)` The reduction operation to be used to combine time series into a single time series, where the value of each data point in the resulting series is a function of all the already aligned values in the input time series.Not all reducer operations can be applied to all time series. The valid choices depend on the `metricKind` and the `valueType` of the original time series. Reduction can yield a time series with a different `metricKind` or `valueType` than the input time series.Time series data must first be aligned (see `perSeriesAligner`) in order to perform cross-time series reduction. If `crossSeriesReducer` is specified, then `perSeriesAligner` must be specified, and must not be `ALIGN_NONE`. An `alignmentPeriod` must also be specified; otherwise, an error is returned.  
`groupByFields[]` |  `string` The set of fields to preserve when `crossSeriesReducer` is specified. The `groupByFields` determine how the time series are partitioned into subsets prior to applying the aggregation operation. Each subset contains time series that have the same value for each of the grouping fields. Each individual time series is a member of exactly one subset. The `crossSeriesReducer` is applied to each subset of time series. It is not possible to reduce across different resource types, so this field implicitly contains `resource.type`. Fields not specified in `groupByFields` are aggregated away. If `groupByFields` is not specified and all the time series have the same resource type, then the time series are aggregated into a single output time series. If `crossSeriesReducer` is not defined, this field is ignored.  
  
## Aligner

The `Aligner` specifies the operation that will be applied to the data points in each alignment period in a time series. Except for `ALIGN_NONE`, which specifies that no operation be applied, each alignment operation replaces the set of data values in each alignment period with a single value: the result of applying the operation to the data values. An aligned time series has a single data value at the end of each `alignmentPeriod`.

An alignment operation can change the data type of the values, too. For example, if you apply a counting operation to boolean values, the data `valueType` in the original time series is `BOOLEAN`, but the `valueType` in the aligned result is `INT64`.

Enums  
---  
`ALIGN_NONE` | No alignment. Raw data is returned. Not valid if cross-series reduction is requested. The `valueType` of the result is the same as the `valueType` of the input.  
`ALIGN_DELTA` | Align and convert to `[DELTA](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind.ENUM_VALUES.DELTA)`. The output is `delta = y1 - y0`.This alignment is valid for `[CUMULATIVE](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind.ENUM_VALUES.CUMULATIVE)` and `DELTA` metrics. If the selected alignment period results in periods with no data, then the aligned value for such a period is created by interpolation. The `valueType` of the aligned result is the same as the `valueType` of the input.  
`ALIGN_RATE` | Align and convert to a rate. The result is computed as `rate = (y1 - y0)/(t1 - t0)`, or "delta over time". Think of this aligner as providing the slope of the line that passes through the value at the start and at the end of the `alignmentPeriod`.This aligner is valid for `CUMULATIVE` and `DELTA` metrics with numeric values. If the selected alignment period results in periods with no data, then the aligned value for such a period is created by interpolation. The output is a `GAUGE` metric with `valueType` `DOUBLE`.If, by "rate", you mean "percentage change", see the `ALIGN_PERCENT_CHANGE` aligner instead.  
`ALIGN_INTERPOLATE` | Align by interpolating between adjacent points around the alignment period boundary. This aligner is valid for `GAUGE` metrics with numeric values. The `valueType` of the aligned result is the same as the `valueType` of the input.  
`ALIGN_NEXT_OLDER` | Align by moving the most recent data point before the end of the alignment period to the boundary at the end of the alignment period. This aligner is valid for `GAUGE` metrics. The `valueType` of the aligned result is the same as the `valueType` of the input.  
`ALIGN_MIN` | Align the time series by returning the minimum value in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `valueType` of the aligned result is the same as the `valueType` of the input.  
`ALIGN_MAX` | Align the time series by returning the maximum value in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `valueType` of the aligned result is the same as the `valueType` of the input.  
`ALIGN_MEAN` | Align the time series by returning the mean value in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `valueType` of the aligned result is `DOUBLE`.  
`ALIGN_COUNT` | Align the time series by returning the number of values in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric or Boolean values. The `valueType` of the aligned result is `INT64`.  
`ALIGN_SUM` | Align the time series by returning the sum of the values in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric and distribution values. The `valueType` of the aligned result is the same as the `valueType` of the input.  
`ALIGN_STDDEV` | Align the time series by returning the standard deviation of the values in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `valueType` of the output is `DOUBLE`.  
`ALIGN_COUNT_TRUE` | Align the time series by returning the number of `True` values in each alignment period. This aligner is valid for `GAUGE` metrics with Boolean values. The `valueType` of the output is `INT64`.  
`ALIGN_COUNT_FALSE` | Align the time series by returning the number of `False` values in each alignment period. This aligner is valid for `GAUGE` metrics with Boolean values. The `valueType` of the output is `INT64`.  
`ALIGN_FRACTION_TRUE` | Align the time series by returning the ratio of the number of `True` values to the total number of values in each alignment period. This aligner is valid for `GAUGE` metrics with Boolean values. The output value is in the range [0.0, 1.0] and has `valueType` `DOUBLE`.  
`ALIGN_PERCENTILE_99` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 99th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `valueType` `DOUBLE`.  
`ALIGN_PERCENTILE_95` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 95th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `valueType` `DOUBLE`.  
`ALIGN_PERCENTILE_50` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 50th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `valueType` `DOUBLE`.  
`ALIGN_PERCENTILE_05` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 5th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `valueType` `DOUBLE`.  
`ALIGN_PERCENT_CHANGE` | Align and convert to a percentage change. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. This alignment returns `((current - previous)/previous) * 100`, where the value of `previous` is determined based on the `alignmentPeriod`.If the values of `current` and `previous` are both 0, then the returned value is 0. If only `previous` is 0, the returned value is infinity.A 10-minute moving mean is computed at each point of the alignment period prior to the above calculation to smooth the metric and prevent false positives from very short-lived spikes. The moving mean is only applicable for data whose values are `>= 0`. Any values `< 0` are treated as a missing datapoint, and are ignored. While `DELTA` metrics are accepted by this alignment, special care should be taken that the values for the metric will always be positive. The output is a `GAUGE` metric with `valueType` `DOUBLE`.  
  
## Reducer

A Reducer operation describes how to aggregate data points from multiple time series into a single time series, where the value of each data point in the resulting series is a function of all the already aligned values in the input time series.

Enums  
---  
`REDUCE_NONE` | No cross-time series reduction. The output of the `Aligner` is returned.  
`REDUCE_MEAN` | Reduce by computing the mean value across time series for each alignment period. This reducer is valid for `[DELTA](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind.ENUM_VALUES.DELTA)` and `[GAUGE](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind.ENUM_VALUES.GAUGE)` metrics with numeric or distribution values. The `valueType` of the output is `[DOUBLE](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#ValueType.ENUM_VALUES.DOUBLE)`.  
`REDUCE_MIN` | Reduce by computing the minimum value across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric values. The `valueType` of the output is the same as the `valueType` of the input.  
`REDUCE_MAX` | Reduce by computing the maximum value across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric values. The `valueType` of the output is the same as the `valueType` of the input.  
`REDUCE_SUM` | Reduce by computing the sum across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric and distribution values. The `valueType` of the output is the same as the `valueType` of the input.  
`REDUCE_STDDEV` | Reduce by computing the standard deviation across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric or distribution values. The `valueType` of the output is `DOUBLE`.  
`REDUCE_COUNT` | Reduce by computing the number of data points across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of numeric, Boolean, distribution, and string `valueType`. The `valueType` of the output is `INT64`.  
`REDUCE_COUNT_TRUE` | Reduce by computing the number of `True`-valued data points across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of Boolean `valueType`. The `valueType` of the output is `INT64`.  
`REDUCE_COUNT_FALSE` | Reduce by computing the number of `False`-valued data points across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of Boolean `valueType`. The `valueType` of the output is `INT64`.  
`REDUCE_FRACTION_TRUE` | Reduce by computing the ratio of the number of `True`-valued data points to the total number of data points for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of Boolean `valueType`. The output value is in the range [0.0, 1.0] and has `valueType` `DOUBLE`.  
`REDUCE_PERCENTILE_99` | Reduce by computing the [99th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
`REDUCE_PERCENTILE_95` | Reduce by computing the [95th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
`REDUCE_PERCENTILE_50` | Reduce by computing the [50th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
`REDUCE_PERCENTILE_05` | Reduce by computing the [5th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
  
## ForecastOptions

Options used when forecasting the time series and testing the predicted value against the threshold.

JSON representation  
---  
      
    
    {
      "forecastHorizon": string
    }  
  
Fields  
---  
`forecastHorizon` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. The length of time into the future to forecast whether a time series will violate the threshold. If the predicted value is found to violate the threshold, and the violation is observed in all forecasts made for the configured `duration`, then the time series is considered to be failing. The forecast horizon can range from 1 hour to 60 hours.  
  
## ComparisonType

Specifies an ordering relationship on two arguments, called `left` and `right`.

Enums  
---  
`COMPARISON_UNSPECIFIED` | No ordering relationship is specified.  
`COMPARISON_GT` | True if the left argument is greater than the right argument.  
`COMPARISON_GE` | True if the left argument is greater than or equal to the right argument.  
`COMPARISON_LT` | True if the left argument is less than the right argument.  
`COMPARISON_LE` | True if the left argument is less than or equal to the right argument.  
`COMPARISON_EQ` | True if the left argument is equal to the right argument.  
`COMPARISON_NE` | True if the left argument is not equal to the right argument.  
  
## Trigger

Specifies how many time series must fail a predicate to trigger a condition. If not specified, then a `{count: 1}` trigger is used.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "count": integer,
      "percent": number
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
A type of trigger. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`count` |  `integer` The absolute number of time series that must fail the predicate for the condition to be triggered.  
`percent` |  `number` The percentage of time series that must fail the predicate for the condition to be triggered.  
End of mutually exclusive fields.  
  
## EvaluationMissingData

A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. This control doesn't affect metric-absence policies.

Enums  
---  
`EVALUATION_MISSING_DATA_UNSPECIFIED` | An unspecified evaluation missing data option. Equivalent to EVALUATION_MISSING_DATA_NO_OP.  
`EVALUATION_MISSING_DATA_INACTIVE` | If there is no data to evaluate the condition, then evaluate the condition as false.  
`EVALUATION_MISSING_DATA_ACTIVE` | If there is no data to evaluate the condition, then evaluate the condition as true.  
`EVALUATION_MISSING_DATA_NO_OP` | Do not evaluate the condition to any value if there is no data.  
  
## MetricAbsence

A condition type that checks that monitored resources are reporting data. The configuration defines a metric and a set of monitored resources. The predicate is considered in violation when a time series for the specified metric of a monitored resource does not include any data in the specified `duration`.

JSON representation  
---  
      
    
    {
      "filter": string,
      "aggregations": [
        {
          object ([Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Aggregation))
        }
      ],
      "duration": string,
      "trigger": {
        object ([Trigger](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Trigger))
      }
    }  
  
Fields  
---  
`filter` |  `string` Required. A [filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the [`timeSeries.list` request](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) (that call is useful to verify the time series that will be retrieved / processed). The filter must specify the metric type and the resource type. Optionally, it can specify resource labels and metric labels. This field must not exceed 2048 Unicode characters in length.  
`aggregations[]` |  `object (`[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Aggregation)`)` Specifies the alignment of data points in individual time series as well as how to combine the retrieved time series together (such as when aggregating multiple streams on each resource to a single stream for each resource or when aggregating streams across all members of a group of resources). Multiple aggregations are applied in the order specified.This field is similar to the one in the [`timeSeries.list` request](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list). It is advisable to use the `timeSeries.list` method when debugging this field.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. The amount of time that a time series must fail to report new data to be considered failing. The minimum value of this field is 120 seconds. Larger values that are a multiple of a minute--for example, 240 or 300 seconds--are supported. If an invalid value is given, an error will be returned.  
`trigger` |  `object (`[Trigger](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Trigger)`)` The number/percent of time series for which the comparison must hold in order for the condition to trigger. If unspecified, then the condition will trigger if the comparison is true for any of the time series that have been identified by `filter` and `aggregations`.  
  
## LogMatch

A condition type that checks whether a log message in the [scoping project](https://cloud.google.com/monitoring/api/v3#project_name) satisfies the given filter. Logs from other projects in the metrics scope are not evaluated.

JSON representation  
---  
      
    
    {
      "filter": string,
      "labelExtractors": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`filter` |  `string` Required. A logs-based filter. See [Advanced Logs Queries](https://cloud.google.com/logging/docs/view/advanced-queries) for how this filter should be constructed.  
`labelExtractors` |  `map (key: string, value: string)` Optional. A map from a label key to an extractor expression, which is used to extract the value for this label key. Each entry in this map is a specification for how data should be extracted from log entries that match `filter`. Each combination of extracted values is treated as a separate rule for the purposes of triggering notifications. Label keys and corresponding values can be used in notifications generated by this condition.Please see [the documentation on logs-based metric `valueExtractor`s](https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric.FIELDS.value_extractor) for syntax and examples.  
  
## MonitoringQueryLanguageCondition

A condition type that allows alerting policies to be defined using [Monitoring Query Language](https://cloud.google.com/monitoring/mql).

JSON representation  
---  
      
    
    {
      "query": string,
      "duration": string,
      "trigger": {
        object ([Trigger](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Trigger))
      },
      "evaluationMissingData": enum ([EvaluationMissingData](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#EvaluationMissingData))
    }  
  
Fields  
---  
`query` |  `string` [Monitoring Query Language](https://cloud.google.com/monitoring/mql) query that outputs a boolean stream.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the `aggregations` field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly. The default value is zero.  
`trigger` |  `object (`[Trigger](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Trigger)`)` The number/percent of time series for which the comparison must hold in order for the condition to trigger. If unspecified, then the condition will trigger if the comparison is true for any of the time series that have been identified by `filter` and `aggregations`, or by the ratio, if `denominatorFilter` and `denominatorAggregations` are specified.  
`evaluationMissingData` |  `enum (`[EvaluationMissingData](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#EvaluationMissingData)`)` A condition control that determines how metric-threshold conditions are evaluated when data stops arriving.  
  
## PrometheusQueryLanguageCondition

A condition type that allows alerting policies to be defined using [Prometheus Query Language (PromQL)](https://prometheus.io/docs/prometheus/latest/querying/basics/).

The PrometheusQueryLanguageCondition message contains information from a Prometheus alerting rule and its associated rule group.

A Prometheus alerting rule is described [here](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/). The semantics of a Prometheus alerting rule is described [here](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#rule).

A Prometheus rule group is described [here](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/). The semantics of a Prometheus rule group is described [here](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#ruleGroup).

Because Cloud Alerting has no representation of a Prometheus rule group resource, we must embed the information of the parent rule group inside each of the conditions that refer to it. We must also update the contents of all Prometheus alerts in case the information of their rule group changes.

The PrometheusQueryLanguageCondition protocol buffer combines the information of the corresponding rule group and alerting rule. The structure of the PrometheusQueryLanguageCondition protocol buffer does NOT mimic the structure of the Prometheus rule group and alerting rule YAML declarations. The PrometheusQueryLanguageCondition protocol buffer may change in the future to support future rule group and/or alerting rule features. There are no new such features at the present time (2023-06-26).

JSON representation  
---  
      
    
    {
      "query": string,
      "duration": string,
      "evaluationInterval": string,
      "labels": {
        string: string,
        ...
      },
      "ruleGroup": string,
      "alertRule": string,
      "disableMetricValidation": boolean
    }  
  
Fields  
---  
`query` |  `string` Required. The PromQL expression to evaluate. Every evaluation cycle this expression is evaluated at the current time, and all resultant time series become pending/firing alerts. This field must not be empty.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Alerts are considered firing once their PromQL expression was evaluated to be "true" for this long. Alerts whose PromQL expression was not evaluated to be "true" for long enough are considered pending. Must be a non-negative duration or missing. This field is optional. Its default value is zero.  
`evaluationInterval` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. How often this rule should be evaluated. Must be a positive multiple of 30 seconds or missing. This field is optional. Its default value is 30 seconds. If this PrometheusQueryLanguageCondition was generated from a Prometheus alerting rule, then this value should be taken from the enclosing rule group.  
`labels` |  `map (key: string, value: string)` Optional. Labels to add to or overwrite in the PromQL query result. Label names [must be valid](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels). Label values can be [templatized by using variables](https://cloud.google.com/monitoring/alerts/doc-variables#doc-vars). The only available variable names are the names of the labels in the PromQL result, including "__name__" and "value". "labels" may be empty.  
`ruleGroup` |  `string` Optional. The rule group name of this alert in the corresponding Prometheus configuration file.Some external tools may require this field to be populated correctly in order to refer to the original Prometheus configuration file. The rule group name and the alert name are necessary to update the relevant AlertPolicies in case the definition of the rule group changes in the future.This field is optional. If this field is not empty, then it must contain a valid UTF-8 string. This field may not exceed 2048 Unicode characters in length.  
`alertRule` |  `string` Optional. The alerting rule name of this alert in the corresponding Prometheus configuration file.Some external tools may require this field to be populated correctly in order to refer to the original Prometheus configuration file. The rule group name and the alert name are necessary to update the relevant AlertPolicies in case the definition of the rule group changes in the future.This field is optional. If this field is not empty, then it must be a [valid Prometheus label name](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels). This field may not exceed 2048 Unicode characters in length.  
`disableMetricValidation` |  `boolean` Optional. Whether to disable metric existence validation for this condition.This allows alerting policies to be defined on metrics that do not yet exist, improving advanced customer workflows such as configuring alerting policies using Terraform.Users with the `monitoring.alertPolicyViewer` role are able to see the name of the non-existent metric in the alerting policy condition.  
  
## SqlCondition

A condition that allows alerting policies to be defined using GoogleSQL. SQL conditions examine a sliding window of logs using GoogleSQL. Alert policies with SQL conditions may incur additional billing.

JSON representation  
---  
      
    
    {
      "query": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "minutes": {
        object ([Minutes](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Minutes))
      },
      "hourly": {
        object ([Hourly](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Hourly))
      },
      "daily": {
        object ([Daily](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Daily))
      }
      // End of mutually exclusive fields.
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "rowCountTest": {
        object ([RowCountTest](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#RowCountTest))
      },
      "booleanTest": {
        object ([BooleanTest](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#BooleanTest))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`query` |  `string` Required. The Log Analytics SQL query to run, as a string. The query must conform to the required shape. Specifically, the query must not try to filter the input by time. A filter will automatically be applied to filter the input so that the query receives all rows received since the last time the query was run.For example, the following query extracts all log entries containing an HTTP request:
    
    
    SELECT
      timestamp, logName, severity, httpRequest, resource, labels
    FROM
      my-project.global._Default._AllLogs
    WHERE
      httpRequest IS NOT NULL
      
  
The schedule indicates how often the query should be run. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`minutes` |  `object (`[Minutes](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Minutes)`)` Schedule the query to execute every so many minutes.  
`hourly` |  `object (`[Hourly](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Hourly)`)` Schedule the query to execute every so many hours.  
`daily` |  `object (`[Daily](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#Daily)`)` Schedule the query to execute every so many days.  
End of mutually exclusive fields.  
The test to be run against the SQL result set. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`rowCountTest` |  `object (`[RowCountTest](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#RowCountTest)`)` Test the row count against a threshold.  
`booleanTest` |  `object (`[BooleanTest](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#BooleanTest)`)` Test the boolean value in the indicated column.  
End of mutually exclusive fields.  
  
## Minutes

Used to schedule the query to run every so many minutes.

JSON representation  
---  
      
    
    {
      "periodicity": integer
    }  
  
Fields  
---  
`periodicity` |  `integer` Required. Number of minutes between runs. The interval must be greater than or equal to 5 minutes and less than or equal to 1440 minutes.  
  
## Hourly

Used to schedule the query to run every so many hours.

JSON representation  
---  
      
    
    {
      "periodicity": integer,
      "minuteOffset": integer
    }  
  
Fields  
---  
`periodicity` |  `integer` Required. The number of hours between runs. Must be greater than or equal to 1 hour and less than or equal to 48 hours.  
`minuteOffset` |  `integer` Optional. The number of minutes after the hour (in UTC) to run the query. Must be greater than or equal to 0 minutes and less than or equal to 59 minutes. If left unspecified, then an arbitrary offset is used.  
  
## Daily

Used to schedule the query to run every so many days.

JSON representation  
---  
      
    
    {
      "periodicity": integer,
      "executionTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#TimeOfDay))
      }
    }  
  
Fields  
---  
`periodicity` |  `integer` Required. The number of days between runs. Must be greater than or equal to 1 day and less than or equal to 31 days.  
`executionTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#TimeOfDay)`)` Optional. The time of day (in UTC) at which the query should run. If left unspecified, the server picks an arbitrary time of day and runs the query at the same time each day.  
  
## TimeOfDay

Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are `google.type.Date` and `google.protobuf.Timestamp`.

JSON representation  
---  
      
    
    {
      "hours": integer,
      "minutes": integer,
      "seconds": integer,
      "nanos": integer
    }  
  
Fields  
---  
`hours` |  `integer` Hours of a day in 24 hour format. Must be greater than or equal to 0 and typically must be less than or equal to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`minutes` |  `integer` Minutes of an hour. Must be greater than or equal to 0 and less than or equal to 59.  
`seconds` |  `integer` Seconds of a minute. Must be greater than or equal to 0 and typically must be less than or equal to 59. An API may allow the value 60 if it allows leap-seconds.  
`nanos` |  `integer` Fractions of seconds, in nanoseconds. Must be greater than or equal to 0 and less than or equal to 999,999,999.  
  
## RowCountTest

A test that checks if the number of rows in the result set violates some threshold.

JSON representation  
---  
      
    
    {
      "comparison": enum ([ComparisonType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#ComparisonType)),
      "threshold": string
    }  
  
Fields  
---  
`comparison` |  `enum (`[ComparisonType](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#ComparisonType)`)` Required. The comparison to apply between the number of rows returned by the query and the threshold.  
`threshold` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The value against which to compare the row count.  
  
## BooleanTest

A test that uses an alerting result in a boolean column produced by the SQL query.

JSON representation  
---  
      
    
    {
      "column": string
    }  
  
Fields  
---  
`column` |  `string` Required. The name of the column containing the boolean value. If the value in a row is NULL, that row is ignored.  
  
## ConditionCombinerType

Operators for combining conditions.

Enums  
---  
`COMBINE_UNSPECIFIED` | An unspecified combiner.  
`AND` | Combine conditions using the logical `AND` operator. An incident is created only if all the conditions are met simultaneously. This combiner is satisfied if all conditions are met, even if they are met on completely different resources.  
`OR` | Combine conditions using the logical `OR` operator. An incident is created if any of the listed conditions is met.  
`AND_WITH_MATCHING_RESOURCE` | Combine conditions using logical `AND` operator, but unlike the regular `AND` option, an incident is created only if all conditions are met simultaneously on at least one resource.  
  
## AlertStrategy

Control over how the notification channels in `notificationChannels` are notified when this alert fires.

JSON representation  
---  
      
    
    {
      "notificationRateLimit": {
        object ([NotificationRateLimit](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#NotificationRateLimit))
      },
      "notificationPrompts": [
        enum ([NotificationPrompt](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#NotificationPrompt))
      ],
      "autoClose": string,
      "notificationChannelStrategy": [
        {
          object ([NotificationChannelStrategy](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#NotificationChannelStrategy))
        }
      ]
    }  
  
Fields  
---  
`notificationRateLimit` |  `object (`[NotificationRateLimit](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#NotificationRateLimit)`)` Required for log-based alerting policies, i.e. policies with a `LogMatch` condition.This limit is not implemented for alerting policies that do not have a LogMatch condition.  
`notificationPrompts[]` |  `enum (`[NotificationPrompt](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#NotificationPrompt)`)` For log-based alert policies, the notification prompts is always [OPENED]. For non log-based alert policies, the notification prompts can be [OPENED] or [OPENED, CLOSED].  
`autoClose` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` If an alerting policy that was active has no data for this long, any open incidents will close  
`notificationChannelStrategy[]` |  `object (`[NotificationChannelStrategy](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#NotificationChannelStrategy)`)` Control how notifications will be sent out, on a per-channel basis.  
  
## NotificationRateLimit

Control over the rate of notifications sent to this alerting policy's notification channels.

JSON representation  
---  
      
    
    {
      "period": string
    }  
  
Fields  
---  
`period` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Not more than one notification per `period`.  
  
## NotificationPrompt

Control when notifications will be sent out.

Enums  
---  
`NOTIFICATION_PROMPT_UNSPECIFIED` | No strategy specified. Treated as error.  
`OPENED` | Notify when an incident is opened.  
`CLOSED` | Notify when an incident is closed.  
  
## NotificationChannelStrategy

Control over how the notification channels in `notificationChannels` are notified when this alert fires, on a per-channel basis.

JSON representation  
---  
      
    
    {
      "notificationChannelNames": [
        string
      ],
      "renotifyInterval": string
    }  
  
Fields  
---  
`notificationChannelNames[]` |  `string` The full REST resource name for the notification channels that these settings apply to. Each of these correspond to the name field in one of the NotificationChannel objects referenced in the notificationChannels field of this AlertPolicy. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID]
      
  
`renotifyInterval` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The frequency at which to send reminder notifications for open incidents. The value must be between 30 minutes and 24 hours.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create)`

|  Creates a new alerting policy.  
  
### `[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/delete)`

|  Deletes an alerting policy.  
  
### `[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/get)`

|  Gets a single alerting policy.  
  
### `[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/list)`

|  Lists the existing alerting policies for the workspace.  
  
### `[patch](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/patch)`

|  Updates an alerting policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-04 UTC."],[],[]] 
