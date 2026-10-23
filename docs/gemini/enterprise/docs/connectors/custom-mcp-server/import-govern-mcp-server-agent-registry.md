---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/import-govern-mcp-server-agent-registry/
title: Import MCP servers from Agent Registry \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:50.741045+00:00
---

# Import MCP servers from Agent Registry  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/import-govern-mcp-server-agent-registry/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Import MCP servers from Agent Registry Stay organized with collections  Save and categorize content based on your preferences. 

As an administrator of Gemini Enterprise, you can add MCP servers from Agent Registry to Gemini Enterprise apps. The MCP servers are added as connected data stores. The MCP servers can be ones that you have created and added to the registry or they can be Google MCP servers that you discovered and added to the registry.

You can apply access control policies to traffic through Agent Gateway. These policies let you enforce egress governance to control traffic to and from these MCP servers.

## About Agent Registry

[Agent Registry](https://docs.cloud.google.com/agent-registry/overview) is a centralized, queryable catalog that acts as the single source of truth for discovering, tracking, and managing A2A agents, endpoints, and MCP servers.

The MCP servers in the registry might be MCP servers created by Google or MCP servers that you have created for your end users.

You can add MCP servers from Agent Registry as data stores for your Gemini Enterprise apps. This makes the MCP servers available to the apps' end users.

## About Agent Gateway

[Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) is also part of the govern pillar of Agent Platform. Agent Gateway is the managed regional networking component of Agent Platform that acts as the traffic controller and runtime policy enforcement point for A2A agents, MCP servers, and endpoints. It secures and governs connectivity: between MCP servers and A2A agents; clients and A2A agents; A2A agents and backend tools; or A2A agents and other agents.

Before you can add an MCP server to a Gemini Enterprise app, you need to have set up an Agent Gateway through which the MCP server traffic can be routed. See Before you begin below.

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

The following limitations apply when you import MCP servers from Agent Registry and associate those MCP servers with apps:

  * You can only import MCP servers from Agent Registry if the registry is associated with the Agent Gateway set up for the same region as the Gemini Enterprise app.

  * You can apply governance policies only to MCP servers that are in the registry associated with the Agent Gateway.

  * Direct communication between Gemini Enterprise agents and Gemini Enterprise data connectors (including MCP-based connectors such as the custom MCP server) doesn't trigger Agent Gateway policy enforcement.




## Before you begin

Before you begin, make sure you've completed the following prerequisites:

  * You have the [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role.

  * You've set up a gateway to route agent traffic through Agent Gateway. For more information, see [Route Gemini Enterprise traffic through Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-ge-deploy).




## Add MCP servers from Agent Registry to Gemini Enterprise

After you have set up Agent Gateway (Before you begin above), then the MCP servers in the associated Agent Registry become available to add as data sources for your Gemini Enterprise apps.

### Console

To add an MCP server from Agent Registry to a Gemini Enterprise app, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that you want to add the MCP server to.

  3. Click **Connected data stores**.

  4. Click **\+ New data store**.

  5. On the **Select a data source** page, **MCP servers** section, click **Show all**.

Except for the [Custom MCP Server](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server), the MCP servers listed in the **MCP servers** section are those in Agent Registry.

  6. Click **Add tool** for the MCP server that you want to add.

  7. Review the imported information.

  8. If the MCP server doesn't require authentication, select **No authentication** , enter the MCP server URL, and click **Continue**.

  9. If the MCP server does require authentication, select **OAuth 2.0** and complete the authentication fields as follows:

Field | Description  
---|---  
**MCP Server URL** | This is the endpoint where your MCP server is hosted. It must be the same as the one in the **interface URLS** in the **MCP Server details**. Gemini Enterprise only supports the `StreamableHTTP` transport, and the URL often ends with `/mcp`. For example, `https://mcp.example.com/mcp`.  
**Authorization URL** | The URL for the user to authorize Gemini Enterprise to access your MCP server. For example, `https://mcp.example.com/authorize`. Make sure that the OAuth app has the following redirect URI: `https://vertexaisearch.cloud.google.com/oauth-redirect` **Note** : Enter only the base URL, without query parameters. Gemini Enterprise automatically appends standard OAuth parameters (such as `client_id`, `redirect_uri`, and `scope`) during authorization. If your authorization server requires additional parameters, specify them in the **Authorization URL Parameters** field.  
**Authorization URL Parameters** | Optional. Any additional parameters required by your authorization URL. For example, to get a refresh token from a Google MCP server, enter `&access_type=offline&prompt=consent`.   
  
If your authorization server requires an `audience` parameter, you can add it as a parameter in this setting. For example, `&audience=https://api.your-domain.com/v1/`.   
**Token URL** | The endpoint is used for token exchange. For example, `https://mcp.example.com/token`.  
**Client ID** | The unique identifier of the OAuth app that you registered in your identity provider to represent Gemini Enterprise.  
**Client Secret** | The confidential key associated with the OAuth app that you registered in your identity provider to represent Gemini Enterprise.  
**Scopes** | The permissions that define what actions Gemini Enterprise is allowed to perform on behalf of a user, or what data it's allowed to access. The scopes are used to access the MCP server. Gemini Enterprise requests these scopes during user authorization. Ensure that your OAuth app is configured to use these scopes.   
  
When you specify scopes ensure that the provided scopes are sufficient to let the user sign in and use the tools or actions enabled by the administrator; otherwise, the agent cannot access your app.   
  10. Click **Finish**.




## Set up and apply egress governance policies

Using Agent Gateway, you can assess and apply semantic and IAM control [policies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/overview) to egress MCP server traffic. You can create granular egress policies to manage agent-to-MCP-server access for your MCP servers.

You define allow and deny rules restricting an MCP server's access to specific entries within Agent Registry.

To create and apply egress governance rules to MCP servers, do one of the following:

  * [Create IAM agent policies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/configure-iam-policies)

  * [Configure semantic governance policies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/configure-semantic-governance)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
