---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.SearchProductsResponse
title: Cloud Private Catalog v1beta1 API - Class SearchProductsResponse (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:35.754507+00:00
---

# Cloud Private Catalog v1beta1 API - Class SearchProductsResponse (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.SearchProductsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Private Catalog v1beta1 API - Class SearchProductsResponse (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.SearchProductsResponse)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/2.0.0-beta05/Google.Cloud.PrivateCatalog.V1Beta1.SearchProductsResponse)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/1.0.0-beta02/Google.Cloud.PrivateCatalog.V1Beta1.SearchProductsResponse)


    
    
    public sealed class SearchProductsResponse : IMessage<SearchProductsResponse>, IEquatable<SearchProductsResponse>, IDeepCloneable<SearchProductsResponse>, IBufferMessage, IMessage, IPageResponse<Product>, IEnumerable<Product>, IEnumerable

Reference documentation and code samples for the Cloud Private Catalog v1beta1 API class SearchProductsResponse.

Response message for [PrivateCatalog.SearchProducts][google.cloud.privatecatalog.v1beta1.PrivateCatalog.SearchProducts].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SearchProductsResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SearchProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.SearchProductsResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SearchProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.SearchProductsResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SearchProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.SearchProductsResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.Product), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.Product), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.PrivateCatalog.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1)

## Assembly

Google.Cloud.PrivateCatalog.V1Beta1.dll

## Constructors 

### SearchProductsResponse()
    
    
    public SearchProductsResponse()

### SearchProductsResponse(SearchProductsResponse)
    
    
    public SearchProductsResponse(SearchProductsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SearchProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.SearchProductsResponse)`  
  
  
## Properties 

### NextPageToken
    
    
    public string NextPageToken { get; set; }

A pagination token returned from a previous call to SearchProducts that indicates from where listing should continue.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Products
    
    
    public RepeatedField<Product> Products { get; }

The `Product` resources computed from the resource context.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.Product)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<Product> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PrivateCatalog.V1Beta1/latest/Google.Cloud.PrivateCatalog.V1Beta1.Product)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
