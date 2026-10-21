---
url: https://docs.cloud.google.com/stackdriver/docs/instrumentation/advanced-topics/exemplars/
title: Correlate metrics and traces by using exemplars \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:04.728477+00:00
---

# Correlate metrics and traces by using exemplars  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/instrumentation/advanced-topics/exemplars/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Correlate metrics and traces by using exemplars Stay organized with collections  Save and categorize content based on your preferences. 

You can use exemplars to correlate your metric and trace data. An _exemplar_ is a representative sample request or span associated with a metric measurement. Your application can create and attach exemplars to metric data. Alternatively, Google Cloud Observability can generate them dynamically when charting query results. By linking an individual trace ID to an aggregated metric, exemplars help you quickly investigate the root cause of latency spikes or errors.

This document describes how to configure [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/) to create and attach trace exemplars to your metric data.

If you chart SQL query results on a dashboard, Google Cloud Observability can also generate exemplars automatically. For more information, see [Generate and display trace exemplars](https://docs.cloud.google.com/stackdriver/docs/observability/analytics-chart#show-trace-exemplars).

## About exemplars

Exemplars are a way to associate arbitrary data with metric data. You can use them to attach non-metric data to measurements. One use of exemplars is to associate trace data with metric data. In Cloud Monitoring, exemplars can be attached to metric data that has the [`Distribution`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Distribution) value type. Distribution-valued metrics collect many measurements and group them into buckets. Each "point" is a histogram, which is an array that lists bucket counts. The actual measurements aren't retained, only the bucket counts. For more information, see [About distribution-valued metrics](https://docs.cloud.google.com/monitoring/charts/charting-distribution-metrics).

When a metric data point is written, an array of [`Exemplar`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Exemplar) objects can be attached to that data. Exemplars, when used, attach useful information to the metric data. For example, when OpenTelemetry writes an exemplar, it attaches a link to the current [span of a trace](https://opentelemetry.io/docs/concepts/signals/traces/#spans).

Histogram data is typically displayed by using a heatmap. When a "point" contains an exemplar, Cloud Monitoring annotates the heatmap with a dot:

  * To view summary information about the metric point, activate the tooltip for the annotation.
  * To access the trace, select the annotation.



For example, the [Go instrumentation sample](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/go) uses OpenTelemetry to write metric data, trace data, and exemplars. The following screenshot shows the value of the `prometheus/http_server_duration_milliseconds/histogram` metric after several executions of the application:

![Example of a heatmap showing multiple exemplars.](https://docs.cloud.google.com/static/stackdriver/docs/instrumentation/images/exemplar-sample-trace.png)

The previous screenshot shows multiple exemplars. The tooltip for one exemplar is expanded, and it shows the date, the trace name, percentiles, and a latency value.

When the annotation is selected, the trace linked in the exemplar is displayed:

![Example of the trace details for an exemplar.](https://docs.cloud.google.com/static/stackdriver/docs/instrumentation/images/exemplar-sample-trace-flyout.png)

When the displayed information isn't sufficiently detailed, you can select **View in Trace** , which opens the **Trace Explorer** page. On that page, you can view trace attributes and access links to log entries.

## How to enable OpenTelemetry exemplars

As the previous example illustrates, you can configure OpenTelemetry to write exemplars that link the current [span](https://opentelemetry.io/docs/concepts/signals/traces/#spans) of a trace to a metric measurement. However, for exemplars to be written, you must do the following:

  1. Configure both the OpenTelemetry metric and trace SDKs.
  2. To include exemplars on your custom instrumentation, ensure that the metric is recorded within a span, and that you pass the context from the span with the metric measurement.

For example, the `computeSubrequests` function follows the previous guidance. The function `subRequestsHistogram.Record` is invoked after `tracer.Start` and before `span.End`, which is deferred. Also notice that the context, `ctx`, is passed from `tracer.Start` to the `Record` function:
         
         func computeSubrequests(r *http.Request, subRequests int) error {
         	// Add custom span representing the work done for the subrequests
         	ctx, span := tracer.Start(r.Context(), "subrequests")
         	defer span.End()
         
         	// Make specified number of http requests to the /single endpoint.
         	for i := 0; i < subRequests; i++ {
         		if err := callSingle(ctx); err != nil {
         			return err
         		}
         	}
         	// record number of sub-requests made
         	subRequestsHistogram.Record(ctx, int64(subRequests))
         	return nil
         }
         

For more information about this sample, see [Add custom traces and metrics to your app](https://docs.cloud.google.com/stackdriver/docs/instrumentation/advanced-topics/custom-instrumentation).




## What's next

  * [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/)
  * [OpenTelemetry Exemplars](https://opentelemetry.io/docs/specs/otel/metrics/data-model/#exemplars)
  * [OpenTelemetry Metrics Data Model](https://opentelemetry.io/docs/specs/otel/metrics/data-model/)
  * [OpenTelemetry Histogram](https://opentelemetry.io/docs/specs/otel/metrics/data-model/#histogram)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
