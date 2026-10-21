---
url: https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-overview/
title: Fulfillment \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:39.729035+00:00
---

# Fulfillment  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Fulfillment Stay organized with collections  Save and categorize content based on your preferences. 

By default, your agent responds to a matched intent with a static response. If you're using one of the [integration](https://docs.cloud.google.com/dialogflow/docs/integrations) options, you can provide a more dynamic response by using _fulfillment_. When you enable fulfillment for an intent, Dialogflow responds to that intent by calling a service that you define. For example, if an end-user wants to schedule a haircut on Friday, your service can check your database and respond to the end-user with availability information for Friday. 

Each [intent](https://docs.cloud.google.com/dialogflow/docs/intents-overview) has a setting to enable fulfillment. If an intent requires some action by your system or a dynamic response, you should enable fulfillment for the intent. If an intent without fulfillment enabled is matched, Dialogflow uses the static response you defined for the intent. 

When an intent with fulfillment enabled is matched, Dialogflow sends a request to your _webhook_ service with information about the matched intent. Your system can perform any required actions and respond to Dialogflow with information for how to proceed. When fulfillment is enabled, the static response you defined for the intent is only used if your [webhook service fails](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook#errors). The following diagram shows the processing flow for fulfillment. 

![Diagram showing flow for fulfillment](https://docs.cloud.google.com/static/dialogflow/es/docs/images/fulfillment-flow.svg)

  1. The end-user types or speaks an expression.
  2. Dialogflow matches the end-user expression to an intent and extracts parameters.
  3. Dialogflow sends a [webhook request](https://docs.cloud.google.com/dialogflow/docs/fulfillment-webhook#webhook_request) message to your webhook service. This message contains information about the matched intent, the action, the parameters, and the response defined for the intent. 
  4. Your service performs actions as needed, like database queries or external API calls.
  5. Your service sends a [webhook response](https://docs.cloud.google.com/dialogflow/docs/fulfillment-webhook#webhook_response) message to Dialogflow. This message contains the response that should be sent to the end-user. 
  6. Dialogflow sends the response to the end-user.
  7. The end-user sees or hears the response.



[ Previous arrow_back  Custom events  ](https://docs.cloud.google.com/dialogflow/es/docs/events-custom)

[ Next Inline editor  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-inline-editor)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
