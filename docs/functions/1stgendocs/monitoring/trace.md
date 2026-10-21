---
url: https://docs.cloud.google.com/functions/1stgendocs/monitoring/trace/
title: Use distributed tracing \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:43.481513+00:00
---

# Use distributed tracing  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/monitoring/trace/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use distributed tracing

All inbound requests to a Cloud Run function automatically generate a basic set of _trace data_ to help you measure timing and identify causes of latency in your function.

For more detailed tracing, you can add [additional instrumentation](https://docs.cloud.google.com/trace/docs/setup#instrumenting_tracing_for_applications) to your Cloud Run function. This lets you measure the time it takes for the request to complete different sub-operations within your function, such as database queries, API requests, or complex business logic. Each of these layer-specific time measurements is a called a _span_.

You can view an analysis of your traces with [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview).

## Trace sampling rate

Cloud Run functions performs tracing at a maximum rate of one request per ten second interval for each Cloud Run function instance. You can also [force a particular request to be traced](https://docs.cloud.google.com/trace/docs/setup#force-trace).

## Billing charges

Automatically generated traces, whether sampled or forced, don't cause billing charges. However, if you use Cloud Trace libraries and add your own spans by correlating them to Cloud Run functions provided spans, you are charged by [Cloud Trace](https://cloud.google.com/stackdriver/pricing#trace-costs).

## When to add instrumentation

If you need more trace information than the automatically-generated trace data, you must add instrumentation code to your service to enable additional tracing. For example, you need to add instrumentation to:

  * Create custom trace spans, such as monitoring how long it takes your service to get results back from API requests.
  * Propagate trace context so Cloud Trace shows the request flow across multiple services as a single request.



To add instrumentation, refer to [Instrumenting tracing for applications](https://docs.cloud.google.com/trace/docs/setup#instrumenting_tracing_for_applications).

**Note:** If you add custom tracing, [adding labels to your spans](https://docs.cloud.google.com/trace/docs/trace-labels) makes it easier to filter for them in the Cloud Trace UI.

## View your traces

To view an analysis of your trace data, see [viewing traces](https://docs.cloud.google.com/trace/docs/finding-traces).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
