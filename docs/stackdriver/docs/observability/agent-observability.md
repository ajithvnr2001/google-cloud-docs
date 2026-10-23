---
url: https://docs.cloud.google.com/stackdriver/docs/observability/agent-observability/
title: Agent observability \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:42:09.459402+00:00
---

# Agent observability  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/observability/agent-observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Agent observability Stay organized with collections  Save and categorize content based on your preferences. 

In the rapidly evolving landscape of AI, building and deploying agents introduces unique challenges. AI agents can drift, hallucinate, and regress silently. They can make decisions and take actions that you don't expect. They can also fail in ways that are different from non-agentic software. _Agent observability_ refers to the methods for gaining insights into the internal state and behavior of software agents, particularly AI-powered agents such as those built using Large Language Models (LLMs).

## Benefits of agent observability

Because AI agents are non-deterministic and complex, observability is crucial for understanding, debugging, evaluating, and improving their performance, safety, and reliability.

Key aspects of agent observability include monitoring and analyzing the following:

  * LLM interactions: Track prompts, responses, token usage, latency, and error rates.
  * Tool usage: Monitor external tools and APIs the agent interacts with, including call counts, successes or failures, latency, and the data exchanged.
  * Agent behavior and reasoning: Understand the agent's decision-making process, the sequence of steps taken, and internal state changes.
  * Performance: Measure end-to-end latency of agent invocations, latency of individual steps, and resource consumption, which often involves detailed tracing.
  * Security and safety: Track policy enforcement, identify risky operations, analyze content safety, and monitor access patterns.
  * Quality and evaluation: Assess the correctness, factuality, helpfulness, and overall quality of the agent's outputs, often integrating with evaluation frameworks.



## What is agent observability within Google Cloud?

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

## Get started with agent observability

  * For information about how to build, deploy, and manage AI agents that use reasoning and tools to perform complex enterprise tasks, see [Agents overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents).

  * To learn about the observability tools provided by Gemini Enterprise Agent Platform, see [Observability overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/overview).

  * To learn how to perform evaluations, which provide information about agent quality, see [Agent evaluation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation).

  * For code samples, see the following:

    * [Observability for AI agent developers](https://docs.cloud.google.com/stackdriver/docs/opentelemetry/ai-agent-developers).
    * [Collect and view multimodal prompts and responses](https://docs.cloud.google.com/stackdriver/docs/instrumentation/collect-view-multimodal-prompts-responses).



## What's next

  * For information about how to secure and govern your agents, see [Govern your agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
