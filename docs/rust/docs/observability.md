---
url: https://docs.cloud.google.com/rust/docs/observability/
title: Enable telemetry signals in Rust client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:42:00.324655+00:00
---

# Enable telemetry signals in Rust client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/rust/docs/observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Rust ](https://docs.cloud.google.com/rust/docs)
  * [ Guides ](https://docs.cloud.google.com/rust/docs/overview)



Send feedback 

#  Enable telemetry signals in Rust client libraries Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud provides powerful monitoring, logging, and diagnostics for Rust applications.

The Rust client libraries are instrumented to emit tracing, metrics, and logging data. The instrumentation is opt-in; you need to explicitly enable it. This document describes the available signals and how to enable them.

## Available signals

The Rust client libraries are instrumented to generate the following signals:

  1. `INFO` spans for each logical client request. Typically a single method call in the client struct gets such a span (for example, calling `access_secret_version` on a `SecretManagerService` client).
  2. A histogram metric measuring the elapsed time for each logical client request. The primary metric is `gcp.client.request.duration`.
  3. `WARN` logs for each logical client request that fails.
  4. `INFO` spans for each low-level RPC attempt. Typically a single method in the client struct gets one such span, but there may be more if the library has to retry the RPC.
  5. `DEBUG` logs for each low-level attempt that fails.



These spans and logs follow [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/) with additional Google Cloud attributes. Both the spans and logs should be suitable for production monitoring.

The signals include standard OpenTelemetry attributes (for example, `http.response.status_code` and `rpc.system.name`) and Google Cloud-specific custom attributes, which may include these and similar attributes:

  * `gcp.client.service`: The service name (for example, `pubsub` or `storage`).
  * `gcp.client.repo`: The client library repository (for example, `googleapis/google-cloud-rust`).
  * `gcp.client.version`: The client library version.
  * `gcp.client.artifact`: The specific module path (for example, `google-cloud-secretmanager`).
  * `gcp.resource.destination.id`: The ID of the resource being acted upon.
  * `gcp.errors.domain`: The error domain for actionable error logs.
  * `gcp.errors.metadata.<key>`: Additional error metadata keys for failed requests (flattened).



For a full list of standard attributes, see the [OpenTelemetry HTTP and gRPC semantic conventions](https://opentelemetry.io/docs/specs/semconv/).

The libraries also have `DEBUG` spans for each request. These include the full request body, the full response body for successful requests, and the full error message, with details, for failed requests.

Consider the contents of these requests and responses before enabling them in production environments, as the request or responses may include sensitive data.

These `DEBUG` spans use the client library crate followed by `::tracing` as their target (for example, `google_cloud_secretmanager_v1::tracing`) and the method name as the span name (for example, `access_secret_version`). You can use the name, target, or both to set up your filters.

## Enabling telemetry

Observability signals at any level may contain sensitive data such as resource names, full URLs, and error messages.

Before configuring subscribers or exporters for traces and logs, review the contents of the spans and consult the [tracing](https://docs.rs/tracing/latest/tracing/) framework documentation to set up filters and formatters to prevent leaking sensitive information, depending on your intended use case.

To protect sensitive data, telemetry signals are disabled by default.

In Rust, you must configure the client to emit traces, metrics, and logs **and** must configure subscribers and exporters to send these signals to an external service.

To configure the client, you can set the following environment variable:
    
    
    export GOOGLE_CLOUD_RUST_LOGGING=true
    

Alternatively, you can explicitly enable tracing programmatically when building your client by using the `.with_tracing()` method on the client builder:
    
    
    use google_cloud_secretmanager_v1::client::SecretManagerService;
    
    let client = SecretManagerService::builder()
        .with_tracing()
        .build()
        .await?;
    

## Trace context propagation

The Rust client libraries automatically propagate active trace contexts to Google Cloud services, even if trace generation isn't explicitly enabled using `.with_tracing()`.

Use the `tracing-opentelemetry` or `opentelemetry` crates to provide a tracing context for the client libraries.

## Exporting telemetry

Once telemetry is enabled in the client libraries, your application must be configured to collect and export this data to your observability service. The Rust client libraries natively use the [tracing](https://crates.io/crates/tracing) ecosystem.

### Tracing

To export the `tracing` spans generated by the Google Cloud client libraries to OpenTelemetry, you must configure a `Subscriber` in your application that pipes data to an OpenTelemetry exporter (for example, OTLP).

Use the `tracing-opentelemetry` and `opentelemetry-otlp` crates to configure the exporter:
    
    
    use google_cloud_secretmanager_v1::client::SecretManagerService;
    use opentelemetry::trace::TracerProvider as _;
    use tracing_subscriber::Registry;
    use tracing_subscriber::layer::SubscriberExt;
    
    pub async fn sample() -> anyhow::Result<()> {
        let exporter = opentelemetry_otlp::SpanExporter::builder()
            .with_tonic()
            .build()?;
        let provider = opentelemetry_sdk::trace::SdkTracerProvider::builder()
            .with_batch_exporter(exporter)
            .build();
        let tracer = provider.tracer("example");
    
        // Create a tracing layer that sends data to an OpenTelemetry Collector running on localhost.
        let telemetry = tracing_opentelemetry::layer().with_tracer(tracer);
    
        // Register the subscriber globally
        let subscriber = Registry::default().with(telemetry);
        tracing::subscriber::set_global_default(subscriber)?;
    
        let _client = SecretManagerService::builder()
            .with_tracing()
            .build()
            .await?;
    
        Ok(())
    }

### Metrics

To export metrics, you must install a global OpenTelemetry `MeterProvider` in your application before initializing the client. The client libraries will automatically use it to record and export metric data.

For more details on collecting and exporting OpenTelemetry data to Cloud Monitoring or Cloud Trace, see [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach).

### Logging

The Rust client libraries use the `tracing` crate to emit actionable error logs at the `WARN` and `DEBUG` levels. The exported logs will include trace IDs and span IDs to ensure seamless correlation with your traces, provided you use an appropriate formatter.

To route these structured logs to Cloud Logging, configure a tracing subscriber to format events as JSON and output to standard output (`stdout`). If you are deploying to an environment like Google Kubernetes Engine or Cloud Run, the built-in agents automatically scrape these logs.

The following example configures a subscriber to capture and route only `WARN` level logs.
    
    
    use google_cloud_secretmanager_v1::client::SecretManagerService;
    use tracing_subscriber::layer::SubscriberExt;
    use tracing_subscriber::util::SubscriberInitExt;
    
    pub async fn sample() -> anyhow::Result<()> {
        // Enable all `WARN` logs to include failed client requests in all client libraries.
        let filter = tracing_subscriber::EnvFilter::new("warn");
    
        tracing_subscriber::registry()
            .with(filter)
            .with(tracing_subscriber::fmt::layer().json())
            .init();
    
        let _client = SecretManagerService::builder()
            .with_tracing()
            .build()
            .await?;
    
        Ok(())
    }

For detailed instructions on configuring the OpenTelemetry trace correlation data (like `logging.googleapis.com/trace`) in the JSON formatter, see [Overview of collector-based instrumentation samples](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/sample-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
