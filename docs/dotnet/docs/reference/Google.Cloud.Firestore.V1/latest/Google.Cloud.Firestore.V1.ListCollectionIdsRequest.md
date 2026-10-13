---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.ListCollectionIdsRequest
title: Firestore v1 API - Class ListCollectionIdsRequest (4.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:38.437588+00:00
---

# Firestore v1 API - Class ListCollectionIdsRequest (4.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.ListCollectionIdsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Firestore v1 API - Class ListCollectionIdsRequest (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.1  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.5.0  2.4.0  2.3.0 
    
    
    public sealed class ListCollectionIdsRequest : IMessage<ListCollectionIdsRequest>, IEquatable<ListCollectionIdsRequest>, IDeepCloneable<ListCollectionIdsRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Firestore v1 API class ListCollectionIdsRequest.

The request for [Firestore.ListCollectionIds][google.firestore.v1.Firestore.ListCollectionIds].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListCollectionIdsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListCollectionIdsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.ListCollectionIdsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListCollectionIdsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.ListCollectionIdsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListCollectionIdsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.ListCollectionIdsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Firestore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1)

## Assembly

Google.Cloud.Firestore.V1.dll

## Constructors 

### ListCollectionIdsRequest()
    
    
    public ListCollectionIdsRequest()

### ListCollectionIdsRequest(ListCollectionIdsRequest)
    
    
    public ListCollectionIdsRequest(ListCollectionIdsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListCollectionIdsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.ListCollectionIdsRequest)`  
  
  
## Properties 

### ConsistencySelectorCase
    
    
    public ListCollectionIdsRequest.ConsistencySelectorOneofCase ConsistencySelectorCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ListCollectionIdsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.ListCollectionIdsRequest)[ConsistencySelectorOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.ListCollectionIdsRequest.ConsistencySelectorOneofCase)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

The maximum number of results to return.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

A page token. Must be a value from [ListCollectionIdsResponse][google.firestore.v1.ListCollectionIdsResponse].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent document. In the format: `projects/{project_id}/databases/{database_id}/documents/{document_path}`. For example: `projects/my-project/databases/my-database/documents/chatrooms/my-chatroom`

Use `projects/{project_id}/databases/{database_id}/documents` to list top-level collections.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ReadTime
    
    
    public Timestamp ReadTime { get; set; }

Reads documents as they were at the given time.

This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### RequestOptions
    
    
    public RequestOptions RequestOptions { get; set; }

Optional. Any additional options for the request.

**Property Value**  
---  
**Type** | **Description**  
`[RequestOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Firestore.V1/latest/Google.Cloud.Firestore.V1.RequestOptions)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
