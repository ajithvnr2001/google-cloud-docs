---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CloudConversationDebuggingInfo
title: Google Cloud Dialogflow v2 API - Class CloudConversationDebuggingInfo (4.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:58:16.938488+00:00
---

# Google Cloud Dialogflow v2 API - Class CloudConversationDebuggingInfo (4.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CloudConversationDebuggingInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2 API - Class CloudConversationDebuggingInfo (4.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.33.0 (latest)  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public sealed class CloudConversationDebuggingInfo : IMessage<CloudConversationDebuggingInfo>, IEquatable<CloudConversationDebuggingInfo>, IDeepCloneable<CloudConversationDebuggingInfo>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Dialogflow v2 API class CloudConversationDebuggingInfo.

Cloud conversation info for easier debugging. It will get populated in `StreamingDetectIntentResponse` or `StreamingAnalyzeContentResponse` when the flag `enable_debugging_info` is set to true in corresponding requests.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudConversationDebuggingInfo

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CloudConversationDebuggingInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CloudConversationDebuggingInfo), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CloudConversationDebuggingInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CloudConversationDebuggingInfo), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CloudConversationDebuggingInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CloudConversationDebuggingInfo), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2)

## Assembly

Google.Cloud.Dialogflow.V2.dll

## Constructors 

### CloudConversationDebuggingInfo()
    
    
    public CloudConversationDebuggingInfo()

### CloudConversationDebuggingInfo(CloudConversationDebuggingInfo)
    
    
    public CloudConversationDebuggingInfo(CloudConversationDebuggingInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CloudConversationDebuggingInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2/latest/Google.Cloud.Dialogflow.V2.CloudConversationDebuggingInfo)`  
  
  
## Properties 

### AudioDataChunks
    
    
    public int AudioDataChunks { get; set; }

Number of input audio data chunks in streaming requests.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### BargeinEventTriggered
    
    
    public bool BargeinEventTriggered { get; set; }

Whether a barge-in event is triggered in this request.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ClientHalfCloseStreamingTimeOffset
    
    
    public Duration ClientHalfCloseStreamingTimeOffset { get; set; }

Client half close time in terms of API streaming duration.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### ClientHalfCloseTimeOffset
    
    
    public Duration ClientHalfCloseTimeOffset { get; set; }

Client half close time in terms of input audio duration.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### DtmfFinalResultsTimes
    
    
    public RepeatedField<Duration> DtmfFinalResultsTimes { get; }

Time offsets of the DTMF final results relative to the beginning of the stream.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### DtmfPartialResultsTimes
    
    
    public RepeatedField<Duration> DtmfPartialResultsTimes { get; }

Time offsets of the DTMF partial results relative to the beginning of the stream.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### EndpointingTimeout
    
    
    public Duration EndpointingTimeout { get; set; }

Speech endpointing timeout settings for the stream.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### FirstAudioDuration
    
    
    public Duration FirstAudioDuration { get; set; }

Duration of first audio chunk.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### IsInputText
    
    
    public bool IsInputText { get; set; }

Whether the streaming terminates with an injected text query.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### NoSpeechTimeout
    
    
    public Duration NoSpeechTimeout { get; set; }

No speech timeout settings for the stream.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### PartialResponses
    
    
    public int PartialResponses { get; set; }

Total number of partial responses.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ResultEndTimeOffset
    
    
    public Duration ResultEndTimeOffset { get; set; }

Time offset of the end of speech utterance relative to the beginning of the first audio chunk.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### SingleUtterance
    
    
    public bool SingleUtterance { get; set; }

Whether client used single utterance mode.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SingleUtteranceEndTimeOffset
    
    
    public Duration SingleUtteranceEndTimeOffset { get; set; }

Time offset of the end-of-single-utterance signal relative to the beginning of the stream.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### SpeakerIdPassiveLatencyMsOffset
    
    
    public int SpeakerIdPassiveLatencyMsOffset { get; set; }

Time offset of Speaker ID stream close time relative to the Speech stream close time in milliseconds. Only meaningful for conversations involving passive verification.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### SpeechFinalResultsEndTimes
    
    
    public RepeatedField<Duration> SpeechFinalResultsEndTimes { get; }

Time offsets of the speech final results (is_final=true) relative to the beginning of the stream.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### SpeechPartialResultsEndTimes
    
    
    public RepeatedField<Duration> SpeechPartialResultsEndTimes { get; }

Time offsets of the speech partial results relative to the beginning of the stream.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### SpeechSingleUtterance
    
    
    public bool SpeechSingleUtterance { get; set; }

Whether speech uses single utterance mode.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
