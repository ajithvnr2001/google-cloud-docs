---
url: https://docs.cloud.google.com/stackdriver/
title: Observability in Google Cloud \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:48:02.761531+00:00
---

# Observability in Google Cloud  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Observability in Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Observability includes observability services that help you understand the behavior, health, and performance of your applications, including agentic applications. Understanding how applications behave and how components connect helps you anticipate, identify, and respond to unexpected changes quickly and effectively.

This document includes the following information:

  * Definitions of terms such as observability, agent observability, and application observability and APM.
  * The benefits of observability services for developing and maintaining reliable applications.
  * How Google Cloud Observability helps you monitor and maintain application and infrastructure health.
  * Steps to get started with observability in Google Cloud.



## Observability

_Observability_ is a comprehensive approach to collecting and analyzing _telemetry data_ to help you understand the state of your applications, including agentic applications, and their operating environment. Telemetry data includes log data, metric data, and trace data. It can also include other data that your applications generate, such as prompts and responses. Telemetry data provides the information you need to understand the health and performance of your applications.

Metric data
    Metric data is numeric data about health or performance that the system measures at regular intervals—for example, CPU utilization and request latency. Unexpected changes to metric data might indicate an issue that you need to investigate. Over time, you can also analyze patterns to understand usage patterns and anticipate resource needs.
Log data
    

A log is a generated record of system or application activity over time. Each log is a collection of timestamped log entries, and each log entry describes a specific event.

Log data often contains rich, detailed information that helps you understand what occurred in a specific part of your application. However, log data doesn't effectively show how a change in one application component relates to activity in other components. Trace data can bridge this gap.

Trace data
    

A _trace_ represents the path of a request across the components of your distributed application. That is, each trace represents a single end-to-end operation. Because traces are composed of _spans_ , which are records for a single function or operation, they let you follow the flow of requests and examine latency data. This information can help you identify the root cause of an issue.

For agentic applications, traces capture the actions that your agent performs. For example, a trace can capture MCP calls.

Other data
    

You can gain additional insights by analyzing log data, metric data, and trace data along with other relevant information. For example, a label that indicates the severity of an alert or a customer ID in log data provides context that is useful for troubleshooting and debugging.

## Agent observability

_Agent observability_ refers to methods to understand the internal state and behavior of software agents, especially AI-powered agents built using Large Language Models (LLMs). AI agents are non-deterministic and complex. Therefore, observability is crucial to understand, debug, evaluate, and improve their performance, safety, and reliability.

Google Cloud provides support for application observability with [Application Monitoring](https://docs.cloud.google.com/stackdriver/docs/observability/about-application-monitoring), which creates dashboards that display telemetry data, AI resource metric data, and information such as open alerts. To learn more, see the Agent and application observability in Google Cloud section of this document.

## Application observability and APM

_Application Performance Monitoring (APM)_ monitors, diagnoses, and manages the performance, availability, and user experience of software applications, including agentic applications. An APM system typically provides dashboards that display telemetry data and services that monitor telemetry data. These systems help you identify failures.

_Application observability_ uses telemetry data to generate insights that help you understand the behavior of your applications.

Google Cloud provides support for application observability with [Application Monitoring](https://docs.cloud.google.com/stackdriver/docs/observability/about-application-monitoring), which creates dashboards that display telemetry data, AI resource metric data, and information such as open alerts. To learn more, see the Agent and application observability in Google Cloud section of this document.

## Observability services

_Observability services_ collect, analyze, and correlate telemetry data, such as log data, metric data, and trace data. They provide the following capabilities to help you maintain application reliability:

  * Proactively detect issues before they affect users.
  * Troubleshoot both known and new issues.
  * Debug applications during development.
  * Understand the impact of changes to your applications.
  * Discover new insights through data exploration.



To learn more about reliability practices, including principles and practices related to observability, read the book [Site Reliability Engineering: How Google Runs Production Systems](https://sre.google/books/). Topics include [Monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/), [Alerting](https://sre.google/sre-book/practical-alerting/), and [Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/).

## Google Cloud Observability

Services in Google Cloud Observability help you collect, analyze, and correlate telemetry data, from both your applications and the underlying infrastructure. These services also provide built-in defaults to help you get started. For example, [Application Monitoring](https://docs.cloud.google.com/stackdriver/docs/observability/about-application-monitoring) creates dashboards and topology maps for your [App Hub](https://docs.cloud.google.com/app-hub/docs/overview)-registered applications, services, and workloads.

### Automatic collection of telemetry data

[Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview), [Logging](https://docs.cloud.google.com/logging/docs/overview), and [Trace](https://docs.cloud.google.com/trace/docs/overview) are services that are enabled by default when you create a Google Cloud project. These services provide the core capabilities to collect, analyze, and visualize your telemetry data:

  * Automatically collect telemetry data for most Google Cloud services.
  * Automatically collect [audit logs](https://docs.cloud.google.com/logging/docs/audit) for most Google Cloud services.
  * Provide visualization services, including dashboards and telemetry explorers, that let you view and examine your telemetry data. For example, the [Trace explorer](https://docs.cloud.google.com/trace/docs/overview) lets you view traces, spans, and metadata, including multimodal prompts and responses. For more information, see [Query and view telemetry data](https://docs.cloud.google.com/stackdriver/docs/observability/query-and-view-overview).
  * Provide [SQL-based analysis services](https://docs.cloud.google.com/logging/docs/log-analytics#analytics) for your log data and trace data. For example, you can use BigQuery to compare URLs in your log data with a public dataset of known malicious URLs.
  * Provide application monitoring and telemetry monitoring. For example, you can create alerting policies that notify you when your log data or metric data meets conditions that you specify. You can also use [synthetic monitoring](https://docs.cloud.google.com/monitoring/uptime-checks/introduction) to test the performance of your applications.
  * Collect telemetry data from your instrumented applications. _Instrumentation_ is code that you add to an application to emit telemetry data.

To instrument your application, we recommend that you use an open-source, vendor-neutral instrumentation framework, such as [OpenTelemetry](https://opentelemetry.io/), instead of vendor- and product-specific APIs or client libraries. For information about these frameworks, see [ Instrumentation and observability](https://docs.cloud.google.com/stackdriver/docs/instrumentation/overview) and [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach).




### Agent and application observability

[Application Monitoring](https://docs.cloud.google.com/stackdriver/docs/observability/about-application-monitoring) in Google Cloud provides both agent observability and application observability. This service provides dashboards and topology maps that let you understand the health and performance of your [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) applications, services, and workloads. It also generates and displays metrics such as error rates and token usage for AI resources. To generate these metrics, Application Monitoring filters and aggregates your trace data using application-specific labels and events that follow the [OpenTelemetry GenAI semantic conventions](https://github.com/open-telemetry/semantic-conventions/tree/v1.37.0/docs/gen-ai).

For agent observability, we recommend building your agents with the [Agent Development Kit (ADK) framework](https://google.github.io/adk-docs/). Because ADK relies on [OpenTelemetry](https://opentelemetry.io/blog/2025/ai-agent-observability/), the telemetry ADK generates is consistent with the OpenTelemetry GenAI semantic conventions.

To debug failures, monitor costs, or analyze agent behavior—including from Gemini Enterprise Agent Platform, Agent Gateway, and Model Armor agents—you need log, metric, and trace data:

  * Logs provide information about events and errors.
  * Metrics lets you monitor your latency and token usage.
  * Traces provide information about execution paths, and are analyzed to derive metrics such as the number of model calls or total token usage. These derived metrics provide visibility into agent performance and behavior. For more information, see [View AI resources](https://docs.cloud.google.com/monitoring/docs/application-monitoring-ai-resources).
  * Prompt and response data lets you assess agent quality and decision-making using the Gen AI evaluation service.



The Application Monitoring dashboard for an application displays a list of the application's services and workloads, such as [Gemini Enterprise apps](https://docs.cloud.google.com/gemini/enterprise/docs/concepts), [Gemini Enterprise Agent Platform agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents) and MCP servers:

![An overview that lists the services and workloads in an application.](https://docs.cloud.google.com/static/stackdriver/images/aco-app-overview-tab.png)

You can identify agentic services and workloads by using the infrastructure type or the [App Hub functional type](https://docs.cloud.google.com/app-hub/docs/overview#properties-and-attributes). The functional type column is hidden by default.

For code samples, see the following:

  * [Instrument generative AI applications](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-overview).
  * [Collect and view multimodal prompts and responses](https://docs.cloud.google.com/stackdriver/docs/instrumentation/collect-view-multimodal-prompts-responses).



### Support for identifying errors

[Error Reporting](https://docs.cloud.google.com/error-reporting/docs) analyzes log entries from Cloud Logging to find errors. When [Error Reporting](https://docs.cloud.google.com/error-reporting/docs) finds errors, it annotates the associated log entries and creates an error group. Explore these error groups to identify the cause and history of the error.

### Profiling support

[Cloud Profiler](https://docs.cloud.google.com/profiler/docs/about-profiler) lets you analyze CPU and memory usage for your applications to identify opportunities to improve performance.

## Get started

This section describes steps you can take to become familiar with observability features in Google Cloud.

### Try the quickstarts

Try the quickstarts to become familiar with the available services.

  * [Logging](https://docs.cloud.google.com/logging/docs/logging-gce-quickstart)
  * [Monitoring](https://docs.cloud.google.com/monitoring/monitor-compute-engine-virtual-machine)
  * [Trace](https://docs.cloud.google.com/trace/docs/trace-app-latency)
  * [Error Reporting](https://docs.cloud.google.com/error-reporting/docs/check-app-crash)
  * [Profiler](https://docs.cloud.google.com/profiler/docs/measure-app-performance)



### View automatically collected data

Most Google Cloud services automatically generate log data and metric data. This means that you can start viewing some observability data for supported Google Cloud services without additional configuration.

  * Some Google Cloud services such as [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics), [Compute Engine](https://docs.cloud.google.com/compute/docs/instances/observe-monitor-vms), and [Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance) provide default dashboards in the Google Cloud console to view observability data in the context of the service.
  * Compute Engine, GKE, and Cloud Run generate system metric data and log data by default. You configure the collection of additional data. 
    * Compute Engine
    * GKE
    * Cloud Run
  * Cloud Run functions and App Engine automatically generate metric data, log data, and trace data.



You can also chart collected metric data in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer), view log data in [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), or view trace data in [Trace](https://docs.cloud.google.com/trace/docs/overview). To review related data together, create [custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards). For example, you can create a dashboard that includes log data, performance metric data, and alerting policies for virtual machines.

### Configure Compute Engine VMs to collect additional data

By default, Compute Engine VMs collect only basic system metric data and log data. However, you can [install the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-index) to collect additional telemetry data from your Compute Engine instances and applications for troubleshooting, performance monitoring, and alerting. The Ops Agent is not an agentic application. Instead, it is a deterministic piece of software that collects telemetry data.

  * Automatically collect host metric data, such as CPU, GPU, memory, and process metric data.
  * Automatically collect system log data, such as syslog from Linux VMs and Windows Event Log from Windows VMs.
  * You can observe your applications with the following: 
    * [Third-party application integrations](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party) for popular software, such as Postgres, MongoDB, and Java Virtual Machine. These integrations include pre-configured dashboards and alert policies.
    * [Prometheus metric data](https://docs.cloud.google.com/monitoring/agent/ops-agent/prometheus)
    * [OpenTelemetry Protocol (OTLP) metric data and trace data](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/otlp)
    * [Application log data](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration#logging-receivers)
  * For a summary of the collected telemetry data, see the [Ops Agent overview](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent).



### Configure GKE clusters to collect additional data

By default, GKE clusters send system log data and system metric data to Logging and Monitoring. [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) handles the collection of third-party metric data and user-defined metric data.

  * Use [observability metric data packages](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-metrics) to understand the state of your applications and cluster resources. For example, control plane metric data is useful for creating SLOs to monitor service availability and latency.
  * [Monitor third-party applications](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/introduction) such as Postgres, MongoDB, and Redis. These integrations provide pre-configured dashboards and alert policies.



### Configure Cloud Run to collect custom data

If you have a Cloud Run service that writes [Prometheus metric data](https://prometheus.io/docs/concepts/metric_types/), then you can use the [Prometheus sidecar](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cloudrun-sidecar) to send the metric data to Cloud Monitoring.

If your Cloud Run service writes [OTLP metric data](https://opentelemetry.io/docs/concepts/signals/metrics/) instead, then you can use an OpenTelemetry sidecar. For an example, see the [tutorial for collecting OTLP metric data](https://docs.cloud.google.com/run/docs/tutorials/custom-metrics-opentelemetry-sidecar) using the sidecar.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
