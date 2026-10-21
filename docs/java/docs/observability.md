---
url: https://docs.cloud.google.com/java/docs/observability/
title: Enable telemetry signals in Cloud Client Libraries for Java \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:16.222309+00:00
---

# Enable telemetry signals in Cloud Client Libraries for Java  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Guides ](https://docs.cloud.google.com/java/docs/setup)



Send feedback 

#  Enable telemetry signals in Cloud Client Libraries for Java Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud provides powerful monitoring, logging, and diagnostics for Java applications.

The Java client libraries are instrumented to emit tracing, metrics, and logging data. The instrumentation is opt-in; you need to explicitly enable it. This document describes the available signals and how to enable them.

## Available signals

Golden Signals include the following telemetry data, adhering to [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/):

  * **Traces:** Low-level HTTP/gRPC traces representing the network requests made by the client libraries.
  * **Metrics:** Client request metrics, tracking latency and request rates. The primary metric is `gcp.client.request.duration`.
  * **Logs:** Actionable error logs at the `DEBUG` level, providing details for failed requests at the transport layer, even if they are eventually retried successfully.



The signals include standard OpenTelemetry attributes (for example, `http.response.status_code` and `rpc.system.name`) and Google Cloud-specific custom attributes, which may include these and similar attributes:

  * `gcp.client.service`: The service name (for example, `pubsub` or `storage`).
  * `gcp.client.repo`: The client library repository (for example, `googleapis/google-cloud-java`).
  * `gcp.client.version`: The client library version.
  * `gcp.client.artifact`: The specific module path (for example, `com.google.cloud:google-cloud-secretmanager`).
  * `gcp.resource.destination.id`: The ID of the resource being acted upon.
  * `gcp.errors.domain`: The error domain for actionable error logs.
  * `gcp.errors.metadata.<key>`: Additional error metadata keys for failed requests (flattened).



For a full list of standard attributes, see the [OpenTelemetry HTTP and gRPC semantic conventions](https://opentelemetry.io/docs/specs/semconv/).

## Enabling telemetry

To protect sensitive data, telemetry signals are disabled by default. You must explicitly opt in to enable them.

Traces, logs, or metrics may contain sensitive data such as resource names, full URLs, and error messages.

Before configuring subscribers or exporters for traces, logs, or metrics, review the contents of the spans and consult the [OpenTelemetry](https://opentelemetry.io/docs/security/handling-sensitive-data/) documentation to set up filters and formatters to prevent leaking sensitive information, depending on your intended use case.

### Tracing and metrics

In the generated Java client libraries, you must enable tracing and metrics programmatically by providing the appropriate tracer factory to your client's settings during initialization:

  * **Tracing:** Configure the client with an `OpenTelemetryTracingFactory`.
  * **Metrics:** Configure the client with an `OpenTelemetryMetricsFactory`.
  * **Both:** If you want to enable both tracing and metrics, configure the client with a `CompositeTracerFactory` that wraps both factories.



For the Java BigQuery SDK, enable tracing by setting `BigQueryOptions.newBuilder().setEnableOpenTelemetryTracing(true)` and providing the OpenTelemetry tracer.

### Logging

Actionable error logs are integrated directly into the core `ApiTracer` framework. To turn on actionable error logs globally across your Google Cloud client libraries, use the following environment variable:
    
    
    export GOOGLE_SDK_JAVA_LOGGING=true
    

## Trace context propagation

Trace context propagation in the Java client libraries requires tracing to be explicitly enabled.

When trace generation is enabled (for example, by configuring an `OpenTelemetryTracingFactory`) and your application has an active OpenTelemetry span in the current context when a client library method is called, the library uses it to provide a tracing context for the outgoing requests. This ensures that your application-level traces can be correlated with backend service logs and behaviors.

## Exporting telemetry

Once telemetry is enabled in the client libraries, your application must be configured to collect and export this data to your observability backend.

### Tracing and metrics

To export the traces and metrics generated by the Java client libraries, initialize the OpenTelemetry SDK with your preferred exporter (for example, OTLP) and set up the global text map propagator in your application.

For more details on collecting and exporting OpenTelemetry data to Cloud Monitoring or Cloud Trace, see [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach).

### Logging

The Java client libraries use standard logging frameworks like SLF4J and `java.util.logging`. When `GOOGLE_SDK_JAVA_LOGGING=true` is set, actionable error logs are emitted at the `DEBUG` level.

To route these structured logs to Cloud Logging, configure your logging framework (for example, Logback) to write JSON to standard output (`stdout`). If you are deploying to an environment like Google Kubernetes Engine or Cloud Run, the built-in agents automatically scrape these logs.

For detailed instructions on configuring Logback or `java.util.logging` to output Cloud Logging compatible JSON, including trace correlation, see [Configure structured logging for Java](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/java#config-structured-logging).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
