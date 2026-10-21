---
url: https://docs.cloud.google.com/trace/docs/overview/
title: Cloud Trace overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:48.179803+00:00
---

# Cloud Trace overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Cloud Trace overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Trace is a distributed tracing system for Google Cloud that tracks request latency and helps you troubleshoot performance bottlenecks across services and generative AI applications. By collecting latency data from Google Cloud services and instrumented applications, Trace helps you understand how requests are processed in a microservices architecture and identify relevant logs.

With Trace, you can measure end-to-end request latency, compare performance trends over time, and pinpoint which downstream dependencies cause delays. For a walkthrough of correlating traces and logs, see [Using traces and logs together for root-cause analysis](https://cloud.google.com/blog/products/devops-sre/using-cloud-trace-and-cloud-logging-for-root-cause-analysis).

## Environment support

Trace runs on Linux in the following environments:

  * [Compute Engine](https://docs.cloud.google.com/compute/docs)
  * [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-distributed-trace) (Public Preview)
  * [App Engine flexible environment](https://docs.cloud.google.com/appengine/docs/flexible)
  * [App Engine standard environment](https://docs.cloud.google.com/appengine/docs/standard)
  * [Cloud Run](https://docs.cloud.google.com/run/docs/trace)
  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/observability/accessing-traces)
  * [Cloud SQL query insights](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights)
  * Non-Google Cloud environments



## Components

Trace consists of a tracing client, which collects _traces_ and sends them to your Google Cloud project. You can then use the Google Cloud console to view and analyze the data collected by the tracing client. For information about the data model, see [Traces and spans](https://docs.cloud.google.com/trace/docs/traces-and-spans).

### Tracing client

A tracing client collects latency and span data from your application and exports it to your Google Cloud project. Depending on your environment and requirements, you can collect trace data automatically or manually by instrumenting your application code.

### Tracing interface

To view and analyze your span data, you can use the **Trace Explorer** and **Observability Analytics** pages in the Google Cloud console:

  * **Trace Explorer** : Displays aggregate information about your trace data and lets you examine individual traces in detail. The aggregated latency data is shown on a heatmap, which you can explore with your pointer. To restrict which data is displayed, you can add filters. You can also view and explore individual spans and traces:

    * For information about how to view trace data stored in multiple projects, see [Create and manage trace scope](https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage).
    * For information about filtering and viewing your trace data, see [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces).
  * **Observability Analytics** : Provides a SQL query interface. Your queries can join your trace and log data, and you can view the query results either as a table or a chart. You can use [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) to analyze your trace data if you create a linked BigQuery dataset. For more information, see [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics).




## Configurations with automatic tracing

The following configurations automatically capture trace data:

  * App Engine standard environment

    * First-generation runtimes automatically intercept and send trace spans to Cloud Trace. For more information, see [Overview of legacy bundled services](https://docs.cloud.google.com/appengine/docs/standard/bundled-services-overview).

    * Second-generation runtimes automatically capture overall request latency and add the `X-Cloud-Trace-Context` HTTP header to requests. For more information, see [Runtime support schedule](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule).

  * Cloud Run functions and Cloud Run

For incoming and outgoing HTTP requests, latency data is automatically sent to Trace.




## Instrument your application

Instrument your application to collect specific information that helps you understand its performance and troubleshoot failures. Several open-source instrumentation frameworks collect log, metric, and trace data, and can send that data to any vendor, including Google Cloud. For your agentic applications, some frameworks can collect your prompts and responses or pass context that allows tracing of some remote [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview) calls.

To instrument your application, we recommend that you use an open-source, vendor-neutral instrumentation framework, such as [OpenTelemetry](https://opentelemetry.io/), instead of vendor- and product-specific APIs or client libraries. For information about these frameworks, see [ Instrumentation and observability](https://docs.cloud.google.com/stackdriver/docs/instrumentation/overview) and [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach).

The instrumentation samples we provide use [OpenTelemetry](https://opentelemetry.io):

  * For samples that use a collector-based export, see the following:

    * [Go](https://docs.cloud.google.com/trace/docs/setup/go)
    * [Java](https://docs.cloud.google.com/trace/docs/setup/java)
    * [Node.js](https://docs.cloud.google.com/trace/docs/setup/nodejs)
    * [Python](https://docs.cloud.google.com/trace/docs/setup/python)

These samples send metric and trace data that follows the [OpenTelemetry Protocol](https://opentelemetry.io/docs/specs/otlp) (OTLP) format to your project by using the Telemetry API. The samples use a Google Cloud exporter for log data.

  * For information about how to use a direct export of trace data and send that data to the Telemetry API, see [Migrate from the Trace exporter to the OTLP endpoint](https://docs.cloud.google.com/trace/docs/migrate-to-otlp-endpoints).

  * For samples that show you how to configure an agentic application to collect prompts and responses, see [How to instrument your generative AI applications](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-overview#how).



  * For information about Google Cloud MCP servers that can generate trace spans, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/trace/docs/trace-remote-mcp-server-calls).



Although you can use Cloud Trace client libraries to instrument your application, we recommend that you use [OpenTelemetry](https://opentelemetry.io). OpenTelemetry libraries are preferable to Trace client libraries because they are simpler and export trace data in OTLP format, which OpenTelemetry defines. For more information, see [Instrument for Trace](https://docs.cloud.google.com/trace/docs/setup) and [Client libraries for Cloud Trace](https://docs.cloud.google.com/trace/docs/client-libraries).

## Cloud Trace and agentic applications

To understand the behavior of your agentic applications, configure them to collect prompts and responses or to generate spans when they call remote [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview). Prompts and responses help you understand the reasoning your agentic application uses. Spans that record tool calls help you confirm tool invocation, call statuses, and request latencies.

Several instrumentation samples show you how to configure an application to collect prompts and responses. These samples rely on [OpenTelemetry](https://opentelemetry.io). For more information, see [How to instrument your generative AI applications](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-overview#how).

Google Cloud MCP servers can generate trace spans. For more information, see [Investigate MCP calls using Trace](https://docs.cloud.google.com/trace/docs/trace-remote-mcp-server-calls).

## APIs that ingest trace data

You can send trace data to your project by using either the Telemetry API or the Cloud Trace API. We recommend the Telemetry API for the following reasons:

  * The API provides compatibility with the open source OpenTelemetry ecosystem, and [its limits](https://docs.cloud.google.com/trace/docs/quotas#telemetry-api-limits) are often more generous than the limits of the Cloud Trace API, which is a proprietary Google Cloud API.

  * Your trace data is stored in a format that is generally consistent with the proto files defined by [OTLP](https://opentelemetry.io/docs/specs/otlp). Some fields might be converted from an OpenTelemetry-specific data type to a JSON data type before storage. For information about the storage format, see [Schema for trace data](https://docs.cloud.google.com/trace/docs/reference/trace-schema).

  * For collector-based export of trace data, your instrumentation doesn't rely on a Google Cloud-specific exporter.

  * Some features, like Application Monitoring, rely on information that is available only when you send trace data to the Telemetry API.




To prevent your Google Cloud project from storing trace data, disable the Cloud Trace API. Disabling the Cloud Trace API has the following effects:

  * Google Cloud services don't send trace data to your project.
  * Google Cloud replies to requests sent to a Cloud Trace API endpoint with an error code.
  * Google Cloud Observability discards trace data sent to the trace-specific Telemetry API endpoint. Don't disable the Telemetry API, as that API can receive log, metric, and trace data.



If you manage an organization and want to prevent usage of Cloud Trace, then create an [organization policy constraint](https://docs.cloud.google.com/organization-policy/overview#constraints).

## VPC Service Controls support

Google Cloud services and your applications can send trace data to your project by using either the Cloud Trace API or the Telemetry API. Visualization services provided by Cloud Trace use the Cloud Trace API to fetch the trace data that they display:

  * Cloud Trace is a VPC Service Controls-supported service. The Trace service name is `cloudtrace.googleapis.com`. For details and limitations, see [Supported products: Cloud Trace](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_trace).

  * The Telemetry API is a VPC Service Controls-supported service. The service name is `telemetry.googleapis.com`. For details and limitations, see [Supported products: Telemetry API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_telemetry).




To [set defaults](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets) that specify the Google Cloud region where your trace data is stored and whether a customer-managed key encrypts the data, use the Observability API. You also use this API to configure [linked BigQuery datasets](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset), which let you query your trace data using BigQuery services, and to configure [trace scopes](https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage), which let you aggregate trace data stored in multiple projects.

  * The Observability API is a VPC Service Controls-supported service. The service name is `observability.googleapis.com`. For details and limitations, see [Supported products: Observability API](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_observability_api).



For more information, see the following:

  * [VPC Service Controls documentation](https://docs.cloud.google.com/vpc-service-controls/docs).
  * [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).



## Cloud Trace and data residency

If you are using [Assured Workloads](https://cloud.google.com/security/products/assured-workloads) because you have data-residency or [Impact Level 4 (IL4)](https://cloud.google.com/security/compliance/disa) requirements, then don't use the Cloud Trace API to send trace spans.

To prevent your Google Cloud project from storing trace data, disable the Cloud Trace API. Don't disable the Telemetry API, as that API can receive log, metric, and trace data.

## Trace retention

Category | Retention period  
---|---  
Spans stored in the [`_Trace` bucket](https://docs.cloud.google.com/trace/docs/storage-overview) | 30 days  
  
## IAM roles

Cloud Trace uses Identity and Access Management (IAM) to control access to resources. For a list of Cloud Trace API and Telemetry API roles, see [Control access with IAM](https://docs.cloud.google.com/trace/docs/iam).

Because the Telemetry API is a consumer API, sending data to the Telemetry API requires that you specify a quota project and grant the application's service account permission to use that quota. For more information, see [Telemetry API: Authentication](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview#auth).

## Pricing

To learn about pricing for Cloud Trace, see the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

## What's next

  * Try the [Quickstart](https://docs.cloud.google.com/trace/docs/trace-app-latency).

  * For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/trace/docs/quotas).

  * Read our resources about [DevOps](https://cloud.google.com/devops) and explore the [DevOps Research and Assessment](https://dora.dev/) research program.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
