---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateReferenceImageRequest
title: Google Cloud Vision v1 API - Class CreateReferenceImageRequest (3.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:51.184541+00:00
---

# Google Cloud Vision v1 API - Class CreateReferenceImageRequest (3.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateReferenceImageRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Vision v1 API - Class CreateReferenceImageRequest (3.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateReferenceImageRequest)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.7.0/Google.Cloud.Vision.V1.CreateReferenceImageRequest)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.6.0/Google.Cloud.Vision.V1.CreateReferenceImageRequest)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.5.0/Google.Cloud.Vision.V1.CreateReferenceImageRequest)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.4.0/Google.Cloud.Vision.V1.CreateReferenceImageRequest)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.3.0/Google.Cloud.Vision.V1.CreateReferenceImageRequest)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.2.0/Google.Cloud.Vision.V1.CreateReferenceImageRequest)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.1.0/Google.Cloud.Vision.V1.CreateReferenceImageRequest)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.0.0/Google.Cloud.Vision.V1.CreateReferenceImageRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.5.0/Google.Cloud.Vision.V1.CreateReferenceImageRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.4.0/Google.Cloud.Vision.V1.CreateReferenceImageRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.3.0/Google.Cloud.Vision.V1.CreateReferenceImageRequest)


    
    
    public sealed class CreateReferenceImageRequest : IMessage<CreateReferenceImageRequest>, IEquatable<CreateReferenceImageRequest>, IDeepCloneable<CreateReferenceImageRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Vision v1 API class CreateReferenceImageRequest.

Request message for the `CreateReferenceImage` method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateReferenceImageRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateReferenceImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateReferenceImageRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateReferenceImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateReferenceImageRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateReferenceImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateReferenceImageRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Vision.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1)

## Assembly

Google.Cloud.Vision.V1.dll

## Constructors 

### CreateReferenceImageRequest()
    
    
    public CreateReferenceImageRequest()

### CreateReferenceImageRequest(CreateReferenceImageRequest)
    
    
    public CreateReferenceImageRequest(CreateReferenceImageRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateReferenceImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateReferenceImageRequest)`  
  
  
## Properties 

### Parent
    
    
    public string Parent { get; set; }

Required. Resource name of the product in which to create the reference image.

Format is `projects/PROJECT_ID/locations/LOC_ID/products/PRODUCT_ID`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsProductName
    
    
    public ProductName ParentAsProductName { get; set; }

[ProductName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.CreateReferenceImageRequest#Google_Cloud_Vision_V1_CreateReferenceImageRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProductName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductName)` |   
  
### ReferenceImage
    
    
    public ReferenceImage ReferenceImage { get; set; }

Required. The reference image to create. If an image ID is specified, it is ignored.

**Property Value**  
---  
**Type** | **Description**  
`[ReferenceImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ReferenceImage)` |   
  
### ReferenceImageId
    
    
    public string ReferenceImageId { get; set; }

A user-supplied resource id for the ReferenceImage to be added. If set, the server will attempt to use this value as the resource id. If it is already in use, an error is returned with code ALREADY_EXISTS. Must be at most 128 characters long. It cannot contain the character `/`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
