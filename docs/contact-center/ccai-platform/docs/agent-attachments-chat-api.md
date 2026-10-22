---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-attachments-chat-api/
title: Agent file attachments with the chat platform API \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:11.494303+00:00
---

# Agent file attachments with the chat platform API  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-attachments-chat-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Agent file attachments with the chat platform API Stay organized with collections  Save and categorize content based on your preferences. 

With a chat platform API custom app, you can set up a workflow that lets your agents attach files during a chat session.

## Agent file attachment workflow

Here's the workflow for an agent attaching a file during a chat session.

  1. An agent attaches a file during a chat session.
  2. Your webhook endpoint receives a `message_received` event, which includes the `media_id` value for the attached file. For more information, see [Webhooks for the chat API platform](https://docs.cloud.google.com/contact-center/ccai-platform/docs/webhooks).
  3. Send a `GET` request to the following endpoint to get the attachment file, specifying the `media_id` value from the previous step. Authenticate using [basic authentication](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api#basic_authentication).
         
         https://YOUR_CCAAS_HOST/apps/api/v1/chats/CHAT_ID/media?media_id=MEDIA_ID&media_type=MEDIA_TYPE
         

Replace the following:

     * `YOUR_CCAAS_HOST`: your Contact Center AI Platform (CCAI Platform) host

     * `CHAT_ID`: the chat ID

     * `MEDIA_ID`: the ID of the file that you want to download. Get this from the `message_received` webhook event.

     * `MEDIA_TYPE`: the type of the file that you want to download. One of `photo`, `video`, `audio`, or `document`.

A successful request returns the attachment file. For more information, see [Chat platform API Guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-platform-api-guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
