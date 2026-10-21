---
url: https://docs.cloud.google.com/trace/docs/reference/
title: Cloud Trace API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:38:48.769755+00:00
---

# Cloud Trace API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Reference ](https://docs.cloud.google.com/trace/docs/reference)



Send feedback 

#  Cloud Trace API Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Trace API lets you send latency data to, and retrieve latency data from, [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview). To send data to Cloud Trace, we recommend that you use [OpenTelemetry](https://opentelemetry.io/). OpenTelemetry is a Google-supported open source project with Google engineers staffed to ensure support for Cloud Trace. For more information about instrumenting an application, including instrumentation examples, see [Instrumentation and observability](https://docs.cloud.google.com/stackdriver/docs/instrumentation/overview).

To retrieve data from Cloud Trace, we recommend that you use the Cloud Trace API. By using the API, you have access to the exact data stored by Cloud Trace.

You can use the Cloud Trace API from applications you run locally or on any of the following environments:

  * [Compute Engine](https://docs.cloud.google.com/compute/docs)
  * [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-distributed-trace) (Public Preview)
  * [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible)
  * [App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard)
  * [Cloud Run](https://docs.cloud.google.com/run/docs/trace)
  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/observability/accessing-traces)
  * [Cloud SQL query insights](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights)
  * Non-Google Cloud environments



Data sent to Cloud Trace using this API is available for display, reporting, and analysis in the [Google Cloud console](https://console.cloud.google.com/).

## Versions and interfaces

There are two supported versions of the API:

  * Cloud Trace API v1 lets you send and retrieve latency data by using HTTP or by using RPC. For more information, see [v1 REST](https://docs.cloud.google.com/trace/docs/reference/v1/rest) and [v1 RPC](https://docs.cloud.google.com/trace/docs/reference/v2/rpc/google.devtools.cloudtrace.v1).

  * Cloud Trace API v2 lets you send latency data by using HTTP or by using [gRPC](http://www.grpc.io/). For more information, see [v2 REST](https://docs.cloud.google.com/trace/docs/reference/v2/rest) and [v2 RPC](https://docs.cloud.google.com/trace/docs/reference/v2/rpc/google.devtools.cloudtrace.v2).




For more details on how to automatically collect traces from an application, see the [Client libraries](https://docs.cloud.google.com/trace/docs/client-libraries) documentation.

## Data model

For information about the data model, see [Traces and spans](https://docs.cloud.google.com/trace/docs/traces-and-spans).

### Generating `trace_id` and `span_id`

The client libraries for Trace automatically generate the `trace_id` and the `span_id`. If you don't use the Trace client libraries or the OpenTelemetry client libraries, then you must generate the values for these fields. In this case, you should use a pseudo-random or random algorithm. Don't derive these fields from need-to-know data or from personally identifiable information.

## Operations

You can do the following with the Cloud Trace API:

  * Send traces to Cloud Trace
  * Update existing traces (v1 only)
  * Get lists of traces (v1 only)
  * Get the details of a single trace (v1 only)



The v2 API only supports sending trace data. There are no methods to retrieve the data.

### Send spans

**Note:** Cloud Trace quotas restrict the number of write operations performed. When you are developing or testing code, the v2 REST API method [`createSpan`](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2/projects.traces.spans/createSpan) can be useful. However, in production code, to make best use of your quota, use the `batchWrite` method.

In the v2 API, you send trace data to Cloud Trace by using the REST method [`batchWrite`](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2/projects.traces/batchWrite) or the RPC method [`batchWriteSpans`](https://docs.cloud.google.com/trace/docs/reference/v2/rpc/google.devtools.cloudtrace.v2#google.devtools.cloudtrace.v2.TraceService.BatchWriteSpans).

In the v1 API, you construct a [`Trace`](https://docs.cloud.google.com/trace/docs/reference/v1/rest/v1/projects.traces#Trace) object and then pass that to either a REST or gRPC method. The `Trace` object contains a collection spans. For the REST API, use the method [`patchTraces`](https://docs.cloud.google.com/trace/docs/reference/v1/rest/v1/projects/patchTraces). For the RPC API, use the method [`PatchTraces`](https://docs.cloud.google.com/trace/docs/reference/v2/rpc/google.devtools.cloudtrace.v1#google.devtools.cloudtrace.v1.TraceService.PatchTraces).

### Get a list of traces

To get a list of stored traces, send a request to the REST [`list`](https://docs.cloud.google.com/trace/docs/reference/v1/rest/v1/projects.traces/list) or RPC [`ListTraces`](https://docs.cloud.google.com/trace/docs/reference/v2/rpc/google.devtools.cloudtrace.v1#google.devtools.cloudtrace.v1.TraceService.ListTraces) methods. You can pass a filter condition to these requests to retrieve only those traces that were sent between a specific start and end time. The `list` and `ListTraces` methods return a set of trace entities.

### Get trace details

To get the details of particular trace, do the following:

  1. Find the ID of the trace. One way that you can find this information is by running the `list` command.

  2. Send a request to the REST [`get`](https://docs.cloud.google.com/trace/docs/reference/v1/rest/v1/projects.traces/get) or RPC [`GetTrace`](https://docs.cloud.google.com/trace/docs/reference/v2/rpc/google.devtools.cloudtrace.v1#google.devtools.cloudtrace.v1.TraceService.GetTrace) methods. The request specifies the trace by its ID. These methods return a single trace entity.




## Authorization

To use the Cloud Trace API, you or the service account must have authorization to do so. [Identity and Access Management](https://docs.cloud.google.com/iam/docs) defines permissions and roles you can use for authorization. For more information, see [Cloud Trace access control](https://docs.cloud.google.com/trace/docs/iam).

When running on Google Cloud, authorization is normally provided by default. When running outside of Google Cloud, you obtain authorization by creating a service account and then copy its private key credentials to the computer with the application using the Cloud Trace API.

For more information, see [Setting up authentication](https://docs.cloud.google.com/docs/authentication/production).

## Explore the API

You can use the in-page **Try It!** feature in the REST interface documentation to explore the API functionality. Using **Try It!** helps you understand how to assemble the data that you pass to the API and the structure and content of the data it returns. See the documentation of the v1 API [`list`](https://docs.cloud.google.com/trace/docs/reference/v1/rest/v1/projects.traces/list) method for an example.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
