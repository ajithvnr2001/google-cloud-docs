---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsRequest
title: Binary Authorization v1 API - Class ListAttestorsRequest (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:39.820359+00:00
---

# Binary Authorization v1 API - Class ListAttestorsRequest (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Binary Authorization v1 API - Class ListAttestorsRequest (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.7.0 (latest)  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0 
    
    
    public sealed class ListAttestorsRequest : IPageRequest, IMessage<ListAttestorsRequest>, IEquatable<ListAttestorsRequest>, IDeepCloneable<ListAttestorsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Binary Authorization v1 API class ListAttestorsRequest.

Request message for [BinauthzManagementServiceV1.ListAttestors][google.cloud.binaryauthorization.v1.BinauthzManagementServiceV1.ListAttestors].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListAttestorsRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListAttestorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListAttestorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListAttestorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BinaryAuthorization.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1)

## Assembly

Google.Cloud.BinaryAuthorization.V1.dll

## Constructors 

### ListAttestorsRequest()
    
    
    public ListAttestorsRequest()

### ListAttestorsRequest(ListAttestorsRequest)
    
    
    public ListAttestorsRequest(ListAttestorsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListAttestorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

Requested page size. The server may return fewer results than requested. If unspecified, the server will pick an appropriate default.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

A token identifying a page of results the server should return. Typically, this is the value of [ListAttestorsResponse.next_page_token][google.cloud.binaryauthorization.v1.ListAttestorsResponse.next_page_token] returned from the previous call to the `ListAttestors` method.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The resource name of the project associated with the [attestors][google.cloud.binaryauthorization.v1.Attestor], in the format `projects/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsProjectName
    
    
    public ProjectName ParentAsProjectName { get; set; }

[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1/latest/Google.Cloud.BinaryAuthorization.V1.ListAttestorsRequest#Google_Cloud_BinaryAuthorization_V1_ListAttestorsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
