---
url: https://docs.cloud.google.com/dialogflow/es/docs/integrations/line/
title: LINE \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:11.217433+00:00
---

# LINE  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/integrations/line/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  LINE Stay organized with collections  Save and categorize content based on your preferences. 

With Dialogflow's [LINE](https://line.me/en/) integration, you can use your Dialogflow agent as a LINE bot.

**Note:** When using a third party integration, requests and end-user data are sent to both Google and the third party. The terms of service, SLA, pricing, and quotas [for your agent edition](https://docs.cloud.google.com/dialogflow/docs/editions) are applicable for Google's handling of these requests. The third party's terms of service, SLA, pricing, and quotas are applicable for the third party's handling of these requests. 

## Limitations

Only the [default agent language](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings#lang) is supported by this integration.

## How it works

This is how the integration works:

  * You create a [LINE channel](https://developers.line.biz/en/glossary/#channel).
  * You associate your Dialogflow agent with that channel, so that they communicate with each other.
  * The Dialogflow integration sends messages to the end-user by using the [LINE Messaging API](https://developers.line.biz/en/docs/messaging-api/overview/).
  * The Dialogflow integration receives messages from the end-user by acting as the [LINE Webhook](https://developers.line.biz/en/docs/messaging-api/receiving-messages/).



## Setup

To set up the integration:

  1. Follow the steps to create a LINE channel: [Getting started with the Messaging API](https://developers.line.biz/en/docs/messaging-api/getting-started/).
  2. Get the LINE webhook URL from the Dialogflow Console: 
     1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
     2. Click **Integrations** in the left sidebar menu.
     3. Click **LINE**.
     4. Copy the **Webhook URL** value. You will need this to configure your LINE webhook.
  3. Configure a LINE webhook: 
     1. Follow the steps to configure a LINE webhook for your channel: [LINE Receiving messages (webhooks)](https://developers.line.biz/en/docs/messaging-api/receiving-messages/).
     2. Provide the LINE webhook configuration with the webhook URL copied above.
     3. Copy the **Channel ID** , **Channel secret** , and **Channel access token** values. You will need these values to configure your Dialogflow integration.
  4. Configure the Dialogflow integration: 
     1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
     2. Click **Integrations** in the left sidebar menu.
     3. Click **LINE**.
     4. Paste the **Channel ID** , **Channel secret** , and **Channel access token** into the respective fields.
     5. Choose an environment, as applicable.
     6. Click **START**.



## Testing

To test your agent, tap on the three horizontal dots on the main screen of the LINE app. Then tap the QR code icon and scan the QR code on the settings page of your bot. This adds your bot to the list of conversations.

## Rich response messages

The following [rich response messages](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages) are supported.

### Image responses

A Dialogflow image response type is sent to LINE as a [LINE image message type](https://developers.line.biz/en/docs/messaging-api/message-types/#image-messages).

The supported formats and sizes are as follows:

  * jpeg
  * 1 MB max size
  * 240 x 240 max dimensions



### Card responses

A Dialogflow card response type is sent to LINE as a [LINE template message type](https://developers.line.biz/en/docs/messaging-api/message-types/#template-messages).

### Quick reply responses

A Dialogflow quick reply response type is sent to LINE as a [LINE template message type](https://developers.line.biz/en/docs/messaging-api/message-types/#template-messages).

### Custom payload responses

You can send most [LINE message types](https://developers.line.biz/en/docs/messaging-api/message-types) with a custom payload response.

**Caution:** LINE flex message types are currently not supported.

For example, the following custom payload provides a LINE template message:
    
    
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
