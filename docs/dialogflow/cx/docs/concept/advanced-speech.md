---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/advanced-speech/
title: Advanced speech settings \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:57.970440+00:00
---

# Advanced speech settings  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/advanced-speech/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Advanced speech settings Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Advanced speech settings are only supported by [telephony integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration).

This guide provides additional, advanced settings for speech features. You can toggle these advanced settings off and on by navigating to **Agent settings > Speech and IVR > Speech-to-Text > Advanced speech settings**.

These settings are available in agent settings (applies to entire agent), [flow settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#settings) (applies to entire flow and overrides agent settings), [page settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page#settings) (applies to page and overrides flow and agent settings), and [fulfillment settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#settings) (applies to fulfillment and overrides page, flow, and agent settings). A subset of these settings are available at each level, depending on the setting relevance for the level. *Before you can configure these settings at any lower level, you must first check the **Enable advanced speech settings** box at the agent level (Agent settings > Speech and IVR > Speech-to-Text > Advanced speech settings)*.

Updated agent-level settings don't propagate to the flow, page, and fulfillment level when the **Customize** option is selected on these lower levels. If the **Customize** option emcompasses multiple settings and you want to update only some of them, you might also need to update other settings if you want them to be the same as the agent-level settings.

## Settings availability by level

The following table indicates which advanced speech settings are available at each level:

Setting name | Agent | Flow | Page | Fulfillment  
---|---|---|---|---  
Model selection (Speech-to-Text) | ✔ | ✔ | ✔ |   
End of speech sensitivity | ✔ | ✔ | ✔ |   
Advanced timeout-based end of speech sensitivity | ✔ | ✔ | ✔ |   
Enable smart endpointing | ✔ |  |  |   
No speech timeout | ✔ | ✔ | ✔ |   
Barge-in | ✔ | ✔ |  | ✔  
Allow cancellation of partial response playback |  |  |  | ✔  
Audio export bucket | ✔ | ✔ |  |   
DTMF | ✔ | ✔ | ✔ |   
  
## Model selection (Speech-to-Text)

Can be set at the agent, flow, and page levels.

Sets the speech model used for speech recognition. This setting is language-specific, so you can select different models for different languages. You can also check **Override request-level speech model** , which will cause the selected model to be used even if a runtime API call specifies a different model.

For Dialogflow CX Phone Gateway, see [limitations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/phone-gateway#limits). For more information, see [Speech models](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-models).

## End of speech sensitivity

Can be set at the agent, flow, and page levels.

Controls the sensitivity for recognizing the end of speech in end-user audio input. The value ranges from 0 (low sensitivity, less likely to end speech) to 100 (high sensitivity, more likely to end speech).

**Note:** This setting only supports the `phone_call` speech model for the `en-US` [language](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language) tag unless you check the **Enable advanced timeout-based end of speech sensitivity** setting.

## Advanced timeout-based end of speech sensitivity

Can be set at the agent level and disabled at the flow and page levels.

If this setting is enabled, the [**End of speech sensitivity**](https://docs.cloud.google.com/dialogflow/cx/docs/concept/advanced-speech#end-of-speech-sensitivity) setting value is used as a gauge to establish a relative audio silence time-out to determine the end of speech. If this setting is disabled (the default), the **End of speech sensitivity** setting value is used to determine the end of speech by the ML model provided by Google Cloud Speech-to-Text.

While the **End of speech sensitivity** setting supports only the `phone_call` speech model for the `en-US` [language](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language) tag by default, the **Enable advanced timeout-based end of speech sensitivity** setting allows for configuring end of speech sensitivity for all languages and speech models supported by Dialogflow.

## Enable smart endpointing

Can be set at the agent level only.

If this setting is enabled, Dialogflow CX will analyze partial user input to determine the end of speech. For example, if the user says "I would like to" and pauses, Dialogflow CX will wait for the user to continue the sentence.

This is particularly useful for numeric parameter collection, where the user might say "1234" and pause before saying "5678". In order to apply this setting for a specific parameter, you have to set up [Smart endpointing](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#smart-endpointing) in the parameter's form.

This setting is available for the `en-US` language tag only and is disabled by default.

## No speech timeout

Can be set at the agent, flow, and page levels.

The time duration in seconds for which Dialogflow CX will stop waiting for end-user audio input. The default is 5 seconds, and the maximum value is 60 seconds. For this timeout, Dialogflow CX invokes a [no-input event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in).

## Barge-in

Can be set at the agent, flow, and fulfillment levels.

When enabled, an end-user can interrupt Dialogflow CX response audio. When interrupted, Dialogflow CX will stop sending audio, and it will process the next end-user input.

If there are multiple messages in the [message queue](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#queue), and a message was queued by a fulfillment associated with a page, flow, or agent that has barge-in enabled, then all following messages in the queue will also have barge-in enabled. In this case, the integration will stop playing audio for all of the queued messages with barge-in enabled.

**Note:** Enabling barge-in increases the total billable duration for each turn. Because the agent is actively listening for an interruption while it's speaking, you're billed for both **Input Seconds** and **Output Seconds** simultaneously during the response playback, even if the user remains silent.

## Allow cancellation of partial response playback

Can be set at the fulfillment level only.

You can enable this setting when the **Enable advanced speech settings** box is checked in **Agent settings > Speech and IVR** and [partial response](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#partial-response) is enabled at the fulfillment level. This setting allows cancellation of a partial response playback.

If a message in the [message queue](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#queue) is created by a fulfillment that allows cancellation, playback of the message is cancelled if another message is added to the queue. This is useful when you want an initial message to start playback, but for that playback to be cancelled if a working webhook produces another message before playback of the initial message completes.

## Audio export bucket

Can be set at the agent and flow levels.

If supplied, any audio data associated with a request will be saved to the Cloud Storage bucket:

Audio Saved | Applicable requests  
---|---  
End-user audio input | DetectIntent, StreamingDetectIntent, AnalyzeContent, StreamingAnalyzeContent  
Text-to-Speech (TTS) audio synthesized for a response | AnalyzeContent, StreamingAnalyzeContent  
  
Grant the **Storage Object Creator** role to the following service accounts in your project:

  * To the service account of the format `one-click@df-cx-ALPHANUMERIC_VALUE-ALPHANUMERIC_VALUE.iam.gserviceaccount.com` if you use a [partner built-in telephony integration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration#telephony-partner-built-in).

  * To the service account of the format `service-PROJECT_NUMBER@gcp-sa-dialogflow.iam.gserviceaccount.com` if you use the [Dialogflow CX Phone Gateway](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/phone-gateway) integration. To find this service account in IAM, check the **Include Google-provided role grants** option.




## DTMF

See the [DTMF (Dual-tone multi-frequency signaling) documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/dtmf) for more information about this feature.

[ Previous arrow_back  Speech adaptation  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-adaptation)

[ Next Speech model migration Q1 2024  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
