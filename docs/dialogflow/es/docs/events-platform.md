---
url: https://docs.cloud.google.com/dialogflow/es/docs/events-platform/
title: Platform events \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:13.613665+00:00
---

# Platform events  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/events-platform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Platform events Stay organized with collections  Save and categorize content based on your preferences. 

Platform events are provided by platform [integrations](https://docs.cloud.google.com/dialogflow/docs/integrations). They are invoked when platform-specific events occur. See the documentation for your integration platform for details on platform-specific events.

## Welcome events

Welcome events are invoked when a conversation is started. There are two types of welcome events:

  * **Generic welcome event** : The [default welcome intent](https://docs.cloud.google.com/dialogflow/docs/intents-default#welcome) is automatically created when you create an agent. This intent is preconfigured to handle the generic welcome event: `WELCOME`.
  * **Platform-specific welcome events** : Each platform invokes a platform-specific welcome event when a conversation starts. For example, if an end-user clicks the **Get started** button to start a chat with your Facebook Messenger bot, the [`FACEBOOK_WELCOME` event](https://docs.cloud.google.com/dialogflow/docs/integrations/facebook#events) is invoked.



When a platform-specific welcome event is invoked, Dialogflow triggers any intent that is configured for the event. If no intent is configured for the platform-specific welcome event, Dialogflow invokes the generic welcome event, which triggers the default welcome intent.

## Google Assistant events

Dialogflow events are referred to as "intents" in Google Assistant documentation. For more information and a list of events, see the [reference documentation for Google Assistant intents](https://developers.google.com/assistant/conversational/reference/rest/intents).

[ Previous arrow_back  Events  ](https://docs.cloud.google.com/dialogflow/es/docs/events-overview)

[ Next Custom events  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/events-custom)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
