---
url: https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-marketplace-agents/
title: Add and manage A2A agents from Google Cloud Marketplace \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:17:00.106531+00:00
---

# Add and manage A2A agents from Google Cloud Marketplace  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-marketplace-agents/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Add and manage A2A agents from Google Cloud Marketplace Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Admins can add agents from Google Cloud Marketplace that use the Agent-to-Agent (A2A) protocol. After an agent is procured (purchased) and added to Gemini Enterprise, users can access the agent through the Gemini Enterprise web app.

**Note:** To secure agents from Cloud Marketplace, developers must configure Model Armor using the REST API within their agent's application code. The Model Armor settings in the Google Cloud console for Gemini Enterprise don't automatically protect agents registered through Cloud Marketplace.

## Before you begin

Make sure you have the following:

  * The [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role.

  * The [Consumer Procurement Entitlement Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/consumerprocurement#consumerprocurement.entitlementViewer).

  * Enabled Discovery Engine API. To enable the Discovery Engine API for your Google Cloud project, in the Google Cloud console, go to the **Discovery Engine API** page.

[Go to Discovery Engine API](https://console.cloud.google.com/apis/api/discoveryengine.googleapis.com/metrics)

  * An existing Gemini Enterprise app. To create an app, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

  * An A2A agent registered on Cloud Marketplace. To learn how to offer AI agents in Cloud Marketplace, see [Offer AI agents through Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/ai-agents).

**Tip:** A2A agents on Cloud Marketplace must be maintained for them to function within Gemini Enterprise.



## Add an agent from the Cloud Marketplace to Gemini Enterprise

To add an agent from Cloud Marketplace to your Gemini Enterprise app, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app to which you want to add the agent.

  3. Click **Agents > add Add agent**.

  4. In the **Choose an agent type** section, click **Add** for **Agents via Marketplace**.

  5. Search for the agent you want to add, and click it. You can search by the agent's name or use semantic search to search by describing the agent's capabilities or purpose (for example, "generate reports" or "translate text").

  6. Click **Next**.

  7. Review the agent details, then click **Next**.

  8. Enter the required authentication details, then click **Finish**.




## Configure marketplace visibility

Admins can determine which agents from Cloud Marketplace are visible to end users in the Agent Gallery. Agent visibility is based on the agent's procurement, integration, and access status:

Status | Description  
---|---  
**Procured** | Agents that have been purchased for your organization.  
**Integrated** | Procured agents that an administrator has added and configured in your Gemini Enterprise app. These agents are available for users to access or request access to.  
  
To configure marketplace visibility:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app you want to configure.

  3. Click **Agents**.

  4. Click the Settings icon to open the **Agent settings & config** panel.

  5. In the **Marketplace visibility** section, select one of the following options:

     * **Only show accessible agents** : End users see only agents that they have access to. If there are no accessible agents, the Marketplace section is not displayed.
     * **Only show already integrated agents** : End users see only agents that are already integrated. This includes agents that the user already has access to and agents they can request access to.
     * **Only show procured agents** : (Default) End users see all procured Cloud Marketplace agents. This includes integrated agents plus agents that are not integrated yet.
     * **Show all** : End users see all Cloud Marketplace agents, including those that they don't have access to, regardless of whether the agents are procured or integrated.
  6. Click **Done** to save your changes.




## Set procurement contacts

You can set up contacts to receive notifications when users request access to agents that haven't been procured. These contacts receive notifications to procure the agent from Cloud Marketplace.

To set procurement contacts:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app you want to configure.

  3. Click **Agents**.

  4. Click the Settings icon to open the **Agent settings & config** panel.

  5. Under **Procurement contacts** , click **\+ Add contact**.

  6. Enter the email address for the contact.

  7. Click **Done** to save your changes.




## Review and approve access requests

When users request access to agents from Cloud Marketplace, you need to review and either approve or deny those requests.

To review access requests:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app for the agent.

  3. Click **Agents**.

  4. If the agent is already procured and integrated, you can grant access. The agents list shows **Review share request** in the row for agent with any access requests. Select **Review share request** , view the request information, and click **Grant access** to grant access. 

  5. When agents require procurement or integration, a red dot on **Procurements & integration requests** indicates pending requests. Click **Procurements & integration requests** to see and manage the requests.

     * Review the list of requests. The list shows the following information:

       * **Display name** : The name of the agent.
       * **User requests** : The number of users requesting the agent.
       * **Status & action**: Information about procurement and integration.
     * The list shows agent access requests where the agent is not yet procured or not yet integrated.

       * If the agent is not procured, it must be procured as the next step. If the procurement contact for the agent is set, a note indicates that a procurement request was sent to the contact. If the procurement contact for the agent is not set, you are prompted to add a procurement contact.
       * Once the agent is procured, you can click **Integrate & grant access** to complete integration. Once integration is complete you can give users access.



## Delete an agent from Gemini Enterprise

To delete an agent from your Gemini Enterprise app, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that the agent is registered with.

  3. Click **Agents**.

  4. Click the more_vert icon next to the agent you want to delete.

  5. Click **Delete**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
