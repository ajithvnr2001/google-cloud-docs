---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsRequest
title: Managed Service for Apache Kafka API v1 API - Class ListTopicsRequest (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:47.492374+00:00
---

# Managed Service for Apache Kafka API v1 API - Class ListTopicsRequest (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Managed Service for Apache Kafka API v1 API - Class ListTopicsRequest (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsRequest)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/1.0.0-beta07/Google.Cloud.ManagedKafka.V1.ListTopicsRequest)


    
    
    public sealed class ListTopicsRequest : IMessage<ListTopicsRequest>, IEquatable<ListTopicsRequest>, IDeepCloneable<ListTopicsRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Managed Service for Apache Kafka API v1 API class ListTopicsRequest.

Request for ListTopics.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListTopicsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListTopicsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListTopicsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListTopicsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ManagedKafka.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1)

## Assembly

Google.Cloud.ManagedKafka.V1.dll

## Constructors 

### ListTopicsRequest()
    
    
    public ListTopicsRequest()

### ListTopicsRequest(ListTopicsRequest)
    
    
    public ListTopicsRequest(ListTopicsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListTopicsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

Optional. The maximum number of topics to return. The service may return fewer than this value. If unset or zero, all topics for the parent is returned.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. A page token, received from a previous `ListTopics` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListTopics` must match the call that provided the page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent cluster whose topics are to be listed. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsClusterName
    
    
    public ClusterName ParentAsClusterName { get; set; }

[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsRequest#Google_Cloud_ManagedKafka_V1_ListTopicsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
