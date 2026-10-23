---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/meta-messenger/
title: Messenger from Meta \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:26.539517+00:00
---

# Messenger from Meta  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/meta-messenger/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Messenger from Meta Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Using the Meta Messenger Integration, you can create a Meta Messenger bot to interact with your users.

**Note:** When using a third party integration, requests and end-user data are sent to both Google and the third party. The terms of service, SLA, pricing, and quotas [for your agent edition](https://docs.cloud.google.com/dialogflow/docs/editions) are applicable for Google's handling of these requests. The third party's terms of service, SLA, pricing, and quotas are applicable for the third party's handling of these requests. 

## How it works

**Note:** This integration doesn't support [Workplace from Meta](https://developers.facebook.com/docs/workplace).

This is how the integration works:

  * You create a Meta app that uses the [Meta Messenger Platform](https://developers.facebook.com/docs/messenger-platform/overview).
  * You configure the Dialogflow CX Integration and Meta app so that they communicate with each other.
  * The Dialogflow CX Integration sends messages to your users using the [Meta Messenger API](https://developers.facebook.com/docs/messenger-platform/reference/send-api/).
  * The Dialogflow CX Integration receives messages from your users by acting as the [Meta Webhooks for Messenger Platform](https://developers.facebook.com/docs/messenger-platform/getting-started/webhook-setup/).



## Setup

Make sure [billing is enabled](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup#billing) on your project before testing the integration.

To set up the integration:

  1. Follow the steps to create a Meta app: [Meta App Development](https://developers.facebook.com/docs/apps).
  2. Set up the Meta app to use the Meta Messenger Platform. Follow the steps in the [Meta Webhooks for Messenger Platform](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup) documentation to accomplish the following: 
     * Add the Messenger Platform to your Meta app.
     * Subscribe your app to a Meta page. Make sure `messages` and `messaging_postbacks` are enabled in the page subscription.
     * Copy the access token provided at this step. This token is used to configure the integration from the Dialogflow CX console.
     * Don't configure the webhook or test your integration yet.
  3. Configure the integration from the Dialogflow CX console: 
     1. Go to the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
     2. Select the **Manage** tab on the navigation menu.
     3. Select **Integrations**.
     4. Click the **Connect** button on the **Meta Messenger** tile.
     5. Complete the configuration dialog fields: 
        * **App secret:** Enter the app secret from [App Dashboard Basic Settings](https://developers.facebook.com/docs/development/create-an-app/app-dashboard/basic-settings).
        * **Verify token:** Enter any private token you need. Copy this value. This is used to configure the Meta Messenger Webhook.
        * **Page access token:** Enter the access token you copied during the Meta app setup.
        * **Enable get started button:** Select this checkbox to enable the Get started button.
        * **Webhook URL:** Copy this value. This is used to configure the Meta Messenger Webhook.
        * **Start:** Select this checkbox to start the integration service for your agent.
  4. Finish setup of the Meta app and test it. Follow the steps in the [Meta Webhooks for Messenger Platform](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup) documentation to accomplish the following: 
     * Configure the Meta webhook for your app. Use the **Webhook URL** and **Verify token** values you copied earlier. Be sure to enable `messages` and `messaging_postbacks` in the page subscription.
     * Test your app.



## Events

The following events are invoked by this integration. You can create [custom event handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-custom) to define what to do when the events are triggered.

Event | Description  
---|---  
`FACEBOOK_WELCOME` | Triggered when an end-user clicks the [Meta Messenger Get Started Button](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/get-started-button/).  
`FACEBOOK_MEDIA` | Triggered when the message from an end-user contains attachments (for example, audio, image, or video).  
  
## Get started button

Set up the [Meta Messenger get started button](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api/get-started-button/):

  1. Toggle **Enable Get Started Button** when enabling this integration service.

     * This integration service lets you enable the button by calling the [Messenger Profile API](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api).
           
           curl -X POST \
           -H "Content-Type: application/json" \
           -d '{"get_started": {"payload": "FACEBOOK_WELCOME"}}' \
           "https://graph.facebook.com/v10.0/me/messenger_profile?access_token=${PAGE_ACCESS_TOKEN}"
           

  2. Create a [custom event handler](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-custom) for the `FACEBOOK_WELCOME` event.




To test it:

  1. Delete the previous conversation with your Meta page if applicable. 
     * The **Get Started** button only shows up on new conversations.
  2. Start a new conversation with your Meta page.
  3. Click the **Get Started** button, and verify the response from the custom event handler.



You can call [Messenger Profile API](https://developers.facebook.com/docs/messenger-platform/reference/messenger-profile-api) to manage the **Get Started** button. This can help with testing.

To check the status of the **Get Started** button, use the following request:
    
    
    curl -X GET \
    "https://graph.facebook.com/v10.0/me/messenger_profile?fields=get_started&access_token=${PAGE_ACCESS_TOKEN}"
    

You can use the following request to disable the **Get Started** button:
    
    
    curl -X DELETE \
    -H "Content-Type: application/json" \
    -d '{"fields": ["get_started"]}' \
    "https://graph.facebook.com/v10.0/me/messenger_profile?access_token=${PAGE_ACCESS_TOKEN}"
    

## Rich response messages

Rich response messages are supported using **Custom Payload** in [Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment). For more information, see the [Send API Parameters Message Object](https://developers.facebook.com/docs/messenger-platform/reference/send-api#parameters) documentation for the message format.

For example, the following custom payload provides a text message:
    
    
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
    

## Channel-specific responses

After you configure the [channel-specific responses](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#channel-specific), the agent automatically uses the `DF_CX_FB_MESSENGER` channel to respond to Meta Messenger messages.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
