---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest
title: Cloud Quotas v1 API - Class ListQuotaInfosRequest (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:23.674740+00:00
---

# Cloud Quotas v1 API - Class ListQuotaInfosRequest (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Quotas v1 API - Class ListQuotaInfosRequest (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0-beta05 
    
    
    public sealed class ListQuotaInfosRequest : IMessage<ListQuotaInfosRequest>, IEquatable<ListQuotaInfosRequest>, IDeepCloneable<ListQuotaInfosRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Cloud Quotas v1 API class ListQuotaInfosRequest.

Message for requesting list of QuotaInfos

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListQuotaInfosRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListQuotaInfosRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListQuotaInfosRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListQuotaInfosRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudQuotas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1)

## Assembly

Google.Cloud.CloudQuotas.V1.dll

## Constructors 

### ListQuotaInfosRequest()
    
    
    public ListQuotaInfosRequest()

### ListQuotaInfosRequest(ListQuotaInfosRequest)
    
    
    public ListQuotaInfosRequest(ListQuotaInfosRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListQuotaInfosRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. A token identifying a page of results the server should return.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. Identifier. Parent value of QuotaInfo resources. Listing across different resource containers (such as 'projects/-') is not allowed.

Example names: `projects/123/locations/global/services/compute.googleapis.com` `folders/234/locations/global/services/compute.googleapis.com` `organizations/345/locations/global/services/compute.googleapis.com`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsServiceName
    
    
    public ServiceName ParentAsServiceName { get; set; }

[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest#Google_Cloud_CloudQuotas_V1_ListQuotaInfosRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
