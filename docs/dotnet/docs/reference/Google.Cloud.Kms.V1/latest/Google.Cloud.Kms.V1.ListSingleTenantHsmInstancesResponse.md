---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListSingleTenantHsmInstancesResponse
title: Google Cloud Key Management Service v1 API - Class ListSingleTenantHsmInstancesResponse (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:15.327753+00:00
---

# Google Cloud Key Management Service v1 API - Class ListSingleTenantHsmInstancesResponse (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListSingleTenantHsmInstancesResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Class ListSingleTenantHsmInstancesResponse (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class ListSingleTenantHsmInstancesResponse : IMessage<ListSingleTenantHsmInstancesResponse>, IEquatable<ListSingleTenantHsmInstancesResponse>, IDeepCloneable<ListSingleTenantHsmInstancesResponse>, IBufferMessage, IMessage, IPageResponse<SingleTenantHsmInstance>, IEnumerable<SingleTenantHsmInstance>, IEnumerable

Reference documentation and code samples for the Google Cloud Key Management Service v1 API class ListSingleTenantHsmInstancesResponse.

Response message for [HsmManagement.ListSingleTenantHsmInstances][google.cloud.kms.v1.HsmManagement.ListSingleTenantHsmInstances].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListSingleTenantHsmInstancesResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListSingleTenantHsmInstancesResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListSingleTenantHsmInstancesResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListSingleTenantHsmInstancesResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[SingleTenantHsmInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstance), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[SingleTenantHsmInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstance), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Constructors 

### ListSingleTenantHsmInstancesResponse()
    
    
    public ListSingleTenantHsmInstancesResponse()

### ListSingleTenantHsmInstancesResponse(ListSingleTenantHsmInstancesResponse)
    
    
    public ListSingleTenantHsmInstancesResponse(ListSingleTenantHsmInstancesResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ListSingleTenantHsmInstancesResponse)`  
  
  
## Properties 

### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token to retrieve next page of results. Pass this value in [ListSingleTenantHsmInstancesRequest.page_token][google.cloud.kms.v1.ListSingleTenantHsmInstancesRequest.page_token] to retrieve the next page of results.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SingleTenantHsmInstances
    
    
    public RepeatedField<SingleTenantHsmInstance> SingleTenantHsmInstances { get; }

The list of [SingleTenantHsmInstances][google.cloud.kms.v1.SingleTenantHsmInstance].

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SingleTenantHsmInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstance)` |   
  
### TotalSize
    
    
    public int TotalSize { get; set; }

The total number of [SingleTenantHsmInstances][google.cloud.kms.v1.SingleTenantHsmInstance] that matched the query.

This field is not populated if [ListSingleTenantHsmInstancesRequest.filter][google.cloud.kms.v1.ListSingleTenantHsmInstancesRequest.filter] is applied.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<SingleTenantHsmInstance> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[SingleTenantHsmInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.SingleTenantHsmInstance)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
