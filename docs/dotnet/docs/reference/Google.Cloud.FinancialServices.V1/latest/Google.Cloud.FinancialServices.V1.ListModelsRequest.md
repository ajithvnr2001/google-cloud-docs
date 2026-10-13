---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.ListModelsRequest
title: Financial Services v1 API - Class ListModelsRequest (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:20:05.501145+00:00
---

# Financial Services v1 API - Class ListModelsRequest (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.ListModelsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Financial Services v1 API - Class ListModelsRequest (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta02 
    
    
    public sealed class ListModelsRequest : IPageRequest, IMessage<ListModelsRequest>, IEquatable<ListModelsRequest>, IDeepCloneable<ListModelsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Financial Services v1 API class ListModelsRequest.

Request for retrieving a paginated list of Model resources that meet the specified criteria.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListModelsRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListModelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.ListModelsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListModelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.ListModelsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListModelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.ListModelsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.FinancialServices.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1)

## Assembly

Google.Cloud.FinancialServices.V1.dll

## Constructors 

### ListModelsRequest()
    
    
    public ListModelsRequest()

### ListModelsRequest(ListModelsRequest)
    
    
    public ListModelsRequest(ListModelsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListModelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.ListModelsRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

Specify a filter to narrow search results.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrderBy
    
    
    public string OrderBy { get; set; }

Specify a field to use for ordering.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

The number of resources to be included in the response. The response contains a next_page_token, which can be used to retrieve the next page of resources.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

In case of paginated results, this is the token that was returned in the previous ListModelsResponse. It should be copied here to retrieve the next page of resources. Empty will give the first page of ListModelsRequest, and the last page will return an empty page_token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent of the Model is the Instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsInstanceName
    
    
    public InstanceName ParentAsInstanceName { get; set; }

[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.InstanceName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.ListModelsRequest#Google_Cloud_FinancialServices_V1_ListModelsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.InstanceName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
