---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListCompilationResultsRequest
title: Dataform v1beta1 API - Class ListCompilationResultsRequest (1.0.0-beta15) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:04.979303+00:00
---

# Dataform v1beta1 API - Class ListCompilationResultsRequest (1.0.0-beta15)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListCompilationResultsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataform v1beta1 API - Class ListCompilationResultsRequest (1.0.0-beta15) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta15 (latest)  1.0.0-beta14 
    
    
    public sealed class ListCompilationResultsRequest : IMessage<ListCompilationResultsRequest>, IEquatable<ListCompilationResultsRequest>, IDeepCloneable<ListCompilationResultsRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Dataform v1beta1 API class ListCompilationResultsRequest.

`ListCompilationResults` request message.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListCompilationResultsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListCompilationResultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListCompilationResultsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListCompilationResultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListCompilationResultsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListCompilationResultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListCompilationResultsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1)

## Assembly

Google.Cloud.Dataform.V1Beta1.dll

## Constructors 

### ListCompilationResultsRequest()
    
    
    public ListCompilationResultsRequest()

### ListCompilationResultsRequest(ListCompilationResultsRequest)
    
    
    public ListCompilationResultsRequest(ListCompilationResultsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListCompilationResultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListCompilationResultsRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

Optional. Filter for the returned list.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrderBy
    
    
    public string OrderBy { get; set; }

Optional. This field only supports ordering by `name` and `create_time`. If unspecified, the server will choose the ordering. If specified, the default order is ascending for the `name` field.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Optional. Maximum number of compilation results to return. The server may return fewer items than requested. If unspecified, the server will pick an appropriate default.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. Page token received from a previous `ListCompilationResults` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListCompilationResults`, with the exception of `page_size`, must match the call that provided the page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The repository in which to list compilation results. Must be in the format `projects/*/locations/*/repositories/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsRepositoryName
    
    
    public RepositoryName ParentAsRepositoryName { get; set; }

[RepositoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RepositoryName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.ListCompilationResultsRequest#Google_Cloud_Dataform_V1Beta1_ListCompilationResultsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[RepositoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1Beta1/latest/Google.Cloud.Dataform.V1Beta1.RepositoryName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
