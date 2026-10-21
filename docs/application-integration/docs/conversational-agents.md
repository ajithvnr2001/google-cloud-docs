---
url: https://docs.cloud.google.com/application-integration/docs/conversational-agents/
title: Build conversational agents with Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:35:36.238478+00:00
---

# Build conversational agents with Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/conversational-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Build conversational agents with Application Integration

**Preview — Conversational agent tool**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Application Integration now simplifies the creation of conversational experiences by directly integrating with [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs). This feature lets you to build intelligent chatbots and tools that enhance user interactions and automate tasks, directly from your integration workflows using [ API triggers](https://docs.cloud.google.com/application-integration/docs/configure-api-trigger). 

## What is a conversational agent?

A Dialogflow CX conversational agent is a virtual agent that communicates in natural language conversations with users. It analyzes user input, interprets intent, and provides appropriate responses, enabling interactive and personalized conversational experiences. These agents are designed to handle conversations across various channels, such as websites, mobile apps, and messaging platforms. 

## What is a conversational agent tool?

In Dialogflow CX, a [tool](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool) represents a specific functionality or service that the conversational agent can access. Tools are defined within playbooks and allow the agent to perform actions like retrieving data, executing APIs, or interacting with external systems. Application Integration generates these tools based on your integration's API triggers, making it easy to connect your integration logic to your conversational flows. 

## Before you begin

Ensure the following before creating a conversational agent tool using Application Integration: 

  * Assign the following IAM roles to your principal: 
    * [Service Account Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
    * [Service Usage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
    * [Dialogflow Console Agent Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow#dialogflow.consoleAgentEditor) (`roles/dialogflow.consoleAgentEditor`)

For information on granting roles to principals, see [Grant or revoke a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#single-role).




### IAM roles required for service accounts

The following IAM roles are required for the service accounts used to create a conversational agent tool: 

Service account | Description | Required roles  
---|---|---  
Service account | Service account used to create the conversational agent tool. | Application Integration Invoker (`roles/integrations.integrationInvoker`)  
Dialogflow service agent (`service-{$PROJECT_ID}@gcp-sa-dialogflow.iam.gserviceaccount.com`) | Service account used by Dialogflow CX to access the integration. | Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`)  
  
## Create a new conversational agent tool

To create a new conversational agent tool using Application Integration, perform the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project. 

  3. Select an existing integration or click **Create integration** to create a new one. 

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** pane.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, Click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
     4. Click **Create**.

This opens the integration in the _integration editor_. 

  4. Select an existing integration. This opens the integration in the _integration editor_. 
  5. Ensure that the selected integration is configured with one or more [ API triggers](https://docs.cloud.google.com/application-integration/docs/configure-api-trigger).
  6. [Publish](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations#publish-integrations) the integration version.
  7. In the designer toolbar, click  more_vert  (Actions menu) and select **Create Conversational Agent Tool**. 

Application Integration verifies that the required APIs are enabled. If not, you are prompted to enable them.

  8. In the **Create Conversational Agent Tool** pane, provide the following inputs: 
     1. **API Triggers** : All the API triggers from your integration are selected by default. You can optionally deselect any API triggers that you don't want to include in the tool.
     2. **Type** : Select **Create new Conversational Agent** and enter the following details: 
        1. **Region** : Select the region for the agent.
        2. **Agent name** : Enter a name for the agent.
        3. **Tool name** : Enter a name for the tool.
**Note:** The default language for the agent is English (United States).
     3. **Service account** : Choose a service account with the necessary roles and permissions for the agent's resource access. If missing, you will be prompted to **Grant** them. 
  9. Click **View spec** to review the generated specification for the selected triggers. You can optionally edit the specification before saving.
  10. Click **Save**. 

A message appears indicating that the tool is created successfully. Click **View** to open the agent in the Dialogflow CX console.

  11. In the Dialogflow CX console, go to **Playbooks** , click the playbook for the created agent, and add instructions to the playbook to use the tool. For more information, see [Playbook tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool).



## Create a converstational agent tool using an existing agent

To create a conversational agent tool using an existing agent, perform the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project. 

  3. Select an existing integration or click **Create integration** to create a new one. 

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** pane.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, Click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
     4. Click **Create**.

This opens the integration in the _integration editor_. 

  4. Select an existing integration. This opens the integration in the _integration editor_. 
  5. Ensure that the selected integration is configured with one or more [ API triggers](https://docs.cloud.google.com/application-integration/docs/configure-api-trigger).
  6. [Publish](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations#publish-integrations) the integration version.
  7. In the designer toolbar, click  more_vert  (Actions menu) and select **Create Conversational Agent Tool**. 

Application Integration verifies that the required APIs are enabled. If not, you are prompted to enable them.

  8. In the **Create Conversational Agent Tool** pane, provide the following inputs: 
     1. **API Triggers** : All the API triggers from your integration are selected by default. You can optionally deselect any API triggers that you don't want to include in the tool.
     2. **Type** : Select **Choose existing Conversational Agent** and do the following: 
        1. **Conversational Agent** : A list of available agents in your project appears. Select the agent you want to use.
        2. **Tool** : Select either **Create new Tool** or **Choose existing Tool**. 

If you select **Create new Tool** , enter a name for the tool. 

If you select **Choose existing Tool** , a list of available tools in the selected agent appears. Select the tool you want to use. 

  9. **Service account** : Choose a service account with the necessary roles and permissions for the agent's resource access. If missing, you will be prompted to **Grant** them.


* Click **View spec** to review the generated specification for the selected triggers. You can optionally edit the specification before saving.
* Click **Save**. 

A message appears indicating that the tool is created successfully. Click **View** to open the agent in the Dialogflow CX console.

* In the Dialogflow CX console, go to **Playbooks** , click the playbook for the created agent, and add instructions to the playbook to use the tool. For more information, see [Playbook tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool).

## Considerations

The following considerations apply when using conversational agent tools: 

  * Conversational agent tools can only be created for published integrations with API triggers.
  * Review and test your agent in the Dialogflow CX console after creation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
