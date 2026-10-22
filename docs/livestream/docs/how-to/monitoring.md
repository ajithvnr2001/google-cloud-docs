---
url: https://docs.cloud.google.com/livestream/docs/how-to/monitoring/
title: Monitor live streams \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:49.592591+00:00
---

# Monitor live streams  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/how-to/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Guides ](https://docs.cloud.google.com/livestream/docs/overview)



Send feedback 

#  Monitor live streams Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view metrics collected by Live Stream API as part of Cloud Monitoring. You can find the list of Live Stream API metrics at [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

## View Cloud Monitoring metrics

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Live Stream API Channel` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **Live Stream API Channel**.
     2. To select a metric, use the **Active metric categories** and **Active metrics** menus. 
     3. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. Configure how the data is viewed. For example, you can plot the chart for a specific channel by entering `channel_id = my-channel` in the **Filters** field. 

For more information about configuring a chart, see [Select metrics when using Metrics Explorer.](https://docs.cloud.google.com/monitoring/charts/metrics-selector)




## Convert the input stream bitrate unit

You can use the `channel/received_bytes_count` metric to monitor your input stream bitrate. By default, the unit of `channel/received_bytes_count` is bytes per second to be consistent with other Google Cloud metrics.

  1. In the Metrics Explorer **Configuration** tab, set the **Resource Type** field to **Live Stream API Channel** and the **Metric** field to **Received bytes count**.

  2. Select the **PromQL** tab.

  3. For example, to convert the value to megabits per second, add the calculation to the end of the following query:
         
         rate({
             "__name__"="livestream.googleapis.com/channel/received_bytes_count",
             "monitored_resource"="livestream.googleapis.com/Channel",
         }[${__interval}]) * 8 / 1000000
         

  4. Click **RUN QUERY** to replot the chart.




For more information about PromQL, see [Use the code editor for PromQL](https://docs.cloud.google.com/monitoring/promql/promql-in-monitoring).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
