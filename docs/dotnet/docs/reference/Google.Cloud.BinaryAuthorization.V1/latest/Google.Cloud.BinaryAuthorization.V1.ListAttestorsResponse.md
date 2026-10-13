---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsResponse
title: Binary Authorization v1 API - Class ListAttestorsResponse (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:40.314321+00:00
---

# Binary Authorization v1 API - Class ListAttestorsResponse (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Binary Authorization v1 API - Class ListAttestorsResponse (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.7.0 (latest)  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0 
    
    
    public sealed class ListAttestorsResponse : IPageResponse<Attestor>, IEnumerable<Attestor>, IEnumerable, IMessage<ListAttestorsResponse>, IEquatable<ListAttestorsResponse>, IDeepCloneable<ListAttestorsResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Binary Authorization v1 API class ListAttestorsResponse.

Response message for [BinauthzManagementServiceV1.ListAttestors][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.ListAttestors].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListAttestorsResponse

## Implements

[IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.Attestor), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.Attestor), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BinaryAuthorization.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1)

## Assembly

Google.Cloud.BinaryAuthorization.V1.dll

## Constructors 

### ListAttestorsResponse()
    
    
    public ListAttestorsResponse()

### ListAttestorsResponse(ListAttestorsResponse)
    
    
    public ListAttestorsResponse(ListAttestorsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListAttestorsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsResponse)`  
  
  
## Properties 

### Attestors
    
    
    public RepeatedField<Attestor> Attestors { get; }

The list of [attestors][google.cloud.binaryauthorization.v1.Attestor].

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.Attestor)` |   
  
### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token to retrieve the next page of results. Pass this value in the [ListAttestorsRequest.page_token][google.cloud.binaryauthorization.v1.ListAttestorsRequest.page_token] field in the subsequent call to the `ListAttestors` method to retrieve the next page of results.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<Attestor> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[Attestor](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.Attestor)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
