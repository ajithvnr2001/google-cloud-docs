---
url: https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach/
title: Choose an instrumentation approach \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:43.695394+00:00
---

# Choose an instrumentation approach  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Choose an instrumentation approach Stay organized with collections  Save and categorize content based on your preferences. 

You can choose the most effective instrumentation approach for your application based on your Google Cloud compute platform and telemetry requirements. This guide provides recommendations for Google Kubernetes Engine (GKE), Compute Engine, and Cloud Run, helping you decide between the Google-Built OpenTelemetry Collector, the Ops Agent, and direct in-process OpenTelemetry export.

This document provides general recommendations, as well as guidance for the following platforms:

  * GKE
  * Compute Engine
  * Cloud Run
  * Cloud Run functions
  * App Engine



For sample applications, see Samples and implementation guides.

The recommendations on this page aren't the only solutions, and other approaches can work. For additional guidance, contact [Cloud Customer Care](https://docs.cloud.google.com/support).

## General recommendations

This section contains general recommendations about how to instrument your application. For platform-specific guidance, see Platform recommendations.

  * Log data: We recommend that you use a framework that can be configured to output [JSON-structured logs for Cloud Logging](https://docs.cloud.google.com/logging/docs/structured-logging). For writing log data, we recommend the following:

    * Go: [`slog`](https://pkg.go.dev/log/slog).
    * Python: [`logging`](https://docs.python.org/3/library/logging.html).
    * JavaScript: [Pino](https://getpino.io/).
    * Java: [SLF4J](https://www.slf4j.org/) with [Log4j2](https://logging.apache.org/log4j/2.x/).
  * Metric data: We recommend that you use [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry) or [Prometheus client libraries](https://prometheus.io/docs/instrumenting/clientlibs/):

    * OpenTelemetry provides a vendor-neutral, open-source framework and client libraries to instrument applications for metrics.
    * Prometheus client libraries ([Go, Java, Python, etc.](https://prometheus.io/docs/instrumenting/clientlibs/)) generate metrics that can be exposed at an HTTP endpoint and scraped by an agent.
  * Trace data: We recommend that you use [OpenTelemetry](https://opentelemetry.io/docs/what-is-opentelemetry) to generate distributed trace data from your application code.




## OpenTelemetry collection architectures

When you instrument an application with OpenTelemetry libraries, you can route telemetry through the standalone [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) or export directly from your application process. The [OpenTelemetry Collector configuration file](https://opentelemetry.io/docs/collector/configuration/) controls how the collector receives, processes, and exports telemetry. In general, we recommend that collectors receive and export telemetry by using the [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/). The Telemetry (OTLP) API implements this protocol.

There are two fundamental approaches for sending telemetry to your Google Cloud project:

  * **Collector-based export (vendor-neutral):** You instrument your application code with the OpenTelemetry SDK and use the in-process OTLP exporter to send data to an OpenTelemetry collector, such as the Google-Built OpenTelemetry Collector or an Ops Agent receiver. The collector receives the telemetry and forwards it to your Google Cloud project. Your application code remains completely vendor-neutral.

  * **Direct export (vendor-specific):** You instrument your application code with the OpenTelemetry SDK and configure OpenTelemetry to send telemetry to your project by using the Telemetry API. You don't need to deploy a collector, but your application code includes vendor-specific dependencies.




We recommend that you use an OpenTelemetry collector when your compute environment supports one. For environments where running a separate collector process isn't practical, use direct in-process export.

## Platform recommendations

Because Google Cloud compute environments have different lifecycle and sidecar capabilities, the optimal collection pattern varies by platform. The following sections provide specific recommendations for your deployment environment.

### GKE

For general information about GKE, see [GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview).

Type | Recommendation  
---|---  
Metrics | We recommend that you use Google Cloud Managed Service for Prometheus. For instrumentation, do one of the following:

  * Use [ Prometheus client libraries](https://prometheus.io/docs/instrumenting/clientlibs/). If you use this approach, then we also recommend that you use [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed), which includes [copy-and-paste exporter installation instructions](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/introduction) for common applications.
  * Use OpenTelemetry libraries and the OpenTelemetry Collector: 
    1. [Deploy the Google-Built OpenTelemetry Collector on Google Kubernetes Engine.](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-gke)
    2. Use the OpenTelemetry SDK and the OTLP exporter for your language.
The collector receives metric data from the SDK's in-process OTLP exporter, processes that data, and then exports it. Make sure that you configure the collector to export metric data to Managed Service for Prometheus. For more information, see [Get started with the OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-gke).

  
Traces | Do the following:

  1. [Deploy the Google-Built OpenTelemetry Collector on Google Kubernetes Engine.](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-gke) The collector receives trace data from the SDK's in-process OTLP exporter, processes that data, and then sends the processed data to your Google Cloud project by using the Telemetry (OTLP) API.
  2. Use the OpenTelemetry SDK and the OTLP exporter for your language.

  
Logs | Configure your app to output JSON-structured logs to `stdout` and `stderr`. For a list of frameworks, see Recommended logging frameworks. GKE collects logs written to `stdout` and `stderr` automatically. For more information, see [About GKE logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs).  
  
### Compute Engine

For general information about Compute Engine, see [Virtual machine instances](https://docs.cloud.google.com/compute/docs/instances).

Type | Recommendation  
---|---  
Metrics and Traces | Do the following:

  1. Use the Ops Agent to collect metrics and traces. For an example, see [Collect OpenTelemetry Protocol (OTLP) metrics and traces](https://docs.cloud.google.com/monitoring/agent/ops-agent/otlp). This guide describes how to configure the Ops Agent to receive metric and trace data from the SDK's in-process OTLP exporters, transform that data, and then send the data to your Google Cloud project. Metric data is sent by using the Cloud Monitoring API and trace data is sent by using the Cloud Trace API.
  2. Use the OpenTelemetry SDK and the OTLP exporter for your language.

Alternatively, if you only want to configure collection for Prometheus-format metrics, then use the [Ops Agent Prometheus receiver](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/prometheus) to collect metrics instrumented by using [ Prometheus client libraries](https://prometheus.io/docs/instrumenting/clientlibs/) or the OpenTelemetry SDK.  
Logs | Do the following:

  1. Configure your app to output JSON-structured logs to a file. For a list of frameworks, see Recommended logging frameworks.
  2. Install the Ops Agent and configure a receiver. For an example, see [Logging receivers](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#logging-receivers).

  
  
### Cloud Run

For general information about Cloud Run, see [What is Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run).

Type | Recommendation  
---|---  
Metrics and Traces | Do the following:

  1. Use the OpenTelemetry SDK and the OTLP exporter for your language.
  2. Deploy an OpenTelemetry sidecar to collect metrics and traces. For examples, see the following documents:
     * [Write OTLP metrics by using an OpenTelemetry sidecar](https://docs.cloud.google.com/run/docs/tutorials/custom-metrics-opentelemetry-sidecar).
     * [Deploy the Google-Built OpenTelemetry Collector on Cloud Run.](https://docs.cloud.google.com/stackdriver/docs/instrumentation/opentelemetry-collector-cloud-run) The collector receives log, metric, and trace data from the SDK's in-process OTLP exporters and then transforms the received data. Next, it exports metric data by using the `googlemanagedprometheus` exporter, and it exports log and metric data by using Google Cloud exporters.
  3. For your Cloud Run service, use instance-based billing. With instance-based billing, the CPU is allocated for the entire instance lifecycle, which is necessary because OpenTelemetry instrumentation does background processing. For more information, see [Billing settings for Cloud Run services](https://docs.cloud.google.com/run/docs/configuring/billing-settings). 

Alternatively, if you only want to configure collection for Prometheus-format metrics, then use the [Prometheus sidecar for Cloud Run](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cloudrun-sidecar) to collect metrics instrumented by using [ Prometheus client libraries](https://prometheus.io/docs/instrumenting/clientlibs/) or the OpenTelemetry SDK.  
Logs | Configure your app to output JSON-structured logs to `stdout` and `stderr`. For a list of frameworks, see Recommended logging frameworks. Cloud Run collects logs written to `stdout` and `stderr` automatically. For more information, see [Write container logs](https://docs.cloud.google.com/run/docs/logging#container-logs).  
  
### Cloud Run functions

For general information about Cloud Run functions, see [Cloud Run functions overview](https://docs.cloud.google.com/functions/docs/concepts/overview).

Type | Recommendation  
---|---  
Metrics | Writing metric data directly isn't supported in Cloud Run functions. You can generate [log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics).   
Traces | Use the OpenTelemetry SDK and the OTLP exporter for your language.  
Logs | Configure your app to output JSON-structured logs to `stdout` and `stderr`. For a list of frameworks, see Recommended logging frameworks. Cloud Run functions collects logs written to `stdout` and `stderr` automatically. For more information, see [Cloud Run functions: Monitoring and logging overview](https://docs.cloud.google.com/functions/docs/monitoring/logging).  
  
### App Engine

For general information about App Engine, see [An overview of App Engine](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine).

Type | Recommendation  
---|---  
Metrics | Use the OpenTelemetry SDK and the OTLP exporter for your language.  
Traces | Use the OpenTelemetry SDK and the OTLP exporter for your language.  
Logs | Configure your app to output JSON-structured logs to `stdout` and `stderr`. For a list of frameworks, see Recommended logging frameworks. App Engine collects logs written to `stdout` and `stderr` automatically. For more information, see [Write and view logs](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs).  
  
## Samples and implementation guides

  * [Sample overview](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/sample-overview) describes the architecture and required Identity and Access Management roles for the following collector-based code samples:

    * [Go](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/go)
    * [Java](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/java)
    * [Node.js](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/nodejs)
    * [Python](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/python)
  * [Migrate from the Trace exporter to the OTLP endpoint](https://docs.cloud.google.com/stackdriver/docs/instrumentation/migrate-to-otlp-endpoints) describes how to update an application that uses direct export to send OTLP-formatted trace data.

  * [Observability for AI agent developers](https://docs.cloud.google.com/stackdriver/docs/opentelemetry/ai-agent-developers) describes how to instrument or enable generative AI agents built with LangGraph or the Agent Development Kit (ADK) framework.




## OpenTelemetry documentation

This section provides links to the OpenTelemetry SDK and the OTLP exporters in different languages.

General references:

  * [Language APIs and SDKs](https://opentelemetry.io/docs/languages/)
  * [OTLP exporter](https://opentelemetry.io/docs/specs/otel/protocol/exporter/)



### Go

  * [Go SDK](https://opentelemetry.io/docs/languages/go/)
  * [Go OTLP exporter](https://opentelemetry.io/docs/languages/go/exporters/#otlp)



### Java

  * [Java SDK](https://opentelemetry.io/docs/languages/java/)
  * [Java OTLP exporter](https://opentelemetry.io/docs/languages/java/configuration/#properties-exporters)



### JavaScript

  * [JavaScript SDK](https://opentelemetry.io/docs/languages/js/)
  * [JavaScript OTLP exporter](https://opentelemetry.io/docs/languages/js/exporters/#otlp)



### Python

  * [Python SDK](https://opentelemetry.io/docs/languages/python/)
  * [Python OTLP exporter](https://opentelemetry.io/docs/languages/python/exporters/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
