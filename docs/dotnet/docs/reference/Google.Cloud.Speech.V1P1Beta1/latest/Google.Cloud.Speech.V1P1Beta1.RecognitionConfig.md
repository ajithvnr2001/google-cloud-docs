---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.RecognitionConfig
title: Google Cloud Speech v1p1beta1 API - Class RecognitionConfig (3.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:35.161070+00:00
---

# Google Cloud Speech v1p1beta1 API - Class RecognitionConfig (3.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.RecognitionConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Speech v1p1beta1 API - Class RecognitionConfig (3.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta10 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.RecognitionConfig)
  * [ 3.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/3.0.0-beta09/Google.Cloud.Speech.V1P1Beta1.RecognitionConfig)
  * [ 2.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/2.0.0-beta09/Google.Cloud.Speech.V1P1Beta1.RecognitionConfig)


    
    
    public sealed class RecognitionConfig : IMessage<RecognitionConfig>, IEquatable<RecognitionConfig>, IDeepCloneable<RecognitionConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Speech v1p1beta1 API class RecognitionConfig.

Provides information to the recognizer that specifies how to process the request.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RecognitionConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RecognitionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.RecognitionConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RecognitionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.RecognitionConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RecognitionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.RecognitionConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Speech.V1P1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1)

## Assembly

Google.Cloud.Speech.V1P1Beta1.dll

## Constructors 

### RecognitionConfig()
    
    
    public RecognitionConfig()

### RecognitionConfig(RecognitionConfig)
    
    
    public RecognitionConfig(RecognitionConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RecognitionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.RecognitionConfig)`  
  
  
## Properties 

### Adaptation
    
    
    public SpeechAdaptation Adaptation { get; set; }

Speech adaptation configuration improves the accuracy of speech recognition. For more information, see the [speech adaptation](https://cloud.google.com/speech-to-text/docs/adaptation) documentation. When speech adaptation is set it supersedes the `speech_contexts` field.

**Property Value**  
---  
**Type** | **Description**  
`[SpeechAdaptation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.SpeechAdaptation)` |   
  
### AlternativeLanguageCodes
    
    
    public RepeatedField<string> AlternativeLanguageCodes { get; }

A list of up to 3 additional [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tags, listing possible alternative languages of the supplied audio. See [Language Support](https://cloud.google.com/speech-to-text/docs/languages) for a list of the currently supported language codes. If alternative languages are listed, recognition result will contain recognition in the most likely language detected including the main language_code. The recognition result will include the language tag of the language detected in the audio. Note: This feature is only supported for Voice Command and Voice Search use cases and performance may vary for other use cases (e.g., phone call transcription).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AudioChannelCount
    
    
    public int AudioChannelCount { get; set; }

The number of channels in the input audio data. ONLY set this for MULTI-CHANNEL recognition. Valid values for LINEAR16, OGG_OPUS and FLAC are `1`-`8`. Valid value for MULAW, AMR, AMR_WB and SPEEX_WITH_HEADER_BYTE is only `1`. If `0` or omitted, defaults to one channel (mono). Note: We only recognize the first channel by default. To perform independent recognition on each channel set `enable_separate_recognition_per_channel` to 'true'.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### DiarizationConfig
    
    
    public SpeakerDiarizationConfig DiarizationConfig { get; set; }

Config to enable speaker diarization and set additional parameters to make diarization better suited for your application. Note: When this is enabled, we send all the words from the beginning of the audio for the top alternative in every consecutive STREAMING responses. This is done in order to improve our speaker tags as our models learn to identify the speakers in the conversation over time. For non-streaming requests, the diarization results will be provided only in the top alternative of the FINAL SpeechRecognitionResult.

**Property Value**  
---  
**Type** | **Description**  
`[SpeakerDiarizationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.SpeakerDiarizationConfig)` |   
  
### DiarizationSpeakerCount
    
    
    [Obsolete]
    public int DiarizationSpeakerCount { get; set; }

If set, specifies the estimated number of speakers in the conversation. Defaults to '2'. Ignored unless enable_speaker_diarization is set to true. Note: Use diarization_config instead.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### EnableAutomaticPunctuation
    
    
    public bool EnableAutomaticPunctuation { get; set; }

If 'true', adds punctuation to recognition result hypotheses. This feature is only available in select languages. Setting this for requests in other languages has no effect at all. The default 'false' value does not add punctuation to result hypotheses.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EnableSeparateRecognitionPerChannel
    
    
    public bool EnableSeparateRecognitionPerChannel { get; set; }

This needs to be set to `true` explicitly and `audio_channel_count` > 1 to get each channel recognized separately. The recognition result will contain a `channel_tag` field to state which channel that result belongs to. If this is not true, we will only recognize the first channel. The request is billed cumulatively for all channels recognized: `audio_channel_count` multiplied by the length of the audio.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EnableSpeakerDiarization
    
    
    [Obsolete]
    public bool EnableSpeakerDiarization { get; set; }

If 'true', enables speaker detection for each recognized word in the top alternative of the recognition result using a speaker_label provided in the WordInfo. Note: Use diarization_config instead.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EnableSpokenEmojis
    
    
    public bool? EnableSpokenEmojis { get; set; }

The spoken emoji behavior for the call If not set, uses default behavior based on model of choice If 'true', adds spoken emoji formatting for the request. This will replace spoken emojis with the corresponding Unicode symbols in the final transcript. If 'false', spoken emojis are not replaced.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EnableSpokenPunctuation
    
    
    public bool? EnableSpokenPunctuation { get; set; }

The spoken punctuation behavior for the call If not set, uses default behavior based on model of choice e.g. command_and_search will enable spoken punctuation by default If 'true', replaces spoken punctuation with the corresponding symbols in the request. For example, "how are you question mark" becomes "how are you?". See <https://cloud.google.com/speech-to-text/docs/spoken-punctuation> for support. If 'false', spoken punctuation is not replaced.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EnableWordConfidence
    
    
    public bool EnableWordConfidence { get; set; }

If `true`, the top result includes a list of words and the confidence for those words. If `false`, no word-level confidence information is returned. The default is `false`.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EnableWordTimeOffsets
    
    
    public bool EnableWordTimeOffsets { get; set; }

If `true`, the top result includes a list of words and the start and end time offsets (timestamps) for those words. If `false`, no word-level time offset information is returned. The default is `false`.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Encoding
    
    
    public RecognitionConfig.Types.AudioEncoding Encoding { get; set; }

Encoding of audio data sent in all `RecognitionAudio` messages. This field is optional for `FLAC` and `WAV` audio files and required for all other audio formats. For details, see [AudioEncoding][google.cloud.speech.v1p1beta1.RecognitionConfig.AudioEncoding].

**Property Value**  
---  
**Type** | **Description**  
`[RecognitionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.RecognitionConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.RecognitionConfig.Types)[AudioEncoding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.RecognitionConfig.Types.AudioEncoding)` |   
  
### LanguageCode
    
    
    public string LanguageCode { get; set; }

Required. The language of the supplied audio as a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: "en-US". See [Language Support](https://cloud.google.com/speech-to-text/docs/languages) for a list of the currently supported language codes.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MaxAlternatives
    
    
    public int MaxAlternatives { get; set; }

Maximum number of recognition hypotheses to be returned. Specifically, the maximum number of `SpeechRecognitionAlternative` messages within each `SpeechRecognitionResult`. The server may return fewer than `max_alternatives`. Valid values are `0`-`30`. A value of `0` or `1` will return a maximum of one. If omitted, will return a maximum of one.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Metadata
    
    
    [Obsolete]
    public RecognitionMetadata Metadata { get; set; }

Metadata regarding this request.

**Property Value**  
---  
**Type** | **Description**  
`[RecognitionMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.RecognitionMetadata)` |   
  
### Model
    
    
    public string Model { get; set; }

Which model to select for the given request. Select the model best suited to your domain to get best results. If a model is not explicitly specified, then we auto-select a model based on the parameters in the RecognitionConfig. <table> <tr> <td><b>Model</b></td> <td><b>Description</b></td> </tr> <tr> <td><code>latest_long</code></td> <td>Best for long form content like media or conversation.</td> </tr> <tr> <td><code>latest_short</code></td> <td>Best for short form content like commands or single shot directed speech.</td> </tr> <tr> <td><code>command_and_search</code></td> <td>Best for short queries such as voice commands or voice search.</td> </tr> <tr> <td><code>phone_call</code></td> <td>Best for audio that originated from a phone call (typically recorded at an 8khz sampling rate).</td> </tr> <tr> <td><code>video</code></td> <td>Best for audio that originated from video or includes multiple speakers. Ideally the audio is recorded at a 16khz or greater sampling rate. This is a premium model that costs more than the standard rate.</td> </tr> <tr> <td><code>default</code></td> <td>Best for audio that is not one of the specific audio models. For example, long-form audio. Ideally the audio is high-fidelity, recorded at a 16khz or greater sampling rate.</td> </tr> <tr> <td><code>medical_conversation</code></td> <td>Best for audio that originated from a conversation between a medical provider and patient.</td> </tr> <tr> <td><code>medical_dictation</code></td> <td>Best for audio that originated from dictation notes by a medical provider.</td> </tr> </table>

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProfanityFilter
    
    
    public bool ProfanityFilter { get; set; }

If set to `true`, the server will attempt to filter out profanities, replacing all but the initial character in each filtered word with asterisks, e.g. "f***". If set to `false` or omitted, profanities won't be filtered out.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SampleRateHertz
    
    
    public int SampleRateHertz { get; set; }

Sample rate in Hertz of the audio data sent in all `RecognitionAudio` messages. Valid values are: 8000-48000. 16000 is optimal. For best results, set the sampling rate of the audio source to 16000 Hz. If that's not possible, use the native sample rate of the audio source (instead of re-sampling). This field is optional for FLAC and WAV audio files, but is required for all other audio formats. For details, see [AudioEncoding][google.cloud.speech.v1p1beta1.RecognitionConfig.AudioEncoding].

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### SpeechContexts
    
    
    public RepeatedField<SpeechContext> SpeechContexts { get; }

Array of [SpeechContext][google.cloud.speech.v1p1beta1.SpeechContext]. A means to provide context to assist the speech recognition. For more information, see [speech adaptation](https://cloud.google.com/speech-to-text/docs/adaptation).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SpeechContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.SpeechContext)` |   
  
### TranscriptNormalization
    
    
    public TranscriptNormalization TranscriptNormalization { get; set; }

Optional. Use transcription normalization to automatically replace parts of the transcript with phrases of your choosing. For StreamingRecognize, this normalization only applies to stable partial transcripts (stability > 0.8) and final transcripts.

**Property Value**  
---  
**Type** | **Description**  
`[TranscriptNormalization](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.TranscriptNormalization)` |   
  
### UseEnhanced
    
    
    public bool UseEnhanced { get; set; }

Set to true to use an enhanced model for speech recognition. If `use_enhanced` is set to true and the `model` field is not set, then an appropriate enhanced model is chosen if an enhanced model exists for the audio.

If `use_enhanced` is true and an enhanced version of the specified model does not exist, then the speech is recognized using the standard version of the specified model.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
