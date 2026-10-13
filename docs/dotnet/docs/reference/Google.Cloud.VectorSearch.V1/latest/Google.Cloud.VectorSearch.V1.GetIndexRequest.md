---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1.GetIndexRequest
title: Vector Search v1 API - Class GetIndexRequest (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:37.385594+00:00
---

# Vector Search v1 API - Class GetIndexRequest (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1.GetIndexRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vector Search v1 API - Class GetIndexRequest (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0 
    
    
    public sealed class GetIndexRequest : IMessage<GetIndexRequest>, IEquatable<GetIndexRequest>, IDeepCloneable<GetIndexRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Vector Search v1 API class GetIndexRequest.

Message for getting an Index

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetIndexRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1.GetIndexRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1.GetIndexRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1.GetIndexRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VectorSearch.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1)

## Assembly

Google.Cloud.VectorSearch.V1.dll

## Constructors 

### GetIndexRequest()
    
    
    public GetIndexRequest()

### GetIndexRequest(GetIndexRequest)
    
    
    public GetIndexRequest(GetIndexRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetIndexRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1.GetIndexRequest)`  
  
  
## Properties 

### IndexName
    
    
    public IndexName IndexName { get; set; }

[IndexName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1.IndexName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1.GetIndexRequest#Google_Cloud_VectorSearch_V1_GetIndexRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[IndexName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VectorSearch.V1/latest/Google.Cloud.VectorSearch.V1.IndexName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. Name of the resource

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
