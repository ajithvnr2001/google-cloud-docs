---
url: https://docs.cloud.google.com/monitoring/charts/metric-ratios/
title: About ratios of metrics \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:00.336402+00:00
---

# About ratios of metrics  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/charts/metric-ratios/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  About ratios of metrics Stay organized with collections  Save and categorize content based on your preferences. 

Computing a ratio of two metrics in Cloud Monitoring lets you transform raw counts into proportions or rates, such as calculating the percentage of HTTP requests that failed relative to total requests. You can chart and monitor metric ratios by using PromQL, the menu-driven interface in the Google Cloud console, or time-series filters in the Cloud Monitoring API. Understanding how sampling rates, label groupings, and alignment periods interact helps you avoid anomalies when configuring them.

## Best practices

To monitor or chart a ratio of metric data, we recommend that you use [PromQL](https://docs.cloud.google.com/monitoring/promql). You can use PromQL with the Cloud Monitoring API and with the Google Cloud console. The Google Cloud console includes a code editor that provides suggestions, error detection, and other support for creating valid PromQL queries.

To create an alerting policy that monitors a ratio of metrics when you aren't familiar with PromQL, use the Cloud Monitoring API and include a [time-series filter](https://docs.cloud.google.com/monitoring/api/v3/filters). For an example, see [Metric ratio](https://docs.cloud.google.com/monitoring/alerts/policies-in-json#json-ratio).

To chart a ratio of metric data when you aren't familiar with PromQL, we recommend that you use the Google Cloud console and that you use a menu-driven interface. For detailed instructions, see [Chart a ratio of metrics](https://docs.cloud.google.com/monitoring/charts/metrics-explorer#chart-ratio) and [Add charts and tables to a custom dashboard](https://docs.cloud.google.com/monitoring/charts).

## Restrictions with ratios

When you configure a ratio, the following restrictions apply:

  * After aggregation, the labels in the denominator time series must be the same as, or a subset of, the labels in the numerator time series.

We recommend that you select aggregation options such that after aggregation, the numerator and the denominator time series have the same labels.

Consider a configuration where the numerator time series has `method`, `quota_metric`, and `project_id` labels. The denominator time series has `limit_name`, `quota_metric`, and `project_id` labels. The valid choices for the denominator grouping depend on the selections for the numerator:

    * Numerator grouped by the `method` label: Combine the denominator time series into a single time series. No other grouping results in the labels for the denominator time series being a subset of the labels for the numerator time series.
    * Numerator grouped by the `quota_metric` label: Group the denominator by that label or combine all time series in the denominator into a single time series.
    * Numerator grouped by the `quota_metric` and `project_id` labels: Group the denominator by both labels, by one label, or combine the denominator time series into a single time series.

The valid denominator aggregation options always eliminate the `limit_name` label from the grouped time series because that label isn't present in the numerator time series.

  * The alignment period must be the same for the numerator and the denominator when configuring a chart by using the Google Cloud console; however, these fields can be different when using the Cloud Monitoring API.

We recommend that you use the same alignment period for the numerator and the denominator regardless of the tool you use to create the chart.

  * The numerator and denominator must have the same [value type](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types). For example, when the numerator is of type `DOUBLE`, the denominator must also be of type `DOUBLE`.

Ratios require that the numerator and denominator metrics have a value type of `DOUBLE` or `INT64`.

  * The aligned time series for the numerator and the denominator must have the same [metric kind](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types). When the two metrics have different kinds, you must use aligners to convert them to the same kind.

Consider a configuration where a `DELTA` metric is selected for the numerator and a `GAUGE` metric is selected for the denominator. In this situation, use the rate aligner, `ALIGN_RATE`, to convert the `DELTA` metric to a `GAUGE` metric. For an example, see [Ratio alerting policies on usage of rate quota for one limit](https://docs.cloud.google.com/monitoring/alerts/using-quota-metrics#mql-rate-one-limit).

  * For ratios that aren't defined with PromQL, the monitored resource type must be the same for the numerator and the denominator.

For example, if the resource for the numerator metric is Compute Engine instances, then the resource for the denominator metric must also be Compute Engine instances.




## Anomalies due to sampling and alignment mismatches

In general, it is best to compute ratios based on time series collected for a single metric type, by using label values. A ratio computed over two different metric types is subject to anomalies due to different sampling periods and alignment windows.

For example, suppose that you have two different metric types, an RPC total count and an RPC error count, and you want to compute the ratio of error-count RPCs over total RPCs. The unsuccessful RPCs are counted in the time series of both metric types. Therefore, there is a chance that, when you align the time series, an unsuccessful RPC doesn't appear in the same alignment interval for both time series. This difference can happen for several reasons, including the following:

  * Because there are two different time series recording the same event, there are two underlying counter values implementing the collection, and they aren't updated atomically.
  * The sampling rates might differ. When the time series are aligned to a common period, the counts for a single event might appear in adjacent alignment intervals in the time series for the different metrics.



The difference in the number of values in corresponding alignment intervals can lead to nonsensical `error/total` ratio values like 1/0 or 2/1.

Ratios of larger numbers are less likely to result in nonsensical values. You can get larger numbers by aggregation, either by using an alignment window that is longer than the sampling period, or by grouping data for certain labels. These techniques minimize the effect of small differences in the number of points in a given interval. That is, a two-point disparity is more significant when the expected number of points in an interval is 3 than when the expected number is 300.

If you are using built-in metric types, then you might have no choice but to compute ratios across metric types to get the value you need.

If you are designing custom metrics that might count the same thing—like RPCs returning error status—in two different metrics, consider instead a single metric, which includes each count only once. For example, suppose that you are counting RPCs and you want to track the ratio of unsuccessful RPCs to all RPCs. To solve this problem, create a single metric type to count RPCs, and use a label to record the status of the invocation, including the "OK" status. Then each status value, error or "OK", is recorded by updating a single counter for that case.

## False alerts due to ratio calculation anomalies

To avoid false alerts due to transient errors or missing data, set the duration of your PromQL query to at least twice the evaluation interval:

  * Google Cloud console: Set the duration in the **Duration** field when configuring the alerting condition.
  * Cloud Monitoring API or Terraform: Specify the duration using the `AlertPolicy.Condition.PrometheusQueryLanguageCondition.duration` field.



## What's next

  * For information about using PromQL to configure alerting policies, see [PromQL alerting overview](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting).

  * For information about creating charts, see the following documents:

    * To create temporary charts, see [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).
    * To add charts to a dashboard by using the Google Cloud console, see [Add charts and tables to a custom dashboard](https://docs.cloud.google.com/monitoring/charts).
    * To manage charts by using the Cloud Monitoring API, see [Create and manage dashboards by API](https://docs.cloud.google.com/monitoring/dashboards/api-dashboard).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
