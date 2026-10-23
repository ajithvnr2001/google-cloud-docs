---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/salesforce-chat/
title: Salesforce chat integration \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:56.740498+00:00
---

# Salesforce chat integration  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/salesforce-chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Salesforce chat integration Stay organized with collections  Save and categorize content based on your preferences. 

This chat integration uses a Salesforce Lightning Web Component (LWC) to integrate with Agent Assist UI modules for chat conversations.

Here's a high level overview of the chat integration:

![Architecture for the Agent Assist chat integration with Salesforce](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aa-salesforce-messaging-architecture.jpg)

## Before you begin

To integrate Agent Assist UI modules with Salesforce, you must first set up the [required resources](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/salesforce-required-resources).

## Step 1: Set up your Salesforce development project

To start integrating Agent Assist UI modules, follow these steps.

  1. Run the following code to clone the Agent Assist integration repository and open your project:
         
         git clone https://github.com/GoogleCloudPlatform/agent-assist-integrations
         cd salesforce/aa-lwc
         

  2. Run the following commands to download the [UI modules JavaScript](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/modules-overview) files which you deploy later as **Static Resources**. Salesforce requires static resources to load third-party JavaScript. It also enforces a 5-MB limit for static resource files, so the JavaScript files are uploaded as a zip file.
         
         npm run generate-static-resources
         npm install
         




## Step 2: Set up your Salesforce environment

You can integrate Agent Assist UI modules in a specific environment, such as production or development. Salesforce calls these environments [organizations (orgs)](https://help.salesforce.com/s/articleView?id=sf.setup_overview.htm&type=5).

### Configure your org in the Salesforce console

Within the Salesforce console, follow these steps to configure your org for Agent Assist integration.

  1. Click **Setup** > **Setup**. In the **Quick Find** box, enter **Omni-Channel Settings** , then click **Omni-Channel Settings**. 
     1. Select **Enable Omni-Channel**.
     2. Select **Automatically log agents into Omni-Channel in the new window or tab**.
     3. Click **Save**.
  2. Click **Setup** > **Setup**. In the **Quick Find** box, enter **Communities** , then click **Digital Experiences** > **Settings**. 
     1. Select **Enable Experience Workspaces**.
     2. Click **Save**.



### Configure your org with the Salesforce CLI

Follow these steps to use the Salesforce CLI to configure your org for Agent Assist integration.

  1. Run the following code and authenticate the CLI using the Salesforce login details you normally use.
         
         npm run login
         

  2. Run the following code to deploy the LWC to the org.
         
         npm run deploy
         




## Step 3: Create an external client app

The Salesforce LWC uses the client credentials OAuth 2.0 flow to authenticate you. An external client app enables the client credentials flow. Use the app's consumer key and consumer secret to configure the Salesforce LWC to authenticate users with Salesforce.

  1. Click **Setup** > **Setup**. In the **Quick Find** box, enter **External Client App Manager**. 
     1. Click **External Client App Manager** > **New External Client App** > **Create** , then enter the following information. 
        * **External Client App Name** : `lwc auth`
        * **API Name** : `lwc_auth`
        * **Contact Email** : `your_email@example.com`
        * **API (Enable OAuth Settings)** > **Enable OAuth** : Selected
        * **API (Enable OAuth Settings)** > **Callback URL** : `https://login.salesforce.com/services/oauth2/callback`
        * **API (Enable OAuth Settings) > Selected OAuth Scopes**: Access the identity URL service
        * **API (Enable OAuth Settings) > Enable Client Credentials Flow**: Selected
     2. Click **Create**.
  2. Click **Setup** > **Setup**. In the **Quick Find** box, enter **External Client App Manager**. 
     1. Click your external client app's name > **Edit**.
     2. Navigate to **OAuth Policies** > **OAuth Flows and External Client App Enhancements**.
     3. Ensure **Enable Client Credentials Flow** is selected.
     4. For **Run As** , enter your login username.
     5. Click **Save**.
  3. Click **Setup** > **Setup**. In the **Quick Find** box, enter **External Client App Manager**. 
     1. Click your external client app's name > **Edit**.
     2. Navigate to **OAuth Settings** > **App Settings** > **Consumer Key and Secret**.
     3. Enter the verification code sent to your email.
     4. Copy the consumer key and consumer secret somewhere secure. You will need these for a later step.



### Establish CORS and content security policies

  1. Click **Setup** > **Setup**.
  2. In the **Quick Find** box, enter **CORS** , then click **Edit**. 
     1. Select **Enable CORS for OAuth endpoints**.
     2. Click **Save**.
  3. Click **Setup** > **Setup**.
  4. In the **Quick Find** box, enter **Trusted URLs** , then click **New Trusted URL**.
  5. Enter the following information: 
     * **API Name** : `ui_connector`
     * **URL** : Enter the URL of the UI connector Cloud Run service endpoint you deployed with your Agent Assist integration backend. You can find this URL in the [Cloud Run console](https://console.cloud.google.com/run). For example: `https://UI_CONNECTOR_SUBDOMAIN.GCP_REGION.run.app`.
     * **CSP Directives** : Select all checkboxes.
     * Click **Save & New**.
  6. Enter the following information: 
     * **API Name** : `ui_connector_wss`
     * **URL** : Enter the Secure WebSockets URL for your UI Connector service endpoint: `wss://UI_CONNECTOR_SUBDOMAIN.GCP_REGION.run.app`.
     * **CSP Directives** : Select all checkboxes.
     * Click **Save & New**.
  7. Enter the following information: 
     * **API Name** : `salesforce_domain`
     * **URL** : Enter the URL of your Salesforce Domain with the following format: `https://YOUR_SUBDOMAIN.my.salesforce.com`.
     * **CSP Directives** : Select all checkboxes.
     * Click **Save**.



## Step 4: Configure the chat client

To use Agent Assist UI modules with Salesforce, you need a chat client on your agent desktop.

### Configure Enhanced Chat

Follow these steps to configure your messenger.

  1. Click **Setup** > **Setup**. Enter a **Quick Find** search for **Queues** , then click **New**. 
     1. Enter the following information: 
        * **Label** : `Messaging Queue`
        * **Queue Name** : `Messaging_Queue`
        * **Routing Configuration** : `Messaging_Routing_Configuration`
     2. Click **Supported Objects** , then add **Messaging User** and **Messaging Session**.
     3. Click **Queue Members** , then add **User: Your Login User**.
     4. Click **Save**.
  2. Click **Setup** > **Setup**. In the **Quick Find** box, enter **Permission Sets**. 
     1. Click **Messaging Agents Permission Set**.
     2. Click **Service Presence Statuses Access** > **Edit**.
     3. Select statuses **Busy** and **Online - Messaging**.
     4. Click **Add** > **Save**.
  3. Click **Setup** > **Setup**. In the **Quick Find** box, enter **Users** , then click **Users**. 
     1. Click your username and verify that **Service Cloud User** is enabled.
     2. Find **Permission Set License Assignments** on the page.
     3. Click **Edit Assignments** , then select `Enhanced Chat User`.
     4. Click **Save**.
     5. Find **Permission Set Assignments** on the page.
     6. Click **Edit Assignments** , then select **Messaging Agent Permission Set**.
     7. Click **Add** > **Save**.
  4. Click **Setup** > **Setup**. In the **Quick Find** box, enter **Messaging Settings** , then click **New Channel**. 
     1. Select **Enhanced Chat**.
     2. Enter the **Name** : `Messaging Channel`.
     3. Click **Save**.
     4. Set **Routing Type** to **Omni-Queue** and **Queue** to **Messaging Queue**.
     5. Click **Save** and navigate to **Messaging Settings**.
     6. Click your messaging channel's name, then click **Activate**.
     7. After reading, accept the **Terms and Conditions**.
  5. Click **Setup** > **Setup**. In the **Quick Find** box, enter **Embedded Service Deployments** , then click **New Deployment**. 
     1. Click **Enhanced Chat** > **Next** > **Web** > **Next**.
     2. Fill in the following details: 
        * **Name** : `Messaging Embedded Service Deployment`
        * **Developer Name** : **Messaging_Embedded_Service_Deployment**
        * **Domain** : **example.com**
        * **Channel** : **Messaging Channel**
     3. Click **Save**. Wait for deployment to complete.
     4. In **Embedded Service Deployment** settings, click **Publish**.
     5. Click **Refresh** , then **Test Messaging**.



### Test Enhanced Chat

Follow these steps to test your messenger.

  1. Click **Test Messaging**.
  2. After the new tab loads, click the speech bubble to start a new test conversation.
  3. Send a message, such as **Test**.
  4. Navigate to the Salesforce browser tab.
  5. Click the **App Launcher** menu, then select **Service Console**.
  6. Click **Omni-Channel**.
  7. Set your status to **Online - Messaging**.
  8. Accept the incoming message. This opens a new tab in the **Service Console** for the conversation. You can't see the chat transcript.
  9. Click **Settings** and select **Edit Page**.
  10. From the **Components** menu, drag the **Enhanced Conversation** component into the **Conversation** section.
  11. Click **Save** > **Activate** > **Assign as Org Default** > **Desktop** > **Back** arrow_back.
  12. Refresh the page.
  13. Click **Omni-Channel**.
  14. Set your status to **Online - Messaging**.
  15. Reply to the **Test** message to validate messaging is working.



If you get stuck and need more information, see the comprehensive [Salesforce Enhanced Chat Set Up Guide](https://help.salesforce.com/s/articleView?id=sf.miaw_setup_stages.htm&language=en_US&type=5).

## Step 5: Install the Salesforce Lightning Web Component

Follow these steps to add the Salesforce LWC into a messaging session page using the [Lightning Experience Editor](https://help.salesforce.com/s/articleView?id=sf.lightning_app_builder_customize_lex_pages.htm&type=5). Continue with the test conversation from Step 4.

  1. Click **Settings** and select **Edit Page**.
  2. From the **Components** list, drag `agentAssistContainerModule` onto the page.

**Note:** The `npm deploy` command provided this component.
  3. Click the component you placed in the previous step.

  4. Fill in the form fields as follows to add configuration details.

     * **endpoint** : The URL of your [Agent Integration Backend](https://github.com/GoogleCloudPlatform/agent-assist-integrations/tree/HEAD/aa-integration-backend) UI connector, such as a URL from the [Cloud Run console](https://cloud.google.com/run), like: `https://UI_CONNECTOR_ENDPOINT.GCP_REGION.run.app`
     * **channel** : Indicate that the channel is `chat`.
     * **platform** : Indicate that the platform is `messaging`.
     * **conversationProfile** : Your [Agent Assist conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) resource name (example: `projects/GCP_PROJECT_ID/locations/GCP_REGION/conversationProfiles/CONVERSATION_PROFILE_ID`)
     * **consumerKey** : The external client app consumer key from Step 3.
     * **consumerSecret** : The external client app consumer secret from Step 3.
     * **containerHeight** : The height of the Agent Assist container.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
