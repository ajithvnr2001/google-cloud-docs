---
url: https://docs.cloud.google.com/monitoring/charts/charting-distribution-metrics/
title: About distribution-valued metrics \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:58.892214+00:00
---

# About distribution-valued metrics  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/charts/charting-distribution-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  About distribution-valued metrics Stay organized with collections  Save and categorize content based on your preferences. 

Distribution-valued metrics in Cloud Monitoring let you analyze the statistical distribution of large volumes of measurements—such as HTTP response latencies—when collecting every individual data point is impractical. Instead of recording raw values, a [`Distribution`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Distribution) metric groups measurements into value ranges called _buckets_ to form a histogram over each sampling interval. You can visualize these metrics as heatmaps or aggregate them into percentiles and means on line and bar charts.

## How distribution metrics work

To illustrate how a histogram is created, consider a service that measures the HTTP latency of requests and that reports this data by using a metric with a distribution-value type. The data is reported every minute. The service defines ranges of values for the metric, called _buckets_ , and records the count of measured values that fall into each bucket. For example, when an HTTP request completes, the service increments the count in the bucket whose range includes the request's latency value. These counts create a histogram of values for that minute.

Assume that the latencies measured in a one-minute interval are 5, 1, 3, 5, 6, 10, and 14. If the buckets are [0, 4), [4, 8), [8, 12), and [12, 16), then the histogram of this data is [2, 3, 1, 1]. The following table shows how individual measurements affect the count for each bucket:

Bucket | Latency measurements | Number of values in the bucket  
---|---|---  
[12,16) | 14 | 1  
[8,12) | 10 | 1  
[4,8) | 5, 5, 6 | 3  
[0,4) | 1, 3 | 2  
  
When this data is written to the time series, a [`Point`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries#Point) object is created. For metrics with a distribution value, that object includes the histogram of values. For this sampling period, the `Point` contains [2, 3, 1, 1]. The individual measurements aren't written to the time series.

Assume that the previous table records the histogram for the latency data as measured at time 1:00. That table illustrates how to take a series of measurements and convert them into bucket counts. Suppose that the bucket counts at times 1:01, 1:02, and 1:03 are as shown in the following table:

Bucket | Histogram for  
1:00 | Histogram for  
1:01 | Histogram for  
1:02 | Histogram for  
1:03  
---|---|---|---|---  
[12,16) | 1 | 6 | 0 | 1  
[8,12) | 1 | 0 | 2 | 2  
[4,8) | 3 | 1 | 1 | 8  
[0,4) | 2 | 6 | 10 | 3  
  
The previous table displays a sequence of histograms indexed by time. Each column in the table represents the latency data for a one-minute period. To get the number of measurements at a specific time, sum the bucket counts. However, the actual measurements aren't shown because those measurements aren't available in distribution-valued metrics.

## Heatmap charts

Heatmap charts are designed to display a single time series with distribution values. For these charts, the _X_ -axis represents time, the _Y_ -axis represents the buckets, and color represents the value. Brighter colors indicate higher values. For example, dark areas of the heatmap indicate lower bucket counts than yellow or white areas.

The following figure is one representation of a heatmap for the previous example:

![Heatmap chart for the example.](https://docs.cloud.google.com/static/monitoring/images/distribution-heatmap.png)

In the previous figure, the heatmap uses black to represent the smallest bucket count, 0, and yellow to represent the largest bucket count, 10. Reds and oranges represent values between these two extremes.

Because heatmap charts can display only a single time series, you must set the [aggregation](https://docs.cloud.google.com/monitoring/api/v3/aggregation#aggr-intro) options to combine all time series.

To use Metrics Explorer to display the sum of the RTT latencies of a VM instance, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `RTT latencies` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **VM Instance**.
     2. In the **Active metric categories** menu, select **Vm_flow**.
     3. In the **Active metrics** menu, select **RTT latencies**. 
     4. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).




## Line and bar charts

Line charts, stacked bar charts, and stacked line charts, which are designed to display scalar data, can't display distribution values. To display a metric with a distribution value with one of these chart types, you must convert the histogram values into scalar values. For example, you can set the aggregation options to compute the mean of the values in the histogram or to compute a percentile.

For information about how to display a distribution-valued metric on a line chart, see the following section.

## Aggregation and distribution metrics

[Aggregation](https://docs.cloud.google.com/monitoring/api/v3/aggregation#aggr-intro) is the process of regularizing points within a time series and of combining multiple time series. Aggregation is the same for distribution-valued metrics as it is for metrics that have a value type of integer or double. However, the chart type enforces some requirements on the choices used for aligning and grouping time series.

### Heatmap charts

Heatmap charts display one distribution-valued time series. Therefore, the [alignment function](https://docs.cloud.google.com/monitoring/api/v3/aggregation#alignment-intro) and [grouping function](https://docs.cloud.google.com/monitoring/api/v3/aggregation#aggr-grouping) must be set to create a single time series.

Select a `sum` or `delta` alignment function when a chart displays a heatmap. These functions combine, at the bucket level, all samples for a single time series that are in the same alignment period, and the result is a distribution value. For example, if two adjacent samples of a time series are [2, 3, 1, 1] and [2, 5, 4, 1], then the sum alignment function produces [4, 8, 5, 2].

The grouping function defines how different time series are combined. This function is sometimes called an aggregator or a reducer. For heatmaps, set the grouping function to the `sum` function. The sum function adds the values of the same buckets across all histograms, resulting in a new histogram. For example, the sum of the value [2, 3, 1, 1] from timeseries-A and the value [1, 5, 2, 2] from timeseries-B is [3, 8, 3, 3].

### Line charts

Line charts display only scalar-valued time series. If you select a distribution-valued metric, then the chart is configured with optimal parameters to display a heat map. The fields of the **Aggregation** element are set to **Distribution** and **None**.

  * The interpretation of **Distribution** depends on the specific metric. For distribution-valued metric types that have a `GAUGE` metric kind, the default alignment function is set to `sum`. When a distribution-valued metric type has a `CUMULATIVE` metric kind, the default alignment function is `DELTA`.

  * The setting of **None** ensures that all time series are combined.




If you want to display a distribution-valued metric on a line chart, then you must change the default settings of your chart. For example, to configure a line chart on a dashboard to display the 99th percentile of every time series for a distribution-valued metric, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. In the toolbar, click _add_ **Add widget**.
  4. In the **Add widget** dialog, select _leaderboard_ **Metric**.
  5. In the **Metric** element, select the **VM Instance - RTT latencies** metric.
  6. In the **Aggregation** element, expand the first menu and select **99th percentile**.
  7. In the **Display** pane, set the value of the **Widget type** menu to **Line chart**.
  8. Optional: In the **Aggregation** element, expand the second menu and select the labels used to group time series. By default, no labels are selected, and therefore one line is displayed on the chart.



## What's next

For information about how to determine the bucket model for a metric and how to interpret percentiles, see [Percentiles and distribution-valued metrics](https://docs.cloud.google.com/monitoring/api/v3/distribution-metrics).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
