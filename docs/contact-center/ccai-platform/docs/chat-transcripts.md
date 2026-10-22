---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-transcripts/
title: View previous chats and download chat transcripts \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:47.495938+00:00
---

# View previous chats and download chat transcripts  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-transcripts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  View previous chats and download chat transcripts Stay organized with collections  Save and categorize content based on your preferences. 

This section explains how agents and end-users can view previous chats. It also explains how end-users can download chat transcripts.

## View previous chats in the agent adapter, web SDK, and mobile SDKs

If your administrator has configured it, agents and end-users can see previous chat interactions during a chat. Agents see previous chats in the chat adapter, and end-users see them in the web SDK and mobile SDK widgets. For more information, see [Enable the display of previous chat interactions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-external-storage#enable-display-of-previous-chat-interactions).

#### Chat history in the chat adapter

The following is an example of chat history in the chat adapter:

![The chat history in the chat adapter.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/chat-history-chat-adapter.png)

#### Chat history in the web SDK

The following is an example of chat history in the web SDK widget:

![The chat history in the web SDK.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/chat-history-web-sdk.png)

#### Chat history in the mobile SDKs

The following is an example of chat history in a mobile SDK widget:

![The chat history in the mobile SDK.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/chat-history-mobile-sdk.png)

## Download chat transcripts using the web SDK and mobile SDKs

If your administrator [configures](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-external-storage#configure-how-chat-transcripts-are-added) it, an end-user can download a chat transcript using the web SDK or the mobile SDKs. They can do this during a chat session or after a chat session has ended. The option to download a chat transcript is available only after the agent and the end-user have both sent at least one message.

### Download a transcript during a chat session

To download a transcript during a chat session, the end-user does the following:

  1. In the chat pane, the end-user clicks more_horiz **More** , and then clicks **Download transcript**.

![The Download transcript option in the chat pane.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/three-ellipsis.png)

  2. The end-user chooses a download location on their device.




When an end-user downloads a chat transcript during an active chat session, the transcript includes the messages that were exchanged up until the time that it was downloaded. To get a transcript of the entire session, the end-user must wait until the session is completed to download the transcript.

### Download a transcript after a chat session is completed

If CSAT is enabled, a CSAT rating dialog appears at the end of a chat. The end-user can download a chat transcript from the **Thank you** dialog that follows the CSAT rating dialog. If CSAT isn't enabled, the end-user can download a chat transcript from the chat pane.

#### Download a transcript when CSAT is enabled

To download a transcript when CSAT is enabled, the end-user does the following:

  1. In the CSAT rating dialog that appears when a chat session is completed, the end-user provides a CSAT rating. A **Thank you!** dialog appears.

  2. In the **Thank you!** dialog, the end-user clicks **Download Transcript**.

![The CSAT Thank you! dialog.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/csat-score.png)

  3. The end-user chooses a download location on their device.




#### Download a transcript when CSAT isn't enabled

To download a transcript when CSAT isn't enabled, the end-user does the following:

  1. In the chat pane, when the chat is completed, the end-user clicks **Download transcript**.

![The chat pane when the chat is completed.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/chat-ended-transcript.png)

  2. The end-user chooses a download location on their device.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
