---
url: https://docs.cloud.google.com/dialogflow/es/docs/integrations/google-chat/
title: Dialogflow Google Chat integration \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:42.965378+00:00
---

# Dialogflow Google Chat integration  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/integrations/google-chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Dialogflow Google Chat integration Stay organized with collections  Save and categorize content based on your preferences. 

By integrating Dialogflow with Google Chat, you leverage features in both services:

  * **Google Chat**. Provides a messaging platform with a front-end user interface for one-on-one conversations and chat spaces. Through Google Chat, you can enhance user interfaces by building cards incorporating icons, images, buttons, text-entry fields, or apps like Google Maps.
  * **Dialogflow**. Provides a natural language understanding platform for automated conversations and dynamic responses. Through Dialogflow, you can interpret and fulfill user intents, for example, to schedule appointments or process purchases.



Although you can also use Google Chat to fulfill user requests, Dialogflow lets users express their requests through regular conversation.

## How it works

Once you build a Dialogflow-enabled Google Chat app, you can make the app available to the following:

  * **General public**. Licensed Google Workspace users can download your app through the Google Workspace Marketplace.
  * **Google Workspace domain**. A Google Workspace administrator can specify which apps users can add to Google Chat.
  * **App testers**. While testing your app, you can restrict access to the app.



In Google Chat, a user can have a direct conversation with your app or invoke the app from within a space. The following happens:

  1. A user sends a message to a Chat app.
  2. Google Chat sends a JSON request to the Chat app, which could be hosted in Cloud Functions.
  3. The Chat app receives the JSON request, and parses it. During this parsing, the Chat app invokes Dialogflow.
  4. The Chat app sends a request to Dialogflow that includes the user's natural-language message text.
  5. Dialogflow interprets the user's text and sends a response to the Chat app.
  6. The Chat app parses Dialogflow's response and sends a JSON response to Google Chat.
  7. Google Chat receives the Chat app's JSON response and renders a response in the form of a text message, a card message, or a dialog message in the UI.
  8. Google Chat shares this response as-is or presents a rich response using a card-based UI.



This page describes how to integrate Dialogflow with Google Chat and configure rich chat responses.

**Note:** Google Chat was formerly called Hangouts Chat, and Chat apps were formerly called Chat bots. Although Google Chat and the Google Cloud console use the term _apps_ , the Dialogflow console still uses the term _bots_.

## Limitations

With Google Chat integrations, a Dialogflow agent can use only the [default agent language](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings#lang).

## Before you begin

Only licensed Google Workspace users can use Google Chat apps. Your Google Workspace administrator must do the following:

  * [Add a Google Workspace account for you](https://support.google.com/a/answer/33310). 
  * [Allow users to install Chat apps](https://support.google.com/a/answer/7651360).



## Build a Dialogflow agent

If you haven't yet built a Dialogflow agent but would like to see how an agent interacts with Google Chat, follow this [Quickstart](https://docs.cloud.google.com/dialogflow/es/docs/quick/build-agent) to create a simple agent. Do not however delete the agent. Next, we set up the agent with a Google Chat interface.

## Set up Google Chat

To set up your Dialogflow agent with Google Chat, you can use either of the following:

  * Dialogflow console
  * Google Cloud console



### Set up Google Chat using the Dialogflow console

To integrate Google Chat using the Dialogflow console, follow these steps:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. In the left menu, select a Dialogflow project.
  3. Click **Integrations**.
  4. Click **Google Chat**. If Google Chat is not one of the options, see Troubleshoot.
  5. Select who can access the app.
  6. [Optional] Select an environment to run the agent.
  7. Click **Start**. 



Your Google Chat app is now live and available to those you selected.

To configure the app, click **Google Chat** again, then **CONFIGURE BOT DETAILS**. This displays the Google Cloud console page for the Google Chat API, where you can configure [app parameters](https://developers.google.com/chat/how-tos/apps-publish#about_app_configuration) like the app avatar.

### Set up Google Chat using the Google Cloud console

To integrate Google Chat using the Google Cloud console, follow these steps:

  1. Select the Dialogflow project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Click _menu_.

  3. Click **APIs & Services**, then **Library**.

  4. Search for and click **Google Chat API**.

  5. Click **Enable**.

  6. Click the **Configuration** tab.

  7. Configure the app.

  8. In the **Visibility** pane, select who can access the app:

     * App testers. Select **Make this chat available to specific people** and enter their email addresses.
     * General public or Enterprise Google Workspace domain. [Publish the app](https://developers.google.com/chat/how-tos/apps-publish).
  9. Click **Save**. Your Google Chat app is now live and available to those you selected.




## Test

Before testing your Chat app, make sure you've started it, as described in Set up Google Chat.

You can test your app using either of these methods:

  * Chat directly with the app
  * Invoke the app from a space



### Chat directly with the app

  1. Open [Google Chat](https://chat.google.com).
  2. In the **Chat** pane, click **+** and select **Find apps**.
  3. Search for and select your app. If Google Chat does not list your app, see Troubleshoot.
  4. Click **Chat**.
  5. In the chat entry field, enter a natural language phrase to test the app.



### Invoke the app from a space

  1. Open [Google Chat](https://chat.google.com).
  2. In the **Spaces** pane, click **+** and select **Create a space**.
  3. Enter the space name **Test**.
  4. Click **Create**.
  5. In the chat entry field, enter **@** and select your app to auto-complete the name.
  6. After the auto-completed app name, enter a natural language phrase to test the app.



## Troubleshoot

Error | Solution  
---|---  
The [Dialogflow ES console](https://dialogflow.cloud.google.com) > Integrations page does not display Google Chat as an option. | Try refreshing the page: In the left menu, click **Intents** , then click **Integrations**.  
[Google Chat](https://chat.google.com) does not list your app as available. | Ensure your Google Workspace administrator [added a Google Workspace account for you](https://support.google.com/domains/answer/6304542) and [allowed users to install Chat apps](https://support.google.com/a/answer/7651360). Then make sure you've started the Chat app, as described in Set up Google Chat.  
  
## Rich response messages

This integration translates some [rich response messages](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages) messages to [Google Chat message formats](https://developers.google.com/chat/reference/message-formats).

### Text Responses

[Text responses](https://cloud.google.com/dialogflow/docs/intents-rich-messages#text) are sent to Google Chat as [Text messages](https://developers.google.com/chat/reference/message-formats/basic). With this formatting you can make text bold or italics by wrapping the text in certain (markdown light) symbols.

The text message response, visually looks the same as the Default Text Response in the Dialogflow Console. However, the raw API response will look a bit different. It also sets the platform config to _GOOGLE_HANGOUTS_ , which could be interesting when building agents for multiple integrations.
    
    
    "fulfillmentMessages": [
    {
       "text": {
       "text": [
            "This is a test."
       ]
    },
      "platform": "GOOGLE_HANGOUTS"
    },
    

### Cards

[Card responses](https://cloud.google.com/dialogflow/docs/intents-rich-messages#card) are sent to Google Chat as [Card messages](https://developers.google.com/chat/reference/message-formats/cards).

### Images

[Image responses](https://cloud.google.com/dialogflow/docs/intents-rich-messages#image) are sent to Google Chat as [Google Chat Image Widgets](https://developers.google.com/chat/ui/widgets/image).

### Custom Payload

**Note:** This integration does not support [card actions](https://developers.google.com/chat/api/reference/rest/v1/cards#action).

To send other types of Google Chat messages, you can use a [custom payload](https://docs.cloud.google.com/dialogflow/es/docs/intents-rich-messages#custom).

Google Chat Custom Payload allows you to create more advanced cards. One card can have one or many sections. Each section could have a header. You can have a look into the [Google Chat message formats cards reference guide](https://developers.google.com/chat/reference/message-formats/cards), to see some of the combinations you can create with this. However, using custom payloads means that you will have to provide the JSON format.

**Note:** When you copy and paste the examples from the reference guide to the custom payload box in Dialogflow, make sure the editor doesn't contain any linting errors. You can't test the results in the Dialogflow Simulator but can test it directly in Google Chat.

Here is an example of a custom payload using the Cards v1 format:
    
    
    {
      "hangouts": {
        "header": {
          "title": "Pizza Delivery Customer Support",
          "subtitle": "pizzadelivery@example.com",
          "imageUrl": "https://goo.gl/aeDtrS"
        },
        "sections": [{
          "widgets": [{
            "keyValue": {
              "icon": "TRAIN",
              "topLabel": "Order No.",
              "content": "12345"
            }
          },
          {
            "keyValue": {
              "topLabel": "Status",
              "content": "In Delivery"
            }
          }]
        },
        {
          "header": "Location",
          "widgets": [{
            "image": {
              "imageUrl": "https://dummyimage.com/600x400/000/fff"
            }
          }]
        },
        {
          "header": "Buttons - I could leave the header out",
          "widgets": [{
            "buttons": [{
              "textButton": {
                "text": "OPEN ORDER",
                "onClick": {
                  "openLink": {
                    "url": "https://example.com/orders/..."
                  }
                }
              }
            }]
          }]
        }]
      }
    }

## Stop the Chat app

To stop the Google Chat app from being available, you can use either of the following:

  * Dialogflow console

  * Google Cloud console




### Stop the Chat app using the Dialogflow console

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. In the left menu, select a Dialogflow project.
  3. Click **Integrations**.
  4. Click **Google Chat**. If Google Chat is not one of the options, see Troubleshoot.
  5. Click **Stop**.



### Stop the Chat app using the Google Cloud console

  1. Select the Dialogflow project from the Google Cloud console.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Click _menu_.

  3. Click **APIs & Services**, then **Library**.

  4. Search for and click **Google Chat API**.

  5. Click **Manage**.

  6. Click the **Configuration** tab.

  7. In the **App status** field, select **DISABLED**.




## More information

For more information about using Google Chat, see the following:

  * [Google Chat API developer docs](https://developers.google.com/chat/)
  * [Build a Google Workspace add-on that extends Google Chat](https://developers.google.com/workspace/add-ons/chat/)
  * [Video: Integrate Dialogflow with Google Chat](https://youtu.be/aRswG2oowEA)
  * [Codelab: Integrating Dialogflow with Google Chat](https://codelabs.developers.google.com/codelabs/chatbots-dialogflow-hangouts#0)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
