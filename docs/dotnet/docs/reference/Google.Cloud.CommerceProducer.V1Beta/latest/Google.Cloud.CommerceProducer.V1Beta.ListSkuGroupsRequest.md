---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.ListSkuGroupsRequest
title: Cloud Commerce Producer v1beta API - Class ListSkuGroupsRequest (1.0.0-beta03) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:55.194479+00:00
---

# Cloud Commerce Producer v1beta API - Class ListSkuGroupsRequest (1.0.0-beta03)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.ListSkuGroupsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Commerce Producer v1beta API - Class ListSkuGroupsRequest (1.0.0-beta03) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta03 (latest)  1.0.0-beta02 
    
    
    public sealed class ListSkuGroupsRequest : IMessage<ListSkuGroupsRequest>, IEquatable<ListSkuGroupsRequest>, IDeepCloneable<ListSkuGroupsRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Cloud Commerce Producer v1beta API class ListSkuGroupsRequest.

Message for requesting list of SkuGroups

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListSkuGroupsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListSkuGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.ListSkuGroupsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListSkuGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.ListSkuGroupsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListSkuGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.ListSkuGroupsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CommerceProducer.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta)

## Assembly

Google.Cloud.CommerceProducer.V1Beta.dll

## Constructors 

### ListSkuGroupsRequest()
    
    
    public ListSkuGroupsRequest()

### ListSkuGroupsRequest(ListSkuGroupsRequest)
    
    
    public ListSkuGroupsRequest(ListSkuGroupsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListSkuGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.ListSkuGroupsRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

Optional. Maximum results to return. The service may return fewer than this value. The maximum value is 500; values above 500 will be coerced to 500. If unspecified, the server will default to the maximum.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. A page token, received from a previous list response message. Provide this to retrieve the subsequent page.

When paginating, all other parameters of the list request must match the request that returned the page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. Parent value for ListSkuGroupsRequest

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CommerceProducer.V1Beta/latest/Google.Cloud.CommerceProducer.V1Beta.ListSkuGroupsRequest#Google_Cloud_CommerceProducer_V1Beta_ListSkuGroupsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
