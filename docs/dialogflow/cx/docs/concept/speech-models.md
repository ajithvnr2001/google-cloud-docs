---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-models/
title: Speech models \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:50.281279+00:00
---

# Speech models  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-models/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Speech models Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow CX voice agents use [Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs) for speech recognition, which is included in [Dialogflow CX pricing](https://cloud.google.com/dialogflow/pricing). Dialogflow CX automatically selects a speech recognition model for you, but you can optionally specify the model.

## Available models

All available models are listed at [Speech-to-Text models](https://docs.cloud.google.com/speech-to-text/docs/transcription-model). Select a model that is best suited to your domain and [supports your agent language and speech features](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages).

If a model is not explicitly specified, then Dialogflow CX auto-selects a model based on the audio configuration in API requests and agent settings.

The following models typically have the best performance:

  * telephony_short (best for telephony Dialogflow CX)
  * telephony (best for Agent Assist) (also good for telephony Dialogflow CX when [advanced timeout-based end of speech sensitivity](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#advanced-end-of-speech-sensitivity) is enabled) 
  * phone_call (good for Agent Assist and telephony Dialogflow CX)
  * latest_short (best for non-telephony Dialogflow CX)
  * command_and_search (best for languages where other models are not available)



## Specify a model

You can supply the model for an agent, flow, or page with the [model selection setting](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#stt-model-selection). 

You can also supply the model when calling the `Sessions.detectIntent` or `Sessions.streamingDetectIntent` methods; Go to the Session API reference

**Select a protocol and version for the Session reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [Session resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions) |  [Session resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.sessions)  
RPC |  [Session interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Sessions) |  [Session interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.Sessions)  
C++ |  [SessionsClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1SessionsClient.html) |  Not available   
C# |  [SessionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SessionsClient) |  Not available   
Go |  [SessionsClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_SessionsClient) |  Not available   
Java |  [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionsClient) |  [SessionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.SessionsClient)  
Node.js |  [SessionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.SessionsClient.html) |  [SessionsClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.SessionsClient.html)  
PHP |  Not available  |  Not available   
Python |  [SessionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.sessions.SessionsClient) |  [SessionsClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.sessions.SessionsClient)  
Ruby |  Not available  |  Not available   
  
Close

or when configuring the [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2#google.cloud.dialogflow.v2.ConversationProfile) for [Agent Assist](https://docs.cloud.google.com/agent-assist/docs). Specifying the model in a detect intent or conversation profile API call will override any model selections applied to the agent, flow, or page, unless you enable the [**Override request-level speech model**](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#stt-model-selection) setting. **Note:** If you specify the model with a conversation profile, Agent Assist and the associated virtual agent use this model for all speech recognition.

[ Previous arrow_back  Agent settings  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings)

[ Next Voice cloning  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/voice-cloning)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
