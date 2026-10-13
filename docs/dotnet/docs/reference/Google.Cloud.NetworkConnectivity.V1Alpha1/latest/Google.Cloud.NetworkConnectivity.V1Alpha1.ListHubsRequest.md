---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.ListHubsRequest
title: Network Connectivity v1alpha1 API - Class ListHubsRequest (2.0.0-alpha05) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:44.294045+00:00
---

# Network Connectivity v1alpha1 API - Class ListHubsRequest (2.0.0-alpha05)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.ListHubsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Connectivity v1alpha1 API - Class ListHubsRequest (2.0.0-alpha05) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-alpha05 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.ListHubsRequest)
  * [ 2.0.0-alpha04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/2.0.0-alpha04/Google.Cloud.NetworkConnectivity.V1Alpha1.ListHubsRequest)
  * [ 1.0.0-alpha03 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/1.0.0-alpha03/Google.Cloud.NetworkConnectivity.V1Alpha1.ListHubsRequest)


    
    
    public sealed class ListHubsRequest : IMessage<ListHubsRequest>, IEquatable<ListHubsRequest>, IDeepCloneable<ListHubsRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Network Connectivity v1alpha1 API class ListHubsRequest.

Request for [HubService.ListHubs][google.cloud.networkconnectivity.v1alpha1.HubService.ListHubs] method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListHubsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListHubsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.ListHubsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListHubsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.ListHubsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListHubsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.ListHubsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkConnectivity.V1Alpha1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1)

## Assembly

Google.Cloud.NetworkConnectivity.V1Alpha1.dll

## Constructors 

### ListHubsRequest()
    
    
    public ListHubsRequest()

### ListHubsRequest(ListHubsRequest)
    
    
    public ListHubsRequest(ListHubsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListHubsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.ListHubsRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

A filter expression that filters the results listed in the response.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OrderBy
    
    
    public string OrderBy { get; set; }

Sort the results by a certain order.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

The maximum number of results per page that should be returned.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

The page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent resource's name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Alpha1/latest/Google.Cloud.NetworkConnectivity.V1Alpha1.ListHubsRequest#Google_Cloud_NetworkConnectivity_V1Alpha1_ListHubsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
