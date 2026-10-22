---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/resume-a-chat/
title: Resume a chat \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:53.141184+00:00
---

# Resume a chat  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/resume-a-chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Resume a chat Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use the resume chat endpoint to resume chat sessions that are in `dismissed` or `va_dismissed` status. You can use this endpoint to reconnect an end-user to an agent after a period of inactivity, displaying the chat history to both the end-user and the agent.

## Resume a dismissed chat

To resume a dismissed chat, send a `PATCH` request with an empty request body to the following endpoint. Authenticate with [basic authentication](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api#basic_authentication). For more information, see [Dismiss Inactive Chats](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dismiss-inactive-chats).
    
    
    https://YOUR_CCAAS_HOST/apps/api/v1/chats/CHAT_ID/resume
    

Replace the following:

  * `YOUR_CCAAS_HOST`: your Google Cloud Contact Center as a Service (Google Cloud CCaaS) host

  * `CHAT_ID`: the ID of the chat to resume




If you try to resume a chat that isn't in `dismissed` or `va_dismissed` status, the request returns this message: `This chat is not in dismissed state`. The chat isn't resumed.

If you try to resume a chat outside of operating hours, the request returns the after-hours message. The chat isn't resumed.

For more information, see [Resume chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-platform-api-endpoints#resume-chat).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
