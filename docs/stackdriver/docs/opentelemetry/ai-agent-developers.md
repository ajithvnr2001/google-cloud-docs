---
url: https://docs.cloud.google.com/stackdriver/docs/opentelemetry/ai-agent-developers/
title: Observability for AI agent developers \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:24.785132+00:00
---

# Observability for AI agent developers  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/opentelemetry/ai-agent-developers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Observability for AI agent developers Stay organized with collections  Save and categorize content based on your preferences. 

If you develop AI agents, then you can instrument your applications with OpenTelemetry to observe how your agents reason, call tools, and respond to prompts. This guide explains how to capture agent telemetry using frameworks such as LangGraph and the Agent Development Kit (ADK), and how to analyze multimodal prompts and responses in Cloud Trace.

## Instrument agents to understand their behavior

When you are developing or managing generative AI applications, telemetry data captures the reasoning steps, tool calls, and external interactions of your autonomous agents. This data is useful for the following reasons:

  * **Understand non-deterministic behavior:** Because an agent's reasoning process isn't deterministic, telemetry is the only reliable way to inspect the decisions an agent makes and the tools it selects.
  * **Troubleshoot and diagnose errors:** Traces help you identify failed API requests, infinite execution loops, and latency bottlenecks across distributed agent workflows.
  * **Support governance and validate traffic:** Telemetry lets you visualize communication flows—such as in [Application Topology](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology)—to verify that your agents communicate only with authorized agents, MCP servers, and external endpoints.
  * **Evaluate output quality and cost:** Collecting prompts, responses, and token usage helps you assess model accuracy, detect hallucinations, and optimize resource consumption.



## How you can instrument your generative AI applications

Instrumenting your application involves generating telemetry and sending it to a destination where the data can be stored, queried, and analyzed. For example, when your instrumentation sends telemetry to your Google Cloud project, you can use [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) to view and analyze that data.

[Cloud Trace](https://docs.cloud.google.com/trace/docs/finding-traces#view_generative_ai_events) automatically extracts events from spans written by generative AI applications when those spans conform to the semantic conventions for spans and events. For information about those conventions, see the following documents:

  * [Semantic conventions for generative AI spans](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/)
  * [Semantic conventions for generative AI events](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-events/)



Cloud Trace can also display multimodal prompts and responses. In this scenario, your prompts and responses aren't attached to your trace data. Instead, they are stored in a Cloud Storage bucket. To learn more about this configuration, see [Collect and view multimodal prompts and responses](https://docs.cloud.google.com/stackdriver/docs/instrumentation/collect-view-multimodal-prompts-responses).

## Best practices

We recommend that you instrument your application with OpenTelemetry, which is an open-source project that provides a unified framework for application instrumentation. The instrumentation samples listed in this document use OpenTelemetry.

We also recommend that you store your prompts and responses in a Cloud Storage bucket instead of in a log entry:

  * You have fine-grained control over the content in the Cloud Storage bucket. For example, you can delete individual conversations stored in a bucket. However, you can't delete individual log entries.

  * Cloud Storage buckets can store objects that are much larger than the maximum size of a log entry, which is limited to 256 KiB. Cloud Logging responds with an `INVALID_ARGUMENT` error and discards data if the received data exceeds the maximum log entry size. If the command completes without error but individual fields exceed their size limits, then Cloud Logging truncates that data.




For information about OpenTelemetry, see [What is OpenTelemetry?](https://opentelemetry.io/docs/what-is-opentelemetry).

## Instrumentation samples

To get started with agent instrumentation, see the following sample applications and guides:

  * [Collect and view multimodal prompts and responses](https://docs.cloud.google.com/stackdriver/docs/instrumentation/collect-view-multimodal-prompts-responses) describes how to configure a LangGraph ReAct agent or a generative AI agent built with ADK to collect multimodal prompts and responses. It also describes how to do the following:

    * Store prompts and responses in a Cloud Storage bucket.
    * View prompts and responses with the **Trace Explorer** page.
    * Analyze prompts and responses with BigQuery.
    * Evaluate prompts and responses with the [Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk).
  * [Instrument a LangGraph ReAct agent with OpenTelemetry](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-langgraph) describes how to use OpenTelemetry to instrument a generative AI application that uses the LangChain or LangGraph framework. It also links to a sample application that you can download and run. The sample application collects text prompts and responses.

  * [Instrument ADK applications with OpenTelemetry](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-adk) describes how to enable built-in instrumentation that collects telemetry from the agent's key actions. The telemetry includes text prompts and agent responses. It also links to a sample application that you can download and run. The sample application collects text prompts and responses.

  * [Investigate MCP calls by using Trace](https://docs.cloud.google.com/stackdriver/docs/instrumentation/trace-remote-mcp-server-calls) describes how to configure your application to pass trace context to remote Google Cloud MCP servers, which lets those servers attach spans to a trace.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
