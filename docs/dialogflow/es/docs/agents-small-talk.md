---
url: https://docs.cloud.google.com/dialogflow/es/docs/agents-small-talk/
title: Small talk \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:36.620445+00:00
---

# Small talk  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/agents-small-talk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Small talk Stay organized with collections  Save and categorize content based on your preferences. 

Small talk is used to provide responses to casual conversation. This feature can greatly improve the end-user experience by answering common questions outside the scope of your agent.

Small talk is available in two ways:

  * **Built-in small talk** : When enabled for an agent, it handles casual conversation automatically, without adding intents to your agent.
  * **Prebuilt small talk** : When the [prebuilt small talk agent](https://docs.cloud.google.com/dialogflow/docs/agents-prebuilt) is imported, it provides intents to handle casual conversation.



## Built-in small talk

### Enable built-in small talk for an agent

To enable built-in small talk for your agent:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Click **Small talk** in the left sidebar menu.
  3. Toggle **Enable** on.
  4. Click **Save**.



### Customize built-in small talk responses

Once enabled, built-in small talk responses can be customized to fit your branding or product needs. Each response category is organized in folders. To customize responses:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Click **Small talk** in the left sidebar menu.
  3. Click a response category folder.
  4. Add new or edit existing responses.
  5. Click **Save**.



### Built-in small talk limitations

The following limitations apply to the built-in small talk:

  * Only supported for [some languages](https://docs.cloud.google.com/dialogflow/docs/reference/language).
  * Only available for the `global` [region](https://docs.cloud.google.com/dialogflow/es/docs/how/region).
  * Does not work for [mega agents](https://docs.cloud.google.com/dialogflow/docs/agents-mega).
  * Based on [Google Assistant policy](https://developers.google.com/assistant/console/policies/general-policies#user_experience), enabling built-in small talk in its entirety will cause your action to be rejected. You can import the prebuilt small talk agent and update or delete intents that do not comply with policy.



## Prebuilt small talk

### Import prebuilt small talk agent

To import the prebuilt small talk agent to your project:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Click **Prebuilt agents** in the left sidebar menu.
  3. Hover the mouse over the **Small Talk** prebuilt agent.
  4. Click **Import**.
  5. Either create a new GCP project or choose an existing one.
  6. Click **OK**.



### Customize prebuilt small talk responses

To customize the [prebuilt](https://docs.cloud.google.com/dialogflow/docs/agents-prebuilt) small talk agent, edit the imported intents as you normally would.

[ Previous arrow_back  Mega agents  ](https://docs.cloud.google.com/dialogflow/es/docs/agents-mega)

[ Next Agent settings  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
