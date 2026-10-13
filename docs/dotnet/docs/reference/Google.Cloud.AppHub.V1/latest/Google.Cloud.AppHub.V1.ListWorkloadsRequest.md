---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListWorkloadsRequest
title: App Hub v1 API - Class ListWorkloadsRequest (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:28.740286+00:00
---

# App Hub v1 API - Class ListWorkloadsRequest (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListWorkloadsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  App Hub v1 API - Class ListWorkloadsRequest (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ListWorkloadsRequest : IPageRequest, IMessage<ListWorkloadsRequest>, IEquatable<ListWorkloadsRequest>, IDeepCloneable<ListWorkloadsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the App Hub v1 API class ListWorkloadsRequest.

Request for ListWorkloads.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListWorkloadsRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListWorkloadsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListWorkloadsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListWorkloadsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListWorkloadsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListWorkloadsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListWorkloadsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AppHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1)

## Assembly

Google.Cloud.AppHub.V1.dll

## Constructors 

### ListWorkloadsRequest()
    
    
    public ListWorkloadsRequest()

### ListWorkloadsRequest(ListWorkloadsRequest)
    
    
    public ListWorkloadsRequest(ListWorkloadsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListWorkloadsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListWorkloadsRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

Optional. Filtering results.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrderBy
    
    
    public string OrderBy { get; set; }

Optional. Hint for how to order the results.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
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

Required. Fully qualified name of the parent Application to list Workloads for. Expected format: `projects/{project}/locations/{location}/applications/{application}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsApplicationName
    
    
    public ApplicationName ParentAsApplicationName { get; set; }

[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ListWorkloadsRequest#Google_Cloud_AppHub_V1_ListWorkloadsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ApplicationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ApplicationName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
