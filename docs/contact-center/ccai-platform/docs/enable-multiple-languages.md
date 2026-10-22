---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/enable-multiple-languages/
title: Enable multiple languages for IVR, mobile, and web channels \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:35.446183+00:00
---

# Enable multiple languages for IVR, mobile, and web channels  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/enable-multiple-languages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Enable multiple languages for IVR, mobile, and web channels Stay organized with collections  Save and categorize content based on your preferences. 

In order to support multiple markets, multiple languages can be activated and used in the channels you make available.

Adding languages creates a new queue structure for each channel, enabling all queue settings and assignments, messages, and all queue-specific settings to be set per language.

  * The English US menu is used as the template for all queues during the setup process.

To add new queues you will need to add using the English US language then configure each new language queue configuration.

  * If you don't want a queue to be active for a specific language, you can skip assigning agents.

  * After you add a language, it's available for Interactive Voice Response (IVR), Mobile, and Web channels.

  * Adding a language creates a new queue structure, allowing you to:

    * Customize the names of the queues.

    * Upload language-specific messages played or displayed.

    * Adds **language** as a new dimension to reporting.

    * Select from a list of languages when making an outbound call.


**Note:** See [Supported Languages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/supported-languages#UUID-f1750720-b4af-9115-3a1d-c2bde09dd13b) for the full list of languages supported by CCAI Platform.

## Steps to set up a language

  1. Adding the language

  2. Customizing messages

  3. Customizing queues for the language




## Adding the language

  1. Go to **Settings > Languages & Messages**.

  2. Click **Add Language** and select a language of choice from the drop-down.




## Customizing language messages

  1. Go to **Settings > Languages & Messages**.

  2. Select the language from the drop-down.

If you are using Multiple Mobile apps, you can select the app from the channel menu on the right to toggle between configured mobile apps.

  3. Once the language is selected, the page contains all messages callers hear. These messages should be configured for the new language.

**Note:** We recommend completing this step even if the feature associated with the message is not being utilized so that the system is ready if it's ever enabled.

(Example of TTS typed in the new language)

  4. Click **Apply** to save.




## Customize queue settings for the language

All languages other than English depend on the setup of the English queues, so as you create new languages you will be editing the English queue structure as a template. To make changes to the queue structure, use the English settings.

  1. Click **Customize Queues** to edit each live queue channel for your new language. This will need to be repeated for all channels: IVR, mobile and web.

  2. You can edit the queue names in the new language.

Click the name of the queue and type in the new or translated queue name. The queue name will be heard if using text-to-speech for IVR announcements and will be seen if you are using Mobile or Web SDKs.

  3. Mark the checkbox next to **Instant Voice Call** to enable calls to this queue.

  4. Click **Assign agents** to assign Agents to this queue for incoming calls.

  5. **Repeat steps 2-4 for each menu** : Queues will turn from red to white when fully set up and ready to go live.

  6. **Go Live** : Languages can go live before all messages and queues have been configured, but, be aware that once a language is live, it is available for your consumers to access. Only set a language to live if you have configured all the necessary messages and queues. Once live, make sure to test by calling an assigned number or accessing the queues using the SDK.




## Troubleshooting

If the **Go live** button is not working, try following these steps:

  1. Make sure ALL menu options for all channels have been edited. Some may appear to have been named but it is only the carry-over from the English US queue upon creation and needs to be edited.

  2. Make sure all prompts in the Languages & Messages have something either uploaded or written in the text-to-speech field.

  3. Even if you aren't using a channel, you may need to assign one agent to a queue in each channel to make sure it's active.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
