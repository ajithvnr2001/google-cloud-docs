---
url: https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/summary_class/
title: Package Classes (2.38.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:24.205810+00:00
---

# Package Classes (2.38.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (2.38.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.38.0 (latest)  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.0  2.19.0  2.18.0  2.17.2  2.16.5  2.15.1  2.14.2  2.13.0  2.12.3  2.11.1  2.10.2  2.9.1  2.8.0  2.7.1  2.6.0  2.5.3  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.5.0 

Summary of entries of Classes for texttospeech.

## Classes 

### [TextToSpeechAsyncClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechAsyncClient)

Service that implements Google Cloud Text-to-Speech API.

### [TextToSpeechClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient)

Service that implements Google Cloud Text-to-Speech API.

### [TextToSpeechLongAudioSynthesizeAsyncClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient)

Service that implements Google Cloud Text-to-Speech API.

### [TextToSpeechLongAudioSynthesizeClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient)

Service that implements Google Cloud Text-to-Speech API.

### [AdvancedVoiceOptions](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AdvancedVoiceOptions)

Used for advanced voice options.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [HarmBlockThreshold](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AdvancedVoiceOptions.HarmBlockThreshold)

Harm block thresholds for the safety settings.

### [HarmCategory](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AdvancedVoiceOptions.HarmCategory)

Harm categories that will block the content.

### [SafetySetting](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AdvancedVoiceOptions.SafetySetting)

Safety setting for a single harm category.

### [SafetySettings](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AdvancedVoiceOptions.SafetySettings)

Safety settings for the request.

### [AudioConfig](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AudioConfig)

Description of audio data to be synthesized.

### [AudioEncoding](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AudioEncoding)

Configuration to set up audio encoder. The encoding determines the output audio format that we'd like.

### [CustomPronunciationParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.CustomPronunciationParams)

Pronunciation customization for a phrase.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PhoneticEncoding](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.CustomPronunciationParams.PhoneticEncoding)

The phonetic encoding of the phrase.
    
    
        The pronunciation can also contain pitch accents. The start
        of a pitch phrase is specified with `^` and the down-pitch
        position is specified with `!`, for example:
    
        ::
    
            phrase:端  pronunciation:^はし
            phrase:箸  pronunciation:^は!し
            phrase:橋  pronunciation:^はし!
    
        We currently only support the Tokyo dialect, which allows at
        most one down-pitch per phrase (i.e. at most one `!`
        between `^`).
    PHONETIC_ENCODING_PINYIN (4):
        Used to specify pronunciations for Mandarin
        words. See https://en.wikipedia.org/wiki/Pinyin.
    
        For example: 朝阳, the pronunciation is "chao2
        yang2". The number represents the tone, and
        there is a space between syllables. Neutral
        tones are represented by 5, for example 孩子 "hai2
        zi5".
    

### [CustomPronunciations](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.CustomPronunciations)

A collection of pronunciation customizations.

### [CustomVoiceParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.CustomVoiceParams)

Description of the custom voice to be synthesized.

### [ReportedUsage](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.CustomVoiceParams.ReportedUsage)

Deprecated. The usage of the synthesized audio. Usage does not affect billing.

### [ListVoicesRequest](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.ListVoicesRequest)

The top-level message sent by the client for the `ListVoices` method.

### [ListVoicesResponse](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.ListVoicesResponse)

The message returned to the client by the `ListVoices` method.

### [MultiSpeakerMarkup](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.MultiSpeakerMarkup)

A collection of turns for multi-speaker synthesis.

### [Turn](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.MultiSpeakerMarkup.Turn)

A multi-speaker turn.

### [MultiSpeakerVoiceConfig](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.MultiSpeakerVoiceConfig)

Configuration for a multi-speaker text-to-speech setup. Enables the use of up to two distinct voices in a single synthesis request.

### [MultispeakerPrebuiltVoice](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.MultispeakerPrebuiltVoice)

Configuration for a single speaker in a Gemini TTS multi-speaker setup. Enables dialogue between two speakers.

### [SsmlVoiceGender](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.SsmlVoiceGender)

Gender of the voice as described in `SSML voice element <https://www.w3.org/TR/speech-synthesis11/#edef_voice>`__.

### [StreamingAudioConfig](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingAudioConfig)

Description of the desired output audio data.

### [StreamingSynthesisInput](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingSynthesisInput)

Input to be synthesized.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [StreamingSynthesizeConfig](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingSynthesizeConfig)

Provides configuration information for the StreamingSynthesize request.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [StreamingSynthesizeRequest](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingSynthesizeRequest)

Request message for the `StreamingSynthesize` method. Multiple `StreamingSynthesizeRequest` messages are sent in one call. The first message must contain a `streaming_config` that fully specifies the request configuration and must not contain `input`. All subsequent messages must only have `input` set.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [StreamingSynthesizeResponse](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingSynthesizeResponse)

`StreamingSynthesizeResponse` is the only message returned to the client by `StreamingSynthesize` method. A series of zero or more `StreamingSynthesizeResponse` messages are streamed back to the client.

### [SynthesisInput](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.SynthesisInput)

Contains text input to be synthesized. Either `text` or `ssml` must be supplied. Supplying both or neither returns `google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT]`. The input size is limited to 5000 bytes.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SynthesizeLongAudioMetadata](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.SynthesizeLongAudioMetadata)

Metadata for response returned by the `SynthesizeLongAudio` method.

### [SynthesizeLongAudioRequest](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.SynthesizeLongAudioRequest)

The top-level message sent by the client for the `SynthesizeLongAudio` method.

### [SynthesizeLongAudioResponse](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.SynthesizeLongAudioResponse)

The message returned to the client by the `SynthesizeLongAudio` method.

### [SynthesizeSpeechRequest](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.SynthesizeSpeechRequest)

The top-level message sent by the client for the `SynthesizeSpeech` method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SynthesizeSpeechResponse](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.SynthesizeSpeechResponse)

The message returned to the client by the `SynthesizeSpeech` method.

### [Voice](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.Voice)

Description of a voice supported by the TTS service.

### [VoiceCloneParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.VoiceCloneParams)

The configuration of Voice Clone feature.

### [VoiceSelectionParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.VoiceSelectionParams)

Description of which voice to use for a synthesis request.

### [TextToSpeechAsyncClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechAsyncClient)

Service that implements Google Cloud Text-to-Speech API.

### [TextToSpeechClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech.TextToSpeechClient)

Service that implements Google Cloud Text-to-Speech API.

### [TextToSpeechLongAudioSynthesizeAsyncClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeAsyncClient)

Service that implements Google Cloud Text-to-Speech API.

### [TextToSpeechLongAudioSynthesizeClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.services.text_to_speech_long_audio_synthesize.TextToSpeechLongAudioSynthesizeClient)

Service that implements Google Cloud Text-to-Speech API.

### [AdvancedVoiceOptions](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.AdvancedVoiceOptions)

Used for advanced voice options.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [HarmBlockThreshold](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.AdvancedVoiceOptions.HarmBlockThreshold)

Harm block thresholds for the safety settings.

### [HarmCategory](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.AdvancedVoiceOptions.HarmCategory)

Harm categories that will block the content.

### [SafetySetting](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.AdvancedVoiceOptions.SafetySetting)

Safety setting for a single harm category.

### [SafetySettings](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.AdvancedVoiceOptions.SafetySettings)

Safety settings for the request.

### [AudioConfig](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.AudioConfig)

Description of audio data to be synthesized.

### [AudioEncoding](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.AudioEncoding)

Configuration to set up audio encoder. The encoding determines the output audio format that we'd like.

### [CustomPronunciationParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.CustomPronunciationParams)

Pronunciation customization for a phrase.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PhoneticEncoding](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.CustomPronunciationParams.PhoneticEncoding)

The phonetic encoding of the phrase.
    
    
        The pronunciation can also contain pitch accents. The start
        of a pitch phrase is specified with `^` and the down-pitch
        position is specified with `!`, for example:
    
        ::
    
            phrase:端  pronunciation:^はし
            phrase:箸  pronunciation:^は!し
            phrase:橋  pronunciation:^はし!
    
        We currently only support the Tokyo dialect, which allows at
        most one down-pitch per phrase (i.e. at most one `!`
        between `^`).
    PHONETIC_ENCODING_PINYIN (4):
        Used to specify pronunciations for Mandarin
        words. See https://en.wikipedia.org/wiki/Pinyin.
    
        For example: 朝阳, the pronunciation is "chao2
        yang2". The number represents the tone, and
        there is a space between syllables. Neutral
        tones are represented by 5, for example 孩子 "hai2
        zi5".
    

### [CustomPronunciations](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.CustomPronunciations)

A collection of pronunciation customizations.

### [CustomVoiceParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.CustomVoiceParams)

Description of the custom voice to be synthesized.

### [ReportedUsage](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.CustomVoiceParams.ReportedUsage)

Deprecated. The usage of the synthesized audio. Usage does not affect billing.

### [ListVoicesRequest](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.ListVoicesRequest)

The top-level message sent by the client for the `ListVoices` method.

### [ListVoicesResponse](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.ListVoicesResponse)

The message returned to the client by the `ListVoices` method.

### [MultiSpeakerMarkup](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.MultiSpeakerMarkup)

A collection of turns for multi-speaker synthesis.

### [Turn](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.MultiSpeakerMarkup.Turn)

A multi-speaker turn.

### [MultiSpeakerVoiceConfig](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.MultiSpeakerVoiceConfig)

Configuration for a multi-speaker text-to-speech setup. Enables the use of up to two distinct voices in a single synthesis request.

### [MultispeakerPrebuiltVoice](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.MultispeakerPrebuiltVoice)

Configuration for a single speaker in a Gemini TTS multi-speaker setup. Enables dialogue between two speakers.

### [SsmlVoiceGender](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.SsmlVoiceGender)

Gender of the voice as described in `SSML voice element <https://www.w3.org/TR/speech-synthesis11/#edef_voice>`__.

### [StreamingAudioConfig](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.StreamingAudioConfig)

Description of the desired output audio data.

### [StreamingSynthesisInput](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.StreamingSynthesisInput)

Input to be synthesized.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [StreamingSynthesizeConfig](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.StreamingSynthesizeConfig)

Provides configuration information for the StreamingSynthesize request.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [StreamingSynthesizeRequest](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.StreamingSynthesizeRequest)

Request message for the `StreamingSynthesize` method. Multiple `StreamingSynthesizeRequest` messages are sent in one call. The first message must contain a `streaming_config` that fully specifies the request configuration and must not contain `input`. All subsequent messages must only have `input` set.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [StreamingSynthesizeResponse](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.StreamingSynthesizeResponse)

`StreamingSynthesizeResponse` is the only message returned to the client by `StreamingSynthesize` method. A series of zero or more `StreamingSynthesizeResponse` messages are streamed back to the client.

### [SynthesisInput](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.SynthesisInput)

Contains text input to be synthesized. Either `text` or `ssml` must be supplied. Supplying both or neither returns `google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT]`. The input size is limited to 5000 bytes.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SynthesizeLongAudioMetadata](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.SynthesizeLongAudioMetadata)

Metadata for response returned by the `SynthesizeLongAudio` method.

### [SynthesizeLongAudioRequest](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.SynthesizeLongAudioRequest)

The top-level message sent by the client for the `SynthesizeLongAudio` method.

### [SynthesizeLongAudioResponse](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.SynthesizeLongAudioResponse)

The message returned to the client by the `SynthesizeLongAudio` method.

### [SynthesizeSpeechRequest](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.SynthesizeSpeechRequest)

The top-level message sent by the client for the `SynthesizeSpeech` method.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TimepointType](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.SynthesizeSpeechRequest.TimepointType)

The type of timepoint information that is returned in the response.

### [SynthesizeSpeechResponse](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.SynthesizeSpeechResponse)

The message returned to the client by the `SynthesizeSpeech` method.

### [Timepoint](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.Timepoint)

This contains a mapping between a certain point in the input text and a corresponding time in the output audio.

### [Voice](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.Voice)

Description of a voice supported by the TTS service.

### [VoiceCloneParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.VoiceCloneParams)

The configuration of Voice Clone feature.

### [VoiceSelectionParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1beta1.types.VoiceSelectionParams)

Description of which voice to use for a synthesis request.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
