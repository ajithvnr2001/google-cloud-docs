---
url: https://docs.cloud.google.com/stackdriver/docs/opentelemetry/operators/
title: Observability for system operators \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:15.646800+00:00
---

# Observability for system operators  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/opentelemetry/operators/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Observability for system operators Stay organized with collections  Save and categorize content based on your preferences. 

As a system operator, you can configure telemetry collection across your deployment environments to observe the health and performance of your applications. This guide introduces the tools and services you can use to collect and ingest telemetry into Google Cloud Observability, including the Google-Built OpenTelemetry Collector, the Ops Agent, and Google Cloud Managed Service for Prometheus.

## Telemetry collection tools

  * [Google-Built OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel)

The Google-Built OpenTelemetry Collector is Google's open-source build of the [OpenTelemetry Collector](https://opentelemetry.io), built from upstream components using a secure supply chain on Google infrastructure. There are examples that show you how to deploy this collector for common configurations, such as Google Kubernetes Engine.

  * [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent)

The Ops Agent is the primary method of collecting telemetry from Compute Engine instances. The following documents provide information about specific configurations:

    * [Collect OTLP metrics and traces](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/otlp)
    * [Collect Prometheus metrics](https://docs.cloud.google.com/monitoring/agent/ops-agent/prometheus)
  * [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus)

Google Cloud Managed Service for Prometheus is Google Cloud's fully managed, multi-cloud, cross-project solution for [Prometheus](https://prometheus.io). This solution lets you globally monitor and alert on your workloads using Prometheus and OpenTelemetry without having to manually manage and operate Prometheus at scale.




## Send data to your project in OTLP format

Google Cloud Observability supports ingesting log, metric, and trace data in OTLP format. For information about the API, authentication methods, and data processing, see [OTLP support in Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs/otlp/overview).

You can migrate your existing collectors to send OTLP-formatted log, metric, and trace data to your project. For more information, see [Migrate collectors to use OTLP exporters](https://docs.cloud.google.com/stackdriver/docs/otlp/migrate-collector-to-otlp-exporters).

## Add observability without code changes

If you use the OpenTelemetry zero-code approach, then you can add observability without modifying your application's code. Instead, you attach a runtime agent and configure collection by using environment variables or system properties. For more information, see [Zero-code](https://opentelemetry.io/docs/concepts/instrumentation/zero-code/).

For an example, see [Use OpenTelemetry zero-code instrumentation for Java workloads on GKE](https://docs.cloud.google.com/stackdriver/docs/instrumentation/otel-zerocode-java-gke).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
