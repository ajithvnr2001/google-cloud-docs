---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.ImageObjectDetectionPredictionResult
title: Vertex AI v1beta1 API - Class ImageObjectDetectionPredictionResult (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:29:24.644759+00:00
---

# Vertex AI v1beta1 API - Class ImageObjectDetectionPredictionResult (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.ImageObjectDetectionPredictionResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ImageObjectDetectionPredictionResult (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class ImageObjectDetectionPredictionResult : IMessage<ImageObjectDetectionPredictionResult>, IEquatable<ImageObjectDetectionPredictionResult>, IDeepCloneable<ImageObjectDetectionPredictionResult>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class ImageObjectDetectionPredictionResult.

Prediction output format for Image Object Detection.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ImageObjectDetectionPredictionResult

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ImageObjectDetectionPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.ImageObjectDetectionPredictionResult), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ImageObjectDetectionPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.ImageObjectDetectionPredictionResult), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ImageObjectDetectionPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.ImageObjectDetectionPredictionResult), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### ImageObjectDetectionPredictionResult()
    
    
    public ImageObjectDetectionPredictionResult()

### ImageObjectDetectionPredictionResult(ImageObjectDetectionPredictionResult)
    
    
    public ImageObjectDetectionPredictionResult(ImageObjectDetectionPredictionResult other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ImageObjectDetectionPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.ImageObjectDetectionPredictionResult)`  
  
  
## Properties 

### Bboxes
    
    
    public RepeatedField<ListValue> Bboxes { get; }

Bounding boxes, i.e. the rectangles over the image, that pinpoint the found AnnotationSpecs. Given in order that matches the IDs. Each bounding box is an array of 4 numbers `xMin`, `xMax`, `yMin`, and `yMax`, which represent the extremal coordinates of the box. They are relative to the image size, and the point 0,0 is in the top left of the image.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ListValue](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.ListValue.html)` |   
  
### Confidences
    
    
    public RepeatedField<float> Confidences { get; }

The Model's confidences in correctness of the predicted IDs, higher value means higher confidence. Order matches the Ids.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### DisplayNames
    
    
    public RepeatedField<string> DisplayNames { get; }

The display names of the AnnotationSpecs that had been identified, order matches the IDs.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Ids
    
    
    public RepeatedField<long> Ids { get; }

The resource IDs of the AnnotationSpecs that had been identified, ordered by the confidence score descendingly.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
