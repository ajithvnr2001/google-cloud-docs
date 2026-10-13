---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult.Types.DetectedObject
title: Vision AI v1 API - Class VideoObjectTrackingPredictionResult.Types.DetectedObject (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:10.533967+00:00
---

# Vision AI v1 API - Class VideoObjectTrackingPredictionResult.Types.DetectedObject (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult.Types.DetectedObject

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vision AI v1 API - Class VideoObjectTrackingPredictionResult.Types.DetectedObject (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class VideoObjectTrackingPredictionResult.Types.DetectedObject : IMessage<VideoObjectTrackingPredictionResult.Types.DetectedObject>, IEquatable<VideoObjectTrackingPredictionResult.Types.DetectedObject>, IDeepCloneable<VideoObjectTrackingPredictionResult.Types.DetectedObject>, IBufferMessage, IMessage

Reference documentation and code samples for the Vision AI v1 API class VideoObjectTrackingPredictionResult.Types.DetectedObject.

Each DetectedObject is one particular identification of an object specified with the AnnotationSpec id and display_name, the bounding box, the associated confidence score and the corresponding track_id.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > VideoObjectTrackingPredictionResult.Types.DetectedObject

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[VideoObjectTrackingPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult.Types)[DetectedObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult.Types.DetectedObject), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[VideoObjectTrackingPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult.Types)[DetectedObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult.Types.DetectedObject), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[VideoObjectTrackingPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult.Types)[DetectedObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult.Types.DetectedObject), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VisionAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1)

## Assembly

Google.Cloud.VisionAI.V1.dll

## Constructors 

### DetectedObject()
    
    
    public DetectedObject()

### DetectedObject(DetectedObject)
    
    
    public DetectedObject(VideoObjectTrackingPredictionResult.Types.DetectedObject other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[VideoObjectTrackingPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult.Types)[DetectedObject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult.Types.DetectedObject)`  
  
  
## Properties 

### BoundingBox
    
    
    public VideoObjectTrackingPredictionResult.Types.BoundingBox BoundingBox { get; set; }

Boundingbox.

**Property Value**  
---  
**Type** | **Description**  
`[VideoObjectTrackingPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult.Types)[BoundingBox](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.VideoObjectTrackingPredictionResult.Types.BoundingBox)` |   
  
### Confidence
    
    
    public float Confidence { get; set; }

The Model's confidence in correction of this identification, higher value means higher confidence.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

The display name of the AnnotationSpec that had been identified.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Id
    
    
    public string Id { get; set; }

The resource ID of the AnnotationSpec that had been identified.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TrackId
    
    
    public long TrackId { get; set; }

The same object may be identified on muitiple frames which are typical adjacent. The set of frames where a particular object has been detected form a track. This track_id can be used to trace down all frames for an detected object.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
