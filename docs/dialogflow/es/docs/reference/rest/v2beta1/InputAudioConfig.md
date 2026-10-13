---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/InputAudioConfig/
title: InputAudioConfig \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:47:34.551900+00:00
---

# InputAudioConfig  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/InputAudioConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  InputAudioConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SpeechContext
    * JSON representation
  * BargeInConfig
    * JSON representation



Instructs the speech recognizer on how to process the audio content.

JSON representation  
---  
      
    
    {
      "audioEncoding": enum ([AudioEncoding](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles#ConversationProfile.AudioEncoding)),
      "sampleRateHertz": integer,
      "languageCode": string,
      "enableWordInfo": boolean,
      "phraseHints": [
        string
      ],
      "speechContexts": [
        {
          object ([SpeechContext](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/InputAudioConfig#SpeechContext))
        }
      ],
      "model": string,
      "modelVariant": enum ([SpeechModelVariant](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles#ConversationProfile.SpeechModelVariant)),
      "singleUtterance": boolean,
      "enableVoiceActivityEvents": boolean,
      "disableNoSpeechRecognizedEvent": boolean,
      "bargeInConfig": {
        object ([BargeInConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/InputAudioConfig#BargeInConfig))
      },
      "enableAutomaticPunctuation": boolean,
      "defaultNoSpeechTimeout": string,
      "phraseSets": [
        string
      ],
      "optOutConformerModelMigration": boolean,
      "geminiAsrConfig": {
        object ([GeminiAsrConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles#ConversationProfile.GeminiAsrConfig))
      },
      "useGeminiAsr": boolean
    }  
  
Fields  
---  
`audioEncoding` |  `enum (`[AudioEncoding](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles#ConversationProfile.AudioEncoding)`)` Required. Audio encoding of the audio content to process.  
`sampleRateHertz` |  `integer` Required. Sample rate (in Hertz) of the audio content sent in the query. Refer to [Cloud Speech API documentation](https://cloud.google.com/speech-to-text/docs/basics) for more details.  
`languageCode` |  `string` Required. The language of the supplied audio. Dialogflow does not do translations. See [Language Support](https://cloud.google.com/dialogflow/docs/reference/language) for a list of the currently supported language codes. Note that queries in the same session do not necessarily need to specify the same language. If not set, the language is inferred from the `[ConversationProfile.stt_config](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles#ConversationProfile.FIELDS.stt_config)`.  
`enableWordInfo` |  `boolean` If `true`, Dialogflow returns `[SpeechWordInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/ConversationEvent#SpeechWordInfo)` in `[StreamingRecognitionResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/ConversationEvent#StreamingRecognitionResult)` with information about the recognized speech words, e.g. start and end time offsets. If false or unspecified, Speech doesn't return any word-level information.  
`phraseHints[]  
**(deprecated)**` |  `string` This item is deprecated!A list of strings containing words and phrases that the speech recognizer should recognize with higher likelihood.See [the Cloud Speech documentation](https://cloud.google.com/speech-to-text/docs/basics#phrase-hints) for more details.This field is deprecated. Please use [`speechContexts`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/InputAudioConfig/) instead. If you specify both [`phraseHints`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/InputAudioConfig/) and [`speechContexts`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/InputAudioConfig/), Dialogflow will treat the [`phraseHints`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/InputAudioConfig/) as a single additional [`SpeechContext`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/InputAudioConfig/).  
`speechContexts[]` |  `object (`[SpeechContext](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/InputAudioConfig#SpeechContext)`)` Context information to assist speech recognition.See [the Cloud Speech documentation](https://cloud.google.com/speech-to-text/docs/basics#phrase-hints) for more details.  
`model` |  `string` Optional. Which Speech model to select for the given request. For more information, see [Speech models](https://cloud.google.com/dialogflow/es/docs/speech-models).  
`modelVariant` |  `enum (`[SpeechModelVariant](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles#ConversationProfile.SpeechModelVariant)`)` Which variant of the `[Speech model](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/InputAudioConfig#FIELDS.model)` to use.  
`singleUtterance` |  `boolean` If `false` (default), recognition does not cease until the client closes the stream. If `true`, the recognizer will detect a single spoken utterance in input audio. Recognition ceases when it detects the audio's voice has stopped or paused. In this case, once a detected intent is received, the client should close the stream and start a new request with a new stream as needed. Note: This setting is relevant only for streaming methods. Note: When specified, InputAudioConfig.single_utterance takes precedence over StreamingDetectIntentRequest.single_utterance.  
`enableVoiceActivityEvents` |  `boolean` Optional. If `true`, responses with voice activity speech events will be returned as they are detected. Note: This setting is relevant only for streaming methods.  
`disableNoSpeechRecognizedEvent` |  `boolean` Only used in `[Participants.AnalyzeContent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants/analyzeContent#google.cloud.dialogflow.v2beta1.Participants.AnalyzeContent)` and `Participants.StreamingAnalyzeContent`. If `false` and recognition doesn't return any result, trigger `NO_SPEECH_RECOGNIZED` event to Dialogflow agent.  
`bargeInConfig` |  `object (`[BargeInConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/InputAudioConfig#BargeInConfig)`)` Configuration of barge-in behavior during the streaming of input audio.  
`enableAutomaticPunctuation` |  `boolean` Enable automatic punctuation option at the speech backend.  
`defaultNoSpeechTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` If set, use this no-speech timeout when the agent does not provide a no-speech timeout itself.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`phraseSets[]` |  `string` A collection of phrase set resources to use for speech adaptation.  
`optOutConformerModelMigration` |  `boolean` If `true`, the request will opt out for STT conformer model migration. This field will be deprecated once force migration takes place in June 2024. Please refer to [Dialogflow ES Speech model migration](https://cloud.google.com/dialogflow/es/docs/speech-model-migration).  
`geminiAsrConfig` |  `object (`[GeminiAsrConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles#ConversationProfile.GeminiAsrConfig)`)` Optional. Configuration for using Gemini ASR models served via Vertex AI. This field is only used when `useGeminiAsr` is true.  
`useGeminiAsr` |  `boolean` Optional. If true, Gemini ASR will be used for transcription instead of Cloud Speech-to-Text. If false, Cloud Speech-to-Text will be used. If unset, this setting is inherited from the ConversationProfile.  
  
## SpeechContext

Hints for the speech recognizer to help with recognition in a specific conversation state.

JSON representation  
---  
      
    
    {
      "phrases": [
        string
      ],
      "boost": number
    }  
  
Fields  
---  
`phrases[]` |  `string` Optional. A list of strings containing words and phrases that the speech recognizer should recognize with higher likelihood.This list can be used to:

  * improve accuracy for words and phrases you expect the user to say, e.g. typical commands for your Dialogflow agent
  * add additional words to the speech recognizer vocabulary
  * ...

See the [Cloud Speech documentation](https://cloud.google.com/speech-to-text/quotas) for usage limits.  
`boost` |  `number` Optional. Boost for this context compared to other contexts:

  * If the boost is positive, Dialogflow will increase the probability that the phrases in this context are recognized over similar sounding phrases.
  * If the boost is unspecified or non-positive, Dialogflow will not apply any boost.

Dialogflow recommends that you use boosts in the range (0, 20] and that you find a value that fits your use case with binary search.  
  
## BargeInConfig

Configuration of the barge-in behavior. Barge-in instructs the API to return a detected utterance at a proper time while the client is playing back the response audio from a previous request. When the client sees the utterance, it should stop the playback and immediately get ready for receiving the responses for the current request.

The barge-in handling requires the client to start streaming audio input as soon as it starts playing back the audio from the previous response. The playback is modeled into two phases:

  * No barge-in phase: which goes first and during which speech detection should not be carried out.

  * Barge-in phase: which follows the no barge-in phase and during which the API starts speech detection and may inform the client that an utterance has been detected. Note that no-speech event is not expected in this phase.




The client provides this configuration in terms of the durations of those two phases. The durations are measured in terms of the audio length from the start of the input audio.

The flow goes like below:
    
    
    --> Time
    
    without speech detection  | utterance only | utterance or no-speech event
                              |                |
              +-------------+ | +------------+ | +---------------+
    ----------+ no barge-in +-|-+  barge-in  +-|-+ normal period +-----------
              +-------------+ | +------------+ | +---------------+
    

No-speech event is a response with END_OF_UTTERANCE without any transcript following up.

JSON representation  
---  
      
    
    {
      "noBargeInDuration": string,
      "totalDuration": string
    }  
  
Fields  
---  
`noBargeInDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Duration that is not eligible for barge-in at the beginning of the input audio.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`totalDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Total duration for the playback at the beginning of the input audio.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
