---
url: https://docs.cloud.google.com/agent-assist/docs/salesforce-voice/
title: Salesforce voice integration with Twilio Flex \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:39:39.904563+00:00
---

# Salesforce voice integration with Twilio Flex  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-assist/docs/salesforce-voice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Salesforce voice integration with Twilio Flex Stay organized with collections  Save and categorize content based on your preferences. 

![Architecture for the Agent Assist and Twilio Flex integration with
Salesforce](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aa-salesforce-twilio-flex-architecture.jpg)

This voice integration uses the [Twilio Open CTI integration](https://www.twilio.com/docs/flex/admin-guide/integrations/salesforce) to bring a [Twilio Flex](https://www.twilio.com/en-us/flex) call center into your Salesforce instance.

Agent Assist uses the media stream from the Twilio Flex call to provide suggestions to your agents in the [Salesforce Lightning Service Console](https://help.salesforce.com/s/articleView?id=service.console_lex_service_intro.htm&type=5).

## Before you begin

To integrate Agent Assist UI modules with Salesforce, you must first set up the [required resources](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/salesforce-required-resources).

Before running the backend deployment script, configure the following Twilio-specific environment variables in your `.env` file (in addition to the common variables):

  * `APP_AUTH_OPTION`: Set this to `Twilio`.
  * `TWILIO_ACCOUNT_SID`: Set this to your **Twilio Account SID**.



## Step 1: Set up Twilio Flex

Twilio Flex serves as the softphone in this integration. You can sign in to the Twilio console to set up a Flex account. Visit the [Twilio setup page](https://www.twilio.com/docs/flex/onboarding-guide/set-up-your-flex-account) to get detailed instructions on how to create a Flex account.

### Install SIPREC connector add-on

The SIPREC connector add-on allows your Twilio Flex account to make SIPREC forks of voice call media streams to Agent Assist. Follow these steps to install the SIPREC connector add-on.

  1. Navigate to **Twilio Home** > **Marketplace** > **Catalog** > **Twilio** > **Siprec Connector**.
  2. Click **Install** > the **Terms and conditions acknowledgment** checkbox > **Install**.
  3. On the **Configure** tab, configure the plugin with the following details: 
     * **Unique Name** : `SipRec1`
     * **Session Recording Server** : 
           
           sip:+<GTP-provisioned-phone-number>@216.239.36.145:5672;transport=tls;secure=true;edge=umatilla

     * See the [telephony integration documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/siprec#telephony_integration) for more details on provisioning a GTP number. You can ignore the SBC configuration and validation steps, because they're complete for the Twilio Siprec connector.
  4. Navigate to **Twilio Home** > **Functions and Assets**. 
     * If **Functions and Assets** is not visible, pin it from **Explore Products**.
  5. Click **Create Service**.
  6. Name the new service `ui-connector-auth`.
  7. In the editor that appears, click **Add +** > **Add Function**.
  8. Name the function `conversation-name`.
  9. Click lock, and change the function visibility to **Public**.
  10. Copy and paste the entire contents of [`ui-connector-auth.js`](https://github.com/GoogleCloudPlatform/agent-assist-integrations/tree/HEAD/salesforce/aa-lwc/twilio/functions/ui-connector-auth.js) from the GitHub repository into the editor.
  11. Click **Save**.
  12. Click **Deploy All**.



### Configure IVR with Flex Studio

The IVR consists of configuring a programmatic call flow with Twilio [Studio](https://www.twilio.com/docs/studio) to make the SIPREC fork of the media stream to Agent Assist. It also makes an HTTP post to share the phone number and conversation ID with Agent Assist. Follow these steps to configure IVR with Flex Studio.

  1. Navigate to the [Twilio Console](http://console.twilio.com).
  2. Click **Develop** > **Phone Numbers** > **Manage** > **Active Numbers**. There should be one row in the table with the default Twilio number provisioned for your Flex Account.
  3. In the **Voice - Studio Workflow** section, click **Voice IVR**.
  4. Drag a **Make HTTP Request** widget into the flow.
  5. Disconnect **Incoming Call** from the **SendCallToAgent** widget's input.
  6. Connect **Incoming Call** to the **Make HTTP Request** widget's input.
  7. Configure the **Make HTTP Request** widget with the following details: 
     * **Widget Name** : `register_twilio`
     * **Request Method** : `POST`
     * **Request URL** : `<your-ui-connector-cloud-run-url>.run.app/register-app`
     * **Content type** : Application/JSON
     * **Request body** : 
           
           {
           "accountSid": "<yourTwilioAccountSid>",
           "authToken": "<yourTwilioAccountAuthToken>"
           }

  8. Drag a **Run Function** widget into the flow.
  9. Connect the **Success** and **Fail** outputs of the `register_twilio` widget to the input of the **Run Function** widget.
  10. Create a widget with the following details: 
     * **Widget Name** : `conversation_name`
     * **Service** : `ui-connector-auth`
     * **Environment** : `ui`
     * **Function** : `conversation-name`
     * **Function Parameters** : 
       * **token** : 
             
             {{ widgets.register_twilio.parsed.token }}

       * **endpoint** : `<your-ui-connector-cloud-run-url>.run.app/conversation-name`
       * **phone** : 
             
             {{ trigger.call.From | replace_first:'+','' }}

       * **conversationName** : 
             
             projects/<project>/locations/<location>/conversations/TW-{{ trigger.call.From | replace_first:'+','' }}-{{ trigger.call.CallSid }}

  11. Drag a **Fork Stream** widget into the flow.
  12. Connect the **Success and Fail** outputs of the **Make HTTP Request** widget to the input of the **Fork Stream** widget.
  13. Connect the **Next** node of the **Fork Stream** widget to the **SendCallToAgent** widget.
  14. Configure the **Fork Stream** widget as follows:

     * **Stream Action** : Start
     * **Stream Type** : Siprec
     * **Connector Name** : `Siprec1`
     * **Tracks** : Both Tracks
     * **Stream Parameters** :

       * **Key** : `conversation`
       * **Value** :
             
             projects/<gcp-project-id>/conversations/TW-{{trigger.call.From | replace_first:'+','' }}-{{trigger.call.CallSid}}
             

  15. Click **Save** > **Publish**.




### Account details

Follow this step to collect your Twilio Flex account details. You need this information to configure the Flex CTI in Salesforce later.

  1. Navigate to **Twilio Home** > [Account Dashboard](http://console.twilio.com), and write down the following information: 
     * Account SID
     * My Twilio phone number



## Step 2: Set up your Salesforce development project

To start integrating Agent Assist UI modules, follow these steps.

  1. Run the following code to clone the Agent Assist integration repository and open your project:
         
         git clone https://github.com/GoogleCloudPlatform/agent-assist-integrations
         cd salesforce/aa-lwc
         

  2. Run the following commands to download the [UI modules JavaScript](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/modules-overview) files which you deploy later as **Static Resources**. Salesforce requires static resources to load third-party JavaScript.
         
         npm run generate-static-resources
         npm install
         




## Step 3: Set up your Salesforce environment

You can integrate Agent Assist UI modules in a specific environment, such as production or development. Salesforce calls these environments [organizations (orgs)](https://help.salesforce.com/s/articleView?id=xcloud.setup_overview.htm&type=5).

### Configure your org with the Salesforce CLI

Follow these steps to use the Salesforce CLI to configure your org for Agent Assist integration.

  1. Run the following code and authenticate the CLI using the Salesforce login details you normally use. 
         
         npm run login

  2. Run the following code to deploy the LWC to the org. 
         
         npm run deploy




## Step 4: Create an external client app

The Salesforce LWC uses the client credentials OAuth 2.0 flow to authenticate you. An [external client app](https://help.salesforce.com/s/articleView?id=xcloud.external_client_apps.htm&type=5) enables the client credentials flow. Use the app's consumer key and consumer secret to configure the Salesforce LWC to authenticate users with Salesforce.

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
     * **URL** : Enter the URL of the UI Connector Cloud Run Service endpoint you deployed with your Agent Assist Integration Backend. You can find this URL in the [Cloud Run console](https://console.cloud.google.com/run). For example: `https://UI_CONNECTOR_SUBDOMAIN.GCP_REGION.run.app`.
     * **CSP Directives** : Select all checkboxes.
     * Click **Save & New**.
  6. Enter the following information: 
     * **API Name** : `ui_connector_wss`
     * **URL** : Enter the URL of the UI connector Cloud Run Service endpoint you deployed with your Agent Assist Integration Backend. You can find this URL in the [Cloud Run console](https://console.cloud.google.com/run). Change the protocol to wss, for WebSockets traffic. For example: `wss://UI_CONNECTOR_SUBDOMAIN.GCP_REGION.run.app`.
     * **CSP Directives** : Select all checkboxes.
     * Click **Save & New**.
  7. Enter the following information: 
     * **API Name** : `salesforce_domain`
     * **URL** : Enter the URL of your Salesforce Domain with the following format: `https://YOUR_SUBDOMAIN.my.salesforce.com`.
     * **CSP Directives** : Select all checkboxes.
     * Click **Save & New**.
  8. Enter the following information: 
     * **API Name** : `twilio_flex`
     * **URL** : `https://flex.twilio.com`
     * **CSP Directives** : Select all checkboxes.
     * Click **Save**.



## Step 5: Install Twilio Flex CTI plugin

Salesforce provides [Salesforce Open CTI](https://help.salesforce.com/s/articleView?id=service.cloud_cti_api_overview.htm&type=5) to allow integration of third-party softphones with your Salesforce instance.

[Twilio Flex CTI](https://help.salesforce.com/s/articleView?id=service.cloud_cti_api_overview.htm&type=5) uses Salesforce Open CTI to allow you to use Flex directly within your Salesforce instance. Follow [Twilio's instructions](https://www.twilio.com/docs/flex/admin-guide/integrations/salesforce) to set up Twilo Flex CTI in your Salesforce instance.

## Step 6: Install the Salesforce Lightning Web Component

Follow these steps to use the [Lightning Experience Editor](https://help.salesforce.com/s/articleView?id=platform.lightning_app_builder_customize_lex_pages.htm&type=5) to add the Salesforce Lightning Web Component into the contact page where your Twilio Flex CTI opens when a new call comes in.

  1. Navigate to the **Service Console** , and select **Contacts**.
  2. Select a contact record.
  3. Click **Settings** and select **Edit Page**.
  4. Click **Template** > **Change**. 
     1. Select **Header** and **Two Equal Regions**.
     2. Click **Next**.
     3. Map each region to a new region.
     4. Click **Done**.
  5. From the **Components** list, drag `agentAssistContainerModule` onto the page. Note: The `npm deploy` command provided this component.
  6. Click the component you placed in the previous step and fill in the form fields as follows to add configuration details. 
     * **endpoint** : The URL of your [Agent Integration Backend](https://github.com/GoogleCloudPlatform/agent-assist-integrations/tree/HEAD/aa-integration-backend) UI connector, such as a URL from the [Cloud Run console](https://cloud.google.com/run), like: `https://UI_CONNECTOR_ENDPOINT.GCP_REGION.run.app`
     * **channel** : Indicate that the integration is for `voice`.
     * **platform** : Indicate that the platform is `twilio`.
     * **conversationProfile** : Your [Agent Assist conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) resource name (example: `projects/GCP_PROJECT_ID/locations/GCP_REGION/conversationProfiles/CONVERSATION_PROFILE_ID`)
     * **consumerKey** : The external client app consumer key from a previous step.
     * **consumerSecret** : The external client app consumer secret a previous step.
     * **containerHeight** : The height of the Agent Assist container.



## Step 7: Test the integration

You can test the voice integration with a test call to the Salesforce call center.

  1. Sign in to Twilio Flex from your **Service Console**.
  2. Call your Twilio Flex number. You made a note of this in Step 1.
  3. In your **Service Console** , accept the call. The screen should open a new or existing contact page for the number that called.
  4. If it is a new contact page, save the contact. When the contact page loads, the Salesforce Lightning Web Component should load on the page.
  5. Test both sides of the conversation, ensuring that Agent Assist features are working as you've configured them.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
