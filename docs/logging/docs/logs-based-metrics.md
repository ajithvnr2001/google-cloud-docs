---
url: https://docs.cloud.google.com/logging/docs/logs-based-metrics/
title: Log-based metrics overview \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:08.154398+00:00
---

# Log-based metrics overview  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/logs-based-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Log-based metrics overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a conceptual overview of log-based metrics. These metrics can help you observe trends and patterns in a large volume of log entries.

## About log-based metrics

Log-based metrics are [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) metrics that are derived from the content of log entries. For example, you can use a log-based metric to count the number of log entries that contain a particular message or to extract latency information recorded in log entries. You can display log-based metrics in Cloud Monitoring charts, and alerting policies can monitor these metrics.

Log-based metrics can apply at the project level or log bucket level. Bucket-scoped log-based metrics are useful when you use aggregated sinks to route log entries to a log bucket, and when you route log entries from one project to a log bucket in another project. For more information, see the section of this page titled Sources of log-based metrics.

## How time-series values for log-based metrics are determined

This section briefly describes how the values in a time series for a counter-type log-based metric are determined. It also describes why a time series for a log-based metric might have gaps. The process is similar for distribution-valued log-based metrics.

For counter-type log-based metrics, Logging does the following:

  1. It creates one or more data streams and for each stream, it manages a set of in-memory counters.

There is one stream for each combination of unique values for the set of metric and resource labels. Each in-memory counter is for a different time interval, but each counter records the number of log entries that match the filter and that have a timestamp which corresponds to the interval.

  2. Every minute, for each stream, the Logging backend uses the values of the in-memory counters to determine how to update a time series that is managed by Cloud Monitoring.

If there are five streams, then there are five time series managed by Monitoring. You can chart these time series. You can also create alerting policies to monitor these time series.

**Note:** A time series for a log-based metric can include values of zero and can have data gaps. If you plan to create an alerting policy to monitor a log-based metric, then we recommend that you configure how the policy [handles missing data](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#partial-metric-data).



### Example: How zero values can cause data gaps

Consider the following time series:
    
    
    Example time series: (T1, -), (T2, -), (T3, 0), (T4, 1), (T5, 0), (T6, -)
    

In the previous expression, `(T1, -)` means that no value was written for time `T1`. This corresponds to a gap in the values in the time series. In contrast `(T3, 0)` means that the value of the time series at time `T3` is zero.

For each stream, the backend system for log-based metrics uses the following rules to determine what value to write to the time series stored by Monitoring:

  * When the aggregated count for an interval is non-zero, that value is written to the time series.

In the example time series, only the interval `T4` has a non-zero value. The value of `1` indicates that one log entry with a timestamp that corresponds to the `T4` interval matched the filter of the log-based metric.

  * When the aggregated count for an interval is zero, a value of zero is written to the time series when an adjacent interval has a non-zero value.

In the example time series, at time `T3`, the aggregated count is zero. However, a value of zero is written because at time `T4` the aggregated count is non-zero. Similarly, at time `T5`, the aggregated count is zero. A value of zero is written to the time series because the value for the previous interval was non-zero.

  * Otherwise, the time series isn't updated and there is a data gap for the interval.

In the example time series, there is no value for intervals `T1`, `T2`, and `T6`. In these intervals, the aggregated counts were zero and the counts for the adjacent intervals were also zero.




### Handling of late-arriving and future log entries

When log entries arrive with a timestamp for an interval that has been processed, the Logging backend generates historical data. The historical data is used to update the previously-written counts.

When log entries arrive with a timestamp that is in the future, the Logging backend accumulates these counts. In the time series, these log entries are counted when their timestamp corresponds to the current interval.

## Sources of log-based metrics

You can use the metrics defined by Cloud Logging to collect general usage information, and you can define your own log-based metric to capture information specific to your application or business.

Log-based metrics can apply within a single Google Cloud project or within a log bucket. You can't create log-based metrics for other Google Cloud resources such as Cloud Billing accounts or organizations.

For information about the differences between project-based log-based metrics and bucket-based log-based metrics, see [Bucket-scoped log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/bucket-lbm).

### System-defined metrics

Logging provides a set of metrics for usage values such as the number of log entries stored in log buckets in your project, or the number of bytes you've exported. For a complete list of system-defined metrics, see [Google Cloud metrics: logging](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-logging).

System-defined log-based metrics apply at the project level.

The Log Router counts a log entry when all of the following are true: 

  * The log entry passes through the log sinks of the project where the log-based metric is defined.
  * The log entry is stored in a log bucket. The log bucket can be in any project.

For example, suppose project `A` has a log sink whose destination is project `B`. Also assume that the log sinks in the project `B` route the log entries to a log bucket. In this scenario, the log entries routed from project `A` to project `B` contribute to project `A`'s system-defined log-based metrics. These log entries also contribute to project `B`'s system-defined log-based metrics.




### User-defined metrics

You can create user-defined log-based metrics to track other metrics that are important for your project. For example, you might create a log-based metric to count the number of log entries that match a given filter.

By default, user-defined log-based metrics are calculated from all logs received by the Logging API for the Google Cloud project, regardless of any [inclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#inclusion-filters) or [exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions) that might apply to the Google Cloud project.

You can also create user-defined log-based metrics for a specific log bucket in a Google Cloud project. Bucket-scoped log-based metrics are calculated from all logs destined for the bucket, regardless of where they originated. For more information see [Log-based metrics on log buckets](https://docs.cloud.google.com/logging/docs/logs-based-metrics/bucket-lbm).

The Log Router counts a log entry when all of the following are true: 

  * Billing is enabled on the project where the log-based metric is defined.
  * For bucket-scoped metrics, the log entry is stored in the log bucket where the log-based metric is defined.
  * For project-scoped metrics, the log entry passes through the log sinks of the project where the log-based metric is defined.



## Data types for log-based metrics

Log-based metrics can extract data from logs to create metrics of the following types:

  * Counter: these metrics count the number of log entries that match a specified filter within a specific period. Use counters when you want to keep track of the number of times a value or string appears in your logs.
  * Distribution: these metrics also count values, but they collect the counts into ranges of values (_histogram buckets_). Use distributions when you want to extract values like latencies.
  * Boolean: these metrics capture whether or not a log entry matches a specified filter.



User-defined log-based metrics can be of the counter or distribution metric types. Most system-defined log-based metrics are counters, but some are of the boolean type. The characteristics of counters and distributions are described in more detail in subsequent sections.

The data for a user-defined log-based metric comes only from log entries received _after the metric is created_. A metric isn't retroactively populated with data from log entries that are already in Logging.

System log-based metrics are calculated from included logs only. User-defined log-based metrics are calculated from both included and excluded logs.

The following sections describe the characteristics of counter-type and distribution-type metrics.

### Counter metrics

_Counter metrics_ count the number of log entries matching a given filter. For example, you can do the following:

  * Count the log entries that contain a certain specific error message.
  * Count the number of times each user invokes an operation, by looking for log messages that match this pattern:

`... user USERNAME called OPERATION ...`

By extracting USERNAME and OPERATION and using them as values for two labels, you can later ask, "How many times did `sally` call the `update` operation?", "How many people called the `read` operation?", "How many times did `george` call an operation?", and so on.




For more information, see [Configure counter metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/counter-metrics).

### Distribution metrics

_Distribution metrics_ accumulate numeric data from log entries matching a filter. The metrics contain a time series of distribution objects, each of which contains the following:

  * A count of the number of values in the distribution.
  * The mean of the values.
  * The sum of squared deviations: _Sum i=1..n(xi–mean)2_
  * A set of histogram buckets with the count of values in each bucket. You can use the default bucket layout or choose your own.



A common use for distribution metrics is to track latencies. As each log entry is received, a latency value is extracted from somewhere in the log entry and is added to the distribution. At regular intervals, the accumulated distribution is written to Cloud Monitoring.

For information about distributions, including their format within a time series and how they are visualized, see [Charting distribution metrics](https://docs.cloud.google.com/monitoring/charts/charting-distribution-metrics).

For information about creating distribution log-based metrics, see [Configure distribution metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/distribution-metrics).

## Resource types

We recommend that your log-based metrics specify a single resource type. This specification ensures that the time series generated for your log-based metric matches the data model expected by Cloud Monitoring. It also simplifies the process of creating charts and alerting policies, as there is no ambiguity as to which time-series data is charted or monitored.

Consider a log-based metric with the following filter:
    
    
    severity>="ERROR"
    resource.type="gce_instance"
    

Cloud Monitoring recognizes that this data is for a Compute Engine VM instance. Therefore, when you create a chart for a VM instance, your log-based metric is listed as an option in the menus. When you create a chart for a different resource type, your log-based metric isn't listed as an option.

If you create a log-based metric without specifying a resource type, then Monitoring lists your log-based metric as an option for multiple resource types, even though you don't count entries from those resources.

## Labels

Log-based metrics can have labels, which allow multiple time series to be collected for the metric. Values for the labels are extracted from fields in the matching log entries. Logging records separate time series for each combination of label values.

Most log-based metrics provide a default `log` label. This label holds the value of the LOG_ID portion of the [`logName` field in the log entry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.log_name), for example, `cloudresourcemanager.googleapis.com%2Factivity`.

System log-based metrics have predefined labels that can't be changed.

User-defined log-based metrics can include labels that you define. Typically, these labels extract values from the log entries that contribute to the log-based metric.

For example, you can use labels in the log-based metric to record the folder or organization from which a log entry originated, even though bucket-scoped log-based metrics can't be created for folders or organizations. For more information, see [Log-based metric labels](https://docs.cloud.google.com/logging/docs/logs-based-metrics/labels).

## Charts and alerting policies in Cloud Monitoring

You can use both system and user-defined log-based metrics in Cloud Monitoring to create charts and alerting policies. For these charts and alerting policies, you can use labels to filter or combine time series. For example, you can set a filter to show only certain time series. For more information, see [List and chart log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/view_your_log_based_metrics) and [Alert on log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/charts-and-alerts).

In Cloud Monitoring, log-based metrics use the following naming patterns:

  * System: `logging.googleapis.com/SYSTEM_METRIC_NAME`
  * User-defined: `logging.googleapis.com/user/USER_METRIC_NAME`



Note that user-defined log-based metrics include the string `user`.

## Visibility to Monitoring metrics scopes

Log-based metrics are ingested by Cloud Monitoring, and the visibility of metric data to a Google Cloud project is determined by a metrics scope. A _metrics scope_ is a list of projects that are monitored by the project that hosts the metrics scope; the hosting project is called a _scoping project_.

By default, each project hosts a metrics scope that includes only itself, so a project is a scoping project for itself. Therefore, your metrics, including log-based metrics, are visible only to your Google Cloud project.

You can also create a multi-project metrics scope for the scoping project. With a multi-project metrics scope, the scoping project can see the metrics from all the projects in the metrics scope. What is visible to the individual projects in a multi-project metrics scope is determined by the metrics scope hosted by each of those projects. The fact that two projects are in a multi-project metrics scope does not mean that each project has access to the metric or configuration data in the other project.

A single project can also appear in multiple metrics scopes. The metrics from such a project are visible to the scoping projects of each of those metrics scopes.

Metrics, including log-based metrics, are defined within a specific project. When that project appears in multiple metrics scopes, the metrics are visible to projects other than the one in which they are defined. For information about how metrics scopes and bucket-scoped log-based metrics interact, see [Projects and metrics scopes](https://docs.cloud.google.com/logging/docs/logs-based-metrics/bucket-lbm#bucket-lbm-scoping).

For more information about metrics scopes, including multi-project metrics scopes, and about scoping projects, see the following:

  * [Metrics scopes](https://docs.cloud.google.com/monitoring/settings#concept-scope)
  * [View metrics for multiple projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects)



## Limitations

You can't create log-based metrics that count the number of log entries that contain an error group. You also can't extract the ID of an error group into a label attached to a log-based metric.

## Quotas and limits

For information about the quotas and limits associated with user-defined log-based metrics, see [Log-based metrics quotas and limits](https://docs.cloud.google.com/logging/quotas#metric-limits).

## Troubleshooting

If you encounter issues when using log-based metrics, see [Troubleshoot log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/troubleshooting).

## Pricing

All user-defined log-based metrics are a class of Cloud Monitoring custom metrics and are chargeable. For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
