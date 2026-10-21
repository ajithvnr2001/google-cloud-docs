---
url: https://docs.cloud.google.com/agent-registry/register-mcp-servers/
title: Register MCP servers \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:37:01.920743+00:00
---

# Register MCP servers  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/register-mcp-servers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Register MCP servers Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry acts as a centralized catalog by registering and managing [Model Context Protocol (MCP) server](https://docs.cloud.google.com/agent-registry/concepts#server) endpoints and the specific [tools](https://docs.cloud.google.com/agent-registry/concepts#tool) they expose.

This document describes how to register MCP servers and how their tool specifications are managed within Agent Registry.

## Automatic discovery of Google Cloud MCP servers

Official Google and Google Cloud remote MCP servers are automatically registered and ingested into Agent Registry. Available Google and Google Cloud remote MCP servers are listed in [Supported products](https://docs.cloud.google.com/mcp/supported-products) from the Google Cloud MCP servers documentation.

When you enable a supported Google Cloud API in your project, such as the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/mcp), the corresponding MCP server and its tools are immediately registered and made available for discovery in Agent Registry. You don't need to manually configure or upload tool specifications for these servers.

**Note:** If your organization uses [Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub), you can configure it to automatically sync your MCP-styled APIs to Agent Registry. Make sure the sync is enabled in API hub to keep imported MCP API data in Agent Registry. For more information, see [Register MCP APIs](https://docs.cloud.google.com/apigee/docs/apihub/register-mcp-apis).

### Scope and bindings for Google-managed MCP servers

Google-managed remote MCP servers are automatically registered in the `global` location of your project. Because these built-in Google servers reside globally, you must apply any Identity and Access Management (IAM) bindings for them at the global scope by specifying the `--region=global` flag. Regional IAM bindings, such as `--region=us-central1`, aren't supported for these global remote MCP servers and return a `NOT_FOUND` error.

## Register MCP servers from GKE

You can configure automatic registration for custom MCP servers deployed on [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/agentic-adk-vertex) by adding the `registry.gke.io/functional-type: "MCP_SERVER"` label to your GKE deployments.

**Note:** GKE also supports the `apphub.cloud.google.com/functional-type: "MCP_SERVER"` annotation for backward compatibility. However, we recommend using the `registry.gke.io/functional-type: "MCP_SERVER"` label for your GKE deployments.

To let Agent Registry perform an introspection scan and discover your MCP tools, your deployment must also include annotations declaring the server's endpoint URLs and capability details.

To enable authenticated communication, also configure [Agent Identity](https://docs.cloud.google.com/kubernetes-engine/security/about-agent-identity) by adding the `iam.gke.io/spiffe-identity-type: agent-identity` annotation to the Pod specification.

The following example shows a GKE MCP server deployment manifest using these configurations.
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-mcp-server
      labels:
        # GKE takes this label and registers the deployment as an MCP server to the registry
        registry.gke.io/functional-type: "MCP_SERVER"
      annotations:
        # A list of endpoint URLs where the GKE controller can access this MCP server
        modelcontextprotocol.info/urls: |
          - https://my-mcp-server.default.svc.cluster.local/mcp
        # Defines structural capabilities for the MCP server card
        modelcontextprotocol.info/capabilities: |
          card:
            endpoint: "/mcp"
            protocol: "HTTP"
    spec:
      selector:
        matchLabels:
          app: my-mcp-server
      template:
        metadata:
          labels:
            app: my-mcp-server
          annotations:
            # Agent Identity annotation for identity and access management
            iam.gke.io/spiffe-identity-type: agent-identity
        spec:
          containers:
          - name: server
            image: gcr.io/my-project/my-mcp-server:1.0.0
    

When you apply the deployment, GKE automatically attempts to obtain the tool specification from the server and registers the tools directly into the Agent Registry data model. Agent Registry uses your deployment name as the display name for the MCP server.

## Register MCP servers from Cloud Run

You can configure automatic registration for custom MCP servers deployed in [Cloud Run](https://docs.cloud.google.com/run/docs/ai/agent-platform-features) by specifying the `--functional-type=mcp-server` flag when you deploy them.

**Note:** Only Cloud Run services can be exposed as MCP servers. Cloud Run jobs cannot act as MCP servers. 

When you deploy a Cloud Run service with `--functional-type=mcp-server`, it is registered to the MCP server catalog in Agent Registry. During registration, Cloud Run registers the server name and type (`MCP_SERVER`).

You can also specify an identity type using the `--identity-type` flag. For example, specify an `agent-identity` or `service-account` identity. If unspecified, the workload defaults to using a service account identity.

To learn how to deploy an MCP server service in Cloud Run, see [Configure Agent Platform features for Cloud Run](https://docs.cloud.google.com/run/docs/ai/agent-platform-features).

For more information, see [Host MCP servers on Cloud Run](https://docs.cloud.google.com/run/docs/host-mcp-servers) and [Authenticate MCP servers](https://docs.cloud.google.com/run/docs/ai/authenticate-mcp-servers).

Automatic registration only discovers resources deployed within the same Google Cloud project.

## Register external MCP servers

To manage and reuse tools provided by external servers or custom APIs, you must explicitly register the MCP server.

When registering an MCP server manually, Agent Registry registers the endpoint. However, it doesn't automatically introspect the server to determine which tools are available. To let users discover the exact tools available on your MCP server, you must provide the tool specifications during registration by uploading a `toolspec.json` file.

**Warning:** This feature isn't supported in the `us` and `eu` multi-region locations. You must use a supported region or the `global` location. For more information, see [Agent Registry locations](https://docs.cloud.google.com/agent-registry/locations).

### Before you begin

Before you start, [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup). You need [the project ID](https://support.google.com/googleapi/answer/7014113) to perform these tasks.

To use the gcloud CLI commands in this document, make sure you have [set up your Google Cloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).

#### Required roles

To get the permissions that you need to register MCP servers manually in Agent Registry, ask your administrator to grant you the [Agent Registry API Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.editor) (`roles/agentregistry.editor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Prepare your tool specification

Create a `toolspec.json` file that outlines the tools the server provides. The maximum file size for this specification file is 10 KB.

The JSON file must align with the MCP specification for tool schemas, for example:
    
    
    {
      "tools": [
        {
          "name": "get_customer_info",
          "description": "Retrieves customer details from the database.",
          "annotations": {
            "title": "Get Customer Info",
            "readOnlyHint": true,
            "idempotentHint": true
          }
        },
        {
          "name": "create_support_ticket",
          "description": "Creates a new support ticket in the issue tracking system.",
          "annotations": {
            "title": "Create Support Ticket",
            "destructiveHint": true,
            "idempotentHint": false,
            "openWorldHint": true
          }
        }
      ]
    }
    

For detailed structural requirements, see [JSON schemas](https://docs.cloud.google.com/agent-registry/json-schemas) and the [REST reference](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.mcpServers#McpServer).

### Register the server and tools

Register the MCP server and upload the tool definition simultaneously:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **MCP servers** tab.

  4. Click **Add MCP server**.

  5. In the **MCP server details** panel, enter the display name, a description, and the geographic region.

  6. In the **Tool specification** section, enter the MCP server endpoint URL and paste the content of your `toolspec.json` file.

Optionally, click **Import tools** in this panel to import the MCP tools from the URL. This option only works if the endpoint URL of your MCP server is publicly hosted over the internet. You cannot use this feature to import tools from privately hosted MCP servers.

  7. Click **Next**.

The **Select MCP tools** panel displays a list of tools with names and descriptions from your MCP server.

  8. Select all the MCP tools that you want to include. You can filter tools from the list by name or value.

  9. Click **Save**.




###  gcloud 

The specification flags you use determine which resource collection your service belongs to. For a complete mapping of flags to resource collections, see [API resources](https://docs.cloud.google.com/agent-registry/data-model#api-resources).

Register the MCP server with the tool specification:
    
    
    gcloud agent-registry services create SERVER_NAME \
      --project=PROJECT_ID \
      --location=REGION \
      --display-name="DISPLAY_NAME" \
      --mcp-server-spec-type=tool-spec \
      --mcp-server-spec-content=toolspec.json \
      --interfaces=url=SERVER_URL,protocolBinding=PROTOCOL
    

Replace the following:

  * `SERVER_NAME`: The name you want to give to your MCP server, for example, `custom-mcp-server`.
  * `PROJECT_ID`: The project ID.
  * `REGION`: The registry region.
  * `DISPLAY_NAME`: The human-readable name that you want to give to your server, for example, `Custom MCP Server`.
  * `SERVER_URL`: The endpoint URL of the MCP server, for example, `https://api.example.com/mcp`.
  * `PROTOCOL`: The protocol binding for the endpoint. Valid values are `jsonrpc`, `http-json`, or `grpc`. For MCP servers, this value is often `jsonrpc`.



###  Terraform 

The specification block you configure, for example, `mcp_server_spec`, determines which resource collection your service belongs to. For a complete mapping of specifications to resource collections, see [API resources](https://docs.cloud.google.com/agent-registry/data-model#api-resources).

To register an MCP server and specify its tools, configure a `google_agent_registry_service` resource with the `mcp_server_spec` block:
    
    
    resource "google_agent_registry_service" "mcp_server" {
      location     = "REGION"
      service_id   = "SERVER_NAME"
      display_name = "DISPLAY_NAME"
      description  = "An external MCP server registered using Terraform."
    
      interfaces {
        url              = "SERVER_URL"
        protocol_binding = "JSONRPC"
      }
    
      mcp_server_spec {
        type    = "TOOL_SPEC"
        content = file("toolspec.json")
      }
    }
    
    output "server_resource_name" {
      description = "The generated read-only Server resource name."
      value       = google_agent_registry_service.mcp_server.registry_resource
    }
    

Replace the following:

  * `REGION`: The registry region.
  * `SERVER_NAME`: The name you want to give to your MCP server, for example, `custom-mcp-server`.
  * `DISPLAY_NAME`: The human-readable name that you want to give to your server, for example, `Custom MCP Server`.
  * `SERVER_URL`: The endpoint URL of the MCP server, for example, `https://api.example.com/mcp`.



### Verify registration

List, filter, and view the details of your newly registered MCP server. To confirm that your MCP server was successfully registered, you can [list the servers in your registry](https://docs.cloud.google.com/agent-registry/manage-mcp-tools).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
