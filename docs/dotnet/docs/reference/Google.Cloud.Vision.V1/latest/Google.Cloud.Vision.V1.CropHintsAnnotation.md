---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CropHintsAnnotation
title: Google Cloud Vision v1 API - Class CropHintsAnnotation (3.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:30.694340+00:00
---

# Google Cloud Vision v1 API - Class CropHintsAnnotation (3.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CropHintsAnnotation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Vision v1 API - Class CropHintsAnnotation (3.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CropHintsAnnotation)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.7.0/Google.Cloud.Vision.V1.CropHintsAnnotation)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.6.0/Google.Cloud.Vision.V1.CropHintsAnnotation)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.5.0/Google.Cloud.Vision.V1.CropHintsAnnotation)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.4.0/Google.Cloud.Vision.V1.CropHintsAnnotation)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.3.0/Google.Cloud.Vision.V1.CropHintsAnnotation)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.2.0/Google.Cloud.Vision.V1.CropHintsAnnotation)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.1.0/Google.Cloud.Vision.V1.CropHintsAnnotation)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.0.0/Google.Cloud.Vision.V1.CropHintsAnnotation)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.5.0/Google.Cloud.Vision.V1.CropHintsAnnotation)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.4.0/Google.Cloud.Vision.V1.CropHintsAnnotation)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.3.0/Google.Cloud.Vision.V1.CropHintsAnnotation)


    
    
    public sealed class CropHintsAnnotation : IMessage<CropHintsAnnotation>, IEquatable<CropHintsAnnotation>, IDeepCloneable<CropHintsAnnotation>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Vision v1 API class CropHintsAnnotation.

Set of crop hints that are used to generate new crops when serving images.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CropHintsAnnotation

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CropHintsAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CropHintsAnnotation), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CropHintsAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CropHintsAnnotation), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CropHintsAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CropHintsAnnotation), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Vision.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1)

## Assembly

Google.Cloud.Vision.V1.dll

## Constructors 

### CropHintsAnnotation()
    
    
    public CropHintsAnnotation()

### CropHintsAnnotation(CropHintsAnnotation)
    
    
    public CropHintsAnnotation(CropHintsAnnotation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CropHintsAnnotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CropHintsAnnotation)`  
  
  
## Properties 

### CropHints
    
    
    public RepeatedField<CropHint> CropHints { get; }

Crop hint results.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[CropHint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CropHint)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
