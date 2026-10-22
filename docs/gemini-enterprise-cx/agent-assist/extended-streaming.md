---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/extended-streaming/
title: Extended streaming \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:57.416858+00:00
---

# Extended streaming  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/extended-streaming/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Extended streaming Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use the extended streaming to stream audio content to Dialogflow and stream human agent suggestions back. You must configure [a Speech-to-Text model](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-supported-languages) that supports [single utterance](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1#google.cloud.speech.v1.StreamingRecognitionConfig.FIELDS.bool.google.cloud.speech.v1.StreamingRecognitionConfig.single_utterance).

Normally, you half-close or tell the Dialogflow API when to end the stream to generate the final transcript and Agent Assist suggestions. This happens at conversation turns, where the API receives the parameter `is_final=true` from the recognition result, `StreamingAnalyzeContentResponse.recognition_result`.

Extended streaming reduces the need for half-closing at conversation turns. It extends the connection timeout to three minutes, during which you can send audio streams without half-closing. The Dialogflow API automatically sends the final transcripts and Agent Assist suggestions back to the stream. You only restart the stream if it times out.

**Note:** Streaming is supported by the RPC API and client libraries only.

## Streaming basics

Agent Assist extended streaming is similar to [audio streaming](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/transcription) for voice transcription. Your system streams audio data to the API, and Dialogflow streams back `StreamingAnalyzeContentResponse` data. The returned data includes suggestions for your human agents.

**Note:** Streaming automatically times out after three minutes. If your conversation lasts longer than three minutes, you can handle the timeout by closing and re-opening the stream.

To use Extended streaming, call the [`streamingAnalyzeContent`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2beta1#google.cloud.dialogflow.v2beta1.Participants.StreamingAnalyzeContent) method.

Extended streaming only supports Agent Assist stage. See [conversation stage](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/basics). Follow these steps to use extended streaming:

  1. Call the `streamingAnalyzeContent` method and set the following fields: 
     * `StreamingAnalyzeContentRequest.audio_config.audio_encoding`: `AUDIO_ENCODING_LINEAR_16` or `AUDIO_ENCODING_MULAW`
     * `enable_extended_streaming`: `true`.
  2. The first `streamingAnalyzeContent` request prepares the stream and sets your audio configuration.
  3. In subsequent requests, you send audio bytes to the stream.
  4. As long as you continue to send audio, you will keep receiving suggestions. You don't need to manually close the stream. It will close automatically once Agent Assist detects that utterances have stopped.
  5. Restart the stream (which includes resending the initial audio configuration) in the following cases: 
     * The stream is broken (the stream stopped when it wasn't supposed to).
     * Your audio data is approaching the automatic timeout at 3 minutes.
     * You received a re-tryable error. You can retry up to three times.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
