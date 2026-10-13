---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.GetWriteStreamRequest
title: Google BigQuery Storage v1 API - Class GetWriteStreamRequest (3.20.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:51.909683+00:00
---

# Google BigQuery Storage v1 API - Class GetWriteStreamRequest (3.20.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.GetWriteStreamRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google BigQuery Storage v1 API - Class GetWriteStreamRequest (3.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.20.0 (latest)  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0 
    
    
    public sealed class GetWriteStreamRequest : IMessage<GetWriteStreamRequest>, IEquatable<GetWriteStreamRequest>, IDeepCloneable<GetWriteStreamRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google BigQuery Storage v1 API class GetWriteStreamRequest.

Request message for `GetWriteStreamRequest`.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetWriteStreamRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetWriteStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.GetWriteStreamRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetWriteStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.GetWriteStreamRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetWriteStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.GetWriteStreamRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1)

## Assembly

Google.Cloud.BigQuery.Storage.V1.dll

## Constructors 

### GetWriteStreamRequest()
    
    
    public GetWriteStreamRequest()

### GetWriteStreamRequest(GetWriteStreamRequest)
    
    
    public GetWriteStreamRequest(GetWriteStreamRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetWriteStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.GetWriteStreamRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. Name of the stream to get, in the form of `projects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### View
    
    
    public WriteStreamView View { get; set; }

Indicates whether to get full or partial view of the WriteStream. If not set, view returned will be basic.

**Property Value**  
---  
**Type** | **Description**  
`[WriteStreamView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.WriteStreamView)` |   
  
### WriteStreamName
    
    
    public WriteStreamName WriteStreamName { get; set; }

[WriteStreamName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.WriteStreamName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.GetWriteStreamRequest#Google_Cloud_BigQuery_Storage_V1_GetWriteStreamRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[WriteStreamName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Storage.V1/latest/Google.Cloud.BigQuery.Storage.V1.WriteStreamName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
