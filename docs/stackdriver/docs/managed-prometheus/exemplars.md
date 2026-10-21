---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exemplars/
title: Use Prometheus exemplars \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:30.974168+00:00
---

# Use Prometheus exemplars  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exemplars/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Use Prometheus exemplars Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can use Google Cloud Managed Service for Prometheus to ingest [Prometheus exemplars](https://prometheus.io/docs/prometheus/latest/feature_flags/#exemplars-storage) on histogram metrics. You must use one of the following:

  * Managed Service for Prometheus managed collection version 0.7.0 or higher
  * Managed Service for Prometheus self-deployed collection version 2.35.0-gmp.5-gke.0 or higher
  * The [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/)



Exemplars are typically used to associate trace identifiers with metric data collected in a time interval, but they can be used to associate any non-metric data with the collected metrics. Storing trace information with the metric data lets you quickly identify the traces associated with a sudden change in metric values; you don't have to manually cross-reference trace information and metric data by using timestamps to identify what was happening in the application when the metric data was recorded.

Managed Service for Prometheus exemplars are compatible both with Cloud Trace and with 3rd-party trace tools such as Grafana Tempo.

The following screenshot shows a Grafana chart of sets of histogram buckets and associated exemplars, with one exemplar expanded:

![Grafana chart showing histogram buckets and
exemplars.](https://docs.cloud.google.com/static/stackdriver/images/gmp-exemplars-grafana.png)

## Prometheus exemplars in Managed Service for Prometheus

Exemplars are supported in Prometheus by using the [OpenMetrics exposition format](https://github.com/OpenObservability/OpenMetrics/blob/main/specification/OpenMetrics.md). An OpenMetrics exemplar has the following structure:

  * The value of the exemplar: must be either an integer or a 64-bit float.
  * (Optional) A timestamp: must be [Unix Epoch seconds](https://timezonedb.com/unix-time), can be negative.
  * A number of labels for the exemplar, typically including `trace_id` and `span_id` values; the total length of all label names and values must not exceed 128 UTF-8 characters, or 128 [runes](https://go.dev/blog/strings) in Go applications.



Google Cloud Managed Service for Prometheus can only ingest exemplars attached to histogram metrics. **Exemplars attached to counter metrics can't be ingested.** Prometheus histogram metrics are converted to the analogous Cloud Monitoring [`Distribution`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Distribution) type, which supports exemplars. Non-distribution metrics in Cloud Monitoring do not support exemplars.

Exemplars remain available for querying for 24 months. Compare this retention period to upstream Prometheus, where exemplars are retained only while the data is in-memory, typically less than 14 days. Managed Service for Prometheus stores exemplars with the time series, so the exemplars are retained according to the retention policy for the time series. For more information about data retention in Cloud Monitoring, see [Data retention](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy).

## Enable ingestion of exemplars

If you are using Managed Service for Prometheus with [managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) version 0.7.0 or higher, then ingestion of exemplars is automatically enabled.

If you are using Managed Service for Prometheus with [self-deployed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged), then you must enable ingestion of exemplars when you start the server by specifying the following [feature flag](https://prometheus.io/docs/prometheus/latest/feature_flags/#exemplars-storage):
    
    
    --enable-feature=exemplar-storage
    

## Write metrics with exemplars

Each Prometheus client has its own instructions for properly using exemplars in that client. Follow these instructions so that your application exposes metrics in the OpenMetrics format for Prometheus to scrape from the application's `/metrics` endpoint. For examples, see the following:

  * OpenTelemetry [Java example](https://github.com/open-telemetry/opentelemetry-java-docs/tree/main/prometheus#prometheus-example)
  * Prometheus [Java client](https://github.com/prometheus/client_java/blob/main/examples/example-exemplars-tail-sampling/README.md)
  * Prometheus [Python client](https://github.com/prometheus/client_python#exemplars)
  * Prometheus [Go client](https://github.com/prometheus/client_golang/blob/main/examples/exemplars/main.go)



## Integrate with Cloud Trace

You can write Prometheus histograms with exemplars that are compatible with Cloud Trace. You can display the data, including the exemplars, on a Cloud Monitoring heatmap chart, where you can use the exemplars to view details about the related trace spans. You can also analyze the trace data in Trace. For more information, see [Show exemplars on a heatmap chart](https://docs.cloud.google.com/monitoring/charts/working-with-charts#show-exemplars).

To create exemplars that are compatible with Trace, your Prometheus exemplars must contain the following labels:

  * `project_id`
  * `trace_id`
  * `span_id`



If your exemplar includes these three labels, then the labels are used to create a Trace-compatible [`SpanContext`](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#spancontext) object that is attached to the exemplar created for the Cloud Monitoring [`Distribution`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Distribution) bucket.

All labels other than those that make up a complete `SpanContext` are added to a [`DroppedLabels`](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#droppedlabels) object attached to the exemplar for a `Distribution` bucket.

## Query metrics with exemplars

The Prometheus API exposes the [`api/v1/query_exemplars`](https://prometheus.io/docs/prometheus/latest/querying/api/#querying-exemplars) endpoint for querying exemplars.

Query interfaces set up to interact with Google Cloud Managed Service for Prometheus automatically include exemplar querying. For information about setting up query interfaces, see [Query using Grafana](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query) or [Query using the Prometheus API or UI](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
