---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-testing/
title: Test chat integration \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:47.860512+00:00
---

# Test chat integration  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-testing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Test chat integration Stay organized with collections  Save and categorize content based on your preferences. 

Genesys Cloud provides a testing tool for users to test their integration which is available through [the developer center](https://developer.genesys.cloud/devapps). A customer service conversation consists of two participants: The customer and the agent. To complete the test, enable the developer tool to participate as a customer, and in a Genesys Cloud instance you participate as an agent. The first step explains how to enable and login to the developer tool. The second steps explains how to answer the chat from a Genesys Cloud instance and enabling the Google Agent Assist interaction widget.

## Step 1: Set up the developer tool

The following walkthrough explains how to use the developer tool for testing.

  1. Navigate to the [Web chat and messaging tool](https://developer.genesys.cloud/devapps/web-chat-messenger).
  2. Select **Account Selection**.
  3. Click **Add Account**.
  4. Pick the region where your Genesys Cloud is serviced from, for example USE1. This will associate your account with the tool so you can test all the configurations.
  5. Choose whether to test web Messenger or web chat V2: 
     * For Messenger, select the chat configuration you deployed.
     * For chat V2, select the chat configuration you deployed, specify the queue for the message, then click **Populate Fields** in the **Chat Data** section.
  6. Click **Start Chat**.



## Step 2: Test from your Genesys Cloud instance

The following walkthrough explains how to test use a Genesys Cloud instance to test your Web Messenger or chat V2 integration.

  1. Sign in to your Genesys Cloud instance.
  2. Select **Collaborate/Communicate**.
  3. Toggle **On Queue** toggle_on.
  4. Click the **Interaction widget** record_voice_over.
  5. Whether you want to test Messenger or chat V2, click **Start chat**.
  6. When the chat starts, go back to your Genesys Cloud instance.
  7. Navigate to the **Conversations** panel.
  8. Click **Answer**.
  9. Click the integration widget top bar.
  10. Click the Agent Assist integration widget.



Now, the integration widget is listening to the conversation between the agent and customer. For example, the demo conversation profile has the conversation summary and smart reply features configured. When the customer asks for order status, both agent coaching and smart reply provide instructions automatically for the customer. 

If the agent clicks **Generate Summary** , the widget generates the conversation summary.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
