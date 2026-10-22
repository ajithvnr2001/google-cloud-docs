---
url: https://docs.cloud.google.com/agent-registry/manage-agents/
title: Manage agents \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:14.134601+00:00
---

# Manage agents  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/manage-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Manage agents Stay organized with collections  Save and categorize content based on your preferences. 

Effective management of your fleet of agents requires keeping the registry accurate by viewing and updating agent details as your AI ecosystem evolves, overriding metadata or removing agents that are no longer in use.

This document details how to view and modify your registered agents' details and configuration.

## Before you begin

Before you manage agents, make sure [your agents are registered](https://docs.cloud.google.com/agent-registry/register-agents) in Agent Registry. You also need [your project ID](https://support.google.com/googleapi/answer/7014113) to perform these tasks.

To use the Google Cloud CLI commands in this document, make sure you have [set up your gcloud CLI environment](https://docs.cloud.google.com/agent-registry/setup#set-up-cli).

### Required roles

To get the permissions that you need to manage registered agents in Agent Registry, ask your administrator to grant you the [Agent Registry API Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.editor) (`roles/agentregistry.editor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Discover available agents

After registering agents, you can discover them in your environment and view their detailed configurations, such as their endpoints, skills, and associated metadata.

### List and view all agents

You can list all agents registered in your environment and view their detailed configurations, such as their endpoints, [A2A skills](https://docs.cloud.google.com/agent-registry/concepts#a2a-skill), and associated metadata:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Agents** tab.

The page displays a list of all registered agents. The list includes the agent's name, [identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers), type, description, version, runtime, and location.

  4. To view the full details of an agent, click the agent's name.




###  gcloud 

To list all agents in a specific location, use the `agents list` command:
    
    
    gcloud agent-registry agents list \
      --project=PROJECT_ID \
      --location=REGION
    

Replace the following:

  * `PROJECT_ID`: The project ID.
  * `REGION`: The registry region.



### Filter registered agents

If you have multiple agents, or if you want to confirm the registration of a specific agent, you can filter the list by the agent's metadata:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Agents** tab.

The page displays a list of all registered agents. The list includes the agent's name, [identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers), type, description, version, runtime, and location.

  4. Filter the list by the agent's location or their runtime resource:

     * To filter by location, click the **Location** menu, select the locations you want to filter, and click **Apply**.
     * To filter by runtime, click the **Runtime** menu, select the runtimes you want to filter, and click **Apply**.

The page displays a filtered list of the registered agents for your selected conditions.




###  gcloud 

Filter your agent list to only return resources matching specific metadata, using the `--filter` flag:
    
    
    gcloud agent-registry agents list \
      --project=PROJECT_ID \
      --location=REGION \
      --filter="FILTER_EXPRESSION"
    

Replace `FILTER_EXPRESSION` with the filter expression for the agents that you want to filter. For example, you can use the following filters:

  * To filter by display name, use `displayName='DISPLAY_NAME'`.
  * To search by the globally unique [identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers) (URN), use `agentId='urn:agent:AGENT_URN'`.



###  Terraform 

To retrieve a specific registered agent by filtering against its metadata, configure the `google_agent_registry_agent` data source with the `filter` argument:
    
    
    data "google_agent_registry_agent" "filtered_agent" {
      location = "REGION"
      filter   = "displayName=\"DISPLAY_NAME\""
    }
    

Replace the following:

  * `REGION`: The registry region.
  * `DISPLAY_NAME`: The human-readable name of the agent to filter by, for example, `Support Agent`.



### View details of an agent

View details from a specific agent, including its protocols, skills, and identity:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Agents** tab.

The page displays a list of all registered agents. The list includes the agent's name, [identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers), type, description, version, runtime, and location.

  4. Click the name of the agent that you want to view.

The details page includes tabs for the agent details.

  5. Click the corresponding tab to view specific agent details.

Feature availability depends on your runtime. Tabs like **Sessions** , **Playground** , **Memories** , and **Evaluation** are specific capabilities that display for agents built on managed runtimes, such as Agent Runtime on Gemini Enterprise Agent Platform:

     * **Overview** : Core details from the agent, including the agent's name, [identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers), location, description, and runtime. The overview also displays [A2A skills](https://docs.cloud.google.com/agent-registry/concepts#a2a-skill) and the [runtime reference](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#runtime-references), which you require for building queries in the [topology graph](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology#registered-agent).
     * **Observability** : Application-centric insights such as latency, traffic, errors, and token spend. This tab integrates with Google Cloud Observability tools to display real-time performance metrics and system-level utilization to help you manage costs and user experience. For more information, see the [Observability overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/overview).
     * **Traces** : The exact path of a conversation step-by-step, including detailed formatting of input and assistant messages to debug complex multi-agent reasoning loops or tool invocation errors in real time. For more information, see [View agent traces](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/traces).
     * **Security** : Findings from Model Armor and Security Command Center, including content policy violations, data leakage risks, and compliance assessments. For more information on security, see [View security findings](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/view-security-findings).
     * **Topology** : A visual map of the relationships and traffic flows between an agent, its assigned Agent Gateway, and the MCP servers it interacts with. For more information on Agent Gateway, see the [Agent Gateway overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview). For more information on topology, see [View graphs for a registered agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology#registered-agent).
     * **Identity** : The [agent principal](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-principals) used for policy enforcement. You use this identity, for example, to configure [auth provider bindings](https://docs.cloud.google.com/agent-registry/manage-bindings#auth-provider) for [authentication to tools and resources](https://docs.cloud.google.com/agent-registry/authenticate-toolsets).
     * **Sessions** : Persistent conversation history and tracking of active interactions with the agent.
     * **Playground** : A direct chat interface to test the agent's behavior.
     * **Memories** : Long-term personalization features that generate or recall details from past conversations with the agent to preserve context across interactions.
     * **Evaluation** : Details of all agent evaluation tasks. This tab lets you create new evaluation tasks, upload metrics, and evaluate the agent's cognitive performance and model reliability against live traffic or synthetic simulations.



###  gcloud 

To view the detailed metadata of a specific agent, use the `agents describe` command:
    
    
    gcloud agent-registry agents describe AGENT_NAME \
      --project=PROJECT_ID \
      --location=REGION
    

Replace `AGENT_NAME` with the name of your agent, for example, `my-custom-agent`.

###  Terraform 

To retrieve details about a specific registered agent using its ID, configure the `google_agent_registry_agent` data source:
    
    
    data "google_agent_registry_agent" "my_agent" {
      location = "REGION"
      agent_id = "AGENT_ID"
    }
    
    output "agent_create_time" {
      description = "The timestamp when the agent was registered."
      value       = data.google_agent_registry_agent.my_agent.create_time
    }
    
    output "agent_update_time" {
      description = "The timestamp when the agent was last updated."
      value       = data.google_agent_registry_agent.my_agent.update_time
    }
    

Replace the following:

  * `REGION`: The registry region.
  * `AGENT_ID`: The unique identifier of your agent, for example, `my-custom-agent`.



## Update agent metadata and endpoints

If your agent's runtime URL changes, or you want to override its display name, description, or specification, you can update the agent metadata.

For the Agent Registry API, `Agent` resources are used for discovery. Therefore, you must update the registered `Service` resource directly.

###  Console 

Update available agent details from the Google Cloud console:

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Agents** tab.

The page displays a list of all registered agents. The list includes the agent's name, [identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers), type, description, version, runtime, and location.

  4. Click the name of the agent that you want to update.

  5. On the **Overview** tab of the agent, click edit **Edit**.

  6. In the **Edit service** panel, enter the updated information of your agent, such as its new name or description.

  7. Click **Save**.




###  gcloud 

Use the gcloud CLI with specific flags to modify the agent's parameters:

  * **Update the display name and description** : Use the `--display-name` and `--description` flags, for example:
        
        gcloud agent-registry services update AGENT_NAME \
          --project=PROJECT_ID \
          --location=REGION \
          --display-name="New display name" \
          --description="Updated description of the agent's purpose."
        

Replace the following:

    * `AGENT_NAME`: The name of your agent, for example, `my-support-agent`.
    * `PROJECT_ID`: The project ID.
    * `REGION`: The registry region.
  * **Update the endpoint URL** : Use the `--interfaces` flag to specify the new endpoint, for example:
        
        gcloud agent-registry services update AGENT_NAME \
          --project=PROJECT_ID \
          --location=REGION \
          --interfaces=url=ENDPOINT_URL,protocolBinding=PROTOCOL
        

Replace the following:

    * `ENDPOINT_URL`: The new agent endpoint URL, for example, `https://new-api.example.com/agent`.
    * `PROTOCOL`: The protocol binding for the endpoint. Valid values are `http-json`, `grpc`, or `jsonrpc`.
  * **Update the agent's specification** : Use the `--agent-spec-type` and `--agent-spec-content` flags, for example, if you have a new [Agent Card](https://agent2agent.info/docs/concepts/agentcard/):
        
        gcloud agent-registry services update AGENT_NAME \
          --project=PROJECT_ID \
          --location=REGION \
          --agent-spec-type=a2a-agent-card \
          --agent-spec-content=@AGENT_SPEC_FILE
        

Replace `AGENT_SPEC_FILE` with the path to the new agent specification file, for example, `new-agent-card.json`. Note the `@` prefix required when passing the path to `--agent-spec-content`. The maximum file size for the specification file is 10 KB.




###  Terraform 

To update your registered agent's metadata, endpoint URL, or specification, modify the parameters of the existing `google_agent_registry_service` resource in your configuration, and then run `terraform apply`:
    
    
    resource "google_agent_registry_service" "rest_agent" {
      location     = "REGION"
      service_id   = "AGENT_NAME"
      display_name = "New Display Name"
      description  = "Updated description of the agent's purpose."
    
      agent_spec {
        type = "NO_SPEC"
      }
    
      interfaces {
        url              = "ENDPOINT_URL"
        protocol_binding = "PROTOCOL"
      }
    }
    

Replace the following:

  * `REGION`: The registry region.
  * `AGENT_NAME`: The unique name you want to give to your agent, for example, `my-support-agent`.
  * `ENDPOINT_URL`: The agent's API endpoint URL, for example, `https://api.remote-service.com/v1/agents/1234`.
  * `PROTOCOL`: The protocol binding for the endpoint. Valid values are `HTTP_JSON`, `GRPC`, or `JSONRPC`.



## Remove an agent

To delete agents that were automatically registered to Agent Registry, you must delete the underlying agent in its specific Google Cloud runtime. The agent is then automatically removed from the registry.

To remove a manually registered agent from the registry, you must delete the underlying `Service` resource. This action removes the agent from search results and makes it undiscoverable to other tools:

###  Console 

  1. In the Google Cloud console, go to **Agent Registry** :

[Go to Agent Registry](https://console.cloud.google.com/agent-platform/agent-registry)

  2. From the project picker, select the Google Cloud project where you [set up Agent Registry](https://docs.cloud.google.com/agent-registry/setup).

  3. Select the **Agents** tab.

The page displays a list of all registered agents. The list includes the agent's name, [identifier](https://docs.cloud.google.com/agent-registry/identity-and-identifiers#agent-identifiers), type, description, version, runtime, and location.

  4. Click the name of the agent that you want to remove.

  5. On the **Overview** tab of the agent, click delete **Delete**.

  6. In the confirmation dialog, type _DELETE_ to confirm the action.

  7. Click **Delete**.




###  gcloud 
    
    
    gcloud agent-registry services delete AGENT_NAME \
      --project=PROJECT_ID \
      --location=REGION
    

Replace the following:

  * `AGENT_NAME`: The name of the agent you want to remove, for example, `my-support-agent`.
  * `PROJECT_ID`: The project ID.
  * `REGION`: The registry region.



###  Terraform 

Remove the `google_agent_registry_service` resource representing the agent from your Terraform configuration, and then run `terraform apply`.

## What's next

  * Learn how to [view agent relationships](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/topology) using a topology graph.
  * Learn how to [search for agents and tools](https://docs.cloud.google.com/agent-registry/search-agents-and-tools) using natural language queries.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
