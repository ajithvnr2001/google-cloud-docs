---
url: https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery/
title: Component lifecycle and discovery \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:30.388745+00:00
---

# Component lifecycle and discovery  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Component lifecycle and discovery Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry lets you register, discover, and connect modular agentic components so that developers and orchestrator agents can find and reuse AI capabilities across your organization. Understanding how Agent Registry represents components across automatic and manual registration helps you discover capabilities and connect them using bindings and auth providers.

## AI ecosystem

You can register, discover, and govern four types of modular agentic components to integrate your AI ecosystem:

  * **Agents** : autonomous AI actors that plan, reason, invoke tools, and collaborate with other agents.
  * **MCP servers** : programs that implement the [Model Context Protocol (MCP)](https://docs.cloud.google.com/mcp/overview#how-mcp-works) to expose standardized tools and data resources.
  * **Endpoints** : target URLs, typically REST APIs, accessed by agents.
  * **[Skills](https://docs.cloud.google.com/agent-registry/skills-architecture)** : standalone packages of instructions and optional scripts, or inline [A2A skills](https://docs.cloud.google.com/agent-registry/skills-architecture#standalone-vs-a2a), that extend an agent's capabilities.



## Agentic component representation in Agent Registry

In Agent Registry, you can register agentic components through automatic or manual registration. How Agent Registry represents a component depends on its component type and registration model.

### Agents, MCP servers, and endpoints

Regardless of how an agent, MCP server, or endpoint is registered, Agent Registry represents it as a read-only `Agent`, `McpServer`, or `Endpoint` discovery resource with a standard [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names). Consumers of agentic components, such as orchestrator agents, client applications, and developers, use the discovery resources to list, search, and view all available components across the registry.

How Agent Registry creates and updates these discovery resources depends on how the component is registered:

  * **Automatic registration** : Agent Registry ingests metadata directly from supported runtimes, and automatically creates and updates the corresponding `Agent` or `McpServer` discovery resource. Automatically registered components don't have a `Service` resource in Agent Registry. Instead, Agent Registry synchronizes changes when you update or delete the underlying deployment or workload in its runtime.
  * **Manual registration** : when you manually register or update a component, Agent Registry creates or updates two resources: 
    * A writable `Service` resource, identified by its own [resource name](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#resource-names). You use this resource to update or unregister a component. Modifying or deleting the `Service` resource only changes its entry in Agent Registry, and doesn't modify or delete the underlying deployment.
    * A read-only discovery resource for the type of agentic component, which is automatically created and updated based on the metadata for the `Service` resource: 
      * **`Agent` resource**: the read-only discovery resource that orchestrator agents, client applications, and developers read to find and invoke agents.
      * **`McpServer` resource**: the read-only discovery resource that exposes an MCP server's standardized tools and data resources.
      * **`Endpoint` resource**: the read-only discovery resource for external URLs and REST APIs accessed by your agents.



For details on how `Service` resource specification flags map to read-only resource collections, see [Service resources and discovery resources](https://docs.cloud.google.com/agent-registry/data-model#service-resources).

### Standalone skills

Unlike agents, MCP servers, and endpoints, standalone [skills](https://docs.cloud.google.com/agent-registry/skills-architecture) don't use separate `Service` resources and read-only discovery resources. Instead, Agent Registry represents each skill using a top-level `Skill` resource for both management and discovery, along with child `SkillRevision` resources for immutable versioned snapshots and a `Publisher` resource for ownership scoping:

  * **Automatic registration** : Google-managed skills are automatically available as `Skill` and `SkillRevision` resources across all projects.
  * **Manual registration** : when you register or update a private standalone skill, you create or update the `Skill` resource and upload immutable `SkillRevision` resources directly in Agent Registry. Consumers list, search, and retrieve skills using those same `Skill` and `SkillRevision` resources.



## Registration models

Agent Registry supports two models for registering agentic components:

Characteristic | Automatic registration | Manual registration  
---|---|---  
**Scope** | Deployed components are scoped to a single project. Built-in Google agents, Google and Google Cloud remote MCP servers, and Google-managed skills are available across projects. | Scoped to a single project or centralized across multiple projects.  
**Configuration** | Agent Runtime on Gemini Enterprise Agent Platform, built-in Google agents, Google and Google Cloud remote MCP servers, and Google-managed skills register automatically. Google Kubernetes Engine (GKE) and Cloud Run workloads require an opt-in deployment label or flag. | Requires creating a `Service` or `Skill` resource in Agent Registry.  
**Runtimes** | Agent Runtime, GKE, Cloud Run, and Google-managed runtimes. | Compute Engine, GKE, Cloud Run, on-premises systems, and external cloud platforms.  
**Target components** | Agents, MCP servers, and Google-managed standalone skills. | Custom or external agents, MCP servers, endpoints, and private standalone skills.  
**Metadata updates** | Synchronized automatically from the runtime environment or Agent Card endpoints. | Requires manual updates by modifying the `Service` resource or uploading a new `SkillRevision` resource in Agent Registry.  
  
### Automatic registration

Automatic registration ingests agents, MCP servers, and Google-managed standalone skills from supported Google Cloud runtimes without requiring you to manually create resources in Agent Registry. Agents deployed to Agent Runtime, built-in Google agents from Google Workspace and Gemini Enterprise, Google and Google Cloud remote MCP servers, and Google-managed standalone skills are registered automatically. For GKE deployments and Cloud Run workloads, you enable automatic registration by adding a functional type label or flag when you deploy the agent or MCP server.

During automatic registration, Agent Registry extracts the component's endpoints, [registry identifiers](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#registry-identifiers), [runtime references](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#runtime-references), and advertised A2A skills or MCP tools into its discovery resource in Agent Registry.

For more information about configuring automatic registration, see [Use automatic registration for agents](https://docs.cloud.google.com/agent-registry/automatic-registration) and [Register MCP servers](https://docs.cloud.google.com/agent-registry/register-mcp-servers).

### Manual registration

Manual registration lets you register remote or custom agents, MCP servers, endpoints, and private standalone skills by creating resources directly in Agent Registry. You can manually register agents, MCP servers, or REST API endpoints hosted on Compute Engine, GKE, Cloud Run, on-premises infrastructure, or external cloud platforms, including agents that don't implement the A2A protocol. Manual registration also lets you register remote components deployed in separate Google Cloud projects into a central [governance project's](https://docs.cloud.google.com/agent-registry/overview#governance-project) registry for centralized discovery and governance.

To manually register an agent, MCP server, or endpoint, you create a `Service` resource in Agent Registry and specify the component's interface URL, protocol binding, and the `--agent-spec-type`, `--mcp-server-spec-type`, or `--endpoint-spec-type` specification flag. To manually register a standalone skill, you create a `Skill` resource with a ZIP archive payload.

For more information about configuring manual registration, see [Use manual registration for agents](https://docs.cloud.google.com/agent-registry/manual-registration), [Register endpoints](https://docs.cloud.google.com/agent-registry/register-endpoints), and [Register skills](https://docs.cloud.google.com/agent-registry/register-skills).

## Discovery types

In Google Cloud, discovery in Agent Registry differs from discovery in infrastructure management tools:

  * **Consumption discovery** : Agent Registry focuses on finding registered agents, MCP tools, endpoints, and skills that orchestrators can invoke at runtime. Developers and agents query Agent Registry using natural language search, tags, or [registry identifiers](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#registry-identifiers) to locate capabilities needed to complete workflows.
  * **Infrastructure discovery** : services like [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) focus on detecting physical compute resources, such as virtual machines, GKE services, and Cloud Run deployments, across your Google Cloud projects. App Hub organizes these compute assets into applications and environments for infrastructure health, resource monitoring, and reliability tracking.



Infrastructure discovery tracks where workloads run, whereas consumption discovery in Agent Registry identifies what capabilities an agent or tool provides.

## Component relationships

To compose multi-agent workflows and manage outbound credentials, you create explicit relationships between components using bindings and auth providers.

### Bindings

A binding defines a directed connection between a source agent and a target resource using their [registry identifiers](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#registry-identifiers) (URNs):

  * **Agent-to-agent bindings** : establish delegation pathways that let an orchestrator agent invoke specialist subagents.
  * **Agent-to-MCP server bindings** : connect an agent to an MCP server, associating the agent with the server's published tools and data resources.
  * **Agent-to-endpoint bindings** : connect an agent to a registered external endpoint, such as a REST API.



Bindings provide visibility into your multi-agent topology, helping teams audit which agents interact with downstream capabilities. For instructions on creating and managing bindings, see [Manage bindings](https://docs.cloud.google.com/agent-registry/manage-bindings).

### Auth providers

When an agent interacts with external tools, MCP servers, or APIs, it often requires dedicated credentials. An auth provider is a configuration in [Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/agent-identity-overview#agent-auth-manager) that stores, acquires, and manages credentials, such as OAuth tokens or API keys, on behalf of the agent.

By associating a binding with an auth provider, you let the agent authenticate to external destinations without embedding secrets in prompt templates or agent source code. For more information, see [Authenticate to tools and resources](https://docs.cloud.google.com/agent-registry/authenticate-toolsets).

## What's next

  * Learn about [Identity and identifiers](https://docs.cloud.google.com/agent-registry/identity-and-identifiers).
  * Learn about [Skills architecture](https://docs.cloud.google.com/agent-registry/skills-architecture).
  * [Register agents](https://docs.cloud.google.com/agent-registry/register-agents).
  * [Use automatic registration for agents](https://docs.cloud.google.com/agent-registry/automatic-registration).
  * [Use manual registration for agents](https://docs.cloud.google.com/agent-registry/manual-registration).
  * [Manage bindings](https://docs.cloud.google.com/agent-registry/manage-bindings).
  * Explore [Key concepts](https://docs.cloud.google.com/agent-registry/concepts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
