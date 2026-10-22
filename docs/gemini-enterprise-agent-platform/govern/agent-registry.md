---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-registry/
title: Agent Registry \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:41:24.573578+00:00
---

# Agent Registry  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-registry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Agent Registry Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry serves as the central hub for governance, discovery, and search for your AI ecosystem within Gemini Enterprise Agent Platform. It provides a unified catalog that lets you securely store, discover, and manage Model Context Protocol (MCP) servers, tools, standalone skills (Preview), and AI agents across your organization.

As you scale your AI workloads, consolidating these agents, MCP servers, skills, and endpoints in Agent Registry helps you resolve common challenges in AI deployments, such as fragmented tool access, isolated data, and redundant implementations, while maintaining security and access controls.

## Learn more about Agent Registry

Explore the Agent Registry documentation to learn how to integrate and govern your AI agentic components.

### Discover and get started

  * **[Agent Registry overview](https://docs.cloud.google.com/agent-registry/overview)** : Understand the core concepts, architecture, and benefits of the registry.
  * **[Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup)** : Enable the required API and configure IAM roles for your project.



### Register your agentic components

  * **[Register agents](https://docs.cloud.google.com/agent-registry/register-agents)** : Register agents automatically from supported runtimes or manually for custom deployments.
  * **[Register MCP servers](https://docs.cloud.google.com/agent-registry/register-mcp-servers)** : Make remote MCP servers and tools discoverable to your orchestrators.
  * **[Register endpoints](https://docs.cloud.google.com/agent-registry/register-endpoints)** : Define target destinations to centrally govern the external APIs and services that your agents can connect to.
  * **[Register skills](https://docs.cloud.google.com/agent-registry/register-skills) (Preview)**: Centrally govern, version, and share executable capabilities across your organization's AI agents.



### Search and authenticate

  * **[Search for agents, tools, and skills](https://docs.cloud.google.com/agent-registry/search-agents-and-tools)** : Perform keyword, prefix, and semantic searches to find specific capabilities across your organization.
  * **[Authenticate to tools and resources](https://docs.cloud.google.com/agent-registry/authenticate-toolsets)** : Use the auth manager and bindings to securely authenticate agents to discovered tools.



### Compose and orchestrate agents

  * **[Resolve endpoints and build orchestrators](https://docs.cloud.google.com/agent-registry/resolve-endpoints-and-build-orchestrators)** : Resolve endpoints dynamically and build orchestrator agents using the Agent Development Kit (ADK).
  * **[Register a custom ADK agent](https://docs.cloud.google.com/agent-registry/register-custom-adk-agents)** : Expose and register custom ADK agents in Agent Registry.
  * **[Use registered A2A agents in Agent Studio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio/design-agents)** : Select registered Agent2Agent (A2A) agents directly within Agent Studio to design multi-agent applications.



### Govern registry resources declaratively with Terraform

  * **[Register cross-project and custom agents](https://docs.cloud.google.com/agent-registry/manual-registration#cross-project)** : Provision `google_agent_registry_service` resources across central and workload projects.
  * **[Manage tool and auth provider bindings](https://docs.cloud.google.com/agent-registry/manage-bindings#create)** : Connect source agents to downstream MCP servers, endpoints, and auth providers using `google_agent_registry_binding`.
  * **[Configure IAM egress policies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/configure-iam-policies)** : Grant `roles/iap.egressor` access to registered agents, MCP servers, and endpoints using `google_iap_agent_registry_*` IAM resources.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
