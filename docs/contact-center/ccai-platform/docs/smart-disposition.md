---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/smart-disposition/
title: Smart disposition \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:23.904618+00:00
---

# Smart disposition  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/smart-disposition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Smart disposition Stay organized with collections  Save and categorize content based on your preferences. 

Smart disposition is an AI-powered capability that automatically suggests a disposition code during wrap-up that matches the primary reason for the contact. Agents can review the smart disposition suggestion and either accept it or select a different disposition. Smart disposition reduces manual work for agents and improves the consistency of disposition data.

Smart disposition uses the following information when suggesting a disposition:

  * The content of the conversation.

  * The queue the interaction was routed to.

  * The interaction type—for example, call versus chat or inbound versus outbound.




If you turn on smart dispositions, let your agents know what to expect. For more information, see Agent experience.

## Before you begin

To use smart disposition, you need to configure Agent Assist for generative AI session summarization. For more information, see [Agent Assist](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist).

## Turn on smart disposition globally

To turn on smart disposition globally, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Wrap-up** pane, do one of the following:

     * Click the **Automatic wrap-up for inbound calls** toggle to the on position.

     * Click the **Automatic wrap-up for outbound calls** toggle to the on position.

     * Click the **Automatic wrap-up for chats** toggle to the on position.

  3. Click the **Disposition Codes** toggle to the on position.

  4. Click the **Smart Disposition** toggle to the on position, and then click **Save Wrap-Up**.




## Turn on smart disposition at the queue level

Queue level settings override global settings.

To turn on smart disposition at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **IVR (Interactive Voice Response)** , **Mobile** , **Web** or **SMS** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, go to the **Wrap-up settings** section, and then click **Configure**. The **Wrap-up** pane appears.

  5. In the **Wrap-up** pane, do one of the following. The options that appear depend on your channel.

     * Click the **Automatic wrap-up for inbound calls** toggle to the on position.

     * Click the **Automatic wrap-up for outbound calls** toggle to the on position.

     * Click the **Automatic wrap-up for chats** toggle to the on position.

  6. Click the **Disposition Codes** toggle to the on position.

  7. Click the **Smart Disposition** toggle to the on position, and then click **Save**.




## Agent experience

With smart disposition turned on, the **Disposition** field on the **Wrap-up** screen of the agent adapter displays a recommended disposition code during wrap-up. This disposition should match the primary reason for the contact. As an agent, you should evaluate the suggested smart disposition and determine if it's appropriate for the session. If it's not, choose a more appropriate disposition before submitting your wrap-up information.

To use smart disposition during wrap-up, follow these steps:

  1. End a call and enter wrap-up. In the **Wrap-up** screen, the **Disposition** field displays a recommended disposition.

  2. Evaluate the recommended disposition for appropriateness for the session.

  3. Do one of the following:

     * If the recommended disposition is appropriate, complete wrap-up as usual and click **Submit**.

     * If the recommended disposition isn't appropriate, click expand_more, and then select a more appropriate disposition. Continue wrap-up as usual and click **Submit**.




### Always evaluate the disposition field

Depending on circumstances, the **Disposition** field on the **Wrap-up** screen could be any of the following:

  * **Empty** : Smart disposition isn't turned on or isn't able to make a suggestion.

  * **Populated by a default disposition**. Your administrator configured the default disposition.

  * **Populated by a suggested smart disposition**. Your administrator turned on smart disposition and it's working properly.




Evaluate any disposition in the **Disposition** field and either accept it or replace it with a more appropriate disposition. Or, if the **Disposition** field is empty, select an appropriate disposition.

If you notice a pattern of suggested smart dispositions being inappropriate for their sessions, let your administrator know. They might be able to improve the suggestions. Patterns can include the following:

  * The same type of call regularly gets the wrong suggestion.

  * Common call reasons are not reflected well in the suggestions.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
