---
url: https://docs.cloud.google.com/agent-registry/manage-endpoints/
title: Manage and discover endpoints \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:15.872713+00:00
---

# Manage and discover endpoints  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/manage-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Manage and discover endpoints Stay organized with collections  Save and categorize content based on your preferences. 

Agent Registry lets you discover, update, and remove registered endpoints so that your agents route traffic to valid target URLs. You can inspect available endpoints across your project, update their connection details as your infrastructure changes, and remove endpoints that are no longer in use.

## Before you begin

  1. [Register endpoints](https://docs.cloud.google.com/agent-registry/register-endpoints) in Agent Registry.
  2. Get [the project ID](https://support.google.com/googleapi/answer/7014113) for the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled.
  3. To use the Google Cloud CLI commands in this document, [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).



### Required roles

To get the permissions that you need to manage endpoints in Agent Registry, ask your administrator to grant you the following IAM roles on the [governance project](https://docs.cloud.google.com/agent-registry/overview#governance-project) where Agent Registry is enabled: 

  * Discover endpoints: [Agent Registry API Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.viewer) (`roles/agentregistry.viewer`) 
  * Update and delete endpoints: [Agent Registry API Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.editor) (`roles/agentregistry.editor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Discover endpoints

To browse the target URLs and REST APIs registered in your environment, list the available `Endpoint` resources.

### List all endpoints

List all registered endpoints in your environment:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Endpoints** tab.

The page displays a list of all registered endpoints and their details, such as name, description, and location.

  4. To view the full connection details of an endpoint, click the endpoint's name.




###  gcloud 

To list all endpoints in a specific location, run the [`gcloud agent-registry endpoints list`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/endpoints/list) command:
    
    
    gcloud agent-registry endpoints list \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region.



### Filter registered endpoints

If you have multiple endpoints, you can filter the list by the endpoint's metadata:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Endpoints** tab.

The page displays a list of all registered endpoints and their details, such as name, description, and location.

  4. To filter by location, click the **Location** menu, select the locations you want to filter, and click **Apply**.

The page displays a filtered list of the registered endpoints for your selected conditions.




###  gcloud 

Filter your list to only return resources matching specific metadata by passing the `--filter` flag to the [`gcloud agent-registry endpoints list`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/endpoints/list) command:
    
    
    gcloud agent-registry endpoints list \
        --project=PROJECT_ID \
        --location=REGION \
        --filter="FILTER_EXPRESSION"
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region.
  * `FILTER_EXPRESSION`: the filter expression for the endpoints that you want to filter. For example, to filter by display name, use `displayName='DISPLAY_NAME'`. To filter by the globally unique [endpoint identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#endpoint-identifiers) (URN), use `endpointId='urn:endpoint:ENDPOINT_URN'`.



###  Terraform 

To retrieve a specific registered endpoint by filtering against its metadata, configure the `google_agent_registry_endpoint` data source with the `filter` argument:
    
    
    data "google_agent_registry_endpoint" "filtered_endpoint" {
      location = "REGION"
      filter   = "displayName=\"DISPLAY_NAME\""
    }
    

Replace the following:

  * `REGION`: the registry region.
  * `DISPLAY_NAME`: the human-readable name of the endpoint to filter by, for example, `Example API Endpoint`.



### View details from an endpoint

View details from a specific endpoint, including its connection details and protocol bindings:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Endpoints** tab.

The page displays a list of all registered endpoints and their details, such as name, description, and location.

  4. Click the name of the endpoint that you want to view.

The **Overview** page displays the name, description, location, and connection details of the endpoint, including the destination URL and the protocol bindings.




###  gcloud 

Retrieve detailed metadata about a specific endpoint, including its full interface URL and protocol binding, by running the [`gcloud agent-registry endpoints describe`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/endpoints/describe) command:
    
    
    gcloud agent-registry endpoints describe ENDPOINT_NAME \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region.
  * `ENDPOINT_NAME`: the name of your endpoint, for example, `my-external-api`.



###  Terraform 

To retrieve details about a specific registered endpoint using its ID, configure the `google_agent_registry_endpoint` data source:
    
    
    data "google_agent_registry_endpoint" "my_endpoint" {
      location    = "REGION"
      endpoint_id = "ENDPOINT_NAME"
    }
    
    output "endpoint_create_time" {
      description = "The timestamp when the endpoint was registered."
      value       = data.google_agent_registry_endpoint.my_endpoint.create_time
    }
    
    output "endpoint_update_time" {
      description = "The timestamp when the endpoint was last updated."
      value       = data.google_agent_registry_endpoint.my_endpoint.update_time
    }
    

Replace the following:

  * `REGION`: the registry region.
  * `ENDPOINT_NAME`: the unique identifier of your endpoint, for example, `my-external-api`.



## Update an endpoint

If the underlying URL of an external target endpoint changes, you can update the endpoint interface details.

In Agent Registry, `Endpoint` resources are read-only discovery resources. Therefore, to update a registered endpoint, you must update its writable `Service` resource directly.

Follow these steps to update an endpoint:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Endpoints** tab.

The page displays a list of all registered endpoints and their details, such as name, description, and location.

  4. Click the name of the endpoint that you want to update.

The **Overview** page displays the name, description, location, and connection details of the endpoint, including the destination URL and the protocol bindings.

  5. Click edit **Edit**.

  6. In the **Edit service** panel, enter the updated information for the endpoint, such as the display name, description, and destination URL. You can test the connection to the endpoint from this panel.

  7. Click **Save**.




###  gcloud 

Run the [`gcloud agent-registry services update`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/services/update) command with the `--interfaces` flag to specify the new target URL:
    
    
    gcloud agent-registry services update ENDPOINT_NAME \
        --project=PROJECT_ID \
        --location=REGION \
        --interfaces=url=ENDPOINT_URL,protocolBinding=PROTOCOL
    

Replace the following:

  * `ENDPOINT_NAME`: the name of your endpoint, for example, `my-external-api`.
  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region.
  * `ENDPOINT_URL`: the new target URL, for example, `https://new-api.example.com/v1/data`.
  * `PROTOCOL`: the protocol binding for the interface. Valid values are `http-json`, `grpc`, or `jsonrpc`.



###  Terraform 

To update an endpoint URL or protocol binding using Terraform, modify the `interfaces` block of your existing `google_agent_registry_service` resource in your configuration, and then run `terraform apply`:
    
    
    resource "google_agent_registry_service" "endpoint" {
      location     = "REGION"
      service_id   = "ENDPOINT_NAME"
      display_name = "DISPLAY_NAME"
    
      interfaces {
        url              = "ENDPOINT_URL"
        protocol_binding = "PROTOCOL"
      }
    
      endpoint_spec {
        type = "NO_SPEC"
      }
    }
    

Replace the following:

  * `REGION`: the registry region.
  * `ENDPOINT_NAME`: the name of your endpoint.
  * `DISPLAY_NAME`: the human-readable name of the endpoint.
  * `ENDPOINT_URL`: the new target URL, for example, `https://new-api.example.com/v1/data`.
  * `PROTOCOL`: the protocol binding for the interface. Valid values are `HTTP_JSON`, `GRPC`, or `JSONRPC`.



## Remove an endpoint

To remove an endpoint from the registry, you must delete its `Service` resource. This action immediately removes the endpoint from discovery search results.

Follow these steps to remove an endpoint from your registry:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Endpoints** tab.

The page displays a list of all registered endpoints and their details, such as name, description, and location.

  4. Click the name of the endpoint that you want to remove.

The **Overview** page displays the name, description, location, and connection details of the endpoint, including the destination URL and the protocol bindings.

  5. Click delete **Delete**.

  6. In the **Delete endpoint** window, enter `DELETE` to confirm the action.

  7. Click **Delete**.




###  gcloud 

Run the [`gcloud agent-registry services delete`](https://docs.cloud.google.com/sdk/gcloud/reference/agent-registry/services/delete) command:
    
    
    gcloud agent-registry services delete ENDPOINT_NAME \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `ENDPOINT_NAME`: the name of the endpoint you want to remove, for example, `my-external-api`.
  * `PROJECT_ID`: the project ID.
  * `REGION`: the registry region.



###  Terraform 

Remove the `google_agent_registry_service` resource representing the endpoint from your Terraform configuration, and then run `terraform apply`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
