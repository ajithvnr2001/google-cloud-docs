---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/overview/
title: Observability overview \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T23:38:49.240164+00:00
---

# Observability overview  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Observability overview Stay organized with collections  Save and categorize content based on your preferences. 

Agent observability in Gemini Enterprise Agent Platform provides comprehensive visibility into the performance, behavior, and health of your deployed agents and Model Context Protocol (MCP) servers. By monitoring key metrics, tracing execution paths, and observing your multi-agent system as a whole, you can diagnose issues, optimize resource consumption, and improve the reliability of your agents.

This document provides an overview of the observability tools available within Gemini Enterprise Agent Platform, including system-wide topology, individual agent monitoring, and MCP server metrics.

## Telemetry setup

To populate these observability dashboards, topologies, and traces, your agents must be configured to send telemetry data in the OpenTelemetry format to storage systems in Google Cloud Observability.

Ensure your agent and MCP server environments are properly configured to emit this data. Built-in Google Cloud components automatically emit telemetry in the OpenTelemetry format. For example, Model Armor natively emits standardized telemetry, allowing you to seamlessly expose and monitor real-time policy interceptions directly within your trace data without requiring any custom instrumentation.

For agent telemetry setup instructions and requirements, see the following resources:

  * To instrument agents built with the ADK, see [Instrument ADK applications with OpenTelemetry](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-adk).
  * To instrument agents on Agent Runtime that were not built with ADK, see [Instrument generative AI applications](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-overview).
  * For MCP server telemetry, see [Use Cloud Trace to monitor MCP tool use](https://docs.cloud.google.com/mcp/monitor-mcp-tool-use-with-cloud-trace).
  * For Model Armor telemetry, see [Configure Model Armor logging](https://docs.cloud.google.com/model-armor/configure-logging).



## Observability signals

Gemini Enterprise Agent Platform provides observability through metrics, traces, and logs.

When you select a specific agent from the Registry, the **Observability** tab provides a suite of targeted dashboards to monitor its operational health, performance, and infrastructure utilization. Use the left-hand navigation within the **Observability** tab to switch between the following views:

  * **Overview:** Tracks high-level usage over your selected timeframe, including total sessions, average turns per session, and total agent invocations. Time-series charts display token usage (input versus output), overall agent traffic volume, latency percentiles (p50, p95, p99), and error rates.
  * **Evaluation:** Displays online monitors for continuous quality assessment. This includes time-series widgets tracking average response quality, safety metrics, hallucination rates, and tool use quality.
  * **Models:** Breaks down performance by the underlying foundation model. You can monitor p95 latency, total call counts, error rates, quota failures, and token usage isolated by specific models.
  * **Tools:** Monitors the external tools and services connected to the agent. This view details p95 latency, call counts, and error rates per tool, as well as the frequency of interactions where no tool was called.
  * **Usage:** Provides infrastructure-level metrics for the agent's runtime environment, including container CPU allocation, container memory allocation, and token usage.
  * **Logs:** Displays a filterable stream of raw agent logs, including severity, timestamps, and execution summaries for deep-dive troubleshooting. For more information, see [View agent logs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/logging#view-logs).



In addition to the dashboards on the **Observability** tab, you can use the agent's **Traces** tab to inspect the step-by-step execution of specific sessions, including directed acyclic graphs of spans and inputs/outputs. For more information, see [View Agent Traces](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/traces). You can also use the **Topology** tab to view the specific inbound and outbound dependencies for that single agent.

For MCP servers, you can monitor request count and p95 request duration to track utilization and responsiveness.

## Auditing agent actions

To support enterprise security and compliance audits, Gemini Enterprise Agent Platform uses _dual-attribution logging_ to record agent activity in Cloud Logging. When an agent performs an action or calls a tool on behalf of a person (user-delegated authority), audit and execution logs record both the SPIFFE-based [agent identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview#spiffe-identity) (`principal://...` in audit logs, or `spiffe://...` in execution logs) and the identity of the initiating human user. When an agent acts autonomously on its own authority, logs attribute the action directly to the unique agent identity.

Auditors and security administrators can isolate and review agent-initiated events in Cloud Logging by filtering for the `is_agentic=true` flag in log queries. Combining `is_agentic=true` with the agent identity or user principal lets you trace end-to-end execution paths and verify policy enforcement across all agent interactions.

## OpenTelemetry generative AI conventions

Agent traces and prompt-and-response logs rely heavily on the [OpenTelemetry Semantic Conventions for generative AI systems](https://opentelemetry.io/docs/specs/semconv/gen-ai/) to standardize how generative AI telemetry is captured, structured, and reported.

Adhering to these conventions is critical for agent tracing because it establishes a universal, vendor-agnostic format for describing complex, multi-step agent workflows—such as tool executions, retrieval steps, and token consumption. This standardization helps seamless interoperability across different observability backends and analytics tools, both inside and outside of Google Cloud.

## What's next

  * [View agent relationships](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology) as a topology graph.
  * [View agent traces](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/traces) to debug agent behavior.
  * [Evaluate your agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/evaluate-agents).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
