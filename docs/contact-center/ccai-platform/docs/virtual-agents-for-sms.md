---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agents-for-sms/
title: Virtual agents for SMS \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:19.974129+00:00
---

# Virtual agents for SMS  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agents-for-sms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Virtual agents for SMS Stay organized with collections  Save and categorize content based on your preferences. 

You can create virtual agents for the SMS channel, letting end-users perform self-service tasks with no human agent intervention. You can assign virtual agents to SMS queues in the same way you would assign human agents.

While the SMS channel supports Multimedia Messaging Service (MMS), MMS isn't supported in chat sessions with SMS virtual agents.

## Before you begin

Before creating an SMS virtual agent, create a Dialogflow agent and integrate it with Contact Center AI Platform (CCAI Platform). For more information, see [Create and integrate Dialogflow agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-a-dialogflow-agent).

## Create an SMS virtual agent

To create an SMS virtual agent, follow these steps:

  1. Follow the instructions in [Create virtual agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-virtual-agents).

  2. In the **Add a Customer Support Agent** dialog, for **Support area selection** , make the following selections:

     * For **Channel** , select **Chat**.

     * For **Menu** , select the **SMS** checkbox.

     * For **Language** , select the **English (US)** checkbox. English is the only language available for SMS virtual agents.




## Assign an SMS virtual agent to a queue

To assign an SMS virtual agent to a queue, follow these steps:

  1. Follow the instructions in [Assign a chat virtual agent to a queue](https://docs.cloud.google.com/contact-center/ccai-platform/docs/assign-virtual-agents-to-queues#assign-chat-va-to-queue).

  2. For step 2, in the **SMS Messaging** pane, click **Edit / View**.




## Custom payloads

Virtual agents for SMS can use the same [custom payloads](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-payload) as virtual agents for web chat and mobile chat. However, the SMS end-user experience differs from the web chat and mobile chat experiences in some cases.

### End-user experience

The [inline button](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-payload#inline-button) is an example of a custom payload where the SMS end-user experience differs from the web chat and mobile chat experiences. The inline button payload for an SMS virtual agent renders as a numbered text menu. This lets the end-user choose an option by typing either the response number or the response itself.

The following is an example of an end-user's conversation with an SMS virtual agent. The conversation is formatted differently on the end-user's mobile phone.

  * **SMS virtual agent** : Hi. This is a virtual agent. How can I help you today?

  * **End-user** : I need help with my order

  * **SMS virtual agent** : Sure. I can help with that. Please select an option:

    1. Get Order Status

    2. Cancel Existing Order

    3. Change Order Information

    4. Reorder past purchases

  * **End-user** : 2

  * **SMS virtual agent** : You have selected to cancel order. Please provide your order ID.

  * **End-user** : 08978675

  * **SMS virtual agent** : This is an order for: Portable Monitor m253647. Are you sure you want to cancel this order?

    1. Yes

    2. No

  * **End-user** : Yes

  * **SMS virtual agent** : Your order: 08978675 for Portable Monitor m253647 is now canceled.




## After hours deflections

You can configure to your instance to deflect after hours escalation attempts by SMS virtual agents or end-users. After an after-hours escalation attempt, the system sends a message to the end-user containing your SMS after hours message along with options for continuing or ending the chat session. For more information, see [Hours of operation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hours-of-operation).

### Configure after hours deflections

You configure after hours deflections by setting up an after hours message.

To configure after hours deflections, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **SMS Messaging** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. For **SMS Chat System Message** , select the **Enable after hour messages** checkbox.

  5. In the **Write a message to be sent for after hours** field, enter your after hours message.

  6. Click **Save**.




### End-user experience

The following table shows the interaction between an SMS virtual agent and an end-user after one of them attempts an after-hours escalation. 

Action | Result  
---|---  
An SMS virtual agent or end-user attempts to escalate a chat session to a human agent after hours. |  The system sends a message to the end-user that contains the following:

  * Your SMS after hours message
  * A numbered text menu for the end-user to select from: 
    1. Continue with VA support
    2. Continue waiting for human agent
    3. End chat

  
The end-user selects option 1 by texting `1`. | 

  * The session with the virtual agent resumes.
  * The virtual agent doesn't respond. Instead, it waits for another message from the end-user before responding.

  
The end-user selects option 2 by texting `2`. | 

  * The virtual agent leaves the session without responding.
  * The session is moved to a queue with a human agent and continues until a human agent joins the session.

  
The end-user selects option 3 by texting `3`. | 

  * The session with the virtual agent ends without a response from the virtual agent.

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
