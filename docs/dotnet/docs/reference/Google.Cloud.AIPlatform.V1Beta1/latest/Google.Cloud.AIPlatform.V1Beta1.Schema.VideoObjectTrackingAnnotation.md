---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.VideoObjectTrackingAnnotation
title: Vertex AI v1beta1 API - Class VideoObjectTrackingAnnotation (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:29:15.993771+00:00
---

# Vertex AI v1beta1 API - Class VideoObjectTrackingAnnotation (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.VideoObjectTrackingAnnotation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class VideoObjectTrackingAnnotation (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class VideoObjectTrackingAnnotation : IMessage<VideoObjectTrackingAnnotation>, IEquatable<VideoObjectTrackingAnnotation>, IDeepCloneable<VideoObjectTrackingAnnotation>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class VideoObjectTrackingAnnotation.

Annotation details specific to video object tracking.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > VideoObjectTrackingAnnotation

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[VideoObjectTrackingAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.VideoObjectTrackingAnnotation), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[VideoObjectTrackingAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.VideoObjectTrackingAnnotation), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[VideoObjectTrackingAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.VideoObjectTrackingAnnotation), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1.Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### VideoObjectTrackingAnnotation()
    
    
    public VideoObjectTrackingAnnotation()

### VideoObjectTrackingAnnotation(VideoObjectTrackingAnnotation)
    
    
    public VideoObjectTrackingAnnotation(VideoObjectTrackingAnnotation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[VideoObjectTrackingAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.VideoObjectTrackingAnnotation)`  
  
  
## Properties 

### AnnotationSpecId
    
    
    public string AnnotationSpecId { get; set; }

The resource Id of the AnnotationSpec that this Annotation pertains to.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

The display name of the AnnotationSpec that this Annotation pertains to.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### InstanceId
    
    
    public long InstanceId { get; set; }

The instance of the object, expressed as a positive integer. Used to track the same object across different frames.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### TimeOffset
    
    
    public Duration TimeOffset { get; set; }

A time (frame) of a video to which this annotation pertains. Represented as the duration since the video's start.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### XMax
    
    
    public double XMax { get; set; }

The rightmost coordinate of the bounding box.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### XMin
    
    
    public double XMin { get; set; }

The leftmost coordinate of the bounding box.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### YMax
    
    
    public double YMax { get; set; }

The bottommost coordinate of the bounding box.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### YMin
    
    
    public double YMin { get; set; }

The topmost coordinate of the bounding box.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
