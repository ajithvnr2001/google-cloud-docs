---
url: https://docs.cloud.google.com/logging/docs/logs-based-metrics/view_your_log_based_metrics/
title: List and chart log-based metrics \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:35.247533+00:00
---

# List and chart log-based metrics  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/logs-based-metrics/view_your_log_based_metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  List and chart log-based metrics Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to list and chart log-based metrics by using the Google Cloud console. For information about creating log-based metrics, see [Configure counter metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/counter-metrics) and [Configure distribution metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/distribution-metrics).

## Before you begin

Ensure that your Identity and Access Management role includes the permissions required to create and view log-based metrics, and to create alerting policies. For details, see [Permissions for log-based metrics](https://docs.cloud.google.com/logging/docs/access-control#metrics-permissions).

## List log-based metrics

To view a list of log-based metrics for your Google Cloud project, do the following:

  1. In the Google Cloud console, go to the **Log-based Metrics** page: 

[Go to **Log-based Metrics**](https://console.cloud.google.com/logs/metrics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select an existing Google Cloud project. The log-based metrics interface displays two lists of metric-types: **System metrics** and **User-defined metrics**.

The **User-defined metrics** pane of the log-based metrics interface has several features to help you manage the user-defined metrics in your Google Cloud project:

     * The user-defined metrics table includes **Name** , **Description** , **Type** , and **Filter** columns. These fields are specified when you create the metric.

     * The **Filter user-defined metrics** pane lets you filter your metric list by text search or metric **Name** , **Description** , and **Filter**.

     * The user-defined metrics table includes columns for **Previous month usage** and **Month-to-date usage (MTD)**. This usage data is useful, for example, if you want to determine which metrics ingest the most data or to [estimate your bills](https://docs.cloud.google.com/stackdriver/estimating-bills).

The _more_vert_ **More** menu for each metric in your user-defined metrics pane contains additional features for managing your metrics:

![The user-defined log-based metrics pane overflow menu options.](https://docs.cloud.google.com/static/logging/docs/images/lbm-user-overflow-ui.png)

     * **View metric details** : Shows you the metric's **Name** , **Type** , **Description** , **Filter** , **Units** , and **Labels** , if defined.
     * **Edit metric** : Lets you edit certain fields for the metric.
     * **Disable metric** : Lets you stops the metric from being calculated. You can re-enable a disabled metric from the same menu.
     * **Delete metric** : Lets you delete the metric.
     * **View logs for metric** : Takes you to the Logs Explorer and populates the metric's filter in the **Query builder** and runs the query.
     * **View in Metrics Explorer** : Lets you chart the metric.
     * **Create alert from metric** : Lets you configure notifications when a log-based metric matches criteria that you specify. For more information, see [Alert on log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/charts-and-alerts).



## Chart log-based metrics

To create a chart of a log-based metric, do the following:

  1. In the Google Cloud console, go to the **Log-based Metrics** page: 

[Go to **Log-based Metrics**](https://console.cloud.google.com/logs/metrics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Find the metric you want to view, and then select **View in Metrics Explorer** from the metric's _more_vert_ **More** menu.

[Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) opens and is preconfigured for you. However, you might want to change some chart settings.

For example, the following screenshot shows a chart of the system metric with the name `byte_count` for a particular Google Cloud project:

![Metrics Explorer displaying the system metric named byte_count.](https://docs.cloud.google.com/static/logging/docs/images/metrics-explorer.png)

The **Aggregation** entry shows that each time series on the chart is a sum of the bytes written to a specific log. In the previous example, the project contains multiple logs, so the chart displays multiple time series.

To view the data for a specific log, add a filter. For example, to view the `byte_count` metric for log entries written by BigQuery, click **Add filter** , select **log** , and then select the BigQuery entry. The chart now displays a single time series, which shows the total of the log bytes written by BigQuery. If you want to view the `byte_count` metric by the severity of the log entry, then change the second menu in the **Aggregation** entry from **None** to **Severity**. The following chart shows the `byte_count` metric displayed by severity level for logs written by BigQuery:

![Metrics Explorer displaying the byte_count metric by severity for BigQuery instances ](https://docs.cloud.google.com/static/logging/docs/images/metrics-explorer-by-severity.png)

  3. For distribution-valued log-based metrics, expand **Line chart** and select **Heatmap chart**.

For more information about distribution-valued metrics, see [Distribution metrics](https://docs.cloud.google.com/monitoring/charts/charting-distribution-metrics) and [Percentiles and distribution-valued metrics](https://docs.cloud.google.com/monitoring/api/v3/distribution-metrics).

  4. Optional: To save the chart for future reference, click **Save as** in the toolbar, select **Dashboard chart** , and then complete the dialog. You can save the chart to an existing dashboard or create a new dashboard.


**Tip:** If you don't see any data in the graph, try increasing the time range or changing the default settings.

## What's next

  * To create an alerting policy for a log-based metric, see [Alert on log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/charts-and-alerts).
  * For more information about charting metric data, see these Monitoring resources:

    * [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer)
    * [Creating charts](https://docs.cloud.google.com/monitoring/charts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
