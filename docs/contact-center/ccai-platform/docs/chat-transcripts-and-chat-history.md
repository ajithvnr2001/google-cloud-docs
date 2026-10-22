---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-transcripts-and-chat-history/
title: Chat transcripts and chat history \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:57.760773+00:00
---

# Chat transcripts and chat history  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-transcripts-and-chat-history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Chat transcripts and chat history Stay organized with collections  Save and categorize content based on your preferences. 

You can configure CCAI Platform to upload a chat transcript to your CRM or external storage after the chat has ended. You can also configure CCAI Platform so that your agents, your end-users, or both, can view chat history during a chat.

## Upload chat transcripts to your CRM

To upload chat transcripts to your CRM, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Chat**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Chat Transcript** pane.

  3. Select one or both of the following checkboxes, depending on your use case:

     * **Post the chat transcript as a comment in the record**.

     * **Add the chat transcript as an attachment to the record**.

  4. Click **Save Chat Transcript**.




## View chat history

You can configure your instance so that your agents, your end-users, or both, can view chat history during a chat.

To view chat history, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Chat**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Chat Transcript** pane.

  3. Click the **Display previous chat interactions** toggle to the on position.

  4. Select one of the following:

     * **To agent and consumer** : chat history appears in the agent adapter for agents. For end-users, chat history appears in the chat widgets for the web SDK and the mobile SDKs.

     * **To agent only** : chat history appears in the agent adapter for agents.

     * **To consumer only** : chat history appears in the chat widgets for the web SDK and the mobile SDKs for end-users.

  5. Click **Save Chat Transcript**.




## About transcripts

This section explains the format of a chat transcript and its location after it's uploaded.

### Transcript format

A chat transcript contains a header and a body separated by a dashed line. The header contains the chat ID and a date stamp with the time zone. The body contains message segments separated by dashed lines. Each message segment contains a timestamp, an indicator saying who sent the message, and a message. Here are some characteristics of a chat transcript:

  * Message segments are in chronological order.

  * Consecutive messages sent by the same participant are grouped in the same message segment.

  * If a participant's full name is available, only the initial of the last name is displayed.

  * If a participant's name isn't available, **Agent** or **End User** is displayed instead.

  * If images or videos were included in the chat, then URLs to those files are included in the chat transcript. These URLs expire seven days after the chat ends.




### Transcript upload locations in a CRM or external storage

After the chat is complete, transcripts are uploaded to the CRM or external storage as a TXT file. Transcripts can be found in the same location that the chat ID and other chat information is stored.

  * **Zendesk** : Added in plain text and, optionally, attached as a file to a private comment in the ticket.
  * **Salesforce** : Added in plain text and, optionally, attached as a file to a private comment in the ticket.
  * **Kustomer** : Added as both a file attachment and as a comment.
  * **MS Dynamics** : Added as an attachment under the timeline for the ticket.
  * **Custom CRM** : Depends on configuration. For a completely custom CRM, the chat transcript is stored in external storage, if configured. For a custom CRM with a generic API, the chat transcript can be added as a file attachment if the _Upload a file_ endpoint is configured, or posted as a comment if the _Comment_ endpoint has been configured. For integrated CRMs, chat transcripts are sent to external storage using SFTP. For more information, see [Set up external storage for CRMs](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-external-storage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
