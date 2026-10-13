---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ListEndpointPoliciesRequest
title: Network Services v1 API - Class ListEndpointPoliciesRequest (1.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:03.787055+00:00
---

# Network Services v1 API - Class ListEndpointPoliciesRequest (1.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ListEndpointPoliciesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Services v1 API - Class ListEndpointPoliciesRequest (1.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.0 (latest)  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ListEndpointPoliciesRequest : IMessage<ListEndpointPoliciesRequest>, IEquatable<ListEndpointPoliciesRequest>, IDeepCloneable<ListEndpointPoliciesRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Network Services v1 API class ListEndpointPoliciesRequest.

Request used with the ListEndpointPolicies method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListEndpointPoliciesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListEndpointPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ListEndpointPoliciesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListEndpointPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ListEndpointPoliciesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListEndpointPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ListEndpointPoliciesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkServices.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1)

## Assembly

Google.Cloud.NetworkServices.V1.dll

## Constructors 

### ListEndpointPoliciesRequest()
    
    
    public ListEndpointPoliciesRequest()

### ListEndpointPoliciesRequest(ListEndpointPoliciesRequest)
    
    
    public ListEndpointPoliciesRequest(ListEndpointPoliciesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListEndpointPoliciesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ListEndpointPoliciesRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

Maximum number of EndpointPolicies to return per call.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

The value returned by the last `ListEndpointPoliciesResponse` Indicates that this is a continuation of a prior `ListEndpointPolicies` call, and that the system should return the next page of data.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The project and location from which the EndpointPolicies should be listed, specified in the format `projects/*/locations/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ListEndpointPoliciesRequest#Google_Cloud_NetworkServices_V1_ListEndpointPoliciesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### ReturnPartialSuccess
    
    
    public bool ReturnPartialSuccess { get; set; }

Optional. If true, allow partial responses for multi-regional Aggregated List requests. Otherwise if one of the locations is down or unreachable, the Aggregated List request will fail.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
