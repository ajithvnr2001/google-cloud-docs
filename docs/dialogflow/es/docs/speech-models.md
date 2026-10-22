---
url: https://docs.cloud.google.com/dialogflow/es/docs/speech-models/
title: Speech models \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:09.615624+00:00
---

# Speech models  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/speech-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Speech models Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow CX voice agents use [Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs) for speech recognition, which is included in [Dialogflow CX pricing](https://cloud.google.com/dialogflow/pricing). Dialogflow CX automatically selects a speech recognition model for you, but you can optionally specify the model.

## Available models

All available models are listed at [Speech-to-Text models](https://docs.cloud.google.com/speech-to-text/docs/transcription-model). Select a model that is best suited to your domain and [supports your agent language and speech features](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages).

If a model is not explicitly specified, then Dialogflow CX auto-selects a model based on the audio configuration in API requests and agent settings.

If [enhanced speech model](https://docs.cloud.google.com/dialogflow/es/docs/speech-enhanced-models) is enabled for the agent and an enhanced version of the specified model for the language does not exist, then the speech is recognized using the standard version of the specified model. 

The following models typically have the best performance:

  * telephony_short (best for telephony Dialogflow CX)
  * telephony (best for Agent Assist) 
  * phone_call (good for Agent Assist and telephony Dialogflow CX)
  * latest_short (best for non-telephony Dialogflow CX)
  * command_and_search (best for languages where other models are not available)



## Specify a model

You can supply the model when calling the `detectIntent` or `streamingDetectIntent` methods on the [`Sessions`](https://docs.cloud.google.com/dialogflow/es/docs/reference/common-types#sessions) type; or when configuring the [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2#google.cloud.dialogflow.v2.ConversationProfile) for [Agent Assist](https://docs.cloud.google.com/agent-assist/docs). **Note:** If you specify the model with a conversation profile, Agent Assist and the associated virtual agent use this model for all speech recognition.

[ Previous arrow_back  Mutual TLS authentication  ](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-mtls)

[ Next Speech adaptation  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/speech-adaptation)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
