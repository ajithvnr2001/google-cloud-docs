---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/google-chat/
title: Google Chat \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:50.986435+00:00
---

# Google Chat  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/google-chat/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Google Chat Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Dialogflow CX's Google Chat Integration lets you create Google Chat apps with natural language understanding based on Dialogflow CX technology.

**Note:** When using a third party integration, requests and end-user data are sent to both Google and the third party. The terms of service, SLA, pricing, and quotas [for your agent edition](https://docs.cloud.google.com/dialogflow/docs/editions) are applicable for Google's handling of these requests. The third party's terms of service, SLA, pricing, and quotas are applicable for the third party's handling of these requests. 

## Limitations

  * Only **text input** in the [agent's default language](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings) is supported by this integration.



## Set up Google Chat

In order to set up the Google Chat integration for your agent, you'll need the following:

  * A [Google Workspace](https://workspace.google.com/features/) account with access to [Google Chat](https://workspace.google.com/products/chat/).
  * A [Google Cloud project](https://developers.google.com/workspace/guides/create-project).



### Enable the Google Chat API

Before using Google APIs, you need to turn them on in a Google Cloud project. You can turn on one or more APIs in a single Google Cloud project.

  1. In the https://console.cloud.google.com/, enable the Google Chat API and the Dialogflow API.

  2. Confirm that you're enabling the APIs in the correct Cloud project, then click **Next**.

  3. Confirm that you're enabling the correct APIs, then click **Enable**.




### Set up from Dialogflow CX

  1. Go to the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Integrations** in the left sidebar menu.
  6. Click **Connect** on **Google Chat**.
  7. Fill in the following required information: 
     * **Name** : The name displayed to users who interact with or consume content created by this app, such as in messages, search, and @mentions. For example `Dialogflow CX App`.
     * **Avatar URL** : The avatar image which is displayed to users who interact with the app. Specify an HTTPS URL that hosts a square (aspect ratio of 1:1) PNG image. Recommended minimum size: 256 by 256 pixels. For example `https://developers.google.com/workspace/chat/images/quickstart-app-avatar.png`.
     * **Description** : A description of the app. For example, `A helpful bot that responds to real human conversation`.
  8. Choose an **Environment** as applicable.
  9. Enter **email addresses** to make this Chat app available to specific people and groups as applicable.
  10. Click **Start**.



## Testing

**Note:** Make sure [billing is enabled](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup#billing) on your project before testing the integration.

To test your configured app, mention it in a Google Chat space or send it a DM. For example,

  1. Open [Google Chat](https://chat.google.com).
  2. Click **New chat**.
  3. In the **Add 1 or more people** field, type the name of your Chat app.
  4. Select your Chat app from the results. A direct message opens.

**Note:** If you don't see your Chat app in the list of results, ensure that you've made your Chat app available to your Google Workspace account.

## Rich response messages

The rich response messages are supported using **Custom Payload** in [Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment). See [Google Chat message API](https://developers.google.com/chat/api/reference/rest/v1/spaces.messages#Message) for the message format.

**Note:** If they are not specified in the custom payload, the Space and Thread objects will be automatically injected with the resource ID from the input message.

### Text message

The following custom payload provides a Google Chat [text message](https://developers.google.com/workspace/chat/messages-overview#anatomy-text):
    
    
    {
      "text": "Hello, world"
    }
    

The following custom payload provides a Google Chat [text message](https://developers.google.com/workspace/chat/messages-overview#anatomy-text) if you are using a [Chat add-on](https://developers.google.com/workspace/add-ons/chat):
    
    
            {
                hostAppDataAction: {
                  chatDataAction: {
                    createMessageAction: {
                      message: {
                        text: "Your pizza delivery is here!"
                      }
                    }
                  }
                }
            }
    

### Card message

The following custom payload provides a Google chat [card message](https://developers.google.com/workspace/chat/messages-overview#anatomy-card):
    
    
    {
      'cardsV2': [{
        'cardId': 'createCardMessage',
        'card': {
          'header': {
            'title': 'A card message!',
            'subtitle': 'Sent from Dialogflow CX',
            'imageUrl': 'https://developers.google.com/chat/images/chat-product-icon.png',
            'imageType': 'CIRCLE'
          },
          'sections': [
            {
              'widgets': [
                {
                  'buttonList': {
                    'buttons': [
                      {
                        'text': 'Read the docs!',
                        'onClick': {
                          'openLink': {
                            'url': 'https://developers.google.com/workspace/chat'
                          }
                        }
                      }
                    ]
                  }
                }
              ]
            }
          ]
        }
      }]
    }
    

The following custom payload provides a Google chat [card message](https://developers.google.com/workspace/chat/messages-overview#anatomy-card) if you are using a [Chat add-on](https://developers.google.com/workspace/add-ons/chat):
    
    
    {
      "host_app_data_action": {
        "chat_data_action": {
          "create_message_action": {
            "message": {
              "cardsV2": [
                {
                  "card_id": "basic1",
                  "card": {
                    "header": {
                      "title": "This is a card!",
                      "subtitle": "Sent from Conversational Agents (Dialogflow CX)",
                      "imageUrl": "https://developers.google.com/chat/images/chat-product-icon.png",
                      "imageType": "CIRCLE"
                    },
                    "sections": [
                      {
                        "widgets": [
                          {
                            "buttonList": {
                              "buttons": [
                                {
                                  "text": "Open Google!",
                                  "color": {
                                    "red": 0.101960786,
                                    "green": 0.4509804,
                                    "blue": 0.9098039
                                  },
                                  "onClick": {
                                    "openLink": {
                                      "url": "http://google.com"
                                    }
                                  }
                                }
                              ]
                            }
                          }
                        ]
                      }
                    ]
                  }
                }
              ]
            }
          }
        }
      }
    }
    

## Channel-specific responses

When configured, [channel-specific responses](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#channel-specific) with channel `DF_CX_GOOGLE_CHAT` will be automatically used when the agent responds to Google Chat messages.

## Related topics

  * [Build a Dialogflow CX Google Chat app that understands and responds with natural language](https://developers.google.com/workspace/chat/build-dialogflow-chat-app-natural-language)
  * [Extend Google Chat using Workspace add-ons](https://developers.google.com/workspace/add-ons/chat)
  * [Use event objects to trigger functions](https://developers.google.com/workspace/add-ons/chat/build#event-objects)
  * [Learn how to send Google Chat messages](https://developers.google.com/workspace/add-ons/chat/send-messages)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
