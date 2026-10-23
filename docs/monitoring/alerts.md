---
url: https://docs.cloud.google.com/monitoring/alerts/
title: Alerting overview \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:20:19.384826+00:00
---

# Alerting overview  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Alerting overview Stay organized with collections  Save and categorize content based on your preferences. 

Alerting policies in Cloud Monitoring detect application and infrastructure issues by evaluating metric, log, or SQL query results. When the monitored data meets the conditions that you specify, Monitoring creates an alert and sends notifications.

## How alerting works

The Cloud Monitoring alerting process contains three parts:

  * An _alerting policy_ , which describes the circumstances under which you want to be alerted and how you want to be notified about an alert. The alerting policy can monitor time-series data stored by Monitoring or logs stored by Cloud Logging. When that data meets the alerting policy condition, Monitoring creates an [alert](https://docs.cloud.google.com/monitoring/alerts/incidents-events) and sends the notifications.

  * Each _alert_ is a record of the type of data that was monitored and when the conditions were met. This information can help you troubleshoot the issues that caused the alert.

  * A _[notification channel](https://docs.cloud.google.com/monitoring/support/notification-options)_ defines how you receive notifications when Monitoring creates an alert. For example, you can configure an alerting policy to email `my-support-team@example.com` and to post a Slack message to the channel `#my-support-team`. An alerting policy can contain one or more notification channels.




Alerting policies can evaluate three types of data:

  * Time-series data, also called metric data, which is stored by Monitoring. These types of policies are called _metric-based_ alerting policies.

To learn how to set up a metric-based alerting policy, try the [Quickstart for Compute Engine](https://docs.cloud.google.com/monitoring/monitor-compute-engine-virtual-machine).

  * Log entry data stored by Cloud Logging. Alerting policies that evaluate individual log entries are called _log-based_ alerting policies. Log-based alerting policies notify you when a particular message appears in your logs. For more information, see [Monitor your logs](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

  * The results of a SQL query run in [Observability Analytics](https://docs.cloud.google.com/logging/docs/analyze/query-and-view) against log entry data stored in Logging. Alerting policies that monitor the results of a SQL query are called _SQL-based alerting policies_. For more information, see [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting).

SQL-based alerting policies is in Public Preview.




The alerting process helps you respond to issues when the performance of an application fails to meet acceptable values. For example, you deploy a web application onto a Compute Engine virtual machine (VM) instance. While you expect the [HTTP response latency](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#appengine/http/server/response_latencies) to fluctuate, you want your support team to respond when the application has high latency for a significant time period. You could create a metric-based alerting policy that monitors the application's HTTP response latency metric. If the response latency is higher than two seconds for at least five minutes, then Monitoring creates an alert and sends email notifications to your support team.

## How to create an alerting policy

There are multiple ways to create an alerting policy. For example, you can use pre-configured alerting policies by enabling recommended alerts from integrations or certain pages in the Google Cloud console. You can also configure a new alerting policy by using the Google Cloud console, the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api/v3), the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/policies) and [Terraform](https://docs.cloud.google.com/monitoring/alerts/terraform).

### Use integrations and recommended alerting policies

Monitoring provides pre-built packages to let you create alerting policies for your Google Cloud services and third-party integrations. The packages include recommended alerting policies, sample dashboards, and key metrics for the service. These packages are available for Google Cloud services such as Google Kubernetes Engine, Compute Engine, and Cloud SQL, and common third-party integrations such as MongoDB, Kafka, and Elasticsearch.

When you install a package, you can enable the package's recommended alerting policies. When you enable a recommended alerting policy, you configure its notification channel and optionally modify other values. After configuration, the alerting policy begins monitoring its target immediately, with no further user input required.

Recommended alerting policies are helpful when you've deployed a new service and want to alert on important metrics. For example, the Cloud SQL integration package comes with recommended alerting policies for failed instances and slow transactions:

![Two of the recommended alerting policies for the Cloud SQL integration package.](https://docs.cloud.google.com/static/monitoring/images/recommended-alerts.png)

To learn more, see the following documents:

  * [Install alerting policies](https://docs.cloud.google.com/monitoring/agent/integrations#install-alertpols).
  * [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).
  * [Monitoring third-party applications](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party).



### Create new alerting policies

You can create alerting policies to monitor different types of data depending on your alerting needs. The following sections list the different types of data that you can monitor with alerting policies.

#### Monitor time series data

Condition Type | Description | Example  
---|---|---  
Metric-threshold condition | Metric-threshold conditions are met when the values of a metric are more than, or less than, a threshold for a specific retest window. For more information, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui) and [Create alerting policies by using the API](https://docs.cloud.google.com/monitoring/alerts/policies-in-api). | You want an alerting policy that sends a notification when response latency is 500ms or higher for five consecutive [uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks) over 10 minutes.  
Metric-absence condition | Metric-absence conditions are met when a monitored time series has no data for a specific retest window. The maximum retest window is 24 hours. For more information, see [Create metric-absence alerting policies](https://docs.cloud.google.com/monitoring/alerts/metric-absence) and [Create alerting policies by using the API](https://docs.cloud.google.com/monitoring/alerts/policies-in-api). | You want an alerting policy that opens an alert with your support team when a resource doesn't respond to any HTTP requests over the course of five minutes.  
Prometheus Query Language (PromQL) condition | PromQL is a functional query language used to evaluate time series data in real time. Your PromQL queries can use any valid expression, such as metric combinations, ratios, and dynamic thresholds based on a metric. For more information, see [PromQL in Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql) and [PromQL alerting overview](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting). | You want to use a PromQL alerting expression found in a public repository, you want an alerting policy that is based on more than one metric such as a ratio, or you want an alerting policy that operates over more than 25 hours of data.  
Forecasted metric-value condition | Forecasted metric-value conditions are met when the alerting policy predicts that the threshold will be violated within the upcoming forecast window. The forecast window can range from 1 hour to 7 days. For more information, see [Create forecasted metric-value alerting policies](https://docs.cloud.google.com/monitoring/alerts/metric-forecast) and [Create alerting policies by using the API](https://docs.cloud.google.com/monitoring/alerts/policies-in-api). | You want an alerting policy that opens an alert with your support team when a resource is likely to reach 80% disk space usage within the next 24 hours.  
  
We recommend filtering on the labels defined on [monitored-resource types](https://docs.cloud.google.com/monitoring/api/resources) instead of labels defined on [metric types](https://docs.cloud.google.com/monitoring/api/metrics) when possible, particularly if you are querying high-cardinality metrics. If you have a resource label and a metric label that capture similar information, then use the resource label in your queries.

For example, if your monitored resource includes a `cluster` label and your metric includes a `kubernetes_cluster_name` label that captures similar information, then filter on the resource `cluster` label.

Don't rely on the values of [ system- or user-defined resource metadata labels](https://docs.cloud.google.com/monitoring/api/v3/metric-model#meta-labels) when selecting time series for sensitive alerting policies. Instead, use the values of labels defined by the [monitored-resource types](https://docs.cloud.google.com/monitoring/api/resources). 

Resource metadata labels are added asynchronously to time series and aren't subject to the same [ latency expectations](https://docs.cloud.google.com/monitoring/api/v3/latency-n-retention#latency) as values of labels defined metric types or monitored-resource types. Therefore, an alerting policy that depends on metadata values to trigger an action can behave erratically if the population of resource metadata labels is delayed.

#### Monitor log entry data

To monitor individual log entries, use a log-based alerting policy. A condition on a log-based alerting policy is met when the alerting policy detects that a phrase from a log entry match the alerting policy criteria. For example, you want an alerting policy that opens an alert with your support team when a log entry's `message` contains `product_ids=['tier_1_support', 'tier_2_support']`.

For more information, see [Configure log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts) in the Logging documentation.

#### Monitor SQL query results

To monitor SQL query results, use a SQL-based alerting policy. The condition of a SQL-based alerting policy periodically analyzes your log entry data and then create alerts when the table of query results meets certain criteria. This type of alerting policy is helpful when you need an alerting policy that monitors aggregations of data or complex patterns across multiple log entries. For example, you want to get notified when more than 50 log entries in the last 60 minutes have a severity of `WARNING`.

For more information, see [Monitor your SQL query results with an alerting policy](https://docs.cloud.google.com/logging/docs/analyze/sql-in-alerting) in the Logging documentation.

## Alerting policy components

Each alerting policy has the following components:

  * A condition that describes when a resource, or a group of resources, is in a state that requires you to respond. The condition includes the data source, a static or dynamic threshold, and data aggregation methods such as filters and groupby. Your conditions can monitor a single metric, multiple metrics, or a ratio of metrics. You can also use the [Prometheus Query Language (PromQL)](https://prometheus.io/docs/prometheus/latest/querying/basics/) to include complex expressions such as dynamic thresholds and conditional logic.

If you use an integration to enable a recommended alerting policy, then the alerting policy condition is pre-populated.

  * A list of notification channels that describe who to notify when action is required. For more information, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

  * Documentation that appears in notifications and alert pages. You can [configure the subject line of a notification](https://docs.cloud.google.com/monitoring/alerts/doc-variables#subjects), and you can add helpful information to the body of the notification. For example, you might configure the notification to display links to internal playbooks or to Google Cloud pages such as custom dashboards. For more information about documentation, including examples, see [Annotate alerts with user-defined documentation](https://docs.cloud.google.com/monitoring/alerts/doc-variables).




## Manage alerting policies and alerts

After an alerting policy is enabled, Monitoring continuously monitors the conditions of that policy. You can't configure the alerting policy to monitor conditions only for certain time periods. If you want to disable the alerting policy for a certain time period, then create a [snooze](https://docs.cloud.google.com/monitoring/alerts/snooze).

If an alert is open and Monitoring determines that the conditions of the metric-based policy are no longer met, then Monitoring automatically closes the alert and sends a notification about the closure.

## Pricing

To learn about pricing for Cloud Monitoring, see the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

For information about how to monitor the number of trace spans or logs that are ingested, or how to be notified when specific content is included in a log entry, see the following documents:

  * [Alerting on monthly log ingestion](https://docs.cloud.google.com/stackdriver/docs/observability/pricing-optimize-and-monitor#logging-alert-log-bytes)
  * [Alerting on monthly trace span ingestion](https://docs.cloud.google.com/stackdriver/docs/observability/pricing-optimize-and-monitor#trace-alert-span-usage)
  * [Configure log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts)



## What's next

  * For information about notification latency and how the choices for the parameters of an alerting policy affect when notifications are sent, see [Behavior of metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth).

  * For a list of metric-based policy examples, including how to use JSON to write a metric-threshold condition that monitors a ratio of metric types, see [Summary of example alerting policies](https://docs.cloud.google.com/monitoring/alerts/types-of-conditions).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
