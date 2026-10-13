---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn/
title: ConversationTurn \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:31.612050+00:00
---

# ConversationTurn  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  ConversationTurn Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * UserInput
    * JSON representation
  * QueryInput
    * JSON representation
  * TextInput
    * JSON representation
  * IntentInput
    * JSON representation
  * AudioInput
    * JSON representation
  * InputAudioConfig
    * JSON representation
  * AudioEncoding
  * SpeechModelVariant
  * BargeInConfig
    * JSON representation
  * EventInput
    * JSON representation
  * DtmfInput
    * JSON representation
  * ToolCallResult
    * JSON representation
  * Error
    * JSON representation
  * VirtualAgentOutput
    * JSON representation
  * TestRunDifference
    * JSON representation
  * DiffType



One interaction between a human and virtual agent. The human provides some input and the virtual agent provides a response.

JSON representation  
---  
      
    
    {
      "userInput": {
        object ([UserInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#UserInput))
      },
      "virtualAgentOutput": {
        object ([VirtualAgentOutput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#VirtualAgentOutput))
      }
    }  
  
Fields  
---  
`userInput` |  `object (`[UserInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#UserInput)`)` The user input.  
`virtualAgentOutput` |  `object (`[VirtualAgentOutput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#VirtualAgentOutput)`)` The virtual agent output.  
  
## UserInput

The input from the human user.

JSON representation  
---  
      
    
    {
      "input": {
        object ([QueryInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#QueryInput))
      },
      "injectedParameters": {
        object
      },
      "isWebhookEnabled": boolean,
      "enableSentimentAnalysis": boolean
    }  
  
Fields  
---  
`input` |  `object (`[QueryInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#QueryInput)`)` Supports `[text input](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#QueryInput.FIELDS.text)`, `[event input](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#QueryInput.FIELDS.event)`, `[dtmf input](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#QueryInput.FIELDS.dtmf)` in the test case.  
`injectedParameters` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Parameters that need to be injected into the conversation during intent detection.  
`isWebhookEnabled` |  `boolean` If webhooks should be allowed to trigger in response to the user utterance. Often if parameters are injected, webhooks should not be enabled.  
`enableSentimentAnalysis` |  `boolean` Whether sentiment analysis is enabled.  
  
## QueryInput

Represents the query input. It can contain one of:

  1. A conversational query in the form of text.

  2. An intent query that specifies which intent to trigger.

  3. Natural language speech audio to be processed.

  4. An event to be triggered.

  5. DTMF digits to invoke an intent and fill in parameter value.

  6. The results of a tool executed by the client.


JSON representation  
---  
      
    
    {
      "languageCode": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "text": {
        object ([TextInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#TextInput))
      },
      "intent": {
        object ([IntentInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#IntentInput))
      },
      "audio": {
        object ([AudioInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#AudioInput))
      },
      "event": {
        object ([EventInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#EventInput))
      },
      "dtmf": {
        object ([DtmfInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#DtmfInput))
      },
      "toolCallResult": {
        object ([ToolCallResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#ToolCallResult))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`languageCode` |  `string` Required. The language of the input. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. Note that queries in the same session do not necessarily need to specify the same language.  
Required. The input specification. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`text` |  `object (`[TextInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#TextInput)`)` The natural language text to be processed.  
`intent` |  `object (`[IntentInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#IntentInput)`)` The intent to be triggered.  
`audio` |  `object (`[AudioInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#AudioInput)`)` The natural language speech audio to be processed.  
`event` |  `object (`[EventInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#EventInput)`)` The event to be triggered.  
`dtmf` |  `object (`[DtmfInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#DtmfInput)`)` The DTMF event to be handled.  
`toolCallResult` |  `object (`[ToolCallResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#ToolCallResult)`)` The results of a tool executed by the client.  
End of mutually exclusive fields.  
  
## TextInput

Represents the natural language text to be processed.

JSON representation  
---  
      
    
    {
      "text": string
    }  
  
Fields  
---  
`text` |  `string` Required. The UTF-8 encoded natural language text to be processed.  
  
## IntentInput

Represents the intent to trigger programmatically rather than as a result of natural language processing.

JSON representation  
---  
      
    
    {
      "intent": string
    }  
  
Fields  
---  
`intent` |  `string` Required. The unique identifier of the intent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>`.  
  
## AudioInput

Represents the natural speech audio to be processed.

JSON representation  
---  
      
    
    {
      "config": {
        object ([InputAudioConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#InputAudioConfig))
      },
      "audio": string
    }  
  
Fields  
---  
`config` |  `object (`[InputAudioConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#InputAudioConfig)`)` Required. Instructs the speech recognizer how to process the speech audio.  
`audio` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The natural language speech audio to be processed. A single request can contain up to 2 minutes of speech audio data. The `[transcribed text](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryResult#FIELDS.transcript)` cannot contain more than 256 bytes.For non-streaming audio detect intent, both `config` and `audio` must be provided. For streaming audio detect intent, `config` must be provided in the first request and `audio` must be provided in all following requests.A base64-encoded string.  
  
## InputAudioConfig

Instructs the speech recognizer on how to process the audio content.

JSON representation  
---  
      
    
    {
      "audioEncoding": enum ([AudioEncoding](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#AudioEncoding)),
      "sampleRateHertz": integer,
      "enableWordInfo": boolean,
      "phraseHints": [
        string
      ],
      "model": string,
      "modelVariant": enum ([SpeechModelVariant](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#SpeechModelVariant)),
      "singleUtterance": boolean,
      "bargeInConfig": {
        object ([BargeInConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#BargeInConfig))
      },
      "optOutConformerModelMigration": boolean
    }  
  
Fields  
---  
`audioEncoding` |  `enum (`[AudioEncoding](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#AudioEncoding)`)` Required. Audio encoding of the audio content to process.  
`sampleRateHertz` |  `integer` Sample rate (in Hertz) of the audio content sent in the query. Refer to [Cloud Speech API documentation](https://cloud.google.com/speech-to-text/docs/basics) for more details.  
`enableWordInfo` |  `boolean` Optional. If `true`, Dialogflow returns `SpeechWordInfo` in `StreamingRecognitionResult` with information about the recognized speech words, e.g. start and end time offsets. If false or unspecified, Speech doesn't return any word-level information.  
`phraseHints[]` |  `string` Optional. A list of strings containing words and phrases that the speech recognizer should recognize with higher likelihood.See [the Cloud Speech documentation](https://cloud.google.com/speech-to-text/docs/basics#phrase-hints) for more details.  
`model` |  `string` Optional. Which Speech model to select for the given request. For more information, see [Speech models](https://cloud.google.com/dialogflow/cx/docs/concept/speech-models).  
`modelVariant` |  `enum (`[SpeechModelVariant](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#SpeechModelVariant)`)` Optional. Which variant of the `[Speech model](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#InputAudioConfig.FIELDS.model)` to use.  
`singleUtterance` |  `boolean` Optional. If `false` (default), recognition does not cease until the client closes the stream. If `true`, the recognizer will detect a single spoken utterance in input audio. Recognition ceases when it detects the audio's voice has stopped or paused. In this case, once a detected intent is received, the client should close the stream and start a new request with a new stream as needed. Note: This setting is relevant only for streaming methods.  
`bargeInConfig` |  `object (`[BargeInConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#BargeInConfig)`)` Configuration of barge-in behavior during the streaming of input audio.  
`optOutConformerModelMigration` |  `boolean` If `true`, the request will opt out for STT conformer model migration. This field will be deprecated once force migration takes place in June 2024. Please refer to [Dialogflow CX Speech model migration](https://cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration).  
  
## AudioEncoding

Audio encoding of the audio content sent in the conversational query request. Refer to the [Cloud Speech API documentation](https://cloud.google.com/speech-to-text/docs/basics) for more details.

Enums  
---  
`AUDIO_ENCODING_UNSPECIFIED` | Not specified.  
`AUDIO_ENCODING_LINEAR_16` | Uncompressed 16-bit signed little-endian samples (Linear PCM). LINT: LEGACY_NAMES  
`AUDIO_ENCODING_FLAC` | [`FLAC`](https://xiph.org/flac/documentation.html) (Free Lossless Audio Codec) is the recommended encoding because it is lossless (therefore recognition is not compromised) and requires only about half the bandwidth of `LINEAR16`. `FLAC` stream encoding supports 16-bit and 24-bit samples, however, not all fields in `STREAMINFO` are supported.  
`AUDIO_ENCODING_MULAW` | 8-bit samples that compand 14-bit audio samples using G.711 PCMU/mu-law.  
`AUDIO_ENCODING_AMR` | Adaptive Multi-Rate Narrowband codec. `sampleRateHertz` must be 8000.  
`AUDIO_ENCODING_AMR_WB` | Adaptive Multi-Rate Wideband codec. `sampleRateHertz` must be 16000.  
`AUDIO_ENCODING_OGG_OPUS` | Opus encoded audio frames in Ogg container ([OggOpus](https://wiki.xiph.org/OggOpus)). `sampleRateHertz` must be 16000.  
`AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE` | Although the use of lossy encodings is not recommended, if a very low bitrate encoding is required, `OGG_OPUS` is highly preferred over Speex encoding. The [Speex](https://speex.org/) encoding supported by Dialogflow API has a header byte in each block, as in MIME type `audio/x-speex-with-header-byte`. It is a variant of the RTP Speex encoding defined in [RFC 5574](https://tools.ietf.org/html/rfc5574). The stream is a sequence of blocks, one block per RTP packet. Each block starts with a byte containing the length of the block, in bytes, followed by one or more frames of Speex data, padded to an integral number of bytes (octets) as specified in RFC 5574. In other words, each RTP header is replaced with a single byte containing the block length. Only Speex wideband is supported. `sampleRateHertz` must be 16000.  
`AUDIO_ENCODING_ALAW` | 8-bit samples that compand 13-bit audio samples using G.711 PCMU/a-law.  
  
## SpeechModelVariant

Variant of the specified `[Speech model](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#InputAudioConfig.FIELDS.model)` to use.

See the [Cloud Speech documentation](https://cloud.google.com/speech-to-text/docs/enhanced-models) for which models have different variants. For example, the "phone_call" model has both a standard and an enhanced variant. When you use an enhanced model, you will generally receive higher quality results than for a standard model.

Enums  
---  
`SPEECH_MODEL_VARIANT_UNSPECIFIED` | No model variant specified. In this case Dialogflow defaults to USE_BEST_AVAILABLE.  
`USE_BEST_AVAILABLE` | Use the best available variant of the [Speech model][InputAudioConfig.model] that the caller is eligible for.  
`USE_STANDARD` | Use standard model variant even if an enhanced model is available. See the [Cloud Speech documentation](https://cloud.google.com/speech-to-text/docs/enhanced-models) for details about enhanced models.  
`USE_ENHANCED` | Use an enhanced model variant:

  * If an enhanced variant does not exist for the given `[model](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#InputAudioConfig.FIELDS.model)` and request language, Dialogflow falls back to the standard variant.

The [Cloud Speech documentation](https://cloud.google.com/speech-to-text/docs/enhanced-models) describes which models have enhanced variants.  
  
## BargeInConfig

Configuration of the barge-in behavior. Barge-in instructs the API to return a detected utterance at a proper time while the client is playing back the response audio from a previous request. When the client sees the utterance, it should stop the playback and immediately get ready for receiving the responses for the current request.

The barge-in handling requires the client to start streaming audio input as soon as it starts playing back the audio from the previous response. The playback is modeled into two phases:

  * No barge-in phase: which goes first and during which speech detection should not be carried out.

  * Barge-in phase: which follows the no barge-in phase and during which the API starts speech detection and may inform the client that an utterance has been detected. Note that no-speech event is not expected in this phase.




The client provides this configuration in terms of the durations of those two phases. The durations are measured in terms of the audio length from the start of the input audio.

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
  
## EventInput

Represents the event to trigger.

JSON representation  
---  
      
    
    {
      "event": string
    }  
  
Fields  
---  
`event` |  `string` Name of the event.  
  
## DtmfInput

Represents the input for dtmf event.

JSON representation  
---  
      
    
    {
      "digits": string,
      "finishDigit": string
    }  
  
Fields  
---  
`digits` |  `string` The dtmf digits.  
`finishDigit` |  `string` The finish digit (if any).  
  
## ToolCallResult

The result of calling a tool's action that has been executed by the client.

JSON representation  
---  
      
    
    {
      "tool": string,
      "action": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "error": {
        object ([Error](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#Error))
      },
      "outputParameters": {
        object
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`tool` |  `string` Required. The `[tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)` associated with this call. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>`.  
`action` |  `string` Required. The name of the tool's action associated with this call.  
The tool call's result. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`error` |  `object (`[Error](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#Error)`)` The tool call's error.  
`outputParameters` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The tool call's output parameters.  
End of mutually exclusive fields.  
  
## Error

An error produced by the tool call.

JSON representation  
---  
      
    
    {
      "message": string
    }  
  
Fields  
---  
`message` |  `string` Optional. The error message of the function.  
  
## VirtualAgentOutput

The output from the virtual agent.

JSON representation  
---  
      
    
    {
      "sessionParameters": {
        object
      },
      "differences": [
        {
          object ([TestRunDifference](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#TestRunDifference))
        }
      ],
      "diagnosticInfo": {
        object
      },
      "triggeredIntent": {
        object ([Intent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent))
      },
      "currentPage": {
        object ([Page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page))
      },
      "textResponses": [
        {
          object ([Text](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Text))
        }
      ],
      "status": {
        object ([Status](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Status))
      }
    }  
  
Fields  
---  
`sessionParameters` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The session parameters available to the bot at this point.  
`differences[]` |  `object (`[TestRunDifference](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#TestRunDifference)`)` Output only. If this is part of a [result conversation turn][TestCaseResult.conversation_turns], the list of differences between the original run and the replay for this output, if any.  
`diagnosticInfo` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Required. Input only. The diagnostic [info][Session.DetectIntentResponse.QueryResult.diagnostic_info] output for the turn. Required to calculate the testing coverage.  
`triggeredIntent` |  `object (`[Intent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent)`)` The `[Intent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent)` that triggered the response. Only name and displayName will be set.  
`currentPage` |  `object (`[Page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page)`)` The `[Page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.pages#Page)` on which the utterance was spoken. Only name and displayName will be set.  
`textResponses[]` |  `object (`[Text](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Text)`)` The `[text](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Text)` responses from the agent for the turn.  
`status` |  `object (`[Status](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Status)`)` Response error from the agent in the test result. If set, other output is empty.  
  
## TestRunDifference

The description of differences between original and replayed agent output.

JSON representation  
---  
      
    
    {
      "type": enum ([DiffType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#DiffType)),
      "description": string
    }  
  
Fields  
---  
`type` |  `enum (`[DiffType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#DiffType)`)` The type of diff.  
`description` |  `string` A human readable description of the diff, showing the actual output vs expected output.  
  
## DiffType

What part of the message replay differs from the test case.

Enums  
---  
`DIFF_TYPE_UNSPECIFIED` | Should never be used.  
`INTENT` | The intent.  
`PAGE` | The page.  
`PARAMETERS` | The parameters.  
`UTTERANCE` | The message utterance.  
`FLOW` | The flow.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
