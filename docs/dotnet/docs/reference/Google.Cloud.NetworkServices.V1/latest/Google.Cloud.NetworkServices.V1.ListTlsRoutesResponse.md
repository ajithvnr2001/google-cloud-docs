---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ListTlsRoutesResponse
title: Network Services v1 API - Class ListTlsRoutesResponse (1.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:05.273617+00:00
---

# Network Services v1 API - Class ListTlsRoutesResponse (1.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ListTlsRoutesResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Services v1 API - Class ListTlsRoutesResponse (1.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.0 (latest)  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ListTlsRoutesResponse : IPageResponse<TlsRoute>, IEnumerable<TlsRoute>, IEnumerable, IMessage<ListTlsRoutesResponse>, IEquatable<ListTlsRoutesResponse>, IDeepCloneable<ListTlsRoutesResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Services v1 API class ListTlsRoutesResponse.

Response returned by the ListTlsRoutes method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListTlsRoutesResponse

## Implements

[IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[TlsRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.TlsRoute), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[TlsRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.TlsRoute), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListTlsRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ListTlsRoutesResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListTlsRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ListTlsRoutesResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListTlsRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ListTlsRoutesResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkServices.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1)

## Assembly

Google.Cloud.NetworkServices.V1.dll

## Constructors 

### ListTlsRoutesResponse()
    
    
    public ListTlsRoutesResponse()

### ListTlsRoutesResponse(ListTlsRoutesResponse)
    
    
    public ListTlsRoutesResponse(ListTlsRoutesResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListTlsRoutesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.ListTlsRoutesResponse)`  
  
  
## Properties 

### NextPageToken
    
    
    public string NextPageToken { get; set; }

If there might be more results than those appearing in this response, then `next_page_token` is included. To get the next set of results, call this method again using the value of `next_page_token` as `page_token`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TlsRoutes
    
    
    public RepeatedField<TlsRoute> TlsRoutes { get; }

List of TlsRoute resources.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[TlsRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.TlsRoute)` |   
  
### Unreachable
    
    
    public RepeatedField<string> Unreachable { get; }

Unreachable resources. Populated when the request opts into [return_partial_success][google.cloud.networkservices.v1.ListTlsRoutesRequest.return_partial_success] and reading across collections e.g. when attempting to list all resources across all supported locations.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<TlsRoute> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[TlsRoute](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1/latest/Google.Cloud.NetworkServices.V1.TlsRoute)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
