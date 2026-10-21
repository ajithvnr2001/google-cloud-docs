---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-profile-flags-chat/
title: User profile tags for chat \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:32.546660+00:00
---

# User profile tags for chat  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-profile-flags-chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  User profile tags for chat Stay organized with collections  Save and categorize content based on your preferences. 

User profile flags appear in the chat adapter during a session. These flags provide information about the end-user, helping you determine how to handle the session. There are flags for **Unverified user** , **Verified user** , **Bad actor** , and **Repeat customer**. These flags appear in the chat adapter on the details page, next to **User profile**. The flags that appear depend on the [reserved data properties](https://docs.cloud.google.com/contact-center/ccai-platform/docs/send-reserved-data-properties) that your organization sends to CCAI Platform during the session. In addition, you can change the verification status of an end-user yourself.

Here are the user profile flags that can appear in the chat adapter:

  * ![Unverified user](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/unverified-user.png) **Unverified user** : indicates that the end-user is not verified as a legitimate customer. This flag appears by default and continues to appear until you or your organization verify the end-user. When the end-user is verified, the ![Unverified user](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/unverified-user.png) **Unverified user** flag is replaced with the ![Verified user](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/verified-user.png) **Verified user** flag.
  * ![Verified user](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/verified-user.png) **Verified user** : indicates that the end-user is verified as a legitimate customer.
  * ![Bad actor](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/bad-actor.png) **Bad actor** : indicates that your organization has determined that the end-user is potentially a bad actor.
  * ![Repeat customer](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/repeat-customer.png) **Repeat customer** : indicates that your organization has determined that the end-user is a repeat customer.



## View the details page of the chat adapter

To view the details page of the chat adapter, do the following:

  1. Answer a chat request. For more information, see [Answer a chat request](https://docs.cloud.google.com/contact-center/ccai-platform/docs/handle-a-chat#answer-a-chat-request).

  2. In the chat adapter, click person **Details**. The **Details** page appears.

  3. Click the chat that you want details for. Information about the chat and the end-user appear, including the following:

     * **SDK custom data** : this displays custom data from the web or mobile SDKs. For more information, see [View session data in the agent adapter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/session-data-agent-adapter).

     * **VA session variables** : this displays virtual agent session variables. If there are multiple virtual agent interactions during the call, each interaction is listed. Clicking an interaction displays the sessions variables for that interaction. For more information, see [View session data in the agent adapter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/session-data-agent-adapter).




## Change the verification status of an end-user

The call adapter indicates the verification status of an end-user by displaying either the ![Unverified user flag.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/unverified-user.png) **Unverified user** flag or the ![Verified
user flag.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/verified-user.png) **Verified user** flag. Your organization can evaluate an end-user's verification status and display the appropriate flag. You can also evaluate an end-user's verification status and then change their status by clicking the verification flag.

To change the verification status of an end-user, follow these steps:

  1. Answer a call. For more information, see [Receive an inbound call](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-agent-guide#receive-inbound-call).
  2. In the call adapter, do one of the following: 
     * To change the status of the end-user to **Verified user** , click the ![Unverified user flag.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/unverified-user.png) **Unverified user** flag. The flag is replaced with the ![Verified user flag.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/verified-user.png) **Verified user** flag.
     * To change the status of the end-user to **Unverified user** , click the ![Verified user flag.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/verified-user.png) **Verified user** flag. The flag is replaced with the ![Unverified user flag.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/unverified-user.png) **Unverified user** flag.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
