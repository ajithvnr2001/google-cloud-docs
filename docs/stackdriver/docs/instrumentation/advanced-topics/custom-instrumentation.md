---
url: https://docs.cloud.google.com/stackdriver/docs/instrumentation/advanced-topics/custom-instrumentation/
title: Add custom traces and metrics to your app \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:39.354501+00:00
---

# Add custom traces and metrics to your app  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/instrumentation/advanced-topics/custom-instrumentation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Add custom traces and metrics to your app Stay organized with collections  Save and categorize content based on your preferences. 

Adding custom [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/) instrumentation to your application code lets you record custom trace spans and metrics that measure application-specific behavior beyond what standard framework libraries collect. You can apply the concepts in this document to applications written in any language supported by OpenTelemetry; for background information, see [Observability for application developers](https://docs.cloud.google.com/stackdriver/docs/opentelemetry/application-developers) and [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach).

The examples in this document use the Go sample application described in [Go instrumentation sample](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/go), which is available in GitHub.

## Before you begin

Enable the Cloud Logging, Cloud Monitoring, and Cloud Trace APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=logging.googleapis.com,monitoring.googleapis.com,cloudtrace.googleapis.com)

## Create custom traces

To generate custom [traces](https://opentelemetry.io/docs/concepts/signals/traces/) from your application, you add instrumentation code that creates [OpenTelemetry spans](https://opentelemetry.io/docs/concepts/signals/traces/#spans). In OpenTelemetry, spans are the building blocks for traces.

To create a span, do the following:

  1. Modify your app to acquire an OpenTelemetry [`Tracer`](https://opentelemetry.io/docs/concepts/signals/traces/#tracer). In OpenTelemetry, a tracer is a creator of spans. You can acquire a tracer as demonstrated in the following code. To view the full sample, in the sample's toolbar, select the GitHub logo.
         
         const scopeName = "github.com/GoogleCloudPlatform/golang-samples/opentelemetry/instrumentation/app/work"
         
         var (
         	meter                = otel.Meter(scopeName)
         	tracer               = otel.Tracer(scopeName)
         	sleepHistogram       metric.Float64Histogram
         	subRequestsHistogram metric.Int64Histogram
         )
         

The tracer name, which is represented by `scopeName`, identifies the [instrumentation scope](https://opentelemetry.io/docs/concepts/instrumentation-scope/) of the generated traces.

  2. Use the `tracer` instance to create spans. In the following code sample, the `computeSubrequests` function generates a span whenever it is called:
         
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
         

In the previous code sample, the span generated from the `computeSubrequests` function represents the work done by the entire function. This is because the first step of the function is to start a new span using `tracer.Start` and the `defer` keyword before the `span.End()` ensures that the span is ended right before the function exits.

**Note:** You must call `End()` to complete the span. OpenTelemetry only exports completed spans.



## Create custom metrics

To generate [metrics](https://opentelemetry.io/docs/concepts/signals/metrics/) from your application, you add instrumentation code that records measurements taken during your app's execution.

To create metrics, do the following:

  1. Modify your app to acquire an OpenTelemetry [`Meter`](https://opentelemetry.io/docs/specs/otel/metrics/api/#meter). In OpenTelemetry, a meter provides access to [metric instruments](https://opentelemetry.io/docs/concepts/signals/metrics/#metric-instruments) for recording metrics. You can acquire a meter as demonstrated in the following code:
         
         const scopeName = "github.com/GoogleCloudPlatform/golang-samples/opentelemetry/instrumentation/app/work"
         
         var (
         	meter                = otel.Meter(scopeName)
         	tracer               = otel.Tracer(scopeName)
         	sleepHistogram       metric.Float64Histogram
         	subRequestsHistogram metric.Int64Histogram
         )
         

The meter name, which is represented by `scopeName`, identifies the [instrumentation scope](https://opentelemetry.io/docs/concepts/instrumentation-scope/) of the generated metrics.

  2. Use the `meter` instance to create instruments that can record metrics. For example, the following code uses the `meter` to create an [OpenTelemetry Histogram](https://opentelemetry.io/docs/specs/otel/metrics/data-model/#histogram):
         
         sleepHistogram, err = meter.Float64Histogram("example.sleep.duration",
         	metric.WithDescription("Sample histogram to measure time spent in sleeping"),
         	metric.WithExplicitBucketBoundaries(0.05, 0.075, 0.1, 0.125, 0.150, 0.2),
         	metric.WithUnit("s"))
         if err != nil {
         	panic(err)
         }

The previous code generates a histogram named `sleepHistogram`.

  3. Use the `sleepHistogram` instance to record the sleep time, which is determined when the function `randomSleep` is invoked:
         
         func randomSleep(r *http.Request) time.Duration {
         	// simulate the work by sleeping 100 to 200 ms
         	sleepTime := time.Duration(100+rand.Intn(100)) * time.Millisecond
         	time.Sleep(sleepTime)
         
         	hostValue := attribute.String("host.value", r.Host)
         	// custom histogram metric to record time slept in seconds
         	sleepHistogram.Record(r.Context(), sleepTime.Seconds(), metric.WithAttributes(hostValue))
         	return sleepTime
         }
         

The recorded metrics from these instruments are exported from your application based on your OpenTelemetry exporter configuration.




## What's next

  * [Correlate metrics and traces by using exemplars](https://docs.cloud.google.com/stackdriver/docs/instrumentation/advanced-topics/exemplars)
  * [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/)
  * [OpenTelemetry Instrumentation](https://opentelemetry.io/docs/concepts/instrumentation/)
  * [OpenTelemetry Metrics Data Model](https://opentelemetry.io/docs/specs/otel/metrics/data-model/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
