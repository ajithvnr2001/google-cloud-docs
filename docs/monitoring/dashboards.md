---
url: https://docs.cloud.google.com/monitoring/dashboards/
title: Dashboards overview \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:41.507642+00:00
---

# Dashboards overview  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Dashboards overview Stay organized with collections  Save and categorize content based on your preferences. 

Dashboards in Cloud Monitoring let you visualize, correlate, and monitor telemetry data across your Google Cloud services, third-party integrations, and custom applications. This document helps you choose between predefined and custom dashboards, select the right chart and table widgets for your data, and design dashboards to avoid performance issues.

## Choose Google Cloud, third-party, or custom dashboards

Cloud Monitoring automatically installs a dashboard when you create a resource in a Google Cloud project. These dashboards display metrics and general information about a single Google Cloud service. For example, if you add Compute Engine instances to your Google Cloud project, then Monitoring installs a dashboard named **VM Instances** in your Google Cloud project. You can't modify or copy these service-specific dashboards. However, you can copy charts from these dashboards to your custom dashboards. For more information, see [View and customize Google Cloud dashboards](https://docs.cloud.google.com/monitoring/charts/predefined-dashboards).

Cloud Monitoring automatically installs a dashboard when you configure a supported third-party application and that application sends metric data to your Google Cloud project. These dashboards display metrics and general information about a single third-party application. You can find the list of supported third-party applications on the **Integrations** page. You can copy these dashboards and then edit the copy, and you can copy charts on these dashboards to custom dashboards. For more information, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

Custom dashboards are dashboards that you [create](https://docs.cloud.google.com/monitoring/charts/dashboards), [copy from one project to another](https://docs.cloud.google.com/monitoring/charts/dashboards#copy-dashboard), [install from a shared location](https://docs.cloud.google.com/monitoring/dashboards/dashboard-templates), or [import Grafana dashboards into Cloud Monitoring](https://docs.cloud.google.com/monitoring/dashboards/import-grafana-dashboards). Unlike dashboards for Google Cloud services and those for your supported integrations, custom dashboards let you view and analyze data from different sources in the same context. For example, you can create a dashboard that displays metric data, alerting policies, and log data.

When troubleshooting, you might want to use [permanent filters](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent) that apply to some or all items on a custom dashboard. Or, you might want to [share a dashboard](https://docs.cloud.google.com/monitoring/charts/share-dashboards) with other people or groups in your organization.

To create custom dashboards, you can use the Google Cloud console, the Google Cloud CLI, or the Cloud Monitoring API. For more information, see [Create and manage dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards) and [Create and manage dashboards by API](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard).

## Choose the right widgets for your dashboard

When creating a custom dashboard, consider what kind of information you want to view and how best to display that data. In addition to [displaying metric data](https://docs.cloud.google.com/monitoring/charts), dashboards can [display alerts and charts for alerting policies](https://docs.cloud.google.com/monitoring/dashboards/alerts-and-incidents), [show log entries](https://docs.cloud.google.com/monitoring/charts/view-logs), and [include descriptive text](https://docs.cloud.google.com/monitoring/dashboards/text-and-grouping). When displaying metric data, you can view that data over a time interval or show only the most recent values.

Each dashboard contains a time-range selector that applies to every widget that doesn't specify its own time range. This lets you customize a chart's time range when you want it to show data over a longer or shorter time range than is appropriate for other dashboard widgets. For more information, see [Set a chart's time range](https://docs.cloud.google.com/monitoring/charts/chart-view-options#set-time-range).

To facilitate debugging, pair charts with tables. Charts display data over a time interval, so you can view historical behavior and identify anomalies. When you spot an anomaly on a chart, you can switch to the table view and then sort and filter the table to find values for specific time series. For example, you might modify the table to show values only for a particular disk or for instances located in a specific zone.

To simplify management of your dashboard content, place related charts and tables in a collapsible group. Groups have collapsed and expanded modes, and they let you manage what they contain as a collection.

Indicators show only the most recent value. Indicators are useful when you don't want to be notified that a single value is outside a desired operational range, but you do want a visual indication. The background color of an indicator changes based on how the measured value compares to the thresholds you select. You can create an alerting policy to notify you when all values recorded over a time interval are outside the desired range.

### Charts that show data over time

To view time-series data over a time interval, add one of the following types to your dashboard:

  * Line chart
  * Stacked-area chart
  * Stacked-bar chart
  * Heatmap chart



The following screenshot is an example of a line chart in color mode:

![Example of a line chart in color mode.](https://docs.cloud.google.com/static/monitoring/images/chartdef-style-line.png)

To display your time series with the highest possible resolution, use a line chart or a stacked-area chart. Choose a stacked-area chart when you want to view the sum of the time series, in addition to the contribution of each time series to the total. You can configure these charts to show only outliers, to compare current to past data, or to display statistical measures such as the "50th percentile". For more information, see [Set chart display options](https://docs.cloud.google.com/monitoring/charts/chart-view-options).

To display time series with infrequent samples, such as quota metrics, use stacked-bar charts and set the time selector for the dashboard to at least one week. For examples that show how to chart quota metrics, see [Chart and monitor quota metrics](https://docs.cloud.google.com/monitoring/alerts/using-quota-metrics).

To display metrics with distribution values, use heatmap charts. Heatmaps use color to represent the values in the distribution. You can also display percentile lines or outliers. For more information, see [About distribution-valued metrics](https://docs.cloud.google.com/monitoring/charts/charting-distribution-metrics).

### Charts that show the most recent data

To view the most recent measurement, add a table, a gauge, or a scorecard to your dashboard. Tables can display multiple time series, and they let you sort and filter rows. In contrast, gauges and scorecards are indicators that display a single time series as compared to a color-coded threshold. For example, a red gauge indicates that the most recent measurement is in a danger range.

The following screenshot is an example of a gauge:

![Example of a gauge.](https://docs.cloud.google.com/static/monitoring/images/widget-scorecard-gaugeview.png)

## Avoid dashboard performance issues

The performance of a dashboard is sensitive to the number of charts it displays and to the number of time series each chart displays. For example, when a chart displays many time series, it might take a long time to load or to refresh. The number of time series depends, in part, on the structure of the metric type and monitored-resource type associated with the time series. Each of these types has several labels; the [Metrics list](https://docs.cloud.google.com/monitoring/api/metrics) and [Monitored resource list](https://docs.cloud.google.com/monitoring/api/resources) include the labels for each metric and monitored-resource type.

There is a single time series for each unique combination of values for the set of labels. The number of possible combinations is called the _cardinality_. For more information about labels, values, and cardinality, see [Cardinality](https://docs.cloud.google.com/monitoring/api/v3/metric-model#cardinality).

If you encounter performance issues when opening a dashboard or when displaying metric data, you can often mitigate the issues by using one of the following techniques:

  * Remove unnecessary information by [filtering](https://docs.cloud.google.com/monitoring/charts/selecting-aggregating-metrics#filter-option).
  * Combine related information by [grouping time series](https://docs.cloud.google.com/monitoring/charts/selecting-aggregating-metrics#groupby-option).
  * Focus on unusual data by sorting the time series that match a query, and then limiting the number of time series that are charted. For more information, see [Show outliers](https://docs.cloud.google.com/monitoring/charts/working-with-charts#using-outlier-mode).
  * Reduce the number of labels or the range of possible values for a label in your user-defined metrics.
  * Remove charts or other widgets from dashboards.
  * Prioritize loading of metric data by [grouping dashboard widgets](https://docs.cloud.google.com/monitoring/dashboards/text-and-grouping).



## Quotas and limits

For information about dashboard-specific quotas and limits, see [Limits for charts](https://docs.cloud.google.com/monitoring/quotas#charting_limits).

## What's next

  * Create dashboards:

    * [Create and manage dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards)
    * [Create and manage dashboards by API](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard)
    * [Import Grafana dashboards](https://docs.cloud.google.com/monitoring/dashboards/import-grafana-dashboards)
  * Add widgets to your dashboards:

    * [Add charts, tables, and indicators](https://docs.cloud.google.com/monitoring/charts)
    * [Display alerts and charts for alerting policies](https://docs.cloud.google.com/monitoring/dashboards/alerts-and-incidents)
    * [Display logs and errors](https://docs.cloud.google.com/monitoring/charts/view-logs)
    * [Add text and groupings](https://docs.cloud.google.com/monitoring/dashboards/text-and-grouping)
    * [Display service-level objectives for a set of services](https://docs.cloud.google.com/monitoring/dashboards/slos)
  * Configure dashboard properties:

    * [Add dashboard filters and variables](https://docs.cloud.google.com/monitoring/dashboards/filter-permanent)
    * [Add or remove labels](https://docs.cloud.google.com/monitoring/charts/dashboards#add-remove-labels)
    * [Show events on a dashboard](https://docs.cloud.google.com/monitoring/dashboards/show-events)
    * [Use Tags to control access to dashboards](https://docs.cloud.google.com/monitoring/docs/access-control-with-tags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
