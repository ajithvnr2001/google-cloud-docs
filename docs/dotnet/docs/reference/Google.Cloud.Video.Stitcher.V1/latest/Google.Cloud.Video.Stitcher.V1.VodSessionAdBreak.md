---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSessionAdBreak
title: Video Stitcher v1 API - Class VodSessionAdBreak (3.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:03.608868+00:00
---

# Video Stitcher v1 API - Class VodSessionAdBreak (3.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSessionAdBreak

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Video Stitcher v1 API - Class VodSessionAdBreak (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSessionAdBreak)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.3.0/Google.Cloud.Video.Stitcher.V1.VodSessionAdBreak)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.2.0/Google.Cloud.Video.Stitcher.V1.VodSessionAdBreak)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.1.0/Google.Cloud.Video.Stitcher.V1.VodSessionAdBreak)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.0.0/Google.Cloud.Video.Stitcher.V1.VodSessionAdBreak)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/2.0.0/Google.Cloud.Video.Stitcher.V1.VodSessionAdBreak)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/1.1.0/Google.Cloud.Video.Stitcher.V1.VodSessionAdBreak)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/1.0.0/Google.Cloud.Video.Stitcher.V1.VodSessionAdBreak)


    
    
    public sealed class VodSessionAdBreak : IMessage<VodSessionAdBreak>, IEquatable<VodSessionAdBreak>, IDeepCloneable<VodSessionAdBreak>, IBufferMessage, IMessage

Reference documentation and code samples for the Video Stitcher v1 API class VodSessionAdBreak.

Metadata for an inserted ad break.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > VodSessionAdBreak

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[VodSessionAdBreak](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSessionAdBreak), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[VodSessionAdBreak](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSessionAdBreak), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[VodSessionAdBreak](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSessionAdBreak), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1)

## Assembly

Google.Cloud.Video.Stitcher.V1.dll

## Constructors 

### VodSessionAdBreak()
    
    
    public VodSessionAdBreak()

### VodSessionAdBreak(VodSessionAdBreak)
    
    
    public VodSessionAdBreak(VodSessionAdBreak other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[VodSessionAdBreak](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSessionAdBreak)`  
  
  
## Properties 

### Ads
    
    
    public RepeatedField<VodSessionAd> Ads { get; }

Ordered list of ads stitched into the ad break.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[VodSessionAd](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodSessionAd)` |   
  
### EndTimeOffset
    
    
    public Duration EndTimeOffset { get; set; }

Ad break end time in seconds relative to the start of the VOD asset.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### ProgressEvents
    
    
    public RepeatedField<ProgressEvent> ProgressEvents { get; }

List of events that are expected to be triggered, ordered by time.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ProgressEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.ProgressEvent)` |   
  
### StartTimeOffset
    
    
    public Duration StartTimeOffset { get; set; }

Ad break start time in seconds relative to the start of the VOD asset.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
