---
url: https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs/
title: Monitor your logs \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:29.397283+00:00
---

# Monitor your logs  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Monitor your logs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can use Cloud Monitoring to observe trends in your log data and to notify you when conditions that you specify occur. To provide Cloud Monitoring with data from your log data, Logging supports the following features:

  * You can generate custom metrics from your log entries. These metrics are called **log-based-metrics**. You can also create _metric-based alerting policies_ to notify you when a log-based metric meets a condition. For more information, see [Visualize log entry data with log-based metrics](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs#lbm).

  * You can use alerting policies to monitor, in near real time, when a message appears in your log entries. These alerting policies are called _log-based alerting policies_. For more information, see [Monitor individual log entries for messages](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs#lba).

  * You can write a SQL query in Observability Analytics and create an alerting policy that monitors the results of the query. These alerting policies are called _SQL-based alerting policies_. For more information, see [Monitor SQL query results](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs#sql).

SQL-based alerting policies is in Public Preview.




The rest of this document describes the differences between these three alerting policies, and provides information about authorization, costs, and limits.

## Visualize log entry data with log-based metrics

When you want to monitor recurring events in your log data over time, use log-based metrics. Log-based metrics generate numeric data from your log data and they are suitable when you want to do any of the following:

  * Count the occurrences of a message, like a warning or error, in your log data and receive a notification when the number of occurrences crosses a threshold.
  * Observe trends in your data, like latency values in your log data, and receive a notification when the values change in an unacceptable way.
  * Create charts to display the extracted numeric data.



Because log-based metrics generate numeric data from your log data, you can use these metrics in alerting policies and display them in charts. For information about creating alerting policies and charts for log-based metrics, see [Configure notifications for log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/charts-and-alerts).

Cloud Monitoring provides a set of predefined log-based metrics, and you can define your own. To see a list of the system-defined log-based metrics, click the following _add_circle_ button:

### System-defined log-based metrics

The "metric type" strings in this table must be prefixed with `logging.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`billing/bytes_ingested` GA ** _(project)_**   
Bytes streamed into log buckets   
`DELTA`, `INT64`, `By`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Number of bytes streamed into log buckets for indexing, querying, and analysis; includes up to 30 days of storage. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`resource_type`: Monitored resource type for the log entry.   
`billing/bytes_stored` GA ** _(project)_**   
Logging Retention   
`GAUGE`, `INT64`, `By`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Volume of logs that are retained past the default 30 days. No data exists when the retention period of a log bucket is never larger than 30 days. This metric might have a value of zero when the retention period of a log bucket is shortened to 30 days. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`data_type`: This field indicates that log volume reported here is charged for retention past the default 30 days. The data_type for all reported retention is set to `CHARGED`.   
`log_bucket_location`: The location where the log bucket resides.   
`log_bucket_id`: The id of the log bucket.   
`billing/log_bucket_bytes_ingested` GA ** _(project)_**   
Bytes streamed into log buckets   
`DELTA`, `INT64`, `By`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Number of bytes streamed into log buckets for indexing, querying, and analysis; includes up to 30 days of storage. Sampled every 60 seconds. After sampling, data is not visible for up to 300 seconds._   
`log_source`: The resource container where the log comes from.   
`resource_type`: Monitored resource type for the logs streamed into log buckets.   
`log_bucket_location`: The location where the log bucket resides.   
`log_bucket_id`: The id of the log bucket.   
`billing/log_bucket_monthly_bytes_ingested` GA ** _(project)_**   
Bytes streamed into log buckets monthly   
`GAUGE`, `INT64`, `By`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Number of bytes streamed into log buckets for indexing, querying, and analysis for this month-to-date; include up to 30 days of storage. Sampled every 1800 seconds. After sampling, data is not visible for up to 6000 seconds._   
`log_source`: The resource container where the log comes from.   
`resource_type`: Monitored resource type for the logs streamed into log buckets.   
`log_bucket_location`: The location where the log bucket resides.   
`log_bucket_id`: The id of the log bucket.   
`billing/monthly_bytes_ingested` GA ** _(project)_**   
Monthly bytes streamed into log buckets   
`GAUGE`, `INT64`, `By`   
**[global](https://docs.cloud.google.com/monitoring/api/resources#tag_global)** |  _Month-to-date number of bytes streamed into log buckets for indexing, querying, and analysis; includes up to 30 days of storage. Sampled every 1800 seconds. After sampling, data is not visible for up to 6000 seconds._   
`resource_type`: Monitored resource type for the log entry.   
`byte_count` GA ** _(project)_**   
Log bytes   
`DELTA`, `INT64`, `By` |  _Total bytes of log entries, either written directly or routed to this project via project-sink, that are stored in at least one log bucket. Sampled every 60 seconds._   
`log`: Name of the log.   
`severity`: Severity of the log entry.   
`dropped_log_entry_count` DEPRECATED ** _(project)_**   
Logs-based metric errors (Deprecated)   
`DELTA`, `INT64`, `1` |  _Use "logging.googleapis.com/logs_based_metrics_error_count" instead. Sampled every 60 seconds._   
`log`: Name of the log.   
`exports/byte_count` GA ** _(project)_**   
Exported log bytes   
`DELTA`, `INT64`, `By`   
**[logging_sink](https://docs.cloud.google.com/monitoring/api/resources#tag_logging_sink)** |  _Number of bytes in log entries that were exported. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._  
`exports/error_count` GA ** _(project)_**   
Exported log entries failures   
`DELTA`, `INT64`, `1`   
**[logging_sink](https://docs.cloud.google.com/monitoring/api/resources#tag_logging_sink)** |  _Number of log entries that failed to be exported. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._  
`exports/log_entry_count` GA ** _(project)_**   
Exported log entries   
`DELTA`, `INT64`, `1`   
**[logging_sink](https://docs.cloud.google.com/monitoring/api/resources#tag_logging_sink)** |  _Number of log entries that were exported. Sampled every 60 seconds. After sampling, data is not visible for up to 420 seconds._  
`log_entry_count` GA ** _(project)_**   
Log entries   
`DELTA`, `INT64`, `1` |  _Number of log entries, either written directly or routed to this project via project-sink, that are stored in at least one log bucket. By default, log entries are stored for 30 days. Excluded logs are not counted. Sampled every 60 seconds._   
`log`: Name of the log.   
`severity`: Severity of the log entry.   
`logs_based_metrics_error_count` GA ** _(project)_**   
Logs-based metric errors   
`DELTA`, `INT64`, `1` |  _Number of log entries, either written directly or routed to this project via project-sink, and are stored in a log bucket but excluded from any system or user-defined logs-based metrics. This condition can occur if the timestamp of a log entry is more than 24 hours older, or 10 minutes newer, than the actual receive time. Sampled every 60 seconds._   
`log`: Name of the log.   
`metric_label_cardinality` BETA ** _(project)_**   
Logs-based metric active cardinality count by label   
`GAUGE`, `INT64`, `1`   
**[metric](https://docs.cloud.google.com/monitoring/api/resources#tag_metric)** |  _Cardinality estimate for each metric label of a logs-based metric. The estimate is computed over approximately 25 hours. Sampled every 60 seconds. After sampling, data is not visible for up to 270 seconds._   
`label`: Name of the metric label.   
`metric_label_throttled` BETA ** _(project)_**   
Logs-based metric label throttled status   
`GAUGE`, `BOOL`, ``   
**[metric](https://docs.cloud.google.com/monitoring/api/resources#tag_metric)** |  _Indicates if metric labels are being dropped for logs-based metrics due to exceeding cardinality limits. Sampled every 60 seconds. After sampling, data is not visible for up to 270 seconds._   
`label`: Name of the metric label.   
`metric_throttled` GA ** _(project)_**   
Logs-based metric throttled status   
`GAUGE`, `BOOL`, ``   
**[metric](https://docs.cloud.google.com/monitoring/api/resources#tag_metric)** |  _Indicates if labels or points are being dropped for logs-based metrics due to exceeding active time series (cardinality) limits. Sampled every 60 seconds. After sampling, data is not visible for up to 270 seconds._  
`time_series_count` BETA ** _(project)_**   
Logs-based metric active time series (cardinality) count   
`GAUGE`, `INT64`, `1`   
**[metric](https://docs.cloud.google.com/monitoring/api/resources#tag_metric)** |  _Active time series (cardinality) estimates for logs-based metrics. Only metric labels are counted and the estimate is computed over approximately 25 hours. Sampled every 60 seconds. After sampling, data is not visible for up to 270 seconds._  
  
Table generated at 2026-10-14 20:24:33 UTC.

### User-defined log-based metrics

You can create log-based metrics to extract numeric data from your log data. User-defined log-based metrics calculate values from both included and excluded log entries.

By default, user-defined log-based metrics collect data from all log entries received by the Log Router in your Google Cloud project, but you can define log-based metrics that collect data from log entries routed to a specific log bucket.

  * For information about defining and using project-level log-based metrics, see [Using log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics).
  * For information about defining and using bucket-level log-based metrics, see [Log-based metrics on log buckets](https://docs.cloud.google.com/logging/docs/logs-based-metrics/bucket-lbm).



If you define your own log-based metrics, you might incur charges. For more information about costs associated with metric ingestion, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).

## Monitor individual log entries for messages

When you want to be notified anytime a specific message occurs in a log entry, use log-based alerting policies. Log-based alerting policies are useful for catching security-related events in log entries, like the following:

  * You want to be notified when an event appears in an audit log; for example, a human user accesses the security key of a service account.
  * Your application writes deployment messages to logs, and you want to be notified when a deployment change is logged.



Log-based alerting policies are useful for events that you expect to be both rare and important. You don't want to know about a trend or pattern; you want to know that something occurred.

Log-based alerting policies are defined in a project, and they scan a log entry when the following conditions are true:

  * Billing is enabled.
  * The log entry originates in a project.
  * Sinks in the project where the log entry originates, or in a project to which the log entry is routed, route the log entry to a log bucket.

For example, assume a log entry originates in project `A`. If a log sink in project `A` routes the log entry to a log bucket, then log-based alerting policies defined in project `A` scan the log entry.

As a second example, assume a log entry originates in project `X` and that a log sink in project `X` routes the log entry to project `Y`. If a sink in project `Y` routes the log entry to a log bucket, then log-based alerting policies defined in project `X` and in project `Y` scan the log entry.




You can't use log-based alerting policies to monitor log entries that originate in folders, billing accounts, or organizations, or to monitor log entries that aren't stored in log buckets. If you create aggregated sinks, then these sinks might intercept a log entry and prevent it from being routed by the sinks in the project where the log entry originates.

For information about creating log-based alerting policies, see [Configure log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

## Monitor SQL query results

You can configure alerting policies that use Observability Analytics to run SQL queries on your log entry data. These types of alerting policies are effective when you want to get notified based on patterns that can't be evaluated by log-based alerting policies, such as complex patterns in log entries or aggregations of log data. For more information, see [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting).

## Comparison of alerting options

This section compares alerting policies built on log-based metrics, log-based alerting policies, and SQL-based alerting policies.

### Summary table

The following table summarizes the alerting techniques and provides links to additional information:

Metric-based alerting policies | Log-based alerting policies | SQL-based alerting policies | More information  
---|---|---|---  
Based on metrics derived from log entries | Based on strings in individual log entries | Based on tables returned by SQL queries over log entries | Log-based metrics  
Log-based alerting  
[SQL-based alerting](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting)  
Used to notify you of trends over time | Used to notify you when a specific message appears in a log | Used to notify you of a pattern in a window of log entries | Log-based metrics  
Log-based alerting  
[SQL-based alerting](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting)  
Calculated from 

  * Included log entries (system-defined log-based metrics)
  * Included and excluded log entries (user-defined log-based metrics)

| Match only included log entries | Calculated from log entries in a sliding window | Available log entries  
[SQL-based alerting](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting)  
Operate on metrics from all projects in the metrics scope of the scoping project | Operate on log entries that satisfy the following conditions: 

  * The log entry originates in the project where the policy is defined.
  * Sinks in the project where the log entry originates, or in a project to which the log entry is routed, route the log entry to a log bucket.

| Operate on log views which are accessible through linked BigQuery datasets. These datasets can be in any project. | Metrics scope  
[Linked BigQuery datasets](https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset)  
Alert is created when the value of a metric meets a condition for a specified period | Alert is created each time a specific log entry matches a filter | Alert is created when the table of query results meets a condition | Alerts and notifications  
Created and managed in Monitoring | Created in Logging;  
managed in Monitoring | Created in Observability Analytics; managed in Monitoring | Creating and managing alerting policies  
[SQL-based alerting](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting)  
Viewed in Monitoring | Viewed in Monitoring | Viewed in Monitoring | Viewing alerting policies  
Can use any notification channel supported in Monitoring | Can use any notification channel supported in Monitoring | Can use any notification channel supported in Monitoring | Notification channels  
  
### Available log entries

This section describes which log entries are available to be counted by a log-based metric and which can be monitored by a log-based alerting policy.

#### Log entries that log-based metrics can count

[User-defined log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics#user-defined_metrics) are calculated from all log entries received by the Logging API for the Google Cloud project, regardless of any [inclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#inclusion-filters) or [exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions) that may apply to the Google Cloud project. If you create an alerting policy based on a user-defined log-based metric, then the policy monitors data from all log entries.

[System-defined log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics#system-defined_metrics) are calculated only from log entries that have been stored in log buckets in the Google Cloud project. If a log has been explicitly [excluded](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions), then it isn't included in these metrics. If you create an alerting policy based on a system-defined log-based metric, then the policy monitors data only from included log entries.

#### Log entries that log-based alerting policies can monitor

Log-based alerting policies are defined in a project, and they scan a log entry when the following conditions are true:

  * Billing is enabled.
  * The log entry originates in a project.
  * Sinks in the project where the log entry originates, or in a project to which the log entry is routed, route the log entry to a log bucket.

For example, assume a log entry originates in project `A`. If a log sink in project `A` routes the log entry to a log bucket, then log-based alerting policies defined in project `A` scan the log entry.

As a second example, assume a log entry originates in project `X` and that a log sink in project `X` routes the log entry to project `Y`. If a sink in project `Y` routes the log entry to a log bucket, then log-based alerting policies defined in project `X` and in project `Y` scan the log entry.




You can't use log-based alerting policies to monitor log entries that originate in folders, billing accounts, or organizations, or to monitor log entries that aren't stored in log buckets. If you create aggregated sinks, then these sinks might intercept a log entry and prevent it from being routed by the sinks in the project where the log entry originates.

#### Log entries that SQL-based alerting policies can monitor

SQL-based alerting policies don't have access to individual logs. Instead, these policies query linked BigQuery datasets and then monitor the query result. The linked BigQuery datasets provide access to the data in log views.

Each log view is on a log bucket. You create the [linked BigQuery dataset for that log bucket](https://docs.cloud.google.com/logging/docs/buckets#link-bq-dataset) after you [upgrade the log bucket to use Observability Analytics](https://docs.cloud.google.com/logging/docs/buckets#upgrade-bucket).

For more information about SQL-based alerting policies, see [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting).

### Monitor metrics across multiple projects

You can monitor metrics from several projects by configuring a metrics scope. A _metrics scope_ lists all the projects and accounts that it monitors. A _scoping project_ hosts the metrics scope. The scoping project stores the alerting policies and other configurations that you create for the metrics scope. The scoping project for a metrics scope is the project selected by the Google Cloud console project picker.

Alerting policies based on log-based metrics, like alerting policies based on other metrics, work across all projects in the metrics scope of the scoping project.

The metrics scope isn't relevant to alerting policies based on log entries, like log-based and SQL-based policies.

For more information about metrics scopes, including multi-project metrics scopes, and about scoping projects, see the following:

  * [Metrics scopes](https://docs.cloud.google.com/monitoring/settings)
  * [View metrics for multiple projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects)



### Alerts and notifications

When the condition of an alerting policy is met, Monitoring opens an alert and sends notifications to the notification channels of the alerting policy. To see the details of the alert, click **View alert** in the notification message, or navigate directly to the **Alerts** page in Monitoring.

#### Alerts for metric-based alerting policies

Alerting policies based on log-based metrics create alert and notifications like all other metric-based alerting policies in Monitoring, as described in [Alerting behavior](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth). For more information about managing alerts for metric-based alerting policies, see [Alerts for metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/incidents-events).

#### Alerts for log-based alerting policies

**The content in this section applies only to[log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts). These policies monitor individual log entries. It doesn't apply to alerting policies that monitor metric data—including log-based metrics—or SQL query results**.

**Note:** If the query of your log-based alerting policy extracts labels, then each combination of extracted label values represents its own alert timeline. For example, assume a log-based alerting policy extracts one label and that label has two possible values. For this alerting policy, you can have two open alerts, one for each label value.

When Cloud Logging writes the log entry to a log bucket, each log-based alerting policy scans the log entry. If a log entry matches the filter of the alerting policy, then Cloud Logging extracts labels and forwards the data to Cloud Monitoring.

Upon receiving data from Cloud Logging, Cloud Monitoring uses the following rules to determine what actions to take:

  * If there are no open alerts for the alerting policy, Monitoring opens a new alert and sends a notification.

When extracted labels are available, the identifying information for the alert includes those labels.

  * If there is a closed alert whose extracted label values match the extracted label values for the current log entry, then Monitoring either re-opens the closed alert or it opens a new alert. Monitoring determines what action to take based on whether the closed alert has been purged, which might take up to three minutes.

  * If there is an open alert whose label values match the extracted label values for the current log entry, then the system either sends another notification or does nothing. The system behavior depends on whether the alerting policy has exceeded a alert or notification limit.




For each log-based alerting policy, the following limits apply:

  * A maximum of 20 alerts per day per log-based alerting policy.

When this limit is met, the notification includes a statement similar to the following: "Maximum of 20 daily alerts has been reached. Alerts for this policy will resume within the next 24 hours."

The daily limit resets at a random time. This reset interval is not user-configurable.

  * A maximum of 2 new alerts per minute per log-based alerting policy.

When a log-based alerting policy extracts label values, this limit might prevent you from receiving notifications that you expect. For example, suppose a log-based alerting policy extracts one label that has five possible values. In any one-minute interval, the system can open at most 2 alerts.

  * The minimum interval between repeated notifications for an open alert is 5 minutes. You can configure this interval when you create or edit your alerting policy.




Alerts automatically close when the time period specified by the auto-close duration elapses, without a repeat of the cause of the alert. By default, the auto-close duration is 7 days. Due to repeat events, alert can stay open longer than the auto-close duration.

For more information about managing alerts for log-based alerting policies, see [Manage alerts for log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-incidents).

#### Alerts for SQL-based alerting policies

For SQL-based alerting policies, Cloud Monitoring creates an alert the first time the result of the SQL query meets the condition specified in the policy. Each alerting policy has only one open alert. While the alert is open, if the condition is met again, Monitoring doesn't create further alerts or send additional notifications. Monitoring closes SQL-based alerts after seven days, unless you configure a shorter alert closure period or close the alert on your own.

For more information about managing alerts for SQL-based alerting policies, see [Manage alerts for SQL-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/sql-based-incidents).

### Creating and managing alerting policies

You create, modify, and delete alerting policies based on log-based metrics in Cloud Monitoring, like any other metric-based alerting policy. For more information, see [Managing policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#managing_policies).

You can create log-based alerting policies by using the Logs Explorer or the Cloud Monitoring API. You modify and delete log-based alerting policies in Monitoring or with the Cloud Monitoring API. For more information, see [Managing log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

You can create SQL-based alerting policies by using Observability Analytics or the Cloud Monitoring API. You modify and delete SQL-based alerting policies in Monitoring or by using the Cloud Monitoring API. For more information, see [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting).

### Viewing alerting policies

The **Policies** page in Monitoring lists all the alerting policies in your Google Cloud project. This list includes policies that use log-based metrics and log-based alerting policies.

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select **See all policies**.



Log-based alerting policies appear in the list with the value `Logs` in the **Type** column. Alerting policies based on metrics, including log-based metrics, appear in the list with the value `Metrics` in the **Type** column. SQL-based alerting policies appear in the list with the value `SQL` in the **Types** column. The following screenshot shows an excerpt of a policy list:

![To view alerting policies by type, use the **Type** column in the list of
alerting policies.](https://docs.cloud.google.com/static/logging/docs/images/alert-policy-list-w-lba.png)

### Notification channels

You can send notifications from any type of alerting policy to any of the notification channels supported by Monitoring. You must configure these channels before you can use them in alerting policies.

For more information, see [Managing notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

## Authorization requirements

Using log-based metrics or log-based alerting policies requires authorization for both Cloud Logging and Cloud Monitoring.

  * For user-defined log-based metrics, see [Permissions for log-based metrics](https://docs.cloud.google.com/logging/docs/access-control#metrics-permissions).

  * For log-based alerting policies, see [Permissions for log-based alerting policies](https://docs.cloud.google.com/logging/docs/access-control#lba-permissions).

  * For SQL-based alerting policies, see [Permissions for SQL-based alerting policies](https://docs.cloud.google.com/logging/docs/access-control#sql-permissions).




## Limits

This section lists limits for log-based metrics and limits for alerting policies. The limits for alerting policies depend on the type of data the policy monitors.

### Limits for log-based metrics

There are limits on the number and structure of user-defined log-based metrics. For more information about these limits, see [limits for log-based metrics](https://docs.cloud.google.com/logging/quotas#metric-limits).

### Limits for alerting policies

The first two columns in the following table list a category and limit value. The third column lists the types of policies to which the limit applies:

  * **Metric:** Applies to alerting policies that monitor metric data—including log-based metrics.
  * **LBA:** Applies to alerting policies that monitor log entries. These policies are called log-based alerting policies.
  * **SQL:** Applies to alerting policies that monitor a SQL query result.
  * **All:** Applies to all alerting policies.

Category | Value | Policy type  
---|---|---  
Alerting policies (sum of metric and log) [per metrics scope ](https://docs.cloud.google.com/monitoring/settings)1 | 2,000 | Metric, LBA  
Conditions per metric-based alerting policy | 6 | Metric  
Conditions per [SQL-based alerting policy](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting)  
(Public Preview) | 1 | SQL  
Maximum query execution time for a  
SQL-based alerting policy  
(Public Preview) | 5 minutes | SQL  
Maximum time period that a  
metric-absence condition evaluates2 | 1 day | Metric  
Maximum time period that a  
metric-threshold condition evaluates2 | 25 hours | Metric  
Maximum time period that a  
PromQL condition evaluates | 2 years | Metric  
Maximum length of the filter used  
in a metric-threshold condition | 2,048 Unicode characters | Metric  
Maximum number of time series  
monitored by a forecast condition | 64 | Metric  
Minimum forecast window | 1 hour (3,600 seconds) | Metric  
Maximum forecast window | 2.5 days (216,000 seconds) | Metric  
Notification channels per alerting policy | 16 | All  
Maximum number of new alerts  
per log-based alerting policy | 20 alerts per day | LBA  
Maximum number of notifications3  
per log-based alerting policy | 20 notifications per day | LBA  
Maximum rate of new alerts  
per log-based alerting policy | 2 new alerts per minute | LBA  
Minimum interval between notifications for an open alert4  
per log-based alerting policy | 5 minutes | LBA  
Maximum number of simultaneously triggering alerting policies   
per project | 80,000 | All  
Maximum number of simultaneously open alerts  
per alerting policy | 1,000 | All  
Period after which an alert with no new data is  
automatically closed | 7 days | Metric, SQL  
Maximum duration of an alert if not manually closed | 7 days | LBA  
Retention of closed alerts | 13 months | Not applicable  
Retention of open alerts | Indefinite | Not applicable  
Notification channels [per metrics scope ](https://docs.cloud.google.com/monitoring/settings) | 4,000 | Not applicable  
Maximum number of alerting policies per snooze | 16 | All  
Retention of a snooze | 13 months | Not applicable  
1You can request to increase this limit from the default of 2,000 policies per metrics scope up to 10,000 policies per metrics scope.  
2The maximum time period that a condition evaluates is the sum of the alignment period and the duration window values. For example, if the alignment period is set to 15 hours, and the duration window is set 15 hours, then 30 hours of data is required to evaluate the condition.  
3Monitoring generates notifications for an open alert when the minimum time between notifications elapses and a log entry matches the alert labels. If a log-based alert policy is snoozed when Monitoring generates a notification, then the notification is discarded and it isn't sent to the policy's notification channels. Otherwise, Monitoring sends the notification to the alerting policy's notification channels. All notifications that Monitoring generates count towards the alerting policy's limit of 20 notifications per day.  
4If the query of your log-based alerting policy extracts labels, then each combination of extracted label values represents its own alert timeline. Therefore, you can receive multiple notifications within 5 minutes. 

## Pricing

To learn about pricing for Cloud Logging, see the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
