---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.ListProductSuitesRequest
title: Cloud Product Registry v1 API - Class ListProductSuitesRequest (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:57.106146+00:00
---

# Cloud Product Registry v1 API - Class ListProductSuitesRequest (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.ListProductSuitesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Product Registry v1 API - Class ListProductSuitesRequest (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class ListProductSuitesRequest : IMessage<ListProductSuitesRequest>, IEquatable<ListProductSuitesRequest>, IDeepCloneable<ListProductSuitesRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Cloud Product Registry v1 API class ListProductSuitesRequest.

Request message for ListProductSuites.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListProductSuitesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListProductSuitesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.ListProductSuitesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListProductSuitesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.ListProductSuitesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListProductSuitesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.ListProductSuitesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ProductRegistry.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1)

## Assembly

Google.Cloud.ProductRegistry.V1.dll

## Constructors 

### ListProductSuitesRequest()
    
    
    public ListProductSuitesRequest()

### ListProductSuitesRequest(ListProductSuitesRequest)
    
    
    public ListProductSuitesRequest(ListProductSuitesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListProductSuitesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.ListProductSuitesRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

Optional. The maximum number of suites to return. The service may return fewer than this value. If unspecified, at most 100 suites will be returned. The maximum value is 500; values above 500 will be coerced to 500.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. A page token, received from a previous `ListProductSuites` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListProductSuites` must match the call that provided the page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
