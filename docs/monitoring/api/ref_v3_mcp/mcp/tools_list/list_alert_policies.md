---
url: https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_alert_policies/
title: MCP Tools Reference: monitoring.googleapis.com \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:24.346935+00:00
---

# MCP Tools Reference: monitoring.googleapis.com  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_alert_policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  MCP Tools Reference: monitoring.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_alert_policies`

Use this as the primary tool to list the alerting policies in a Google Cloud project. Alerting policies define the conditions under which you want to be notified about issues with your services. This is useful for understanding what alerts are currently configured.

The following code sample shows how to use `curl` to call the `list_alert_policies` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://monitoring.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_alert_policies",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

The protocol for the `ListAlertPolicies` request.

### ListAlertPoliciesRequest

JSON representation  
---  
      
    
    {
      "name": string,
      "filter": string,
      "orderBy": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) whose alert policies are to be listed. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

Note that this field names the parent container in which the alerting policies to be listed are stored. To retrieve a single alerting policy by name, use the `GetAlertPolicy` operation, instead.  
`filter` |  `string` Optional. If provided, this field specifies the criteria that must be met by alert policies to be included in the response.For more details, see [sorting and filtering](https://cloud.google.com/monitoring/api/v3/sorting-and-filtering).  
`orderBy` |  `string` Optional. A comma-separated list of fields by which to sort the result. Supports the same set of field references as the `filter` field. Entries can be prefixed with a minus sign to sort by the field in descending order.For more details, see [sorting and filtering](https://cloud.google.com/monitoring/api/v3/sorting-and-filtering).  
`pageSize` |  `integer` Optional. The maximum number of results to return in a single response.  
`pageToken` |  `string` Optional. If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return more results from the previous method call.  
  
## Output Schema

The protocol for the `ListAlertPolicies` response.

### ListAlertPoliciesResponse

JSON representation  
---  
      
    
    {
      "alertPolicies": [
        {
          object ([AlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.AlertPolicy))
        }
      ],
      "nextPageToken": string,
      "totalSize": integer
    }  
  
Fields  
---  
`alertPolicies[]` |  `object (`[AlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.AlertPolicy)`)` The returned alert policies.  
`nextPageToken` |  `string` If there might be more results than were returned, then this field is set to a non-empty value. To see the additional results, use that value as `page_token` in the next call to this method.  
`totalSize` |  `integer` The total number of alert policies in all pages. This number is only an estimate, and may change in subsequent pages. <https://aip.dev/158>  
  
### AlertPolicy

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "documentation": {
        object ([Documentation](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Documentation))
      },
      "userLabels": {
        string: string,
        ...
      },
      "conditions": [
        {
          object ([Condition](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Condition))
        }
      ],
      "combiner": enum ([ConditionCombinerType](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.ConditionCombinerType)),
      "enabled": boolean,
      "validity": {
        object ([Status](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Status))
      },
      "notificationChannels": [
        string
      ],
      "creationRecord": {
        object ([MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.MutationRecord))
      },
      "mutationRecord": {
        object ([MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.MutationRecord))
      },
      "alertStrategy": {
        object ([AlertStrategy](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.AlertStrategy))
      },
      "severity": enum ([Severity](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Severity))
    }  
  
Fields  
---  
`name` |  `string` Identifier. Required if the policy exists. The resource name for this policy. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[ALERT_POLICY_ID]
    

`[ALERT_POLICY_ID]` is assigned by Cloud Monitoring when the policy is created. When calling the `alertPolicies.create` method, do not include the `name` field in the alerting policy passed as part of the request.  
`displayName` |  `string` A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion, don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode characters.The convention for the display_name of a PrometheusQueryLanguageCondition is "{rule group name}/{alert name}", where the {rule group name} and {alert name} should be taken from the corresponding Prometheus configuration file. This convention is not enforced. In any case the display_name is not a unique key of the AlertPolicy.  
`documentation` |  `object (`[Documentation](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Documentation)`)` Documentation that is included with notifications and incidents related to this policy. Best practice is for the documentation to include information to help responders understand, mitigate, escalate, and correct the underlying problems detected by the alerting policy. Notification channels that have limited capacity might not show this documentation.  
`userLabels` |  `map (key: string, value: string)` User-supplied key/value data to be used for organizing and identifying the `AlertPolicy` objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.Note that Prometheus {alert name} is a [valid Prometheus label names](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels), whereas Prometheus {rule group} is an unrestricted UTF-8 string. This means that they cannot be stored as-is in user labels, because they may contain characters that are not allowed in user-label values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`conditions[]` |  `object (`[Condition](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Condition)`)` A list of conditions for the policy. The conditions are combined by AND or OR according to the `combiner` field. If the combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions. If `condition_time_series_query_language` is present, it must be the only `condition`. If `condition_monitoring_query_language` is present, it must be the only `condition`.  
`combiner` |  `enum (`[ConditionCombinerType](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.ConditionCombinerType)`)` How to combine the results of multiple conditions to determine if an incident should be opened. If `condition_time_series_query_language` is present, this must be `COMBINE_UNSPECIFIED`.  
`enabled` |  `boolean` Whether or not the policy is enabled. On write, the default interpretation if unset is that the policy is enabled. On read, clients should not make any assumption about the state if it has not been populated. The field should always be populated on List and Get operations, unless a field projection has been specified that strips it out.  
`validity` |  `object (`[Status](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Status)`)` Read-only description of how the alerting policy is invalid. This field is only set when the alerting policy is invalid. An invalid alerting policy will not generate incidents.  
`notificationChannels[]` |  `string` Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when new violations occur on an already opened incident. Each element of this array corresponds to the `name` field in each of the ``NotificationChannel`` objects that are returned from the ``ListNotificationChannels`` method. The format of the entries in this field is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID]
      
  
`creationRecord` |  `object (`[MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.MutationRecord)`)` A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be ignored.  
`mutationRecord` |  `object (`[MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.MutationRecord)`)` A read-only record of the most recent change to the alerting policy. If provided in a call to create or update, this field will be ignored.  
`alertStrategy` |  `object (`[AlertStrategy](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.AlertStrategy)`)` Control over how this alerting policy's notification channels are notified.  
`severity` |  `enum (`[Severity](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Severity)`)` Optional. The severity of an alerting policy indicates how important incidents generated by that policy are. The severity level will be displayed on the Incident detail page and in notifications.  
  
### Documentation

JSON representation  
---  
      
    
    {
      "content": string,
      "mimeType": string,
      "subject": string,
      "links": [
        {
          object ([Link](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Link))
        }
      ]
    }  
  
Fields  
---  
`content` |  `string` The body of the documentation, interpreted according to `mime_type`. The content may not exceed 8,192 Unicode characters and may not exceed more than 10,240 bytes when encoded in UTF-8 format, whichever is smaller. This text can be [templatized by using variables](https://cloud.google.com/monitoring/alerts/doc-variables#doc-vars).  
`mimeType` |  `string` The format of the `content` field. Presently, only the value `"text/markdown"` is supported. See [Markdown](https://en.wikipedia.org/wiki/Markdown) for more information.  
`subject` |  `string` Optional. The subject line of the notification. The subject line may not exceed 10,240 bytes. In notifications generated by this policy, the contents of the subject line after variable expansion will be truncated to 255 bytes or shorter at the latest UTF-8 character boundary. The 255-byte limit is recommended by [this thread](https://stackoverflow.com/questions/1592291/what-is-the-email-subject-length-limit). It is both the limit imposed by some third-party ticketing products and it is common to define textual fields in databases as VARCHAR(255).The contents of the subject line can be [templatized by using variables](https://cloud.google.com/monitoring/alerts/doc-variables#doc-vars). If this field is missing or empty, a default subject line will be generated.  
`links[]` |  `object (`[Link](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Link)`)` Optional. Links to content such as playbooks, repositories, and other resources. This field can contain up to 3 entries.  
  
### Link

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
  
### UserLabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### Condition

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
    
      // Union field condition can be only one of the following:
      "conditionThreshold": {
        object ([MetricThreshold](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.MetricThreshold))
      },
      "conditionAbsent": {
        object ([MetricAbsence](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.MetricAbsence))
      },
      "conditionMatchedLog": {
        object ([LogMatch](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.LogMatch))
      },
      "conditionMonitoringQueryLanguage": {
        object ([MonitoringQueryLanguageCondition](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.MonitoringQueryLanguageCondition))
      },
      "conditionPrometheusQueryLanguage": {
        object ([PrometheusQueryLanguageCondition](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.PrometheusQueryLanguageCondition))
      },
      "conditionSql": {
        object ([SqlCondition](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.SqlCondition))
      }
      // End of list of possible types for union field condition.
    }  
  
Fields  
---  
`name` |  `string` Required if the condition exists. The unique resource name for this condition. Its format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[POLICY_ID]/conditions/[CONDITION_ID]
    

`[CONDITION_ID]` is assigned by Cloud Monitoring when the condition is created as part of a new or updated alerting policy.When calling the `alertPolicies.create` method, do not include the `name` field in the conditions of the requested alerting policy. Cloud Monitoring creates the condition identifiers and includes them in the new policy.When calling the `alertPolicies.update` method to update a policy, including a condition `name` causes the existing condition to be updated. Conditions without names are added to the updated policy. Existing conditions are deleted if they are not updated.Best practice is to preserve `[CONDITION_ID]` if you make only small changes, such as those to condition thresholds, durations, or trigger values. Otherwise, treat the change as a new condition and let the existing condition be deleted.  
`displayName` |  `string` A short name or phrase used to identify the condition in dashboards, notifications, and incidents. To avoid confusion, don't use the same display name for multiple conditions in the same policy.  
Union field `condition`. Only one of the following condition types will be specified. `condition` can be only one of the following:  
`conditionThreshold` |  `object (`[MetricThreshold](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.MetricThreshold)`)` A condition that compares a time series against a threshold.  
`conditionAbsent` |  `object (`[MetricAbsence](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.MetricAbsence)`)` A condition that checks that a time series continues to receive new data points.  
`conditionMatchedLog` |  `object (`[LogMatch](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.LogMatch)`)` A condition that checks for log messages matching given constraints. If set, no other conditions can be present.  
`conditionMonitoringQueryLanguage` |  `object (`[MonitoringQueryLanguageCondition](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.MonitoringQueryLanguageCondition)`)` A condition that uses the Monitoring Query Language to define alerts.  
`conditionPrometheusQueryLanguage` |  `object (`[PrometheusQueryLanguageCondition](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.PrometheusQueryLanguageCondition)`)` A condition that uses the Prometheus query language to define alerts.  
`conditionSql` |  `object (`[SqlCondition](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.SqlCondition)`)` A condition that periodically evaluates a SQL query result.  
  
### MetricThreshold

JSON representation  
---  
      
    
    {
      "filter": string,
      "aggregations": [
        {
          object ([Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Aggregation))
        }
      ],
      "denominatorFilter": string,
      "denominatorAggregations": [
        {
          object ([Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Aggregation))
        }
      ],
      "forecastOptions": {
        object ([ForecastOptions](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.ForecastOptions))
      },
      "comparison": enum ([ComparisonType](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.ComparisonType)),
      "thresholdValue": number,
      "duration": string,
      "trigger": {
        object ([Trigger](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Trigger))
      },
      "evaluationMissingData": enum ([EvaluationMissingData](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.EvaluationMissingData))
    }  
  
Fields  
---  
`filter` |  `string` Required. A [filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the [`ListTimeSeries` request](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) (that call is useful to verify the time series that will be retrieved / processed). The filter must specify the metric type and the resource type. Optionally, it can specify resource labels and metric labels. This field must not exceed 2048 Unicode characters in length.  
`aggregations[]` |  `object (`[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Aggregation)`)` Specifies the alignment of data points in individual time series as well as how to combine the retrieved time series together (such as when aggregating multiple streams on each resource to a single stream for each resource or when aggregating streams across all members of a group of resources). Multiple aggregations are applied in the order specified.This field is similar to the one in the [`ListTimeSeries` request](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list). It is advisable to use the `ListTimeSeries` method when debugging this field.  
`denominatorFilter` |  `string` A [filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies a time series that should be used as the denominator of a ratio that will be compared with the threshold. If a `denominator_filter` is specified, the time series specified by the `filter` field will be used as the numerator.The filter must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length.  
`denominatorAggregations[]` |  `object (`[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Aggregation)`)` Specifies the alignment of data points in individual time series selected by `denominatorFilter` as well as how to combine the retrieved time series together (such as when aggregating multiple streams on each resource to a single stream for each resource or when aggregating streams across all members of a group of resources).When computing ratios, the `aggregations` and `denominator_aggregations` fields must use the same alignment period and produce time series that have the same periodicity and labels.  
`forecastOptions` |  `object (`[ForecastOptions](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.ForecastOptions)`)` When this field is present, the `MetricThreshold` condition forecasts whether the time series is predicted to violate the threshold within the `forecast_horizon`. When this field is not set, the `MetricThreshold` tests the current value of the timeseries against the threshold.  
`comparison` |  `enum (`[ComparisonType](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.ComparisonType)`)` The comparison to apply between the time series (indicated by `filter` and `aggregation`) and the threshold (indicated by `threshold_value`). The comparison is applied on each time series, with the time series on the left-hand side and the threshold on the right-hand side.Only `COMPARISON_LT` and `COMPARISON_GT` are supported currently.  
`thresholdValue` |  `number` A value against which to compare the time series.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the `aggregations` field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`trigger` |  `object (`[Trigger](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Trigger)`)` The number/percent of time series for which the comparison must hold in order for the condition to trigger. If unspecified, then the condition will trigger if the comparison is true for any of the time series that have been identified by `filter` and `aggregations`, or by the ratio, if `denominator_filter` and `denominator_aggregations` are specified.  
`evaluationMissingData` |  `enum (`[EvaluationMissingData](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.EvaluationMissingData)`)` A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. To use this control, the value of the `duration` field must be greater than or equal to 60 seconds.  
  
### Aggregation

JSON representation  
---  
      
    
    {
      "alignmentPeriod": string,
      "perSeriesAligner": enum ([Aligner](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Aligner)),
      "crossSeriesReducer": enum ([Reducer](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Reducer)),
      "groupByFields": [
        string
      ]
    }  
  
Fields  
---  
`alignmentPeriod` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The `alignment_period` specifies a time interval, in seconds, that is used to divide the data in all the `[time series](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.TimeSeries)` into consistent blocks of time. This will be done before the per-series aligner can be applied to the data.The value must be at least 60 seconds. If a per-series aligner other than `ALIGN_NONE` is specified, this field is required or an error is returned. If no per-series aligner is specified, or the aligner `ALIGN_NONE` is specified, then this field is ignored.The maximum value of the `alignment_period` is 104 weeks (2 years) for charts, and 90,000 seconds (25 hours) for alerting policies.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`perSeriesAligner` |  `enum (`[Aligner](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Aligner)`)` An `Aligner` describes how to bring the data points in a single time series into temporal alignment. Except for `ALIGN_NONE`, all alignments cause all the data points in an `alignment_period` to be mathematically grouped together, resulting in a single data point for each `alignment_period` with end timestamp at the end of the period.Not all alignment operations may be applied to all time series. The valid choices depend on the `metric_kind` and `value_type` of the original time series. Alignment can change the `metric_kind` or the `value_type` of the time series.Time series data must be aligned in order to perform cross-time series reduction. If `cross_series_reducer` is specified, then `per_series_aligner` must be specified and not equal to `ALIGN_NONE` and `alignment_period` must be specified; otherwise, an error is returned.  
`crossSeriesReducer` |  `enum (`[Reducer](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Reducer)`)` The reduction operation to be used to combine time series into a single time series, where the value of each data point in the resulting series is a function of all the already aligned values in the input time series.Not all reducer operations can be applied to all time series. The valid choices depend on the `metric_kind` and the `value_type` of the original time series. Reduction can yield a time series with a different `metric_kind` or `value_type` than the input time series.Time series data must first be aligned (see `per_series_aligner`) in order to perform cross-time series reduction. If `cross_series_reducer` is specified, then `per_series_aligner` must be specified, and must not be `ALIGN_NONE`. An `alignment_period` must also be specified; otherwise, an error is returned.  
`groupByFields[]` |  `string` The set of fields to preserve when `cross_series_reducer` is specified. The `group_by_fields` determine how the time series are partitioned into subsets prior to applying the aggregation operation. Each subset contains time series that have the same value for each of the grouping fields. Each individual time series is a member of exactly one subset. The `cross_series_reducer` is applied to each subset of time series. It is not possible to reduce across different resource types, so this field implicitly contains `resource.type`. Fields not specified in `group_by_fields` are aggregated away. If `group_by_fields` is not specified and all the time series have the same resource type, then the time series are aggregated into a single output time series. If `cross_series_reducer` is not defined, this field is ignored.  
  
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
  
### ForecastOptions

JSON representation  
---  
      
    
    {
      "forecastHorizon": string
    }  
  
Fields  
---  
`forecastHorizon` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. The length of time into the future to forecast whether a time series will violate the threshold. If the predicted value is found to violate the threshold, and the violation is observed in all forecasts made for the configured `duration`, then the time series is considered to be failing. The forecast horizon can range from 1 hour to 60 hours.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### Trigger

JSON representation  
---  
      
    
    {
    
      // Union field type can be only one of the following:
      "count": integer,
      "percent": number
      // End of list of possible types for union field type.
    }  
  
Fields  
---  
Union field `type`. A type of trigger. `type` can be only one of the following:  
`count` |  `integer` The absolute number of time series that must fail the predicate for the condition to be triggered.  
`percent` |  `number` The percentage of time series that must fail the predicate for the condition to be triggered.  
  
### MetricAbsence

JSON representation  
---  
      
    
    {
      "filter": string,
      "aggregations": [
        {
          object ([Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Aggregation))
        }
      ],
      "duration": string,
      "trigger": {
        object ([Trigger](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Trigger))
      }
    }  
  
Fields  
---  
`filter` |  `string` Required. A [filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the [`ListTimeSeries` request](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) (that call is useful to verify the time series that will be retrieved / processed). The filter must specify the metric type and the resource type. Optionally, it can specify resource labels and metric labels. This field must not exceed 2048 Unicode characters in length.  
`aggregations[]` |  `object (`[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Aggregation)`)` Specifies the alignment of data points in individual time series as well as how to combine the retrieved time series together (such as when aggregating multiple streams on each resource to a single stream for each resource or when aggregating streams across all members of a group of resources). Multiple aggregations are applied in the order specified.This field is similar to the one in the [`ListTimeSeries` request](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list). It is advisable to use the `ListTimeSeries` method when debugging this field.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. The amount of time that a time series must fail to report new data to be considered failing. The minimum value of this field is 120 seconds. Larger values that are a multiple of a minute--for example, 240 or 300 seconds--are supported. If an invalid value is given, an error will be returned.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`trigger` |  `object (`[Trigger](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Trigger)`)` The number/percent of time series for which the comparison must hold in order for the condition to trigger. If unspecified, then the condition will trigger if the comparison is true for any of the time series that have been identified by `filter` and `aggregations`.  
  
### LogMatch

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
`labelExtractors` |  `map (key: string, value: string)` Optional. A map from a label key to an extractor expression, which is used to extract the value for this label key. Each entry in this map is a specification for how data should be extracted from log entries that match `filter`. Each combination of extracted values is treated as a separate rule for the purposes of triggering notifications. Label keys and corresponding values can be used in notifications generated by this condition.Please see [the documentation on logs-based metric `valueExtractor`s](https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric.FIELDS.value_extractor) for syntax and examples.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### LabelExtractorsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### MonitoringQueryLanguageCondition

JSON representation  
---  
      
    
    {
      "query": string,
      "duration": string,
      "trigger": {
        object ([Trigger](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Trigger))
      },
      "evaluationMissingData": enum ([EvaluationMissingData](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.EvaluationMissingData))
    }  
  
Fields  
---  
`query` |  `string` [Monitoring Query Language](https://cloud.google.com/monitoring/mql) query that outputs a boolean stream.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the `aggregations` field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly. The default value is zero.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`trigger` |  `object (`[Trigger](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Trigger)`)` The number/percent of time series for which the comparison must hold in order for the condition to trigger. If unspecified, then the condition will trigger if the comparison is true for any of the time series that have been identified by `filter` and `aggregations`, or by the ratio, if `denominator_filter` and `denominator_aggregations` are specified.  
`evaluationMissingData` |  `enum (`[EvaluationMissingData](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.EvaluationMissingData)`)` A condition control that determines how metric-threshold conditions are evaluated when data stops arriving.  
  
### PrometheusQueryLanguageCondition

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
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Alerts are considered firing once their PromQL expression was evaluated to be "true" for this long. Alerts whose PromQL expression was not evaluated to be "true" for long enough are considered pending. Must be a non-negative duration or missing. This field is optional. Its default value is zero.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`evaluationInterval` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. How often this rule should be evaluated. Must be a positive multiple of 30 seconds or missing. This field is optional. Its default value is 30 seconds. If this PrometheusQueryLanguageCondition was generated from a Prometheus alerting rule, then this value should be taken from the enclosing rule group.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels to add to or overwrite in the PromQL query result. Label names [must be valid](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels). Label values can be [templatized by using variables](https://cloud.google.com/monitoring/alerts/doc-variables#doc-vars). The only available variable names are the names of the labels in the PromQL result, including "__name__" and "value". "labels" may be empty.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`ruleGroup` |  `string` Optional. The rule group name of this alert in the corresponding Prometheus configuration file.Some external tools may require this field to be populated correctly in order to refer to the original Prometheus configuration file. The rule group name and the alert name are necessary to update the relevant AlertPolicies in case the definition of the rule group changes in the future.This field is optional. If this field is not empty, then it must contain a valid UTF-8 string. This field may not exceed 2048 Unicode characters in length.  
`alertRule` |  `string` Optional. The alerting rule name of this alert in the corresponding Prometheus configuration file.Some external tools may require this field to be populated correctly in order to refer to the original Prometheus configuration file. The rule group name and the alert name are necessary to update the relevant AlertPolicies in case the definition of the rule group changes in the future.This field is optional. If this field is not empty, then it must be a [valid Prometheus label name](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels). This field may not exceed 2048 Unicode characters in length.  
`disableMetricValidation` |  `boolean` Optional. Whether to disable metric existence validation for this condition.This allows alerting policies to be defined on metrics that do not yet exist, improving advanced customer workflows such as configuring alerting policies using Terraform.Users with the `monitoring.alertPolicyViewer` role are able to see the name of the non-existent metric in the alerting policy condition.  
  
### LabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### SqlCondition

JSON representation  
---  
      
    
    {
      "query": string,
    
      // Union field schedule can be only one of the following:
      "minutes": {
        object ([Minutes](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Minutes))
      },
      "hourly": {
        object ([Hourly](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Hourly))
      },
      "daily": {
        object ([Daily](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Daily))
      }
      // End of list of possible types for union field schedule.
    
      // Union field evaluate can be only one of the following:
      "rowCountTest": {
        object ([RowCountTest](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.RowCountTest))
      },
      "booleanTest": {
        object ([BooleanTest](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.BooleanTest))
      }
      // End of list of possible types for union field evaluate.
    }  
  
Fields  
---  
`query` |  `string` Required. The Log Analytics SQL query to run, as a string. The query must conform to the required shape. Specifically, the query must not try to filter the input by time. A filter will automatically be applied to filter the input so that the query receives all rows received since the last time the query was run.For example, the following query extracts all log entries containing an HTTP request:
    
    
    SELECT
      timestamp, log_name, severity, http_request, resource, labels
    FROM
      my-project.global._Default._AllLogs
    WHERE
      http_request IS NOT NULL
      
  
Union field `schedule`. The schedule indicates how often the query should be run. `schedule` can be only one of the following:  
`minutes` |  `object (`[Minutes](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Minutes)`)` Schedule the query to execute every so many minutes.  
`hourly` |  `object (`[Hourly](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Hourly)`)` Schedule the query to execute every so many hours.  
`daily` |  `object (`[Daily](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.Daily)`)` Schedule the query to execute every so many days.  
Union field `evaluate`. The test to be run against the SQL result set. `evaluate` can be only one of the following:  
`rowCountTest` |  `object (`[RowCountTest](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.RowCountTest)`)` Test the row count against a threshold.  
`booleanTest` |  `object (`[BooleanTest](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.BooleanTest)`)` Test the boolean value in the indicated column.  
  
### Minutes

JSON representation  
---  
      
    
    {
      "periodicity": integer
    }  
  
Fields  
---  
`periodicity` |  `integer` Required. Number of minutes between runs. The interval must be greater than or equal to 5 minutes and less than or equal to 1440 minutes.  
  
### Hourly

JSON representation  
---  
      
    
    {
      "periodicity": integer,
    
      // Union field _minute_offset can be only one of the following:
      "minuteOffset": integer
      // End of list of possible types for union field _minute_offset.
    }  
  
Fields  
---  
`periodicity` |  `integer` Required. The number of hours between runs. Must be greater than or equal to 1 hour and less than or equal to 48 hours.  
Union field `_minute_offset`.`_minute_offset` can be only one of the following:  
`minuteOffset` |  `integer` Optional. The number of minutes after the hour (in UTC) to run the query. Must be greater than or equal to 0 minutes and less than or equal to 59 minutes. If left unspecified, then an arbitrary offset is used.  
  
### Daily

JSON representation  
---  
      
    
    {
      "periodicity": integer,
      "executionTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.TimeOfDay))
      }
    }  
  
Fields  
---  
`periodicity` |  `integer` Required. The number of days between runs. Must be greater than or equal to 1 day and less than or equal to 31 days.  
`executionTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.TimeOfDay)`)` Optional. The time of day (in UTC) at which the query should run. If left unspecified, the server picks an arbitrary time of day and runs the query at the same time each day.  
  
### TimeOfDay

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
  
### RowCountTest

JSON representation  
---  
      
    
    {
      "comparison": enum ([ComparisonType](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.ComparisonType)),
      "threshold": string
    }  
  
Fields  
---  
`comparison` |  `enum (`[ComparisonType](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.ComparisonType)`)` Required. The comparison to apply between the number of rows returned by the query and the threshold.  
`threshold` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The value against which to compare the row count.  
  
### BooleanTest

JSON representation  
---  
      
    
    {
      "column": string
    }  
  
Fields  
---  
`column` |  `string` Required. The name of the column containing the boolean value. If the value in a row is NULL, that row is ignored.  
  
### BoolValue

JSON representation  
---  
      
    
    {
      "value": boolean
    }  
  
Fields  
---  
`value` |  `boolean` The bool value.  
  
### Status

JSON representation  
---  
      
    
    {
      "code": integer,
      "message": string,
      "details": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ]
    }  
  
Fields  
---  
`code` |  `integer` The status code, which should be an enum value of `google.rpc.Code`.  
`message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `google.rpc.Status.details` field, or localized by the client.  
`details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Any

JSON representation  
---  
      
    
    {
      "typeUrl": string,
      "value": string
    }  
  
Fields  
---  
`typeUrl` |  `string` Identifies the type of the serialized Protobuf message with a URI reference consisting of a prefix ending in a slash and the fully-qualified type name.Example: type.googleapis.com/google.protobuf.StringValueThis string must contain at least one `/` character, and the content after the last `/` must be the fully-qualified name of the type in canonical form, without a leading dot. Do not write a scheme on these URI references so that clients do not attempt to contact them.The prefix is arbitrary and Protobuf implementations are expected to simply strip off everything up to and including the last `/` to identify the type. `type.googleapis.com/` is a common default prefix that some legacy implementations require. This prefix does not indicate the origin of the type, and URIs containing it are not expected to respond to any requests.All type URL strings must be legal URI references with the additional restriction (for the text format) that the content of the reference must consist only of alphanumeric characters, percent-encoded escapes, and characters in the following set (not including the outer backticks): `/-.~_!$&()*+,;=`. Despite our allowing percent encodings, implementations should not unescape them to prevent confusion with existing parsers. For example, `type.googleapis.com%2FFoo` should be rejected.In the original design of `Any`, the possibility of launching a type resolution service at these type URLs was considered but Protobuf never implemented one and considers contacting these URLs to be problematic and a potential security issue. Do not attempt to contact type URLs.  
`value` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Holds a Protobuf serialization of the type described by type_url.A base64-encoded string.  
  
### MutationRecord

JSON representation  
---  
      
    
    {
      "mutateTime": string,
      "mutatedBy": string
    }  
  
Fields  
---  
`mutateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` When the change occurred.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`mutatedBy` |  `string` The email address of the user making the change.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### AlertStrategy

JSON representation  
---  
      
    
    {
      "notificationRateLimit": {
        object ([NotificationRateLimit](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.NotificationRateLimit))
      },
      "notificationPrompts": [
        enum ([NotificationPrompt](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.NotificationPrompt))
      ],
      "autoClose": string,
      "notificationChannelStrategy": [
        {
          object ([NotificationChannelStrategy](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.NotificationChannelStrategy))
        }
      ]
    }  
  
Fields  
---  
`notificationRateLimit` |  `object (`[NotificationRateLimit](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.NotificationRateLimit)`)` Required for log-based alerting policies, i.e. policies with a `LogMatch` condition.This limit is not implemented for alerting policies that do not have a LogMatch condition.  
`notificationPrompts[]` |  `enum (`[NotificationPrompt](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.NotificationPrompt)`)` For log-based alert policies, the notification prompts is always [OPENED]. For non log-based alert policies, the notification prompts can be [OPENED] or [OPENED, CLOSED].  
`autoClose` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` If an alerting policy that was active has no data for this long, any open incidents will closeA duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`notificationChannelStrategy[]` |  `object (`[NotificationChannelStrategy](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/get_alert_policy#Output.Schema.NotificationChannelStrategy)`)` Control how notifications will be sent out, on a per-channel basis.  
  
### NotificationRateLimit

JSON representation  
---  
      
    
    {
      "period": string
    }  
  
Fields  
---  
`period` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Not more than one notification per `period`.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### NotificationChannelStrategy

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
`notificationChannelNames[]` |  `string` The full REST resource name for the notification channels that these settings apply to. Each of these correspond to the name field in one of the NotificationChannel objects referenced in the notification_channels field of this AlertPolicy. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID]
      
  
`renotifyInterval` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The frequency at which to send reminder notifications for open incidents. The value must be between 30 minutes and 24 hours.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### Aligner

The `Aligner` specifies the operation that will be applied to the data points in each alignment period in a time series. Except for `ALIGN_NONE`, which specifies that no operation be applied, each alignment operation replaces the set of data values in each alignment period with a single value: the result of applying the operation to the data values. An aligned time series has a single data value at the end of each `alignment_period`.

An alignment operation can change the data type of the values, too. For example, if you apply a counting operation to boolean values, the data `value_type` in the original time series is `BOOLEAN`, but the `value_type` in the aligned result is `INT64`.

Enums  
---  
`ALIGN_NONE` | No alignment. Raw data is returned. Not valid if cross-series reduction is requested. The `value_type` of the result is the same as the `value_type` of the input.  
`ALIGN_DELTA` | Align and convert to `DELTA`. The output is `delta = y1 - y0`.This alignment is valid for `CUMULATIVE` and `DELTA` metrics. If the selected alignment period results in periods with no data, then the aligned value for such a period is created by interpolation. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_RATE` | Align and convert to a rate. The result is computed as `rate = (y1 - y0)/(t1 - t0)`, or "delta over time". Think of this aligner as providing the slope of the line that passes through the value at the start and at the end of the `alignment_period`.This aligner is valid for `CUMULATIVE` and `DELTA` metrics with numeric values. If the selected alignment period results in periods with no data, then the aligned value for such a period is created by interpolation. The output is a `GAUGE` metric with `value_type` `DOUBLE`.If, by "rate", you mean "percentage change", see the `ALIGN_PERCENT_CHANGE` aligner instead.  
`ALIGN_INTERPOLATE` | Align by interpolating between adjacent points around the alignment period boundary. This aligner is valid for `GAUGE` metrics with numeric values. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_NEXT_OLDER` | Align by moving the most recent data point before the end of the alignment period to the boundary at the end of the alignment period. This aligner is valid for `GAUGE` metrics. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_MIN` | Align the time series by returning the minimum value in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_MAX` | Align the time series by returning the maximum value in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_MEAN` | Align the time series by returning the mean value in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `value_type` of the aligned result is `DOUBLE`.  
`ALIGN_COUNT` | Align the time series by returning the number of values in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric or Boolean values. The `value_type` of the aligned result is `INT64`.  
`ALIGN_SUM` | Align the time series by returning the sum of the values in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric and distribution values. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_STDDEV` | Align the time series by returning the standard deviation of the values in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `value_type` of the output is `DOUBLE`.  
`ALIGN_COUNT_TRUE` | Align the time series by returning the number of `True` values in each alignment period. This aligner is valid for `GAUGE` metrics with Boolean values. The `value_type` of the output is `INT64`.  
`ALIGN_COUNT_FALSE` | Align the time series by returning the number of `False` values in each alignment period. This aligner is valid for `GAUGE` metrics with Boolean values. The `value_type` of the output is `INT64`.  
`ALIGN_FRACTION_TRUE` | Align the time series by returning the ratio of the number of `True` values to the total number of values in each alignment period. This aligner is valid for `GAUGE` metrics with Boolean values. The output value is in the range [0.0, 1.0] and has `value_type` `DOUBLE`.  
`ALIGN_PERCENTILE_99` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 99th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `value_type` `DOUBLE`.  
`ALIGN_PERCENTILE_95` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 95th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `value_type` `DOUBLE`.  
`ALIGN_PERCENTILE_50` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 50th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `value_type` `DOUBLE`.  
`ALIGN_PERCENTILE_05` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 5th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `value_type` `DOUBLE`.  
`ALIGN_PERCENT_CHANGE` | Align and convert to a percentage change. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. This alignment returns `((current - previous)/previous) * 100`, where the value of `previous` is determined based on the `alignment_period`.If the values of `current` and `previous` are both 0, then the returned value is 0. If only `previous` is 0, the returned value is infinity.A 10-minute moving mean is computed at each point of the alignment period prior to the above calculation to smooth the metric and prevent false positives from very short-lived spikes. The moving mean is only applicable for data whose values are `>= 0`. Any values `< 0` are treated as a missing datapoint, and are ignored. While `DELTA` metrics are accepted by this alignment, special care should be taken that the values for the metric will always be positive. The output is a `GAUGE` metric with `value_type` `DOUBLE`.  
  
### Reducer

A Reducer operation describes how to aggregate data points from multiple time series into a single time series, where the value of each data point in the resulting series is a function of all the already aligned values in the input time series.

Enums  
---  
`REDUCE_NONE` | No cross-time series reduction. The output of the `Aligner` is returned.  
`REDUCE_MEAN` | Reduce by computing the mean value across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric or distribution values. The `value_type` of the output is `DOUBLE`.  
`REDUCE_MIN` | Reduce by computing the minimum value across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric values. The `value_type` of the output is the same as the `value_type` of the input.  
`REDUCE_MAX` | Reduce by computing the maximum value across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric values. The `value_type` of the output is the same as the `value_type` of the input.  
`REDUCE_SUM` | Reduce by computing the sum across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric and distribution values. The `value_type` of the output is the same as the `value_type` of the input.  
`REDUCE_STDDEV` | Reduce by computing the standard deviation across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric or distribution values. The `value_type` of the output is `DOUBLE`.  
`REDUCE_COUNT` | Reduce by computing the number of data points across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of numeric, Boolean, distribution, and string `value_type`. The `value_type` of the output is `INT64`.  
`REDUCE_COUNT_TRUE` | Reduce by computing the number of `True`-valued data points across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of Boolean `value_type`. The `value_type` of the output is `INT64`.  
`REDUCE_COUNT_FALSE` | Reduce by computing the number of `False`-valued data points across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of Boolean `value_type`. The `value_type` of the output is `INT64`.  
`REDUCE_FRACTION_TRUE` | Reduce by computing the ratio of the number of `True`-valued data points to the total number of data points for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of Boolean `value_type`. The output value is in the range [0.0, 1.0] and has `value_type` `DOUBLE`.  
`REDUCE_PERCENTILE_99` | Reduce by computing the [99th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
`REDUCE_PERCENTILE_95` | Reduce by computing the [95th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
`REDUCE_PERCENTILE_50` | Reduce by computing the [50th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
`REDUCE_PERCENTILE_05` | Reduce by computing the [5th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
  
### ComparisonType

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
  
### EvaluationMissingData

A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. This control doesn't affect metric-absence policies.

Enums  
---  
`EVALUATION_MISSING_DATA_UNSPECIFIED` | An unspecified evaluation missing data option. Equivalent to EVALUATION_MISSING_DATA_NO_OP.  
`EVALUATION_MISSING_DATA_INACTIVE` | If there is no data to evaluate the condition, then evaluate the condition as false.  
`EVALUATION_MISSING_DATA_ACTIVE` | If there is no data to evaluate the condition, then evaluate the condition as true.  
`EVALUATION_MISSING_DATA_NO_OP` | Do not evaluate the condition to any value if there is no data.  
  
### ConditionCombinerType

Operators for combining conditions.

Enums  
---  
`COMBINE_UNSPECIFIED` | An unspecified combiner.  
`AND` | Combine conditions using the logical `AND` operator. An incident is created only if all the conditions are met simultaneously. This combiner is satisfied if all conditions are met, even if they are met on completely different resources.  
`OR` | Combine conditions using the logical `OR` operator. An incident is created if any of the listed conditions is met.  
`AND_WITH_MATCHING_RESOURCE` | Combine conditions using logical `AND` operator, but unlike the regular `AND` option, an incident is created only if all conditions are met simultaneously on at least one resource.  
  
### NotificationPrompt

Control when notifications will be sent out.

Enums  
---  
`NOTIFICATION_PROMPT_UNSPECIFIED` | No strategy specified. Treated as error.  
`OPENED` | Notify when an incident is opened.  
`CLOSED` | Notify when an incident is closed.  
  
### Severity

An enumeration of possible severity level for an alerting policy.

Enums  
---  
`SEVERITY_UNSPECIFIED` | No severity is specified. This is the default value.  
`CRITICAL` | This is the highest severity level. Use this if the problem could cause significant damage or downtime.  
`ERROR` | This is the medium severity level. Use this if the problem could cause minor damage or downtime.  
`WARNING` | This is the lowest severity level. Use this if the problem is not causing any damage or downtime, but could potentially lead to a problem in the future.  
  
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
