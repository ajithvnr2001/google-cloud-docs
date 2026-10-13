---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.ListReplicationsRequest
title: NetApp v1 API - Class ListReplicationsRequest (1.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:38.283324+00:00
---

# NetApp v1 API - Class ListReplicationsRequest (1.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.ListReplicationsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  NetApp v1 API - Class ListReplicationsRequest (1.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.0 (latest)  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ListReplicationsRequest : IPageRequest, IMessage<ListReplicationsRequest>, IEquatable<ListReplicationsRequest>, IDeepCloneable<ListReplicationsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the NetApp v1 API class ListReplicationsRequest.

ListReplications lists replications.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListReplicationsRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListReplicationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.ListReplicationsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListReplicationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.ListReplicationsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListReplicationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.ListReplicationsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetApp.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1)

## Assembly

Google.Cloud.NetApp.V1.dll

## Constructors 

### ListReplicationsRequest()
    
    
    public ListReplicationsRequest()

### ListReplicationsRequest(ListReplicationsRequest)
    
    
    public ListReplicationsRequest(ListReplicationsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListReplicationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.ListReplicationsRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

List filter.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrderBy
    
    
    public string OrderBy { get; set; }

Sort results. Supported values are "name", "name desc" or "" (unsorted).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

The maximum number of items to return.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

The next_page_token value to use if there are additional results to retrieve for this list request.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The volume for which to retrieve replication information, in the format `projects/{project_id}/locations/{location}/volumes/{volume_id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsVolumeName
    
    
    public VolumeName ParentAsVolumeName { get; set; }

[VolumeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.VolumeName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.ListReplicationsRequest#Google_Cloud_NetApp_V1_ListReplicationsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[VolumeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetApp.V1/latest/Google.Cloud.NetApp.V1.VolumeName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
