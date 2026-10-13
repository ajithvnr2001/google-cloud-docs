---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.ListEndpointPoliciesResponse
title: Network Services v1beta1 API - Class ListEndpointPoliciesResponse (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:58.554723+00:00
---

# Network Services v1beta1 API - Class ListEndpointPoliciesResponse (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.ListEndpointPoliciesResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Services v1beta1 API - Class ListEndpointPoliciesResponse (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class ListEndpointPoliciesResponse : IMessage<ListEndpointPoliciesResponse>, IEquatable<ListEndpointPoliciesResponse>, IDeepCloneable<ListEndpointPoliciesResponse>, IBufferMessage, IMessage, IPageResponse<EndpointPolicy>, IEnumerable<EndpointPolicy>, IEnumerable

Reference documentation and code samples for the Network Services v1beta1 API class ListEndpointPoliciesResponse.

Response returned by the ListEndpointPolicies method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListEndpointPoliciesResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListEndpointPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.ListEndpointPoliciesResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListEndpointPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.ListEndpointPoliciesResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListEndpointPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.ListEndpointPoliciesResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[EndpointPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointPolicy), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[EndpointPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointPolicy), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkServices.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1)

## Assembly

Google.Cloud.NetworkServices.V1Beta1.dll

## Constructors 

### ListEndpointPoliciesResponse()
    
    
    public ListEndpointPoliciesResponse()

### ListEndpointPoliciesResponse(ListEndpointPoliciesResponse)
    
    
    public ListEndpointPoliciesResponse(ListEndpointPoliciesResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListEndpointPoliciesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.ListEndpointPoliciesResponse)`  
  
  
## Properties 

### EndpointPolicies
    
    
    public RepeatedField<EndpointPolicy> EndpointPolicies { get; }

List of EndpointPolicy resources.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[EndpointPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointPolicy)` |   
  
### NextPageToken
    
    
    public string NextPageToken { get; set; }

If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<EndpointPolicy> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[EndpointPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.EndpointPolicy)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
