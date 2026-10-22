---
url: https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook-slot-filling/
title: Webhook for slot filling \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:29.857347+00:00
---

# Webhook for slot filling  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook-slot-filling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Webhook for slot filling Stay organized with collections  Save and categorize content based on your preferences. 

When an intent is matched at runtime, the Dialogflow agent continues collecting information from the end-user until the end-user has provided data for each of the required parameters. This process is called [slot filling](https://docs.cloud.google.com/dialogflow/docs/intents-actions-parameters#required).

By default, Dialogflow does not send a fulfillment webhook request until it has collected all required data from the end-user.

If _webhook for slot filling_ is enabled, Dialogflow sends a fulfillment webhook request for each conversational turn during slot filling.

While in most cases, the parameter prompts are enough to collect all required parameters, a webhook for slot-filling allows you to define more specific agent logic during collection of the parameters. For example, your webhook could handle the customization of follow-up questions or setting parameter slots that cannot be retrieved from the end-user response, like from a database.

## Enable webhook for slot filling

To enable webhook for slot filling at design-time:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Select **Intents** in the left sidebar menu.
  4. Select an intent.
  5. Scroll down to the **Fulfillment** section.
  6. Toggle **Enable webhook call for slot filling** on.
  7. Click **Save**.



## Handle webhook for slot filling calls at runtime

The webhook request message received by your webhook service has a `queryResult.parameters` field. This field contains the current set of parameters provided by the end-user. Values that have not been collected yet are set to empty strings.

An example of the webhook response message for setting parameters can be found in [Webhook Response examples](https://docs.cloud.google.com/dialogflow/docs/fulfillment-webhook#session_entity).

[ Previous arrow_back  Webhook service  ](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook)

[ Next Mutual TLS authentication  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-mtls)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
