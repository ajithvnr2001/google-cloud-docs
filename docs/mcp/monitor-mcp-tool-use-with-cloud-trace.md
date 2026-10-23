---
url: https://docs.cloud.google.com/mcp/monitor-mcp-tool-use-with-cloud-trace/
title: Use Cloud Trace to monitor MCP tool use \u00a0|\u00a0 Google Cloud MCP servers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:37.560958+00:00
---

# Use Cloud Trace to monitor MCP tool use  |  Google Cloud MCP servers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mcp/monitor-mcp-tool-use-with-cloud-trace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Google Cloud MCP servers ](https://docs.cloud.google.com/mcp)
  * [ Guides ](https://docs.cloud.google.com/mcp/overview)



Send feedback 

#  Use Cloud Trace to monitor MCP tool use Stay organized with collections  Save and categorize content based on your preferences. 

To get answers about Google and Google Cloud remote MCP tool use, tool failures, and latency causes, you can use [Cloud Trace](https://docs.cloud.google.com/trace/docs). Cloud Trace can help you understand what paths were taken in the processing of a given request, and the errors that took place within the processing of the request. Cloud Trace can also help you when you're developing AI and non-AI applications or troubleshooting a failure. For more information, see [Cloud Trace overview](https://docs.cloud.google.com/trace/docs/overview).

## Example use-cases for Cloud Trace

You can use Cloud Trace to answer questions like the following:

  * Which Google MCP servers and tools does your project invoke?
  * Did your agent fail because it didn't identify the correct tool, or did the tool fail?
  * Are there agents calling Google Cloud services over MCP that lack instrumentation?
  * Was MCP request latency due to the MCP client, the network, or the MCP server?



## Cloud Trace terminology

The following terminology is useful to understand when discussing Cloud Trace:

Trace
    Represents a single end-to-end operation. Traces are composed of _spans_ , which are records for a single function or unit of processing. For more information about traces and spans, see [Traces and spans](https://docs.cloud.google.com/trace/docs/traces-and-spans).
Span
    A record of a unit of processing within the end-to-end operation. For more information about spans, see [Span data model](https://docs.cloud.google.com/trace/docs/traces-and-spans#span_data_model).
Trace context
    Identifies the end-to-end trace with a **Trace ID** , identifies the parent operation for the current span with the **Parent span ID** , includes flags that determine the tracing behavior, such as sampling decisions, and contains additional information for advanced tracing behaviors in the **State** field. For more information about trace context, see [Cloud Trace context](https://docs.cloud.google.com/trace/docs/trace-context).
Context propagation
    Passing context information to Cloud Trace. Some instrumentation libraries, such as OpenTelemetry (OTel), can propagate a `context` object that contains the data necessary for tracing. For a list of OTel libraries that support tracing, see [Language APIs & SDKs](https://opentelemetry.io/docs/languages/).
Sampling
    Whether or not data for a span is sent to Cloud Trace. Different sampling strategies are appropriate for different use-cases. For more information, read [Cloud Trace Sampling](https://docs.cloud.google.com/trace/docs/trace-sampling).

## Supported services

Not all remote MCP servers support Cloud Trace. To determine if a product supports Cloud Trace, refer to the list of [Remote MCP servers that support Cloud Trace](https://docs.cloud.google.com/trace/docs/trace-remote-mcp-server-calls#supported).

## Limitations

MCP support for Cloud Trace has the following limitations:

  * [X-Cloud-Trace-Context](https://docs.cloud.google.com/trace/docs/trace-context#legacy-http-header) and other non-W3C headers aren't supported. Only [W3C headers](https://www.w3.org/TR/trace-context/) are supported.
  * MCP operations other than `tools/call` don't send spans to Cloud Trace.
  * Requests that are unauthenticated, unauthorized, or don't pass API enablement or other policy checks might not be included in the set of requests eligible to be traced.



## Send trace spans to Cloud Trace

Remote MCP servers for Google and Google Cloud services generate trace spans when tracing context is supplied and the [sampled flag](https://www.w3.org/TR/trace-context/#sampled-flag) is set to `1`.

You can provide tracing context in the following ways:

  * In HTTP headers using the `traceparent` header.
  * In the MCP body using the `traceparent` key in the `params._meta` field.



For more information, see [Trace context](https://docs.cloud.google.com/trace/docs/trace-context).

Some libraries that interact with MCP can be configured to enable tracing. For example, you can [instrument Agent Development Kit with OpenTelemetry](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-adk).

For more information, read [Observability for AI agent developers](https://docs.cloud.google.com/stackdriver/docs/opentelemetry/ai-agent-developers) and [Instrument for Cloud Trace](https://docs.cloud.google.com/trace/docs/setup).

## View traces and spans

To view your MCP traces and spans, follow the instructions in [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces).

When you use the [Trace Explorer](https://docs.cloud.google.com/trace/docs/overview#tracing_interface), you can apply filters that let you view only the data that interests you. For data generated by MCP tools, you might want to filter by the resource, span, or scope attributes described in the following sections.

### Resource attributes

The following table describes resource attributes:

Attribute | Description  
---|---  
`cloud.account.id` | The ID of the Google Cloud billing project for the operation.  
`cloud.provider` | The cloud service. This value is always `gcp`.  
`gcp.mcp.server.id` | The Uniform Resource Name (URN) of the MCP server.  
`gcp.project_id` | The ID of the Google Cloud project where the telemetry data is sent.  
  
### Span attributes

The following table describes span attributes:

Attribute | Description  
---|---  
`error.message` | Error message in the case of an error.  
`error.type` | Low cardinality error type in the case of an error.  
`gen_ai.operation.name` | The kind of Generative AI operation. For MCP, this value is always `execute_tool` because the only supported operation is `tools/call`.  
`gen_ai.tool.name` | The name of the MCP tool that was invoked.  
`jsonrpc.protocol.version` | The version of the JSON-RPC protocol.  
`jsonrpc.request.id` | The unique ID used for the JSON-RPC invocation.  
`mcp.method.name` | The MCP operation name. For example, `tools/call`.  
`mcp.protocol.version` | The version of the MCP protocol used.  
  
### Scope attributes

The following table describes scope attributes:

Attribute | Description  
---|---  
`gcp.server.service` | The MCP server service name. For example, `bigquery.googleapis.com`.  
  
## What's next

  * Read about different [instrumentation approaches](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach) for Cloud Trace.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
