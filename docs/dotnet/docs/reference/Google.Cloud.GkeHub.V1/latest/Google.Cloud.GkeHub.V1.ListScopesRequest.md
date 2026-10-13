---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ListScopesRequest
title: GKE Hub v1 API - Class ListScopesRequest (2.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:23.986745+00:00
---

# GKE Hub v1 API - Class ListScopesRequest (2.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ListScopesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  GKE Hub v1 API - Class ListScopesRequest (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ListScopesRequest)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.7.0/Google.Cloud.GkeHub.V1.ListScopesRequest)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.6.0/Google.Cloud.GkeHub.V1.ListScopesRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.5.0/Google.Cloud.GkeHub.V1.ListScopesRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.4.0/Google.Cloud.GkeHub.V1.ListScopesRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.3.0/Google.Cloud.GkeHub.V1.ListScopesRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.2.0/Google.Cloud.GkeHub.V1.ListScopesRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.1.0/Google.Cloud.GkeHub.V1.ListScopesRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.0.0/Google.Cloud.GkeHub.V1.ListScopesRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/1.2.0/Google.Cloud.GkeHub.V1.ListScopesRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/1.1.0/Google.Cloud.GkeHub.V1.ListScopesRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/1.0.0/Google.Cloud.GkeHub.V1.ListScopesRequest)


    
    
    public sealed class ListScopesRequest : IPageRequest, IMessage<ListScopesRequest>, IEquatable<ListScopesRequest>, IDeepCloneable<ListScopesRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the GKE Hub v1 API class ListScopesRequest.

Request to list Scopes.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListScopesRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListScopesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ListScopesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListScopesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ListScopesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListScopesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ListScopesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GkeHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1)

## Assembly

Google.Cloud.GkeHub.V1.dll

## Constructors 

### ListScopesRequest()
    
    
    public ListScopesRequest()

### ListScopesRequest(ListScopesRequest)
    
    
    public ListScopesRequest(ListScopesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListScopesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ListScopesRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

Optional. When requesting a 'page' of resources, `page_size` specifies number of resources to return. If unspecified or set to 0, all resources will be returned.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. Token returned by previous call to `ListScopes` which specifies the position in the list from where to continue listing the resources.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent (project and location) where the Scope will be listed. Specified in the format `projects/*/locations/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ListScopesRequest#Google_Cloud_GkeHub_V1_ListScopesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
