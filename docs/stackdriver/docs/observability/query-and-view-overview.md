---
url: https://docs.cloud.google.com/stackdriver/docs/observability/query-and-view-overview/
title: Query and view telemetry data \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:36.102951+00:00
---

# Query and view telemetry data  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/observability/query-and-view-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Query and view telemetry data Stay organized with collections  Save and categorize content based on your preferences. 

To view, investigate, or analyze your log, metric, and trace telemetry, Google Cloud Observability offers three primary analytical workflows:

  * **Predefined dashboards:** Turnkey visualizations automatically generated for your Google Cloud resources and registered App Hub applications.

  * **Interactive telemetry explorers:** Specialized interfaces—Logs Explorer, Metrics Explorer, and Trace Explorer—for querying, filtering, and live debugging.

  * **SQL-based analytics:** Standard SQL querying capabilities inside the **Observability Analytics** or BigQuery for deep trend analysis and custom reporting.




## Predefined dashboards

When you create a resource like a Compute Engine virtual machine (VM), Google Cloud Observability automatically creates and installs a dashboard in your project. These dashboards display metric data and general information about the resources that you use. To view your dashboards, go to the **Dashboards** page in the Google Cloud console:

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you register applications with [App Hub](https://docs.cloud.google.com/app-hub/docs/overview), then you can use dashboards that Application Monitoring creates. These dashboards display telemetry and other information from the perspective of your application.

For more information, see the following documents:

  * [Dashboards overview](https://docs.cloud.google.com/monitoring/dashboards).
  * [View and customize Google Cloud dashboards](https://docs.cloud.google.com/monitoring/charts/predefined-dashboards).
  * [Application Monitoring overview](https://docs.cloud.google.com/stackdriver/docs/observability/about-application-monitoring).



## Interactive telemetry explorers

To view or explore telemetry, use the explorer pages for log, metric, and trace data. These pages provide access to individual log entries, time series, and trace spans, and they help you troubleshoot and analyze the performance of your services and applications.

The explorer pages rely on scopes to determine what resources to query for data. Scopes let you view and analyze data that is stored in multiple projects. If you don't configure observability scopes, then the explorer pages query your project for data. For more information, see [Configure observability scopes](https://docs.cloud.google.com/stackdriver/docs/scopes/configure).

The explorer pages provide filtering and aggregation capabilities that you can use to control what data appears and how the pages process that data. The explorer pages for logging and trace also perform some analysis for you. For example, the **Logs Explorer** page displays the rate of errors as a function of time. The **Trace Explorer** page displays a heatmap of aggregated latency data.

### Log data

For information about how to use the **Logs Explorer** page, see [View and explore log data](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

### Metric data

For information about how to use the **Metrics Explorer** page, see [Chart metric data](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

### Trace data

For information about how to use the **Trace Explorer** page, see [Find and explore trace data](https://docs.cloud.google.com/trace/docs/finding-traces).

In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Trace explorer** page: 

[Go to **Trace explorer**](https://console.cloud.google.com/traces/explorer)

You can also find this page by using the search bar.

## SQL-based analytics

To generate insights or identify trends in your data, use the **Observability Analytics** page or BigQuery services.

### Use Observability Analytics

The **Observability Analytics** page provides a [SQL](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax) interface and can query all of the following:

  * [Log views on log buckets](https://docs.cloud.google.com/logging/docs/logs-views): A log view provides read access to a subset of log entries that are stored in a log bucket.

  * [`_AllSpans` view on your `Spans` dataset](https://docs.cloud.google.com/stackdriver/docs/observability/storage-overview#views-on-datasets): This view includes all trace data stored by your project.

  * [Analytics views](https://docs.cloud.google.com/logging/docs/analyze/about-analytics-views): An analytics view queries either log views or the `_AllSpans` view on your `Spans` dataset and is itself a resource that can be queried. You can use analytics views to transform your log or trace data into a custom format.




By default, query results are shown in tabular form. However, you can display the results in a chart, which can help you identify patterns and trends. The **Observability Analytics** page lets you save queries, share queries, view query results as a table or chart, and save charts to custom dashboards.

### Log data

For information about how to query your log data with SQL, see [Query and analyze by using Observability Analytics](https://docs.cloud.google.com/logging/docs/analyze/query-and-view).

In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

### Metric data

Not supported.

### Trace data

For information about how to query your trace data with SQL, see [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics).

In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

### Use BigQuery

If you want to query your log or trace data using BigQuery services, then create a link on the resource that stores that data. For more information, see:

  * [Create a linked BigQuery dataset on your trace data](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset)
  * [Create a linked BigQuery dataset on your log data](https://docs.cloud.google.com/logging/docs/analyze/query-linked-dataset)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
