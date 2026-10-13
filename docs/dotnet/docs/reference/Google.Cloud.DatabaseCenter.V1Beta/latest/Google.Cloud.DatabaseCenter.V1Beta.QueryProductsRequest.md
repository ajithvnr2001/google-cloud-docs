---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsRequest
title: Database Center v1beta API - Class QueryProductsRequest (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:35:00.332488+00:00
---

# Database Center v1beta API - Class QueryProductsRequest (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class QueryProductsRequest (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public sealed class QueryProductsRequest : IPageRequest, IMessage<QueryProductsRequest>, IEquatable<QueryProductsRequest>, IDeepCloneable<QueryProductsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Center v1beta API class QueryProductsRequest.

QueryProductsRequest is the request to get a list of products.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > QueryProductsRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[QueryProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[QueryProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[QueryProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Constructors 

### QueryProductsRequest()
    
    
    public QueryProductsRequest()

### QueryProductsRequest(QueryProductsRequest)
    
    
    public QueryProductsRequest(QueryProductsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[QueryProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.QueryProductsRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

Optional. If unspecified, at most 50 products will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. A page token, received from a previous `ListLocations` call. Provide this to retrieve the subsequent page. All other parameters except page size should match the call that provided the page page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. Parent can be a project, a folder, or an organization.

The allowed values are:

  * projects/{PROJECT_ID}/locations/{LOCATION} (e.g.,"projects/foo-bar/locations/us-central1")
  * projects/{PROJECT_NUMBER}/locations/{LOCATION} (e.g.,"projects/12345678/locations/us-central1")
  * folders/{FOLDER_NUMBER}/locations/{LOCATION} (e.g.,"folders/1234567/locations/us-central1")
  * organizations/{ORGANIZATION_NUMBER}/locations/{LOCATION} (e.g.,"organizations/123456/locations/us-central1")
  * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
  * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
  * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
  * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
