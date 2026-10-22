---
url: https://docs.cloud.google.com/agent-registry/concepts/
title: Key concepts \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:22.836796+00:00
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

This document explains the key terms and concepts related to Agent Registry.

## A2A skill

_Compare withskills._

A capability description listed inline within an agent's [Agent Card](https://agent2agent.info/docs/concepts/agentcard/) (`agent-card.json`). A2A skills describe the tasks an agent can perform and its communication interfaces so that other agents know when and how to delegate work to it.

Agent Registry supports versions `0.3` and `1.0` of the [Agent2Agent (A2A) specification](https://a2a-protocol.org/).

## Agent

An autonomous actor in your AI ecosystem, defined by its identifier and the specific A2A skills or skills it possesses.

## Agent identifier

A globally unique, immutable Uniform Resource Name (URN) for an agent. This identifier provides a stable reference for consumers to look up and invoke the agent, remaining constant regardless of underlying infrastructure changes or code updates.

For detailed URN syntax formats across supported runtimes, see [Agent identifiers](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers).

Agent Registry uses agent identifiers for inventory tracking, registry discovery, and filtering. If you want to govern access and authentication in IAM, use the agent principal instead.

## Agent principal

The unique Identity and Access Management (IAM) identity assigned to an agent, letting it hold permissions, access downstream resources, and generate audit logs. It takes the form of a verifiable Google Cloud service account or managed workload identity, such as a [SPIFFE ID](https://spiffe.io/), bound directly to the compute runtime of the agent.

Principal strings incorporate the runtime resource path and support three scopes: the engine instance, project-wide principal sets, and organization-wide principal sets.

For complete syntax and access control guidance, see [Agent principals](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-principals).

## Agentic component

A modular, functional entity within an AI ecosystem that Agent Registry lets you register, discover, and govern. The registry categorizes agentic components into four primary types: agents, MCP servers, endpoints, and skills.

## Agentic workflow

A sequence of steps where an AI agent independently determines tool usage, reasoning, and execution paths to accomplish a task.

## Auth provider

A configuration within [Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/agent-identity-overview#agent-auth-manager) to store, acquire, and manage credentials, such as API keys or OAuth tokens, for connecting your agent to specific external tools and applications and define the authentication type.

## Binding

A connection between a source agent and a target resource, such as another agent, an MCP server, or an endpoint. By creating bindings, you establish explicit relationships that let your orchestrator agents interact with downstream capabilities. Bindings are also used to associate an agent with an auth provider to support delegated permissions.

## Data resource

A specific data context or dataset exposed by an MCP server that an agent can access to ground its responses or inform its actions.

## Discovery

The process of querying the registry to find existing agents, MCP tools, or endpoints based on descriptions, tags, or skills.

Discovery in Agent Registry focuses on consumption-centric capabilities that your AI orchestrators can use. You discover already-registered capabilities to build and orchestrate AI systems.

This process in Agent Registry differs from infrastructure discovery, such as in [App Hub](https://docs.cloud.google.com/app-hub/docs/overview), which identifies unregistered compute resources in your Google Cloud projects.

## Endpoint

For the Agent Registry API, a resource that represents a target URL, typically a REST API, accessed by an agent. By abstracting these destinations into manageable resources, Agent Registry lets you centrally govern which external services an agent can access.

## Endpoint identifier

A globally unique, immutable Uniform Resource Name (URN) for a registered endpoint. Similar to agent identifiers and MCP server identifiers, this URN provides a stable registry reference for discovering target API destinations. For more information, see [Endpoint identifiers](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#endpoint-identifiers).

## Governance scope

The geographic and architectural boundary where Agent Registry resources are registered and governed.

Google-managed MCP servers are registered exclusively in the `global` location. You can manually register agents, MCP servers, and endpoints, and create bindings, in a supported regional location or the `global` location. Regional gateways can govern and route traffic to both regional resources and `global` MCP servers.

For full regional scoping rules and policy requirements, see [Agent Registry locations](https://docs.cloud.google.com/agent-registry/locations#governance-scope).

## Model Context Protocol (MCP)

The open standard used to connect AI models to data sources and tools, replacing bespoke plugins.

## MCP server (or server)

A service that implements the [Model Context Protocol (MCP)](https://cloud.google.com/discover/what-is-model-context-protocol) to provide standardized tools and data resources to AI agents.

## MCP server identifier

A globally unique, immutable Uniform Resource Name (URN) for an MCP server. Similar to agent identifiers, this URN provides a stable reference for discovering specific toolsets.

MCP server identifiers are logical names used for registry lookup and inventory management. For more information, see [MCP server identifiers](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#mcp-server-identifiers).

## Registration

The process of adding an agentic component, such as an agent, MCP server, or endpoint, to the registry. Agent Registry provides the following registration mechanisms:

  * **Automatic registration** : Automatic ingestion of supported Google Cloud AI resources, such as in Agent Runtime. Automatic registration operates within the scope of a single project.
  * **Manual registration** : Manual onboarding of custom or external agentic components, or agents deployed across multiple Google Cloud projects for centralized discovery and governance.



## Runtime reference

The physical runtime location or compute infrastructure hosting an agent, MCP server, or endpoint, represented in the Agent Registry API by the `agentregistry.googleapis.com/system/RuntimeReference` attribute. For example, a runtime reference can point to a Agent Runtime reasoning engine, a GKE deployment, or a Cloud Run service.

The runtime reference path is embedded within the agent principal for IAM policy evaluation. For more information, see [Runtime references](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#runtime-references).

## Service

For the Agent Registry API, the writable resource used to manually register custom or external agentic components into the registry. A `Service` represents an agent, an MCP server, or an endpoint that is manually added to your registry. You create and manage a `Service` resource to define the endpoint and metadata for agentic components that Agent Registry doesn't automatically ingest.

Depending on the specification you provide, Agent Registry automatically projects this `Service` onto the consumer side as a read-only `Agent`, `McpServer`, or `Endpoint` resource for discovery.

You always use the `Service` resource to create, edit, or delete registry entries. However, to get, list, or search for those entries, you query the read-only `Agent`, `McpServer`, or `Endpoint` resources.

## Skill

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

_Compare withA2A skills._

A standalone package registered as a top-level resource in Agent Registry that extends the capabilities of an agent by providing specific instructions and optional scripts to complete a task. Skills contain instruction files (`SKILL.md`), optional scripts, and metadata assets.

Skills are identified by a Uniform Resource Name (URN). The exact format depends on the publisher. The following are examples:

  * **Google-created skills** : `urn:skill:PUBLISHER_ID:NAMESPACE:SKILL_ID`. For example: `urn:skill:discoveryengine.googleapis.com:discoveryengine:report-writing`.
  * **Manually registered skills** : `urn:skill:projects-PROJECT_NUMBER:locations:LOCATION:private-SKILL_ID`. For example: `urn:skill:projects-123456789:locations:global:private-create-docs`.



Google-created skills are visible immediately when you set up Agent Registry. However, you can also [register your own skills](https://docs.cloud.google.com/agent-registry/register-skills). You register skills in Agent Registry as sibling resources to agents and MCP servers. Each skill has a default revision and can contain multiple versioned skill revisions.

Platform administrators govern skills by [managing their lifecycle states](https://docs.cloud.google.com/agent-registry/manage-skills#lifecycle) and [setting default version pointers](https://docs.cloud.google.com/agent-registry/manage-skills#update-skill) for runtime resolution.

## Skill revision

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

An immutable, versioned snapshot of a skill package. Revisions let you update skill instructions or scripts without changing the parent skill's identifier.

You can [manage skill revisions](https://docs.cloud.google.com/agent-registry/manage-skill-revisions) to allow for version control of your skills.

## Publisher

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

An entity that creates and registers skills in Agent Registry.

Prepopulated publishers include Google publishers, such as `cloud.google.com` and `discoveryengine.googleapis.com`, and verified partners. Google-created skills from these publishers are visible immediately when you set up Agent Registry.

The skills that you create are automatically assigned to the default `private` publisher, so the published ID of a particular skill is prefixed with `private-`. You can't register custom publisher resources.

Review and inspect [publisher details](https://docs.cloud.google.com/agent-registry/review-publishers) for your registered skills.

## Tool

A deterministic function provided by an MCP server that an agent can invoke.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
