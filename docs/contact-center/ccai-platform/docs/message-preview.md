---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/message-preview/
title: Message Preview \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:15.861122+00:00
---

# Message Preview  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/message-preview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Message Preview Stay organized with collections  Save and categorize content based on your preferences. 

With **Message Preview** , agents can see what the consumer is typing before the message is sent. Allowing agents to proactively prepare for the consumer's incoming queries by performing actions such as retrieving information from the customer's account or checking on the status of an order before the message is sent. By being better prepared for consumer inquiries, agents will be able to significantly decrease the Average Hold Time and improve the consumer's overall experience.

**Note:** For implementation information contact Support.

### Enable Message Preview

  1. Go to **Settings > Chat**.

  2. Navigate to the **Web & Mobile** section.

  3. In the **Web & Mobile Chat Settings** section, toggle the **Message Preview** switch to On.

  4. Click the **Set Chat Details** button. The Message Preview feature is enabled and available to agents in all Mobile and Web queues.

**Note:** Message Preview will only be available in chats initiated after this feature was enabled and won't be applied to active chats.



### Agent Experience - Message Preview

In the Agent Adapter, the appearance of a Message Preview is very similar to chat messages that have already been sent, but with a few small differences. To differentiate between a Message Preview and a message that was previously sent by the consumer, the Message Preview is displayed with the following changes while the consumer is typing:

  * The background of the chat bubble is either white or transparent

  * The chat bubble has a dashed-line border

  * The chat font is italicized

  * The chat displays **Message Preview** below the bubble instead of the timestamp


  
---  
![Message Preview bubble](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/16331bc49ebaae.mp4)  
  
Once the consumer sends their message, the Message Preview is updated to display as a typical message with the colored background, standard font, and timestamp. The preview message is only displayed when the web SDK calls the start typing message. The duration of the display of the Message Preview is controlled by the web SDK client sending the stop typing request.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
