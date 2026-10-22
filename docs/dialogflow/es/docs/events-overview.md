---
url: https://docs.cloud.google.com/dialogflow/es/docs/events-overview/
title: Events \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:27.629921+00:00
---

# Events  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/events-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Events Stay organized with collections  Save and categorize content based on your preferences. 

Intents are normally matched when an end-user expression matches an intent training phrase. However, you can also trigger intents using _events_. Events can be invoked in many ways.

There are two types of events:

  * [**Platform events**](https://docs.cloud.google.com/dialogflow/docs/events-platform): These built-in events are provided by platform [integrations](https://docs.cloud.google.com/dialogflow/docs/integrations). They are invoked when platform-specific events occur. For example, the `FACEBOOK_LOCATION` event is invoked by the Facebook integration when an end-user accepts or rejects a request for the end-user's location.
  * [**Custom events**](https://docs.cloud.google.com/dialogflow/docs/events-custom): These are events that you define. You can invoke these events using either [fulfillment](https://docs.cloud.google.com/dialogflow/docs/fulfillment-overview) or [the API](https://docs.cloud.google.com/dialogflow/docs/api-overview). For example, you might set a timed alert during a conversation, which invokes an event at a certain time. This event could trigger an intent that alerts the end-user about something.



## Configure an intent for events

Events are identified simply by their name. Platform-specific events have specific names, but you can name custom events anything.

To configure an intent so that it is triggered when certain events are invoked:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Select **Intents** in the left sidebar menu.
  4. Select an intent.
  5. Expand the _Events_ section.
  6. Enter one or more event names.



To update intent events with the API, see the [Intents](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#intents) type.

## Event parameters

When invoked, events may also have parameter data that you can access in the triggered intent's responses. For more information, see [Parameter reference for an event parameter](https://docs.cloud.google.com/dialogflow/docs/intents-actions-parameters#event).

[ Previous arrow_back  Manage contexts  ](https://docs.cloud.google.com/dialogflow/es/docs/contexts-manage)

[ Next Platform events  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/events-platform)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
