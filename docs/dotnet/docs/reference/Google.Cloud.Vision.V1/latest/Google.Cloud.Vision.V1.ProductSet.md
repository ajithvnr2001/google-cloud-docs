---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet
title: Google Cloud Vision v1 API - Class ProductSet (3.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:02.740536+00:00
---

# Google Cloud Vision v1 API - Class ProductSet (3.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Vision v1 API - Class ProductSet (3.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.7.0/Google.Cloud.Vision.V1.ProductSet)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.6.0/Google.Cloud.Vision.V1.ProductSet)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.5.0/Google.Cloud.Vision.V1.ProductSet)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.4.0/Google.Cloud.Vision.V1.ProductSet)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.3.0/Google.Cloud.Vision.V1.ProductSet)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.2.0/Google.Cloud.Vision.V1.ProductSet)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.1.0/Google.Cloud.Vision.V1.ProductSet)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.0.0/Google.Cloud.Vision.V1.ProductSet)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.5.0/Google.Cloud.Vision.V1.ProductSet)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.4.0/Google.Cloud.Vision.V1.ProductSet)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.3.0/Google.Cloud.Vision.V1.ProductSet)


    
    
    public sealed class ProductSet : IMessage<ProductSet>, IEquatable<ProductSet>, IDeepCloneable<ProductSet>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Vision v1 API class ProductSet.

A ProductSet contains Products. A ProductSet can contain a maximum of 1 million reference images. If the limit is exceeded, periodic indexing will fail.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ProductSet

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ProductSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ProductSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ProductSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Vision.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1)

## Assembly

Google.Cloud.Vision.V1.dll

## Constructors 

### ProductSet()
    
    
    public ProductSet()

### ProductSet(ProductSet)
    
    
    public ProductSet(ProductSet other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ProductSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet)`  
  
  
## Properties 

### DisplayName
    
    
    public string DisplayName { get; set; }

The user-provided name for this ProductSet. Must not be empty. Must be at most 4096 characters long.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IndexError
    
    
    public Status IndexError { get; set; }

Output only. If there was an error with indexing the product set, the field is populated.

This field is ignored when creating a ProductSet.

**Property Value**  
---  
**Type** | **Description**  
`[Status](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status.html)` |   
  
### IndexTime
    
    
    public Timestamp IndexTime { get; set; }

Output only. The time at which this ProductSet was last indexed. Query results will reflect all updates before this time. If this ProductSet has never been indexed, this timestamp is the default value "1970-01-01T00:00:00Z".

This field is ignored when creating a ProductSet.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Name
    
    
    public string Name { get; set; }

The resource name of the ProductSet.

Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`.

This field is ignored when creating a ProductSet.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProductSetName
    
    
    public ProductSetName ProductSetName { get; set; }

[ProductSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSetName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSet#Google_Cloud_Vision_V1_ProductSet_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProductSetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ProductSetName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
