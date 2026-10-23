---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-voice-twilio/
title: Agent Assist for Salesforce voice integration with Twilio Flex \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:53.742047+00:00
---

# Agent Assist for Salesforce voice integration with Twilio Flex  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-voice-twilio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Agent Assist for Salesforce voice integration with Twilio Flex Stay organized with collections  Save and categorize content based on your preferences. 

The integration of Twilio with Salesforce Service Cloud Voice (SCV) enables Salesforce representatives to make and receive calls in Salesforce using the capabilities of the Twilio platform.

## Before you begin

To integrate Salesforce voice with Twilio Flex, you need access to the following resources:

  * [Salesforce and Agent Assist resources](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-byb)
  * [Agent Assist for Salesforce app](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-setup)
  * Flex account

Follow the instructions in [Twilio setup page](https://www.twilio.com/docs/flex/onboarding-guide/set-up-your-flex-account) to create a Flex account. Write down your account string identifier (SID), Twilio phone number, and Auth token.

  * Google telephony platform provisioned phone number

Follow the instructions in [Google telephony platform](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/siprec#telephony_integration) to obtain a provisioned phone number to integrate with Twilio's Siprec connector add-on.




## Step 1: Setup Twilio service cloud voice

Follow the instructions in [Twilio guide](https://www.twilio.com/docs/flex/admin-guide/integrations/salesforce-service-cloud-voice) to set up Salesforce SCV with Twilio as a partner telephony provider. 

## Step 2: Integrate Agent Assist with Twilio Flex

Follow these steps to integrate Agent Assist with Twilio Flex.

### Install SIPREC connector add-on

The SIPREC connector add-on allows your Twilio Flex account to make [SIPREC forks](https://www.twilio.com/docs/voice/api/siprec) of voice call media streams to Agent Assist. Follow these steps to install the SIPREC connector add-on.

  1. Navigate to **Twilio Home** and enter **Marketplace** in the search box.

[Twilio Home](http://console.twilio.com/)

  2. Click **Catalog** > **Stream connectors** > **Siprec connector** > **Install** > **Add instance**.

  3. Navigate to the **Configure** tab and configure the plugin with the following details:

     * **Unique name** : `SipRec1`
     * **Session recording server** : `sip:+<GTP-provisioned-phone-number>@216.239.36.145:5672;transport=tls;secure=true;edge=umatilla`
  4. Click **Save**.




### Configure Twilio functions

Follow these steps to configure two Twilio functions, `conversation-name` and `wrap-up`.

  1. Navigate to the [Twilio console](http://console.twilio.com/) and enter **Function** in the search box.
  2. Click **Functions** > **Create service**.
  3. Name the new service `ui-connector-auth` and click **Next**.
  4. Click **Add +** > **Add Function**.



Follow these steps to create the `conversation-name` function.

  1. Name the function `conversation-name`.
  2. Click the lock and change the function visibility to **Public**.
  3. Copy the [`ui-connector-auth.js`](https://github.com/GoogleCloudPlatform/agent-assist-integrations/tree/HEAD/salesforce/aa-lwc/twilio/functions/ui-connector-auth.js) code and paste it in the editor.
  4. Click **Save**.



You can automate the call completion process with a `wrap-up` function and [`EventCallbackUrl`](https://www.twilio.com/docs/taskrouter/api/event/reference#event-callbacks). This eliminates the need to manually close out calls in both Salesforce and Twilio Flex. Follow these steps to create a `wrap-up` function to receive events through `EventCallbackUrl`.

  1. Navigate to the [Twilio console](http://console.twilio.com/) > search bar and enter **Taskrouter Workspace**.
  2. Select **Taskrouter workspaces**.
  3. Make a note of the SID in the workspace column.
  4. Navigate to the editor and name the function `wrap-up`.
  5. Add the following code into the editor.
         
         /**
         * @desc A Twilio Function that wraps up a conversation automatically to avoid agents being stuck
         * in a wrap up state while in Salesforce's Service Console.
         */
         exports.handler = function(context, event, callback) {
          const response = new Twilio.Response();
          const client = context.getTwilioClient();
         
          /**
           * @TODO Add your workspaceSid to this variable.
           */
          const workspaceSid = ""
         
          response.appendHeader('Content-Type', 'application/json');
         
          if (!event.EventType) {
            response.setBody({});
             return callback(null, response);
           }
         
           /**
            * This event is dispatched with the Event Callback Url, which is assigned in a Taskrouter Workspace's
            * Settings.
            */
           if (event.EventType === 'task.wrapup') {
            client.taskrouter.v1.workspaces(workspaceSid)
               .tasks(event.TaskSid)
               .update({
                assignmentStatus: 'completed',
                reason: 'Auto-completed via Function'
               })
               .then(() => {
                 response.setBody({ status: "completed" });
                 callback(null, response);
               })
               .catch(err => {
                response.setStatusCode(500);
                response.setBody({ error: err.message });
                callback(null, response);
              });
           } else {
            response.setBody({ status: "ignored" });
             callback(null, response);
           }
         };
         

  6. Locate the variable **`workspaceSid`** , and update it with the workspace SID from the Taskrouter Workspace SID step.

  7. Make note of the URL of your service. You must use the full URL of the `wrap-up` function in the next step.

  8. Click **Save** > **Deploy all**.

  9. Navigate to the Twilio console and enter **Taskrouter Workspaces** in the search bar.

  10. Click the workspace you're using > **Settings** > **Event callbacks** > **Event callback URL**.

  11. Enter the URL of the `wrap-up` function from the previous step.

  12. Click **Callback events** and set it to **Specific events**.

  13. Click **Select all** > **Save**.




### Configure IVR with Flex Studio

To set up your automated phone menu, use Twilio Studio to build a call flow that initiates a SIPREC fork. That fork sends a media stream directly to Agent Assist. The call flow also makes an HTTP post to share the phone number and conversation ID with Agent Assist.

Follow these steps to configure interactive voice response (IVR) with Flex Studio.

  1. Navigate to the [Twilio console](http://console.twilio.com/) and enter **Studio** in the search box.
  2. Click **Studio** and the studio dashboard page opens with the list of flows.
  3. On the studio dashboard page, you can do the following:

     * Update existing flow.
     * Create a flow.



#### Update existing flow

Follow these steps in the Twilio console to update existing flows.

  1. Select the flow you want to update.
  2. Click **Develop** > **Phone Numbers** > **Manage** > **Active Numbers**. There should be one row in the table with the default Twilio number provisioned for your Flex Account.
  3. Navigate to **Voice - Studio Workflow** and click **Voice IVR**.



#### Create a flow

Create new flows to make a HTTP request, run a function, fork a stream, and send to Flex. Follow these steps in the Twilio console to create an HTTP request flow.

  1. Navigate to the **Studio dashboard** page and click **Create new flow**.
  2. Navigate to **Search widget** and enter **HTTP**.
  3. Drag the **Make HTTP request** widget onto the flow panel.
  4. Configure a widget with the following details and click **Save**.

     * **Widget name** : `register_twilio`
     * **Request method** : `POST`
     * **Request URL** : 
           
           your-ui-connector-cloud-run-url.run.app/register-app

     * **Content type** : Application/JSON
     * **Request body** :
           
           {
           "accountSid": "yourTwilioAccountSid",
           "authToken": "yourTwilioAccountAuthToken"
           }
           




Follow these steps to create a run function flow.

  1. Enter **Run function** in the search widget.
  2. Drag the **Run function** widget onto the flow panel to connect with **Success** and **Fail** outputs of the `register_twilio` widget.
  3. Configure the run function widget with the following details:

     * **Widget name** : `conversation_name`
     * **Service** : `ui-connector-auth`
     * **Environment** : ui
     * **Function** : `/conversation-name`
     * **Function parameters** : Enter following function parameters

       * **Token** : 
             
             {{ widgets.register_twilio.parsed.token }}

       * **Endpoint** : 
             
             your-ui-connector-cloud-run-url.run.app/conversation-name

       * **Phone** : 
             
             {{ trigger.call.From | replace_first:'+','' }}

       * **`ConversationName`** : 
             
             projects/project/locations/location/conversations/{{ trigger.call.CallSid }}

  4. Click **Save**.




Follow these steps to create a fork stream flow.

  1. Enter **Fork stream** in the search widget.
  2. Move the **Fork Stream widget** onto the flow panel to connect with **Success** and **Fail** outputs of the make HTTP request widget.
  3. Configure the fork stream widget with following details:

     * **Stream action** : Start
     * **Stream type** : `Siprec`
     * **Connector name** : `Siprec1`
     * **Tracks** : Both tracks
     * **Stream parameters** : Enter the following stream parameters.

       * **Key** : conversation
       * **Value** : 
             
             projects/project-id/conversations/{{trigger.call.CallSid}}

  4. Click **Save**.




Follow these steps to create the send to Flex flow.

  1. Enter **Send to Flex** in the search widget.
  2. Move **Send to Flex** onto the flow panel, and connect **Next** from **Fork Stream** to **Send to Flex**.
  3. Click **Send to Flex**.
  4. Configure the send to flex widget with following details.

     * **Workflow** : Choose the workflow you're using for SCV.
     * **Task channel** : Voice
     * **Attributes** : 
           
           {"agent_assist__ConversationId__c":"{{trigger.call.CallSid}}"}

     * **URL method** : `POST`
  5. Click **Save** > **Publish**.




## Step 4: Configure record page for Agent Assist

Follow these steps to configure the record page for Agent Assist.

  1. Create a [voice call record page](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-setup#record-pages) for Agent Assist.
  2. Click **Activation** > **App default** > **Assign as app default**.
  3. Select **Twilio for service cloud voice**.
  4. Click **Next** > **Save**.



## Step 5: Test Agent Assist integration

Follow these steps to test Agent Assist.

  1. Navigate to Salesforce.
  2. Click **apps App Launcher**.
  3. In the search field, enter **Twilio for service cloud voice**. This opens the **Cases** page.
  4. Navigate to the **Omni channel** panel and click **New**.
  5. Click **check_circle Check** to call your Twilio Flex number. You made a note of this at the beginning.
  6. Test both sides of the conversation and ensure that Agent Assist features are working as you've configured them.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
