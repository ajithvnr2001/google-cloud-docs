---
url: https://docs.cloud.google.com/agent-registry/manage-mcp-tools/
title: Manage MCP servers and tools \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:17.136295+00:00
---

# Manage MCP servers and tools  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/manage-mcp-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Manage MCP servers and tools Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry lets you inspect, update, and remove registered Model Context Protocol (MCP) servers and tools so that your agents have accurate tool schemas and endpoints at runtime. You can discover automatically and [manually registered MCP servers](https://docs.cloud.google.com/agent-registry/register-mcp-servers), update manually registered tool definitions, and remove MCP servers that are no longer in use.

## Before you begin

  1. [Register MCP servers](https://docs.cloud.google.com/agent-registry/register-mcp-servers) in Agent Registry.
  2. Get [the project ID](https://support.google.com/googleapi/answer/7014113) for the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled.
  3. To use the Google Cloud CLI commands in this document, [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).



### Required roles

To get the permissions that you need to manage MCP servers and tools in Agent Registry, ask your administrator to grant you the following IAM roles on the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled: 

  * Discover available MCP servers and tools: [Agent Registry API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.viewer) (`roles/agentregistry.viewer`) 
  * Update tool definitions: [Agent Registry API Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.editor) (`roles/agentregistry.editor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Discover available MCP servers and tools

After registering MCP servers, you can discover them to bind them to your agents.

### List all available MCP servers

You can list all MCP servers registered in your environment and view their detailed configurations, such as their endpoints and associated metadata:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **MCP servers** tab.

The page displays a list of all registered MCP servers and their details, such as name, [identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#mcp-server-identifiers), description, runtime, and location.

  4. To view the full details of a server, click the server's name.




###  gcloud 

To list all MCP servers in a specific location, run the [`gcloud agent-registry mcp-servers list`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/mcp-servers/list) command:
    
    
    gcloud agent-registry mcp-servers list \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region.



### Filter registered MCP servers

If you have multiple servers, or if you want to confirm the registration of a specific server, you can filter the list by the server's metadata:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **MCP servers** tab.

The page displays a list of all registered MCP servers and their details, such as name, [identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#mcp-server-identifiers), description, runtime, and location.

  4. To filter by location, click the **Location** menu, select the locations you want to filter, and click **Apply**.

The page displays a filtered list of the registered MCP servers for your selected conditions.




###  gcloud 

Filter your list to only return resources matching specific metadata by passing the `--filter` flag to the [`gcloud agent-registry mcp-servers list`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/mcp-servers/list) command:
    
    
    gcloud agent-registry mcp-servers list \
        --project=PROJECT_ID \
        --location=REGION \
        --filter="FILTER_EXPRESSION"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region.
  * `FILTER_EXPRESSION`: the filter expression for the MCP servers that you want to filter. For example, you can use the following filters: 
    * To filter by display name, use `displayName='DISPLAY_NAME'`.
    * To search by the globally unique [MCP server identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#mcp-server-identifiers) (URN), use `mcpServerId='urn:mcp:SERVER_URN'`.



###  Terraform 

To retrieve a specific registered MCP server by filtering against its metadata, configure the `google_agent_registry_mcp_server` data source with the `filter` argument:
    
    
    data "google_agent_registry_mcp_server" "filtered_mcp_server" {
      location = "REGION"
      filter   = "displayName=\"DISPLAY_NAME\""
    }
    

Replace the following:

  * `REGION`: the registry region.
  * `DISPLAY_NAME`: the human-readable name of the MCP server to filter by, for example, `Custom MCP Server`.



### View details from an MCP server

View details from a specific MCP server, for example, its tools:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **MCP servers** tab.

The page displays a list of all registered MCP servers and their details, such as name, [identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#mcp-server-identifiers), description, runtime, and location.

  4. Click the name of the MCP server that you want to view.

The details page includes tabs for the MCP server details.

  5. Click the corresponding tab to view specific MCP server details:

     * **Overview** : core details from the MCP server, including the server's name, [identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#mcp-server-identifiers), location, and description. The overview also displays a code snippet to let you build your agents using the [Agent Development Kit (ADK)](https://docs.cloud.google.com/agent-registry/resolve-endpoints-and-build-orchestrators).
     * **Observability** : insights into the operational health and usage of the MCP server. It surfaces application-centric metrics such as latency, traffic, errors, and token spend. This tab integrates with Google Cloud Observability to display real-time performance metrics and system-level utilization to help you manage costs, debug issues, and track user experience. For more information, see the [Observability overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/overview).
     * **Tools** : the capabilities provided by the server. This tab lists the specific functions exposed by an MCP server that agents can invoke to perform specific actions. For each tool, the interface displays its schema, including its name, description, and critical behavioral annotations that guide how an orchestrating agent should interact with it. Click the name of a tool to display a code snippet that lets you build your agents using the [ADK](https://docs.cloud.google.com/agent-registry/resolve-endpoints-and-build-orchestrators).



###  gcloud 

To view the detailed metadata of a specific MCP server, run the [`gcloud agent-registry mcp-servers describe`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/mcp-servers/describe) command:
    
    
    gcloud agent-registry mcp-servers describe SERVER_NAME \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `SERVER_NAME`: the name of your MCP server, for example, `custom-mcp-server`.
  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region.



###  Terraform 

To retrieve details about a specific registered MCP server using its ID, configure the `google_agent_registry_mcp_server` data source:
    
    
    data "google_agent_registry_mcp_server" "my_mcp_server" {
      location      = "REGION"
      mcp_server_id = "SERVER_NAME"
    }
    
    output "server_create_time" {
      description = "The timestamp when the MCP server was registered."
      value       = data.google_agent_registry_mcp_server.my_mcp_server.create_time
    }
    
    output "server_update_time" {
      description = "The timestamp when the MCP server was last updated."
      value       = data.google_agent_registry_mcp_server.my_mcp_server.update_time
    }
    

Replace the following:

  * `REGION`: the registry region.
  * `SERVER_NAME`: the unique identifier of your MCP server, for example, `custom-mcp-server`.



## Update server details and tool definitions

If your MCP server adds new tools or changes existing schemas, you must update the registry to reflect these changes.

In Agent Registry, `McpServer` resources are read-only discovery resources. For automatically registered MCP servers, update the deployment or workload in its underlying runtime so that Agent Registry synchronizes the changes. To update a manually registered MCP server, you must update its writable `Service` resource directly. Because the registry doesn't automatically inspect manually registered MCP servers, you must manually upload the updated tool specification, which replaces the existing tool definitions for the server.

###  Console 

Update available server details from the Google Cloud console:

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **MCP servers** tab.

The page displays a list of all registered MCP servers and their details, such as name, [identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#mcp-server-identifiers), description, runtime, and location.

  4. Click the name of the server that you want to update.

  5. On the **Overview** tab of the server, click edit **Edit**.

  6. In the **Edit service** panel, enter the updated information of your server, such as its new name or description.

  7. Click **Save**.




###  gcloud 

[Prepare your new tool specification](https://docs.cloud.google.com/agent-registry/register-mcp-servers#prepare-tool-spec). Then, run the [`gcloud agent-registry services update`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/services/update) command with your updated JSON file:
    
    
    gcloud agent-registry services update SERVER_NAME \
        --project=PROJECT_ID \
        --location=REGION \
        --mcp-server-spec-content=TOOL_SPEC
    

Replace the following:

  * `SERVER_NAME`: the name of your MCP server, for example, `custom-mcp-server`.
  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region.
  * `TOOL_SPEC`: the path to the new tool specification file, for example, `new-toolspec.json`. The maximum file size for the specification file is 10 KB.



###  Terraform 

To update your registered MCP server's metadata, endpoint URL, or tool specification, modify the parameters of the existing `google_agent_registry_service` resource in your configuration, and then run `terraform apply`:
    
    
    resource "google_agent_registry_service" "mcp_server" {
      location     = "REGION"
      service_id   = "SERVER_NAME"
      display_name = "DISPLAY_NAME"
      description  = "Updated description of the MCP server."
    
      interfaces {
        url              = "SERVER_URL"
        protocol_binding = "JSONRPC"
      }
    
      mcp_server_spec {
        type    = "TOOL_SPEC"
        content = file("TOOL_SPEC")
      }
    }
    

Replace the following:

  * `REGION`: the registry region.
  * `SERVER_NAME`: the name of your MCP server, for example, `custom-mcp-server`.
  * `DISPLAY_NAME`: the human-readable display name of your MCP server, for example, `Custom MCP Server`.
  * `SERVER_URL`: the endpoint URL of the MCP server, for example, `https://api.example.com/mcp`.
  * `TOOL_SPEC`: the path to your updated tool specification file, for example, `new-toolspec.json`. The maximum file size for the specification file is 10 KB.



## Remove an MCP server

To delete MCP servers that were automatically registered to Agent Registry, you must delete the underlying MCP server or disable the Google Cloud API of the MCP server in your project. The server is then automatically removed from the registry.

To remove a manually registered MCP server from the registry, you must delete its `Service` resource. This action removes the MCP server from search results and makes it undiscoverable to other tools:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **MCP servers** tab.

The page displays a list of all registered MCP servers and their details, such as name, [identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#mcp-server-identifiers), description, runtime, and location.

  4. Click the name of the server that you want to remove.

  5. On the **Overview** tab of the server, click delete **Delete**.

  6. In the confirmation dialog, enter `DELETE` to confirm the action.

  7. Click **Delete**.




###  gcloud 

Run the [`gcloud agent-registry services delete`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/services/delete) command:
    
    
    gcloud agent-registry services delete SERVER_NAME \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `SERVER_NAME`: the name of the MCP server you want to remove, for example, `my-mcp-server`.
  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region.



###  Terraform 

Remove the `google_agent_registry_service` resource representing the MCP server from your Terraform configuration, and then run `terraform apply`.

## Govern tool access

Implement enterprise-grade governance and security for your MCP servers and tools. Use Agent Registry as your central registry and [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) for active policy enforcement.

Agent Gateway lets you securely govern interactions between agents and tools, regardless of whether those agents are running on Google Cloud or are external developer tools.

For more information about governing tool access, see the following:

  * [Identity and Access Management (IAM) policies overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/overview): define who can access specific tools and under what conditions.
  * [Agent Gateway overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview): understand how the gateway enforces security and observability across all agent-to-tool (MCP) interactions.
  * [View security findings](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/view-security-findings): monitor and review security insights for your agentic ecosystem using Gemini Enterprise Agent Platform.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
