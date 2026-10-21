---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/conditional-actions/
title: Conditional actions \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:35.255487+00:00
---

# Conditional actions  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/conditional-actions/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Conditional actions Stay organized with collections  Save and categorize content based on your preferences. 

By default, playbooks use LLMs to control the conversation, take actions, and respond to end-users. If you need more explicit control over the agent's behavior, you can use [flows](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow) or _conditional actions_ , which are described in this guide.

Conditional actions are an optional configuration for playbooks. You can set conversation triggers and conditions that invoke specific actions like responding with a specific message, calling an external tool, invoking another playbook, or performing any other specified action.

## Triggers

You can define triggers that are the first step in determining whether a conditional action is applicable. The following describes trigger types and the specific triggers for each type:

  * **Lifecycle stage**
    * **Playbook start** : Triggered the first time a playbook is started.
    * **Before the LLM decides its next action** : Triggered every time before the LLM predicts the next action.
    * **Before the LLM executes its next action** : Triggered every time before the LLM executes an action.
  * **Event**
    * **Custom event**
    * **No input from user**



## Conditions

Once a trigger occurs, the second step is to evaluate any optionally supplied conditions. Conditions are supplied using the same [condition syntax](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition) used by flow routes.

If no conditions are supplied, the trigger alone will be used to initiate actions.

You can use the following syntax to reference parameters and last/next actions:

  * Session parameters 
    * `$session.params.PARAMETER_NAME`
  * Playbook input parameters 
    * `$playbook.input.INPUT_FIELD_NAME`
  * Last action (previously executed action) 
    * `$last-action.name`
    * `$last-action.input.INPUT_FIELD_NAME`
    * `$last-action.output.OUTPUT_FIELD_NAME`
    * `$last-action.status`
  * Next action (LLM predicted next action) 
    * `$next-action.name`
    * `$next-action.input.INPUT_FIELD_NAME`



You can also use [system functions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions).

Examples:

  * `$session.params.current_user = null`
  * `$last-action.name = "query_order"`
  * `$last-action.name = "query_order" AND $last-action.status != SUCCESS`
  * `$last-action.name = "query_order" AND $last-action.output.orders = null`



## Actions

Once a trigger and optional condition evaluation have occurred, you can configure the following actions to take place:

  * **Provide a response to the end-user** : text, conditional response, custom payload, and pre-recorded audio. When supplying text, you can insert `[pause]`, `[pauseShort]`, or `[pause long]` to inject pauses in agent speech. Sample: `How can I help you today? [pause long] I can help with...`.
  * **Override the next LLM action** : tool use, playbook invocation, playbook completion, flow invocation, playbook transition, flow transition.
  * **Change speech settings** : model name, no speech timeout, endpointer sensitivity, adaptation.
  * **Enable barge-in**
  * **Allow cancellation of partial response playback**
  * **Send Call Companion SMS**
  * **Enable DTMF** : see [DTMF for telephony integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/dtmf)



[ Previous arrow_back  Code blocks  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/code-block)

[ Next Playbook examples  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/example)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
