---
url: https://docs.cloud.google.com/agent-registry/data-model/
title: Agent Registry data model \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:10.230554+00:00
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

Agent Registry categorizes [agentic components](https://docs.cloud.google.com/agent-registry/concepts#agentic-component) of your ecosystem into four main resource types that you can manage and discover:

  * **Agents** : Autonomous AI actors that carry out specific tasks, invoke tools, and collaborate with other agents.
  * **MCP servers** : Providers of standardized data resources and [tools](https://docs.cloud.google.com/agent-registry/concepts#tool). Tools are deterministic functions exposed by an MCP server that agents can invoke to perform specific actions.
  * **Endpoints** : Target URLs, typically REST APIs, accessed by an agent. By abstracting these destinations into manageable resources, Agent Registry lets you centrally govern which external APIs your agents can access.
  * **Skills** : Modular capabilities that extend what an agent can do. Agent Registry distinguishes between standalone skills, which are packages of instructions and optional scripts governed directly in the registry, and [A2A skills](https://docs.cloud.google.com/agent-registry/concepts#a2a-skill), which are capability descriptions listed on an agent's Agent Card that tell other agents when and how to communicate with it.



For more information about these and other concepts that Agent Registry uses, see [Key concepts](https://docs.cloud.google.com/agent-registry/concepts).

### API resources

The Agent Registry API separates read and write operations for agents, endpoints, and MCP servers:

  * **Writable API resource** : You manage these agentic components by manually creating, updating, or deleting a `Service` resource in the registry.
  * **Read-only API resource** : To query, list, or search for these agentic components, you request the read-only `Agent`, `McpServer`, or `Endpoint` resource to the Agent Registry API.



The specification flags you use when creating a `Service` determine the resulting read-only resource collection:

Flags | Resource collection | Use case | Valid values  
---|---|---|---  
`--agent-spec-type`  
`--agent-spec-content` | `Agent` (`agents`) | Remote agents (A2A-compliant or standard REST agents) | `a2a-agent-card`, `no-spec`  
`--endpoint-spec-type`  
`--endpoint-spec-content` | `Endpoint` (`endpoints`) | External target REST APIs or service URLs | `no-spec`  
`--mcp-server-spec-type`  
`--mcp-server-spec-content` | `McpServer` (`mcp-servers`) | External Model Context Protocol (MCP) servers | `tool-spec`  
  
These flag pairs are mutually exclusive. If you specify invalid flags, your resource is created in the incorrect collection and might not work with type-specific policies.

Standalone [skills](https://docs.cloud.google.com/agent-registry/concepts#skill) don't use the `Service` projection model. Instead, you manage, version-control, and list skills directly using the `Skill`, `SkillRevision`, and `Publisher` API resources.

To get started, see [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup). For more information about the Agent Registry API, see the [API reference documentation](https://docs.cloud.google.com/agent-registry/apis).

## Supported products and components

Agent Registry categorizes supported products and components by how they are registered: automatically or manually.

### Automatic registration

Agent Registry automatically discovers and ingests supported Google Cloud workloads deployed within your project. For agents that implement the open Agent2Agent (A2A) protocol, the registry automatically extracts their A2A skills and capabilities from their Agent Card. Google-created standalone skills are also globally discoverable when you set up Agent Registry.

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

  * [ Official Google and Google Cloud remote MCP servers](https://docs.cloud.google.com/mcp/supported-products)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/agent-registry/register-mcp-servers#gke-mcp) deployments including a specific functional type label
  * [Cloud Run](https://docs.cloud.google.com/agent-registry/register-mcp-servers#cloud-run-mcp) services configured with a specific functional type flag

  
**Skills** | [ Google's public skills](https://github.com/google/skills/tree/main) are globally discoverable from all projects  
  
### Manual registration

For custom workloads, external cloud runtimes, on-premises infrastructure, or agents that don't implement the A2A protocol, you manually register components using the writable `Service` resource. For custom standalone skills, you use the `Skill` resource.

The following table lists the products and components that you register manually:

Component type | Supported resources  
---|---  
**Agents** | [ Remote agents](https://docs.cloud.google.com/agent-registry/manual-registration) deployed on Compute Engine, Google Kubernetes Engine, Cloud Run, on-premises systems, or external clouds  
**MCP servers** | [ Custom agentic components on unsupported runtimes or external MCP servers](https://docs.cloud.google.com/agent-registry/register-mcp-servers#register-external-servers)  
**Endpoints** | External target REST APIs or service URLs governed as endpoints  
**Skills** | [ Your own standalone skills](https://docs.cloud.google.com/agent-registry/register-skills) authored by your organization  
  
## What's next

  * Review [Key concepts](https://docs.cloud.google.com/agent-registry/concepts) to familiarize yourself with the essential terms used in Agent Registry.
  * Learn about [Identity and identifiers](https://docs.cloud.google.com/agent-registry/identity-and-identifiers).
  * [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).
  * Learn about the difference between [automatic and manual registration](https://docs.cloud.google.com/agent-registry/register-agents).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
