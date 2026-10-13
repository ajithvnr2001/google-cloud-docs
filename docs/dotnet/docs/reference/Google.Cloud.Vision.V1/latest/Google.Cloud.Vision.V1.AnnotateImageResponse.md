---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AnnotateImageResponse
title: Google Cloud Vision v1 API - Class AnnotateImageResponse (3.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:39.337425+00:00
---

# Google Cloud Vision v1 API - Class AnnotateImageResponse (3.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AnnotateImageResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Vision v1 API - Class AnnotateImageResponse (3.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AnnotateImageResponse)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.7.0/Google.Cloud.Vision.V1.AnnotateImageResponse)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.6.0/Google.Cloud.Vision.V1.AnnotateImageResponse)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.5.0/Google.Cloud.Vision.V1.AnnotateImageResponse)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.4.0/Google.Cloud.Vision.V1.AnnotateImageResponse)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.3.0/Google.Cloud.Vision.V1.AnnotateImageResponse)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.2.0/Google.Cloud.Vision.V1.AnnotateImageResponse)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.1.0/Google.Cloud.Vision.V1.AnnotateImageResponse)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.0.0/Google.Cloud.Vision.V1.AnnotateImageResponse)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.5.0/Google.Cloud.Vision.V1.AnnotateImageResponse)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.4.0/Google.Cloud.Vision.V1.AnnotateImageResponse)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.3.0/Google.Cloud.Vision.V1.AnnotateImageResponse)


    
    
    public sealed class AnnotateImageResponse : IMessage<AnnotateImageResponse>, IEquatable<AnnotateImageResponse>, IDeepCloneable<AnnotateImageResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Vision v1 API class AnnotateImageResponse.

Response to an image annotation request.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AnnotateImageResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AnnotateImageResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AnnotateImageResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AnnotateImageResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AnnotateImageResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AnnotateImageResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AnnotateImageResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Vision.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1)

## Assembly

Google.Cloud.Vision.V1.dll

## Constructors 

### AnnotateImageResponse()
    
    
    public AnnotateImageResponse()

### AnnotateImageResponse(AnnotateImageResponse)
    
    
    public AnnotateImageResponse(AnnotateImageResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AnnotateImageResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AnnotateImageResponse)`  
  
  
## Properties 

### Context
    
    
    public ImageAnnotationContext Context { get; set; }

If present, contextual information is needed to understand where this image comes from.

**Property Value**  
---  
**Type** | **Description**  
`[ImageAnnotationContext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ImageAnnotationContext)` |   
  
### CropHintsAnnotation
    
    
    public CropHintsAnnotation CropHintsAnnotation { get; set; }

If present, crop hints have completed successfully.

**Property Value**  
---  
**Type** | **Description**  
`[CropHintsAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CropHintsAnnotation)` |   
  
### Error
    
    
    public Status Error { get; set; }

If set, represents the error message for the operation. Note that filled-in image annotations are guaranteed to be correct, even when `error` is set.

**Property Value**  
---  
**Type** | **Description**  
`[Status](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status.html)` |   
  
### FaceAnnotations
    
    
    public RepeatedField<FaceAnnotation> FaceAnnotations { get; }

If present, face detection has completed successfully.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[FaceAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.FaceAnnotation)` |   
  
### FullTextAnnotation
    
    
    public TextAnnotation FullTextAnnotation { get; set; }

If present, text (OCR) detection or document (OCR) text detection has completed successfully. This annotation provides the structural hierarchy for the OCR detected text.

**Property Value**  
---  
**Type** | **Description**  
`[TextAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.TextAnnotation)` |   
  
### ImagePropertiesAnnotation
    
    
    public ImageProperties ImagePropertiesAnnotation { get; set; }

If present, image properties were extracted successfully.

**Property Value**  
---  
**Type** | **Description**  
`[ImageProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ImageProperties)` |   
  
### LabelAnnotations
    
    
    public RepeatedField<EntityAnnotation> LabelAnnotations { get; }

If present, label detection has completed successfully.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[EntityAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.EntityAnnotation)` |   
  
### LandmarkAnnotations
    
    
    public RepeatedField<EntityAnnotation> LandmarkAnnotations { get; }

If present, landmark detection has completed successfully.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[EntityAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.EntityAnnotation)` |   
  
### LocalizedObjectAnnotations
    
    
    public RepeatedField<LocalizedObjectAnnotation> LocalizedObjectAnnotations { get; }

If present, localized object detection has completed successfully. This will be sorted descending by confidence score.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[LocalizedObjectAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.LocalizedObjectAnnotation)` |   
  
### LogoAnnotations
    
    
    public RepeatedField<EntityAnnotation> LogoAnnotations { get; }

If present, logo detection has completed successfully.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[EntityAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.EntityAnnotation)` |   
  
### ProductSearchResults
    
    
    public ProductSearchResults ProductSearchResults { get; set; }

If present, product search has completed successfully.

**Property Value**  
---  
**Type** | **Description**  
`[ProductSearchResults](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSearchResults)` |   
  
### SafeSearchAnnotation
    
    
    public SafeSearchAnnotation SafeSearchAnnotation { get; set; }

If present, safe-search annotation has completed successfully.

**Property Value**  
---  
**Type** | **Description**  
`[SafeSearchAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.SafeSearchAnnotation)` |   
  
### TextAnnotations
    
    
    public RepeatedField<EntityAnnotation> TextAnnotations { get; }

If present, text (OCR) detection has completed successfully.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[EntityAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.EntityAnnotation)` |   
  
### WebDetection
    
    
    public WebDetection WebDetection { get; set; }

If present, web detection has completed successfully.

**Property Value**  
---  
**Type** | **Description**  
`[WebDetection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.WebDetection)` |   
  
## Methods 

### ThrowOnError()
    
    
    public AnnotateImageResponse ThrowOnError()

If the [Error](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AnnotateImageResponse#Google_Cloud_Vision_V1_AnnotateImageResponse_Error) property is non-null, throws an [AnnotateImageException](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AnnotateImageException). Otherwise, returns `this` (so that the method can be called in a fluent manner).

**Returns**  
---  
**Type** | **Description**  
`[AnnotateImageResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AnnotateImageResponse)` | `this` if the message has no error.  
**Exceptions**  
---  
**Type** | **Description**  
`[AnnotateImageException](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AnnotateImageException)` | The [Error](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.AnnotateImageResponse#Google_Cloud_Vision_V1_AnnotateImageResponse_Error) property is non-null.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
