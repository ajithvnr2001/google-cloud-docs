---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/meta-workplace/
title: Workplace from Meta \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:52.590691+00:00
---

# Workplace from Meta  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/meta-workplace/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Workplace from Meta Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Using the Meta Workplace integration, you can create a Meta Workplace bot to interact with your end-users.

**Note:** When using a third party integration, requests and end-user data are sent to both Google and the third party. The terms of service, SLA, pricing, and quotas [for your agent edition](https://docs.cloud.google.com/dialogflow/docs/editions) are applicable for Google's handling of these requests. The third party's terms of service, SLA, pricing, and quotas are applicable for the third party's handling of these requests. 

## How it works

This is how the integration works:

  * You create a Customer Integration that uses the [Meta Workplace](https://developers.facebook.com/docs/workplace/).
  * You configure the Dialogflow CX integration and Workplace instance, so that they communicate with each other.
  * The Dialogflow CX integration sends messages to the end-user by using the [Send API from Meta](https://developers.facebook.com/docs/messenger-platform/reference/send-api/).
  * The Dialogflow CX integration receives messages from the end-user by acting as the [ Workplace Webhook from Meta](https://developers.facebook.com/docs/workplace/reference/webhooks/).



## Setup

**Note:** Make sure [billing is enabled](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup#billing) on your project before testing the integration.

To set up the integration:

  1. Follow the steps to create a Meta Workplace Custom Integration : [Creating an Meta Workplace custom integration](https://www.workplace.com/resources/tech/integrations/chat-bot).

     * Create a Meta Workplace Custom Integration.
     * You are provided with an App Secret at this step. Copy this value. This token will be used to configure the integration from the Dialogflow CX console.
     * Create or reset the Access token of your integration. Copy this value. This token will be used to configure the integration from the Dialogflow CX console.
     * Set up the Custom Integration Permissions. Make sure `Message any member` is enabled in Permissions.
  2. Configure the integration from the Dialogflow CX console:

     1. Go to the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
     2. Click the **Manage** tab on the left panel.
     3. Click **Integrations** in the left sidebar menu.
     4. Click the **Connect** button on the **Meta Workplace** tile.
     5. A configuration dialog opens:

        * **App secret** : Enter the app secret from [App Dashboard Basic Settings](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/basic-settings/).

        * **Access token** : Enter the access token you copied during the Meta app setup above.

        * **Verify token** : You can enter any private token you desire. Copy this value. This will be used to configure the Meta Workplace Webhook.

        * **Webhook URL** : Copy this value. This will be used to configure the Meta Workplace Webhook.

        * **Start** : Click to start this integration service for your agent.

  3. Finish setup of the Meta Workplace Custom Integration and test it. Follow steps in the [Webhook for Meta Workplace](https://developers.facebook.com/docs/workplace/integrations/custom-integrations/webhooks/) documentation to accomplish the following:

     * Configure the Meta webhook for your app. Use the **Webhook URL** and **Verify token** values you copied above.
     * Subscribe your Integration to Webhook Topics. Be sure to enable `messages` and `messaging_postbacks` in the page subscription.
     * Test your app.



## Rich response messages

The rich response messages are supported using **Custom Payload** in [Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment). See [Send API Parameters Message Object](https://developers.facebook.com/docs/messenger-platform/reference/send-api#parameters) for the message format.

For example, the following custom payload provides a simple text message:
    
    
    {
      "text": "Hello, world"
    }
    

The following custom payload provides an image message:
    
    
    {
      "attachment": {
        "type": "image",
        "payload": {
          "url": "https://example.com/test.jpg"
        }
      }
    }
    

## Channel specific responses

When configured, [channel specific responses](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#channel-specific) with channel `DF_CX_FB_MESSENGER` are automatically used when the agent responds to Meta Messenger messages.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
