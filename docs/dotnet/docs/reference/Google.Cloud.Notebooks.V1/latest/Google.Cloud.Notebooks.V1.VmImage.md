---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.VmImage
title: Vertex AI Notebooks v1 API - Class VmImage (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:26.301483+00:00
---

# Vertex AI Notebooks v1 API - Class VmImage (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.VmImage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI Notebooks v1 API - Class VmImage (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.VmImage)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.5.0/Google.Cloud.Notebooks.V1.VmImage)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.4.0/Google.Cloud.Notebooks.V1.VmImage)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.3.0/Google.Cloud.Notebooks.V1.VmImage)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.2.0/Google.Cloud.Notebooks.V1.VmImage)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.1.0/Google.Cloud.Notebooks.V1.VmImage)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/2.0.0/Google.Cloud.Notebooks.V1.VmImage)
  * [ 1.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/1.0.0-beta04/Google.Cloud.Notebooks.V1.VmImage)


    
    
    public sealed class VmImage : IMessage<VmImage>, IEquatable<VmImage>, IDeepCloneable<VmImage>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI Notebooks v1 API class VmImage.

Definition of a custom Compute Engine virtual machine image for starting a notebook instance with the environment installed directly on the VM.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > VmImage

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[VmImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.VmImage), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[VmImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.VmImage), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[VmImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.VmImage), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Notebooks.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1)

## Assembly

Google.Cloud.Notebooks.V1.dll

## Constructors 

### VmImage()
    
    
    public VmImage()

### VmImage(VmImage)
    
    
    public VmImage(VmImage other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[VmImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.VmImage)`  
  
  
## Properties 

### HasImageFamily
    
    
    public bool HasImageFamily { get; }

Gets whether the "image_family" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasImageName
    
    
    public bool HasImageName { get; }

Gets whether the "image_name" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ImageCase
    
    
    public VmImage.ImageOneofCase ImageCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[VmImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.VmImage)[ImageOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1/latest/Google.Cloud.Notebooks.V1.VmImage.ImageOneofCase)` |   
  
### ImageFamily
    
    
    public string ImageFamily { get; set; }

Use this VM image family to find the image; the newest image in this family will be used.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ImageName
    
    
    public string ImageName { get; set; }

Use VM image name to find the image.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Project
    
    
    public string Project { get; set; }

Required. The name of the Google Cloud project that this VM image belongs to. Format: `{project_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
