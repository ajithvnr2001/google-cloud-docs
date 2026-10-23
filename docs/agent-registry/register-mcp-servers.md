---
url: https://docs.cloud.google.com/agent-registry/register-mcp-servers/
title: Register MCP servers \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:16.912103+00:00
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

Agent Registry lets you register Model Context Protocol (MCP) servers automatically or manually so that developers and orchestrator agents can discover and invoke standardized tools across your AI ecosystem.

Automatic registration for custom MCP servers deployed on Google Kubernetes Engine (GKE) or Cloud Run only discovers resources deployed within the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled. To register custom MCP servers deployed in separate Google Cloud projects or hosted externally, see Register external MCP servers.

## Automatic discovery of MCP servers

[Google and Google Cloud remote MCP servers](https://docs.cloud.google.com/mcp/supported-products) are automatically registered and ingested into Agent Registry.

When you enable a Google Cloud API with MCP support in your project, such as the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/mcp), the corresponding MCP server and its tools are immediately registered and made available for discovery in Agent Registry. You don't need to manually configure or upload tool specifications for these servers.

**Note:** If your organization uses [Apigee API hub](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub), you can configure it to automatically sync your MCP-styled APIs to Agent Registry. Make sure the sync is enabled in API hub to keep imported MCP API data in Agent Registry. For more information, see [Register MCP APIs](https://docs.cloud.google.com/apigee/docs/apihub/register-mcp-apis).

### Location and conditions

When Agent Registry automatically registers a Google or Google Cloud remote MCP server, it creates the `McpServer` resource only in the `global` location, not in individual regions such as `us-central1`. If the service provides regional endpoints (REPs), Agent Registry lists those regional URLs in the `interfaces` field of that single `global` `McpServer` resource.

Because the automatically registered resource exists only in `global`, keep the following conditions in mind when querying the server or configuring Identity-Aware Proxy (IAP) access policies:

  * **Use`global` for automatically registered servers**: specify the `global` location when you query the server in Agent Registry with `--location=global` or apply IAP policies to it with `--region=global`. If you specify a region such as `us-central1`, the command returns a `NOT_FOUND` error because no regional `McpServer` resource exists there by default.
  * **Manually register in a region for data residency** : if you need to keep registry metadata in a specific region, manually register the MCP server and its regional endpoint URL in that region, and then apply your IAP policy in that same region.



For more information, see [Governance scope across regional and global locations](https://docs.cloud.google.com/agent-registry/locations#governance-scope) and [Remote MCP server not found in a regional location](https://docs.cloud.google.com/agent-registry/troubleshooting#remote-mcp-server-regional-location).

## Before you begin

  1. [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).
  2. Get [the project ID](https://support.google.com/googleapi/answer/7014113) for the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled.
  3. To use the Google Cloud CLI commands in this document, [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).



### Required roles

To get the permissions that you need to register MCP servers in Agent Registry, ask your administrator to grant you the [Agent Registry API Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.editor) (`roles/agentregistry.editor`) IAM role on the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Register MCP servers from GKE

To register custom MCP servers deployed on [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/agentic-adk-vertex), add the required Kubernetes [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) and [annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) to your deployment manifest. The following example shows a GKE MCP server deployment manifest configured for automatic registration:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-mcp-server
      labels:
        # GKE takes this label and registers the deployment as an MCP server
        registry.gke.io/functional-type: "MCP_SERVER"
      annotations:
        # Endpoint URLs where the GKE controller can access this MCP server
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
            image: gcr.io/PROJECT_ID/my-mcp-server:1.0.0
    

Replace `PROJECT_ID` with your Google Cloud project ID.

To configure and apply the deployment manifest, do the following:

  1. In `metadata.labels` of your `Deployment` manifest, add the `registry.gke.io/functional-type: "MCP_SERVER"` label.

**Note:** GKE also supports the `apphub.cloud.google.com/functional-type: "MCP_SERVER"` annotation for backward compatibility. However, use the `registry.gke.io/functional-type: "MCP_SERVER"` label for your GKE deployments.
  2. In `metadata.annotations` of your `Deployment` manifest, enable automated discovery of your MCP tools by providing the `modelcontextprotocol.info/urls` and `modelcontextprotocol.info/capabilities` annotations to declare the server's endpoint URLs and capability details.

  3. In `spec.template.metadata.annotations` of the Pod template, enable authenticated communication by configuring [Agent Identity](https://docs.cloud.google.com/kubernetes-engine/security/about-agent-identity) with the `iam.gke.io/spiffe-identity-type: agent-identity` annotation.

  4. Apply the deployment manifest to your cluster.

When you apply the deployment, GKE automatically attempts to obtain the tool specification from the server and registers the server and its tools directly into a read-only `McpServer` discovery resource in Agent Registry. Agent Registry uses your deployment name as the display name for the MCP server.




## Register MCP servers from Cloud Run

You can automatically register custom MCP servers when you deploy them as Cloud Run services by specifying the [`--functional-type=mcp-server`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/deploy#--functional-type) flag. The `--functional-type=mcp-server` flag identifies the Cloud Run service as an MCP server rather than a standard containerized workload, instructing Cloud Run to register the server with Agent Registry. During registration, Cloud Run automatically adds the server's name and the `MCP_SERVER` type to the registry.

**Note:** Only Cloud Run services can be exposed as MCP servers. Cloud Run jobs can't act as MCP servers.

You can also specify an identity type using the [`--identity-type`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/deploy#--identity-type) flag. For example, specify an `agent-identity` or `service-account` identity. If unspecified, the workload defaults to using a service account identity.

To configure automatic registration on a new or existing Cloud Run service, see [Configure Gemini Enterprise Agent Platform features for Cloud Run](https://docs.cloud.google.com/run/docs/ai/agent-platform-features#configure-features). To deploy and secure MCP servers on Cloud Run, see [Host MCP servers on Cloud Run](https://docs.cloud.google.com/run/docs/host-mcp-servers) and [Authenticate MCP servers](https://docs.cloud.google.com/run/docs/ai/authenticate-mcp-servers).

## Register external MCP servers

To manage and reuse tools provided by external servers or custom APIs, you must manually register the MCP server.

When registering an MCP server manually, Agent Registry registers the endpoint. However, it doesn't automatically inspect the server to determine which tools are available. To let users discover the exact tools available on your MCP server, you must provide the tool specifications during registration by uploading a `toolspec.json` file.

**Warning:** This feature isn't supported in the `us` and `eu` multi-region locations. You must use a supported region or the `global` location. For more information, see [Agent Registry locations](https://docs.cloud.google.com/agent-registry/locations).

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

Optionally, click **Import tools** in this panel to import the MCP tools from the URL. This option only works if the endpoint URL of your MCP server is publicly hosted over the internet. You can't use this feature to import tools from privately hosted MCP servers.

  7. Click **Next**.

The **Select MCP tools** panel displays a list of tools with names and descriptions from your MCP server.

  8. Select all the MCP tools that you want to include. You can filter tools from the list by name or value.

  9. Click **Save**.




###  gcloud 

The specification flags you use determine which resource collection your component belongs to. For a complete mapping of flags to resource collections, see [Service resources and discovery resources](/agent-registry/data-model#service-resources).

Register the MCP server with the tool specification by using the [`gcloud agent-registry services create`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/services/create) command:
    
    
    gcloud agent-registry services create SERVER_NAME \
        --project=PROJECT_ID \
        --location=REGION \
        --display-name="DISPLAY_NAME" \
        --mcp-server-spec-type=tool-spec \
        --mcp-server-spec-content=toolspec.json \
        --interfaces=url=SERVER_URL,protocolBinding=PROTOCOL
    

Replace the following:

  * `SERVER_NAME`: the name you want to give to your MCP server, for example, `custom-mcp-server`. The name must be 4 to 63 characters and can contain only lowercase letters, numbers, and hyphens.
  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region.
  * `DISPLAY_NAME`: the human-readable name that you want to give to your server, for example, `Custom MCP Server`.
  * `SERVER_URL`: the endpoint URL of the MCP server, for example, `https://api.example.com/mcp`.
  * `PROTOCOL`: the protocol binding for the endpoint. Valid values are `jsonrpc`, `http-json`, or `grpc`. For MCP servers, this value is often `jsonrpc`.



###  Terraform 

The specification block you configure determines which resource collection your component belongs to. For a complete mapping of specifications to resource collections, see [Service resources and discovery resources](/agent-registry/data-model#service-resources).

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
      description = "The generated read-only McpServer resource name."
      value       = google_agent_registry_service.mcp_server.registry_resource
    }
    

Replace the following:

  * `REGION`: the registry region.
  * `SERVER_NAME`: the name you want to give to your MCP server, for example, `custom-mcp-server`. The name must be 4 to 63 characters and can contain only lowercase letters, numbers, and hyphens.
  * `DISPLAY_NAME`: the human-readable name that you want to give to your server, for example, `Custom MCP Server`.
  * `SERVER_URL`: the endpoint URL of the MCP server, for example, `https://api.example.com/mcp`.



### Verify registration

List, filter, and view the details of your newly registered MCP server. To confirm that your MCP server was successfully registered, you can [list the servers in your registry](https://docs.cloud.google.com/agent-registry/manage-mcp-tools).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
