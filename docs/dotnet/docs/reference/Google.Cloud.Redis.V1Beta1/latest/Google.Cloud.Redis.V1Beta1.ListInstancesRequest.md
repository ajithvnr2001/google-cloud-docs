---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesRequest
title: Google Cloud Memorystore for Redis v1beta1 API - Class ListInstancesRequest (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:02.241436+00:00
---

# Google Cloud Memorystore for Redis v1beta1 API - Class ListInstancesRequest (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis v1beta1 API - Class ListInstancesRequest (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesRequest)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/3.0.0-beta05/Google.Cloud.Redis.V1Beta1.ListInstancesRequest)
  * [ 2.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/2.0.0-beta09/Google.Cloud.Redis.V1Beta1.ListInstancesRequest)


    
    
    public sealed class ListInstancesRequest : IMessage<ListInstancesRequest>, IEquatable<ListInstancesRequest>, IDeepCloneable<ListInstancesRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Google Cloud Memorystore for Redis v1beta1 API class ListInstancesRequest.

Request for [ListInstances][google.cloud.redis.v1beta1.CloudRedis.ListInstances].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListInstancesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Redis.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1)

## Assembly

Google.Cloud.Redis.V1Beta1.dll

## Constructors 

### ListInstancesRequest()
    
    
    public ListInstancesRequest()

### ListInstancesRequest(ListInstancesRequest)
    
    
    public ListInstancesRequest(ListInstancesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

The maximum number of items to return.

If not specified, a default value of 1000 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's [`next_page_token`][google.cloud.redis.v1beta1.ListInstancesResponse.next_page_token] to determine if there are more instances left to be queried.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

The `next_page_token` value returned from a previous [ListInstances][google.cloud.redis.v1beta1.CloudRedis.ListInstances] request, if any.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The resource name of the instance location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.ListInstancesRequest#Google_Cloud_Redis_V1Beta1_ListInstancesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
