---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CloudConversationDebuggingInfo
title: Dialogflow v3 API - Class CloudConversationDebuggingInfo (3.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:56.383883+00:00
---

# Dialogflow v3 API - Class CloudConversationDebuggingInfo (3.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CloudConversationDebuggingInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dialogflow v3 API - Class CloudConversationDebuggingInfo (3.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.0 (latest)  3.1.0  3.0.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class CloudConversationDebuggingInfo : IMessage<CloudConversationDebuggingInfo>, IEquatable<CloudConversationDebuggingInfo>, IDeepCloneable<CloudConversationDebuggingInfo>, IBufferMessage, IMessage

Reference documentation and code samples for the Dialogflow v3 API class CloudConversationDebuggingInfo.

Cloud conversation info for easier debugging. It will get populated in `StreamingDetectIntentResponse` or `StreamingAnalyzeContentResponse` when the flag `enable_debugging_info` is set to true in corresponding requests.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudConversationDebuggingInfo

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CloudConversationDebuggingInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CloudConversationDebuggingInfo), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CloudConversationDebuggingInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CloudConversationDebuggingInfo), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CloudConversationDebuggingInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CloudConversationDebuggingInfo), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.Cx.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3)

## Assembly

Google.Cloud.Dialogflow.Cx.V3.dll

## Constructors 

### CloudConversationDebuggingInfo()
    
    
    public CloudConversationDebuggingInfo()

### CloudConversationDebuggingInfo(CloudConversationDebuggingInfo)
    
    
    public CloudConversationDebuggingInfo(CloudConversationDebuggingInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CloudConversationDebuggingInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.CloudConversationDebuggingInfo)`  
  
  
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
