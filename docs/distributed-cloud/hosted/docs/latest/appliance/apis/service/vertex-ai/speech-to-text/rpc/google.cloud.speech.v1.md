---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1
title: Package google.cloud.location \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:13.621740+00:00
---

# Package google.cloud.location  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Package google.cloud.location Stay organized with collections  Save and categorize content based on your preferences. 

Package google.cloud.speech.v1

## Speech

Service that implements Vertex AI Speech API.

Recognize  
---  
` rpc Recognize(`[RecognizeRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#google.cloud.speech.v1.html.RecognizeRequest)`) returns (`[RecognizeResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#google.cloud.speech.v1.html.RecognizeResponse)`) ` Performs synchronous speech recognition: receive results after all audio has been sent and processed.  
StreamingRecognize  
---  
` rpc StreamingRecognize(`[StreamingRecognizeRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#google.cloud.speech.v1.html.StreamingRecognizeRequest)`) returns (`[StreamingRecognizeResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#google.cloud.speech.v1.html.StreamingRecognizeResponse)`) ` Performs bidirectional streaming speech recognition: receive results while sending audio. This method is only available via the gRPC API (not REST).  
  
## RecognitionAudio

Contains audio data in the encoding specified in the `RecognitionConfig`. See content limits (https://cloud.google.com/speech-to-text/quotas#content).

Fields  
---  
Union field `audio_source`. The audio source is inline content.  
`content` |  `bytes` The audio data bytes encoded as specified in `RecognitionConfig`. All `bytes` fields and proto buffers use a pure binary representation. JSON representations use `base64`.  
  
## RecognitionConfig

Provides information to the recognizer that specifies how to process the request.

Fields  
---  
`encoding` |  ``[AudioEncoding](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#google.cloud.speech.v1.html.RecognitionConfig.AudioEncoding)`` Encoding of audio data sent in all `RecognitionAudio` messages. This field is optional for `FLAC` and `WAV` audio files and required for all other audio formats. For details, see `[AudioEncoding](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#google.cloud.speech.v1.html.RecognitionConfig.AudioEncoding)`.  
`sample_rate_hertz` |  `int32` Sample rate in Hertz of the audio data sent in all `RecognitionAudio` messages. Valid values are: 8000-48000. 16000 is optimal. For best results, set the sampling rate of the audio source to 16000 Hz. If that's not possible, use the native sample rate of the audio source (instead of re-sampling). This field is optional for FLAC and WAV audio files, but is required for all other audio formats. For details, see `[AudioEncoding](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#google.cloud.speech.v1.html.RecognitionConfig.AudioEncoding)`.  
`audio_channel_count` |  `int32` The number of channels in the input audio data. ONLY set this for MULTI-CHANNEL recognition. Valid values for LINEAR16 and FLAC are `1`-`8`. Valid values for OGG_OPUS are '1'-'254'. Valid value for MULAW, AMR, and AMR_WB is only `1`. If `0` or omitted, defaults to one channel (mono). Note: We only recognize the first channel by default. To perform independent recognition on each channel set `enable_separate_recognition_per_channel` to 'true'.  
`enable_separate_recognition_per_channel` |  `bool` This needs to be set to `true` explicitly and `audio_channel_count` > 1 to get each channel recognized separately. The recognition result will contain a `channel_tag` field to state which channel that result belongs to. If this is not true, we will only recognize the first channel. The request is billed cumulatively for all channels recognized: `audio_channel_count` multiplied by the length of the audio.  
`language_code` |  `string` Required. The language of the supplied audio as a BCP-47 (https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: "en-US". See Language Support (https://cloud.google.com/speech-to-text/docs/languages) for a list of the currently supported language codes.  
`enable_automatic_punctuation` |  `bool` If 'true', adds punctuation to recognition result hypotheses. This feature is only available in select languages. Setting this for requests in other languages has no effect at all. The default 'false' value does not add punctuation to result hypotheses.  
`model` |  `string` Which model to select for the given request. Select the model best suited to your domain to get best results. If a model is not explicitly specified, then we auto-select a model based on the parameters in the RecognitionConfig. | **Model** | **Description**  
---|---  
`default` | Best for audio that is not one of the specific audio models. For example, long-form audio. Ideally the audio is high-fidelity, recorded at a 16khz or greater sampling rate.  
  
## AudioEncoding

The encoding of the audio data sent in the request.

All encodings support only 1 channel (mono) audio, unless the `audio_channel_count` and `enable_separate_recognition_per_channel` fields are set.

For best results, the audio source should be captured and transmitted using a lossless encoding (`FLAC` or `LINEAR16`). The accuracy of the speech recognition can be reduced if lossy codecs are used to capture or transmit audio, particularly if background noise is present. Lossy codecs include `MULAW`, `AMR`, `AMR_WB`, and `OGG_OPUS`.

The `FLAC` and `WAV` audio file formats include a header that describes the included audio content. You can request recognition for `WAV` files that contain either `LINEAR16` or `MULAW` encoded audio. If you send `FLAC` or `WAV` audio file format in your request, you do not need to specify an `AudioEncoding`; the audio encoding format is determined from the file header. If you specify an `AudioEncoding` when you send send `FLAC` or `WAV` audio, the encoding configuration must match the encoding described in the audio header; otherwise the request returns an `google.rpc.Code.INVALID_ARGUMENT` error code.

Enums  
---  
`ENCODING_UNSPECIFIED` | Not specified.  
`LINEAR16` | Uncompressed 16-bit signed little-endian samples (Linear PCM).  
`FLAC` | `FLAC` (Free Lossless Audio Codec) is the recommended encoding because it is lossless--therefore recognition is not compromised--and requires only about half the bandwidth of `LINEAR16`. `FLAC` stream encoding supports 16-bit and 24-bit samples, however, not all fields in `STREAMINFO` are supported.  
`MULAW` | 8-bit samples that compand 14-bit audio samples using G.711 PCMU/mu-law.  
`OGG_OPUS` | Opus encoded audio frames in Ogg container OggOpus (https://wiki.xiph.org/OggOpus). `sample_rate_hertz` must be one of 8000, 12000, 16000, 24000, or 48000.  
  
## RecognizeRequest

The top-level message sent by the client for the `Recognize` method.

Fields  
---  
`config` |  ``[RecognitionConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#google.cloud.speech.v1.html.RecognitionConfig)`` Required. Provides information to the recognizer that specifies how to process the request.  
`audio` |  ``[RecognitionAudio](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#google.cloud.speech.v1.html.RecognitionAudio)`` Required. The audio data to be recognized.  
  
## RecognizeResponse

The only message returned to the client by the `Recognize` method. It contains the result as zero or more sequential `SpeechRecognitionResult` messages.

Fields  
---  
`results[]` |  ``[SpeechRecognitionResult](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#google.cloud.speech.v1.html.SpeechRecognitionResult)`` Sequential list of transcription results corresponding to sequential portions of audio.  
  
## SpeechRecognitionAlternative

Alternative hypotheses (a.k.a. n-best list).

Fields  
---  
`transcript` |  `string` Transcript text representing the words that the user spoke.  
`words[]` |  ``[WordInfo](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#google.cloud.speech.v1.html.WordInfo)`` A list of word-specific information for each recognized word.  
  
## SpeechRecognitionResult

A speech recognition result corresponding to a portion of the audio.

Fields  
---  
`alternatives[]` |  ``[SpeechRecognitionAlternative](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#google.cloud.speech.v1.html.SpeechRecognitionAlternative)`` May contain one or more recognition hypotheses (up to the maximum specified in `max_alternatives`). These alternatives are ordered in terms of accuracy, with the top (first) alternative being the most probable, as ranked by the recognizer.  
`channel_tag` |  `int32` For multi-channel audio, this is the channel number corresponding to the recognized result for the audio from that channel. For audio_channel_count = N, its output values can range from '1' to 'N'.  
  
## StreamingRecognitionConfig

Provides information to the recognizer that specifies how to process the request.

Fields  
---  
`config` |  ``[RecognitionConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#google.cloud.speech.v1.html.RecognitionConfig)`` Required. Provides information to the recognizer that specifies how to process the request.  
  
## StreamingRecognitionResult

A streaming speech recognition result corresponding to a portion of the audio that is currently being processed.

Fields  
---  
`alternatives[]` |  ``[SpeechRecognitionAlternative](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#google.cloud.speech.v1.html.SpeechRecognitionAlternative)`` May contain one or more recognition hypotheses (up to the maximum specified in `max_alternatives`). These alternatives are ordered in terms of accuracy, with the top (first) alternative being the most probable, as ranked by the recognizer.  
`is_final` |  `bool` If `false`, this `StreamingRecognitionResult` represents an interim result that may change. If `true`, this is the final time the speech service will return this particular `StreamingRecognitionResult`, the recognizer will not return any further hypotheses for this portion of the transcript and corresponding audio.  
`result_end_time` |  `` Duration (https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration) `` Time offset of the end of this result relative to the beginning of the audio.  
`channel_tag` |  `int32` For multi-channel audio, this is the channel number corresponding to the recognized result for the audio from that channel. For audio_channel_count = N, its output values can range from '1' to 'N'.  
  
## StreamingRecognizeRequest

The top-level message sent by the client for the `StreamingRecognize` method. Multiple `StreamingRecognizeRequest` messages are sent. The first message must contain a `streaming_config` message and must not contain `audio_content`. All subsequent messages must contain `audio_content` and must not contain a `streaming_config` message.

Fields  
---  
Union field `streaming_request`. The streaming request, which is either a streaming config or audio content. `streaming_request` can be only one of the following:  
`streaming_config` |  ``[StreamingRecognitionConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/speech-to-text/rpc/google.cloud.speech.v1#google.cloud.speech.v1.html.StreamingRecognitionConfig)`` Provides information to the recognizer that specifies how to process the request. The first `StreamingRecognizeRequest` message must contain a `streaming_config` message.  
`audio_content` |  `bytes` The audio data to be recognized. Sequential chunks of audio data are sent in sequential `StreamingRecognizeRequest` messages. The first `StreamingRecognizeRequest` message must not contain `audio_content` data and all subsequent `StreamingRecognizeRequest` messages must contain `audio_content` data. The audio bytes must be encoded as specified in `RecognitionConfig`. Note: as with all bytes fields, proto buffers use a pure binary representation (not base64). See content limits (https://cloud.google.com/speech-to-text/quotas#content).  
  
## StreamingRecognizeResponse

`StreamingRecognizeResponse` is the only message returned to the client by `StreamingRecognize`. A series of zero or more `StreamingRecognizeResponse` messages are streamed back to the client. 

Here's an example of a series of `StreamingRecognizeResponse` messages that might be returned while processing audio:

  1. `results` { alternatives { transcript: "tube" } }

  2. `results` { alternatives { transcript: "to be a" } }

  3. `results` { alternatives { transcript: "to be" } } `results` { alternatives { transcript: " or not to be" } }

  4. `results` { alternatives { transcript: "to be or not to be" } alternatives { transcript: "to bee or not to bee" } is_final: true }

  5. `results` { alternatives { transcript: " that's" } }

  6. `results` { alternatives { transcript: " that is" } } `results` { alternatives { transcript: " the question" } }

  7. `results` { alternatives { transcript: " that is the question" } alternatives { transcript: " that was the question" } is_final: true }




Notes:

  * Responses #4 and #7 contain final results, which are indicated by `is_final: true`. Concatenating these messages together generates the full transcript: "to be or not to be that is the question."

  * The other responses contain interim `results`. Responses #3 and #6 contain two interim `results`. 


Fields  
---  
`error` |  ``Status`` If set, returns a `google.rpc.Status` message that specifies the error for the operation.  
`results[]` |  ``StreamingRecognitionResult`` This repeated list contains zero or more results that correspond to consecutive portions of the audio currently being processed. It contains zero or one `is_final=true` result (the newly settled portion), followed by zero or more `is_final=false` results (the interim results).  
`speech_event_type` |  ``SpeechEventType`` Indicates the type of speech event.  
  
## SpeechEventType

Indicates the type of speech event.

Enums  
---  
`SPEECH_EVENT_UNSPECIFIED` | No speech event specified.  
  
## WordInfo

Word-specific information for recognized words.

Fields  
---  
`start_time` |  ``Duration (https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` Time offset relative to the beginning of the audio, and corresponding to the start of the spoken word. This field is only set if `enable_word_time_offsets=true` and only in the top hypothesis. This is an experimental feature and the accuracy of the time offset can vary.  
`end_time` |  ``Duration (https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` Time offset relative to the beginning of the audio, and corresponding to the end of the spoken word. This field is only set if `enable_word_time_offsets=true` and only in the top hypothesis. This is an experimental feature and the accuracy of the time offset can vary.  
`word` |  `string` The word corresponding to this set of information.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-11 UTC."],[],[]] 
