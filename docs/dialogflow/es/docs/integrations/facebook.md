---
url: https://docs.cloud.google.com/dialogflow/es/docs/integrations/facebook/
title: Messenger from Facebook \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:50.733448+00:00
---

# Messenger from Facebook  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/integrations/facebook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Messenger from Facebook Stay organized with collections  Save and categorize content based on your preferences. 

The Dialogflow Facebook Messenger integration lets you create a Facebook Messenger bot to interact with your end-users.

**Note:** When using a third party integration, requests and end-user data are sent to both Google and the third party. The terms of service, SLA, pricing, and quotas [for your agent edition](https://docs.cloud.google.com/dialogflow/docs/editions) are applicable for Google's handling of these requests. The third party's terms of service, SLA, pricing, and quotas are applicable for the third party's handling of these requests. 

## Limitations

This integration supports only the [default agent language](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings#lang).

## How it works

The integration works as follows:

  1. Create a Facebook app that uses the [Facebook Messenger platform](https://developers.facebook.com/docs/messenger-platform/overview).
  2. Configure the Dialogflow integration and Facebook app so that they communicate with each other.
  3. The Dialogflow integration sends messages to the end-user using the [Facebook Messenger API](https://developers.facebook.com/docs/messenger-platform/reference/send-api/).
  4. The Dialogflow integration receives messages from the end-user by acting as the [Facebook Messenger webhook](https://developers.facebook.com/docs/messenger-platform/webhooks).



## Setup

To set up the integration:

  1. Follow the steps to create a Facebook app: [Facebook app development](https://developers.facebook.com/docs/development).

  2. Set up the Facebook app to use the Facebook Messenger Platform. Follow steps in the [Setting up your Facebook app](https://developers.facebook.com/docs/messenger-platform/webhooks) documentation to accomplish the following:

     * Add the Messenger Platform to your Facebook app.
     * Subscribe your app to a Facebook page. You are provided with an access token at this step. Copy this value. This token is used to configure the integration from the Dialogflow console.
     * Don't configure the webhook or test your integration yet.
  3. Configure the integration from the Dialogflow console:

     1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
     2. Click **Integrations** in the sidebar menu.
     3. Click **Facebook Messenger**.
     4. A configuration dialog opens: 
        * **Show old callback URL:** If this toggle is shown, it defaults to Off. This is a temporary option to accommodate a recent modification to the Facebook Messenger API. Don't change this toggle unless instructed by Dialogflow support. After all agents have been updated, this option is removed.
        * **Callback URL:** Copy this value. This is used to configure the Facebook Messenger webhook.
        * **Verify Token:** You can enter any private token you need. Copy this value. This is used to configure the Facebook Messenger webhook.
        * **Page Access Token:** Enter the access token you copied when creating the Facebook page.
        * **Start:** Click to start this integration service for your agent.
  4. Finish setup of the Facebook app and test it. Follow steps in the [Setting up your Facebook app](https://developers.facebook.com/docs/messenger-platform/webhooks) documentation to accomplish the following:

     * Configure the Facebook webhook for your app. Use the **Callback URL** and **Verify Token** values you copied earlier. Be sure to enable **messages** and **messaging_postbacks**.
     * Test your app.



## Events

The following [events](https://docs.cloud.google.com/dialogflow/docs/events-overview) are invoked by this integration:

  * `FACEBOOK_WELCOME`: Triggered when an end-user starts a conversation with your bot.



## Rich response messages

This integration translates some [rich response messages](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages) messages to [Facebook Messenger Platform message types](https://developers.facebook.com/docs/messenger-platform/send-messages).

### Image responses

[Image responses](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages#image) are sent to Facebook Messenger as [Facebook Messenger file attachment messages](https://developers.facebook.com/docs/messenger-platform/reference/attachment-upload-api#attachment). The `message.attachment.type` value is set to `image`.

The following formats are supported:

  * JPG
  * PNG
  * Static GIF
  * Animated GIF



### Card responses

[Card responses](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages#card) are sent to Facebook Messenger as [Facebook Messenger generic templates](https://developers.facebook.com/docs/messenger-platform/reference/templates/generic).

### Quick reply responses

[Quick reply responses](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages#quick) are sent to Facebook Messenger as [Facebook Messenger quick replies](https://developers.facebook.com/docs/messenger-platform/reference/buttons/quick-replies).

### Custom payload responses

To send other types of Facebook Messenger messages, you can use a [custom payload](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages#custom).

The general format of the custom payload looks like the following:
    
    
    {
      "facebook": {
        message
      }
    }
    

In place of `message`, provide the Facebook Messenger `message` object. For details of the `message` object, see the [Facebook Messenger API reference](https://developers.facebook.com/docs/messenger-platform/reference/send-api/).

For example:

  * Send an audio link: 
        
        {
          "facebook": {
            "attachment": {
              "type": "audio",
              "payload": {
                "url": "https://example.com/audio/test.mp3"
              }
            }
          }
        }
            

  * Send a playable video: 
        
        {
          "facebook": {
            "attachment": {
              "type": "video",
              "payload": {
                "url": "https://example.com/video.mp4"
              }
            }
          }
        }
            

  * Send a file: 
        
        {
          "facebook": {
            "attachment": {
              "type": "file",
              "payload": {
                "url": "https://example.com/file.pdf"
              }
            }
          }
        }
            




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
