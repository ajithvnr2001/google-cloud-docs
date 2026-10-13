---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Params.VideoClassificationPredictionParams
title: Vertex AI v1beta1 API - Class VideoClassificationPredictionParams (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:29:22.948051+00:00
---

# Vertex AI v1beta1 API - Class VideoClassificationPredictionParams (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Params.VideoClassificationPredictionParams

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class VideoClassificationPredictionParams (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class VideoClassificationPredictionParams : IMessage<VideoClassificationPredictionParams>, IEquatable<VideoClassificationPredictionParams>, IDeepCloneable<VideoClassificationPredictionParams>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class VideoClassificationPredictionParams.

Prediction model parameters for Video Classification.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > VideoClassificationPredictionParams

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[VideoClassificationPredictionParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Params.VideoClassificationPredictionParams), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[VideoClassificationPredictionParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Params.VideoClassificationPredictionParams), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[VideoClassificationPredictionParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Params.VideoClassificationPredictionParams), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Params](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Params)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### VideoClassificationPredictionParams()
    
    
    public VideoClassificationPredictionParams()

### VideoClassificationPredictionParams(VideoClassificationPredictionParams)
    
    
    public VideoClassificationPredictionParams(VideoClassificationPredictionParams other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[VideoClassificationPredictionParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Params.VideoClassificationPredictionParams)`  
  
  
## Properties 

### ConfidenceThreshold
    
    
    public float ConfidenceThreshold { get; set; }

The Model only returns predictions with at least this confidence score. Default value is 0.0

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### MaxPredictions
    
    
    public int MaxPredictions { get; set; }

The Model only returns up to that many top, by confidence score, predictions per instance. If this number is very high, the Model may return fewer predictions. Default value is 10,000.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### OneSecIntervalClassification
    
    
    public bool OneSecIntervalClassification { get; set; }

Set to true to request classification for a video at one-second intervals. Vertex AI returns labels and their confidence scores for each second of the entire time segment of the video that user specified in the input WARNING: Model evaluation is not done for this classification type, the quality of it depends on the training data, but there are no metrics provided to describe that quality. Default value is false

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SegmentClassification
    
    
    public bool SegmentClassification { get; set; }

Set to true to request segment-level classification. Vertex AI returns labels and their confidence scores for the entire time segment of the video that user specified in the input instance. Default value is true

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ShotClassification
    
    
    public bool ShotClassification { get; set; }

Set to true to request shot-level classification. Vertex AI determines the boundaries for each camera shot in the entire time segment of the video that user specified in the input instance. Vertex AI then returns labels and their confidence scores for each detected shot, along with the start and end time of the shot. WARNING: Model evaluation is not done for this classification type, the quality of it depends on the training data, but there are no metrics provided to describe that quality. Default value is false

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
