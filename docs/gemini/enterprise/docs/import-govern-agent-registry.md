---
url: https://docs.cloud.google.com/gemini/enterprise/docs/import-govern-agent-registry/
title: Import A2A agents from Agent Registry \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:38:51.686269+00:00
---

# Import A2A agents from Agent Registry  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/import-govern-agent-registry/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Import A2A agents from Agent Registry Stay organized with collections  Save and categorize content based on your preferences. 

As an administrator of Gemini Enterprise, you can add an A2A agent from Agent Registry to a Gemini Enterprise app.

You can apply access control policies to traffic through Agent Gateway. These policies let you enforce egress governance to control traffic to agents.

## About A2A agents and Agent Registry

[Agent2Agent (A2A) Protocol](https://a2a-protocol.org/) is an open communication protocol and a universal language for agents. The protocol enables agents from different builders and platforms to discover each other, collaborate, and securely delegate tasks.

[Agent Registry](https://docs.cloud.google.com/agent-registry/overview) is a centralized, queryable catalog that acts as the single source of truth for discovering, tracking, and managing A2A agents, endpoints, and MCP servers.

The A2A agents in the registry can be custom agents built by you and your colleagues and deployed on various runtimes such as Agent Runtime on Gemini Enterprise Agent Platform, Cloud Run or Google Kubernetes Engine (GKE). These agents can also be agents built in our Google products, such as Google Workspace.

You can associate the agents in Agent Registry with your Gemini Enterprise apps to make them available to the app's end users.

## About Agent Gateway

Agent Gateway is the managed regional networking component of Agent Platform that acts as the traffic controller and runtime policy enforcement point for A2A agents, MCP servers, and endpoints. It secures and governs connectivity: between clients and A2A agents; A2A agents and backend tools; or A2A agents and other agents.

Before you can associate A2A agents with your Gemini Enterprise apps, you need to have set up an Agent Gateway through which agent traffic can be routed. See Before you begin below.

## Regional constraints for the registry, gateway, and app

To ensure compliance with data residency requirements, both Agent Registry and Agent Gateway resources are project-and-region-specific.

A Agent Gateway must be configured to associate with a Agent Registry that is in a region compatible with the Gemini Enterprise app's operational region. This prevents violations of data residency conventions. For example, a Gemini Enterprise app created in the US region must use an Agent Gateway configured with a US-regional Agent Registry, not a global one.

For Gemini Enterprise apps, the regional alignment is strictly enforced through a specific binding process:

  * The Gemini Enterprise app must bind only to an Agent Gateway located within one of the allowed regions for that app.

  * The selected Agent Gateway must be associated with an Agent Registry. This Agent Registry must also be located in the same specific region as the Agent Gateway and the app.

  * This means the three components (app, gateway, and registry) must be regionally aligned. The table below provides the specific region mappings:


Gemini Enterprise app location | Agent Gateway location | Agent Registry location  
---|---|---  
`global` | `us-central1` | `us-central1`, `us`, or `global`  
`us` | `us-central1` | `us-central1` or `us`  
`eu` | `europe-west1` | `europe-west1` or `eu`  
  
## Limitations

The following limitations apply when you import agents from Agent Registry:

  * You can only discover and import agents from Agent Registry if the registry is associated with the Agent Gateway set up for your Gemini Enterprise app.

  * You can apply governance policies only to agents residing within the single registry associated with the Agent Gateway.

  * Direct communication between Gemini Enterprise agents, or between a Gemini Enterprise agent and a Gemini Enterprise data connector (including MCP-based connectors such as the custom MCP server) doesn't trigger Agent Gateway policy enforcement.




## Before you begin

Before you begin, make sure you've completed the following prerequisites:

  * You have the [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role.

  * You've set up a gateway to route agent traffic through Agent Gateway. For more information, see [Route Gemini Enterprise traffic through Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-ge-deploy).




## Import agents from Agent Registry to a Gemini Enterprise app

Importing an A2A agent from Agent Registry into your Gemini Enterprise app lets you make the agent available to the app's end users.

**Important:** When you configure, and allow your End Users to access, an agent imported from Agent Registry, their query string — which may be rewritten based on prior conversation context — and tool parameters may be sent to the agent (and to any tools or MCP servers the agent invokes), and those systems may be able to link this data with their identity. Data in such systems is subject to the agent provider's Terms of Service and Privacy Policy.

### Console

To import an agent from Agent Registry to a Gemini Enterprise app, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that you want to associate an A2A agent with.

  3. Click **Agents**.

  4. Click **\+ Add agent** , and click **Add** for **Custom agent via Agent Runtime**.

  5. Find the agent that you want to add, and click **Add agent**.

  6. Review the agent details, and click **Next**.

  7. Do one of the following:

     * If the agent is publicly available or if permission for a runtime already exists, click **Skip & Finish**.

     * Otherwise, review or enter the **Provider credentials** and **Additional details** , and click **Finish**. 

Field | Description  
---|---  
**Client ID** | The unique identifier of the OAuth application that you registered with your identity provider to represent Gemini Enterprise.   
**Client secret** | The confidential key associated with the OAuth application that you registered with your identity provider to represent Gemini Enterprise.   
**Authorization URL** | The URL that users use to authorize Gemini Enterprise to access the agent. For example, `https://accounts.google.com/o/oauth2/v2/auth?client_id=123...abc.apps.googleusercontent&redirect_uri=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Foauth-redirect&oauth-redirect&include_granted_scopes=true&response_type=code&access_type=offline&prompt=consent`. **Note:** Make sure that your OAuth app has this redirect URI: `https://vertexaisearch.cloud.google.com/oauth-redirect`  
**Token URL** | The endpoint used to exchange the authorization code for an access token. For example, if the agent is hosted by Google, the token URL is `https://oauth2.googleapis.com/token`.   
**Scopes** | The permissions that define what actions Gemini Enterprise can perform on behalf of a user, or what data it can access. Gemini Enterprise requests these scopes during user authorization. For example, `https://www.googleapis.com/auth/cloud-platform`.   
  
When you specify scopes, consider the following: 
       * Provide a space-separated list of scopes. For example: `read write`.
       * Ensure the scopes are sufficient to let the user sign in and use the agent.  
**PKCE verification enabled** | Select this if Proof Key for Code Exchange is required by the agent.  
  8. To make the agent available to the app's end users, do the following:

     1. Navigate to the **User permissions** tab for the agent: **Apps** > APP_NAME > **Agents** > AGENT_NAME > **User permissions**.

     2. Click person_add**Add user**.

     3. In the **Add user permissions roles to agent** dialog, assign the **Agent User** role to a user, a group, or all users.




## Set up and apply egress governance policies

Using Agent Gateway, you can assess and apply semantic and IAM control [policies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/overview) to egress agent traffic. You can create granular egress policies to manage agent-to-agent access for your A2A agents.

You define allow and deny rules restricting an agent's access to specific entries within Agent Registry.

To create and apply egress governance rules to agents, do one of the following:

  * [Create IAM agent policies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/assign-identity-iam)

  * [Configure semantic governance policies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/configure-semantic-governance)




## What's next

  * [Test the agent](https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview#manage_agents)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
