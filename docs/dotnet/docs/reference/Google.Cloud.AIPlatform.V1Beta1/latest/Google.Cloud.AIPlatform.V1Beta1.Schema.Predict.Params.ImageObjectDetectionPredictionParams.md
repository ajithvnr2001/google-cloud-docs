---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Params.ImageObjectDetectionPredictionParams
title: Vertex AI v1beta1 API - Class ImageObjectDetectionPredictionParams (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:29:20.915058+00:00
---

# Vertex AI v1beta1 API - Class ImageObjectDetectionPredictionParams (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Params.ImageObjectDetectionPredictionParams

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ImageObjectDetectionPredictionParams (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class ImageObjectDetectionPredictionParams : IMessage<ImageObjectDetectionPredictionParams>, IEquatable<ImageObjectDetectionPredictionParams>, IDeepCloneable<ImageObjectDetectionPredictionParams>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class ImageObjectDetectionPredictionParams.

Prediction model parameters for Image Object Detection.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ImageObjectDetectionPredictionParams

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ImageObjectDetectionPredictionParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Params.ImageObjectDetectionPredictionParams), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ImageObjectDetectionPredictionParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Params.ImageObjectDetectionPredictionParams), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ImageObjectDetectionPredictionParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Params.ImageObjectDetectionPredictionParams), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Params](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Params)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### ImageObjectDetectionPredictionParams()
    
    
    public ImageObjectDetectionPredictionParams()

### ImageObjectDetectionPredictionParams(ImageObjectDetectionPredictionParams)
    
    
    public ImageObjectDetectionPredictionParams(ImageObjectDetectionPredictionParams other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ImageObjectDetectionPredictionParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Params.ImageObjectDetectionPredictionParams)`  
  
  
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

The Model only returns up to that many top, by confidence score, predictions per instance. Note that number of returned predictions is also limited by metadata's predictionsLimit. Default value is 10.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
