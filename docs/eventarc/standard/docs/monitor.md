---
url: https://docs.cloud.google.com/eventarc/standard/docs/monitor/
title: Observability in Eventarc \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:05:46.498631+00:00
---

# Observability in Eventarc  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Observability in Eventarc Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview) [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

[Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) lets you monitor the health, activity, and performance of your Eventarc resources. Eventarc automatically sends audit logs to Cloud Logging for troubleshooting and streams metrics to Cloud Monitoring for trend analysis and alerting.

## Send audit logs to Cloud Logging

Eventarc sends the following types of audit log data to Cloud Logging:

  * [Admin Activity audit logs](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
  * [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access)
  * [System Event audit logs](https://docs.cloud.google.com/logging/docs/audit#system-event)
  * [Policy Denied audit logs](https://docs.cloud.google.com/logging/docs/audit#policy_denied)



Data Access audit logs are [disabled by default](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) because these audit logs can be quite large.

For more information, see [Eventarc audit logging](https://docs.cloud.google.com/eventarc/standard/docs/audit-logs) and [Eventarc publishing audit logging](https://docs.cloud.google.com/eventarc/standard/docs/audit-logs-publishing). 

### Query and view logs

You can use following tools to view and analyze your logs:

  * **Logs Explorer** is designed to help you troubleshoot and analyze the performance of your services and applications. To learn how to view logs in the Logs Explorer, follow the instructions in [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).
  * **Observability Analytics** is designed to run queries to analyze your logs, and then view or chart the results. To learn how to use Observability Analytics, follow the instructions in [Query and analyze logs with Observability Analytics](https://docs.cloud.google.com/logging/docs/analyze/query-and-view).



You can filter for Eventarc logs in the Logs Explorer by searching for `eventarc` in the search field.

For more information about querying and analyzing logs, see [Query and view logs overview](https://docs.cloud.google.com/logging/docs/log-analytics).

## Send metrics to Cloud Monitoring

Eventarc sends metric data from monitored resources to Google Cloud Observability. A monitored resource in Monitoring represents a logical or physical entity, such as a virtual machine, a database, or an application. Monitored resources contain a unique set of metrics that can be explored, reported through a dashboard, or used to create alerts. Each resource also has a set of resource labels, which are key-value pairs that hold additional information about the resource. Resource labels are available for all metrics associated with the resource.

Eventarc sends metric data from the following monitored resource to Google Cloud Observability:

  * [`eventarc.googleapis.com/Location`](https://docs.cloud.google.com/monitoring/api/resources#tag_eventarc.googleapis.com/Location)



### Resource metrics and labels

The "metric type" strings in this table must be prefixed with `eventarc.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`quota/enrollments_per_message_bus/exceeded` GA ** _(project)_**   
Enrollments per message bus quota exceeded error   
`DELTA`, `INT64`, `1`   
**[eventarc.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_eventarc.googleapis.com/Location)** |  _Number of attempts to exceed the limit on quota metric eventarc.googleapis.com/enrollments_per_message_bus. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`message_bus`: The message bus that the enrollments are attached to.   
`quota/enrollments_per_message_bus/limit` GA ** _(project)_**   
Enrollments per message bus quota limit   
`GAUGE`, `INT64`, `1`   
**[eventarc.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_eventarc.googleapis.com/Location)** |  _Current limit on quota metric eventarc.googleapis.com/enrollments_per_message_bus. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`message_bus`: The message bus that the enrollments are attached to.   
`quota/enrollments_per_message_bus/usage` GA ** _(project)_**   
Enrollments per message bus quota usage   
`GAUGE`, `INT64`, `1`   
**[eventarc.googleapis.com/Location](https://docs.cloud.google.com/monitoring/api/resources#tag_eventarc.googleapis.com/Location)** |  _Current usage on quota metric eventarc.googleapis.com/enrollments_per_message_bus. After sampling, data is not visible for up to 150 seconds._   
`limit_name`: The limit name.   
`message_bus`: The message bus that the enrollments are attached to.   
  
Table generated at 2026-10-08 15:22:12 UTC.

To view all resource types, see [Monitored resource types](https://docs.cloud.google.com/monitoring/api/resources). To view all metric types, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

### Read metric data

You can read metric data, also called time-series data, by using the `timeSeries.list` method in the Cloud Monitoring API. There are several ways to call the method, including using a language-specific client library, or by creating a chart with [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer). For an introduction to metrics and time series, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics). To learn how to read your metric data, see [Retrieve time-series data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics).

### Use Monitoring dashboards and alerts

You can use Monitoring dashboards and their associated charts to visualize the data for Eventarc metrics.

To monitor these metrics in Monitoring, you can [create custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards#custom_dashboards). You can also [add alerts](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api) based on these metrics.

## What's next

  * [Eventarc audit logging](https://docs.cloud.google.com/eventarc/standard/docs/audit-logs)
  * [Troubleshoot issues](https://docs.cloud.google.com/eventarc/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
