---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.VideoContext
title: Google Cloud Video Intelligence v1 API - Class VideoContext (3.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:57.925412+00:00
---

# Google Cloud Video Intelligence v1 API - Class VideoContext (3.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.VideoContext

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Video Intelligence v1 API - Class VideoContext (3.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.VideoContext)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/3.4.0/Google.Cloud.VideoIntelligence.V1.VideoContext)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/3.3.0/Google.Cloud.VideoIntelligence.V1.VideoContext)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/3.2.0/Google.Cloud.VideoIntelligence.V1.VideoContext)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/3.1.0/Google.Cloud.VideoIntelligence.V1.VideoContext)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/3.0.0/Google.Cloud.VideoIntelligence.V1.VideoContext)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/2.3.0/Google.Cloud.VideoIntelligence.V1.VideoContext)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/2.2.0/Google.Cloud.VideoIntelligence.V1.VideoContext)


    
    
    public sealed class VideoContext : IMessage<VideoContext>, IEquatable<VideoContext>, IDeepCloneable<VideoContext>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Video Intelligence v1 API class VideoContext.

Video context and/or feature-specific parameters.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > VideoContext

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[VideoContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.VideoContext), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[VideoContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.VideoContext), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[VideoContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.VideoContext), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VideoIntelligence.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1)

## Assembly

Google.Cloud.VideoIntelligence.V1.dll

## Constructors 

### VideoContext()
    
    
    public VideoContext()

### VideoContext(VideoContext)
    
    
    public VideoContext(VideoContext other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[VideoContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.VideoContext)`  
  
  
## Properties 

### ExplicitContentDetectionConfig
    
    
    public ExplicitContentDetectionConfig ExplicitContentDetectionConfig { get; set; }

Config for EXPLICIT_CONTENT_DETECTION.

**Property Value**  
---  
**Type** | **Description**  
`[ExplicitContentDetectionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.ExplicitContentDetectionConfig)` |   
  
### FaceDetectionConfig
    
    
    public FaceDetectionConfig FaceDetectionConfig { get; set; }

Config for FACE_DETECTION.

**Property Value**  
---  
**Type** | **Description**  
`[FaceDetectionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.FaceDetectionConfig)` |   
  
### LabelDetectionConfig
    
    
    public LabelDetectionConfig LabelDetectionConfig { get; set; }

Config for LABEL_DETECTION.

**Property Value**  
---  
**Type** | **Description**  
`[LabelDetectionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.LabelDetectionConfig)` |   
  
### ObjectTrackingConfig
    
    
    public ObjectTrackingConfig ObjectTrackingConfig { get; set; }

Config for OBJECT_TRACKING.

**Property Value**  
---  
**Type** | **Description**  
`[ObjectTrackingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.ObjectTrackingConfig)` |   
  
### PersonDetectionConfig
    
    
    public PersonDetectionConfig PersonDetectionConfig { get; set; }

Config for PERSON_DETECTION.

**Property Value**  
---  
**Type** | **Description**  
`[PersonDetectionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.PersonDetectionConfig)` |   
  
### Segments
    
    
    public RepeatedField<VideoSegment> Segments { get; }

Video segments to annotate. The segments may overlap and are not required to be contiguous or span the whole video. If unspecified, each video is treated as a single segment.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[VideoSegment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.VideoSegment)` |   
  
### ShotChangeDetectionConfig
    
    
    public ShotChangeDetectionConfig ShotChangeDetectionConfig { get; set; }

Config for SHOT_CHANGE_DETECTION.

**Property Value**  
---  
**Type** | **Description**  
`[ShotChangeDetectionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.ShotChangeDetectionConfig)` |   
  
### SpeechTranscriptionConfig
    
    
    public SpeechTranscriptionConfig SpeechTranscriptionConfig { get; set; }

Config for SPEECH_TRANSCRIPTION.

**Property Value**  
---  
**Type** | **Description**  
`[SpeechTranscriptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.SpeechTranscriptionConfig)` |   
  
### TextDetectionConfig
    
    
    public TextDetectionConfig TextDetectionConfig { get; set; }

Config for TEXT_DETECTION.

**Property Value**  
---  
**Type** | **Description**  
`[TextDetectionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VideoIntelligence.V1/latest/Google.Cloud.VideoIntelligence.V1.TextDetectionConfig)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
