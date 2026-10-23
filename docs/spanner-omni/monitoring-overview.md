---
url: https://docs.cloud.google.com/spanner-omni/monitoring-overview/
title: Monitoring overview \u00a0|\u00a0 Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:23.594862+00:00
---

# Monitoring overview  |  Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/monitoring-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Monitoring overview Stay organized with collections  Save and categorize content based on your preferences. 

Monitoring in Spanner Omni works similarly to monitoring in Spanner, with some exceptions. This document provides explanations of those exceptions and points you to related information in Spanner monitoring documentation. As you read the Spanner documentation, refer back to this page to confirm how Spanner Omni differs.

## Spanner features that aren't supported

Spanner Omni supports all Spanner monitoring features except [end-to-end tracing](https://docs.cloud.google.com/spanner/docs/tracing-overview#end-to-end-side-tracing).

## Capture telemetry signals

To gain insights into performance, usage, and potential issues, you can capture signals from your Spanner Omni database.

### Signal capture overview

Telemetry signals help you understand how your database is performing.

The following signals are available for Spanner Omni:

Signal type | Description  
---|---  
Metrics | Numeric data about database health or performance.  
Logs | Generated records of system activity over time.  
Traces | Request paths through your application.  
Statistics tables | Built-in tables for querying database information.  
  
In Spanner Omni, client-side metrics aren't supported. Client-side metrics include latencies for GFE metrics, client-side metric collection, and custom client-side metric collection. For more information, see [Signal capture overview](https://docs.cloud.google.com/spanner/docs/signal-capture-overview) in the Spanner documentation.

### Trace collection

Traces represent the path of a request through your application. They let you follow the flow of a request and help you identify the root cause of an issue. For example, tracing can provide information for every request from a client, such as spans with timestamps of when the client sent and received RPC requests. This helps you monitor and debug database requests.

For more information, see [Trace collection overview](https://docs.cloud.google.com/spanner/docs/tracing-overview) in the Spanner documentation.

#### Set up trace collection using OpenTelemetry

You can configure Spanner client libraries to export traces using [OpenTelemetry](https://opentelemetry.io/) APIs. This process involves configuring the OpenTelemetry SDK and using an exporter to send trace data to an observability backend.

Client-side tracing isn't available for Spanner Omni.

For more information, see [Set up trace collection using OpenTelemetry](https://docs.cloud.google.com/spanner/docs/set-up-tracing) in the Spanner documentation.

### Audit logs

Audit logs track administrative changes and data access events for security and compliance. You can use audit logs to monitor request latencies by referring to the processing duration fields. For more information, see [Audit logs](https://docs.cloud.google.com/spanner-omni/audit-logs).

## Monitor instances

Monitor your instances to ensure they are performing as expected and to help you troubleshoot potential issues.

### Monitor instance performance using insights

The system insights dashboard provides charts and metrics for latency, CPU utilization, storage, throughput, and other performance statistics. You can use this dashboard to monitor Spanner Omni instances and databases. For more information, see [Monitor instances with system insights](https://docs.cloud.google.com/spanner/docs/monitoring-console) in the Spanner documentation.

## What's next

  * [Use Grafana dashboards to monitor Spanner Omni](https://docs.cloud.google.com/spanner-omni/grafana-dashboards).

  * [Use Prometheus alerts to monitor Spanner Omni](https://docs.cloud.google.com/spanner-omni/prometheus-alerts).

  * [Learn about audit logging in Spanner Omni](https://docs.cloud.google.com/spanner-omni/audit-logs).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
