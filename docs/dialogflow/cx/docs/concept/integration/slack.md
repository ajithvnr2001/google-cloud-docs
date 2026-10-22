---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/slack/
title: Slack \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:13.006742+00:00
---

# Slack  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/slack/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Slack Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Slack Integration lets you to easily create Slack bots with natural language understanding based on Dialogflow CX technology.

**Note:** When using a third party integration, requests and end-user data are sent to both Google and the third party. The terms of service, SLA, pricing, and quotas [for your agent edition](https://docs.cloud.google.com/dialogflow/docs/editions) are applicable for Google's handling of these requests. The third party's terms of service, SLA, pricing, and quotas are applicable for the third party's handling of these requests. 

## Limitations

  * Only **text input** in the [agent's default language](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings) is supported by this integration.



## Set Up Slack

In order to set up the Slack integration for your agent, you'll need the following:

  * A Slack account
  * A Slack workspace



### Create a Slack bot

  1. Navigate to your [Slack Apps](https://api.slack.com/apps)
  2. Create a new slack app from an app manifest. Below is an example manifest. Make sure that the **oath_config** and **event_subscriptions** fields match with the example manifest. 
         
         display_information:
           name: Dialogflow CX
           description: Dialogflow CX integration
           background_color: "#1148b8"
         features:
           app_home:
             home_tab_enabled: false
             messages_tab_enabled: true
             messages_tab_read_only_enabled: false
           bot_user:
             display_name: CX
             always_online: true
         **oauth_config:
           scopes:
             bot:
               - app_mentions:read
               - chat:write
               - im:history
               - im:read
               - im:write
               - incoming-webhook**
         settings:
           **event_subscriptions:
             request_url: https://dialogflow-slack-4vnhuutqka-uc.a.run.app
             bot_events:
               - app_mention
               - message.im**
           org_deploy_enabled: false
           socket_mode_enabled: false
           token_rotation_enabled: false
         

  3. Install your application into the workspace of your choice 
     * **Bot User OAuth Token**
       * Navigate to Install App > OAuth Tokens for Your Workspace > Bot User OAuth Token
     * **Signing Token**
       * Navigate to Basic Information > App Credentials > Signing Secret



### Set up Dialogflow CX

  1. Click **Manage** tab on the left panel.
  2. Click **Integrations** in the left menu.
  3. Click the **Connect** button on the **Slack** tile.
  4. Fill in the following information: 
     * **Access token**
     * **Signing token**
  5. Choose an environment, as applicable.
  6. Click **Start**.
  7. Copy the **Webhook URL**.



### Enable webhook in Slack

Return to your [Slack App](https://api.slack.com/apps) and paste your webhook url under **Event Subscriptions > Enable Events > Request URL**

## Testing

**Note:** Make sure [billing is enabled](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup#billing) on your project before testing the integration.

To test your configured app, in the workspace you installed it in, mention it in a group channel or send it a DM.

## Rich response messages

The rich response messages are supported via **Custom Payload** in [Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment). Please see [Slack message API](https://api.slack.com/methods/chat.postMessage) for the message format.

**Note:** If it is not specified in the custom payload, the channel field will be automatically injected with the channel id of the input message.

For example, the following custom payload provides a simple Slack text message:
    
    
    {
      "text": "Hello, world"
    }
    

## Channel specific responses

After you configure the [channel-specific responses](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#channel-specific), the channel `DF_CX_SLACK` is automatically used when the agent responds to Slack messages.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
