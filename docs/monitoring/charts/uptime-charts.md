---
url: https://docs.cloud.google.com/monitoring/charts/uptime-charts/
title: Chart uptime-check metrics \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:21.698603+00:00
---

# Chart uptime-check metrics  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/charts/uptime-charts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Chart uptime-check metrics Stay organized with collections  Save and categorize content based on your preferences. 

Charting uptime-check metrics in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) lets you monitor the responsiveness of your service and verify which regions respond successfully to probes. You can create charts for both the uptime-check status metric and the request-latency metric. To add these charts to a custom dashboard, see [Save a chart for future reference](https://docs.cloud.google.com/monitoring/charts/metrics-explorer#save_a_chart).

## Before you begin

You must have an uptime check to use these instructions. If you haven't created an uptime check, then see [Create public uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks) or [Create private uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/private-checks).

## Chart uptime-check status

You can use the Cloud Monitoring `uptime_check/check_passed` metric as the basis for a chart that displays the status of an uptime check. The following example charts, by location, the number of passed checks in a one-minute window: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Check passed` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select the resource monitored by the uptime check.
     2. In the **Active metric categories** menu, select **Uptime_check**.
     3. In the **Active metrics** menu, select **Check passed**. 
     4. Click **Apply**.
The fully qualified name for this metric is `monitoring.googleapis.com/uptime_check/check_passed`. 
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. Configure how the data is viewed. 
     1. In the **Filter** element, expand the menu and select **check_id** , and then select a specific checker.
     2. In the **Aggregation** element, expand the first menu and select **Configure aligner**. The **Alignment function** and **Grouping** elements are added.
     3. In the **Alignment function** element, expand the menu and select **Next older**.
     4. In the **Grouping** element, expand the first menu and select **Count true**.

For more information about configuring a chart, see [Select metrics when using Metrics Explorer.](https://docs.cloud.google.com/monitoring/charts/metrics-selector)


Because the uptime check is configured to execute every minute, it is expected that every location responds approximately 10 times in a 10-minute alignment period. 

## Chart uptime-check latency

You can use the Monitoring `uptime_check/request_latency` metric as a basis for uptime-check latency charts. Your choices for the grouping fields let you create different charts. You can, for example, set these fields to display the maximum latency or to display the total latency: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Request latency` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select the resource monitored by the uptime check.
     2. In the **Active metric categories** menu, select **Uptime_check**.
     3. In the **Active metrics** menu, select **Request latency**. 
     4. Click **Apply**.
The fully qualified name for this metric is `monitoring.googleapis.com/uptime_check/request_latency`. 
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. Configure how the data is viewed. 
     1. In the **Filter** element, expand the menu and select **check_id** , and then select a specific checker.
     2. In the **Aggregation** element, expand the first menu and select **Mean** , and then expand the second menu and select **checker_location**.

For more information about configuring a chart, see [Select metrics when using Metrics Explorer.](https://docs.cloud.google.com/monitoring/charts/metrics-selector)




## What's next

  * [Create and manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards)
  * [Uptime check metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#monitoring/uptime_check/check_passed)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
