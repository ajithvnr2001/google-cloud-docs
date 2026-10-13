---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation
title: Vertex AI v1beta1 API - Class ImageSegmentationAnnotation (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:29:01.505194+00:00
---

# Vertex AI v1beta1 API - Class ImageSegmentationAnnotation (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ImageSegmentationAnnotation (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class ImageSegmentationAnnotation : IMessage<ImageSegmentationAnnotation>, IEquatable<ImageSegmentationAnnotation>, IDeepCloneable<ImageSegmentationAnnotation>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class ImageSegmentationAnnotation.

Annotation details specific to image segmentation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ImageSegmentationAnnotation

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ImageSegmentationAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ImageSegmentationAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ImageSegmentationAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1.Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### ImageSegmentationAnnotation()
    
    
    public ImageSegmentationAnnotation()

### ImageSegmentationAnnotation(ImageSegmentationAnnotation)
    
    
    public ImageSegmentationAnnotation(ImageSegmentationAnnotation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ImageSegmentationAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation)`  
  
  
## Properties 

### AnnotationCase
    
    
    public ImageSegmentationAnnotation.AnnotationOneofCase AnnotationCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ImageSegmentationAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation)[AnnotationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation.AnnotationOneofCase)` |   
  
### MaskAnnotation
    
    
    public ImageSegmentationAnnotation.Types.MaskAnnotation MaskAnnotation { get; set; }

Mask based segmentation annotation. Only one mask annotation can exist for one image.

**Property Value**  
---  
**Type** | **Description**  
`[ImageSegmentationAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation.Types)[MaskAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation.Types.MaskAnnotation)` |   
  
### PolygonAnnotation
    
    
    public ImageSegmentationAnnotation.Types.PolygonAnnotation PolygonAnnotation { get; set; }

Polygon annotation.

**Property Value**  
---  
**Type** | **Description**  
`[ImageSegmentationAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation.Types)[PolygonAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation.Types.PolygonAnnotation)` |   
  
### PolylineAnnotation
    
    
    public ImageSegmentationAnnotation.Types.PolylineAnnotation PolylineAnnotation { get; set; }

Polyline annotation.

**Property Value**  
---  
**Type** | **Description**  
`[ImageSegmentationAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation.Types)[PolylineAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.ImageSegmentationAnnotation.Types.PolylineAnnotation)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
