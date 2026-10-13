---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/monitoring/monitoringalertpolicy/
title: MonitoringAlertPolicy \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:16:25.425557+00:00
---

# MonitoringAlertPolicy  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/monitoring/monitoringalertpolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# MonitoringAlertPolicy

**Property** | **Value**  
---|---  
Google Cloud Service Name | Cloud Monitoring  
Google Cloud Service Documentation | [/monitoring/docs/](https://docs.cloud.google.com/monitoring/docs)  
Google Cloud REST Resource Name | v3.projects.alertPolicies  
Google Cloud REST Resource Documentation | [/monitoring/api/ref_v3/rest/v3/projects.alertPolicies](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies)  
Config Connector Resource Short Names | gcpmonitoringalertpolicies  
gcpmonitoringalertpolicy  
monitoringalertpolicy  
Config Connector Service Name | monitoring.googleapis.com  
Config Connector Resource Fully Qualified Name | monitoringalertpolicies.monitoring.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Annotations

Fields  
---  
`cnrm.cloud.google.com/project-id`  
  
### Spec

#### Schema
    
    
    alertStrategy:
      autoClose: string
      notificationChannelStrategy:
      - notificationChannelNames:
        - string
        renotifyInterval: string
      notificationRateLimit:
        period: string
    combiner: string
    conditions:
    - conditionAbsent:
        aggregations:
        - alignmentPeriod: string
          crossSeriesReducer: string
          groupByFields:
          - string
          perSeriesAligner: string
        duration: string
        filter: string
        trigger:
          count: integer
          percent: float
      conditionMatchedLog:
        filter: string
        labelExtractors:
          string: string
      conditionMonitoringQueryLanguage:
        duration: string
        evaluationMissingData: string
        query: string
        trigger:
          count: integer
          percent: float
      conditionPrometheusQueryLanguage:
        alertRule: string
        duration: string
        evaluationInterval: string
        labels:
          string: string
        query: string
        ruleGroup: string
      conditionSql:
        booleanTest:
          column: string
        daily:
          executionTime:
            hours: integer
            minutes: integer
            nanos: integer
            seconds: integer
          periodicity: integer
        hourly:
          minuteOffset: integer
          periodicity: integer
        minutes:
          periodicity: integer
        query: string
        rowCountTest:
          comparison: string
          threshold: integer
      conditionThreshold:
        aggregations:
        - alignmentPeriod: string
          crossSeriesReducer: string
          groupByFields:
          - string
          perSeriesAligner: string
        comparison: string
        denominatorAggregations:
        - alignmentPeriod: string
          crossSeriesReducer: string
          groupByFields:
          - string
          perSeriesAligner: string
        denominatorFilter: string
        duration: string
        evaluationMissingData: string
        filter: string
        forecastOptions:
          forecastHorizon: string
        thresholdValue: float
        trigger:
          count: integer
          percent: float
      displayName: string
      name: string
    displayName: string
    documentation:
      content: string
      mimeType: string
    enabled: boolean
    notificationChannels:
    - external: string
      name: string
      namespace: string
    resourceID: string
    severity: string
    

Fields  
---  
`alertStrategy` _Optional_ |  `object` Control over how this alert policy's notification channels are notified.  
`alertStrategy.autoClose` _Optional_ |  `string` If an alert policy that was active has no data for this long, any open incidents will close.  
`alertStrategy.notificationChannelStrategy` _Optional_ |  `list (object)` Control over how the notification channels in 'notification_channels' are notified when this alert fires, on a per-channel basis.  
`alertStrategy.notificationChannelStrategy[]` _Optional_ |  `object`  
`alertStrategy.notificationChannelStrategy[].notificationChannelNames` _Optional_ |  `list (string)` The notification channels that these settings apply to. Each of these correspond to the name field in one of the NotificationChannel objects referenced in the notification_channels field of this AlertPolicy. The format is 'projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID]'.  
`alertStrategy.notificationChannelStrategy[].notificationChannelNames[]` _Optional_ |  `string`  
`alertStrategy.notificationChannelStrategy[].renotifyInterval` _Optional_ |  `string` The frequency at which to send reminder notifications for open incidents.  
`alertStrategy.notificationRateLimit` _Optional_ |  `object` Required for alert policies with a LogMatch condition. This limit is not implemented for alert policies that are not log-based.  
`alertStrategy.notificationRateLimit.period` _Optional_ |  `string` Not more than one notification per period.  
`combiner` _Required_ |  `string` How to combine the results of multiple conditions to determine if an incident should be opened. Possible values: ["AND", "OR", "AND_WITH_MATCHING_RESOURCE"].  
`conditions` _Required_ |  `list (object)` A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions.  
`conditions[]` _Required_ |  `object`  
`conditions[].conditionAbsent` _Optional_ |  `object` A condition that checks that a time series continues to receive new data points.  
`conditions[].conditionAbsent.aggregations` _Optional_ |  `list (object)` Specifies the alignment of data points in individual time series as well as how to combine the retrieved time series together (such as when aggregating multiple streams on each resource to a single stream for each resource or when aggregating streams across all members of a group of resources). Multiple aggregations are applied in the order specified.  
`conditions[].conditionAbsent.aggregations[]` _Optional_ |  `object`  
`conditions[].conditionAbsent.aggregations[].alignmentPeriod` _Optional_ |  `string` The alignment period for per-time series alignment. If present, alignmentPeriod must be at least 60 seconds. After per-time series alignment, each time series will contain data points only on the period boundaries. If perSeriesAligner is not specified or equals ALIGN_NONE, then this field is ignored. If perSeriesAligner is specified and does not equal ALIGN_NONE, then this field must be defined; otherwise an error is returned.  
`conditions[].conditionAbsent.aggregations[].crossSeriesReducer` _Optional_ |  `string` The approach to be used to combine time series. Not all reducer functions may be applied to all time series, depending on the metric type and the value type of the original time series. Reduction may change the metric type of value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["REDUCE_NONE", "REDUCE_MEAN", "REDUCE_MIN", "REDUCE_MAX", "REDUCE_SUM", "REDUCE_STDDEV", "REDUCE_COUNT", "REDUCE_COUNT_TRUE", "REDUCE_COUNT_FALSE", "REDUCE_FRACTION_TRUE", "REDUCE_PERCENTILE_99", "REDUCE_PERCENTILE_95", "REDUCE_PERCENTILE_50", "REDUCE_PERCENTILE_05"].  
`conditions[].conditionAbsent.aggregations[].groupByFields` _Optional_ |  `list (string)` The set of fields to preserve when crossSeriesReducer is specified. The groupByFields determine how the time series are partitioned into subsets prior to applying the aggregation function. Each subset contains time series that have the same value for each of the grouping fields. Each individual time series is a member of exactly one subset. The crossSeriesReducer is applied to each subset of time series. It is not possible to reduce across different resource types, so this field implicitly contains resource.type. Fields not specified in groupByFields are aggregated away. If groupByFields is not specified and all the time series have the same resource type, then the time series are aggregated into a single output time series. If crossSeriesReducer is not defined, this field is ignored.  
`conditions[].conditionAbsent.aggregations[].groupByFields[]` _Optional_ |  `string`  
`conditions[].conditionAbsent.aggregations[].perSeriesAligner` _Optional_ |  `string` The approach to be used to align individual time series. Not all alignment functions may be applied to all time series, depending on the metric type and value type of the original time series. Alignment may change the metric type or the value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["ALIGN_NONE", "ALIGN_DELTA", "ALIGN_RATE", "ALIGN_INTERPOLATE", "ALIGN_NEXT_OLDER", "ALIGN_MIN", "ALIGN_MAX", "ALIGN_MEAN", "ALIGN_COUNT", "ALIGN_SUM", "ALIGN_STDDEV", "ALIGN_COUNT_TRUE", "ALIGN_COUNT_FALSE", "ALIGN_FRACTION_TRUE", "ALIGN_PERCENTILE_99", "ALIGN_PERCENTILE_95", "ALIGN_PERCENTILE_50", "ALIGN_PERCENTILE_05", "ALIGN_PERCENT_CHANGE"].  
`conditions[].conditionAbsent.duration` _Required*_ |  `string` The amount of time that a time series must fail to report new data to be considered failing. Currently, only values that are a multiple of a minute--e.g. 60s, 120s, or 300s --are supported.  
`conditions[].conditionAbsent.filter` _Optional_ |  `string` A filter that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length.  
`conditions[].conditionAbsent.trigger` _Optional_ |  `object` The number/percent of time series for which the comparison must hold in order for the condition to trigger. If unspecified, then the condition will trigger if the comparison is true for any of the time series that have been identified by filter and aggregations.  
`conditions[].conditionAbsent.trigger.count` _Optional_ |  `integer` The absolute number of time series that must fail the predicate for the condition to be triggered.  
`conditions[].conditionAbsent.trigger.percent` _Optional_ |  `float` The percentage of time series that must fail the predicate for the condition to be triggered.  
`conditions[].conditionMatchedLog` _Optional_ |  `object` A condition that checks for log messages matching given constraints. If set, no other conditions can be present.  
`conditions[].conditionMatchedLog.filter` _Required*_ |  `string` A logs-based filter.  
`conditions[].conditionMatchedLog.labelExtractors` _Optional_ |  `map (key: string, value: string)` A map from a label key to an extractor expression, which is used to extract the value for this label key. Each entry in this map is a specification for how data should be extracted from log entries that match filter. Each combination of extracted values is treated as a separate rule for the purposes of triggering notifications. Label keys and corresponding values can be used in notifications generated by this condition.  
`conditions[].conditionMonitoringQueryLanguage` _Optional_ |  `object` A Monitoring Query Language query that outputs a boolean stream.  
`conditions[].conditionMonitoringQueryLanguage.duration` _Required*_ |  `string` The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the aggregations field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly.  
`conditions[].conditionMonitoringQueryLanguage.evaluationMissingData` _Optional_ |  `string` A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. Possible values: ["EVALUATION_MISSING_DATA_INACTIVE", "EVALUATION_MISSING_DATA_ACTIVE", "EVALUATION_MISSING_DATA_NO_OP"].  
`conditions[].conditionMonitoringQueryLanguage.query` _Required*_ |  `string` Monitoring Query Language query that outputs a boolean stream.  
`conditions[].conditionMonitoringQueryLanguage.trigger` _Optional_ |  `object` The number/percent of time series for which the comparison must hold in order for the condition to trigger. If unspecified, then the condition will trigger if the comparison is true for any of the time series that have been identified by filter and aggregations, or by the ratio, if denominator_filter and denominator_aggregations are specified.  
`conditions[].conditionMonitoringQueryLanguage.trigger.count` _Optional_ |  `integer` The absolute number of time series that must fail the predicate for the condition to be triggered.  
`conditions[].conditionMonitoringQueryLanguage.trigger.percent` _Optional_ |  `float` The percentage of time series that must fail the predicate for the condition to be triggered.  
`conditions[].conditionPrometheusQueryLanguage` _Optional_ |  `object` A Monitoring Query Language query that outputs a boolean stream A condition type that allows alert policies to be defined using Prometheus Query Language (PromQL). The PrometheusQueryLanguageCondition message contains information from a Prometheus alerting rule and its associated rule group.  
`conditions[].conditionPrometheusQueryLanguage.alertRule` _Optional_ |  `string` The alerting rule name of this alert in the corresponding Prometheus configuration file. Some external tools may require this field to be populated correctly in order to refer to the original Prometheus configuration file. The rule group name and the alert name are necessary to update the relevant AlertPolicies in case the definition of the rule group changes in the future. This field is optional. If this field is not empty, then it must be a valid Prometheus label name.  
`conditions[].conditionPrometheusQueryLanguage.duration` _Optional_ |  `string` Alerts are considered firing once their PromQL expression evaluated to be "true" for this long. Alerts whose PromQL expression was not evaluated to be "true" for long enough are considered pending. The default value is zero. Must be zero or positive.  
`conditions[].conditionPrometheusQueryLanguage.evaluationInterval` _Optional_ |  `string` How often this rule should be evaluated. Must be a positive multiple of 30 seconds or missing. The default value is 30 seconds. If this PrometheusQueryLanguageCondition was generated from a Prometheus alerting rule, then this value should be taken from the enclosing rule group.  
`conditions[].conditionPrometheusQueryLanguage.labels` _Optional_ |  `map (key: string, value: string)` Labels to add to or overwrite in the PromQL query result. Label names must be valid. Label values can be templatized by using variables. The only available variable names are the names of the labels in the PromQL result, including "__name__" and "value". "labels" may be empty. This field is intended to be used for organizing and identifying the AlertPolicy.  
`conditions[].conditionPrometheusQueryLanguage.query` _Required*_ |  `string` The PromQL expression to evaluate. Every evaluation cycle this expression is evaluated at the current time, and all resultant time series become pending/firing alerts. This field must not be empty.  
`conditions[].conditionPrometheusQueryLanguage.ruleGroup` _Optional_ |  `string` The rule group name of this alert in the corresponding Prometheus configuration file. Some external tools may require this field to be populated correctly in order to refer to the original Prometheus configuration file. The rule group name and the alert name are necessary to update the relevant AlertPolicies in case the definition of the rule group changes in the future. This field is optional. If this field is not empty, then it must be a valid Prometheus label name.  
`conditions[].conditionSql` _Optional_ |  `object` A condition that allows alerting policies to be defined using GoogleSQL.  
`conditions[].conditionSql.booleanTest` _Optional_ |  `object` Test the boolean value in the indicated column.  
`conditions[].conditionSql.booleanTest.column` _Required*_ |  `string` The name of the column containing the boolean value.  
`conditions[].conditionSql.daily` _Optional_ |  `object` Schedule the query to execute every so many days.  
`conditions[].conditionSql.daily.executionTime` _Optional_ |  `object` The time of day (in UTC) at which the query should run.  
`conditions[].conditionSql.daily.executionTime.hours` _Optional_ |  `integer` Hours of day in 24 hour format.  
`conditions[].conditionSql.daily.executionTime.minutes` _Optional_ |  `integer` Minutes of hour of day.  
`conditions[].conditionSql.daily.executionTime.nanos` _Optional_ |  `integer` Fractions of seconds in nanoseconds.  
`conditions[].conditionSql.daily.executionTime.seconds` _Optional_ |  `integer` Seconds of minutes of the time.  
`conditions[].conditionSql.daily.periodicity` _Required*_ |  `integer` The number of days between runs.  
`conditions[].conditionSql.hourly` _Optional_ |  `object` Schedule the query to execute every so many hours.  
`conditions[].conditionSql.hourly.minuteOffset` _Optional_ |  `integer` The number of minutes after the hour (in UTC) to run the query.  
`conditions[].conditionSql.hourly.periodicity` _Required*_ |  `integer` Number of hours between runs.  
`conditions[].conditionSql.minutes` _Optional_ |  `object` Schedule the query to execute every so many minutes.  
`conditions[].conditionSql.minutes.periodicity` _Required*_ |  `integer` Number of minutes between runs.  
`conditions[].conditionSql.query` _Required*_ |  `string` The Log Analytics SQL query to run, as a string.  
`conditions[].conditionSql.rowCountTest` _Optional_ |  `object` Test the row count against a threshold.  
`conditions[].conditionSql.rowCountTest.comparison` _Required*_ |  `string` The comparison to apply between the number of rows returned by the query and the threshold.  
`conditions[].conditionSql.rowCountTest.threshold` _Required*_ |  `integer` The value against which to compare the row count.  
`conditions[].conditionThreshold` _Optional_ |  `object` A condition that compares a time series against a threshold.  
`conditions[].conditionThreshold.aggregations` _Optional_ |  `list (object)` Specifies the alignment of data points in individual time series as well as how to combine the retrieved time series together (such as when aggregating multiple streams on each resource to a single stream for each resource or when aggregating streams across all members of a group of resources). Multiple aggregations are applied in the order specified.This field is similar to the one in the MetricService.ListTimeSeries request. It is advisable to use the ListTimeSeries method when debugging this field.  
`conditions[].conditionThreshold.aggregations[]` _Optional_ |  `object`  
`conditions[].conditionThreshold.aggregations[].alignmentPeriod` _Optional_ |  `string` The alignment period for per-time series alignment. If present, alignmentPeriod must be at least 60 seconds. After per-time series alignment, each time series will contain data points only on the period boundaries. If perSeriesAligner is not specified or equals ALIGN_NONE, then this field is ignored. If perSeriesAligner is specified and does not equal ALIGN_NONE, then this field must be defined; otherwise an error is returned.  
`conditions[].conditionThreshold.aggregations[].crossSeriesReducer` _Optional_ |  `string` The approach to be used to combine time series. Not all reducer functions may be applied to all time series, depending on the metric type and the value type of the original time series. Reduction may change the metric type of value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["REDUCE_NONE", "REDUCE_MEAN", "REDUCE_MIN", "REDUCE_MAX", "REDUCE_SUM", "REDUCE_STDDEV", "REDUCE_COUNT", "REDUCE_COUNT_TRUE", "REDUCE_COUNT_FALSE", "REDUCE_FRACTION_TRUE", "REDUCE_PERCENTILE_99", "REDUCE_PERCENTILE_95", "REDUCE_PERCENTILE_50", "REDUCE_PERCENTILE_05"].  
`conditions[].conditionThreshold.aggregations[].groupByFields` _Optional_ |  `list (string)` The set of fields to preserve when crossSeriesReducer is specified. The groupByFields determine how the time series are partitioned into subsets prior to applying the aggregation function. Each subset contains time series that have the same value for each of the grouping fields. Each individual time series is a member of exactly one subset. The crossSeriesReducer is applied to each subset of time series. It is not possible to reduce across different resource types, so this field implicitly contains resource.type. Fields not specified in groupByFields are aggregated away. If groupByFields is not specified and all the time series have the same resource type, then the time series are aggregated into a single output time series. If crossSeriesReducer is not defined, this field is ignored.  
`conditions[].conditionThreshold.aggregations[].groupByFields[]` _Optional_ |  `string`  
`conditions[].conditionThreshold.aggregations[].perSeriesAligner` _Optional_ |  `string` The approach to be used to align individual time series. Not all alignment functions may be applied to all time series, depending on the metric type and value type of the original time series. Alignment may change the metric type or the value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["ALIGN_NONE", "ALIGN_DELTA", "ALIGN_RATE", "ALIGN_INTERPOLATE", "ALIGN_NEXT_OLDER", "ALIGN_MIN", "ALIGN_MAX", "ALIGN_MEAN", "ALIGN_COUNT", "ALIGN_SUM", "ALIGN_STDDEV", "ALIGN_COUNT_TRUE", "ALIGN_COUNT_FALSE", "ALIGN_FRACTION_TRUE", "ALIGN_PERCENTILE_99", "ALIGN_PERCENTILE_95", "ALIGN_PERCENTILE_50", "ALIGN_PERCENTILE_05", "ALIGN_PERCENT_CHANGE"].  
`conditions[].conditionThreshold.comparison` _Required*_ |  `string` The comparison to apply between the time series (indicated by filter and aggregation) and the threshold (indicated by threshold_value). The comparison is applied on each time series, with the time series on the left-hand side and the threshold on the right-hand side. Only COMPARISON_LT and COMPARISON_GT are supported currently. Possible values: ["COMPARISON_GT", "COMPARISON_GE", "COMPARISON_LT", "COMPARISON_LE", "COMPARISON_EQ", "COMPARISON_NE"].  
`conditions[].conditionThreshold.denominatorAggregations` _Optional_ |  `list (object)` Specifies the alignment of data points in individual time series selected by denominatorFilter as well as how to combine the retrieved time series together (such as when aggregating multiple streams on each resource to a single stream for each resource or when aggregating streams across all members of a group of resources).When computing ratios, the aggregations and denominator_aggregations fields must use the same alignment period and produce time series that have the same periodicity and labels.This field is similar to the one in the MetricService.ListTimeSeries request. It is advisable to use the ListTimeSeries method when debugging this field.  
`conditions[].conditionThreshold.denominatorAggregations[]` _Optional_ |  `object`  
`conditions[].conditionThreshold.denominatorAggregations[].alignmentPeriod` _Optional_ |  `string` The alignment period for per-time series alignment. If present, alignmentPeriod must be at least 60 seconds. After per-time series alignment, each time series will contain data points only on the period boundaries. If perSeriesAligner is not specified or equals ALIGN_NONE, then this field is ignored. If perSeriesAligner is specified and does not equal ALIGN_NONE, then this field must be defined; otherwise an error is returned.  
`conditions[].conditionThreshold.denominatorAggregations[].crossSeriesReducer` _Optional_ |  `string` The approach to be used to combine time series. Not all reducer functions may be applied to all time series, depending on the metric type and the value type of the original time series. Reduction may change the metric type of value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["REDUCE_NONE", "REDUCE_MEAN", "REDUCE_MIN", "REDUCE_MAX", "REDUCE_SUM", "REDUCE_STDDEV", "REDUCE_COUNT", "REDUCE_COUNT_TRUE", "REDUCE_COUNT_FALSE", "REDUCE_FRACTION_TRUE", "REDUCE_PERCENTILE_99", "REDUCE_PERCENTILE_95", "REDUCE_PERCENTILE_50", "REDUCE_PERCENTILE_05"].  
`conditions[].conditionThreshold.denominatorAggregations[].groupByFields` _Optional_ |  `list (string)` The set of fields to preserve when crossSeriesReducer is specified. The groupByFields determine how the time series are partitioned into subsets prior to applying the aggregation function. Each subset contains time series that have the same value for each of the grouping fields. Each individual time series is a member of exactly one subset. The crossSeriesReducer is applied to each subset of time series. It is not possible to reduce across different resource types, so this field implicitly contains resource.type. Fields not specified in groupByFields are aggregated away. If groupByFields is not specified and all the time series have the same resource type, then the time series are aggregated into a single output time series. If crossSeriesReducer is not defined, this field is ignored.  
`conditions[].conditionThreshold.denominatorAggregations[].groupByFields[]` _Optional_ |  `string`  
`conditions[].conditionThreshold.denominatorAggregations[].perSeriesAligner` _Optional_ |  `string` The approach to be used to align individual time series. Not all alignment functions may be applied to all time series, depending on the metric type and value type of the original time series. Alignment may change the metric type or the value type of the time series.Time series data must be aligned in order to perform cross- time series reduction. If crossSeriesReducer is specified, then perSeriesAligner must be specified and not equal ALIGN_NONE and alignmentPeriod must be specified; otherwise, an error is returned. Possible values: ["ALIGN_NONE", "ALIGN_DELTA", "ALIGN_RATE", "ALIGN_INTERPOLATE", "ALIGN_NEXT_OLDER", "ALIGN_MIN", "ALIGN_MAX", "ALIGN_MEAN", "ALIGN_COUNT", "ALIGN_SUM", "ALIGN_STDDEV", "ALIGN_COUNT_TRUE", "ALIGN_COUNT_FALSE", "ALIGN_FRACTION_TRUE", "ALIGN_PERCENTILE_99", "ALIGN_PERCENTILE_95", "ALIGN_PERCENTILE_50", "ALIGN_PERCENTILE_05", "ALIGN_PERCENT_CHANGE"].  
`conditions[].conditionThreshold.denominatorFilter` _Optional_ |  `string` A filter that identifies a time series that should be used as the denominator of a ratio that will be compared with the threshold. If a denominator_filter is specified, the time series specified by the filter field will be used as the numerator.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length.  
`conditions[].conditionThreshold.duration` _Required*_ |  `string` The amount of time that a time series must violate the threshold to be considered failing. Currently, only values that are a multiple of a minute--e.g., 0, 60, 120, or 300 seconds--are supported. If an invalid value is given, an error will be returned. When choosing a duration, it is useful to keep in mind the frequency of the underlying time series data (which may also be affected by any alignments specified in the aggregations field); a good duration is long enough so that a single outlier does not generate spurious alerts, but short enough that unhealthy states are detected and alerted on quickly.  
`conditions[].conditionThreshold.evaluationMissingData` _Optional_ |  `string` A condition control that determines how metric-threshold conditions are evaluated when data stops arriving. Possible values: ["EVALUATION_MISSING_DATA_INACTIVE", "EVALUATION_MISSING_DATA_ACTIVE", "EVALUATION_MISSING_DATA_NO_OP"].  
`conditions[].conditionThreshold.filter` _Optional_ |  `string` A filter that identifies which time series should be compared with the threshold.The filter is similar to the one that is specified in the MetricService.ListTimeSeries request (that call is useful to verify the time series that will be retrieved / processed) and must specify the metric type and optionally may contain restrictions on resource type, resource labels, and metric labels. This field may not exceed 2048 Unicode characters in length.  
`conditions[].conditionThreshold.forecastOptions` _Optional_ |  `object` When this field is present, the 'MetricThreshold' condition forecasts whether the time series is predicted to violate the threshold within the 'forecastHorizon'. When this field is not set, the 'MetricThreshold' tests the current value of the timeseries against the threshold.  
`conditions[].conditionThreshold.forecastOptions.forecastHorizon` _Required*_ |  `string` The length of time into the future to forecast whether a timeseries will violate the threshold. If the predicted value is found to violate the threshold, and the violation is observed in all forecasts made for the Configured 'duration', then the timeseries is considered to be failing.  
`conditions[].conditionThreshold.thresholdValue` _Optional_ |  `float` A value against which to compare the time series.  
`conditions[].conditionThreshold.trigger` _Optional_ |  `object` The number/percent of time series for which the comparison must hold in order for the condition to trigger. If unspecified, then the condition will trigger if the comparison is true for any of the time series that have been identified by filter and aggregations, or by the ratio, if denominator_filter and denominator_aggregations are specified.  
`conditions[].conditionThreshold.trigger.count` _Optional_ |  `integer` The absolute number of time series that must fail the predicate for the condition to be triggered.  
`conditions[].conditionThreshold.trigger.percent` _Optional_ |  `float` The percentage of time series that must fail the predicate for the condition to be triggered.  
`conditions[].displayName` _Required_ |  `string` A short name or phrase used to identify the condition in dashboards, notifications, and incidents. To avoid confusion, don't use the same display name for multiple conditions in the same policy.  
`conditions[].name` _Optional_ |  `string` The unique resource name for this condition. Its syntax is: projects/[PROJECT_ID]/alertPolicies/[POLICY_ID]/conditions/[CONDITION_ID] [CONDITION_ID] is assigned by Stackdriver Monitoring when the condition is created as part of a new or updated alerting policy.  
`displayName` _Required_ |  `string` A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion, don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode characters.  
`documentation` _Optional_ |  `object` Documentation that is included with notifications and incidents related to this policy. Best practice is for the documentation to include information to help responders understand, mitigate, escalate, and correct the underlying problems detected by the alerting policy. Notification channels that have limited capacity might not show this documentation.  
`documentation.content` _Optional_ |  `string` The text of the documentation, interpreted according to mimeType. The content may not exceed 8,192 Unicode characters and may not exceed more than 10,240 bytes when encoded in UTF-8 format, whichever is smaller.  
`documentation.mimeType` _Optional_ |  `string` The format of the content field. Presently, only the value "text/markdown" is supported.  
`enabled` _Optional_ |  `boolean` Whether or not the policy is enabled. The default is true.  
`notificationChannels` _Optional_ |  `list (object)`  
`notificationChannels[]` _Optional_ |  `object` MonitoringNotificationChannelRef is a reference to a MonitoringNotificationChannel.  
`notificationChannels[].external` _Optional_ |  `string` A reference to an externally managed MonitoringNotificationChannel resource. Should be in the format "projects/{{projectID}}/notificationChannels/{{channelID}}".  
`notificationChannels[].name` _Optional_ |  `string` The name of a MonitoringNotificationChannel resource.  
`notificationChannels[].namespace` _Optional_ |  `string` The namespace of a MonitoringNotificationChannel resource.  
`resourceID` _Optional_ |  `string` Immutable. Optional. The service-generated name of the resource. Used for acquisition only. Leave unset to create a new resource.  
`severity` _Optional_ |  `string` The severity of an alert policy indicates how important incidents generated by that policy are. The severity level will be displayed on the Incident detail page and in notifications. Possible values: ["CRITICAL", "ERROR", "WARNING"].  
  
* Field is required when parent field is specified

### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    creationRecord:
    - mutateTime: string
      mutatedBy: string
    name: string
    observedGeneration: integer
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observations of the MonitoringAlertPolicy's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`creationRecord` |  `list (object)` A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be ignored.  
`creationRecord[]` |  `object`  
`creationRecord[].mutateTime` |  `string` When the change occurred.  
`creationRecord[].mutatedBy` |  `string` The email address of the user making the change.  
`name` |  `string` The unique resource name for this policy. Its syntax is: projects/[PROJECT_ID]/alertPolicies/[ALERT_POLICY_ID].  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
  
## Sample YAML(s)

### Instance Performance Alert Policy
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: monitoring.cnrm.cloud.google.com/v1beta1
    kind: MonitoringAlertPolicy
    metadata:
      labels:
        checking: instance-performance-bug
        oncall-treatment: urgent-meltdown
      name: monitoringalertpolicy-sample-instanceperformance
    spec:
      displayName: Sample Computing Instance Performance Alert Policy
      enabled: true
      notificationChannels:
        - name: monitoringalertpolicy-dep-instanceperformance
      combiner: AND_WITH_MATCHING_RESOURCE
      conditions:
      - displayName: CPU usage is extremely high
        conditionThreshold:
          filter: metric.type="compute.googleapis.com/instance/cpu/utilization" AND resource.type="gce_instance"
          aggregations:
          - perSeriesAligner: ALIGN_MAX
            alignmentPeriod: 60s
            crossSeriesReducer: REDUCE_MEAN
            groupByFields:
            - project
            - resource.label.instance_id
            - resource.label.zone
          comparison: COMPARISON_GT
          thresholdValue: 0.9
          duration: 900s
          trigger:
            count: 1
      - displayName: CPU usage is increasing at a high rate
        conditionThreshold:
          filter: metric.type="compute.googleapis.com/instance/cpu/utilization" AND resource.type="gce_instance"
          aggregations:
          - alignmentPeriod: 900s
            perSeriesAligner: ALIGN_PERCENT_CHANGE
          comparison: COMPARISON_GT
          thresholdValue: 0.5
          duration: 180s
          trigger:
            count: 1
      - displayName: Process 'nginx' is not running
        conditionThreshold:
          filter: select_process_count("has_substring(\"nginx\")", "www") AND resource.type="gce_instance"
          comparison: COMPARISON_LT
          thresholdValue: 1
          duration: 300s
      documentation:
        content: |-
          This sample is an amalgamation of policy samples found at https://cloud.google.com/monitoring/alerts/policies-in-json. It is meant to give an idea of what is possible rather than be a completely realistic alerting policy in and of itself.
    
          Combiner AND_WITH_MATCHING_RESOURCE
          While more general policies will use an OR combiner, triggering an incident when any of their conditions are met, AND combiners only trigger when all of their conditions are met, allowing for specification of very specific circumstances.
          AND_WITH_MATCHING_RESOURCE combiners go one step further and only trigger when all conditions are met for the same resource, in this case, a GCE instance.
    
          Metric-threshold condition
          The first condition in this policy, "CPU usage is extremely high", tests average CPU usage in a group of VMs.
    
          Rate-of-change condition
          The second condition in this policy, "CPU usage is increasing at a high rate" tests if the rate of CPU utilization is increasing rapidly.
    
          Process-health condition
          The third condition in this policy, "Process 'nginx' is not running", tests if there is no process matching the string nginx and running as user www available for more than 5 minutes.
    
          All together, this policy would monitor for a situation where the lack of an 'nginx' process caused a spike in CPU usage in the same instance and elevated CPU usage across all instances in its group.
    ---
    apiVersion: monitoring.cnrm.cloud.google.com/v1beta1
    kind: MonitoringNotificationChannel
    metadata:
      name: monitoringalertpolicy-dep-instanceperformance
    spec:
      type: sms
      labels:
        number: "12025550196"
    

### Network Connectivity Alert Policy
    
    
    # Copyright 2020 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: monitoring.cnrm.cloud.google.com/v1beta1
    kind: MonitoringAlertPolicy
    metadata:
      labels:
        checking: website-health
        oncall-treatment: stay-aware
      name: monitoringalertpolicy-sample-networkconnectivity
    spec:
      displayName: Sample Website Aetwork Connectivity Alert Policy
      enabled: true
      notificationChannels:
        - name: monitoringalertpolicy-dep1-networkconnectivity
        - name: monitoringalertpolicy-dep2-networkconnectivity
      combiner: OR
      conditions:
      - displayName: Failure of uptime check_id uptime-check-for-google-cloud-site
        conditionThreshold:
          filter: metric.type="monitoring.googleapis.com/uptime_check/check_passed" AND metric.label.check_id="uptime-check-for-google-cloud-site" AND resource.type="uptime_url"
          aggregations:
          - perSeriesAligner: ALIGN_NEXT_OLDER
            alignmentPeriod: 1200s
            crossSeriesReducer: REDUCE_COUNT_FALSE
            groupByFields:
            - resource.label.*
          comparison: COMPARISON_GT
          thresholdValue: 1
          duration: 600s
          trigger:
            count: 1
      - displayName: SSL Certificate for google-cloud-site expiring soon
        conditionThreshold:
          filter: metric.type="monitoring.googleapis.com/uptime_check/time_until_ssl_cert_expires" AND metric.label.check_id="uptime-check-for-google-cloud-site" AND resource.type="uptime_url"
          aggregations:
          - alignmentPeriod: 1200s
            perSeriesAligner: ALIGN_NEXT_OLDER
            crossSeriesReducer: REDUCE_MEAN
            groupByFields:
            - resource.label.*
          comparison: COMPARISON_LT
          thresholdValue: 15
          duration: 600s
          trigger:
            count: 1
      - displayName: Uptime check running
        conditionAbsent:
          filter: metric.type="monitoring.googleapis.com/uptime_check/check_passed" AND metric.label.check_id="uptime-check-for-google-cloud-site" AND resource.type="uptime_url"
          duration: 3900s
      - displayName: Ratio of HTTP 500s error-response counts to all HTTP response counts
        conditionThreshold:
          filter: metric.label.response_code>="500" AND metric.label.response_code<"600" AND metric.type="appengine.googleapis.com/http/server/response_count" AND resource.type="gae_app"
          aggregations:
          - alignmentPeriod: 300s
            perSeriesAligner: ALIGN_DELTA
            crossSeriesReducer: REDUCE_SUM
            groupByFields:
            - project
            - resource.label.module_id
            - resource.label.version_id
          denominatorFilter: metric.type="appengine.googleapis.com/http/server/response_count" AND resource.type="gae_app"
          denominatorAggregations:
          - alignmentPeriod: 300s
            perSeriesAligner: ALIGN_DELTA
            crossSeriesReducer: REDUCE_SUM
            groupByFields:
            - project
            - resource.label.module_id
            - resource.label.version_id
          comparison: COMPARISON_GT
          thresholdValue: 0.5
          duration: 0s
          trigger:
            count: 1
      documentation:
        content: |-
          This sample is a synthesis of policy samples found at https://cloud.google.com/monitoring/alerts/policies-in-json. It is meant to give an idea of what is possible rather than be a completely realistic alerting policy in and of itself.
    
          Combiner OR
          OR combiner policies will trigger an incident when any of their conditions are met. They should be considered the default for most purposes.
    
          Uptime-check conditions
          The first three conditions in this policy involve an uptime check with the ID 'uptime-check-for-google-cloud-site'.
    
          The first condition, "Failure of uptime check_id uptime-check-for-google-cloud-site", tests if the uptime check fails.
          The second condition, "SSL Certificate for google-cloud-site expiring soon", tests if the SSL certificate on the Google Cloud site will expire in under 15 days.
    
          Metric-absence condition
          The third condition in this policy, "Uptime check running" tests if the aforementioned uptime check is not written to for a period of approximately an hour.
          Note that unlike all the conditions so far, the condition used here is conditionAbsent, because the test is for the lack of a metric.
    
          Metric ratio
          The fourth and last condition in this policy, "Ratio of HTTP 500s error-response counts to all HTTP response counts", tests that 5XX error codes do not make up more than half of all HTTP responses. It targets a different set of metrics through appengine.
          
          All together, this policy would monitor for a situation where any of the above conditions threatened the health of the website.
    ---
    apiVersion: monitoring.cnrm.cloud.google.com/v1beta1
    kind: MonitoringNotificationChannel
    metadata:
      name: monitoringalertpolicy-dep1-networkconnectivity
    spec:
      type: sms
      labels:
        number: "12025550196"
    ---
    apiVersion: monitoring.cnrm.cloud.google.com/v1beta1
    kind: MonitoringNotificationChannel
    metadata:
      name: monitoringalertpolicy-dep2-networkconnectivity
    spec:
      type: email
      labels:
        email_address: dev@example.com
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
