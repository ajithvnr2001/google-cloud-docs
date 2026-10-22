---
url: https://docs.cloud.google.com/agent-registry/roles-permissions/
title: Roles and permissions \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:19.804076+00:00
---

# Roles and permissions  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/roles-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Agent Registry.

Grant appropriate Agent Registry IAM roles to users or groups who manage or view agents, MCP servers, tools, standalone skills, endpoints, and bindings in the registry. To grant roles, you can use the IAM page in the Google Cloud console or the Google Cloud CLI. For detailed instructions, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Agent Registry roles

The following table describes Agent Registry IAM roles and their typical responsibilities:

**Caution:** Only grant **Agent Registry API Admin** (`roles/agentregistry.admin`) or **Agent Registry API Editor** (`roles/agentregistry.editor`) roles to trusted administrators who require permissions to manage the registry, and avoid granting these roles directly to agents. These roles contain permissions to create, delete, and update services, including modifying critical agent metadata and [tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) such as `readOnlyHint` or `destructiveHint`. Malicious changes to metadata and annotations can cause unintended and destructive consequences when an orchestrator uses the modified tool. Additionally, an agent with these permissions can explicitly enroll a malicious external agent into the registry.**Role** | **Description** | **Purpose**  
---|---|---  
**Agent Registry API Admin** (`roles/agentregistry.admin`) |  Full access to all Agent Registry resources, including agents, MCP servers, tools, endpoints, standalone skills, skill revisions, bindings, and skill IAM policies. | 

  * Register and manage agents, MCP servers, tools, and endpoints.
  * Create, update, and delete standalone skills and skill revisions.
  * Create and manage bindings and skill IAM policies.

  
**Agent Registry API Editor** (`roles/agentregistry.editor`) |  Edit access to Agent Registry resources, including agents, MCP servers, tools, endpoints, standalone skills, and skill revisions. | 

  * Register and manage agents and MCP servers.
  * Update tool definitions and endpoints.
  * Create, update, and delete standalone skills and skill revisions.

  
**Agent Registry API Viewer** (`roles/agentregistry.viewer`) |  Read-only access to view and search agents, MCP servers, tools, standalone skills, skill revisions, publishers, endpoints, and bindings. | 

  * Discover available agents, MCP servers, and tools.
  * View A2A skills, standalone skills, skill revisions, publishers, endpoints, and bindings for integration.

  
**Agent Registry User** (`roles/agentregistry.user`) |  Read-only access to Agent Registry resources, plus access to create, update, and delete standalone skills and skill revisions. | 

  * Create, update, and delete standalone skills and skill revisions without edit access to agents, MCP servers, or endpoints.
  * Keep version control for skill revisions and centrally manage active states of skills.

  
  
## Agent Registry permissions

The following table lists the permissions that each Agent Registry IAM role has:

Agent Registry API AdminAgent Registry API EditorAgent Registry API ViewerAgent Registry UserClear all

#### Agent Registry API Admin Beta

(`roles/agentregistry.admin`) Full access to Agent Registry API resources.  |  `agentregistry.*`

  * `agentregistry.agents.get`
  * `agentregistry.agents.list`
  * `agentregistry.agents.search`
  * `agentregistry.bindings.create`
  * `agentregistry.bindings.delete`
  * `agentregistry.bindings.fetchAvailable`
  * `agentregistry.bindings.get`
  * `agentregistry.bindings.list`
  * `agentregistry.bindings.update`
  * `agentregistry.endpoints.get`
  * `agentregistry.endpoints.list`
  * `agentregistry.locations.get`
  * `agentregistry.locations.list`
  * `agentregistry.mcpServers.get`
  * `agentregistry.mcpServers.list`
  * `agentregistry.mcpServers.search`
  * `agentregistry.operations.cancel`
  * `agentregistry.operations.delete`
  * `agentregistry.operations.get`
  * `agentregistry.operations.list`
  * `agentregistry.publishers.get`
  * `agentregistry.publishers.list`
  * `agentregistry.services.create`
  * `agentregistry.services.delete`
  * `agentregistry.services.get`
  * `agentregistry.services.list`
  * `agentregistry.services.update`
  * `agentregistry.skillRevisions.create`
  * `agentregistry.skillRevisions.delete`
  * `agentregistry.skillRevisions.get`
  * `agentregistry.skillRevisions.list`
  * `agentregistry.skills.create`
  * `agentregistry.skills.delete`
  * `agentregistry.skills.get`
  * `agentregistry.skills.getIamPolicy`
  * `agentregistry.skills.list`
  * `agentregistry.skills.search`
  * `agentregistry.skills.setIamPolicy`
  * `agentregistry.skills.update`

  
---|---  
  
#### Agent Registry API Editor Beta

(`roles/agentregistry.editor`) Edit access to Agent Registry API resources.  |  `agentregistry.agents.*`

  * `agentregistry.agents.get`
  * `agentregistry.agents.list`
  * `agentregistry.agents.search`

`agentregistry.bindings.fetchAvailable` `agentregistry.bindings.get` `agentregistry.bindings.list` `agentregistry.endpoints.*`

  * `agentregistry.endpoints.get`
  * `agentregistry.endpoints.list`

`agentregistry.locations.*`

  * `agentregistry.locations.get`
  * `agentregistry.locations.list`

`agentregistry.mcpServers.*`

  * `agentregistry.mcpServers.get`
  * `agentregistry.mcpServers.list`
  * `agentregistry.mcpServers.search`

`agentregistry.operations.*`

  * `agentregistry.operations.cancel`
  * `agentregistry.operations.delete`
  * `agentregistry.operations.get`
  * `agentregistry.operations.list`

`agentregistry.publishers.*`

  * `agentregistry.publishers.get`
  * `agentregistry.publishers.list`

`agentregistry.services.*`

  * `agentregistry.services.create`
  * `agentregistry.services.delete`
  * `agentregistry.services.get`
  * `agentregistry.services.list`
  * `agentregistry.services.update`

`agentregistry.skillRevisions.*`

  * `agentregistry.skillRevisions.create`
  * `agentregistry.skillRevisions.delete`
  * `agentregistry.skillRevisions.get`
  * `agentregistry.skillRevisions.list`

`agentregistry.skills.create` `agentregistry.skills.delete` `agentregistry.skills.get` `agentregistry.skills.list` `agentregistry.skills.search` `agentregistry.skills.update`  
  
#### Agent Registry API Viewer Beta

(`roles/agentregistry.viewer`) Readonly access to Agent Registry API resources.  |  `agentregistry.agents.*`

  * `agentregistry.agents.get`
  * `agentregistry.agents.list`
  * `agentregistry.agents.search`

`agentregistry.bindings.fetchAvailable` `agentregistry.bindings.get` `agentregistry.bindings.list` `agentregistry.endpoints.*`

  * `agentregistry.endpoints.get`
  * `agentregistry.endpoints.list`

`agentregistry.locations.*`

  * `agentregistry.locations.get`
  * `agentregistry.locations.list`

`agentregistry.mcpServers.*`

  * `agentregistry.mcpServers.get`
  * `agentregistry.mcpServers.list`
  * `agentregistry.mcpServers.search`

`agentregistry.operations.get` `agentregistry.operations.list` `agentregistry.publishers.*`

  * `agentregistry.publishers.get`
  * `agentregistry.publishers.list`

`agentregistry.services.get` `agentregistry.services.list` `agentregistry.skillRevisions.get` `agentregistry.skillRevisions.list` `agentregistry.skills.get` `agentregistry.skills.list` `agentregistry.skills.search`  
  
#### Agent Registry User Beta

(`roles/agentregistry.user`) Create, update, and delete skills and skill revisions.  |  `agentregistry.agents.*`

  * `agentregistry.agents.get`
  * `agentregistry.agents.list`
  * `agentregistry.agents.search`

`agentregistry.bindings.fetchAvailable` `agentregistry.bindings.get` `agentregistry.bindings.list` `agentregistry.endpoints.*`

  * `agentregistry.endpoints.get`
  * `agentregistry.endpoints.list`

`agentregistry.locations.*`

  * `agentregistry.locations.get`
  * `agentregistry.locations.list`

`agentregistry.mcpServers.*`

  * `agentregistry.mcpServers.get`
  * `agentregistry.mcpServers.list`
  * `agentregistry.mcpServers.search`

`agentregistry.operations.get` `agentregistry.operations.list` `agentregistry.publishers.*`

  * `agentregistry.publishers.get`
  * `agentregistry.publishers.list`

`agentregistry.services.get` `agentregistry.services.list` `agentregistry.skillRevisions.*`

  * `agentregistry.skillRevisions.create`
  * `agentregistry.skillRevisions.delete`
  * `agentregistry.skillRevisions.get`
  * `agentregistry.skillRevisions.list`

`agentregistry.skills.create` `agentregistry.skills.delete` `agentregistry.skills.get` `agentregistry.skills.list` `agentregistry.skills.search` `agentregistry.skills.update`  
  
For more information about IAM permissions, see [Find the right predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles) and [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Access control for registered resources

Agent Registry roles govern who can manage and discover resources in the registry itself. To control which agents can communicate with registered services, endpoints, and MCP servers through [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview), you use [Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs/agent-overview) egress policies:

  * **Egress access permissions** : To authorize an agent to route traffic to a registered agent, MCP server, or endpoint, grant the [**IAP-secured Egressor** (`roles/iap.egressor`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.egressor) role to the [agent principal](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-principals) on the target resource.
  * **Policy administration permissions** : To configure IAP web IAM policies on registered resources, you must obtain the [IAP Policy Admin (`roles/iap.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.admin) role on the project hosting the registry.



For detailed instructions on configuring IAP egress policies, see [Configure IAM agent policies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/configure-iam-policies).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
