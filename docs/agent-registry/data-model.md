---
url: https://docs.cloud.google.com/agent-registry/data-model/
title: Agent Registry data model \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:14.151371+00:00
---

# Agent Registry data model  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/data-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Agent Registry data model Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry organizes your AI ecosystem into standardized resources so that you can register, discover, and govern agents, MCP servers, endpoints, and skills. Understanding how Agent Registry separates writable `Service` resources from read-only discovery resources, and which products support automatic and manual registration, helps you design and govern your registry.

## Agentic components

Agent Registry lets you register, discover, and govern the following types of agentic components:

  * **Agents** : autonomous AI actors that carry out specific tasks, invoke tools, and collaborate with other agents.
  * **MCP servers** : programs that implement the [Model Context Protocol (MCP)](https://docs.cloud.google.com/mcp/overview#how-mcp-works) to expose standardized data resources and tools. Tools are deterministic functions exposed by an MCP server that agents can invoke to perform specific actions.
  * **Endpoints** : target URLs, typically REST APIs, accessed by an agent. By abstracting these destinations into manageable resources, Agent Registry lets you centrally govern which external APIs your agents can access.
  * **Skills** : modular capabilities that extend what an agent can do. Standalone skills are packages of instructions and optional scripts governed directly in the registry. A2A skills are capability descriptions on an agent's Agent Card that tell other agents when and how to communicate with it. For more information, see [Skills architecture](https://docs.cloud.google.com/agent-registry/skills-architecture).



## Service resources and discovery resources

How Agent Registry represents a component depends on its component type and registration model. For more information about component lifecycles and discovery, see [Component lifecycle and discovery](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery).

### Agents, MCP servers, and endpoints

Regardless of whether an agent, an MCP server, or an endpoint is registered automatically or manually, Agent Registry represents it as a read-only `Agent`, `McpServer`, or `Endpoint` discovery resource. Consumers, such as orchestrator agents, client applications, and developers, use these discovery resources to list, search, and view registered components.

For automatically registered components, Agent Registry ingests metadata directly from supported runtimes and creates the discovery resource without a `Service` resource.

When you manually register an agent, an MCP server, or an endpoint, Agent Registry separates management operations from component discovery by creating the following items:

  * **A writable`Service` resource**: stores the component's metadata, including the type of agentic component, its interface URL, description, protocol binding, and capability specification. You create, update, or delete the `Service` resource for management operations such as updating metadata or unregistering the component, without modifying or deleting the underlying deployment.
  * **A discovery resource** : when you create or update a `Service` resource, Agent Registry reads the metadata and automatically creates or updates an `Agent`, `McpServer`, or `Endpoint` discovery resource that represents the component in your registry.



The specification flags you use when creating a `Service` resource determine the resulting read-only resource collection:

Flags | Resource collection | Use case | Valid values  
---|---|---|---  
`--agent-spec-type`  
`--agent-spec-content` | `Agent` resource in `agents` collection | Remote A2A-compliant or standard REST agents | `a2a-agent-card`, `no-spec`  
`--endpoint-spec-type`  
`--endpoint-spec-content` | `Endpoint` resource in `endpoints` collection | External target REST APIs or service URLs | `no-spec`  
`--mcp-server-spec-type`  
`--mcp-server-spec-content` | `McpServer` resource in `mcp-servers` collection | External Model Context Protocol (MCP) servers | `tool-spec`, `no-spec`  
  
These flag pairs are mutually exclusive; specifying flags from more than one pair returns an error. If you specify the flag pair for the wrong component type, Agent Registry creates the discovery resource in the collection that matches the flag you specified. For example, passing `--agent-spec-type=no-spec` when registering an endpoint creates an `Agent` resource instead of an `Endpoint` resource, so type-specific queries and governance policies won't apply as expected.

### Standalone skills

Standalone [skills](https://docs.cloud.google.com/agent-registry/skills-architecture) don't use separate `Service` resources. Instead, you register, version, and query skills directly using top-level `Skill` resources, child `SkillRevision` resources, and `Publisher` resources.

To get started, see [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup). For more information about the Agent Registry API, see the [API reference documentation](https://docs.cloud.google.com/agent-registry/apis).

## Supported products and components

Agent Registry categorizes supported products and components by how they are registered: automatically or manually.

### Automatic registration

Agent Registry automatically discovers and ingests supported Google Cloud workloads deployed within your project. For agents that implement the open Agent2Agent (A2A) protocol, the registry automatically extracts their A2A skills and capabilities from their Agent Card. Google-managed standalone skills are also discoverable across all projects when you set up Agent Registry.

The following table lists the products and components that Agent Registry registers automatically:

Component type | Supported products  
---|---  
**Agents** | 

  * [ Agent Runtime on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/agent-registry/automatic-registration#agent-engine)
  * [ Google Workspace](https://docs.cloud.google.com/agent-registry/automatic-registration#built-in-agents)
  * [ Gemini Enterprise](https://docs.cloud.google.com/agent-registry/automatic-registration#built-in-agents)
  * [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/agent-registry/automatic-registration#gke) deployments including a specific functional type label
  * [Cloud Run](https://docs.cloud.google.com/agent-registry/automatic-registration#cloud-run) workloads configured with a specific functional type flag

  
**MCP servers** | 

  * [ Google and Google Cloud remote MCP servers](https://docs.cloud.google.com/mcp/supported-products)
  * [GKE](https://docs.cloud.google.com/agent-registry/register-mcp-servers#gke-mcp) deployments including a specific functional type label
  * [Cloud Run](https://docs.cloud.google.com/agent-registry/register-mcp-servers#cloud-run-mcp) services configured with a specific functional type flag

  
**Skills** | [ Google-managed skills](https://github.com/google/skills/tree/main) are discoverable from all projects  
  
### Manual registration

For _remote_ components, which are agents, MCP servers, or endpoints hosted outside your [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) in separate Google Cloud projects, on-premises infrastructure, or external clouds, you manually register components in the governance project using a `Service` resource. You also use a `Service` resource to manually register components on unsupported runtimes or agents that don't implement the A2A protocol. For custom standalone skills, you use a `Skill` resource.

The following table lists the products and components that you register manually:

Component type | Supported resources  
---|---  
**Agents** | [ Remote agents](https://docs.cloud.google.com/agent-registry/manual-registration) deployed on Compute Engine, GKE, Cloud Run, on-premises systems, or external clouds  
**MCP servers** | [ Custom agentic components on unsupported runtimes or external MCP servers](https://docs.cloud.google.com/agent-registry/register-mcp-servers#register-external-servers)  
**Endpoints** | External target REST APIs or service URLs governed as endpoints  
**Skills** | [ Your own standalone skills](https://docs.cloud.google.com/agent-registry/register-skills) authored by your organization  
  
## What's next

  * Review [Key concepts](https://docs.cloud.google.com/agent-registry/concepts) to familiarize yourself with the essential terms used in Agent Registry.
  * Learn about [Identity and identifiers](https://docs.cloud.google.com/agent-registry/identity-and-identifiers).
  * Learn about [Component lifecycle and discovery](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery).
  * Learn about [Skills architecture](https://docs.cloud.google.com/agent-registry/skills-architecture).
  * [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).
  * Learn about the difference between [automatic and manual registration](https://docs.cloud.google.com/agent-registry/register-agents).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
