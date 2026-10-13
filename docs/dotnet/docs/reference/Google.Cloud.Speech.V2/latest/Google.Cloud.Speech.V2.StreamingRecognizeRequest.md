---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.StreamingRecognizeRequest
title: Cloud Speech-to-Text v2 API - Class StreamingRecognizeRequest (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:49:30.041114+00:00
---

# Cloud Speech-to-Text v2 API - Class StreamingRecognizeRequest (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.StreamingRecognizeRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Speech-to-Text v2 API - Class StreamingRecognizeRequest (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.StreamingRecognizeRequest)
  * [ 1.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.7.0/Google.Cloud.Speech.V2.StreamingRecognizeRequest)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.6.0/Google.Cloud.Speech.V2.StreamingRecognizeRequest)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.5.0/Google.Cloud.Speech.V2.StreamingRecognizeRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.4.0/Google.Cloud.Speech.V2.StreamingRecognizeRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.3.0/Google.Cloud.Speech.V2.StreamingRecognizeRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.2.0/Google.Cloud.Speech.V2.StreamingRecognizeRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.1.0/Google.Cloud.Speech.V2.StreamingRecognizeRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/1.0.0/Google.Cloud.Speech.V2.StreamingRecognizeRequest)


    
    
    public sealed class StreamingRecognizeRequest : IMessage<StreamingRecognizeRequest>, IEquatable<StreamingRecognizeRequest>, IDeepCloneable<StreamingRecognizeRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Speech-to-Text v2 API class StreamingRecognizeRequest.

Request message for the [StreamingRecognize][google.cloud.speech.v2.Speech.StreamingRecognize] method. Multiple [StreamingRecognizeRequest][google.cloud.speech.v2.StreamingRecognizeRequest] messages are sent in one call.

If the [Recognizer][google.cloud.speech.v2.Recognizer] referenced by [recognizer][google.cloud.speech.v2.StreamingRecognizeRequest.recognizer] contains a fully specified request configuration then the stream may only contain messages with only [audio][google.cloud.speech.v2.StreamingRecognizeRequest.audio] set.

Otherwise the first message must contain a [recognizer][google.cloud.speech.v2.StreamingRecognizeRequest.recognizer] and a [streaming_config][google.cloud.speech.v2.StreamingRecognizeRequest.streaming_config] message that together fully specify the request configuration and must not contain [audio][google.cloud.speech.v2.StreamingRecognizeRequest.audio]. All subsequent messages must only have [audio][google.cloud.speech.v2.StreamingRecognizeRequest.audio] set.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > StreamingRecognizeRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[StreamingRecognizeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.StreamingRecognizeRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[StreamingRecognizeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.StreamingRecognizeRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[StreamingRecognizeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.StreamingRecognizeRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Speech.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2)

## Assembly

Google.Cloud.Speech.V2.dll

## Constructors 

### StreamingRecognizeRequest()
    
    
    public StreamingRecognizeRequest()

### StreamingRecognizeRequest(StreamingRecognizeRequest)
    
    
    public StreamingRecognizeRequest(StreamingRecognizeRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[StreamingRecognizeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.StreamingRecognizeRequest)`  
  
  
## Properties 

### Audio
    
    
    public ByteString Audio { get; set; }

Inline audio bytes to be Recognized. Maximum size for this field is 15 KB per request.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### HasAudio
    
    
    public bool HasAudio { get; }

Gets whether the "audio" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Recognizer
    
    
    public string Recognizer { get; set; }

Required. The name of the Recognizer to use during recognition. The expected format is `projects/{project}/locations/{location}/recognizers/{recognizer}`. The {recognizer} segment may be set to `_` to use an empty implicit Recognizer.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RecognizerAsRecognizerName
    
    
    public RecognizerName RecognizerAsRecognizerName { get; set; }

[RecognizerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.RecognizerName)-typed view over the [Recognizer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.StreamingRecognizeRequest#Google_Cloud_Speech_V2_StreamingRecognizeRequest_Recognizer) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[RecognizerName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.RecognizerName)` |   
  
### StreamingConfig
    
    
    public StreamingRecognitionConfig StreamingConfig { get; set; }

StreamingRecognitionConfig to be used in this recognition attempt. If provided, it will override the default RecognitionConfig stored in the Recognizer.

**Property Value**  
---  
**Type** | **Description**  
`[StreamingRecognitionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.StreamingRecognitionConfig)` |   
  
### StreamingRequestCase
    
    
    public StreamingRecognizeRequest.StreamingRequestOneofCase StreamingRequestCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[StreamingRecognizeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.StreamingRecognizeRequest)[StreamingRequestOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V2/latest/Google.Cloud.Speech.V2.StreamingRecognizeRequest.StreamingRequestOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
