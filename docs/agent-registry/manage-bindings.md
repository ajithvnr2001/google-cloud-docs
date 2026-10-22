---
url: https://docs.cloud.google.com/agent-registry/manage-bindings/
title: Manage bindings \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:11.035720+00:00
---

# Manage bindings  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/manage-bindings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Manage bindings Stay organized with collections  Save and categorize content based on your preferences. 

In Agent Registry, a [binding](https://docs.cloud.google.com/agent-registry/concepts#binding) represents a connection between a source agent and a target resource, such as another agent, an MCP server, or an endpoint. By creating bindings, you establish explicit relationships that let your orchestrator agents interact with downstream capabilities.

You use bindings to handle two scenarios:

  * **Resource connections:** You can link a source agent to a target resource, such as another agent, an MCP server, or an endpoint. This scenario lets you map out multi-agent workflows where a primary orchestrator delegates tasks to specialized sub-agents or tools.
  * **Delegated permissions:** You can associate an agent with an [auth provider](https://docs.cloud.google.com/agent-registry/concepts#auth-provider) to let your agent connect to external targets or custom tools using its own credentials or on behalf of an individual user. This binding is required if your agent needs to authenticate to remote MCP servers or tools using OAuth tokens or API keys. With bindings, you don't have to manually define auth providers in your code. For detailed instructions, see Create an auth provider binding in this document.



This document describes how to create, view, update, and delete bindings in Agent Registry.

**Warning:** This feature isn't supported in the `us` and `eu` multi-region locations. You must use a supported region or the `global` location. For more information, see [Agent Registry locations](https://docs.cloud.google.com/agent-registry/locations).

## Before you begin

Before you can manage bindings, complete the following:

  1. [Set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).
  2. Register the source and target components. For more information, see [Register agentic components](https://docs.cloud.google.com/agent-registry/overview#register).
  3. If you want to configure bindings for delegated permissions, create an auth provider with [Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/agent-identity-overview#agent-auth-manager). For more information, see [Authenticate to tools and resources](https://docs.cloud.google.com/agent-registry/authenticate-toolsets).
  4. To use the Google Cloud CLI commands in this document, make sure you have [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).



### Required roles

To get the permissions that you need to manage bindings in Agent Registry, ask your administrator to grant you the following IAM roles on the project: 

  * Create, update, and delete bindings: [Agent Registry API Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.admin) (`roles/agentregistry.admin`) 
  * View bindings: [Agent Registry API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.viewer) (`roles/agentregistry.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a binding

Create a binding to connect a source agent to a target resource:

###  gcloud 
    
    
    gcloud agent-registry bindings create BINDING_NAME \
      --project=PROJECT_ID \
      --location=REGION \
      --display-name="DISPLAY_NAME" \
      --source-identifier="SOURCE_ID" \
      --target-identifier="TARGET_ID"
    

Replace the following:

  * `BINDING_NAME`: The name you want to give to the binding, for example, `my-custom-binding`.
  * `PROJECT_ID`: The project ID.
  * `REGION`: The registry region.
  * `DISPLAY_NAME`: The human-readable name that you want to give to your binding, for example, `My Custom Binding`.
  * `SOURCE_ID`: The [identifier](https://docs.cloud.google.com/agent-registry/concepts#agent-identifier) of the source agent in Uniform Resource Name (URN) format.
  * `TARGET_ID`: The identifier of the target resource in URN format, such as an [MCP server identifier](https://docs.cloud.google.com/agent-registry/concepts#mcp-server-identifier).



###  Terraform 

To create a binding between a source agent and a target resource, configure a `google_agent_registry_binding` resource. A binding requires the `target` block:
    
    
    resource "google_agent_registry_binding" "agent_binding" {
      location     = "REGION"
      binding_id   = "BINDING_NAME"
      display_name = "DISPLAY_NAME"
      description  = "Connects a source agent to a target resource."
    
      source {
        identifier = "urn:agent:my-publisher:my-namespace:SOURCE_AGENT_NAME"
      }
    
      target {
        identifier = "urn:mcp:my-publisher:my-namespace:TARGET_RESOURCE_NAME"
      }
    }
    

Replace the following:

  * `REGION`: The registry region.
  * `BINDING_NAME`: The unique name you want to give to the binding.
  * `DISPLAY_NAME`: The human-readable name of the binding.
  * `SOURCE_AGENT_NAME`: The name of the source agent.
  * `TARGET_RESOURCE_NAME`: The name of the target resource, such as an MCP server or endpoint.



### Create an auth provider binding

You can associate an agent with an [auth provider](https://docs.cloud.google.com/agent-registry/concepts#auth-provider) for delegated permissions. Before you create this binding, you must first create the auth provider with [Agent Identity auth manager](https://docs.cloud.google.com/iam/docs/agent-identity-overview#agent-auth-manager). For more information, see [Authenticate to tools and resources](https://docs.cloud.google.com/agent-registry/authenticate-toolsets).

When specifying the `--auth-provider` resource name, you must use your project ID:

###  gcloud 
    
    
    gcloud agent-registry bindings create BINDING_NAME \
      --project=PROJECT_ID \
      --location=REGION \
      --display-name="DISPLAY_NAME" \
      --source-identifier="SOURCE_ID" \
      --auth-provider="projects/PROJECT_ID/locations/REGION/connectors/AUTH_PROVIDER_ID"
    

Replace `AUTH_PROVIDER_ID` with the ID of your auth provider.

###  Terraform 

To configure an auth provider binding in Terraform, specify the `auth_provider_binding` block with the full resource path of your connector auth provider, along with its scopes and continue URI:
    
    
    resource "google_agent_registry_binding" "auth_binding" {
      location     = "REGION"
      binding_id   = "BINDING_NAME"
      display_name = "DISPLAY_NAME"
    
      source {
        identifier = "urn:agent:my-publisher:my-namespace:SOURCE_AGENT_NAME"
      }
    
      target {
        identifier = "urn:mcp:my-publisher:my-namespace:TARGET_RESOURCE_NAME"
      }
    
      auth_provider_binding {
        auth_provider = "projects/PROJECT_ID/locations/REGION/connectors/AUTH_PROVIDER_ID"
        scopes        = [SCOPES]
        continue_uri  = "CONTINUE_URI"
      }
    }
    

Replace the following:

  * `REGION`: The registry region.
  * `BINDING_NAME`: The unique name you want to give to the binding.
  * `DISPLAY_NAME`: The human-readable name of the binding.
  * `SOURCE_AGENT_NAME`: The name of the source agent.
  * `TARGET_RESOURCE_NAME`: The name of the target resource, such as an MCP server or endpoint.
  * `PROJECT_ID`: The project ID.
  * `AUTH_PROVIDER_ID`: The ID of the connector auth provider.
  * `SCOPES`: A comma-separated list of OAuth2 scopes, for example, `"https://www.googleapis.com/auth/cloud-platform"`.
  * `CONTINUE_URI`: The continue URI of the auth provider, for example, `https://example.com/continue`.



For examples of how to use these bindings in your agent code, see [Resolve bindings in your Agent Development Kit (ADK) code](https://docs.cloud.google.com/agent-registry/authenticate-toolsets#bindings-in-code).

## List bindings

List all bindings in a specific location:
    
    
    gcloud agent-registry bindings list \
      --project=PROJECT_ID \
      --location=REGION
    

## View binding details

Retrieve the details of a single binding:
    
    
    gcloud agent-registry bindings describe BINDING_NAME \
      --project=PROJECT_ID \
      --location=REGION
    

## Update a binding

Update the parameters of an existing binding, such as its display name or description, using gcloud CLI flags:

###  gcloud 
    
    
    gcloud agent-registry bindings update BINDING_NAME \
      --project=PROJECT_ID \
      --location=REGION \
      --display-name="NEW_DISPLAY_NAME"
    

###  Terraform 

To update a binding's display name or description using Terraform, modify the existing `google_agent_registry_binding` resource in your configuration and run `terraform apply`.

## Delete a binding

To remove a connection between resources, delete the binding record:

###  gcloud 
    
    
    gcloud agent-registry bindings delete BINDING_NAME \
      --project=PROJECT_ID \
      --location=REGION
    

###  Terraform 

Remove the `google_agent_registry_binding` resource representing the binding from your Terraform configuration, and then run `terraform apply`.

## What's next

  * Learn how to [authenticate to tools and resources](https://docs.cloud.google.com/agent-registry/authenticate-toolsets) using auth provider bindings.
  * Learn how to [resolve endpoints and build orchestrators](https://docs.cloud.google.com/agent-registry/resolve-endpoints-and-build-orchestrators) using ADK.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
