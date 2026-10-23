---
url: https://docs.cloud.google.com/run/docs/trace/
title: Using distributed tracing \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:51.725387+00:00
---

# Using distributed tracing  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/trace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Using distributed tracing Stay organized with collections  Save and categorize content based on your preferences. 

Incoming requests to Cloud Run services automatically generate traces that you can view in [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview). You can use these traces to identify sources of any latency issues in your implementation without needing to add further instrumentation in Cloud Trace. The standard W3C trace context propagation header [`traceparent`](https://www.w3.org/TR/trace-context/#traceparent-header) is automatically populated for Cloud Run requests.

However, if you do add [additional instrumentation](https://docs.cloud.google.com/trace/docs/setup#instrumenting_tracing_for_applications), you can also use Cloud Trace to measure the time it takes for the request to propagate through each layer in your implementation, for example, the time it takes to complete a database query, receive results from an API request, or run some complex business logic. Each of these layer-specific time measurements is a "span". You can view the traces in Cloud Trace as waterfall graphs reflecting the latency values.

## Billing charges

Automatically generated traces in Cloud Run, whether sampled or forced, do not result in billing charges. However, if you use Cloud Trace libraries and add your own spans by correlating them to Cloud Run provided spans, you will be charged by [Cloud Trace](https://cloud.google.com/products/observability/pricing#trace-costs).

## Trace sampling rate

Cloud Run doesn't sample the traces for every request. When used with Cloud Run, requests are sampled at a maximum rate of 0.1 requests per second for each instance (or one request every 10 seconds). You can also [force a particular request to be traced](https://docs.cloud.google.com/trace/docs/setup#force-trace). If you force a request to be traced, this request is sampled at a maximum rate of 0.1 second for each instance (or 10 requests per second).

Cloud Run does not support configuration of the Cloud Run sample rate.

## When to add instrumentation

Traces are automatically generated without any instrumentation required in your service. However, in some cases, you may want to add instrumentation code to your service to take full advantage of the Cloud Trace feature. For example, you need to add instrumentation if you want to:

  * Create custom trace spans, for example, to get timing data for how long it takes your service to get work back from the Cloud Translation API.
  * Propagate trace context so Cloud Trace shows the request flow across multiple services as a single request.



To add instrumentation, refer to [Instrumenting tracing for applications](https://docs.cloud.google.com/trace/docs/setup#instrumenting_tracing_for_applications). Note that traces resulting from instrumentation in your service will incur standard [Cloud Trace billing charges](https://cloud.google.com/products/observability/pricing).

**Note:** If you instrument trace and use custom spans, you may want to [add labels to the spans](https://docs.cloud.google.com/trace/docs/trace-labels) to make it easier to filter for them in the Cloud Trace UI.

## Viewing traces

To learn more, refer to the documentation on [viewing traces](https://docs.cloud.google.com/trace/docs/finding-traces).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
