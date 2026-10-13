---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest
title: Backup for GKE v1 API - Class ListRestoreChannelsRequest (2.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:20.702008+00:00
---

# Backup for GKE v1 API - Class ListRestoreChannelsRequest (2.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Backup for GKE v1 API - Class ListRestoreChannelsRequest (2.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.9.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.8.0/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.7.0/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.6.0/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.5.0/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.4.0/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.3.0/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.2.0/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.1.0/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/2.0.0/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest)
  * [ 1.0.0-beta01 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/1.0.0-beta01/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest)


    
    
    public sealed class ListRestoreChannelsRequest : IPageRequest, IMessage<ListRestoreChannelsRequest>, IEquatable<ListRestoreChannelsRequest>, IDeepCloneable<ListRestoreChannelsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Backup for GKE v1 API class ListRestoreChannelsRequest.

Request message for ListRestoreChannels.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListRestoreChannelsRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListRestoreChannelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListRestoreChannelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListRestoreChannelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GkeBackup.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1)

## Assembly

Google.Cloud.GkeBackup.V1.dll

## Constructors 

### ListRestoreChannelsRequest()
    
    
    public ListRestoreChannelsRequest()

### ListRestoreChannelsRequest(ListRestoreChannelsRequest)
    
    
    public ListRestoreChannelsRequest(ListRestoreChannelsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListRestoreChannelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

Optional. Field match expression used to filter the results.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrderBy
    
    
    public string OrderBy { get; set; }

Optional. Field by which to sort the results.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Optional. The target number of results to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's [next_page_token][google.cloud.gkebackup.v1.ListRestoreChannelsResponse.next_page_token] to determine if there are more instances left to be queried.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. The value of [next_page_token][google.cloud.gkebackup.v1.ListRestoreChannelsResponse.next_page_token] received from a previous `ListRestoreChannels` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListRestoreChannels` must match the call that provided the page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The location that contains the RestoreChannels to list. Format: `projects/*/locations/*`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeBackup.V1/latest/Google.Cloud.GkeBackup.V1.ListRestoreChannelsRequest#Google_Cloud_GkeBackup_V1_ListRestoreChannelsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
