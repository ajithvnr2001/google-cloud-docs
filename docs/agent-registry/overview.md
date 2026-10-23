---
url: https://docs.cloud.google.com/agent-registry/overview/
title: Agent Registry overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:14.113757+00:00
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

Agent Registry lets you register, discover, and govern agentic components, including AI agents, Model Context Protocol (MCP) servers and tools, endpoints, and standalone skills, across your Google Cloud environment. By consolidating these components into a single registry, you can help eliminate fragmented tool access, isolated data, and redundant integrations across your AI deployments.

You can view and manage registered components as resources in Agent Registry. For more information about Agent Registry resources, see [Agent Registry data model](https://docs.cloud.google.com/agent-registry/data-model).

## Why use Agent Registry?

Agent Registry is structured around three primary goals to help you manage your agents, MCP servers, endpoints, and skills:

  * **Accelerate development** : discover and reuse existing agentic capabilities such as [A2A skills](https://docs.cloud.google.com/agent-registry/skills-architecture#standalone-vs-a2a), standalone [skills](https://docs.cloud.google.com/agent-registry/skills-architecture), and MCP tools across your organization. You can query the registry to identify and use available capabilities, removing the need to create custom integrations for each new process.
  * **Simplify integration** : use standardized MCP or Agent2Agent (A2A) protocols to locate and connect to functional endpoints, and help reduce infrastructure management overhead.
  * **Support governance** : enforce security through network and access policies and boundaries across your agentic fleet. Other services can use the [identifiers of your agentic components](https://docs.cloud.google.com/agent-registry/identity-and-identifiers) to define permissions and control which agents can access your data, including centralizing agent metadata across multiple Google Cloud projects for governance with [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview).



## Use Agent Registry with Gemini Enterprise Agent Platform

Agent Registry is designed to work alongside other services in [Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview) to secure and govern agent interactions at runtime.

In Agent Platform, Agent Registry maintains the authoritative registry of agents, MCP servers, tools, skills, and external endpoints that you need to govern, and generates the [identifiers and resource names](https://docs.cloud.google.com/agent-registry/identity-and-identifiers) referenced by discovery clients and security policies.

Identity and Access Management (IAM) access policies bind [agent principals](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-principals) to the target resources registered in Agent Registry. You can provision verifiable agent principals for workloads through [Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/agent-identity) and manage credentials for external tools through [auth providers](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery#auth-providers).

[Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) uses your IAM and content security policies to determine where to enforce policies at runtime as the network enforcement point for agent traffic. Before routing requests between agents, MCP servers, or external endpoints, Agent Gateway queries Agent Registry and evaluates your configured IAM and content security policies.

## Define the governance project for a central registry

In Agent Registry, a _governance project_ is the Google Cloud project where you [enable the Agent Registry API](https://docs.cloud.google.com/agent-registry/setup) to centrally catalog, discover, and govern your [agentic components](https://docs.cloud.google.com/agent-registry/data-model). You run discovery queries, manage registry resources, and configure access and egress policies in this project.

Depending on your architecture, you can use a governance project in a single-project or cross-project configuration:

  * **Single-project configuration** : you deploy your AI workloads and enable Agent Registry in the same Google Cloud project. Agent Registry [automatically registers](https://docs.cloud.google.com/agent-registry/automatic-registration) supported workloads deployed in that project, and you can [manually register](https://docs.cloud.google.com/agent-registry/manual-registration) custom components or external endpoints in the same project.
  * **Cross-project configuration** : you designate a central Google Cloud project as your governance project where Agent Registry and shared governance services such as [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) are enabled, while your AI workloads run in separate Google Cloud projects, on-premises environments, or external clouds. In Agent Registry, components hosted outside the governance project are referred to as _remote_ components. Because automatic registration only discovers supported workloads deployed in the governance project, you manually register remote components in the central registry using `Service` resources. For more information, see [Cross-project registration considerations](https://docs.cloud.google.com/agent-registry/register-agents#cross-project-considerations).



## What's next

  * Learn about the Agent Registry [data model](https://docs.cloud.google.com/agent-registry/data-model) to understand how to manage your agentic capabilities.
  * Review [key concepts](https://docs.cloud.google.com/agent-registry/concepts) to familiarize yourself with the essential terms used in Agent Registry.
  * Learn about [Identity and identifiers](https://docs.cloud.google.com/agent-registry/identity-and-identifiers) used for registry discovery and policy governance.
  * Learn about [Component lifecycle and discovery](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery) and [Skills architecture](https://docs.cloud.google.com/agent-registry/skills-architecture).
  * To get started, [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
