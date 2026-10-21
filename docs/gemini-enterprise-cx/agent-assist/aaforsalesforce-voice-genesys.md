---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-voice-genesys/
title: Agent Assist for Salesforce voice with Genesys CX Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:44:27.439640+00:00
---

# Agent Assist for Salesforce voice with Genesys CX Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-voice-genesys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Agent Assist for Salesforce voice with Genesys CX Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This Salesforce voice integration uses Service Cloud Voice to bring Genesys Cloud into your Salesforce instance. Agent Assist uses the media stream from the [Genesys Cloud audiohook](https://help.genesys.cloud/articles/about-audiohook-monitor/) integration to provide suggestions to your agents in the [Salesforce Lightning Service console](https://help.salesforce.com/s/articleView?id=service.console_lex_service_intro.htm&type=5) with Agent Assist for Salesforce. The following diagram illustrates this integration architecture:

![Architecture for the Agent Assist and Genesys Cloud integration with Salesforce.](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/genesys_diagram.webp)

**Figure 1.** Integration architecture for Salesforce voice with Agent Assist and Genesys Cloud.

## Before you begin

Follow these steps to set up the resources needed for your Salesforce Genesys CX Cloud integration.

  1. Set up your [access to resources](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-byb).
  2. Set up your [Agent Assist for Salesforce app](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-setup).
  3. Configure and deploy the following:

     * Agent Assist [UI connector](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules)
     * [Pubsub notifications](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pub-sub)
     * [Genesys Cloud audiohook integration](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-voice)



## Install Genesys CX Cloud for Salesforce

In the [Salesforce AppExchange](https://appexchange.salesforce.com/), [install CX Cloud from Genesys for Salesforce](https://help.genesys.cloud/articles/install-the-cx-cloud-core-services-for-salesforce-service-cloud-package/).

## Configure Genesys

Follow these steps in Genesys to configure CX Cloud for Salesforce.

### Step 1: Create a role and add permissions

Follow these steps to create a role and add permissions to access all the necessary resources.

  1. Navigate to the directory and click **User Management** > **Roles and Permissions** > **Add role**.
  2. Click **Role details** and enter the name **Salesforce CX Cloud**.
  3. Click **Permissions** , and enter a search for **Authorization > License > View**.
  4. Select the matching result and click **Save**.
  5. Repeat steps 3-4 for all the [required permissions](https://help.genesys.cloud/articles/requirements-for-cx-cloud-from-genesys-and-salesforce-integration/) and [open authorization (OAuth) client permissions](https://help.genesys.cloud/articles/oauth-client-permissions-for-cx-cloud-from-genesys-and-salesforce/).



### Step 2: Create an audio connector

The Genesys Cloud audio connector captures, processes, and analyzes real time audio streams from your contact center conversations. It seamlessly integrates with the Genesys Cloud audiohook API using a persistent WebSocket connection to the audiohook service. This connection enables real time audio streaming with gRPC to the Agent Assist integration backend. The connector provides a framework for handling incoming audio chunks, which facilitates custom audio processing, transcription, and other AI-driven Agent Assist features.

Follow these steps to create your audio connector, also called an audiohook monitor.

  1. Navigate to the directory and click **IT & Integrations** > **Integrations** > **Add Integration**.
  2. Enter a search for **Audiohook Monitor**.
  3. Click **Audiohook Monitor** > **Install** > **Details** , and enter the name **Agent Assist Audiohook Monitor**.
  4. Click **Configuration**.
  5. Navigate to **Connection URI** and enter the websocket address for your Genesys audiohook followed by the `/connect` path.
  6. Click **Channel** > **Both** > **Save**.



### Step 3: Create a role for the audio connector

Follow these steps to assign a role and permissions to your audio connector.

  1. Follow the instructions in step 1 to create a role and enter the name **Agent Assist Audiohook Monitor**.
  2. Follow the instructions in step 1 to add the following permissions:

     * `Analytics > Conversation Detail > All Permissions`
     * `Analytics > Conversation Detail > View`
     * `Notifications > All Permissions`
     * `Notifications > Bulk Channel > All Permissions`
     * `Notifications > Bulk Channel > Add`
  3. Click **Save**.




### Step 4: Create an OAuth app

Follow these steps to create an OAuth application to authorize conversation data.

  1. Navigate to the directory and click **IT & Integrations** > **OAuth** > **Add Client**.
  2. Enter a name for your new application.
  3. Navigate to **Grant Type** and select **Client Credentials**.
  4. Click **Next**.
  5. Enable the **Salesforce CX Cloud** and **Agent Assist Audiohook Monitor** roles.
  6. Click **Next**.
  7. Enter a number for **Token duration in seconds**.
  8. Click **Save**.



### Step 5: Configure IVR

When a voice call begins, Genesys creates a `ConversationId` and uses it to create an Agent Assist conversation. The Salesforce API, called Service Cloud Voice (SCV), receives the `ConversationId` that Genesys created. SCV uses the Genesys `ConversationId` to ensure that Agent Assist for Salesforce retrieves the corresponding conversation from Gemini Enterprise for Customer Experience Agent Assist.

To ensure that Genesys, Salesforce, and Agent Assist all access the same `ConversationId`, you must update your interactive voice response (IVR) flow to send the `Call.ConversationId` to Salesforce. To do that, you must first map Genesys data to Salesforce fields. Complete this mapping before any transfers to avoid sending the transfer `ConversationId` to Salesforce, which doesn't align with the `ConversationId` sent to Agent Assist.

Follow these steps to map Genesys data to Salesforce fields: 

  1. Navigate to [Architect](https://help.genesys.cloud/articles/architect-overview/).
  2. Click **Add**.
  3. Enter a name and click **Create Flow** > **\+ Task** > **Search toolbox** and enter **Set participant data**.
  4. Move **Set Participant Data** to **Drag action here**.
  5. Enter the following details. 
     * **Attribute Name** : `agent_assist__ConversationId__c`
     * **Value to assign** : `Call.ConversationId`
  6. For the value to assign, click **docs keyboard_arrow_down Down** > **functions Expression** and remove quotation marks.
  7. Click **Search toolbox** and enter **Set external tag**.
  8. Move **Set External Tag** to **Drag action here**.
  9. For the external tag value, enter `vendorCallKey`.
  10. Complete your IVR as you normally would.
  11. Ensure that **Set Participant Data** and **Set external tag** occur before any transfers.



## Configure Genesys in Salesforce

Follow these steps in Salesforce to configure your Genesys CX Cloud integration.

### Step 1: Remote site settings

Follow these steps to add new remote site settings:

  1. Navigate to **Setup** > **Quick Find** , and enter a search for **remote site settings**.
  2. Click **Remote Site Settings** > **New Remote Site** , and enter the following details: 
     * **Remote Site Name** : `genesys_app`
     * **Remote Site URL** : https://apps.region.pure.cloud
  3. Click **Save & New**, and enter the following details: 
     * **Remote Site Name** : `genesys_login`
     * **Remote Site URL** : https://login.region.pure.cloud 
  4. Click **Save**.

**Note:** [Find your region](https://help.genesys.cloud/faqs/how-can-i-tell-what-region-i-am-in/) in your Genesys URL when you're signed in.

### Step 2: Create a trusted URL

Follow these steps to create a trusted URL so that Genesys CX Cloud can authenticate your Salesforce instance.

  1. Follow the instructions to [create a trusted URL](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-setup#create-trusted-urls).
  2. Enter the following details:

     * **Name** : `genesys_apps`
     * **URL** : https://apps.region.pure.cloud
  3. Navigate to **CSP Directives** and select all of the SRCs.




### Step 3: Add OAuth settings

Follow these steps to add your OAuth settings to CX Cloud:

  1. Navigate to **App Launcher** and enter a search for **CX Cloud**.
  2. Click **CX Cloud Genesys Settings**.
  3. In the **OAuth Settings** section, click **New**.
  4. Enter the name, client ID, and client secret from the OAuth application you previously created in Genesys.
  5. Enter the region from your Genesys URL.
  6. Click **Save**.



### Step 4: Install Voice for Salesforce Service Cloud

Follow these steps to install Voice for Salesforce Service Cloud and enable Service Cloud Voice:

  1. On the CX Cloud Genesys Settings page, navigate to **Voice for Salesforce Service Cloud** , and click **Install**. Installation might take a few minutes.
  2. Enable **Enable Service Cloud Voice**.



### Step 5: Configure Voice for Salesforce Service Cloud

Follow these steps to start your Voice for Salesforce Service Cloud configuration:

  1. On the Package Listings page, navigate to **Voice for Salesforce Service Cloud**.
  2. Click **Configure** > **Get Started**.



#### Add utility items

Follow these steps to add omni-channel and CX utility items:

  1. From the Setup page, navigate to **Quick Find** and enter **App Manager**.
  2. Click **App Manager**.
  3. Navigate to **Service Console** in the list.
  4. Click **Edit** > **Utility Items (Desktop only)** > **Add Utility Item**.
  5. Enter a search for **omni-channel** and click the **Omni-Channel** result > **Add Utility Item**.
  6. Enter a search for **CX utility** and click the **Genesys Cloud CX Utility** result.
  7. Click **Save**.



#### Create presence statuses

Follow these steps to create presence statuses:

  1. Click **Setup** > **Open Presence Manager** > **New**.
  2. Enter the following details:

     * **Status Name** : Available for Voice
     * **Developer Name** : `Available_for_Voice`
     * **Status Options** : Online
  3. Navigate to the **Service Channels** section and click **Phone** > **Add arrow_right Right** > **Save** > **Presence Statuses** > **New**.

  4. Repeat steps 2-3, but use the following details instead:

     * **Status Name** : Available Off Queue
     * **Developer Name** : `Available_Off_Queue`
     * **Status Options** : Online



#### Enable presence statuses

Follow these steps to enable your new presence statuses:

  1. Click **Quick Find** and enter a search for **profiles** > **Profiles** > the name of your user's profile > **Enabled Service Presence Status Access**.
  2. Navigate to **Enabled Service Presence Status Access** and click **Edit**.
  3. Confirm the **Enabled Service Presence Statuses** column contains the following statuses or add them:

     * Available for Voice
     * Available Off Queue
     * Busy
  4. Click **Save**.




#### Assign contact center permissions to user

Follow these steps to assign permissions to a user:

  1. Navigate to **Quick Find** and enter **permissions manager**.
  2. Click **Permissions Manager**.
  3. Navigate to each of the following permissions and click its name:

     * Contact Center Admin (Partner Telephony)
     * Contact Center Agent (Partner Telephony)
  4. Click **Manage Assignments** > **Add Assignment**.

  5. Select a user and click **Next** > **Add Assignment**.




#### Create and configure a voice call record page

Follow the Genesys instructions to create a [Voice Call record page](https://help.genesys.cloud/articles/create-and-configure-the-voice-call-record-page-for-agents/).

### Step 6: Create a contact center

From the Voice for Salesforce Service Cloud page, click **Create Contact Center** and you should see new instructions.

#### Generate a contact center XML

Follow these steps to generate public key and contact center configuration files:

  1. From the Create Contact Center page, click **Generate a Contact Center XML**.
  2. Enter a display name, select your region, and enter your long distance phone number prefix.
  3. Click **Key Generation Documentation** and follow the instructions to generate a public key > **Upload Files** to add your CRT file > **Generate contact center configuration** to download an XML file. 



#### Create a contact center in Salesforce

Follow these steps to add your Genesys contact center to your Salesforce instance:

  1. From the Create Contact Center page, click **Create a Contact Center in Salesforce** > **New**.
  2. Choose the Genesys contact center that matches your region.
  3. Select **Create a contact center** and click **Upload XML File**.
  4. Upload the contact center configuration XML that you generated in the previous section.



#### Select a contact center

Choose the contact center you created in the previous section, which automatically adds data for the following steps.

#### Set up integration settings in Genesys Cloud

Follow these steps to integrate your contact center with Genesys Cloud:

  1. On the Create Contact Center page, navigate to **Set Up Integration Settings** in Genesys Cloud and choose your OAuth application.
  2. Enter a name for your integration.
  3. Navigate to **Genesys Cloud Group Filtering**.
  4. Enter a search to choose any Genesys groups whose members can use the integration, including your contact center agents.
  5. Click **Upload File** to upload the CRT file with your public key.
  6. Click **Create Integration**. After a few seconds, the **Integration Status** should become `Active`.



#### Configure contact center settings

Follow these steps to set up the mappings from Omni-channel to Genesys Cloud statuses:

  1. On the Create Contact Center page, navigate to **Status Mapping**.
  2. Choose the statuses in each column that correspond to the table in the [Genesys Cloud instructions](https://help.genesys.cloud/351149/#status-mapping).
  3. Choose **Available Off Queue** for the default status.
  4. Click **Save**.



#### Genesys Cloud conversation field mapping

Follow these steps to map the Genesys `Conversation.ConversationId` to the Salesforce `VoiceCall.agent_assist__ConversationId__c` field:

  1. On the Create Contact Center page, navigate to **Genesys Cloud Conversation Field Mapping**.
  2. Click **\+ Add Mapping**.
  3. Enter the following details:

     * **Conversation Attributes** :`Conversation.ConversationId`
     * **Salesforce Fields** : Conversation ID
  4. Click **Save**.




#### Add agents to contact center

Follow these steps to add agents as users in your contact center:

  1. On the Create Contact Center page, navigate to **Add agents to Contact Center** > **Add Contact Center Users** > **Contact Center Users**.
  2. Click **Add** > **+** for each of your agents > click **Done**.
  3. Refresh the page to see the agents listed.



### Step 7: Test your contact center

Follow these steps to test your new contact center and integrations:

  1. Navigate to **App Launcher** and enter a search for **service console**.
  2. Click **Service Console** and sign in to Genesys Cloud > **Omni-Channel** and change the status to `Available for Voice`.
  3. Click **New** > the check_circle for a phone number > **End Call**. You should see a voice record page.
  4. Click **Setup** > **Edit Page**.
  5. Navigate to **Template** and click **Change** > **Header and Two Equal Regions** > **Next** > **Done**.
  6. Navigate to **Components** > **Custom Managed** , and move **Agent Assist UI Module** to the window that contains **Add Component(s) Here**.
  7. Click **Save** > **Activate** > **Assign as Org Default** > **Next** > **Save**.



## Conversation ID prefix

The Genesys audiohook service adds the letter _a_ to the beginning of a `conversationId` before sending it to Agent Assist. To access the correct conversation from Agent Assist, you must align the Agent Assist for Salesforce `conversationId` with the Genesys audiohook's `conversationId`. To ensure these two `conversationIds` match, create a [skillset](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-setup#skillsets) for Genesys CX Cloud and set the value of `conversationIdPrefix` to `a`.

## Troubleshoot your contact center

If your calls aren't reaching Salesforce, Genesys Cloud might be in wrap up mode. Follow these steps to ensure your calls reach Salesforce:

  1. Navigate to your agent workspace in Genesys Cloud.
  2. If you're in wrap up mode, click **Done**. You should be able to place a call.



You must add Genesys Cloud's CX Utility in step 5. The CX Utility ensures that you can view Genesys Cloud components on your record page. Follow these steps to confirm you added the CX Utility:

  1. Navigate to the **Salesforce** toolbar.
  2. Click **Genesys Cloud CX Utility**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
