---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/promql-differences/
title: PromQL compatibility \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:18.042545+00:00
---

# PromQL compatibility  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/promql-differences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  PromQL compatibility Stay organized with collections  Save and categorize content based on your preferences. 

[PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) queries in Google Cloud Managed Service for Prometheus are partially evaluated at the [Monarch](https://research.google/pubs/pub50652/) backend, and there are some known differences in query results. This document describes the differences.

Other than the differences listed in this document, the PromQL in Managed Service for Prometheus is at parity with the PromQL available in Prometheus version **2.44**. 

PromQL functions added after Prometheus version **2.44** might not be supported.

## UTF-8 support

PromQL for Cloud Monitoring supports [UTF-8 querying](https://prometheus.io/docs/guides/utf8/#querying).

If your Prometheus metric name only consists of alphanumeric characters plus the `_` or `:` characters, and if your label keys only consist of alphanumeric characters plus the `_` character, then you can query using traditional PromQL syntax. For example, a valid query might look like `job:my_metric:sum{label_key="label_value"}`.

However, if your Prometheus metric name uses any special characters except for the `_` or `:` characters, or if your label keys use any special character except for the `_` character, then you have to construct your query according to the [UTF-8 spec for PromQL](https://prometheus.io/docs/guides/utf8/#querying). 

UTF-8 metric names must be quoted and moved into the braces. Label names must also be quoted if they contain legacy-incompatible characters. The following example valid queries are all equivalent:

  * `{"my.domain.com/metric/name_bucket", "label.key"="label.value"}`
  * `{__name__="my.domain.com/metric/name_bucket", "label.key"="label.value"}`
  * `{"__name__"="my.domain.com/metric/name_bucket", "label.key"="label.value"}`



## Matching on metric names

Only exact matching on metric names is supported. You must include an exact match on the metric name in your query.

We recommend the following workarounds for common scenarios that use a regular expression matcher on the `__name__` label:

  * Prometheus adapter configurations often use the `=~` operator to match on multiple metric names. To fix this usage, expand the config to use a separate policy for each metric and name each metric explicitly. This also prevents you from accidentally autoscaling on unexpected metrics.
  * Regular expressions are often used to graph multiple non-dimensional metrics on the same chart. For example, if you have a metric like `cpu_servicename_usage`, you might use a wildcard to graph all your services together. Using non-dimensional metrics like this is an explicitly bad practice in Cloud Monitoring, and this practice leads to extremely poor query performance. To fix this usage, move all dimensionality into metric labels instead of embedding dimensions in the metric name.
  * Querying over multiple metrics is often used to see what metrics are available to query. We recommend you instead use the `/labels/__name__/values` call to discover metrics. You can also discover metrics using the Cloud Monitoring UI.
  * Matching multiple metrics is useful for seeing how many samples were scraped, ingested, and charged on a per-metric basis. Cloud Monitoring provides this information to you on the [Metrics Management](https://docs.cloud.google.com/monitoring/docs/metrics-management) page. You can also access this information as metric data by using the [Samples Ingested metric or the Samples Written by Attribution ID metric](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls#identify-cost-sources). 



## Staleness

[Staleness](https://prometheus.io/docs/prometheus/latest/querying/basics/#staleness) is not supported in the Monarch backend.

## Calculation of `irate`

When the lookback window for the [`irate`](https://prometheus.io/docs/prometheus/latest/querying/functions/#irate) function is less than the step size, we increase the window to the step size. Monarch requires this change to ensure that none of the input data is completely ignored in the output. This difference applies to `rate` calculations as well.

## Calculation of `rate` and `increase`

When the lookback window for the [`rate`](https://prometheus.io/docs/prometheus/latest/querying/functions/#rate) function is less than the step size, we increase the window to the step size. Monarch requires this change to ensure that none of the input data is completely ignored in the output. This difference applies to `irate` calculations as well.

There are differences in the interpolation and extrapolation calculations. Monarch uses a different interpolation algorithm than Prometheus, and this difference can lead to slightly different results. For example, Monarch counter samples are stored with a time range rather than the single timestamp that Prometheus uses. Therefore, counter samples in Monarch can be included in a rate calculation even though the Prometheus timestamp would exclude them. This generally results in more accurate rate results, especially when querying over the beginning or end of the underlying time series.

## Calculation of `histogram_quantile`

A PromQL [`histogram_quantile`](https://prometheus.io/docs/prometheus/latest/querying/functions/#histogram_quantile) calculation on a histogram with no samples produces a NaN value. The internal query language's calculation produces no value; the point at the timestamp is dropped instead.

The rate-calculation differences can also affect the input to `histogram_quantile` queries.

## Type-specific functions on differently typed metrics

Although upstream Prometheus is weakly typed, Monarch is strongly typed. This means that running functions specific to a single type on a differently typed metric (for example, running `rate()` on a GAUGE metric or `histogram_quantile()` on a COUNTER or untyped metric) doesn't work in Managed Service for Prometheus, even though these functions work in upstream Prometheus.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
