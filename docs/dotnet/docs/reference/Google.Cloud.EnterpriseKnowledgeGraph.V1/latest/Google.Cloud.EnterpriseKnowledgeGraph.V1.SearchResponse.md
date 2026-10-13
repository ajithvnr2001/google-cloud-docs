---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.SearchResponse
title: Enterprise Knowledge Graph v1 API - Class SearchResponse (1.0.0-beta05) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:46.818022+00:00
---

# Enterprise Knowledge Graph v1 API - Class SearchResponse (1.0.0-beta05)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.SearchResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Enterprise Knowledge Graph v1 API - Class SearchResponse (1.0.0-beta05) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta05 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.SearchResponse)
  * [ 1.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/1.0.0-beta04/Google.Cloud.EnterpriseKnowledgeGraph.V1.SearchResponse)


    
    
    public sealed class SearchResponse : IMessage<SearchResponse>, IEquatable<SearchResponse>, IDeepCloneable<SearchResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Enterprise Knowledge Graph v1 API class SearchResponse.

Response message for [EnterpriseKnowledgeGraphService.Search][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Search].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SearchResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.SearchResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.SearchResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.SearchResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.EnterpriseKnowledgeGraph.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1)

## Assembly

Google.Cloud.EnterpriseKnowledgeGraph.V1.dll

## Constructors 

### SearchResponse()
    
    
    public SearchResponse()

### SearchResponse(SearchResponse)
    
    
    public SearchResponse(SearchResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.SearchResponse)`  
  
  
## Properties 

### Context
    
    
    public Value Context { get; set; }

The local context applicable for the response. See more details at <http://www.w3.org/TR/json-ld/#context-definitions>.

**Property Value**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html)` |   
  
### ItemListElement
    
    
    public ListValue ItemListElement { get; set; }

The item list of search results.

**Property Value**  
---  
**Type** | **Description**  
`[ListValue](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.ListValue.html)` |   
  
### Type
    
    
    public Value Type { get; set; }

The schema type of top-level JSON-LD object, e.g. ItemList.

**Property Value**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
