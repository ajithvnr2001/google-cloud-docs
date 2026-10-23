---
url: https://docs.cloud.google.com/agent-registry/use-agentregistry-mcp/
title: Use the Agent Registry MCP server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:15.247722+00:00
---

# Use the Agent Registry MCP server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/use-agentregistry-mcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Use the Agent Registry MCP server Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to use the Agent Registry remote Model Context Protocol (MCP) server to connect with AI applications including Antigravity, ChatGPT, Claude, and custom applications you are developing. The Agent Registry remote MCP server lets your AI applications dynamically discover other agents, endpoints, and MCP servers available in your environment. The Agent Registry remote MCP server is enabled when you enable the Agent Registry API. 

[Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP) standardizes how large language models (LLMs) and AI applications or agents connect to external data sources. MCP servers let you use their tools, resources, and prompts to take actions and get updated data from their backend service.

## What's the difference between local and remote MCP servers?

Local MCP servers
    Typically run on your local machine and use the standard input and output streams (stdio) for communication between services on the same device.
Remote MCP servers
    Run on the service's infrastructure and offer an HTTP endpoint to AI applications for communication between the AI MCP client and the MCP server. For more information about MCP architecture, see [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture).

## Stateless core

With [MCP version 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28), MCP changes from a bidirectional, stateful protocol to a stateless protocol. Each MCP request is self-describing and can be routed using headers. There isn't a need for the `initialize`/`initialized` handshake or `Mcp-Session-Id` because each request includes all the information needed in HTTP headers or the `_meta` parameter. MCP servers can request additional information required by a tool through [multi-round-trip requests (MRTR)](https://modelcontextprotocol.io/specification/latest/basic/patterns/mrtr).

To help route and process requests without parsing the request body, some MCP headers are required, including the following:

  * Headers that are required by the MCP specification such as the [protocol version header](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http#protocol-version-header) and [standard request headers](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http#standard-request-headers).
  * [Custom headers](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http#custom-headers-from-tool-parameters) that are defined by the MCP server. These headers are mirrored into HTTP headers from the tool's input schema using the `x-mcp-header` property. For example, an MCP server might define a custom header to specify the Google Cloud region or project ID.



For more information about MCP architecture, see the MCP version 2026-07-28 [specification](https://modelcontextprotocol.io/specification/2026-07-28) and [key changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog).

## Google and Google Cloud remote MCP servers

Google and Google Cloud remote MCP servers have the following features and benefits: 

  * Simplified, centralized discovery
  * Managed global or regional HTTP endpoints
  * Fine-grained authorization
  * Optional prompt and response security with Model Armor protection
  * Centralized audit logging



For information about other MCP servers and information about security and governance controls available for Google Cloud MCP servers, see [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview).

## Before you begin

  1. [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).
  2. Get [the project ID](https://support.google.com/googleapi/answer/7014113) for the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled.



### Required roles

To get the permissions that you need to use the Agent Registry MCP server, ask your administrator to grant you the following IAM roles on the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled: 

  * Make MCP tool calls: [MCP Tool User ](https://docs.cloud.google.com/iam/docs/roles-permissions/mcp#mcp.toolUser) (`roles/mcp.toolUser`) 
  * Discover resources: [Agent Registry API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.viewer) (`roles/agentregistry.viewer`) 
  * Manage resources: [Agent Registry API Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.editor) (`roles/agentregistry.editor`) 
  * Manage bindings: [Agent Registry API Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.admin) (`roles/agentregistry.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use the Agent Registry MCP server. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use the Agent Registry MCP server:

  * Make MCP tool calls: `mcp.tools.call`
  * Discover resources: 
    * `agentregistry.agents.__`
    * `agentregistry.bindings.fetchAvailable`
    * `agentregistry.bindings.get`
    * `agentregistry.bindings.list`
    * `agentregistry.endpoints.`
    * `agentregistry.locations.__`
    * `agentregistry.mcpServers.`
    * `agentregistry.operations.get`
    * `agentregistry.operations.list`
    * `agentregistry.publishers.*`
    * `agentregistry.services.get`
    * `agentregistry.services.list`
    * `agentregistry.skillRevisions.get`
    * `agentregistry.skillRevisions.list`
    * `agentregistry.skills.get`
    * `agentregistry.skills.list`
    * `agentregistry.skills.search`
  * Manage resources: 
    * `agentregistry.operations.__`
    * `agentregistry.services.`
    * `agentregistry.skillRevisions.*`
    * `agentregistry.skills.create`
    * `agentregistry.skills.delete`
    * `agentregistry.skills.update`
  * Manage bindings: 
    * `agentregistry.bindings.create`
    * `agentregistry.bindings.delete`
    * `agentregistry.bindings.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Authentication and authorization

The Agent Registry remote MCP server uses the [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2) protocol with [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) for authentication and authorization. All [Google Cloud identities](https://docs.cloud.google.com/docs/authentication/identity-products) are supported for authentication to MCP servers. 

The Agent Registry MCP server requires a principal for Identity and Access Management (IAM) control and doesn't accept API keys. As a best practice, create a separate identity for agents that are using MCP tools so that you can control and monitor access to resources.

For more information about authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).

## Agent Registry MCP OAuth scopes

OAuth 2.0 uses scopes and credentials to determine whether an authenticated principal is authorized to take a specific action on a resource. For more information about OAuth 2.0 scopes at Google, see [Using OAuth 2.0 to access Google APIs](https://developers.google.com/identity/protocols/oauth2).

Agent Registry has the following MCP tool OAuth scopes:

Scope URI for Google Cloud CLI | Description  
---|---  
`https://www.googleapis.com/auth/cloud-platform` | Full access to all Google Cloud resources.  
`https://www.googleapis.com/auth/agentregistry.read-write` | Read and write access to Agent Registry resources.  
  
Additional scopes might be required on the resources accessed during a tool call. To view a list of scopes required for Agent Registry, see [Agent Registry API](https://developers.google.com/identity/protocols/oauth2/scopes#agentregistry).

## Configure an MCP client to use the Agent Registry MCP server

AI applications and agents, such as Claude or Antigravity, can instantiate an MCP client that connects to a single MCP server. An AI application can have multiple clients that connect to different MCP servers. If your application isn't listed in the [client-specific guidance](https://docs.cloud.google.com/mcp/configure-mcp-ai-application#client-specific-guidance), then you can use the following information to connect from most applications.

  * **Server name** : Agent Registry MCP server
  * **Server URL** or **Endpoint** : `https://agentregistry.googleapis.com/mcp`
  * **Transport** : [Streamable HTTP](https://modelcontextprotocol.io/specification/latest/basic/transports/streamable-http)
  * **Authentication details** : depending on how you want to authenticate, you can enter your Google Cloud credentials, your OAuth Client ID and secret, or an agent identity and credentials. For more information about authentication, see [Authenticate to MCP servers](https://docs.cloud.google.com/mcp/authenticate-mcp).
  * **OAuth scope** : the [OAuth 2.0 scope](https://developers.google.com/identity/protocols/oauth2/scopes) that you want to use when connecting to the Agent Registry MCP server.



For application-specific guidance about setting up and connecting to MCP server, see [Client-specific guidance](https://docs.cloud.google.com/mcp/configure-mcp-ai-application#client-specific-guidance).

For more general guidance, see the following resources:

  * [Connect to remote MCP servers](https://modelcontextprotocol.io/docs/develop/connect-remote-servers).
  * [Configure MCP in an AI application](https://docs.cloud.google.com/mcp/configure-mcp-ai-application).



## Available tools

To view details of available MCP tools and their descriptions for the Agent Registry MCP server, see the [Agent Registry MCP reference](https://docs.cloud.google.com/agent-registry/reference/mcp).

Agent Registry separates discovery from manual registration and updates. You query the read-only `Agent`, `McpServer`, or `Endpoint` resources to discover capabilities, and you create, update, or delete `Service` resources to manage manually registered entries.

### Discovery tools

The most common tools used by AI agents for dynamic discovery include:

  * **`search_agents`** : performs a keyword or prefix search to discover agents within a specific project and location based on natural language queries, specific [A2A skills](https://docs.cloud.google.com/agent-registry/skills-architecture#standalone-vs-a2a), tags, or descriptions.
  * **`search_mcp_servers`** : performs a keyword or prefix search to discover MCP servers based on the specific tools they offer or their descriptions.
  * **`get_agent`** , **`get_mcp_server`** , **`get_endpoint`** : retrieves the full metadata and configuration details of specific resources using their unique resource names.
  * **`get_service`** : retrieves a specific `Service` resource to inspect the metadata and specification used to manually register an agentic component.
  * **`get_operation`** : gets the latest state of a long-running operation.
  * **`list_bindings`** , **`get_binding`** , **`fetch_available_bindings`** : retrieves [binding](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery#bindings) configurations that connect source agents to target resources or [auth providers](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery#auth-providers).



Search tools are best suited for natural language queries. However, the MCP server also provides listing tools that return paginated lists of resources. These tools are useful to enumerate resources or filter by resource attributes rather than natural language searches:

  * **`list_agents`** : returns a paginated list of agents within a specified Google Cloud project and location.
  * **`list_mcp_servers`** : returns a paginated list of MCP servers within a specified Google Cloud project and location.
  * **`list_endpoints`** , **`list_services`** : returns a paginated list of registered endpoints and manually created `Service` resources in a given project and location.



### Administrative tools

AI applications primarily use Agent Registry for discovery. However, the MCP server also exposes tools to programmatically manage registry entries:

  * **`create_service`** : manually registers a new custom [agentic component](https://docs.cloud.google.com/agent-registry/component-lifecycle-and-discovery), such as an agent, MCP server, or endpoint, by creating a `Service` resource from its JSON specification.
  * **`update_service`** : updates the metadata or specification of an existing `Service` resource, such as patching an uploaded Agent Card.
  * **`delete_service`** : deletes a `Service` resource, removing the entry for the manually registered agent, MCP server, or endpoint from the registry.
  * **`create_binding`** , **`update_binding`** , **`delete_binding`** : programmatically manages connections and delegated access mappings between your agents and target MCP servers or endpoints.



### List tools

Use the [MCP inspector](https://modelcontextprotocol.io/docs/tools/inspector) to list tools, or send a `tools/list` HTTP request directly to the Agent Registry remote MCP server. The `tools/list` method doesn't require authentication.
    
    
    curl -X POST https://agentregistry.googleapis.com/TOOLSET_ENDPOINT \
        -H 'Content-Type: application/json' \
        -H 'Accept: application/json' \
        -H 'MCP-Protocol-Version: MCP_PROTOCOL_VERSION' \
        -H 'Mcp-Method: tools/list' \
        -d '{
          "jsonrpc": "2.0",
          "id": 1,
          "method": "tools/list",
          "params": {
            "_meta": {
              "io.modelcontextprotocol/protocolVersion": "MCP_PROTOCOL_VERSION",
              "io.modelcontextprotocol/clientCapabilities": {
                "extensions": {
                  "io.modelcontextprotocol/ui": {
                    "mimeTypes": ["text/html;profile=mcp-app"]
                  }
                }
              }
            }
          }
        }'
    

Replace the following:

  * `TOOLSET_ENDPOINT`: the remainder of the MCP endpoint after the service name. For example, for Agent Registry, this might be `mcp`.
  * `MCP_PROTOCOL_VERSION`: the MCP protocol version, such as `2026-07-28`.



## Example use cases

When you connect your AI application or agent to the Agent Registry MCP server, you can use natural language prompts to dynamically discover and retrieve resources in your environment.

The following are example prompts you can use with your connected AI application:

  * **Discover an agent by A2A skill** : "Find an agent capable of booking corporate flights."
  * **Discover MCP servers** : "What MCP servers are registered that offer BigQuery data tools?"
  * **Retrieve specific resource details** : "Show me the metadata and configuration details for the agent named projects/123456789/locations/global/agents/travel-agent."



## Optional security and safety configurations

MCP introduces new security risks and considerations due to the wide variety of actions that you can do with the MCP tools. To minimize and manage these risks, Google Cloud offers default settings and customizable policies to control the use of MCP tools in your Google Cloud organization or project.

For more information about MCP security and governance, see [AI security and safety](https://docs.cloud.google.com/mcp/ai-security-safety).

### Use Model Armor

[Model Armor](https://docs.cloud.google.com/model-armor/overview) is a Google Cloud service designed to enhance the security and safety of your AI applications. It works by proactively screening LLM prompts and responses, protecting against various risks and supporting responsible AI practices. Whether you are deploying AI in your cloud environment, or on external cloud providers, Model Armor can help you prevent malicious input, verify content safety, protect sensitive data, maintain compliance, and enforce your AI safety and security policies consistently across your diverse AI landscape.

When Model Armor is enabled with [logging enabled](https://docs.cloud.google.com/model-armor/configure-logging), Model Armor logs the entire payload. This might expose sensitive information in your logs.

#### MCP request routing to Model Armor

Model Armor is available in [certain regions](https://docs.cloud.google.com/model-armor/locations). When Model Armor is enabled and you use an MCP server in a jurisdiction that Model Armor doesn't support, the routing behavior of the call might be different for different MCP servers and might break data residency compliance for in-use and in-transit data. For more information about the behavior of individual MCP servers, see [Model Armor supported products](https://docs.cloud.google.com/mcp/model-armor-supported-products). 

#### Enable Model Armor

You must enable Model Armor APIs before you can use Model Armor.

###  Console 

  1. Enable the Model Armor API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=modelarmor.googleapis.com)

  2. Select the project where you want to activate Model Armor.




###  gcloud 

Before you begin, follow these steps using the Google Cloud CLI with the Model Armor API:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the following command to set the API endpoint for the Model Armor service.
         
         gcloud config set api_endpoint_overrides/modelarmor "https://modelarmor.LOCATION.rep.googleapis.com/"

Replace `LOCATION` with the region where you want to use Model Armor.




#### Configure protection for MCP servers

To help protect your MCP tool calls and responses you can use Model Armor floor settings. A floor setting defines the minimum security filters that apply across the project. This configuration applies a consistent set of filters to all MCP tool calls and responses within the project.

**Tip:** Don't enable the prompt injection and jailbreak filter unless your MCP traffic carries natural language data.

Set up a Model Armor floor setting with MCP sanitization enabled. For more information, see [Configure Model Armor floor settings](https://docs.cloud.google.com/model-armor/configure-floor-settings).

**Note:** If the agent and the MCP server are in different projects, you can create floor settings in both projects (the client project and the resource project). In this case, Model Armor is invoked twice, once for each project.

See the following example command:
    
    
    gcloud model-armor floorsettings update \
    --full-uri='projects/PROJECT_ID/locations/global/floorSetting' \
    --enable-floor-setting-enforcement=TRUE \
    --add-integrated-services=GOOGLE_MCP_SERVER \
    --google-mcp-server-enforcement-type=INSPECT_AND_BLOCK \
    --enable-google-mcp-server-cloud-logging \
    --malicious-uri-filter-settings-enforcement=ENABLED \
    --add-rai-settings-filters='[{"confidenceLevel": "MEDIUM_AND_ABOVE", "filterType": "DANGEROUS"}]'

Replace `PROJECT_ID` with your Google Cloud project ID.

Note the following settings:

  * `INSPECT_AND_BLOCK`: The enforcement type that inspects content for the Google MCP server and blocks prompts and responses that match the filters.
  * `ENABLED`: The setting that enables a filter or enforcement.
  * `MEDIUM_AND_ABOVE`: The confidence level for the Responsible AI - Dangerous filter settings. You can modify this setting, though lower values might result in more false positives. For more information, see [Model Armor confidence levels](https://docs.cloud.google.com/model-armor/overview#ma-confidence-levels).



#### Disable scanning MCP traffic with Model Armor

To stop Model Armor from automatically scanning traffic to and from Google MCP servers based on the project's floor settings, run the following command:
    
    
    gcloud model-armor floorsettings update \
      --full-uri='projects/PROJECT_ID/locations/global/floorSetting' \
      --remove-integrated-services=GOOGLE_MCP_SERVER
    

Replace `PROJECT_ID` with the Google Cloud project ID. Model Armor doesn't automatically apply the rules defined in this project's floor settings to any Google MCP server traffic.

Model Armor floor settings and general configuration can impact more than just MCP. Because Model Armor integrates with services like Vertex AI, any changes you make to floor settings can affect traffic scanning and safety behaviors across all integrated services, not just MCP.

### Control MCP use with IAM policies

Identity and Access Management (IAM) [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview) and [allow policies](https://docs.cloud.google.com/iam/docs/allow-policies) help you secure Google Cloud and Google MCP servers.

You can combine multiple criteria to build customized security and governance policies by allowing or denying access based on the following:

  * The principal.
  * Tool properties like the read-only attribute.
  * The service name or tool name.
  * The application's OAuth client ID.



For more information, see [Control MCP use with Identity and Access Management](https://docs.cloud.google.com/mcp/control-mcp-use-iam).

## What's next

  * Review the [Agent Registry MCP reference documentation](https://docs.cloud.google.com/agent-registry/reference/mcp).
  * Learn more about [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
