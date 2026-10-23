---
url: https://docs.cloud.google.com/agent-registry/concepts/
title: Key concepts \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:16.729051+00:00
---

# Key concepts  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Key concepts Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry uses standardized terminology to describe the components, resources, and governance mechanisms across your AI ecosystem. Understanding these foundational concepts helps you register, discover, connect, and govern agents, MCP servers, endpoints, and skills in Agent Registry.

## A2A skill

_Compare withskill._

A capability description listed inline within an agent's `agent-card.json` [Agent Card](https://agent2agent.info/docs/concepts/agentcard/). An A2A skill describes the tasks an agent can perform and its communication interfaces so that other agents know when and how to delegate work to it.

Agent Registry supports versions `0.3` and `1.0` of the [Agent2Agent (A2A) specification](https://a2a-protocol.org/). For a comparison with standalone skills, see [Differences between standalone and A2A skills](https://docs.cloud.google.com/agent-registry/skills-architecture#standalone-vs-a2a).

## Agent

An autonomous actor in your AI ecosystem that plans, reasons, invokes tools, and collaborates with other agents. An agent is defined by its [agent identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers) and each A2A skill or standalone skill it possesses. In Agent Registry, a registered agent is represented as a read-only `Agent` discovery resource.

## Agent principal

The unique Identity and Access Management (IAM) identity assigned to an agent, letting it hold permissions, access downstream resources, and generate audit logs. It takes the form of a verifiable Google Cloud service account or managed workload identity, such as a [SPIFFE ID](https://spiffe.io/), bound directly to the compute runtime of the agent.

Principal strings incorporate the runtime reference path and support three scopes: the engine instance, project-wide principal sets, and organization-wide principal sets.

For complete syntax and access control guidance, see [Agent principals](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-principals).

## Agentic component

A modular, functional entity within an AI ecosystem that Agent Registry lets you register, discover, and govern. The registry categorizes agentic components into four primary types: agent, MCP server, endpoint, and skill.

For more information, see [Component lifecycle and discovery](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery).

## Agentic workflow

A sequence of steps where an AI agent independently determines tool usage, reasoning, and execution paths to accomplish a task.

## Auth provider

A configuration within [Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/agent-identity-overview#agent-auth-manager) to store, acquire, and manage credentials, such as API keys or OAuth tokens, for connecting your agent to external tools and downstream services.

For more information about binding agents to auth providers, see [Component relationships](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery#component-relationships).

## Binding

A directed connection between a source agent and a target resource, such as another agent, an MCP server, or an endpoint. Bindings establish explicit delegation pathways between components and associate an agent with an auth provider for delegated permissions.

For more information, see [Bindings](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery#bindings).

## Data resource

A specific data context or dataset exposed by an MCP server that an agent can access to ground its responses or inform its actions.

## Discovery

The process of querying Agent Registry to find a registered agent, MCP tool, endpoint, or skill using natural language search, tags, or [registry identifiers](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#registry-identifiers).

Discovery in Agent Registry focuses on consumption discovery, which identifies the capabilities and components that your orchestrator agents can invoke at runtime. For more information, see [Discovery types](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery#discovery-types).

## Endpoint

A target URL, typically a REST API, accessed by an agent. In Agent Registry, a registered endpoint is represented as a read-only `Endpoint` discovery resource, letting you centrally govern which external services an agent can access.

## Governance project

The Google Cloud project where you [enable the Agent Registry API](https://docs.cloud.google.com/agent-registry/setup) to centrally catalog, discover, and govern your agentic components. For more information about single-project and cross-project configurations, see [Define the governance project for a central registry](https://docs.cloud.google.com/agent-registry/overview#governance-project).

## Governance scope

The geographic and architectural boundary where Agent Registry resources are registered and governed.

Agent Registry uses a central Google Cloud [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project), where you enable the Agent Registry API to catalog and govern your agentic components. Automatic registration discovers supported workloads deployed in that governance project. To govern _remote_ components, which are agents, MCP servers, or endpoints hosted outside the governance project in separate Google Cloud projects, on-premises environments, or external clouds, you manually register them in the governance project's registry.

When Agent Registry automatically registers a Google or Google Cloud remote MCP server, it creates the `McpServer` resource only in the `global` location, not in individual regions. You can manually register agents, MCP servers, and endpoints, and create bindings, in a supported regional location or the `global` location. Regional gateways can govern and route traffic to both regional resources and `global` MCP servers.

For full regional scoping rules and policy requirements, see [Agent Registry locations](https://docs.cloud.google.com/agent-registry/locations#governance-scope).

## Model Context Protocol (MCP)

The open standard used to connect AI models to data sources and tools, replacing bespoke plugins.

## MCP server

A program that implements the [Model Context Protocol (MCP)](https://docs.cloud.google.com/mcp/overview#how-mcp-works) to expose standardized tool and data resource capabilities to an AI agent. In Agent Registry, a registered MCP server is represented as a read-only `McpServer` discovery resource.

## Publisher

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

An entity that creates and registers a skill, represented as a `Publisher` resource in Agent Registry. A publisher establishes the ownership and [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers) syntax for a skill.

Google-managed skills use service domains. Manually created skills are automatically scoped to the `private` publisher with a `private-` prefix.

For more information, see [Publishers](https://docs.cloud.google.com/agent-registry/skills-architecture#publishers).

## Registration

The process of adding an agentic component, such as an agent, MCP server, endpoint, or skill, to Agent Registry.

Agent Registry supports two registration models:

  * **Automatic registration** : automatic ingestion of agents, MCP servers, and Google-managed skills from supported Google Cloud runtimes, such as Agent Runtime on Gemini Enterprise Agent Platform, deployed in the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled.
  * **Manual registration** : explicit registration of remote or custom agents, MCP servers, endpoints, and private standalone skills, including components hosted in separate Google Cloud projects, on-premises environments, external clouds, or unsupported runtimes, by creating resources in the governance project's registry.



For a detailed architectural comparison, see [Registration models](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery#registration-models).

## Registry identifier

A globally unique, immutable Uniform Resource Name (URN) that Agent Registry assigns to a registered agentic component. This identifier provides a stable reference for consumers and orchestrator agents to discover, filter, and search components in Agent Registry, remaining constant regardless of underlying infrastructure changes or code updates.

For detailed URN syntax formats, see [Registry identifiers](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#registry-identifiers).

## Runtime reference

The physical runtime location or compute infrastructure hosting an agent, MCP server, or endpoint, represented in Agent Registry by the `agentregistry.googleapis.com/system/RuntimeReference` attribute. For example, a runtime reference can point to an Agent Runtime reasoning engine, a Google Kubernetes Engine (GKE) deployment, or a Cloud Run service.

The runtime reference path is embedded within the agent principal for IAM policy evaluation. For more information, see [Runtime references](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#runtime-references).

## Service resource

The writable resource in Agent Registry, identified by its own [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names), that you use for management operations when you manually register an agent, an MCP server, or an endpoint. The `Service` resource stores the component's metadata, including the type of agentic component and configuration details such as its interface URL, description, protocol binding, and capability specification. An automatically registered component or standalone skill doesn't use a `Service` resource.

You create, update, or delete a `Service` resource to register, update metadata for, or unregister a manually registered component in Agent Registry without modifying or deleting the underlying deployment. When you create or update a `Service` resource, Agent Registry reads the metadata and automatically creates or updates the corresponding `Agent`, `McpServer`, or `Endpoint` discovery resource. In Agent Registry, consumers, such as orchestrator agents, client applications, and developers, use these read-only discovery resources to list, search, and view agentic components. For more information, see [Agentic component representation in Agent Registry](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery#agentic-components-representation).

## Skill

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

_Compare withA2A skill._

A standalone package registered as a top-level `Skill` resource in Agent Registry that extends the capabilities of an agent by providing specific instructions and optional scripts to complete a task. A skill contains a `SKILL.md` instruction file, optional scripts, and metadata assets.

A skill is identified by a [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers) scoped by a publisher and a standard [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names). Each skill maintains a default revision pointer and has one or more versioned snapshots, each represented as a skill revision.

For architecture, packaging, and lifecycle details, see [Skills architecture](https://docs.cloud.google.com/agent-registry/skills-architecture).

### Skill revision

An immutable, versioned snapshot of a skill package, represented as a `SkillRevision` resource in Agent Registry. A skill revision lets you update skill instructions or optional scripts without changing the parent [skill identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#skill-identifiers) or breaking existing agent dependencies.

For more information about revision versioning and immutability, see [Skill revisions](https://docs.cloud.google.com/agent-registry/skills-architecture#skill-revision).

## Tool

A deterministic function provided by an MCP server that an agent can invoke.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
