---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.ImageSegmentationPredictionResult
title: Vertex AI v1beta1 API - Class ImageSegmentationPredictionResult (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:29:26.364818+00:00
---

# Vertex AI v1beta1 API - Class ImageSegmentationPredictionResult (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.ImageSegmentationPredictionResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ImageSegmentationPredictionResult (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class ImageSegmentationPredictionResult : IMessage<ImageSegmentationPredictionResult>, IEquatable<ImageSegmentationPredictionResult>, IDeepCloneable<ImageSegmentationPredictionResult>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class ImageSegmentationPredictionResult.

Prediction output format for Image Segmentation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ImageSegmentationPredictionResult

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ImageSegmentationPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.ImageSegmentationPredictionResult), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ImageSegmentationPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.ImageSegmentationPredictionResult), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ImageSegmentationPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.ImageSegmentationPredictionResult), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### ImageSegmentationPredictionResult()
    
    
    public ImageSegmentationPredictionResult()

### ImageSegmentationPredictionResult(ImageSegmentationPredictionResult)
    
    
    public ImageSegmentationPredictionResult(ImageSegmentationPredictionResult other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ImageSegmentationPredictionResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Prediction.ImageSegmentationPredictionResult)`  
  
  
## Properties 

### CategoryMask
    
    
    public string CategoryMask { get; set; }

A PNG image where each pixel in the mask represents the category in which the pixel in the original image was predicted to belong to. The size of this image will be the same as the original image. The mapping between the AnntoationSpec and the color can be found in model's metadata. The model will choose the most likely category and if none of the categories reach the confidence threshold, the pixel will be marked as background.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ConfidenceMask
    
    
    public string ConfidenceMask { get; set; }

A one channel image which is encoded as an 8bit lossless PNG. The size of the image will be the same as the original image. For a specific pixel, darker color means less confidence in correctness of the cateogry in the categoryMask for the corresponding pixel. Black means no confidence and white means complete confidence.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
