---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-events/
title: Virtual agent custom events \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:37.169792+00:00
---

# Virtual agent custom events  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Virtual agent custom events Stay organized with collections  Save and categorize content based on your preferences. 

We have created a Dialogflow CX custom event for Contact Center AI Platform (CCAI Platform) that you can use with your Dialogflow CX agent's [event handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event). This is the `wrapup` custom event.

You can use custom events to handle things that happen outside of the conversation with an end-user. Custom events are identified by name, and you can configured them in your Dialogflow CX virtual agents using event handlers. For more information, see [Custom Events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-custom).

## wrapup

This custom event indicates when an end-user leaves the session for any reason, helping an agent react before the session closes.

For example, if a voice session with a Dialogflow CX virtual agent is dropped due to customer desertion or call failure, CCAI Platform transmits an event to Dialogflow CX. The `wrapup` custom event allows the virtual agent to be configured to react to this event by running through a specific wrap up flow, such as sending specific session data to an external API endpoint.

The `wrapup` custom event only works with [support agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent). It's doesn't work with virtual task assistants.

### Best practices

The following are best practices to consider:

  * If you are using a Dialogflow CX virtual agent integrated with CCAI Platform, you might see errors in your Dialogflow CX application logs if no [event handler](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-custom) is defined for the `wrapup` event. To react to the `wrapup` custom event more broadly than on a specific page in your agent, you can set up a [flow-level event handler](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-flow).

  * When using the [TurnSignals](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#turnsignals) method with Dialogflow CX, there could be issues with syncing the session parameters from the `reached_end_page` conversation turn signal and the transmission of the `wrapup` event by CCAI Platform that follows. To handle this more gracefully, consider using the CCAI Platform custom payload [end conversation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-payload#end_conversation) with your Dialogflow CX agent instead of the End Session transition in your flow. The End Session transition can then be configured on the event handler for `wrapup`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
