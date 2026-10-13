---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.LongRunningRecognizeMetadata
title: Google Cloud Speech v1p1beta1 API - Class LongRunningRecognizeMetadata (3.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:59.487167+00:00
---

# Google Cloud Speech v1p1beta1 API - Class LongRunningRecognizeMetadata (3.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.LongRunningRecognizeMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Speech v1p1beta1 API - Class LongRunningRecognizeMetadata (3.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta10 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.LongRunningRecognizeMetadata)
  * [ 3.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/3.0.0-beta09/Google.Cloud.Speech.V1P1Beta1.LongRunningRecognizeMetadata)
  * [ 2.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/2.0.0-beta09/Google.Cloud.Speech.V1P1Beta1.LongRunningRecognizeMetadata)


    
    
    public sealed class LongRunningRecognizeMetadata : IMessage<LongRunningRecognizeMetadata>, IEquatable<LongRunningRecognizeMetadata>, IDeepCloneable<LongRunningRecognizeMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Speech v1p1beta1 API class LongRunningRecognizeMetadata.

Describes the progress of a long-running `LongRunningRecognize` call. It is included in the `metadata` field of the `Operation` returned by the `GetOperation` call of the `google::longrunning::Operations` service.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > LongRunningRecognizeMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[LongRunningRecognizeMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.LongRunningRecognizeMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[LongRunningRecognizeMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.LongRunningRecognizeMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[LongRunningRecognizeMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.LongRunningRecognizeMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Speech.V1P1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1)

## Assembly

Google.Cloud.Speech.V1P1Beta1.dll

## Constructors 

### LongRunningRecognizeMetadata()
    
    
    public LongRunningRecognizeMetadata()

### LongRunningRecognizeMetadata(LongRunningRecognizeMetadata)
    
    
    public LongRunningRecognizeMetadata(LongRunningRecognizeMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[LongRunningRecognizeMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.LongRunningRecognizeMetadata)`  
  
  
## Properties 

### LastUpdateTime
    
    
    public Timestamp LastUpdateTime { get; set; }

Time of the most recent processing update.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### OutputConfig
    
    
    public TranscriptOutputConfig OutputConfig { get; set; }

Output only. A copy of the TranscriptOutputConfig if it was set in the request.

**Property Value**  
---  
**Type** | **Description**  
`[TranscriptOutputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1P1Beta1/latest/Google.Cloud.Speech.V1P1Beta1.TranscriptOutputConfig)` |   
  
### ProgressPercent
    
    
    public int ProgressPercent { get; set; }

Approximate percentage of audio processed thus far. Guaranteed to be 100 when the audio is fully processed and the results are available.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### StartTime
    
    
    public Timestamp StartTime { get; set; }

Time when the request was received.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Uri
    
    
    public string Uri { get; set; }

Output only. The URI of the audio file being transcribed. Empty if the audio was sent as byte content.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
