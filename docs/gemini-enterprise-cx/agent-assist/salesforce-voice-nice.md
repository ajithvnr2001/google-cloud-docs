---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/salesforce-voice-nice/
title: Salesforce voice integration with NiCE CXone \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:31.964497+00:00
---

# Salesforce voice integration with NiCE CXone  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/salesforce-voice-nice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Salesforce voice integration with NiCE CXone Stay organized with collections  Save and categorize content based on your preferences. 

![Architecture for the Agent Assist and NiCE CXone integration
with Salesforce](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/salesforce_nice_voice_architecture.jpg)

This voice integration uses the [NiCE CXone Agent for Service Cloud Voice (BYOT)](https://help.nicecxone.com/content/agent/agentforscv/agentforservicecloudvoiceagent.htm) Salesforce App to allow your agents to accept NiCE CXone calls in Salesforce Service Cloud Voice.

Agent Assist uses the voice call stream from [NiCE CXone Agent Assist Hub](https://help.nicecxone.com/content/aiassistantsandbots/agentassisthub/agentassisthub.htm) to provide suggestions to your agents in the [Salesforce Lightning Service Console](https://help.salesforce.com/s/articleView?id=service.console_lex_service_intro.htm&type=5).

## Before you begin

To integrate Agent Assist UI modules with Salesforce, you must first set up the [required resources](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/salesforce-required-resources).

In addition, you need access to the following resources:

  * A [**NiCE CXone instance**](https://www.nice.com/products)

  * A [**NiCE CXone Agent Assist Hub add-on license**](https://www.nice.com/products/agent-assist-hub): The NiCE CXone Agent Assist Hub add-on allows your NiCE CXone instance to send voice call media streams to Google Cloud's Agent Assist. NiCE CXone is a licensed product. More details are available in the [NiCE CXone Agent Assist Hub documentation](https://www.nice.com/products/agent-assist-hub).




## Step 1: Configure NiCE CXone Studio and NiCE CXone Agent Assist Hub

This step describes all the configuration necessary in your NiCE CXone instance.

### Configure call flow with NiCE CXone Studio

In this step, you'll configure a programmatic call flow with [**NiCE CXone Studio**](https://help.nicecxone.com/content/studio/studio.htm) to route incoming calls to your agents and send the call media streams to Agent Assist. Configure this call flow with the following NiCE CXone Studio triggers and actions, in this order:

  1. Sign in to **NiCE CXone console**.
  2. Open the **Applications** menu (apps).
  3. Open **Omnichannel Routing** > **Studio**.
  4. In the Studio page, create a **New Script**.



Configure this call flow with the following NiCE CXone Studio triggers and actions:

  1. [**Begin**](https://help.nicecxone.com/content/Studio/actionscx/begin/begin.htm): This trigger is activated when a call comes into your [NiCE Point of Contact (POC)](https://help.incontact.com/Content/ACD/Channels/AdditionalChannelFeatures/PointsOfContact/PointsOfContact.htm) phone number.
  2. [**Reqagent**](https://help.nicecxone.com/content/Studio/actions/reqagent/reqagent.htm): This action sends the call to a specified skill. Select the skill associated with the agents who you would like to receive calls.
  3. [**Music**](https://help.nicecxone.com/content/studio/actions/music/music.htm): This action plays hold music.
  4. [**Wait**](https://help.nicecxone.com/content/studio/actions/wait/wait.htm): This action suspends the flow until another trigger is activated.



Separately, but in the same Studio flow, configure what happens when an agent picks up the incoming call.

  1. [**Onanswer**](https://help.nicecxone.com/content/studio/actions/onanswer/onanswer.htm): This trigger is activated when an agent in the skill.
  2. [**Ziptone**](https://help.nicecxone.com/content/studio/actions/ziptone/ziptone.htm): This plays a beep when an agent picks up the phone in a NiCE CXone agent desktop (such as the NiCE CXone Agent for Service Cloud Voice (BYOT) softphone).
  3. [**Agent Assist**](https://help.incontact.com/Content/Studio/Actions/AgentAssistV1/AgentAssistV1.htm): This action is responsible for creating a conversation and sending an incoming call's media streams to Dialogflow, so that the Agent Assist UI modules LWC can render the transcript and Agent Assist suggestions (such as PGKA, GKA, AI Coaching) in Salesforce. See [this integration documentation](https://help.staging.nice-incontact.com/content/studio/integrations/agentassisthub/googleccai.htm) for configuration details. Note: this step requires a [pre-configured conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile).



You can also configure Agent Assist for outbound calls. The integration requires triggering the [**Agent Assist**](https://help.incontact.com/Content/Studio/Actions/AgentAssistV1/AgentAssistV1.htm) action when an outbound call is answered by the remote party. While the exact implementation depends on your configuration, this can typically be achieved in your script by using the [**Placecall**](https://help.nicecxone.com/content/studio/actions/placecall/placecall.htm) action to initiate the call, and connecting the **Agent Assist** action to the `OnAnswer` branch of `Placecall`. See the NiCE CXone Studio help documentation for [**Placecall**](https://help.nicecxone.com/content/studio/actions/placecall/placecall.htm), [**Onanswer**](https://help.nicecxone.com/content/studio/actions/onanswer/onanswer.htm), and [**Agent Assist**](https://help.incontact.com/Content/Studio/Actions/AgentAssistV1/AgentAssistV1.htm) for more information.

### Note NiCE CXone account details

Follow this step to collect your NiCE CXone account details. You will need this information to configure the NiCE CXone Agent for Service Cloud Voice (BYOT) in Salesforce later.

  * Make a note of your [NiCE Business Unit](https://help.nicecxone.com/content/acd/businessunits/businessunit.htm) number from the NiCE CXone console. In your Salesforce project (which you will clone in an upcoming step), in `ServiceCloudVoicePlatformService.js`, update `CONFIG.niceBusNo` to reflect your NiCE Business Unit number. This will let your Agent Assist UI modules LWC determine the conversationName that NiCE CXone Agent Assist Hub creates (see the `generateNiCEConversationName` method in the same file for details).
  * Make a note of your [NiCE Point of Contact (POC)](https://help.nicecxone.com/content/acd/channels/additionalchannelfeatures/pointsofcontact/pointsofcontact.htm) phone number from the NiCE CXone console. This is the number that your customers will call into to talk to your agents, and that you will use to test this Agent Assist integration.



## Step 2: Set up your Salesforce development project

To start integrating Agent Assist UI modules, follow these steps.

  1. Run the following code to clone the Agent Assist integration repository and open your project:
         
         git clone https://github.com/GoogleCloudPlatform/agent-assist-integrations
         cd salesforce/aa-lwc
         

  2. Run the following commands to download the [UI modules JavaScript](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/modules-overview) files which you deploy later as **Static Resources**. Salesforce requires the static resources to load third-party JavaScript.
         
         npm run generate-static-resources
         npm install
         

  3. Update `ServiceCloudVoicePlatformService.js` with the **NiCE Business Unit number** you noted in a previous step:
         
         const CONFIG = {
         // For this.platform = "servicecloudvoice-nice", the NiCE Business Unit Number
         // https://help.nicecxone.com/content/acd/businessunits/managebusinessunit.htm
         niceBusNo: 1234567 // Make sure this matches your NiCE CXone Business Unit Number.
         };
         




## Step 3: Set up your Salesforce environment

You can integrate Agent Assist UI modules in a specific environment, such as production or development. Salesforce calls these environments [organizations (orgs)](https://help.salesforce.com/s/articleView?id=xcloud.setup_overview.htm&type=5).

### Configure your org with the Salesforce CLI

Follow these steps to use the Salesforce CLI to configure your org for Agent Assist integration.

  1. Run the following code and authenticate the CLI using the Salesforce login details you normally use.
         
         npm run login
         

  2. Run the following code to deploy the LWC to the org.
         
         npm run deploy
         




## Step 4: Create an external client app

The Salesforce LWC uses the client credentials OAuth 2.0 flow to authenticate you. An [external client app](https://help.salesforce.com/s/articleView?id=xcloud.external_client_apps.htm) enables the client credentials flow. Use the app's consumer key and consumer secret to configure the Salesforce LWC to authenticate users with Salesforce.

  1. Click **Setup** > **Setup**.
  2. In the **Quick Find** box, enter **External Client App Manager**.
  3. Click **External Client App Manager** > **New External Client App** > **Create** , then enter the following information. 
     * **External Client App Name** : `lwc auth`
     * **API Name** : `lwc_auth`
     * **Contact Email** : `your_email@example.com`
     * **API (Enable OAuth Settings)** > **Enable OAuth** : Selected
     * **API (Enable OAuth Settings)** > **Callback URL** : `https://login.salesforce.com/services/oauth2/callback`
     * **API (Enable OAuth Settings) > Selected OAuth Scopes**: Access the identity URL service
     * **API (Enable OAuth Settings) > Enable Client Credentials Flow**: Selected
  4. Click **Create**.
  5. Click **Setup** > **Setup**.
  6. In the **Quick Find** box, enter **External Client App Manager**.
  7. Click your external client app's name > **Edit**.
  8. Navigate to **OAuth Policies** > **OAuth Flows and External Client App Enhancements**.
  9. Ensure **Enable Client Credentials Flow** is selected.
  10. For **Run As** , enter your login username.
  11. Click **Save**.
  12. Click **Setup** > **Setup**. In the **Quick Find** box, enter **External Client App Manager**.
  13. Click your external client app's name > **Edit**.
  14. Navigate to **OAuth Settings** > **App Settings** > **Consumer Key and Secret**.
  15. Enter the verification code sent to your email.
  16. Copy the consumer key and consumer secret somewhere secure. You will need these for a later step.



### Establish CORS and content security policies

  1. Click **Setup** > **Setup**.
  2. In the **Quick Find** box, enter **CORS** , then click **Edit**. 
     1. Select **Enable CORS for OAuth endpoints**.
     2. Click **Save**.
  3. Click **Setup** > **Setup**.
  4. In the **Quick Find** box, enter **Trusted URLs** , then click **New Trusted URL**.
  5. Enter the following information: 
     * **API Name** : `ui_connector`
     * **URL** : Enter the URL of the UI Connector Cloud Run Service endpoint you deployed with your Agent Assist Integration Backend. You can find this URL in the [Cloud Run console](https://console.cloud.google.com/run). For example: `https://UI_CONNECTOR_SUBDOMAIN.GCP_REGION.run.app`.
     * **CSP Directives** : Select all checkboxes.
     * Click **Save & New**.
  6. Enter the following information: 
     * **API Name** : `ui_connector_wss`
     * **URL** : Enter the URL of the UI connector Cloud Run Service endpoint you deployed with your Agent Assist Integration Backend. You can find this URL in the [Cloud Run console](https://console.cloud.google.com/run). Change the protocol to wss, for WebSockets traffic. For example: `wss://UI_CONNECTOR_SUBDOMAIN.GCP_REGION.run.app`.
     * **CSP Directives** : Select all checkboxes.
     * Click **Save & New**.
  7. Enter the following information: 
     * **API Name** : **salesforce_domain**
     * **URL** : Enter the URL of your Salesforce Domain with the following format: `https://YOUR_SUBDOMAIN.my.salesforce.com`.
     * **CSP Directives** : Select all checkboxes.
     * Click **Save**.



## Step 5: Install NiCE CXone Agent for Service Cloud Voice (BYOT)

Salesforce provides the add-on license Service Cloud Voice, which allows integration of third-party softphones with your Salesforce instance. NiCE CXone provides a Service Cloud Voice add-on called **NiCE CXone Agent for Service Cloud Voice (BYOT)**. Follow NiCE's documentation to [set up NiCE CXone Agent for Service Cloud Voice (BYOT)](https://help.nicecxone.com/content/agent/agentapplicationadministration/agentforscv/setupagentforscv.htm) in your SCV-enabled Salesforce instance.

## Step 6: Install the Salesforce Lightning Web Component

Follow these steps to use the [Lightning Experience Editor](https://help.salesforce.com/s/articleView?id=platform.lightning_app_builder_customize_lex_pages.htm&type=5) to add the Salesforce Lightning Web Component into the contact page where NiCE CXone Agent for Service Cloud Voice (BYOT) opens when a new call comes in.

  1. Navigate to the **Service Console**.
  2. Sign in to NiCE CXone Agent for Service Cloud Voice (BYOT).
  3. Call the NiCE POC number associated with the NiCE account you signed in with.
  4. Accept the incoming call. This should result in a new Voice Call record tab being opened.
  5. Click **Settings** and select **Edit Page**.
  6. Click **Template** > **Change**. 
     1. Select **Header** and **Two Equal Regions**.
     2. Click **Next**.
     3. Map each region to a new region.
     4. Click **Done**.
  7. From the **Components** list, drag `agentAssistContainerModule` onto the page. Note: The `npm deploy` command provided this component.
  8. Click the component you placed in the previous step and fill in the form fields as follows to add configuration details. 
     * **endpoint** : The URL of your [Agent Integration Backend](https://github.com/GoogleCloudPlatform/agent-assist-integrations/tree/HEAD/aa-integration-backend) UI connector, such as a URL from the [Cloud Run console](https://cloud.google.com/run), like: `https://UI_CONNECTOR_ENDPOINT.GCP_REGION.run.app`
     * **channel** : Indicate that the integration is `voice`.
     * **platform** : Indicate that the platform is `servicecloudvoice-nice`.
     * **conversationProfile** : Your [Agent Assist conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) resource name (example: `projects/GCP_PROJECT_ID/locations/GCP_REGION/conversationProfiles/CONVERSATION_PROFILE_ID`)
     * **consumerKey** : The external client app consumer key from Step 4.
     * **consumerSecret** : The external client app consumer secret from Step 4.
     * **containerHeight** : The height of the Agent Assist container.



## Step 7: Test the integration

You can test the voice integration with a test call to the Salesforce call center.

  1. Sign in to NiCE CXone Agent for Service Cloud Voice (BYOT) from the Omni-Channel widget in the Service Console.
  2. Call your NiCE CXone POC number. You can find this in the [NiCE CXone console](https://help.nicecxone.com/content/acd/channels/additionalchannelfeatures/pointsofcontact/pointsofcontact.htm).
  3. In your Service Console, accept the incoming call. The screen should open a new Voice Call record.
  4. In the Voice Call record, the Salesforce Lightning Web Component should load on the page.
  5. Test both sides of the conversation, ensuring that Agent Assist transcription and features are working [as you've configured them in your conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) in the Agent Assist console.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
