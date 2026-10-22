---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/session-data-agent-adapter/
title: Display session data in the agent adapter \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:24.081639+00:00
---

# Display session data in the agent adapter  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/session-data-agent-adapter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Display session data in the agent adapter Stay organized with collections  Save and categorize content based on your preferences. 

You can configure CCAI Platform to display session data in the agent adapter. This includes virtual agent session variables and custom data from the web and mobile SDKs. This information can be useful for an agent to get additional information during a session, or for a supervisor to get an overview of a session that they [barge](https://docs.cloud.google.com/contact-center/ccai-platform/docs/barge) into.

## Display virtual agent session variables

You can configure CCAI Platform to display [virtual agent session variables](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-payload#session-variables-custom-payload) in the agent adapter. This gives an agent or supervisor an overview of previous interactions that the end-user had with the virtual agent.

For session variables that contain custom payloads, you can use the following properties:

  * `invisible_to_agent`: Use this to specify payload properties that you don't want to be displayed in the agent adapter or sent to your CRM. For more information, see [Capture from intent response](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-payload#capture_from_intent_response).

  * `display_order_in_adapter`: Specifies the order that session variables should appear in the agent adapter and in CRM records. If you don't include this property with your custom payload, session variables appear in the agent adapter and in CRM records in random order. The `display_order_in_adapter` property doesn't affect properties that are specified as `invisible_to_agent`. For more information, see [Custom Session variables for custom payload handling](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-payload#session-variables-custom-payload).




### Display virtual agent session variables in the chat adapter

To display virtual agent session variables in the chat adapter, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Virtual Agent** pane.

  3. Do one or both of the following, depending on your use case:

     * To display chat session variables from customer support virtual agents, do the following:

       1. Go to **Customer support agents**.

       2. For **Chats** , select the **Collect configured custom data in chat sessions and send it to CRM** checkbox.

       3. Select the **Display collected custom data in Agent Adapter** checkbox.

     * To display chat session variables from virtual task assistants, do the following:

       1. Go to **Task assistants**.

       2. For **Chats** , select the **Collect configured custom data in chat sessions and send it to CRM** checkbox.

       3. Select the **Display collected custom data in Agent Adapter** checkbox.

  4. Click **Save Changes**




### Display virtual agent session variables in the call adapter

To display virtual agent session variables in the call adapter, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Virtual Agent** pane.

  3. Do one or both of the following, depending on your use case:

     * To display call session variables from customer support virtual agents, do the following:

       1. Go to **Customer support agents**.

       2. For **Calls** , select the **Collect configured custom data in call sessions and sent it to CRM** checkbox.

       3. Select the **Display collected custom data in Agent Adapter** checkbox.

     * To display call session variables from virtual task assistants, do the following:

       1. Go to **Task assistants**.

       2. For **Calls** , select the **Collect configured custom data in call sessions and send it to CRM** checkbox.

       3. Select the **Display collected custom data in Agent Adapter** checkbox.

  4. Click **Save Changes**




## Display SDK custom data

You can configure CCAI Platform to display SDK custom data in the agent adapter. This custom data can come from the [web SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk#chat-unsigned-custom-data), the [Android SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide#send-custom-data-to-your-crm) or the [iOS SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide#send-custom-data-to-your-crm). This gives the user quick access to the SDK custom data for that session.

You can use the `invisible_to_agent` property to specify custom properties that you don't want to be displayed in the agent adapter. For more information, see the "Prevent the display of custom data" section of the [web SDK guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk#prevent-the-display-of-custom-data), the [Android SDK guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide#prevent-the-display-of-custom-data), and the [iOS SDK guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide#prevent-the-display-of-custom-data).

To let users view SDK custom data, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Data Parameters** pane.

  3. Under **Display SDK custom data in Agent Adapter** , select the type of SDK custom data that you want to be displayed in the agent adapter, and then click **Save Data Parameters**.




## What's next

  * [Send SDK custom data](https://docs.cloud.google.com/contact-center/ccai-platform/docs/send-sdk-custom-data)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
