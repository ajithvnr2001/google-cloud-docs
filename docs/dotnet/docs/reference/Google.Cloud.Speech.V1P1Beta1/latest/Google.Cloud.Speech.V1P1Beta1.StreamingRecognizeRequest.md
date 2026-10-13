---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.StreamingRecognizeRequest
title: Google Cloud Speech v1p1beta1 API - Class StreamingRecognizeRequest (3.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:34.098656+00:00
---

# Google Cloud Speech v1p1beta1 API - Class StreamingRecognizeRequest (3.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.StreamingRecognizeRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Speech v1p1beta1 API - Class StreamingRecognizeRequest (3.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta10 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.StreamingRecognizeRequest)
  * [ 3.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/3.0.0-beta09/Google.Cloud.Speech.V1P1Beta1.StreamingRecognizeRequest)
  * [ 2.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/2.0.0-beta09/Google.Cloud.Speech.V1P1Beta1.StreamingRecognizeRequest)


    
    
    public sealed class StreamingRecognizeRequest : IMessage<StreamingRecognizeRequest>, IEquatable<StreamingRecognizeRequest>, IDeepCloneable<StreamingRecognizeRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Speech v1p1beta1 API class StreamingRecognizeRequest.

The top-level message sent by the client for the `StreamingRecognize` method. Multiple `StreamingRecognizeRequest` messages are sent. The first message must contain a `streaming_config` message and must not contain `audio_content`. All subsequent messages must contain `audio_content` and must not contain a `streaming_config` message.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > StreamingRecognizeRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[StreamingRecognizeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.StreamingRecognizeRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[StreamingRecognizeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.StreamingRecognizeRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[StreamingRecognizeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.StreamingRecognizeRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Speech.V1P1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1)

## Assembly

Google.Cloud.Speech.V1P1Beta1.dll

## Constructors 

### StreamingRecognizeRequest()
    
    
    public StreamingRecognizeRequest()

### StreamingRecognizeRequest(StreamingRecognizeRequest)
    
    
    public StreamingRecognizeRequest(StreamingRecognizeRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[StreamingRecognizeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.StreamingRecognizeRequest)`  
  
  
## Properties 

### AudioContent
    
    
    public ByteString AudioContent { get; set; }

The audio data to be recognized. Sequential chunks of audio data are sent in sequential `StreamingRecognizeRequest` messages. The first `StreamingRecognizeRequest` message must not contain `audio_content` data and all subsequent `StreamingRecognizeRequest` messages must contain `audio_content` data. The audio bytes must be encoded as specified in `RecognitionConfig`. Note: as with all bytes fields, proto buffers use a pure binary representation (not base64). See [content limits](https://cloud.google.com/speech-to-text/quotas#content).

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### HasAudioContent
    
    
    public bool HasAudioContent { get; }

Gets whether the "audio_content" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### StreamingConfig
    
    
    public StreamingRecognitionConfig StreamingConfig { get; set; }

Provides information to the recognizer that specifies how to process the request. The first `StreamingRecognizeRequest` message must contain a `streaming_config` message.

**Property Value**  
---  
**Type** | **Description**  
`[StreamingRecognitionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.StreamingRecognitionConfig)` |   
  
### StreamingRequestCase
    
    
    public StreamingRecognizeRequest.StreamingRequestOneofCase StreamingRequestCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[StreamingRecognizeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.StreamingRecognizeRequest)[StreamingRequestOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.StreamingRecognizeRequest.StreamingRequestOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
