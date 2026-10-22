---
url: https://docs.cloud.google.com/trace/docs/traces-and-spans/
title: Traces and spans \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:42.991087+00:00
---

# Traces and spans  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/traces-and-spans/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Traces and spans Stay organized with collections  Save and categorize content based on your preferences. 

In Cloud Trace, traces and spans form the data model used to track the path and latency of requests through your distributed applications. A _trace_ captures how a request runs end-to-end across your services. A trace is composed of _spans_ , which record the individual operations, function calls, and RPCs that occur during that request.

## Trace data model

A trace consists of the following:

  * **Trace ID** : The unique identifier of the end-to-end operation. The trace ID is propagated in the [request context](https://docs.cloud.google.com/trace/docs/trace-context) across service boundaries.

  * **Span collection** : A set of spans that share the same trace ID. These spans form a tree or a directed acyclic graph that represents the call hierarchy of a request.




Cloud Trace uses the trace ID to identify which spans in its repository are associated with the same trace.

## Span data model

A span represents a single operation that occurred within a specific time period. Each span contains fields that provide information about the span and the status of the operation:

  * Identifiers include the following fields:

    * **Trace ID** : The unique identifier of the overall request or trace to which the span belongs.
    * **Span ID** : The unique identifier for the span. If an operation is invoked multiple times within a single trace, each invocation generates a separate span with the same name but a unique span ID.
    * **Parent span ID** : Identifies the parent operation that invoked this span. The "root" span has the parent span ID set to `null`.
    * **Name** : The name of the operation that was performed.
    * **Kind** : The span kind provides information to tracing tools, such as the **Trace Explorer** , about how spans are related to each other. For more information, see [OpenTelemetry SpanKind](https://opentelemetry.io/docs/specs/otel/trace/api/#spankind).
  * Execution information is provided in the following fields:

    * **Status** : Records the completion status of the operation. The value of this field is `Unset` (default), `Error`, or `Ok`. The default value doesn't indicate an error.
    * **Start time** : The start time of the operation.
    * **End time** : The end time of the operation.



Spans can contain other fields, such as events, attributes, and links:

  * **Events** record timestamped structured messages within a span.
  * **Attributes** store additional information about an operation by using key-value pairs. When writing attributes, we recommend that you follow the [OpenTelemetry Semantic Conventions](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/README.md) where possible.
  * **Links** let you relate one span to another.



For more information, see [OpenTelemetry: Spans](https://opentelemetry.io/docs/concepts/signals/traces/#spans).

## Resources

OpenTelemetry resources:

  * [OpenTelemetry](https://opentelemetry.io)
  * [OpenTelemetry Trace overview](https://opentelemetry.io/docs/specs/otel/overview/#traces)
  * [OpenTelemetry Traces](https://opentelemetry.io/docs/concepts/signals/traces/)
  * [OpenTelemetry `trace.proto`](https://github.com/open-telemetry/opentelemetry-proto/blob/v1.1.0/opentelemetry/proto/trace/v1/trace.proto)



## What's next

  * Learn about [context and context propagation](https://docs.cloud.google.com/trace/docs/trace-context).
  * Learn about [sampling](https://docs.cloud.google.com/trace/docs/trace-sampling).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
