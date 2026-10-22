---
url: https://docs.cloud.google.com/dialogflow/es/docs/integrations/workplace/
title: Workplace from Facebook \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:17.131547+00:00
---

# Workplace from Facebook  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/integrations/workplace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Workplace from Facebook Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Using the Dialogflow Facebook Workplace integration, you can create a Workplace from Facebook bot to interact with your end-users.

**Note:** When using a third party integration, requests and end-user data are sent to both Google and the third party. The terms of service, SLA, pricing, and quotas [for your agent edition](https://docs.cloud.google.com/dialogflow/docs/editions) are applicable for Google's handling of these requests. The third party's terms of service, SLA, pricing, and quotas are applicable for the third party's handling of these requests. 

## Limitations

Only the [default agent language](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings#lang) is supported by this integration.

## How it works

This is how the integration works:

  * You configure the Dialogflow integration and Workplace instance, so that they communicate with each other.
  * The Dialogflow integration sends messages to the end-user by using the [Messenger API from Facebook](https://developers.facebook.com/docs/messenger-platform/reference/send-api/).
  * The Dialogflow integration receives messages from the end-user by acting as the [Workplace Webhook from Facebook](https://developers.facebook.com/docs/workplace/reference/webhooks).



## Start

To start the integration:

  1. Register a [Workplace](https://www.workplace.com/) instance if you don't have one, and make sure you are the **System Admin** of the group.

  2. Enable the integration from the Dialogflow Console:

     1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
     2. Click **Integrations** in the left sidebar menu.
     3. Click **Workplace from Facebook**.
     4. Click **START** and you will be redirected to Workplace to finish the installation: 
        * Log into your Workplace account. The account needs to be a **System Admin** on Workplace to install integrations.
        * Click **Add to Workplace** in the pop-up window that asks you to install Dialogflow integration. You also have the option to customize the name for the bot.
  3. Test your app:

     1. Go to [Workplace](https://www.workplace.com/) and log into the account.
     2. Find **Dialogflow** (or the customized name of your bot) in **Bots** from the **Home** section of the sidebar and start chatting with the bot.



## Cancel

If you clicked the **START** button but do not want to finish the installation on Workplace:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).

  2. Click **Integrations** in the left sidebar menu.

  3. Click **Facebook Workplace** :

     1. If you see a **CANCEL** button: Click **CANCEL** to cancel the installation.
     2. If you see a **STOP** button: Follow instructions below to uninstall the integration.



## Stop

To stop a successfully installed integration:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).

  2. Click **Integrations** in the left sidebar menu.

  3. Click **Facebook Workplace**.

  4. Click **STOP** and you will be redirected to Workplace to finish the installation:

     1. Log into your Workplace account. The account needs to be a **System Admin** on [Workplace](https://www.workplace.com/) to uninstall integrations.
     2. Find and select the Dialogflow integration from the installed integrations on Workplace, click **Uninstall** to finish the uninstallation.
  5. Dialogflow integration will be uninstalled.




## Rich response messages

This integration translates some [rich response messages](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages) messages to [Facebook Messenger Platform message types](https://developers.facebook.com/docs/messenger-platform/send-messages).

### Image responses

[Image responses](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages#image) are sent to Facebook Messenger as [Facebook Messenger file attachment messages](https://developers.facebook.com/docs/messenger-platform/reference/attachment-upload-api#attachment). The `message.attachment.type` value is set to `image`. The following formats are supported:

  * jpg
  * png
  * static gif
  * animated gif



### Card responses

[Card responses](https://cloud.google.com/dialogflow/docs/intents-rich-messages#card) are sent to Facebook Messenger as [Facebook Messenger generic templates](https://developers.facebook.com/docs/messenger-platform/reference/templates/generic).

### Quick reply responses

[Quick reply responses](https://cloud.google.com/dialogflow/docs/intents-rich-messages#quick) are sent to Facebook Messenger as [Facebook Messenger quick replies](https://developers.facebook.com/docs/messenger-platform/reference/buttons/quick-replies).

### Custom payload responses

To send other types of Facebook Messenger messages, you can use a [custom payload](https://cloud.google.com/dialogflow/docs/intents-rich-messages#custom).

The general format of the custom payload looks like:
    
    
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
            




## Limitations

  1. A Dialogflow agent can only be installed on one Workplace instance, but you can install multiple Dialogflow agents on one Workplace instance.

  2. To remove a failed installation, you need to both cancel the installation on Dialogflow and remove the installation on Workplace.




## Migration

If you are using Messenger integration and you are going to migrate it to Workplace integration, you'll need to:

  1. Stop the Messenger integration.

  2. Remove the callback_url on the Facebook app by reversing steps in [Setting Up Your Facebook App](https://developers.facebook.com/docs/messenger-platform/getting-started/app-setup).

  3. Start the Workplace integration following steps above.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
