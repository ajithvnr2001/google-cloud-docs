---
url: https://docs.cloud.google.com/agent-registry/manual-registration/
title: Use manual registration \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:21.869738+00:00
---

# Use manual registration  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/manual-registration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Use manual registration Stay organized with collections  Save and categorize content based on your preferences. 

You require manual registration in Agent Registry for agents hosted outside Google Cloud, running on unsupported runtimes, or deployed across different Google Cloud projects. This document shows you how to manually register agents in Agent Registry.

**Warning:** This feature isn't supported in the `us` and `eu` multi-region locations. You must use a supported region or the `global` location. For more information, see [Agent Registry locations](https://docs.cloud.google.com/agent-registry/locations). 

## Before you begin

Before you start, [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup). You need [the project ID](https://support.google.com/googleapi/answer/7014113) to perform these tasks.

To use the Google Cloud CLI commands in this document, make sure you have [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).

### Required roles

To get the permissions that you need to manually register agents in Agent Registry, ask your administrator to grant you the following IAM roles on the project: 

  * To register agents in Agent Registry: [Agent Registry API Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.editor) (`roles/agentregistry.editor`) 
  * For cross-project registration, to access agent metadata in a remote project: [Agent Registry API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.viewer) (`roles/agentregistry.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You don't require any additional permissions if the agent's endpoint or Agent Card is accessible using standard public URLs or authenticated through pre-configured credentials.

## Register an A2A-compliant agent

If your remote agent implements [the Agent2Agent (A2A) specification](https://a2a-protocol.org/latest/), direct Agent Registry to the agent's `agent-card.json` payload. The registry automatically synchronizes the [Agent Card](https://agent2agent.info/docs/concepts/agentcard/) and indexes the agent's available [A2A skills](https://docs.cloud.google.com/agent-registry/concepts#a2a-skill) for discovery.

Follow these steps to register the agent:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Agents** tab.

  4. Click **Add agent**.

  5. In the **Agent details** panel, enter the following details:

     * **Type** : Select **A2A**.
     * **Region** : Select the geographic location where you want to register the agent.
  6. Choose one of the following options:

     * To register the agent using its Agent Card URL, select the **From URI** tab and enter a valid URL in the **URI** field. Then, click **Import** to get the Agent Card from the URL.
     * To copy and paste the Agent Card content, select the **Paste JSON** tab and paste the full contents of your `agent-card.json` file.
  7. Click **Save**.




###  gcloud 

The specification flags you use determine which resource collection your service belongs to. For a complete mapping of flags to resource collections, see [API resources](https://docs.cloud.google.com/agent-registry/data-model#api-resources).

To register an A2A agent, save the agent's Agent Card as a local JSON file, for example, `agent-card.json`, and do the following:
    
    
    gcloud agent-registry services create AGENT_NAME \
      --project=PROJECT_ID \
      --location=REGION \
      --display-name="DISPLAY_NAME" \
      --agent-spec-type=a2a-agent-card \
      --agent-spec-content=@agent-card.json
    

The maximum file size for the specification file is 10 KB.

Replace the following:

  * `AGENT_NAME`: The name you want to give to your agent, for example, `my-support-agent`.
  * `PROJECT_ID`: The project ID.
  * `REGION`: The [region](https://docs.cloud.google.com/agent-registry/locations) where you want to register the agent. If you don't want to use a specific region, use the value `global`.
  * `DISPLAY_NAME`: The human-readable name that you want to give to your agent, for example, `Support Agent`.



###  Terraform 

The specification block you configure, for example, `agent_spec`, determines which resource collection your service belongs to. For a complete mapping of specifications to resource collections, see [API resources](https://docs.cloud.google.com/agent-registry/data-model#api-resources).

To register an A2A-compliant agent, configure the `google_agent_registry_service` resource. Specify the `agent_spec` block with the `A2A_AGENT_CARD` type and the `content` representing your Agent Card JSON payload:
    
    
    resource "google_agent_registry_service" "a2a_agent" {
      location     = "REGION"
      service_id   = "AGENT_NAME"
      display_name = "DISPLAY_NAME"
    
      agent_spec {
        type    = "A2A_AGENT_CARD"
        content = jsonencode({
          schemaVersion = "v1"
          displayName   = "DISPLAY_NAME"
          description   = "A custom support agent registered using Terraform."
          skills = [
            {
              name        = "customer_lookup"
              description = "Looks up customer info by email address."
            }
          ]
        })
      }
    }
    
    output "agent_resource_name" {
      description = "The generated read-only Agent resource name."
      value       = google_agent_registry_service.a2a_agent.registry_resource
    }
    

Replace the following:

  * `REGION`: The region where you register the agent.
  * `AGENT_NAME`: The unique name you want to give to your agent, for example, `my-support-agent`.
  * `DISPLAY_NAME`: The human-readable name that you want to give to your agent, for example, `Support Agent`.



## Register a standard REST agent

Standard REST agents are [discoverable](https://docs.cloud.google.com/agent-registry/concepts#discovery) by name and description, but don't have searchable [A2A skills](https://docs.cloud.google.com/agent-registry/concepts#a2a-skill) unless they adopt the [A2A](https://a2a-protocol.org/latest/) protocol.

To register a remote agent that doesn't implement the A2A specification, create a `Service` resource configured with `--agent-spec-type=no-spec`. Agent Registry then generates a corresponding `Agent` resource in the `agents` collection.

Using `--agent-spec-type=no-spec` registers an agent, not a target API destination. If you want to register an external API destination that agents connect to, you must register an endpoint. For instructions, see [Register endpoints](https://docs.cloud.google.com/agent-registry/register-endpoints).

Follow these steps to register the agent:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Agents** tab.

  4. Click **Add agent**.

  5. In the **Agent details** panel, enter the following details:

     * **Type** : Select **Non-A2A**.
     * **Name** : Enter a human-readable display name for your agent, such as `Travel Agent`.
     * **Description** : Enter a description of the agent's capabilities, such as `A test agent that plans travel itineraries.`
     * **Region** : Select the geographic location where you want to register the agent.
     * **Endpoint** : Enter the endpoint where the agent is hosted.
  6. Click **Save**.




###  gcloud 

The specification flags you use determine which resource collection your service belongs to. For a complete mapping of flags to resource collections, see [API resources](https://docs.cloud.google.com/agent-registry/data-model#api-resources).

You can optionally provide the defined `HTTP/JSON` endpoint interface with the `--interfaces` flag so that the registry establishes a connection with the agent.

To register a standard REST agent, do the following:
    
    
    gcloud agent-registry services create AGENT_NAME \
      --project=PROJECT_ID \
      --location=REGION \
      --display-name="DISPLAY_NAME" \
      --agent-spec-type=no-spec \
      --interfaces=url=ENDPOINT_URL,protocolBinding=PROTOCOL
    

Replace the following:

  * `AGENT_NAME`: The name you want to give to your agent, for example, `my-remote-rest-agent`.
  * `PROJECT_ID`: The project ID.
  * `REGION`: The registry region.
  * `DISPLAY_NAME`: The human-readable name that you want to give to your agent, for example, `Remote REST Agent`.
  * `ENDPOINT_URL`: The agent's API endpoint URL, for example, `https://api.remote-service.com/v1/agents/1234`.
  * `PROTOCOL`: The protocol binding for the endpoint. Valid values are `http-json`, `grpc`, or `jsonrpc`.



###  Terraform 

The specification block you configure, for example, `agent_spec`, determines which resource collection your service belongs to. For a complete mapping of specifications to resource collections, see [API resources](https://docs.cloud.google.com/agent-registry/data-model#api-resources).

To register a standard REST agent, configure the `google_agent_registry_service` resource with `agent_spec` set to `NO_SPEC` type, and define the endpoint interface connections:
    
    
    resource "google_agent_registry_service" "rest_agent" {
      location     = "REGION"
      service_id   = "AGENT_NAME"
      display_name = "DISPLAY_NAME"
      description  = "A standard REST agent registered using Terraform."
    
      agent_spec {
        type = "NO_SPEC"
      }
    
      interfaces {
        url              = "ENDPOINT_URL"
        protocol_binding = "PROTOCOL"
      }
    }
    
    output "agent_resource_name" {
      description = "The generated read-only Agent resource name."
      value       = google_agent_registry_service.rest_agent.registry_resource
    }
    

Replace the following:

  * `REGION`: The region where you register the agent.
  * `AGENT_NAME`: The unique name you want to give to your agent, for example, `my-remote-rest-agent`.
  * `DISPLAY_NAME`: The human-readable name that you want to give to your agent, for example, `Remote REST Agent`.
  * `ENDPOINT_URL`: The agent's API endpoint URL, for example, `https://api.remote-service.com/v1/agents/1234`.
  * `PROTOCOL`: The protocol binding for the endpoint. Valid values are `HTTP_JSON`, `GRPC`, or `JSONRPC`.



## Register an agent from another project

If your organization deploys agents across multiple Google Cloud projects and uses a central [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) to govern egress traffic, you can register agents from spoke or workload projects into the central Agent Registry catalog.

Because automatic registration only discovers resources created in the same project, you must manually register each remote agent into the central governance project's registry.

### Considerations for cross-project registration

Before you register agents across projects, review the following:

  * **Compatible locations** : The Agent Registry instance, the Agent Gateway, and the agent endpoints must reside in the same geographic region or the `global` location.
  * **Automatic discovery limitation** : Automatic cross-project discovery is not supported. You must manually register each remote agent.
  * **Lifecycle management** : Manual entries in Agent Registry are not automatically updated or deleted when changes occur in the remote project. You must manage the lifecycle of these entries in the central registry when remote agents are modified or removed.
  * **Egress mode only** : Cross-project governance with Agent Gateway is supported only for Agent-to-Anywhere (egress) gateways. Client-to-Agent ingress gateways require the agent and gateway to be in the same project.



### Register the remote agent

To manually register an agent from another project, follow these steps:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the central governance Google Cloud project where you want to register the agent.

  3. Select the **Agents** tab.

  4. Click **Add agent**.

  5. In the **Agent details** panel, enter the following details:

     * **Type** : Select **A2A** if the remote agent implements the A2A protocol, or **Non-A2A** for a standard REST endpoint.
     * **Region** : Select the region matching your central gateway and remote agent deployment.
  6. Provide the agent endpoint:

     * For A2A agents, select **From URI** and enter the remote agent's Agent Card URL, or select **Paste JSON** and paste the `agent-card.json` content.
     * For non-A2A agents, enter the **Endpoint** URL of the remote agent.
  7. Click **Save**.




###  gcloud 

The specification flags you use determine which resource collection your service belongs to. For a complete mapping of flags to resource collections, see [API resources](https://docs.cloud.google.com/agent-registry/data-model#api-resources).

  * **A2A agent** : To register an A2A agent from another project using the gcloud CLI, run the following command in the central governance project:


    
    
    gcloud agent-registry services create AGENT_NAME \
      --project=CENTRAL_PROJECT_ID \
      --location=REGION \
      --display-name="DISPLAY_NAME" \
      --agent-spec-type=a2a-agent-card \
      --agent-spec-content=@agent-card.json
    

  * **REST agent** : To register a standard REST agent from another project, run the following command in the central governance project:


    
    
    gcloud agent-registry services create AGENT_NAME \
      --project=CENTRAL_PROJECT_ID \
      --location=REGION \
      --display-name="DISPLAY_NAME" \
      --agent-spec-type=no-spec \
      --interfaces=url=REMOTE_ENDPOINT_URL,protocolBinding=PROTOCOL
    

Replace the following:

  * `AGENT_NAME`: The name for your agent in the central registry, for example, `remote-support-agent`.
  * `CENTRAL_PROJECT_ID`: The project ID of the central governance project.
  * `REGION`: The region where you register the agent.
  * `DISPLAY_NAME`: The human-readable name for the agent, for example, `Remote Support Agent`.
  * `REMOTE_ENDPOINT_URL`: The endpoint URL of the agent running in the remote project, for example, `https://<var>AGENT_SERVICE_NAME</var>-<var>HASH</var>.<var>REGION</var>.run.app`.
  * `PROTOCOL`: The protocol binding for the endpoint. Valid values are `http-json`, `grpc`, or `jsonrpc`.



###  Terraform 

The specification block you configure, for example, `agent_spec`, determines which resource collection your service belongs to. For a complete mapping of specifications to resource collections, see [API resources](https://docs.cloud.google.com/agent-registry/data-model#api-resources).

To register a remote agent in a central governance project using Terraform, configure the `google_agent_registry_service` resource and specify the central project:
    
    
    resource "google_agent_registry_service" "remote_agent" {
      project      = "CENTRAL_PROJECT_ID"
      location     = "REGION"
      service_id   = "AGENT_NAME"
      display_name = "DISPLAY_NAME"
      description  = "Remote agent registered from project REMOTE_PROJECT_ID."
    
      agent_spec {
        type = "NO_SPEC"
      }
    
      interfaces {
        url              = "REMOTE_ENDPOINT_URL"
        protocol_binding = "PROTOCOL"
      }
    }
    
    output "agent_resource_name" {
      description = "The generated read-only Agent resource name."
      value       = google_agent_registry_service.remote_agent.registry_resource
    }
    

Replace the following:

  * `CENTRAL_PROJECT_ID`: The project ID of the central governance project.
  * `REGION`: The region where you register the agent.
  * `AGENT_NAME`: The unique name for your agent in the registry, for example, `remote-support-agent`.
  * `DISPLAY_NAME`: The human-readable name for the agent, for example, `Remote Support Agent`.
  * `REMOTE_PROJECT_ID`: The project ID where the agent is hosted.
  * `REMOTE_ENDPOINT_URL`: The endpoint URL of the agent running in the remote project.
  * `PROTOCOL`: The protocol binding for the endpoint. Valid values are `HTTP_JSON`, `GRPC`, or `JSONRPC`.



## Verify registration

After registering your agent, verify that Agent Registry successfully processed the `Service` and created the corresponding `Agent` resource:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Agents** tab.

The page displays a list of all registered agents and their details.




###  gcloud 
    
    
    gcloud agent-registry agents list \
      --project=PROJECT_ID \
      --location=REGION
    

If you have multiple agents, or if you want to confirm the registration of a single agent, you can filter the list by the agent's metadata:
    
    
    gcloud agent-registry agents list \
      --project=PROJECT_ID \
      --location=REGION \
      --filter="FILTER_EXPRESSION"
    

Replace the following:

  * `PROJECT_ID`: The project ID.
  * `REGION`: The [region](https://docs.cloud.google.com/agent-registry/locations) where you want to register the agent. If you don't want to use a specific region, use the value `global`.
  * `FILTER_EXPRESSION`: The filter expression for the agents that you want to filter. For example, to filter by display name, you can use `displayName='DISPLAY_NAME'`. To filter by the globally unique [identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers) (URN), you can use `agentId='urn:agent:AGENT_URN'`.



###  Terraform 

Reference your registered agent in other Terraform configurations by using the `google_agent_registry_agent` data source:
    
    
    data "google_agent_registry_agent" "my_agent" {
      location = "REGION"
      filter = "displayName=\"DISPLAY_NAME\""
    }
    
    output "agent_urn" {
      value = data.google_agent_registry_agent.my_agent.urn
    }
    

Replace the following:

  * `REGION`: The registry region.
  * `DISPLAY_NAME`: The human-readable display name of the agent.



## What's next

  * Learn how to [manage registered agents](https://docs.cloud.google.com/agent-registry/manage-agents).
  * Learn about [automatic registration](https://docs.cloud.google.com/agent-registry/automatic-registration), the recommended method to register agents deployed to managed runtimes.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
