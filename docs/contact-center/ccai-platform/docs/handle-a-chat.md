---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/handle-a-chat/
title: Handle a chat \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:37:48.026667+00:00
---

# Handle a chat  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/handle-a-chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Handle a chat Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how handle a chat using the agent chat adapter. This includes answering a chat request, managing the conversation, and wrap-up. This page assumes that you are signed into the Contact Center AI Platform (CCAI Platform) portal. For more information, see [Access the CCAI Platform portal](https://docs.cloud.google.com/contact-center/ccai-platform/docs/getting-started-for-agents#access-the-ccaip-portal).

To handle a chat, do the following:

  * Answer a chat request

  * Wrap up




## Answer a chat request

To answer a chat request, follow these steps:

  1. In the CCAI Platform portal, click chat_bubble **Chat icon** to open the agent chat adapter.

  2. In the chat adapter, look for **New Chat** indicators. The indicators pulse to help draw your attention. Each indicator shows: (1) A chat icon, which indicates that this is a chat request, and (2) A number that indicates how many chat messages the end-user has already sent.

  3. Click a **New Chat** indicator. An active chat indicator replaces the **New Chat** indicator and the chat session begins. The active chat indicator includes the following:

     * An icon that indicates the channel that the chat is in. Here are the icons and the channels that they represent:

       * **Computer monitor** : the web channel

       * **Mobile phone** : the mobile channel

       * **WhatsApp logo** : the WhatsApp channel

       * **SMS bubble** : the SMS messaging channel

     * The end-user's phone number or their name. The end-user's name displays only if the following are true:

       * Your organization is using a customer relationship management (CRM) app.

       * The chat is in either the web channel or the mobile channel.

  4. Type a response in the text field, and then click the **Send** button. You can also press the **Enter** key to send a chat message.

  5. Watch for responses from the end-user in the chat pane. Depending on how your administrator has configured CCAI Platform, the chat pane might display one of the following while the end-user is typing:

     * A typing indicator.

     * A typing indicator and a message preview.

  6. Continue corresponding with the end-user. If your administrator has configured target response times, you'll see a target response timer on the active chat indicators. The timer indicates how much time has elapsed since the end-user's last message. In addition, the timer displays one of the following colors to indicate how much of the target response time remains:

     * **Yellow** : more than 45 seconds remain until the target response time expires

     * **Orange** : between 45 and 15 seconds remain until the target response time expires

     * **Red** : less than 15 seconds remain until the target response time expires

If the target response time expires, the active chat adapter continues to display red until you respond. At that time, the response timer resets. For more information, see [Agent chat response time](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-chat-response-time).

  7. When the conversation comes to a close, do one of the following:

     * Let the end-user leave the chat. If the end-user leaves, the chat pane indicates this. Also, the end-user's chat icon appears with a slash through it. Go to the following step and end the chat.

     * If the end-user does not leave the chat and you are sure that the conversation is at a close, go to the following step and end the chat.

  8. To end the chat, do the following:

     * Click the **End chat** button (a chat bubble with an **X** in it). This button is available when the chat overview is not expanded. The **End chat?** dialog appears.

     * Click **End chat**.

  9. Wrap up your chat. For more information, see Wrap up.




## Wrap up

This procedure assumes that you are viewing the **Wrap-up** screen after answering a chat request and ending the chat.

To wrap up after ending a chat, do the following:

  * In the **Wrap up** screen, if you see only the **Submit** button, click **Submit**.

  * In the **Wrap up** screen, if you see the **Disposition** and **Notes** fields, do the following:

    1. Click the **Dispostion** field and choose the applicable disposition code.

    2. Click the **Notes** field and enter any notes that are relevant to the chat conversation. If your administrator turned on session summarization, the **Insert summary** button displays. To insert an auto-generated summary of the conversation, click **Insert summary**.

    3. Click **Submit** , and then click **End wrap-up**.




## What's next

  * [Transfer a chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/transfer-a-chat)

  * [Getting started for agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/getting-started-for-agents)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
