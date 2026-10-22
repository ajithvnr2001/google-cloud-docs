---
url: https://docs.cloud.google.com/agent-registry/setup/
title: Set up Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:19.361320+00:00
---

# Set up Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Guides ](https://docs.cloud.google.com/agent-registry/overview)



Send feedback 

#  Set up Agent Registry Stay organized with collections  Save and categorize content based on your preferences. 

To register and discover your AI agents, Model Context Protocol (MCP) servers, standalone skills, and endpoints in Agent Registry, you must enable the Agent Registry API in your Google Cloud project. Agent Registry operates at the project level, letting you discover and manage agents, servers, skills, and endpoints deployed within the specific project where the API is enabled.

This document explains how to set up Agent Registry and enable the required API.

## Before you begin

To set up Agent Registry, use an existing project or [create a new one](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

### Required roles

To get the permissions that you need to set up Agent Registry, ask your administrator to grant you the following IAM roles on your Google Cloud project: 

  * Enable the Agent Registry API: [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`) 
  * Grant roles for using the Agent Registry API: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 
  * Get full access to Agent Registry API resources: [Agent Registry API Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/agentregistry#agentregistry.admin) (`roles/agentregistry.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Set up your gcloud CLI environment

If you plan to use the Google Cloud CLI for Agent Registry, follow these steps:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Make sure that the most recent version of gcloud CLI is installed:
         
         gcloud components update
         




## Enable the Agent Registry API

###  Console 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=agentregistry.googleapis.com&redirect=https%3A//console.cloud.google.com)

###  gcloud 

Enable the Agent Registry API in your project:
    
    
    gcloud services enable agentregistry.googleapis.com \
        --project=PROJECT_ID
    

Replace `PROJECT_ID` with [your project ID](https://support.google.com/googleapi/answer/7014113).

After enabling the Agent Registry API, you can begin registering and discovering agents in this project.

**Note:** If you integrate Agent Registry with [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway) for policy enforcement, you must also enable the Identity-Aware Proxy API (`iap.googleapis.com`) in your project. The gateway uses the Identity-Aware Proxy API to authenticate and authorize egress traffic from your agents. 

## Grant permissions

To view and manage resources in Agent Registry, you must grant users the appropriate [Identity and Access Management (IAM) permissions](https://docs.cloud.google.com/agent-registry/roles-permissions).

Grant your users one or more of the following Agent Registry roles:

  * **Agent Registry API Viewer** (`roles/agentregistry.viewer`): View and search agents, MCP servers, tools, standalone skills, skill revisions, publishers, endpoints, and bindings.
  * **Agent Registry API Editor** (`roles/agentregistry.editor`): View and edit Agent Registry resources, including registering, updating, and deleting agents, MCP servers, tools, endpoints, standalone skills, and skill revisions.
  * **Agent Registry API Admin** (`roles/agentregistry.admin`): Perform all actions on Agent Registry resources, including registering and managing agents, MCP servers, tools, endpoints, standalone skills, skill revisions, bindings, and skill IAM policies.
  * **Agent Registry User** (`roles/agentregistry.user`): View all Agent Registry resources, and create, update, and delete standalone skills and skill revisions without edit access to agents, MCP servers, or endpoints.



To learn how to grant IAM roles on a project, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Note:** Because Workforce Identity Federation is in Preview, it has limited support for Agent Registry and Agent Gateway. If you encounter loading or authorization errors in Google Cloud console, access the service with a standard Google Account managed through Cloud Identity or Google Workspace. 

## Change your Agent Registry project

If you want to change the project where you use Agent Registry and remove dependencies from the old project, disable the Agent Registry API in that project. You can then enable the Agent Registry API in another project. Your data isn't migrated, and you must recreate your resources in this new project.

## Disable the Agent Registry API

If you no longer need Agent Registry, disable the Agent Registry API on the project:

###  Console 

  1. In the Google Cloud console, go to the Agent Registry API management page:

[Go to Agent Registry API](https://console.cloud.google.com/apis/api/agentregistry.googleapis.com/overview)

  2. From the project picker, select the Google Cloud project where you set up Agent Registry.

  3. Click **Disable API**.

  4. In the confirmation dialog, click **Disable**.




###  gcloud 
    
    
    gcloud services disable agentregistry.googleapis.com \
        --project=PROJECT_ID
    

Replace `PROJECT_ID` with [the ID of the project](https://support.google.com/googleapi/answer/7014113).

## What's next

  * [Register an agent](https://docs.cloud.google.com/agent-registry/quickstart-register-agent)
  * [Manage agents](https://docs.cloud.google.com/agent-registry/manage-agents)
  * [Register MCP servers](https://docs.cloud.google.com/agent-registry/register-mcp-servers)
  * [Manage MCP tools](https://docs.cloud.google.com/agent-registry/manage-mcp-tools)
  * [Register endpoints](https://docs.cloud.google.com/agent-registry/register-endpoints)
  * [Manage and discover endpoints](https://docs.cloud.google.com/agent-registry/manage-endpoints)
  * [Register skills](https://docs.cloud.google.com/agent-registry/register-skills)
  * [Manage skills](https://docs.cloud.google.com/agent-registry/manage-skills)
  * [Search for agents, tools, and skills](https://docs.cloud.google.com/agent-registry/search-agents-and-tools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
