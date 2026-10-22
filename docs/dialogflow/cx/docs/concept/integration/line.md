---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/line/
title: LINE \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:40.572960+00:00
---

# LINE  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/line/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  LINE Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Dialogflow CX's LINE integration lets you to easily create LINE bots with natural language understanding based on Dialogflow CX technology.

**Note:** When using a third party integration, requests and end-user data are sent to both Google and the third party. The terms of service, SLA, pricing, and quotas [for your agent edition](https://docs.cloud.google.com/dialogflow/docs/editions) are applicable for Google's handling of these requests. The third party's terms of service, SLA, pricing, and quotas are applicable for the third party's handling of these requests. 

## Set Up LINE

In order to set up the LINE integration for your agent, you'll need the following:

  * A LINE account
  * The LINE app installed on a mobile device

**Note:** Account sign-up is completed through the mobile app.

### Create a LINE bot

  1. Follow LINE's guide [Getting started with the Messaging API](https://developers.line.biz/en/docs/messaging-api/getting-started/) to create a provider and a **Messaging API** channel (if not created before).
  2. Copy the following information from the created channel in [LINE Developers Console](https://developers.line.biz/console/):

     * **Channel access token (long-lived)**
     * **Channel ID**
     * **Channel secret**



### Set up Dialogflow CX

  1. Click **Manage** tab on the left panel.
  2. Click **Integrations** in the left menu.
  3. Click the **Connect** button on the **Line** tile.
  4. Fill in the following information: 
     * **Channel access token**
     * **Channel ID**
     * **Channel secret**
  5. Choose an environment, as applicable.
  6. Click **Start**.
  7. Copy the **Webhook URL**.



### Enable webhook in LINE

Follow LINE's guide [Set a Webhook URL](https://developers.line.biz/en/docs/messaging-api/building-bot/#setting-webhook-url) to finish the setup.

## Testing

**Note:** Make sure [billing is enabled](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup#billing) on your project before testing the integration.

To test your agent, follow LINE's guide [Adding friends via QR code](https://help.line.me/line/android/pc?lang=en&contentId=20000378) to add the bot to the conversation list. The QR code can be found on the **Messaging API** tab in the [LINE Developers Console](https://developers.line.biz/console/). After that, you can send messages to the bot for testing.

## Rich response messages

The rich response messages are supported via **Custom Payload** in [Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment). Please see [LINE Message Objects](https://developers.line.biz/en/reference/messaging-api/#message-objects) for the message format.

For example, the following custom payload provides a simple LINE text message:
    
    
    {
      "type": "text",
      "text": "Hello, world"
    }
    

The following custom payload provides a LINE template message:
    
    
    {
      "type": "template",
      "altText": "this is a buttons template",
      "template": {
        "type": "buttons",
        "thumbnailImageUrl": "https://example.com/bot/images/image.jpg",
        "title": "Menu",
        "text": "Please select",
        "actions": [
          {
            "type": "postback",
            "label": "Buy",
            "data": "action=buy&itemid=123"
          },
          {
            "type": "postback",
            "label": "Add to cart",
            "data": "action=add&itemid=123"
          },
          {
            "type": "uri",
            "label": "View detail",
            "uri": "http://example.com/page/123"
          }
        ]
      }
    }
    

## Channel specific responses

After you configure the [channel-specific responses](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#channel-specific), the channel `DF_CX_LINE` is automatically used when the agent responds to Line messages.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
