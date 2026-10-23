---
url: https://docs.cloud.google.com/stackdriver/estimating-bills/
title: Estimate your bills \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:24.368276+00:00
---

# Estimate your bills  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/estimating-bills/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Resources ](https://docs.cloud.google.com/stackdriver/quotas)



Send feedback 

#  Estimate your bills Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to estimate your bills. For pricing information, see the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

You might also be interested in the following documents:

  * [Optimize and monitor your costs](https://docs.cloud.google.com/stackdriver/docs/observability/pricing-optimize-and-monitor). This document helps you reduce or monitor your costs.

  * [Optimize costs with the Cost Explorer](https://docs.cloud.google.com/stackdriver/docs/costs/optimize-costs). The Cost Explorer provides current and historical visualizations of cost data and utilization metrics. As such, the data helps you identify optimization opportunities.




## Overview

Based on your usage data, you can estimate your bills for using Google Cloud Observability.

The Cloud Billing **Reports** page shows you your current usage data. In addition, the Logging and Monitoring pages in the Google Cloud console display your projected usage data for the current month.

This document details how to access your usage data, depending on the aggregation that you prefer:

  * Usage by billing account
  * View detailed usage in Metrics Explorer
  * Logging usage by project or resource type
  * Logs-based metrics usage
  * Monitoring usage by metrics scope



## Review usage data to estimate your bill

Once you have the usage data you want, as described on this page, you can estimate your future bill in two ways:

  * Refer to the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) document. Compare your current usage data with the prices found in this table to get an approximation of your future bills for Google Cloud Observability.

  * Use the [pricing calculator](https://cloud.google.com/products/calculator):

**Note:** You must use the legacy pricing calculator. The pricing calculator doesn't support estimating costs for Synthetic Monitors.
    1. Select the Google Cloud Observability product.
    2. Add your current or projected metric usage data to the **Metrics** section and click **Add to estimate**.
    3. Add your current or projected Logging usage data to the **Logs** section and click **Add to estimate**.
    4. Add your current Trace usage data to the **Trace spans** section and click **Add to estimate**.
    5. Add your current uptime check usage data to the **Uptime Checks** section and click **Add to estimate**.
    6. After you have input your usage data, click **Estimate**.

Estimates of your future bills for using Google Cloud Observability appear. You can also email and save the estimate.


**Note:** Any estimated fees are approximations and for discussion purposes only.

## View usage by billing account

You can view your usage information for all Google Cloud Observability services or for a subset of services or SKUs, and you can view usage for specific time periods.

  1. In the Google Cloud console, go to the **Billing** page: 

[Go to **Billing**](https://console.cloud.google.com/billing)

You can also find this page by using the search bar.

  2. If you have more than one billing account, then select the billing account. If you don't know which billing account is used for a specific project, then do the following:

     1. Select the **My projects** tab.
     2. Verify the proper organization is selected, and then search for your project.
     3. Select the account listed in the **Billing account** column.
  3. In the navigation pane, select **Reports**.

  4. If the **Filters** pane isn't visible, then go to the **Reports** toolbar and click _first_page_ **Filters**.

  5. In the **Filters** pane, expand the **Group By** menu and then select **SKU**.

  6. In the **Filters** pane, expand the **Services** menu and then make the following selections:

     * **Cloud Logging**
     * **Cloud Monitoring**
     * **Cloud Trace**

The **Reports** page displays a bar chart and a table, each with one entry for every SKU that corresponds to the services that you selected that have charges. The table displays the cost and the usage per SKU:

![The user interface showing usage data filtered
by SKU.](https://docs.cloud.google.com/static/stackdriver/images/billing_legends.png)

  7. To view information only for a specific SKU or set of SKUs, expand the **SKUs** menu and select that SKU or set of SKUs. For example, if you only want to view the usage for your log storage costs, expand the **SKUs** menu and select **Log Storage cost**.

  8. Optional: Update the time period for the billing data. By default, the time period is set to the current month.




## View detailed usage in Metrics Explorer

You can use Metrics Explorer to view the data used for billing.

**Note:** Cloud Logging charges for both of the following: 

  * Storage: the volume of logs that are streamed into log bucket storage for indexing, querying, and analysis.
  * Retention: the volume of logs stored in log buckets for longer than the free retention period of the log bucket.



The metrics described in this section are for storage only.

For more information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing). For information about estimating Logging retention costs, see View Logging usage.

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Global` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **Global**.
     2. In the **Active metric categories** menu, select **Billing**.
     3. In the **Active metrics** menu, select a _billing metric_ †. 
        * [ Log bytes ingested](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#logging/billing/bytes_ingested): Log bytes for a project streamed for storage in Logging.

Don't select [Log bytes](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#logging/byte_count), which isn't a billing metric. This metric is computed differently from the billing metric.

        * [ Log bucket bytes ingested](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#logging/billing/log_bucket_bytes_ingested): Bytes steamed for storage into individual log buckets in Logging.

        * [ Monthly log bytes ingested](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#logging/billing/monthly_bytes_ingested): Each point represents the month-to-date sum of log bytes streamed for storage in Logging for your project. The monthly total is available on the last day of the month, when it also resets.

        * [ Log bucket monthly bytes ingested](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#logging/billing/log_bucket_monthly_bytes_ingested): Each point represents the month-to-date sum of log bytes streamed for storage into individual log buckets in Logging. The monthly total is available on the last day of the month, when it also resets.

        * [ Metric bytes ingested](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#monitoring/billing/bytes_ingested): Chargeable number of bytes of metric data streamed for storage in Monitoring.

        * [ Metric samples ingested](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#monitoring/billing/samples_ingested): Chargeable number of samples of metric data streamed for storage in Monitoring. For more information about features that charge by samples, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).

        * [ Trace spans ingested](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#cloudtrace/billing/spans_ingested): Chargeable trace spans streamed for storage in Trace.

        * [ Monthly trace spans ingested](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#cloudtrace/billing/monthly_spans_ingested): Each point represents the month-to-date sum of trace spans streamed for storage in Trace. It resets on the last day of the month; the monthly total is found on the last day of the month.

† Billing metrics have `billing` in their names, for example, `logging.googleapis.com/**billing** /log_bytes_ingested`.

     4. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.

  6. For quota and other metrics that report one sample per day, do the following: 
     1. In the **Display** pane, set the **Widget type** to **Stacked bar chart**.
     2. Set the time period to at least one week.



Your usage data appears, filtered by the metrics you selected. If metrics usage data doesn't appear in the chart, then you might need to zoom out to `1w` or `1m` in the time range selector above the chart.

**Key Points:**

  * To **identify the metric or resource type with the highest usage** , use the **Sort & Limits** fields in Metrics Explorer. 
  * For information about **managing costs of user-defined metrics** , see [View and manage metric usage](https://docs.cloud.google.com/monitoring/docs/metrics-management). 



## View Logging usage

  1. In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

The **Logs Storage** page displays a summary of your logging data streamed for storage for the selected Google Cloud project. This data includes the current calendar month's to-date usage, the previous calendar month's total usage, and the projected total usage for the current calendar month.

  2. Optional: To review your project-level billing data in detail, click **See bill** under **Previous month volume**.

The Cloud Billing **Reports** page opens.

  3. Optional: To view usage by resource type, in the summary section, go to the **Current month ingestion** pane and click **See ingestion analysis**.

Your usage data appears in Metrics Explorer, grouped by `resource_type`. You can further modify how the data is displayed, using the **Filter** , **Group By** , and **Aggregator** menus. For more details, see View detailed usage in Metrics Explorer.




## View logs-based metrics usage

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select **Logs-based metrics**.
  3. In the **User-defined Metrics** table, your usage data appears:

     * **Previous Month Usage** represents the sum of bytes for the logs-based metric in the previous calendar month.
     * **Usage (MTD)** represents the sum of bytes for the logs-based metric in the current calendar month.
  4. Optional: To sort the data in ascending or descending order, click a column name. Sorting the rows is helpful, for example, when you want to review which metrics have the most data.




## View Monitoring metrics usage by metrics scope

A [metrics scope](https://docs.cloud.google.com/monitoring/settings#concept-scope) is used in Cloud Monitoring to let you _view_ metrics that are stored in multiple Google Cloud projects or AWS accounts. When you configure a metrics scope, you don't affect which project receives metric data or cause data to be duplicated.

For example, suppose Project-A contains 60 VMs and Project-B contains 40 VMs. If you create a metrics scope that includes Project-A and Project-B, then you can view the combined metrics for the 100 VMs. You can now view just the metrics for Project-A, just the metrics of Project-B, or the combination of metrics from both projects. Even though you have two ways to view the metrics of Project-A, there aren't billing implications.

To view your Monitoring usage by metrics scope, do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Summary** tab.

The **Metrics Ingested** table displays a summary of your metrics streamed for storage by resource. This data includes the previous month's total usage, the current month's to-date usage, and projected usage for the current month.

  3. Optional: To get your project-level usage in detail, click **View Bill** in the **Metrics Ingested** table.

The Cloud Billing **Reports** page opens.




## View the number of time series billed for queries

Calls to the Cloud Monitoring API that return time series are charged by the number of time series that are returned or for a single time series, whichever is larger. You can use the [`time_series_billed_for_queries_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#monitoring/billing/time_series_billed_for_queries_count) metric to estimate your costs based on the number of time series that have been queried.

To find the number of time series that have been queried, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  4. To find the number of time series that have been queried in the last day, do the following: 
     1. Enter the following PromQL query into the query editor:
    
    sum(increase({"monitoring.googleapis.com/billing/time_series_billed_for_queries_count"}[1d]))
    

     1. In the **Results** pane, select **Table**.

     2. Click **Run Query**. The results table lists of the number of time series in the **Value** column.

For more information about using PromQL, see [PromQL in Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql). 




To estimate your cost from the number of time series queried, do the following:

  1. Use the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) information to find the the cost of API reads based on time series queried.

  2. For a daily estimate, multiply the rate from the pricing table by the value returned by the previous PromQL query.

  3. For a monthly estimate, multiply the daily estimate by 30.




These estimates don't take into account the monthly free allotment of API read requests.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
