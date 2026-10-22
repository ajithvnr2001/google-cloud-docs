---
url: https://docs.cloud.google.com/agent-registry/overview/
title: Agent Registry overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:06.339877+00:00
---

# Agent Registry overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Agent Registry overview Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry is a centralized catalog that lets you store, discover, and govern [agentic components](https://docs.cloud.google.com/agent-registry/concepts#agentic-component), such as Model Context Protocol (MCP) servers, tools, standalone skills, and AI agents, within Google Cloud.

As you deploy and expand AI capabilities, Agent Registry provides the core infrastructure for your environment, bringing together autonomous agents with the consistent data contexts and tools that MCP servers offer. By consolidating these agents, MCP servers, skills, and endpoints, Agent Registry addresses common challenges in complex AI deployments, such as fragmented tool access, isolated data, and redundant implementations.

Based on the [data model](https://docs.cloud.google.com/agent-registry/data-model) that the Agent Registry API uses, you manage `Agent`, `McpServer`, `Endpoint`, `Skill`, `SkillRevision`, and `Publisher` resources to register, search for, and govern agents, endpoints, MCP servers, and skills in Agent Registry.

## Why use Agent Registry?

Agent Registry is structured around three primary goals to help you manage your agents, MCP servers, and endpoints:

  * **Accelerate development** : Discover and reuse existing agentic capabilities such as [A2A skills](https://docs.cloud.google.com/agent-registry/concepts#a2a-skill), standalone [skills](https://docs.cloud.google.com/agent-registry/concepts#skill), and MCP [tools](https://docs.cloud.google.com/agent-registry/concepts#tool) across your organization. You can query the registry to identify and use available capabilities, removing the need to create custom integrations for each new process.
  * **Simplify integration** : Use standardized MCP or Agent2Agent (A2A) protocols to locate and connect to functional endpoints, and help reduce infrastructure management overhead.
  * **Support governance** : Enforce security and implement boundaries across your agentic fleet. Other services can use the [identifiers of your agentic components](https://docs.cloud.google.com/agent-registry/identity-and-identifiers) to define permissions and control which agents can access your data, including centralizing agent metadata across multiple Google Cloud projects for governance with [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview).



## Use Agent Registry with Agent Platform

Agent Registry isn't only a standalone catalog for discovering and managing agentic components. Agent Registry is designed to work alongside other services in [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview) to secure and govern agent interactions at runtime.

In Agent Platform, Agent Registry provides the catalog of capabilities and destinations that you want to register. It maintains the authoritative inventory of agents, MCP servers, tools, skills, and external endpoints, and generates the [identifiers and resource names](https://docs.cloud.google.com/agent-registry/identity-and-identifiers) referenced by discovery clients and security policies.

Other services, such as [Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity), determine who makes the request. Agent Identity provisions verifiable [agent principals](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-principals) for workloads and manages credentials for external tools through [auth providers](https://docs.cloud.google.com/agent-registry/concepts#auth-provider). Identity and Access Management (IAM) access policies bind these agent principals to the target resources registered in Agent Registry.

Finally, [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) determines where the policies are enforced. Agent Gateway acts as the runtime network enforcement point for agent traffic. Before routing requests between agents, MCP servers, or external endpoints, Agent Gateway queries Agent Registry and evaluates IAM and content security policies.

## What's next

  * Learn about the Agent Registry [data model](https://docs.cloud.google.com/agent-registry/data-model) to understand how to manage your agentic capabilities.
  * Review [key concepts](https://docs.cloud.google.com/agent-registry/concepts) to familiarize yourself with the essential terms used in Agent Registry.
  * Learn about [Identity and identifiers](https://docs.cloud.google.com/agent-registry/identity-and-identifiers) used for catalog discovery and policy governance.
  * To get started, [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
