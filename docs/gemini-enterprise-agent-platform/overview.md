---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview/
title: Agent Platform overview \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:43:24.898774+00:00
---

# Agent Platform overview  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)



Send feedback 

#  Agent Platform overview Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise Agent Platform is a unified platform to build, deploy, govern, and optimize enterprise-grade AI agents and model-based solutions. As an evolution of Vertex AI, it supports the complete AI lifecycle from accessing over 200 foundation models to deploying and managing your agents. 

Agent Platform meets you where you are, with tools for all skill levels:

  * **Low-code development:**
    * **Agent Studio:** Design agents and interact with models without code.
  * **Code-based development:**
    * **Colab Enterprise Notebooks:** Perform code-based development, data analysis, and experimentation.
    * **Agent Development Kit:** Build sophisticated agents capable of complex reasoning and tool use with this modular, model-agnostic framework.



To meet enterprise requirements, Agent Platform includes integrated security and governance. Agent Identity lets you grant granular permissions to agents. Agent Gateway, together with Model Armor, secures all agent interactions, enforces runtime policies, and helps protect against threats and helps ensure compliant operations. 

## Gemini Enterprise Agent Platform Components

![Agent Platform is organized around four key pillars: Build, Scale, Govern, and Optimize.](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/images/gemini-enterprise-agent-platform.svg)**Figure 1:** Agent Platform is organized around four pillars: Build, Scale, Govern, and Optimize.

The Gemini Enterprise Agent Platform is organized around four key pillars:

  * Build
  * Scale
  * Govern
  * Optimize



### Build

Use these tools and services to design, prototype, and develop your AI agents.

  * [**Agent Development Kit:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk) A modular, model-agnostic framework for building and deploying complex AI agents.
  * [**Agent Studio:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio) A low-code visual canvas for designing, prototyping, and managing agent reasoning loops and workflows.
  * [**Agent Garden:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/agent-garden) A library of prebuilt agents and templates to accelerate development.
  * [**CodeMender:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/codemender) An autonomous AI code security agent that finds, verifies, and fixes vulnerabilities in your codebase.
  * [**Model Garden:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models) Access to Google's frontier models (like Gemini models), third-party, and open-source models.
  * [**RAG Engine:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview) Securely connects private enterprise data to LLMs to improve answer accuracy and reduce hallucinations.
  * [**Vector Search:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/overview) AI-native search engine for storing, searching, and managing data for AI applications.
  * [**Managed Agents API on Agent Platform:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/managed-agents) A config-driven, REST-first API for building autonomous agents inside a fully managed sandbox. Create and manage agent configurations and sandbox environments with mounted sources, such as skills and artifacts, by using the **Agents API** , and interact directly with your deployed agents at runtime by using the **Interactions API**.



### Scale

Deploy and manage your agents in a high-performance, stateful runtime environment.

  * [**Scale agents with Agent Runtime:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale) High-performance, scalable runtime environment for deploying and managing agents, supporting features like sub-second cold starts and long-running agents.
  * [**Agent Platform Sessions:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions) Manages stateful data and context within a single agent interaction.
  * [**Agent Platform Memory Bank:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank) Enables agents to have persistent memory and recall information across multiple sessions.
  * [**Code Execution:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/code-execution-overview) Enables AI agents to generate and run Python code in a secure, sandboxed environment to perform calculations, data analysis, and other complex logic.



### Govern

Secure, catalog, and govern your agents with enterprise-grade controls and policies.

  * [**Agent Registry:**](https://docs.cloud.google.com/agent-registry/overview) A centralized catalog for discovering, tracking, and managing all agents, tools, and MCP servers across the organization.
  * [**Agent Identity:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity) Provides a fully managed, unique identity for each agent, enabling secure access control and auditing.
  * [**Agent Gateway:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) A central policy enforcement point to govern all agent tool calls, manage authentication, and apply security policies.
  * [**Governance Policies:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/overview) Including Content Protection and Semantic Governance to mitigate risks like data leakage and ensure compliance.
  * [**AI threat and vulnerability scanning:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/view-security-findings) Real-time threat detection and vulnerability scanning specific to agentic systems.
  * [**AI Content Detection API:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/ai-content-detection) Provides a method to identify AI-generated content to support responsible media governance.



### Optimize

Assess, monitor, and refine your agents to ensure high quality and reliability.

  * [**Agent evaluation:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation) Systematically assess agent quality with tools like Multi-Turn AutoRaters and Online Evaluation for live traffic.
  * [**Simulate and evaluate agent behavior:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/evaluate-simulated) Generate synthetic test scenarios and simulate multi-turn user interactions with configurable personas to stress-test agent logic.
  * [**Observability:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/overview) Comprehensive monitoring, logging, and tracing tools, including the Unified Trace Viewer, provide detailed visibility into agent reasoning and performance for effective debugging.
  * [**Optimize agent prompts:**](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/optimize-agent) Programmatically refine agent system instructions and tool descriptions by analyzing failure patterns and proposing targeted updates. 



## How to use this documentation

The Agent Platform documentation is organized into sections to help you find the information you need.

Use the navigation tabs to explore the different areas of the platform:

  * **Studio** : Discover how to use Agent Studio for prompt design, model tuning, and other UI-based interactions with models.
  * **Agents** : Explore how to build, deploy, and manage AI agents for enterprise use cases using Agent Platform's agent framework and tools.
  * **Models** : Learn about the generative AI models available in Agent Platform, including Gemini models, and how to use them in your applications.
  * **Notebooks** : Find information on using Colab Enterprise notebooks for code-based model development, data analysis, and experimentation.



## What's next

Overview 

###  [ Build overview ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build)

Learn how to build agents in Google Agent Platform. 

Guide 

###  [ Deploy agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent)

Learn the five ways to deploy an agent on Agent Platform Runtime based on your development needs. 

Guide 

###  [ Common use cases ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents#common_use_cases)

Explore common use cases for agents. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
