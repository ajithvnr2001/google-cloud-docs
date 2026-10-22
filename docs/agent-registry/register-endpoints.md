---
url: https://docs.cloud.google.com/agent-registry/register-endpoints/
title: Register endpoints \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:20.388202+00:00
---

# Register endpoints  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/register-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Register endpoints Stay organized with collections  Save and categorize content based on your preferences. 

In Agent Registry, an [endpoint](https://docs.cloud.google.com/agent-registry/concepts#endpoint) represents a target URL, typically a REST API, that your agents access. By registering these destinations as managed agentic components within Agent Registry, you can centrally govern which external endpoints your fleet of agents can connect to.

This document explains how to explicitly register external endpoints in the registry.

**Warning:** This feature isn't supported in the `us` and `eu` multi-region locations. You must use a supported region or the `global` location. For more information, see [Agent Registry locations](https://docs.cloud.google.com/agent-registry/locations).

## Before you begin

Before you start, [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup). You need [your project ID](https://support.google.com/googleapi/answer/7014113) to perform these tasks.

To use the Google Cloud CLI commands in this document, make sure you have [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).

### Required roles

To get the permissions that you need to register endpoints in Agent Registry, ask your administrator to grant you the [Agent Registry API Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.editor) (`roles/agentregistry.editor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Register an endpoint

Because endpoints are custom, external destinations, use [manual registration](https://docs.cloud.google.com/agent-registry/concepts#registration) to add them to Agent Registry:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Endpoints** tab.

  4. Click **Add endpoint**.

  5. In the **Endpoint details** panel, enter the display name, a description, the geographic region, and the destination URL.

Optionally, click **Test connection** in this panel to test your connection to the destination URL.

**Note:** You can register endpoints that use private URLs. However, the connection test only works for public endpoints, checking if the public URL is reachable. The test doesn't support private URLs or endpoints that require sending authenticated data, such as Agent Runtime on Gemini Enterprise Agent Platform endpoints.
  6. Click **Save**.




###  gcloud 

The specification flags you use determine which resource collection your service belongs to. For a complete mapping of flags to resource collections, see [API resources](https://docs.cloud.google.com/agent-registry/data-model#api-resources).

You create a `Service` resource with an `endpoint-spec-type` of `no-spec`.

Register the endpoint and define its interface connection details:
    
    
    gcloud agent-registry services create ENDPOINT_NAME \
      --project=PROJECT_ID \
      --location=REGION \
      --display-name="DISPLAY_NAME" \
      --endpoint-spec-type=no-spec \
      --interfaces=url=ENDPOINT_URL,protocolBinding=PROTOCOL
    

Replace the following:

  * `ENDPOINT_NAME`: The name you want to give to your endpoint, for example, `my-external-api`.
  * `PROJECT_ID`: The project ID.
  * `REGION`: The registry region.
  * `DISPLAY_NAME`: The human-readable name of the endpoint.
  * `ENDPOINT_URL`: The target URL, for example, `https://api.example.com/v1/data`.
  * `PROTOCOL`: The protocol binding for the interface. Valid values are `http-json`, `grpc`, or `jsonrpc`.



After the `Service` resource is created, Agent Registry automatically generates a read-only `Endpoint` resource on the consumer side that agents and orchestrators can [discover and use](https://docs.cloud.google.com/agent-registry/manage-endpoints).

###  Terraform 

The specification block you configure, for example, `endpoint_spec`, determines which resource collection your service belongs to. For a complete mapping of specifications to resource collections, see [API resources](https://docs.cloud.google.com/agent-registry/data-model#api-resources).

To register an external endpoint, configure the `google_agent_registry_service` resource with the `endpoint_spec` block:
    
    
    resource "google_agent_registry_service" "endpoint" {
      location     = "REGION"
      service_id   = "ENDPOINT_NAME"
      display_name = "DISPLAY_NAME"
      description  = "An external REST API registered using Terraform."
    
      interfaces {
        url              = "ENDPOINT_URL"
        protocol_binding = "PROTOCOL"
      }
    
      endpoint_spec {
        type = "NO_SPEC"
      }
    }
    
    output "endpoint_resource_name" {
      description = "The generated read-only Endpoint resource name."
      value       = google_agent_registry_service.endpoint.registry_resource
    }
    

Replace the following:

  * `REGION`: The registry region.
  * `ENDPOINT_NAME`: The unique name you want to give to your endpoint, for example, `my-external-api`.
  * `DISPLAY_NAME`: The human-readable name of the endpoint.
  * `ENDPOINT_URL`: The target URL, for example, `https://api.example.com/v1/data`.
  * `PROTOCOL`: The protocol binding for the interface. Valid values are `HTTP_JSON`, `GRPC`, or `JSONRPC`.



## Register a composite Google APIs endpoint

In a cross-project architecture, a central governance project hosts shared infrastructure such as Agent Registry and Agent Gateway, and individual workload projects host agent compute instances.

When you route agent traffic through [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) in egress mode, outbound network traffic is blocked by default. To let agents in workload projects communicate with essential Google Cloud APIs, you can group multiple API interfaces into a single composite `Service` endpoint in the central governance project.

Grouping interfaces into a single endpoint simplifies policy administration by letting you manage a single IAP policy binding for the entire suite of core Google APIs.

Follow these steps to register a composite Google APIs endpoint:

###  gcloud 

Register the endpoint with multiple interface URLs in the central governance project:
    
    
    gcloud agent-registry services create SERVICE_NAME \
      --project=CENTRAL_PROJECT_ID \
      --location=REGION \
      --display-name="DISPLAY_NAME" \
      --description="DESCRIPTION" \
      --endpoint-spec-type=no-spec \
      --interfaces=protocolBinding=jsonrpc,url=API_URL \
      --interfaces=protocolBinding=jsonrpc,url=ADDITIONAL_API_URL
    

Replace the following:

  * `SERVICE_NAME`: The identifier for the service, for example, `core-gapi-services`.
  * `CENTRAL_PROJECT_ID`: The project ID of the central governance project hosting Agent Registry and Agent Gateway.
  * `REGION`: The [region](https://docs.cloud.google.com/agent-registry/locations) where your gateway and registry reside.
  * `DISPLAY_NAME`: The human-readable name, for example, `Core Google APIs`.
  * `DESCRIPTION`: A brief description, for example, `Essential Google APIs for agent operations`.
  * `API_URL`: The URL of the primary Google API, such as `https://telemetry.googleapis.com`.
  * `ADDITIONAL_API_URL`: Repeat the `--interfaces` flag for each additional Google API URL or variant required by your agents, such as `https://cloudresourcemanager.googleapis.com`, `https://iamcredentials.googleapis.com`, `https://agentregistry.googleapis.com`, or regional and mTLS variants like `https://telemetry.mtls.googleapis.com`.



###  Terraform 

To register the composite Google APIs endpoint using Terraform, define the `google_agent_registry_service` resource with multiple `interfaces` blocks:
    
    
    resource "google_agent_registry_service" "core_gapi_services" {
      project      = "CENTRAL_PROJECT_ID"
      location     = "REGION"
      service_id   = "SERVICE_NAME"
      display_name = "DISPLAY_NAME"
      description  = "DESCRIPTION"
    
      endpoint_spec {
        type = "NO_SPEC"
      }
    
      interfaces {
        url              = "API_URL"
        protocol_binding = "JSONRPC"
      }
    
      # Add an interfaces block for each additional Google API URL
      interfaces {
        url              = "ADDITIONAL_API_URL"
        protocol_binding = "JSONRPC"
      }
    }
    

Replace the following:

  * `CENTRAL_PROJECT_ID`: The project ID of the central governance project.
  * `REGION`: The registry region.
  * `SERVICE_NAME`: The service ID.
  * `DISPLAY_NAME`: The human-readable name.
  * `DESCRIPTION`: The service description.
  * `API_URL`: The URL of the primary Google API, such as `https://telemetry.googleapis.com`.
  * `ADDITIONAL_API_URL`: Repeat the `interfaces` block for each additional Google API URL or variant required by your agents, such as `https://cloudresourcemanager.googleapis.com`, `https://iamcredentials.googleapis.com`, `https://agentregistry.googleapis.com`, or regional and mTLS variants like `https://telemetry.mtls.googleapis.com`.



## What's next

  * Learn how to [manage and discover registered endpoints](https://docs.cloud.google.com/agent-registry/manage-endpoints).
  * Learn how to [configure IAM egress policies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/configure-iam-policies#agent-to-endpoint) for registered endpoints.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
