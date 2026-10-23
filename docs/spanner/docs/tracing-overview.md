---
url: https://docs.cloud.google.com/spanner/docs/tracing-overview/
title: Trace collection overview \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:51.114755+00:00
---

# Trace collection overview  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/tracing-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Trace collection overview Stay organized with collections  Save and categorize content based on your preferences. 

This page offers overview information about trace collection with OpenTelemetry. To monitor and debug Spanner requests, you can enable traces in the [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries). Client-side and end-to-end tracing can help you monitor performance and debug issues.

Traces provide relevant information for every request from a client, such as the following:

  * Spans with timestamps of when the client sent an RPC request and when the client received the RPC response, including latency caused by the network and client system.

  * Attributes (key-value pairs) that provide information about the client and its configuration.

  * Annotations with important events in the spans.




For more information about spans and attributes, see [Spans](https://opentelemetry.io/docs/concepts/observability-primer/#spans) and [Attributes](https://opentelemetry.io/docs/concepts/signals/traces/#attributes) in the OpenTelemetry documentation.

## End-to-end tracing

In addition to client-side tracing, you can opt in for end-to-end tracing. End-to-end tracing helps you understand and debug latency issues that are specific to Spanner such as the following:

  * Identify whether the latency is due to network latency between your application and Spanner, or if the latency is occurring within Spanner.

  * Identify the Google Cloud regions that your application requests are being routed through and if there is a cross-region request. A cross-region request usually means higher latencies between your application and Spanner.




To prevent overloading Cloud Trace and help manage costs effectively, end-to-end tracing has a limit on the number of trace spans you can export. There's no impact on using end-to-end tracing for troubleshooting because of this limit.

## OpenTelemetry

Spanner client libraries support trace collection using [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry/) APIs. OpenTelemetry is an open-source observability framework. OpenTelemetry offers a wide range of configurations such as exporters for specific backends, sampling ratios, and span limits.

### Export traces using OTLP

As part of your OpenTelemetry configuration, you use an exporter to send trace data to an observability backend. We recommend using an [OpenTelemetry Protocol (OTLP) exporter](https://opentelemetry.io/docs/specs/otel/protocol/exporter/) that sends data using the OpenTelemetry protocol. You can configure the OTLP exporter to send traces directly to observability backends that support OTLP, such as Cloud Trace using [`Telemetry API`](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview), or to an OpenTelemetry [collector](https://opentelemetry.io/docs/collector/).

## Limitations

Spanner traces have the following limitations:

  * Trace spans are available only for the Java, Go, Node, and Python client libraries.
  * End-to-end traces can only be exported to Cloud Trace.



## Pricing

In addition to Spanner usage, tracing can incur charges through your observability backend.

Ingestion of trace spans into your observability backend is billable. For example, if you use Cloud Trace as your backend, you are billed according to [Cloud Trace pricing](https://cloud.google.com/stackdriver/pricing#trace-costs).

To better understand billing, start with a small trace sampling ratio based on your traffic.

## What's next

To set up client-side and end-to-end tracing, see [Set up trace collection using OpenTelemetry](https://docs.cloud.google.com/spanner/docs/set-up-tracing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
