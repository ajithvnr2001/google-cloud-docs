---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-cm/
title: Query using Cloud Monitoring \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:14.205279+00:00
---

# Query using Cloud Monitoring  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-cm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Query using Cloud Monitoring Stay organized with collections  Save and categorize content based on your preferences. 

After you have deployed Google Cloud Managed Service for Prometheus, you can query the data sent to the managed service and display the results in charts and dashboards.

This document describes _metrics scopes_ , which determine the data you can query, and how to use Cloud Monitoring to retrieve and use the data you've collected.

All query interfaces for Managed Service for Prometheus are configured to retrieve data from Monarch using the Cloud Monitoring API. By querying Monarch instead of querying data from local Prometheus servers, you get global monitoring at scale.

## Before you begin

If you have not already deployed the managed service, then set up [managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) or [self-deployed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged). You can skip this if you're only interested in [querying Cloud Monitoring metrics using PromQL](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/promql).

## Queries and metrics scopes

The data you can query is determined by the Cloud Monitoring construct _metrics scope_ , regardless of the method you use to query the data.

A Monitoring metrics scope is a read-time-only construct that lets you query metric data belonging to multiple Google Cloud projects. Every metrics scope is hosted by a designated Google Cloud project, called the _scoping project_.

By default, a project is the scoping project for its own metrics scope, and the metrics scope contains the metrics and configuration for that project. A scoping project can have more than one monitored project in its metrics scope, and the metrics and configurations from all the monitored projects in the metrics scope are visible to the scoping project. A monitored project can also belong to more than one metrics scope.

When you query the metrics in a scoping project, and if that scoping project hosts a multi-project metrics scope, you can retrieve data from multiple projects. If your metrics scope contains all your projects, then your queries and rules evaluate globally.

For more information about scoping projects and metrics scope, see [Metrics scopes](https://docs.cloud.google.com/monitoring/settings#concept-scope). For information about configuring multi-project metrics scope, see [View metrics for multiple projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects).

## Managed Service for Prometheus data in Cloud Monitoring

Managed Service for Prometheus shares the data-storage backend, Monarch, with Cloud Monitoring. You can use all of the tools provided by Cloud Monitoring with the data collected by Managed Service for Prometheus. For example, you can use [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer), as described in Google Cloud console for Monitoring, and you can set alerts based on these metrics. You can also [import your Grafana dashboards into Cloud Monitoring](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/import-grafana-dashboards).

When working with metric data, including data from Managed Service for Prometheus, in Cloud Monitoring, you can use the query tools provided by Cloud Monitoring:

  * [PromQL](https://docs.cloud.google.com/monitoring/promql)
  * [ Monitoring Query Language (MQL)](https://docs.cloud.google.com/monitoring/mql)
  * [Monitoring filters](https://docs.cloud.google.com/monitoring/api/v3/filters)



### Querying using PromQL in Cloud Monitoring

The simplest way to query your Prometheus data is to use the Cloud Monitoring Metrics Explorer page in the Google Cloud console. To verify that your Prometheus data is being collected correctly, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.

  3. Enter the following query into the editor, and then click **Run query** :
         
         up
         




If your data is being ingested, then you see a chart like the following:

![Metrics Explorer chart for the Managed Service for Prometheus up metric.](https://docs.cloud.google.com/static/stackdriver/images/gmp-metrics-explorer.png)

For information about how to query Cloud Monitoring system metrics using PromQL, see [PromQL for Cloud Monitoring metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/promql).

For more information about using PromQL in Metrics Explorer and Cloud Monitoring charts, see [PromQL in Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql).

**Note:** You can create Cloud Monitoring alerting policies based on PromQL queries and Prometheus alert rules. For more information, see [Alerting policies with PromQL](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting).

### Other query options in Cloud Monitoring

To view your Prometheus data as Cloud Monitoring time series and to create charts and dashboards, you can also use the menu-driven interfaces or MQL. The following shows a simple query in Metrics Explorer:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Specify the data to appear on the chart. In addition to using the **PromQL** button described previously, you can also use the menu-driven interface. To construct a query, do the following:

     1. Within the query-builder pane, click "Select a metric".

     2. In the search field, type "up/" to filter the list, then select **Prometheus Target** , then select **Up** , then select **Prometheus/up/gauge**.

     3. Click "Apply".




The chart that results from this query shows the same data as the chart shown in the PromQL example.

Queries created using the menu-driven interface can be converted to PromQL by selecting the **PromQL** button. This translation might not correctly convert histogram functions or other uncommon operators.

### The `prometheus_target` resource

In Cloud Monitoring, time-series data is written against a monitored-resource type. For Prometheus metrics, the monitored-resource type is [`prometheus_target`](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target). Monitoring queries for Prometheus metrics _that are not written in PromQL_ must specify this resource type.

The `prometheus_target` resource has the following labels, which you can use for filtering and manipulating queried data: 

  * `project_id`: The identifier of the Google Cloud project associated with this resource.
  * `location`: The physical location (Google Cloud region) where the data is stored. This value is typically the region of your GKE cluster or Compute Engine instance. If data is collected from an AWS or on-premises deployment, then the value might be the closest Google Cloud region.
  * `cluster`: The GKE cluster or related concept; might be empty.
  * `namespace`: The GKE namespace or related concept; might be empty.
  * `job`: The job label of the Prometheus target, if known; might be empty for rule-evaluation results.
  * `instance`: The instance label of the Prometheus target, if known; might be empty for rule-evaluation results.



The values for these labels are set during collection.

## What's next

  * [Set up PromQL alerts using Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting).
  * [Import Grafana dashboards into Cloud Monitoring](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/import-grafana-dashboards).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
