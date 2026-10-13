---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.VideoClassificationPredictionResult
title: Vertex AI v1beta1 API - Class VideoClassificationPredictionResult (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:29:27.601356+00:00
---

# Vertex AI v1beta1 API - Class VideoClassificationPredictionResult (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.VideoClassificationPredictionResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class VideoClassificationPredictionResult (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class VideoClassificationPredictionResult : IMessage<VideoClassificationPredictionResult>, IEquatable<VideoClassificationPredictionResult>, IDeepCloneable<VideoClassificationPredictionResult>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class VideoClassificationPredictionResult.

Prediction output format for Video Classification.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > VideoClassificationPredictionResult

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[VideoClassificationPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.VideoClassificationPredictionResult), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[VideoClassificationPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.VideoClassificationPredictionResult), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[VideoClassificationPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.VideoClassificationPredictionResult), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### VideoClassificationPredictionResult()
    
    
    public VideoClassificationPredictionResult()

### VideoClassificationPredictionResult(VideoClassificationPredictionResult)
    
    
    public VideoClassificationPredictionResult(VideoClassificationPredictionResult other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[VideoClassificationPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.VideoClassificationPredictionResult)`  
  
  
## Properties 

### Confidence
    
    
    public float? Confidence { get; set; }

The Model's confidence in correction of this prediction, higher value means higher confidence.

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
  
### TimeSegmentEnd
    
    
    public Duration TimeSegmentEnd { get; set; }

The end, exclusive, of the video's time segment in which the AnnotationSpec has been identified. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with "s" appended at the end. Note that for 'segment-classification' prediction type, this equals the original 'timeSegmentEnd' from the input instance, for other types it is the end of a shot or a 1 second interval respectively.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### TimeSegmentStart
    
    
    public Duration TimeSegmentStart { get; set; }

The beginning, inclusive, of the video's time segment in which the AnnotationSpec has been identified. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with "s" appended at the end. Note that for 'segment-classification' prediction type, this equals the original 'timeSegmentStart' from the input instance, for other types it is the start of a shot or a 1 second interval respectively.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### Type
    
    
    public string Type { get; set; }

The type of the prediction. The requested types can be configured via parameters. This will be one of

  * segment-classification
  * shot-classification
  * one-sec-interval-classification



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
