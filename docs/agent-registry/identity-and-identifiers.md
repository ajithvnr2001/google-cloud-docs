---
url: https://docs.cloud.google.com/agent-registry/identity-and-identifiers/
title: Identity and identifiers \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:14.375217+00:00
---

# Identity and identifiers  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/identity-and-identifiers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Identity and identifiers Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry assigns distinct identifiers and identities to your registered agents, MCP servers, endpoints, and skills so that you can discover capabilities, enforce access policies, and route runtime traffic. Understanding how each identifier layer works helps you configure search queries, security policies, and network routes across your AI ecosystem.

## Architectural layers

Agent Registry uses four distinct layers to identify, govern, and route registered components:

  * **Registry identifiers** : logical, immutable Uniform Resource Names (URNs), including agent identifiers, MCP server identifiers, endpoint identifiers, and skill identifiers, used for searching, registry discovery, and filtering. These URNs aren't used for runtime governance.
  * **Resource names** : standard, globally unique Google Cloud [resource names](https://docs.cloud.google.com/apis/design/resource_names) that Agent Registry assigns to `Service`, `Agent`, `McpServer`, `Endpoint`, and `Skill` resources. Downstream services, such as Agent Gateway route rules, Identity-Aware Proxy (IAP) egress policies, and Identity and Access Management (IAM) policy bindings, use the resource names of `Agent`, `McpServer`, `Endpoint`, and `Skill` resources to enforce governance policies.
  * **Agent principals** : verifiable IAM identities, such as [SPIFFE IDs](https://spiffe.io/) for agents running on Google Cloud or service accounts for external agents, used for caller authentication, authorization, and audit logging.
  * **Runtime references** : compute or infrastructure paths stored in the `RuntimeReference` message and used for topology queries and egress traffic matching.



The following table compares each layer, its primary purpose, downstream governance role, and syntax:

Layer | Primary purpose | Governance role | Syntax  
---|---|---|---  
**Registry identifiers** | Stable registry discovery, metadata tagging, and search. | Immutable and not used for governance. | 

  * **Agent identifier** : `urn:agent:IDENTIFIER`
  * **MCP server identifier** : `urn:mcp:IDENTIFIER`
  * **Endpoint identifier** : `urn:endpoint:IDENTIFIER`
  * **Skill identifier** : `urn:skill:IDENTIFIER`

  
**Resource names** | Target resource identification for policy enforcement. | Required by policies and used by Agent Gateway routes and IAP bindings. | 

  * **Agent** : `projects/PROJECT_NUMBER/locations/LOCATION/agents/agentregistry-ID`
  * **MCP server** : `projects/PROJECT_NUMBER/locations/LOCATION/mcpServers/agentregistry-ID`
  * **Endpoint** : `projects/PROJECT_NUMBER/locations/LOCATION/endpoints/agentregistry-ID`
  * **Skill** : `projects/PROJECT_NUMBER/locations/LOCATION/skills/SKILL_ID`

  
**Agent principals** | Caller authentication, authorization, and audit logging. | Enforced by IAM. | 

  * `principal://PRINCIPAL_PATH`
  * `principalSet://PRINCIPAL_SET_PATH`

  
**Runtime references** | Physical compute routing and outbound traffic matching. | Evaluated in topology queries and in Agent Gateway to match network traffic. |  `agentregistry.googleapis.com/system/RuntimeReference` containing the compute or infrastructure path as `uri: "RUNTIME_URI"`  
  
## Registry identifiers

A registry identifier is a globally unique, immutable Uniform Resource Name (URN) that Agent Registry assigns to a registered component. This URN provides a stable reference for consumers and orchestrator agents to discover, filter, and search components in Agent Registry, remaining constant regardless of underlying infrastructure migrations or code updates.

Registry identifiers are logical URNs used exclusively for registry discovery and metadata annotation. They differ from agent principals and resource names, and can't be used in IAM policy bindings, authorization headers, or Agent Gateway route rules.

Agent Registry uses four types of registry identifiers:

  * Agent identifiers (`agentId`)
  * MCP server identifiers (`mcpServerId`)
  * Endpoint identifiers (`endpointId`)
  * Skill identifiers (`skillId`)



### Agent identifiers

Agent Registry assigns an agent identifier (`agentId`) to all registered agents, including built-in Google agents and custom or external agents. Agent identifiers are only used to discover and filter agents in Agent Registry, not in IAM policies. To grant or restrict an agent's access in IAM policies, use its agent principal.

Agent Registry automatically generates agent identifiers during ingestion. The exact URN structure depends on the compute environment where the agent is deployed:

  * **Agent Runtime on Gemini Enterprise Agent Platform** : `urn:agent:projects-PROJECT_NUMBER:projects:PROJECT_NUMBER:locations:REGION:aiplatform:reasoningEngines:AGENT_ID`
  * **Cloud Run services** : `urn:agent:projects-PROJECT_NUMBER:projects:PROJECT_NUMBER:locations:REGION:run:services:SERVICE_NAME`
  * **Cloud Run jobs** : `urn:agent:projects-PROJECT_NUMBER:projects:PROJECT_NUMBER:locations:REGION:run:jobs:JOB_NAME`
  * **Google Kubernetes Engine (GKE) deployments** : `urn:agent:projects-PROJECT_NUMBER:projects:PROJECT_NUMBER:locations:REGION:container:clusters:CLUSTER_NAME:k8s:namespaces:NAMESPACE:apps:deployments:DEPLOYMENT_NAME`
  * **Gemini Enterprise** : `urn:agent:projects-PROJECT_NUMBER:projects:PROJECT_NUMBER:locations:global:discoveryengine:collections:default_collection:engines:ENGINE_ID:assistants:default_assistant:agents:AGENT_ID`
  * **Google Workspace** : `urn:agent:googleapis.com:locations:global:workspaceagent:workspaceagent--a2a`
  * **Manually registered agents** : `urn:agent:projects-PROJECT_NUMBER:projects:PROJECT_NUMBER:locations:LOCATION:agentregistry:services:AGENT_ID`



### MCP server identifiers

An MCP server identifier (`mcpServerId`) is a registry identifier used to discover an MCP server and its tools in Agent Registry.

MCP servers only respond to requests and don't have an IAM principal. When an agent invokes tools on an MCP server, access is authorized using the calling agent principal.

The following are the URN formats for MCP server identifiers:

  * **Google and Google Cloud remote MCP servers** : `urn:mcp:googleapis.com:projects:PROJECT_NUMBER:locations:global:SERVER_ID`
  * **Cloud Run services** : `urn:mcp:projects-PROJECT_NUMBER:projects:PROJECT_NUMBER:locations:REGION:run:services:SERVICE_NAME`
  * **GKE deployments** : `urn:mcp:projects-PROJECT_NUMBER:projects:PROJECT_NUMBER:locations:REGION:container:clusters:CLUSTER_NAME:k8s:namespaces:NAMESPACE:apps:deployments:DEPLOYMENT_NAME`
  * **Manually registered MCP servers** : `urn:mcp:projects-PROJECT_NUMBER:projects:PROJECT_NUMBER:locations:LOCATION:agentregistry:services:SERVER_ID`



### Endpoint identifiers

An endpoint identifier (`endpointId`) is a registry identifier assigned to a [registered endpoint](https://docs.cloud.google.com/agent-registry/register-endpoints) for discovering target API destinations.

The URN format for manually registered endpoints is `urn:endpoint:projects-PROJECT_NUMBER:projects:PROJECT_NUMBER:locations:LOCATION:agentregistry:services:ENDPOINT_ID`.

### Skill identifiers

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A skill identifier (`skillId`) is a registry identifier assigned to a standalone [skill](https://docs.cloud.google.com/agent-registry/skills-architecture) for discovering and resolving skill packages in Agent Registry.

The following are the URN formats for skill identifiers, which depend on the skill's [publisher](https://docs.cloud.google.com/agent-registry/skills-architecture#publishers):

  * **Google-managed publishers** : `urn:skill:PUBLISHER_ID:NAMESPACE:SKILL_ID`
  * **Private publishers** : `urn:skill:projects-PROJECT_NUMBER:locations:LOCATION:private-SKILL_ID`



## Resource names

Whether a component is registered automatically or manually, Agent Registry assigns a standard Google Cloud [resource name](https://docs.cloud.google.com/apis/design/resource_names) to the resulting read-only `Agent`, `McpServer`, or `Endpoint` discovery resource, or `Skill` resource. Each resource name is formatted as a hierarchical URI path in your [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project):

  * **Agents** : `projects/PROJECT_NUMBER/locations/LOCATION/agents/agentregistry-ID`
  * **MCP servers** : `projects/PROJECT_NUMBER/locations/LOCATION/mcpServers/agentregistry-ID`
  * **Endpoints** : `projects/PROJECT_NUMBER/locations/LOCATION/endpoints/agentregistry-ID`
  * **Skills** : `projects/PROJECT_NUMBER/locations/LOCATION/skills/SKILL_ID`

For manually registered skills, `SKILL_ID` includes the `private-` prefix, such as `private-SKILL_ID`.

Each versioned [skill revision](https://docs.cloud.google.com/agent-registry/skills-architecture#skill-revision) uses `projects/PROJECT_NUMBER/locations/LOCATION/skills/SKILL_ID/revisions/REVISION_ID`.




When you [manually register](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery#registration-models) an agent, an MCP server, or an endpoint, you create a writable `Service` resource that generates the corresponding read-only `Agent`, `McpServer`, or `Endpoint` resource. The `Service` resource has its own resource name:

`projects/PROJECT_NUMBER/locations/LOCATION/services/SERVICE_ID`

You can query both read-only and writable resources to view their resource names. When you query a `Service` resource in a terminal by using, for example, the [`gcloud agent-registry services describe`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/services/describe) command, the output also displays a `registryResource` field, which shows the resource name of the corresponding read-only `Agent`, `McpServer`, or `Endpoint` resource. For more information, see [Manage agents](https://docs.cloud.google.com/agent-registry/manage-agents#view-details), [Manage MCP servers and tools](https://docs.cloud.google.com/agent-registry/manage-mcp-tools#view-details), [Manage and discover endpoints](https://docs.cloud.google.com/agent-registry/manage-endpoints#view-details), and [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills#list-view).

Resource names can be used to bind policies, route network traffic, and configure access controls. Downstream governance surfaces, including Agent Gateway route rules, IAP egress policies, and IAM resource policies, evaluate against this resource name. Don't use registry identifier URNs in policy bindings or route rules. Use resource names instead. For troubleshooting information, see [Resource entity not found error when managing IAP policies](https://docs.cloud.google.com/agent-registry/troubleshooting#resource-entity-not-found).

## Agent principals

An agent principal is an agent's identity in IAM. Grant roles to an agent principal in the same way you would to a user or service account to grant or restrict access.

In Agent Registry, how an agent is identified as a principal depends on where it runs:

  * **Agents running on Google Cloud infrastructure** : for managed runtimes such as Agent Runtime, Google Cloud automatically provisions a managed workload identity formatted as a [SPIFFE ID](https://spiffe.io/), which is bound directly to the agent's compute runtime. When referencing this identity in IAM allow policies and bindings, you must use the IAM principal or principal set string format rather than the SPIFFE URI scheme. Using a SPIFFE string for an IAM policy binding returns an `INVALID_ARGUMENT` error.
  * **Agents running outside Google Cloud** : external or on-premises agents must federate their external identity through [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) or use a standard service account to interact with Google Cloud resources. After authentication, that federated workload identity string or service account email acts as the agent principal in IAM policies.



For agents running on Google Cloud, because the managed agent principal is bound directly to the compute resource of the agent's runtime, the principal string incorporates the full path to that underlying compute resource.

IAM supports governing agent access across the following scopes:

  * **Single engine instance** : grants permissions to a specific agent deployment. For example, an individual Agent Runtime instance is represented through a single principal string: `principal://agents.global.org-ORGANIZATION_ID.system.id.goog/resources/aiplatform/projects/PROJECT_NUMBER/locations/REGION/reasoningEngines/REASONING_ENGINE_ID`
  * **Project scope** : grants permissions to all reasoning engines running inside a specific project through a principal set: `principalSet://agents.global.org-ORGANIZATION_ID.system.id.goog/attribute.platformContainer/aiplatform/projects/PROJECT_NUMBER`
  * **Organization-wide scope** : grants permissions to all agents across the entire organization through a principal set wildcard: `principalSet://agents.global.org-ORGANIZATION_ID.system.id.goog/*`



Agent Registry displays the individual agent principal as an output-only attribute when you [view the details of an agent](https://docs.cloud.google.com/agent-registry/manage-agents#view-details).

## Runtime references

A runtime reference points to the underlying compute infrastructure where the code for an agent, MCP server, or endpoint runs. For example, a runtime reference can point to an Agent Runtime reasoning engine, a GKE deployment, or a Cloud Run service.

An agent's principal string includes its runtime reference path, which ties IAM permissions directly to where the agent runs. If you register an agent in a [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) that is different from where it is deployed, the runtime reference points to the project hosting the underlying workload.

In Agent Registry, the runtime reference is represented by the `agentregistry.googleapis.com/system/RuntimeReference` attribute, which contains the compute or infrastructure path in its `uri` field. You can view this output-only attribute as part of the agent details or use it to query traffic flows and relationships in the [topology graph](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology#registered-agent).

## What's next

  * Learn about [Roles and permissions](https://docs.cloud.google.com/agent-registry/roles-permissions).
  * [Manage agents](https://docs.cloud.google.com/agent-registry/manage-agents).
  * Understand the [Agent Registry data model](https://docs.cloud.google.com/agent-registry/data-model).
  * Explore general [Key concepts](https://docs.cloud.google.com/agent-registry/concepts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
