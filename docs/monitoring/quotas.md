---
url: https://docs.cloud.google.com/monitoring/quotas/
title: Cloud Monitoring quotas and limits \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:22.616644+00:00
---

# Cloud Monitoring quotas and limits  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Resources ](https://docs.cloud.google.com/monitoring/quotas)



Send feedback 

#  Cloud Monitoring quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Cloud Monitoring.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

There are also _system limits_ on Monitoring resources. System limits can't be changed. 

## User-defined metrics

The Cloud Monitoring **Metrics Management** page provides information that can help you control the amount you spend on billable metrics without affecting observability. The **Metrics Management** page reports the following information: 

  * Ingestion volumes for both byte- and sample-based billing, across metric domains and for individual metrics.
  * Data about labels and cardinality of metrics.
  * Number of reads for each metric.
  * Use of metrics in alerting policies and custom dashboards.
  * Rate of metric-write errors.



You can also use the **Metrics Management** page to [exclude unneeded metrics](https://docs.cloud.google.com/monitoring/docs/metrics-management#exclude-metrics), eliminating the cost of ingesting them. For more information about the **Metrics Management** page, see [View and manage metric usage](https://docs.cloud.google.com/monitoring/docs/metrics-management).

Category | Maximum value  
---|---  
[Custom metric descriptors](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics) per project1 | 10,000  
Labels per custom, external, and workload metric descriptor | 30  
Labels per Prometheus metric descriptor | 200  
String length for label key | 100  
String length for label value | 1024  
Time series included in a write request2 | 200  
Rate at which data can be written to a single time series3 | one point each 5 seconds  
Histogram [buckets](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#BucketOptions) per custom [distribution metric](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Distribution) | 200  
Workload, Prometheus, and [external4 metric descriptors](https://docs.cloud.google.com/monitoring/api/metrics_other) per project | 25,000  
Active [time series](https://docs.cloud.google.com/monitoring/api/v3/metric-model#time-series) from custom metrics per monitored resource5 | 200,000  
Active [time series](https://docs.cloud.google.com/monitoring/api/v3/metric-model#time-series) from workload metrics per monitored resource5 | 200,000  
Active [time series](https://docs.cloud.google.com/monitoring/api/v3/metric-model#time-series) from Prometheus per monitored resource5 | 1,000,000  
Active [time series](https://docs.cloud.google.com/monitoring/api/v3/metric-model#time-series) from external metrics per monitored resource5 | 200,000  
Rate at which metric descriptors can be created | 6,000 per minute per project  
  
1 This limit is imposed by Cloud Monitoring. Other services might impose lower maximum values. Custom metrics are those written to `custom.googleapis.com`.   
2 You can write only one data point for each time series in a request, so this limit also functions as the maximum number of points that can be written per request.    
3 The Cloud Monitoring API requires that the end times of points written to a time series be at least 5 seconds apart. You can batch write points to a time series, provided that the data points are written in order.    
4 External metrics are those written to `external.googleapis.com`.    
5 A time series is active if you have written data points to it within the previous 24 hours. The limit specified in the row is the total number of active time series for a single monitored resource (for example, a single `gce_instance` VM or a single `k8s_container` container) across all user-defined metrics within that row (custom, workload, Prometheus, or external). An exception is the `global` monitored resource, for which the limit applies to each user-defined metric separately. This is a system-wide safety limit and isn't customizable. 

## Monitoring API quotas and limits

Category | Maximum value  
---|---  
Limits to API usage |  To find the API quotas and limits, do one of the following:

  * In the Google Cloud console, go to the [Quotas dashboard page](https://console.cloud.google.com/iam-admin/quotas).
  * In the Cloud Shell, run the [`gcloud alpha services quota list`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/quota/list) command.

  
Lifetime of API page tokens | 24 hours  
Maximum response size | 200 MB Applies to the size of the serialized response payload, which includes both the raw data and the label keys and values for every time series returned. If a query's response exceeds 200 MB, then the request fails with a `RESOURCE_EXHAUSTED` (HTTP 429 Too Many Requests) error. To prevent or resolve `RESOURCE_EXHAUSTED` errors, do the following:

  * Reduce the cardinality of your metrics or apply filters to reduce the number of time series.
  * Increase the alignment period.
  * Decrease the time range of the query.
  * If you are using PromQL, then consider implementing [Recording Rules](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed).

  
  
## About Monitoring API quotas

The Monitoring API has quota limits for the rates of time-series ingestion requests and time-series queries. Ingestion requests are calls that write time-series data, and queries are calls that retrieve time-series data. There are also internal limits on other Monitoring API endpoints; these endpoints aren't intended to handle high rates of requests.

To reduce the number of API requests you issue when your services write time-series data, use one API request to write data for multiple time series. We recommend that you write at least 10 objects per request. For more information about batching API requests, see [`timeSeries.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create).

If, after batching your API requests, you still require a higher Monitoring API quota limits, contact [Google Cloud Support](https://docs.cloud.google.com/support).

The other limits are fixed and are described in this document.

For more information, see the [Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/overview).

## Telemetry API quotas and limits for metric ingestion

This section describes the quotas and limits that apply to the [Telemetry (OTLP) API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) when used for [metric ingestion](https://docs.cloud.google.com/stackdriver/docs/otlp/overview). The Telemetry API implements the [OpenTelemetry OTLP specification](https://opentelemetry.io/docs/specs/otlp/).

Description | Value | Note  
---|---|---  
Maximum number of datapoints per request | 200 | Limit  
Maximum number of ResourceMetrics per request | 200 | Limit  
Maximum number of quantiles per Summary metric | 10 | Limit  
Number of metric-ingestion requests per minute per region (quota) | 60,000 | Quota  
  
Using the Telemetry API does not consume Cloud Monitoring API ingestion quota. After metrics are ingested, the other Cloud Monitoring quotas and limits described in this document apply.

## Data retention

Metric data points older than the retention period are deleted from time series.

Category | Value  
---|---  
Retention of data points from custom, external, and agent metric types, including: 

  * Custom metrics, prefix `custom.googleapis.com`
  * Metrics from [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) and [OpenTelemetry's OTLP exporter](https://docs.cloud.google.com/stackdriver/docs/otlp/overview), prefix `prometheus.googleapis.com`2
  * [Agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent), prefix `agent.googleapis.com`, including  
all `processes` metrics.
  * External metrics, prefix `external.googleapis.com`
  * Other workload metrics sent by non-OTLP OpenTelemetry exporters, prefix `workload.googleapis.com`

| 24 months1  
Retention of data points for some Google Cloud services, including most metrics within the following categories: 

  * Compute Engine metrics, prefix `compute.googleapis.com`
  * GKE and GKE Enterprise metrics, prefix `kubernetes.io`
  * Cloud Storage metrics, prefix `storage.googleapis.com`
  * BigQuery metrics, prefix `bigquery.googleapis.com`
  * Cloud SQL metrics, prefix `cloudsql.googleapis.com`
  * Internal, https, and L7 load balancer metrics, prefix `loadbalancing.googleapis.com`

|  24 months1  
Retention of data points from all other metric types, including: 

  * All other [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp)
  * [Istio metrics](https://docs.cloud.google.com/monitoring/api/metrics_istio)
  * [AWS metrics](https://docs.cloud.google.com/monitoring/api/metrics_aws)
  * [Log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics)

| 6 weeks  
Lifetime of API page tokens | 24 hours  
  
1 Metric data is stored for 6 weeks at its original sampling frequency, then it is down-sampled to 10-minute intervals for extended storage.    
2 Google Cloud Managed Service for Prometheus and OTLP metric data is stored for 1 week at its original sampling frequency, then it is down-sampled to 1-minute intervals for the next 5 weeks, then it is down-sampled to 10-minute intervals for extended storage. 

## Resource groups

Category | Value  
---|---  
Number of resource groups [per metrics scope ](https://docs.cloud.google.com/monitoring/settings) | 500  
Maximum number of groups included in an email report1 | 10  
  
1 When you configure Cloud Monitoring email reports, you can request information on utilization of your resource groups. Due to a limitation in the email reporter, the generated reports include information for only 10 groups.

## Monitored project limits

Cloud Monitoring officially supports up to 375 Google Cloud projects [per metrics scope ](https://docs.cloud.google.com/monitoring/settings).

You can add up to 3,500 Google Cloud projects per metrics scope , but you might experience performance issues, especially when querying custom metrics or historical data. Cloud Monitoring guarantees performant queries and charts only for 375 Google Cloud projects per metrics scope .

To raise your Google Cloud projects per metrics scope quota, you can request an increase of the "Monitored Projects / Monitoring Metrics Scope" quota. See the documentation about [managing your quota](https://docs.cloud.google.com/docs/quotas/view-manage) for more details.

## Limits on creating and updating metric descriptors

Cloud Monitoring enforces a per-minute rate limit on creating new metrics, on adding new label names to existing metrics, and on deleting metrics. This rate limit is usually only hit when first integrating with Cloud Monitoring, for example when you migrate an existing, mature Prometheus deployment to Cloud Monitoring. **This is not a rate limit on ingesting data points**. This rate limit only applies when creating never-before-seen metrics or when adding new label names to existing metrics.

This quota is fixed, but any issues should automatically resolve as new metrics and metric labels get created up to the per-minute limit.

## Limits for alerting

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

## Limits for SMS messages

The SMS message limits are applied on a 24-hour rolling window.

Category | Value  
---|---  
Number of SMS verification codes | 40  
Number of SMS verification codes per phone number | 5  
Number of SMS alert messages | 2,500  
Number of SMS alert messages per phone number | 200  
  
## Limits for synthetic monitors

Category | Value  
---|---  
Uptime checks [per metrics scope ](https://docs.cloud.google.com/monitoring/settings)* | 100  
Maximum number of [ICMP pings](https://docs.cloud.google.com/monitoring/uptime-checks#ping) per public uptime check | 3  
Synthetic monitors [per metrics scope ](https://docs.cloud.google.com/monitoring/settings) | 100†  
*This limit applies to the number of uptime-check configurations. Each uptime-check configuration includes the time interval between testing the status of the specified resource.  
†For information about how to increase this limit, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).  


## Limits for charting

Category | Value  
---|---  
Dashboards [per metrics scope ](https://docs.cloud.google.com/monitoring/settings) | 1000  
Charts on a dashboard | 100  
Dashboard version history retention | 90 days  
Lines on a chart | 50*  
Rows in a table | 300  
Maximum number of alerting policies per **Alerts** widget | 20  
Maximum number of resources per **Alerts** widget | 20  
Maximum number of characters in the query of a logs panel widget | 2,000  
*This limit is applied for performance reasons. When there more than 50 time series to chart, an icon with a red dot is added to the toolbar. The tooltip for the icon displays the message `To improve performance, we've limited the time series displayed in this chart`. To display all time series, expand the tooltip and select the button labeled **Show All Time Series**.

## Service-level objectives

Category | Value  
---|---  
Number of SLOs per service | 500  
  
## Limits on Tags

Category | Value  
---|---  
Maximum number of teams per project when using [Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) for access control | 250  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
