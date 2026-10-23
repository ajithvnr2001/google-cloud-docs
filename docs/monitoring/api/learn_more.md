---
url: https://docs.cloud.google.com/monitoring/api/learn_more/
title: Learn more about... \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:25.279803+00:00
---

# Learn more about...  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/learn_more/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)



Send feedback 

#  Learn more about... Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Monitoring lets you evaluate system performance and health across your infrastructure using data aggregation, custom metrics, filtering, and metrics scopes. Understanding these foundational concepts helps you structure cross-project observability and isolate specific signals from your time-series data.

## Aggregation

When you read metric data using the Metrics Explorer or the Monitoring API, you can use _aggregation_ to summarize the time series data. Aggregation typically starts with an alignment step in which each time series' data is placed on the same time boundaries. Next, a new time series is created by combining the data points from multiple time series, using operations like average, sum, minimum, maximum, and so forth.

For more information about aggregation, see the [`projects.timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) API method.

## Custom metrics

Cloud Monitoring has a large number of built-in system metrics, but you can also create custom metrics. You must create a metric descriptor that describes your custom metric and one or more time series that contain its data. You can use your custom metric data in charts and alerts. You can also create custom metrics based on logs data. For more information, see the following pages:

  * [Metrics, Time Series, and Resources](https://docs.cloud.google.com/monitoring/api/v3/metrics) provides an overview.
  * [Using Custom Metrics](https://docs.cloud.google.com/monitoring/custom-metrics) shows you how to create, write, and read custom metrics.
  * [Logs-based Metrics](https://docs.cloud.google.com/logging/docs/view/logs_based_metrics) describes how to create custom metrics from logs.
  * [Monitoring API](https://docs.cloud.google.com/monitoring/api/ref_v3/rest), is the API used to for custom metrics. See the `projects.metricDescriptors` and `projects.timeSeries` collections.



## Filtering

Cloud Logging and Cloud Monitoring provide different kinds of filters that let you select sets of items. Filters are strings that contain combinations of comparisons appropriate to their kind. For example:

  * [Logging filters](https://docs.cloud.google.com/logging/docs/view/advanced_filters) let you select particular log entries based on log names, where the logs came from, their payload content, and so on.
  * [Monitoring filters](https://docs.cloud.google.com/monitoring/api/v3/filters) let you select particular metric descriptors, resource groups, and time series data.
  * [Trace filters](https://docs.cloud.google.com/trace/docs/trace-filters) let you select traces based on span names, latency, and label values.



## Metrics scope

Monitoring organizes itself around metrics scopes that let you view and monitor metrics for one or more Google Cloud projects. For more information about metrics scopes, see [Configuring your Google Cloud project for Cloud Monitoring](https://docs.cloud.google.com/monitoring/settings).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
