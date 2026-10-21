---
url: https://docs.cloud.google.com/dialogflow/docs/console/
title: Dialogflow Console overview \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:51.177336+00:00
---

# Dialogflow Console overview  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/docs/console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Dialogflow Console overview Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow provides a web user interface called the _Dialogflow Console_ ([open console](https://dialogflow.cloud.google.com)). You use this console to create, build, and test agents. 

The Dialogflow Console is different from the Google Cloud Platform (GCP) Console ([visit documentation](https://support.google.com/cloud/answer/3465889?hl=en&ref_topic=3340599), [open console](https://console.cloud.google.com/)). The Dialogflow Console is used to manage Dialogflow agents, while the GCP Console is used to manage GCP-specific Dialogflow settings (for example, billing) and other GCP resources. 

In most cases you should use the Dialogflow Console to build agents, but you can also use the Dialogflow API to build agents for advanced scenarios. 

Many quickstart, concept, and how-to guides take you through the steps of using the console. This page provides a high-level summary of the user interface layout and what the console is used for.

## How the console is used

The console is used to create, build, manage, fine-tune, and test your agents. With it, you can:

  * Create [agents](https://docs.cloud.google.com/dialogflow/docs/agents-overview) that define the conversational experience
  * Create [intents](https://docs.cloud.google.com/dialogflow/docs/intents-overview) that map user input to responses
  * Create [entities](https://docs.cloud.google.com/dialogflow/docs/entities-overview) to extract useful data from user input
  * Control conversation paths with [contexts](https://docs.cloud.google.com/dialogflow/docs/contexts-overview)
  * Add [events](https://docs.cloud.google.com/dialogflow/docs/events-overview) that are triggered by occurrences outside of the conversation
  * [Integrate](https://docs.cloud.google.com/dialogflow/docs/integrations) with other conversational platforms
  * Implement [fulfillment](https://docs.cloud.google.com/dialogflow/docs/fulfillment-overview) to connect your service when using integrations
  * [Analyze](https://docs.cloud.google.com/dialogflow/docs/analytics) agent performance
  * Test your agent via the simulator
  * And more ...

**Note:** As an alternative to using the console, you can use the API to build and test agents. You should only do this in advanced scenarios, because it is usually much easier to use the console.

## Sign in to the console

When you sign in to the Dialogflow console, sign in with your Google account used to access GCP services. When you sign in for the first time, you will be prompted with the following:

  1. Allow Dialogflow to access your Google account. Dialogflow uses the following permissions: 
     * **View and manage your data across Google Cloud Platform services** : This permission lets you optionally deploy Cloud Functions for Firebase. See [Fulfillment](https://docs.cloud.google.com/dialogflow/docs/fulfillment-overview) for more information.
     * **View and manage your Google Assistant voice commands, dialog, and grammar** : This permission lets you optionally test your Dialogflow agent on the Google Assistant. See [Google Assistant integration](https://docs.cloud.google.com/dialogflow/docs/integrations/aog) for more information.
     * **View and manage your Actions on Google** : This permission lets you optionally deploy your Dialogflow agent to the Google Assistant and Actions on Google as a conversational action(s).
  2. Accept Dialogflow's terms of service.



## Console interface layout

The console is arranged in three main panels:

![](https://docs.cloud.google.com/static/dialogflow/es/docs/images/console-intent-selected.png)

### Sidebar menu (left)

Only one agent is selected at a time, and you select the agent at the top of the sidebar menu. Once you have selected an agent, you use these menu options to build and manage various elements of the agent. For example, if you click **Intents** , you will see a list of intents for the selected agent in the middle panel.

**Note:** If you're working on a small screen, and the sidebar menu is hidden, click the menu _menu_ button in the upper left corner.

### Main content (middle)

This panel shows data and editing controls for the option selected in the sidebar menu. For example, if you have selected **Intents** , you will see an editable list of intents for the selected agent.

### Dialogflow simulator (right)

You can have a conversation with your agent by speaking or typing messages in the Dialogflow simulator. This is a useful tool to test that your agent behaves as expected. There are examples of using the simulator in many quickstart and how-to guides.

[ Previous arrow_back  Interactions with the API  ](https://docs.cloud.google.com/dialogflow/es/docs/quick/api)

[ Next Agents  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/agents-overview)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
