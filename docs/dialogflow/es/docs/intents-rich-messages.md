---
url: https://docs.cloud.google.com/dialogflow/es/docs/intents-rich-messages/
title: Rich response messages \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:26.733614+00:00
---

# Rich response messages  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/intents-rich-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Rich response messages Stay organized with collections  Save and categorize content based on your preferences. 

Many of the [integration](https://docs.cloud.google.com/dialogflow/docs/integrations) platforms support platform-specific _rich response messages_. These messages can be used to provide the end-user with more than just text responses. There are a variety of response types to choose from. For example, you can show images, play audio, or provide buttons. Each platform supports a subset of the available response types.

## Where to find this data

When building an agent, it is most common to use the Dialogflow ES console ([visit documentation](https://docs.cloud.google.com/dialogflow/docs/console), [open console](https://dialogflow.cloud.google.com)). The instructions below focus on using the console. To access intent response data:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Select **Intents** in the left sidebar menu.
  4. Select an intent.
  5. Scroll down to the **Responses** section.



If you are building an agent using the API instead of the console, see the [Intents reference](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#intents). The API field names are similar to the console field names. The instructions below highlight any important differences between the console and the API.

## Add rich response messages

The **Responses** section has tabs for each platform, including a _default_ platform. You can define responses for the default platform, which can be used on all platforms.

![Screenshot of adding rich messages.](https://docs.cloud.google.com/static/dialogflow/es/docs/images/intent-rich-messages.png)

You can define responses for platform-specific tabs, which only work on the corresponding platforms. You can also opt to use the default responses for a specific platform, so you do not need to create duplicate text responses for all platforms.

![Screenshot of adding rich messages.](https://docs.cloud.google.com/static/dialogflow/es/docs/images/intent-rich-messages-slack.png)

To add rich response messages:

  1. Select the tab for your desired platform. If the desired platform tab is not shown, click the add _add_ button and select it.
  2. Click the **Add Responses** button. A dropdown shows the response types supported by the platform.
  3. Choose the response type. These are described below.
  4. Enter fields for the selected response type.
  5. Add more platform tabs and responses as needed. You can add up to 10 ordered messages in each tab.
  6. Click **Save**.



You can use [parameter references](https://docs.cloud.google.com/dialogflow/docs/intents-actions-parameters#values) in your responses to reference parameters provided by the end-user or [events](https://docs.cloud.google.com/dialogflow/docs/events-overview#param) at runtime.

## Text responses

By default, **Text** responses send a text response to the end-user.

If text-to-speech is [enabled for an agent](https://docs.cloud.google.com/dialogflow/docs/agents-settings#speech) or [requested by detect intent requests](https://docs.cloud.google.com/dialogflow/docs/how/detect-intent-tts), the supplied text is used to synthesize speech and play the audio. In this case, supplied text can optionally use the [Speech Synthesis Markup Language (SSML)](https://cloud.google.com/text-to-speech/docs/ssml).

The fields are:

  * List of text or SSML entries



When entering a response, press **Shift** \+ **Enter** to input a newline or just **Enter** to input another text response.

The following limitations apply:

  * Max of 300 text entries per text response



## Image responses

**Image** responses send an image to the end-user. They contain the following fields:

  * Publicly accessible URL for the image



## Card responses

**Card** responses send an image, a card title, a card subtitle, and interactive buttons to the end-user. The style of the card varies by platform.

You can configure buttons to send the end-user to a URL or to send pre-configured text to Dialogflow as though the end-user provided an expression.

Some of the fields are optional, depending on the platform:

  * Publicly accessible URL for an image
  * Card title
  * Card subtitle
  * List of buttons with the following fields: 
    * Button title
    * Text to send as end-user expression or URL to open



The following limitations apply:

  * Max of 10 cards per platform and per language for an intent. For example, if your agent supports English, French, platform X, and platform Y, an intent can have at most 40 cards:

    * 10 English cards for platform X
    * 10 English cards for platform Y
    * 10 French cards for platform X
    * 10 French cards for platform Y



## Quick reply responses

**Quick Reply** responses send a button to the end-user. You can configure buttons to send pre-configured text to Dialogflow as though the end-user provided an expression.

The fields are:

  * Button title
  * List of text entries to send as end-user expression



The following limitations apply:

  * Max of one quick reply response per platform and per language for an intent. For example, if your agent supports English, French, platform X, and platform Y, an intent can have at most 4 quick replies:

    * 1 English quick reply for platform X
    * 1 English quick reply for platform Y
    * 1 French quick reply for platform X
    * 1 French quick reply for platform Y
  * Max of 10 text entries per quick reply response.

  * Max of 20 characters per text entry.




## Synthesize speech responses

**Synthesize Speech** responses are used to synthesize speech from text responses and play the audio. The supplied text can optionally use the [Speech Synthesis Markup Language (SSML)](https://docs.cloud.google.com/text-to-speech/docs/ssml).

The fields are:

  * Text or SSML



The following limitations apply:

  * Only supported by the [Dialogflow phone gateway](https://docs.cloud.google.com/dialogflow/es/docs/integrations/phone-gateway) integration
  * Max of 20 synthesize speech responses per intent



## Play audio responses

**Play Audio** responses are used to play audio files. Audio files are supplied in a [Cloud Storage](https://docs.cloud.google.com/storage/docs) bucket.

The fields are:

  * Cloud Storage object URI in `gs://bucket-name/object-name` format.



The following limitations apply:

  * Only supported by the [Dialogflow phone gateway](https://docs.cloud.google.com/dialogflow/es/docs/integrations/phone-gateway) integration
  * Audio file specifications: a single channel (mono) of linear PCM audio (2 bytes / sample) at 8kHz
  * Max of 20 play audio responses per intent



## Transfer call responses

**Transfer Call** responses are used to transfer the caller for a telephony integration.

The fields are:

  * The telephone number to transfer to.



The following limitations apply:

  * Only supported by the [Dialogflow phone gateway](https://docs.cloud.google.com/dialogflow/es/docs/integrations/phone-gateway) integration

  * Only US telephone numbers are supported




## Custom payload responses

Some platforms support a custom payload response to handle non-standard, advanced responses. These custom payloads are supplied in a JSON format defined in the platform's documentation.

You can also send a custom payload to integrations that you develop. It won't be processed by Dialogflow, so you need to handle it in your own business logic.

You can configure a custom payload for multiple platforms. To configure this, use the default platform and a JSON format similar to the following:
    
    
    {
      "facebook": {
        "attachment": {
          "type": "",
          "payload": {}
        }
      },
      "slack": {
        "text": "",
        "attachments": []
      }
    }
    

**Note:** Custom payload JSON must be limited to 24 levels of depth.

## Google Assistant response types

The Google Assistant integration provides many response message types. For more information, see the [Google Assistant responses reference](https://developers.google.com/assistant/conversational/responses).

## Additional response types

Other message types are supported by various platforms. You can see the complete list in the [response message REST reference](https://docs.cloud.google.com/dialogflow/docs/reference/rest/v2/projects.agent.intents#Message). See the platform integration documentation for more information.

[ Previous arrow_back  Responses  ](https://docs.cloud.google.com/dialogflow/es/docs/intents-responses)

[ Next Default intents  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/intents-default)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
