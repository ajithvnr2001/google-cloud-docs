---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingRecognitionResult
title: Google Cloud Dialogflow v2beta1 API - Class StreamingRecognitionResult (1.0.0-beta33) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:10.857396+00:00
---

# Google Cloud Dialogflow v2beta1 API - Class StreamingRecognitionResult (1.0.0-beta33)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingRecognitionResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2beta1 API - Class StreamingRecognitionResult (1.0.0-beta33) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta33 (latest)  1.0.0-beta32 
    
    
    public sealed class StreamingRecognitionResult : IMessage<StreamingRecognitionResult>, IEquatable<StreamingRecognitionResult>, IDeepCloneable<StreamingRecognitionResult>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2beta1 API class StreamingRecognitionResult.

Contains a speech recognition result corresponding to a portion of the audio that is currently being processed or an indication that this is the end of the single requested utterance.

While end-user audio is being processed, Dialogflow sends a series of results. Each result may contain a `transcript` value. A transcript represents a portion of the utterance. While the recognizer is processing audio, transcript values may be interim values or finalized values. Once a transcript is finalized, the `is_final` value is set to true and processing continues for the next transcript.

If `StreamingDetectIntentRequest.query_input.audio_config.single_utterance` was true, and the recognizer has completed processing audio, the `message_type` value is set to `END_OF_SINGLE_UTTERANCE and the following (last) result contains the last finalized transcript.

The complete end-user utterance is determined by concatenating the finalized transcript values received for the series of results.

In the following example, single utterance is enabled. In the case where single utterance is not enabled, result 8 would not occur.
    
    
    Num | transcript               | message_type            | is_final
    --- | ------------------------ | ----------------------- | --------
    1   | "tube"                   | TRANSCRIPT              | false
    2   | "to be a"                | TRANSCRIPT              | false
    3   | "to be"                  | TRANSCRIPT              | false
    4   | "to be or not to be"     | TRANSCRIPT              | true
    5   | "that's"                 | TRANSCRIPT              | false
    6   | "that is                 | TRANSCRIPT              | false
    7   | " that is the question"  | TRANSCRIPT              | true
    8   | unset                    | END_OF_SINGLE_UTTERANCE | unset
    9   | ". Whether 'tis nobler"  | TRANSCRIPT              | true
    10  | " in the mind"           | TRANSCRIPT              | false
    11  | " in the mind to suffer" | TRANSCRIPT              | true
    

Concatenating the finalized transcripts with `is_final` set to true, the complete utterance becomes "to be or not to be that is the question".

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > StreamingRecognitionResult

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[StreamingRecognitionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingRecognitionResult), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[StreamingRecognitionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingRecognitionResult), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[StreamingRecognitionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingRecognitionResult), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1)

## Assembly

Google.Cloud.Dialogflow.V2Beta1.dll

## Constructors 

### StreamingRecognitionResult()
    
    
    public StreamingRecognitionResult()

### StreamingRecognitionResult(StreamingRecognitionResult)
    
    
    public StreamingRecognitionResult(StreamingRecognitionResult other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[StreamingRecognitionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingRecognitionResult)`  
  
  
## Properties 

### Confidence
    
    
    public float Confidence { get; set; }

The Speech confidence between 0.0 and 1.0 for the current portion of audio. A higher number indicates an estimated greater likelihood that the recognized words are correct. The default of 0.0 is a sentinel value indicating that confidence was not set.

This field is typically only provided if `is_final` is true and you should not rely on it being accurate or even set.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### DtmfDigits
    
    
    public TelephonyDtmfEvents DtmfDigits { get; set; }

DTMF digits. Populated if and only if `message_type` = `DTMF_DIGITS`.

**Property Value**  
---  
**Type** | **Description**  
`[TelephonyDtmfEvents](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.TelephonyDtmfEvents)` |   
  
### IsFinal
    
    
    public bool IsFinal { get; set; }

If `false`, the `StreamingRecognitionResult` represents an interim result that may change. If `true`, the recognizer will not return any further hypotheses about this piece of the audio. May only be populated for `message_type` = `TRANSCRIPT`.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### LanguageCode
    
    
    public string LanguageCode { get; set; }

Detected language code for the transcript.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MessageType
    
    
    public StreamingRecognitionResult.Types.MessageType MessageType { get; set; }

Type of the result message.

**Property Value**  
---  
**Type** | **Description**  
`[StreamingRecognitionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingRecognitionResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingRecognitionResult.Types)[MessageType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.StreamingRecognitionResult.Types.MessageType)` |   
  
### SpeechEndOffset
    
    
    public Duration SpeechEndOffset { get; set; }

Time offset of the end of this Speech recognition result relative to the beginning of the audio. Only populated for `message_type` = `TRANSCRIPT`.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### SpeechWordInfo
    
    
    public RepeatedField<SpeechWordInfo> SpeechWordInfo { get; }

Word-specific information for the words recognized by Speech in [transcript][google.cloud.dialogflow.v2beta1.StreamingRecognitionResult.transcript]. Populated if and only if `message_type` = `TRANSCRIPT` and [InputAudioConfig.enable_word_info] is set.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SpeechWordInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SpeechWordInfo)` |   
  
### Stability
    
    
    public float Stability { get; set; }

An estimate of the likelihood that the speech recognizer will not change its guess about this interim recognition result:

  * If the value is unspecified or 0.0, Dialogflow didn't compute the stability. In particular, Dialogflow will only provide stability for `TRANSCRIPT` results with `is_final = false`.
  * Otherwise, the value is in (0.0, 1.0] where 0.0 means completely unstable and 1.0 means completely stable.



**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### Transcript
    
    
    public string Transcript { get; set; }

Transcript text representing the words that the user spoke. Populated if and only if `message_type` = `TRANSCRIPT`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
