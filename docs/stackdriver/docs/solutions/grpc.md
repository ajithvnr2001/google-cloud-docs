---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/
title: Microservices observability overview \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:53.921508+00:00
---

# Microservices observability overview  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Reference ](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview)



Send feedback 

#  Microservices observability overview Stay organized with collections  Save and categorize content based on your preferences. 

Microservices observability tools provide you with the ability to instrument your applications to collect and present telemetry data in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview), [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview), and [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview) from [gRPC](https://grpc.io/) workloads deployed on Google Cloud and elsewhere.

This documentation is intended for gRPC service owners, site reliability engineers, and anyone who uses telemetry data for troubleshooting and optimizing gRPC workloads.

Observability wraps the [OpenCensus](https://opencensus.io/) plugins for metrics, traces, and gRPC logging into a single unified plugin, without exposing any dependencies. Microservices observability uses observability data that's integrated with Cloud Monitoring, Cloud Logging, and Cloud Trace. The documentation provides instructions for incorporating observability plugins into your gRPC applications.

To help you collect information and debug your applications, Microservices observability includes the following features:

  * Transport-level RPC events logging generation.
  * Distributed tracing support.
  * Cloud Monitoring support, including predefined dashboards.
  * Cloud Logging suggested queries.
  * Resource labels and custom labels.



## Features

This section describes Microservices observability features.

### Telemetry Integration

The observability plugin packages for each gRPC language (C++, Go, and Java) are integrated with Google Cloud Observability by default. With minimal configuration, the plugin retrieves metadata about your project and deployment, and configures the default quantities of tracing, metrics, and logging data generation.

### Inspect RPC transport-level events

The lifecycle of a remote procedure call (RPC) can contain metadata events, including headers and trailers; message events; and status events, including OK status and error status, and finishing events. When you use Microservices observability, you can inspect the details for each type of event. You can inspect serialized message length, authority, client/server addresses, and whether the client or the server canceled the RPC.

With explicit settings, Microservices observability can enable payload logging for messages or headers. You can set size limits for the payload logs, control message, or header payload logs separately. You can also specify the target group of methods with or without wildcards.

### Distributed tracing support for RPCs

Server architecture can allow an RPC to fan out into multiple calls or separate requests that flow through components. Microservices observability uses distributed tracing to make it easier to analyze and troubleshoot complex systems. The Microservices observability product provides built-in support for gRPC applications to start traces, generate [spans](https://opencensus.io/tracing/span/#span), and propagate the tracing context.

### Capture measurements for metrics monitoring

The plugin provides first-party support for a wide range of measures at message- level, RPC-level, or method-level, from message counts and message sizes to latencies. The measurements are uploaded to Cloud Monitoring. You can explore the collected metrics using the Cloud Monitoring [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer), which has a dashboard with a set of pre-existing charts. You can also present the metrics in your own custom dashboards.

### Traces and logs correlation

Traces help you identify errors and issues in your systems, while log entries help you identify the details of any errors and issues. Taken together, traces and logs provide you with an in-depth picture of the errors or issues, giving you a more complete understanding of RPCs that span different systems. Microservices observability automatically correlates logs with traces, which are sampled based on upstream sampling decisions or user-defined sampling rates.

### Resource labels and custom labels

To make it more effective for you to explore observability data, Microservices observability provides resource labels by default and allows your application to define custom labels. Resource labels are deployment-specific key-value pairs that annotate the location of the workload, for example, the Compute Engine node name or the Google Kubernetes Engine namespace.

Custom labels provide a mechanism for attaching customized information as follows:

  * As span labels to tracing data.
  * As metric labels to metrics data.
  * As log entry labels to logging data.



Custom labels are helpful when you want to include source versions or canonical service names. You can use them to add user-specific information, which helps to identify specific observability data in your logs, metrics, and traces.

### Suggested queries

Microservices observability automatically provides several suggested queries in Cloud Logging. For complete information, see [Suggested queries](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/set-up-observability#suggested-queries).

## Architecture

The following diagram illustrates how Microservices observability collects and serves observability data:

[ ![Microservices observability data collection and serving.](https://docs.cloud.google.com/static/stackdriver/docs/solutions/grpc/images/observability-flow.svg)](https://docs.cloud.google.com/static/stackdriver/docs/solutions/grpc/images/observability-flow.svg) Microservices observability data collection and serving (click to enlarge)

First, you specify observability configuration to your gRPC workload. The observability configuration consists of fields that you set in an environment variable. The configuration defines the following:

  * Trace spans that are exported to Cloud Trace.
  * Metrics data that is exported to Cloud Monitoring.
  * RPC events that are exported to Cloud Logging.



You can then view this information on custom dashboards in Cloud Monitoring and obtain suggested queries in Cloud Logging. You can also export information from Cloud Trace, Cloud Monitoring, and Cloud Logging to third-party platforms of your choice.

## Pricing

Microservices observability pricing is the same as Google Cloud Observability pricing. There are no separate charges for using Cloud Trace, Cloud Logging, and Cloud Monitoring with the Microservices observability plugins. For more information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).

## What's next

  * For information about setting up Microservices observability, see [Set up Microservices observability](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/set-up-observability).

  * For detailed information about configuration data, trace definitions, metrics definitions, and log definitions, see [Microservices observability reference](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/observability-reference).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
