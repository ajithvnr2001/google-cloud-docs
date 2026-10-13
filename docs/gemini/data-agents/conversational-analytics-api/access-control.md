---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control/
title: Conversational Analytics API access control with IAM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:41.039612+00:00
---

# Conversational Analytics API access control with IAM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Conversational Analytics API access control with IAM Stay organized with collections  Save and categorize content based on your preferences. 

The Conversational Analytics API uses [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) for access control, which lets you share data agents and control who has permission to create, manage, and interact with them. This page describes the predefined IAM roles that you can assign to [_principals_](https://docs.cloud.google.com/iam/docs/overview#principals) (such as users, groups, and service accounts) to grant these permissions.

In addition to IAM, you can use [organization policies](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/organization-policies) to set constraints on Conversational Analytics API resources to control how they can be used at the organization, folder, or project level.

## Before you begin

To get the permissions that you need to assign Conversational Analytics API IAM roles, ask your administrator to grant you the [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) IAM role on the project in which the Conversational Analytics API is enabled. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to assign Conversational Analytics API IAM roles. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Overview of Conversational Analytics API IAM roles

Predefined IAM roles for the Conversational Analytics API provide granular control over who can create, manage, and interact with data agents. This section explains how to share data agents by assigning IAM roles and describes the IAM roles that are required for other common user tasks.

### How agent sharing works

You can grant roles at the project level to provide permissions for all agents within a project. To control access to a specific agent instead, an agent owner (a principal with the Gemini Data Analytics Data Agent Owner role) can modify that agent's IAM policy programmatically.

**Important:** Conversational Analytics API IAM roles control access to agents and their configurations, not to the underlying data sources. When a user interacts with an agent, the API queries the connected data source by using that user's credentials. Therefore, to successfully chat with an agent, a user must have the following permissions: 

  * An appropriate Conversational Analytics API IAM role to access the agent
  * Sufficient permissions in the data source (such as in BigQuery, Looker, or a database data source) to access the data that is being queried



The following diagram shows how an agent owner can manage access to a specific agent:

![An agent owner grants the Data Agent Editor and Data Agent User roles to other users.](https://docs.cloud.google.com/static/gemini/data-agents/conversational-analytics-api/images/ca-api-agent-sharing.png)

![](https://docs.cloud.google.com/static/gemini/data-agents/conversational-analytics-api/images/ca-api-agent-sharing.png)

In this scenario, a Senior Data Analyst with the Gemini Data Analytics Data Agent Creator role creates an agent. When a user creates an agent, they are automatically granted the Gemini Data Analytics Data Agent Owner role for that agent. As the agent owner, the Senior Data Analyst manages access to the agent by setting its IAM policy and grants the following roles to team members:

  * Gemini Data Analytics Data Agent Editor: The agent owner grants this role to Junior Data Analysts. This role lets the junior analysts edit the agent's configuration and chat with the agent.
  * Gemini Data Analytics Data Agent User: The agent owner grants this role to team members who don't need to be able to edit the agent's configuration. This role lets those team members chat with the agent.



### Required roles for common user tasks

To help you decide which roles to assign, consider the following common user tasks:

Administer all Gemini Data Analytics resources
    Assign the Gemini Data Analytics Admin role to administrators who need full access to all data agents and locations within a project.
View all Gemini Data Analytics resources and chat
    Assign the Gemini Data Analytics Viewer role to users who need read-only access to all agent configurations in the project and the ability to chat with them.
Create new data agents
    Assign the Gemini Data Analytics Data Agent Creator role to users who are responsible for creating new data agents within a project.
Share agents
    Assign the Gemini Data Analytics Data Agent Owner role to users who need to share agents with other principals by managing agent permissions.
Manage agent permissions
    Assign the Gemini Data Analytics Data Agent Owner role to users who need to share agents with other users by managing agent permissions, or who need the highest level of control over an agent, including the ability to delete agents. When a user creates an agent, the system automatically grants this role to that user for the specific agent.
Edit agent configurations
    Assign the Gemini Data Analytics Data Agent Editor role to users who modify an agent's configuration, such as its context or data source mappings. These users don't have permissions to share or delete the agent.
Chat with agents
    Assign the Gemini Data Analytics Data Agent User role to users or applications that primarily interact with agents by asking questions and receiving responses.
View agent configurations
    Assign the Gemini Data Analytics Data Agent Viewer role to users who need read-only access to view agent configurations.
Chat by using inline context
    Assign the Gemini Data Analytics Stateless Chat User role to users or applications that interact with the API in a stateless mode, where the user provides all context for the conversation within each request.
Query data by using natural language
    Assign the Gemini Data Analytics Query Data User role to users or applications that query database data sources by using the `QueryData` method (AlloyDB, GoogleSQL for Spanner, Cloud SQL for MySQL, and Cloud SQL for PostgreSQL). Optionally, if you use context sets ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) for database data sources, to create, upload, and manage context sets, also assign the Dataplex Catalog Editor (`roles/dataplex.catalogEditor`) or Dataplex Catalog Admin (`roles/dataplex.catalogAdmin`) role on the project (see [Context sets permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#context-set-permissions)). To chat with a data agent instead, assign a data agent role.

## Predefined roles for the Conversational Analytics API

**Note:** Granting a user access to a data agent doesn't provide the ability to view conversations that were initiated by other users. For example, listing conversations for an agent only returns conversations that were created by the current user.

The following table describes the predefined roles for the Conversational Analytics API and their typical grant levels, which can be at the project level or for a specific data agent. If the predefined roles don't provide the set of permissions that you want, you can also create your own [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

Grant the `dataAgentOwner`, `dataAgentEditor`, `dataAgentUser`, and `dataAgentViewer` roles at the agent resource level. To avoid granting overly broad permissions, restrict project-level grants of these roles to administrators only, as project-level access grants permissions for all agents within the project.

The predefined roles include permissions from the following categories:

  * `geminidataanalytics.dataAgents.*`: Controls access to data agent resources, including creating, viewing, updating, deleting, and chatting with data agents, as well as managing agent IAM policies.
  * `geminidataanalytics.operations.*`: Controls access to inspect, list, cancel, or delete long-running background operations.
  * `geminidataanalytics.locations.*`: Controls access to view and list available Google Cloud locations and invoke location-level capabilities such as stateless chat and data engineering agents.

Role | Typical grant level | Permissions  
---|---|---  
**Gemini Data Analytics Admin** (`roles/geminidataanalytics.admin`) Grants full administrative access to all Gemini Data Analytics resources within a project. Lets principals create, edit, share, and delete data agents, chat with agents, and manage background operations. | Project |  `geminidataanalytics.*`

  * `geminidataanalytics.dataAgents.chat`
  * `geminidataanalytics.dataAgents.create`
  * `geminidataanalytics.dataAgents.delete`
  * `geminidataanalytics.dataAgents.get`
  * `geminidataanalytics.dataAgents.getIamPolicy`
  * `geminidataanalytics.dataAgents.list`
  * `geminidataanalytics.dataAgents.setIamPolicy`
  * `geminidataanalytics.dataAgents.update`
  * `geminidataanalytics.locations.chat`
  * `geminidataanalytics.locations.get`
  * `geminidataanalytics.locations.list`
  * `geminidataanalytics.locations.useDataEngineeringAgent`
  * `geminidataanalytics.operations.cancel`
  * `geminidataanalytics.operations.delete`
  * `geminidataanalytics.operations.get`
  * `geminidataanalytics.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
**Gemini Data Analytics Viewer** (`roles/geminidataanalytics.viewer`) Grants permission to view agent configurations and chat with any agent in a project. Doesn't grant permission to create, edit, share, or delete agents. | Project | 

  * `geminidataanalytics.dataAgents.chat`
  * `geminidataanalytics.dataAgents.get`
  * `geminidataanalytics.dataAgents.getIamPolicy`
  * `geminidataanalytics.dataAgents.list`

`geminidataanalytics.locations.*`

  * `geminidataanalytics.locations.chat`
  * `geminidataanalytics.locations.get`
  * `geminidataanalytics.locations.list`
  * `geminidataanalytics.locations.useDataEngineeringAgent`



  * `geminidataanalytics.operations.get`
  * `geminidataanalytics.operations.list`
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`

  
**Gemini Data Analytics Data Agent Creator** (`roles/geminidataanalytics.dataAgentCreator`) Grants a principal permission to create new data agent resources in a specific project. When a principal creates an agent, the system automatically grants that principal the `dataAgentOwner` role for the specific agent. | Project | 

  * `geminidataanalytics.dataAgents.create`
  * `geminidataanalytics.locations.chat`
  * `geminidataanalytics.operations.get`

  
**Gemini Data Analytics Data Agent Owner** (`roles/geminidataanalytics.dataAgentOwner`) Grants a principal full control over the lifecycle of any agent within the project, including sharing and deleting agents. This role is for trusted principals who can manage agent sharing. This role inherits all permissions from the `dataAgentEditor`, `dataAgentUser`, and `dataAgentViewer` roles. A principal with this role can share and delete agents. | **Agent** or Project | 

  * `geminidataanalytics.dataAgents.chat`
  * `geminidataanalytics.dataAgents.delete`
  * `geminidataanalytics.dataAgents.get`
  * `geminidataanalytics.dataAgents.getIamPolicy`
  * `geminidataanalytics.dataAgents.list`
  * `geminidataanalytics.dataAgents.setIamPolicy`
  * `geminidataanalytics.dataAgents.update`
  * `geminidataanalytics.locations.get`
  * `geminidataanalytics.locations.list`

`geminidataanalytics.operations.*`

  * `geminidataanalytics.operations.cancel`
  * `geminidataanalytics.operations.delete`
  * `geminidataanalytics.operations.get`
  * `geminidataanalytics.operations.list`

  
**Gemini Data Analytics Data Agent Editor** (`roles/geminidataanalytics.dataAgentEditor`) Grants permission to modify and manage existing agent configurations. This role inherits all permissions from the `dataAgentUser` and `dataAgentViewer` roles. | **Agent** or Project | 

  * `geminidataanalytics.dataAgents.chat`
  * `geminidataanalytics.dataAgents.get`
  * `geminidataanalytics.dataAgents.list`
  * `geminidataanalytics.dataAgents.update`
  * `geminidataanalytics.operations.get`

  
**Gemini Data Analytics Data Agent User** (`roles/geminidataanalytics.dataAgentUser`) Grants permission to chat with the specific agents to which the principal has been granted access. This role inherits all permissions from the `dataAgentViewer` role. | **Agent** or Project | 

  * `geminidataanalytics.dataAgents.chat`
  * `geminidataanalytics.dataAgents.get`
  * `geminidataanalytics.dataAgents.list`

  
**Gemini Data Analytics Data Agent Viewer** (`roles/geminidataanalytics.dataAgentViewer`) Grants a principal read-only permission to list and view agent configurations. This role doesn't allow chatting with agents. | **Agent** or Project | 

  * `geminidataanalytics.dataAgents.get`
  * `geminidataanalytics.dataAgents.list`

  
**Gemini Data Analytics Stateless Chat User** (`roles/geminidataanalytics.dataAgentStatelessUser`) Grants a principal permission to call the Chat API in stateless mode. With stateless chat, context is provided directly in the request instead of being saved explicitly in the agent configuration during creation. | Project | 

  * `geminidataanalytics.locations.chat`
  * `geminidataanalytics.locations.useDataEngineeringAgent`

  
**Gemini Data Analytics Query Data User** (`roles/geminidataanalytics.queryDataUser`) Grants a principal permission to use natural language to query database data sources by using the `QueryData` method (AlloyDB, GoogleSQL for Spanner, Cloud SQL for MySQL, and Cloud SQL for PostgreSQL). This role doesn't grant access to data agents. | Project |  `geminidataanalytics.locations.queryData`  
  
## Grant IAM roles

You can grant Conversational Analytics API IAM roles at the project level or for a specific agent. Granting a role at the project level gives a principal the same permissions for all agents in that project, while setting the policy on a specific agent provides more granular control.

The predefined IAM roles for the Conversational Analytics API are part of the `geminidataanalytics` service. The technical names for these roles follow the pattern `roles/geminidataanalytics.ROLE_NAME`. In the Google Cloud console, you can find these roles by filtering for the **Gemini Data Analytics** service.

### Grant roles for all agents in a project

Use the Google Cloud console or the Google Cloud CLI to grant roles for an entire project.

### console

To grant a role to a principal in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project)

  2. Click **Grant access**.

  3. In the **New principals** field, enter the email address of the user, group, or service account.

  4. From the **Select a role** menu, filter for **Gemini Data Analytics** to see the available IAM roles for the Conversational Analytics API.

  5. Select the appropriate role, such as **Gemini Data Analytics Data Agent User**.

  6. Click **Save**.




###  gcloud 

To grant roles by using the gcloud CLI, complete the following steps:

  1. Sign in to Google Cloud and set your project:


    
    
    gcloud auth login
    gcloud config set project PROJECT_ID
    

  1. Optionally, to list the Conversational Analytics API IAM roles that you can grant for your project, use the `gcloud iam list-grantable-roles` command as follows:


    
    
    gcloud iam list-grantable-roles //cloudresourcemanager.googleapis.com/projects/PROJECT_ID --filter "geminidataanalytics"
    

  1. Grant a role to a principal by using the `gcloud projects add-iam-policy-binding` command.


  * To grant a role to a user, use the following command:


    
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member='user:USER_EMAIL' --role='roles/GDA_GRANTABLE_ROLE'
    

  * To assign a role to a service account, use the following command:


    
    
    gcloud projects add-iam-policy-binding PROJECT_ID --member='serviceAccount:SERVICE_ACCOUNT_EMAIL' --role='roles/GDA_GRANTABLE_ROLE'
    

In the previous instructions, replace the sample values as follows:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `USER_EMAIL`: The email address of the user, such as `test-user@example.com`.
  * `SERVICE_ACCOUNT_EMAIL`: The email address of the service account, such as `test-sa@example.com`.
  * `GDA_GRANTABLE_ROLE`: The specific Conversational Analytics API IAM role that you want to grant, such as `geminidataanalytics.dataAgentCreator`.



### Grant roles for a specific agent

To manage access for a specific data agent, you must programmatically modify that agent's [allow policy](https://docs.cloud.google.com/iam/docs/allow-policies). This process follows a standard [read-modify-write pattern](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#multiple-roles-programmatic) where you read the current policy, modify it, and then write it back.

**Important:** The `setIamPolicy` method overrides any existing policy on the agent. To preserve existing permissions when granting new roles, you must call `getIAMPolicy` first to fetch the existing policy, modify that policy, and then pass the updated policy object in the call to `setIamPolicy`.

The following samples show the request bodies for getting and setting IAM policies for a data agent.

### HTTP

To get the existing policy for an agent, send a `POST` request to the `:getIamPolicy` endpoint with the following request body:
    
    
    {
      "resource": "projects/PROJECT_ID/locations/LOCATION/dataAgents/AGENT_ID"
    }
    

To set the policy for an agent, send a `POST` request to the `:setIamPolicy` endpoint with the following request body:
    
    
    {
      "policy": {
        "bindings": [
          {
            "role": "ROLE",
            "members": [
              "user:EMAIL"
            ]
          }
        ]
      }
    }
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The location where the data agent is stored (for example, `global`, `us`, or `us-east4`). For more information, see [Data residency](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency).
  * `AGENT_ID`: The ID of the data agent for which to get or set the policy.
  * `ROLE`: The role to grant, such as `roles/geminidataanalytics.dataAgentUser`.
  * `EMAIL`: The email address of the user, such as `test-user@example.com`.



For complete examples, see [Get the IAM policy for a data agent](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http#get-iam-policy-for-data-agent) and [Set the IAM policy for a data agent](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http#set-iam-policy-for-data-agent).

### Python SDK

To get the existing policy for an agent, use the `get_iam_policy` method, such as in the following sample request:
    
    
    resource = "projects/PROJECT_ID/locations/LOCATION/dataAgents/AGENT_ID"
    request = iam_policy_pb2.GetIamPolicyRequest(
                resource=resource,
            )
    

To set the policy for an agent, use the `set_iam_policy` method, such as in the following sample request:
    
    
    resource = "projects/PROJECT_ID/locations/LOCATION/dataAgents/AGENT_ID"
    policy = policy_pb2.Policy(
        bindings=[
            policy_pb2.Binding(
                role="ROLE",
                members=["user:EMAIL"]
            )
        ]
    )
    request = iam_policy_pb2.SetIamPolicyRequest(
        resource=resource,
        policy=policy
    )
    

Replace the following:

  * `PROJECT_ID`: Your Google Cloud project ID.
  * `LOCATION`: The location where the data agent is stored (for example, `global`, `us`, or `us-east4`). For more information, see [Data residency](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency).
  * `AGENT_ID`: The ID of the data agent for which to get or set the policy.
  * `ROLE`: The role to grant, such as `roles/geminidataanalytics.dataAgentUser`.
  * `EMAIL`: The email address of the user, such as `test-user@example.com`.



For complete examples, see [Get the IAM policy for a data agent](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk#get-iam-policy-for-data-agent) and [Set the IAM policy for a data agent](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk#set-iam-policy-for-data-agent).

## What's next

  * Learn more about the [Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview).
  * Learn how to [Authenticate to your data source and the API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
