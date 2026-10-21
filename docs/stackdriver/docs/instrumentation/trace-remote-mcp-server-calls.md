---
url: https://docs.cloud.google.com/stackdriver/docs/instrumentation/trace-remote-mcp-server-calls/
title: Investigate MCP calls using Trace \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:49.020990+00:00
---

# Investigate MCP calls using Trace  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/instrumentation/trace-remote-mcp-server-calls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Investigate MCP calls using Trace Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Trace lets you analyze the behavior and performance of agentic applications that call remote Google Cloud MCP servers. You can instrument your application to record prompts, responses, and method invocations, while remote MCP servers generate spans for tool calls. A _trace_ captures the end-to-end operation to show call sequences and overall latency, while individual _spans_ provide status and timing details for specific functions.

## About tools

_Tools_ let an agent gather information outside of its training data, typically by interacting with external APIs. With Google Cloud MCP servers, your agentic applications can call tools that invoke Google Cloud API methods. For example, your application can call the [list_log_entries](https://docs.cloud.google.com/logging/docs/reference/v2_mcp/mcp/tools_list/list_log_entries) tool to fetch recent log data.

The [Model Context Protocol (MCP)](https://cloud.google.com/discover/what-is-model-context-protocol) is a specification that defines a standardized way for AI agents to communicate and interact with external tools, data sources, and resources. For a complete list of products that provide an MCP server and links to their reference documentation, see [Supported products](https://docs.cloud.google.com/mcp/supported-products).

## How trace context is passed to an MCP server

MCP reference pages, such as the documentation for [`list_log_entries`](https://docs.cloud.google.com/logging/docs/reference/v2_mcp/mcp/tools_list/list_log_entries), provide an example `curl` command that you can use to send HTTP requests to the tool. The JSON payload sent in the request is similar to the following:
    
    
    {
      "jsonrpc": "2.0",
      "method": "tools/call",
      "params": {
        "name": "NAME",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "id": 1
    }
    

The value of the `name` field lists the tool name, such as `list_log_entries`. The `arguments` field contains the information required by the operation to complete the request.

The MCP standard defines a [`_meta` field](https://modelcontextprotocol.io/specification/2025-06-18/basic#_meta), which lets clients and servers attach metadata to their interactions. Clients and servers can use this field to pass the [trace context](https://docs.cloud.google.com/trace/docs/trace-context):
    
    
    {
      "jsonrpc": "2.0",
      "method": "tools/call",
      "params": {
        "name": "NAME",
        "arguments": {
          // provide these details according to the tool's MCP specification
        },
        "_meta": {
            "traceparent": "00-TRACE_ID-PARENT_SPAN_ID-SAMPLED_FLAG",
            "tracestate": "Vendor specific information."
          },
      },
      "id": 1
    }
    

The `_meta` data includes a `traceparent` field. The format of the value of this field is defined by the World Wide Web Consortium (W3C) [`traceparent` header](https://www.w3.org/TR/trace-context/). The value includes the following:

  * Version of the `traceparent` specification (`00`).
  * ID of the trace (TRACE_ID).
  * ID of the calling span (PARENT_SPAN_ID).
  * Whether the calling span sampled the request (SAMPLED_FLAG). This field has a value of `01` when sampled and `00` when not sampled.



The `tracestate` field carries vendor-specific tracing information.

### Limitations

  * The trace context must follow the [W3C Trace Context](https://www.w3.org/TR/trace-context/) standard, and the [`sampled` flag](https://www.w3.org/TR/trace-context/#sampled-flag) must be set to 1.

  * Remote Google Cloud MCP servers can generate a single span for a `tools/call` operation, but they don't generate spans for other types of operations or child spans for the `tools/call` operation.

  * Remote Google Cloud MCP servers generate a span only when the request is authenticated, authorized, and passes other internal checks.




## MCP servers that support tracing

This section lists the remote Google and Google Cloud MCP servers that support tracing. It also describes how your self-hosted MCP servers can generate trace spans.

### Self-hosted servers

We recommend that you instrument your self-hosted MCP servers to send telemetry data to your Google Cloud project. If you use Python, then the instrumentation can generate spans for `tools/call` operations. For more information, see [Instrument a self-hosted MCP server with OpenTelemetry](https://docs.cloud.google.com/stackdriver/docs/instrumentation/self-hosted-mcp-servers).

### Remote Google and Google Cloud MCP servers that support tracing

The following products contain an integration that lets their remote MCP server generate a trace span for a `tools/call` operation:

Product | Reference  
---|---  
Cloud Logging | [Cloud Logging MCP reference](https://docs.cloud.google.com/logging/docs/reference/v2_mcp/mcp)  
Cloud Monitoring | [Cloud Monitoring MCP reference](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp)  
Maps Grounding Lite | [Maps Grounding Lite MCP reference](https://developers.google.com/maps/ai/grounding-lite/reference/mcp)  
GKE | [GKE MCP reference](https://docs.cloud.google.com/kubernetes-engine/docs/reference/mcp)  
Cloud Run | [Cloud Run MCP reference](https://docs.cloud.google.com/run/docs/reference/mcp)  
Compute Engine | [Compute Engine MCP reference](https://docs.cloud.google.com/compute/docs/reference/mcp)  
Google Security Operations | [Google SecOps MCP reference](https://docs.cloud.google.com/chronicle/docs/reference/mcp)  
AlloyDB for PostgreSQL | [AlloyDB for PostgreSQL MCP reference](https://docs.cloud.google.com/alloydb/docs/reference/mcp)  
Agent Search | [Agent Search MCP reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/mcp)  
Cloud SQL | 

  * [Cloud SQL for MySQL MCP reference](https://docs.cloud.google.com/sql/docs/mysql/reference/mcp)
  * [Cloud SQL for PostgreSQL MCP reference](https://docs.cloud.google.com/sql/docs/postgres/reference/mcp)
  * [Cloud SQL for SQL Server MCP reference](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp)

  
BigQuery | [BigQuery MCP reference](https://docs.cloud.google.com/bigquery/docs/reference/mcp)  
Personalized Service Health | [Personalized Service Health MCP reference](https://docs.cloud.google.com/service-health/docs/reference/mcp)  
Cloud Billing | [Cloud Billing MCP reference](https://docs.cloud.google.com/billing/docs/reference/mcp)  
Policy Troubleshooter | [Policy Troubleshooter MCP reference](https://docs.cloud.google.com/policy-intelligence/docs/reference/policytroubleshooter/mcp)  
Managed Service for Apache Airflow | [ Managed Service for Apache Airflow MCP reference](https://docs.cloud.google.com/composer/docs/reference/mcp)  
Datastream | [Datastream MCP reference](https://docs.cloud.google.com/datastream/docs/reference/mcp)  
Policy Analyzer | [Policy Analyzer MCP reference](https://docs.cloud.google.com/policy-intelligence/docs/reference/policyanalyzer/mcp/policy-analyzer-mcp)  
Unified Maintenance | [Unified Maintenance MCP reference](https://docs.cloud.google.com/unified-maintenance/docs/reference/mcp)  
Identity and Access Management | [Identity and Access Management MCP reference](https://docs.cloud.google.com/iam/docs/reference/mcp)  
Organization Policy Service | [Organization Policy Service MCP reference](https://docs.cloud.google.com/organization-policy/reference/mcp)  
Spanner | [Spanner MCP reference](https://docs.cloud.google.com/spanner/docs/reference/mcp)  
Security Command Center | [Security Command Center MCP reference](https://docs.cloud.google.com/security-command-center/docs/reference/mcp)  
  
## Configure your application

You can use any framework or SDK that passes the trace context using the [`_meta` field](https://modelcontextprotocol.io/specification/2025-06-18/basic#_meta). These frameworks and SDKs include those that support the [OpenTelemetry Semantic Conventions for MCP](https://opentelemetry.io/docs/specs/semconv/gen-ai/mcp).

For example, you can use the [Agent Development Kit (ADK) framework](https://google.github.io/adk-docs/). To learn more, see [Instrument ADK applications with OpenTelemetry](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-adk).

## View spans

To view your trace data, use the **Trace Explorer**. This page lets you view aggregate information about your trace data and explore individual traces and spans. To learn more, see [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces).

To view spans written by MCP servers, filter your trace data by the span name. For example, some remote Google Cloud MCP servers can generate a trace span when they receive a `tools/call` operation. These spans have the following naming convention:
    
    
    tools/call NAME
    

In the previous expression, NAME refers to the invoked tool—for example, `list_keys`. This naming convention is defined by the [OpenTelemetry Semantic Conventions for MCP](https://opentelemetry.io/docs/specs/semconv/gen-ai/mcp).

To find these spans, use the filter bar and add an attribute filter for `mcp.method.name`. Set the value of the filter to `tools/call`. For detailed information about these steps, see [View calls to remote MCP servers](https://docs.cloud.google.com/trace/docs/finding-traces#mcp-tool-calls).

## Instrumentation samples

For instrumentation recommendations, see [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach).

The instrumentation samples we provide use [OpenTelemetry](https://opentelemetry.io):

  * For samples that use a collector-based export, see the following:

    * [Go](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/go)
    * [Java](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/java)
    * [Node.js](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/nodejs)
    * [Python](https://docs.cloud.google.com/stackdriver/docs/instrumentation/setup/python)

These samples send metric and trace data that follows the [OpenTelemetry Protocol](https://opentelemetry.io/docs/specs/otlp) (OTLP) format to your project by using the Telemetry API. The samples use a Google Cloud exporter for log data.

  * For information about how to use a direct export of trace data and send that data to the Telemetry API, see [Migrate from the Trace exporter to the OTLP endpoint](https://docs.cloud.google.com/stackdriver/docs/instrumentation/migrate-to-otlp-endpoints).

  * For samples that show you how to configure an agentic application to collect prompts and responses, see [How to instrument your generative AI applications](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-overview#how).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
