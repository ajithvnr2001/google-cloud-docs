---
url: https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview/
title: Agents overview \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:49.281471+00:00
---

# Agents overview  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Agents overview Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise provides centralized oversight and management for agents used by your organization, including those from Google, third parties, and internal teams.

## Agent types

The following table details the different types of agents available in Gemini Enterprise, the Gemini Enterprise tools that are used to create the agent, and the admin configurations required to view and manage them on the web app.

Agent type | Gemini Enterprise tool | Description  
---|---|---  
**Employee-made agents from your organization** | Workflow Builder |  This interactive, no-code, low-code tool lets users in your organization create, launch, and manage single and multi-step agents on the Gemini Enterprise web app. For more information, see [Workflow Builder overview](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder).   
  
A Gemini Enterprise admin must enable this feature on the web app by turning on the **Enable Workflow Builder** toggle in the **End user features control** page. For more information, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).   
**Google-made agents** | Core Assistant |  Handles interactions when users talk to the Gemini Enterprise engine without specifying any other agent. For more information, see [Core Assistant agent](https://docs.cloud.google.com/gemini/enterprise/docs/core-assistant).   
Deep Research |  Helps users perform in-depth exploration of topics. For more information, see [Get reports with Deep Research](https://docs.cloud.google.com/gemini/enterprise/docs/research-assistant).   
**Custom agents from your organization** | ADK agents hosted on Agent Runtime on Gemini Enterprise Agent Platform |  Gemini Enterprise admins can register custom agents built by your organization and hosted on Agent Runtime, making them available to users on the Gemini Enterprise web app. For more information, see [ Register and manage ADK agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent).   
Agent2Agent (A2A) |  Gemini Enterprise admins can register custom agents built using the [Agent2Agent (A2A) Protocol](https://a2a-protocol.org), making them available to users on the Gemini Enterprise web app. For more information, see [ Register and manage A2A agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent).  
Also, A2A agents in [ Agent Registry](https://docs.cloud.google.com/agent-registry/overview) can be discovered and added to apps in Gemini Enterprise. For more information, see [Import A2A agents from Agent Registry](https://docs.cloud.google.com/gemini/enterprise/docs/import-govern-agent-registry).   
Dialogflow |  Gemini Enterprise admins can register conversational agents built with Dialogflow, making them available to users on the Gemini Enterprise web app. For more information, see [ Register and manage Dialogflow agents](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-a-dialogflow-agent).   
  
## View agents

To view the agents that are registered or available, do the following:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that has the agents.

  3. Click **Agents**. The **Agents** page is displayed.




## Agent identity

As a Gemini Enterprise administrator, you can view an agent's identity. This is typically the agent's SPIFFE ID. However, the SPIFFE ID is only visible if the publisher has made it available. If the SPIFFE ID is not published, the Agent Registry resource ID is displayed as a fallback.

The following image shows an example of an agent's details displaying a SPIFFE ID:

![The Agent details page in the Gemini Enterprise console, displaying the agent's SPIFFE ID.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/agent-details-spiffe-id.png)

## Manage agents

A Gemini Enterprise admin can manage the lifecycle of the available agents from the **Agents** page in the Gemini Enterprise console and can perform the following tasks:

Task | Description  
---|---  
**Update an agent** |  You can update the details of an agent. For more information, see:  


  * [Update an A2A agent](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent#update_an_a2a_agent)
  * [Update an ADK agent](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent#update_an_adk_agent)
  * [Update a Dialogflow agent](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-a-dialogflow-agent#update-a-dialogflow-agent)

  
  
**Test an agent** |  Test your agents before your end users find problems.   
  
On the **Agents** page, click _more_vert_ next to the agent that you want to test, and then click **Preview**. This opens the agent in the Gemini Enterprise app.   
**Invoke an agent programmatically** |  Call a specific registered agent from custom applications, orchestrators, or scripts. For instructions, see:  


  * [Call a specific agent with the StreamAssist API](https://docs.cloud.google.com/gemini/enterprise/docs/invoke-agent-streamassist)
  * [Call an agent using its registry A2A endpoint](https://docs.cloud.google.com/gemini/enterprise/docs/invoke-agent-a2a)

  
**Share an agent or transfer ownership** |  You can share available agents or transfer ownership of shared agents in your Google Cloud console. For more information, see [Share agents from Google Cloud console](https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents).   
**Configure agent sharing by end users and review their requests to share** |  For agents created using Workflow Builder, you can let end users share their agents with other users in the organization through email addresses or groups. You can also configure whether sharing requires administrator review and approval. For more information, see the settings **Enable agent sharing** , **Enable agent sharing without admin approval** , and **Enable End Users to share with Groups** in [Manage features on the web app](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features). Also see [Share an agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-chat-agent).  
**Delete an agent** |  You can delete an agent from the **Agents** page. After an agent is deleted, it is removed from the **Agents** page and the Gemini Enterprise web app.   
  
On the **Agents** page, click _more_vert_ next to the agent you want to delete, and then click **Delete**.   
  
## Agent states

This table describes each state that an agent might be in. In the Google Cloud console on the **Agents** page, you can see the state listed for each agent in the **Agent state** column of the **Agents** table.

State | Description  
---|---  
**Private** | The agent is intended for personal use and is available exclusively to its creator. After the agent's status is changed to _Enabled_ , the agent is visible to other users on the Gemini Enterprise web app.   
**Suspended** | The agent is temporarily deactivated. It remains visible in the Agent Gallery with a message explaining its deactivation. Although users can't interact with the agent, owners and admins retain full access.   
**Enabled** | The agent is active and available for use on the Gemini Enterprise web app. Authorized users can interact with the agent as intended.   
**Disabled** | The agent is inactive and hidden from the Agent Gallery. Interaction isn't available for any user until the owner or admin re-enables the agent.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
