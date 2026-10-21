---
url: https://docs.cloud.google.com/trace/docs/trace-context/
title: Trace context \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:58.689700+00:00
---

# Trace context  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/trace-context/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Trace context Stay organized with collections  Save and categorize content based on your preferences. 

_Trace context_ and _context propagation_ let your distributed applications pass request identifiers across services in headers or metadata. Cloud Trace uses this shared context to link individual spans into complete distributed traces, reconstruct execution hierarchies, and evaluate whether requests are sampled.

## How context propagation works

When your application handles a request and calls downstream services, it passes identifiers—such as the trace ID, parent span ID, and sampling status—by using request headers or metadata. Child operations use this context to populate the following fields on new spans:

  * **Span ID** : A unique identifier for the child operation. If an operation is executed multiple times, then each invocation generates a span with a distinct span ID.
  * **Trace ID** : The unique identifier of the overall end-to-end request, provided by the parent.
  * **Parent span ID** : The unique identifier of the invoking parent span. This field is `null` for root spans.



Using these shared identifiers, Trace reconstructs the execution hierarchy and measures latency across all participating services. Context can also include additional state information, such as whether a request was [sampled](https://docs.cloud.google.com/trace/docs/trace-sampling).

## Protocols for context propagation

The following sections describe how specific request protocols propagate context.

### HTTP requests

For HTTP requests, context propagation is typically accomplished through HTTP headers such as the `traceparent` and `tracestate` headers, which were [standardized by W3C](https://www.w3.org/TR/trace-context/). The `traceparent` header contains the identifiers to uniquely identify a request. In contrast, the `tracestate` header is optional and it contains vendor-specific metadata.

The `traceparent` header has the following format:
    
    
    traceparent: VERSION-TRACE_ID-PARENT_SPAN_ID-TRACE_FLAGS
    

The fields of the `traceparent` header are defined as follows:

  * `VERSION` is the header version. Must be `00`.
  * `TRACE_ID` is a 32-character hexadecimal value representing a 128-bit number.
  * `PARENT_SPAN_ID` is a 16-character hexadecimal value that identifies the parent span.
  * `TRACE_FLAGS` is a 2-character hexadecimal value that identifies the parent's sampling decision. When a parent sampled the span, the value is `01`.



Google Cloud services that support trace context propagation typically support both the `traceparent` and the legacy `X-Cloud-Trace-Context` header.

When possible, use the [`traceparent` header](https://www.w3.org/TR/trace-context/) in your applications. If an application only supports the `X-Cloud-Trace-Context` header, then we recommend that you update the application to support and prioritize the `traceparent` header. Your application can continue to use the `X-Cloud-Trace-Context` header as a fallback solution.

The following table summarizes some significant differences between the two headers:

Attribute | `traceparent`  
header | `X-Cloud-Trace-Context`  
header  
---|---|---  
Separators | hyphens `(-)` | forward slash `(/)` and semicolon `(;)`  
Span ID  
representation | Hexadecimal | Decimal  
  
#### Legacy `X-Cloud-Trace-Context` header

The `X-Cloud-Trace-Context` header used by Google Cloud predates the W3C specification. For backwards compatibility, some Google Cloud services continue to accept, generate, and propagate the `X-Cloud-Trace-Context` header. However, it is likely that these systems also support the `traceparent` header.

The `X-Cloud-Trace-Context` header has the following format:
    
    
    X-Cloud-Trace-Context: TRACE_ID/SPAN_ID;o=OPTIONS
    

The fields of the header are defined as follows:

  * `TRACE_ID` is a 32-character hexadecimal value representing a 128-bit number.
  * `SPAN_ID` is a 64-bit decimal representation of the unsigned span ID.
  * `OPTIONS` supports `0` (parent not sampled) and `1` (parent was sampled).



### gRPC requests

For [gRPC](https://grpc.io/) requests, context propagation is accomplished using [gRPC metadata](https://grpc.io/docs/guides/metadata/), which is implemented on top of HTTP headers. gRPC applications might use the `traceparent` header or a metadata context key called `grpc-trace-bin`.

For components that you own, we recommend that you use the `traceparent` header.

## Context propagation for Google Cloud services

**Note:** Cloud Trace isn't responsible for context propagation. Context propagation is the responsibility of the components that submit data to Cloud Trace. These components include Google Cloud services and user applications.

Google Cloud services might act as initiators or intermediaries in request processing. For example, the following services are known to participate in processing requests:

  * [Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-distributed-trace)
  * [App Engine](https://docs.cloud.google.com/appengine)
  * [Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/tracing#trace_sampling_rate)
  * [Cloud Run functions](https://docs.cloud.google.com/functions)
  * [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing)
  * [Cloud Run](https://docs.cloud.google.com/run/docs/trace)
  * [Cloud Scheduler](https://docs.cloud.google.com/scheduler)
  * [Cloud Tasks](https://docs.cloud.google.com/tasks)
  * [Pub/Sub](https://docs.cloud.google.com/pubsub)



Support for trace context initiation and propagation depends on the specific Google Cloud service. To request that a Google Cloud service add support for context propagation, use the [Google Issue Tracker](https://developers.google.com/issue-tracker/guides/access-ui).

## Context propagation in your applications

Some instrumentation libraries, such as OpenTelemetry, can propagate a `context` object that contains the data necessary for tracing. For a list of OpenTelemetry libraries that support tracing, see [Language APIs & SDKs](https://opentelemetry.io/docs/languages/).

If you rely on an open-source library, then determine whether context propagation is available and whether configuration is required. For example, if you use OpenTelemetry to instrument a Go app, then your app should call `SetTextMapPropagator`, which configures the context to use the W3C `traceparent` format. For an example, see [Go instrumentation sample](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/go).

When there isn't a suitable instrumentation library, you must ensure that your application propagates the trace context to child operations.

## What's next

  * Learn about [Trace sampling](https://docs.cloud.google.com/trace/docs/trace-sampling).

  * OpenTelemetry resources:

    * [OpenTelemetry home](https://opentelemetry.io)
    * [OpenTelemetry context](https://opentelemetry.io/docs/specs/otel/context/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
