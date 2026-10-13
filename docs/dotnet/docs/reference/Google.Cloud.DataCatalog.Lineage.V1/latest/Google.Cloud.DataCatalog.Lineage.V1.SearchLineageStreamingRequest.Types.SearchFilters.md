---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.SearchFilters
title: Data Lineage v1 API - Class SearchLineageStreamingRequest.Types.SearchFilters (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:40.103579+00:00
---

# Data Lineage v1 API - Class SearchLineageStreamingRequest.Types.SearchFilters (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.SearchFilters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Lineage v1 API - Class SearchLineageStreamingRequest.Types.SearchFilters (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class SearchLineageStreamingRequest.Types.SearchFilters : IMessage<SearchLineageStreamingRequest.Types.SearchFilters>, IEquatable<SearchLineageStreamingRequest.Types.SearchFilters>, IDeepCloneable<SearchLineageStreamingRequest.Types.SearchFilters>, IBufferMessage, IMessage

Reference documentation and code samples for the Data Lineage v1 API class SearchLineageStreamingRequest.Types.SearchFilters.

Filters for the search.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SearchLineageStreamingRequest.Types.SearchFilters

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types)[SearchFilters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.SearchFilters), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types)[SearchFilters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.SearchFilters), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types)[SearchFilters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.SearchFilters), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DataCatalog.Lineage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1)

## Assembly

Google.Cloud.DataCatalog.Lineage.V1.dll

## Constructors 

### SearchFilters()
    
    
    public SearchFilters()

### SearchFilters(SearchFilters)
    
    
    public SearchFilters(SearchLineageStreamingRequest.Types.SearchFilters other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types)[SearchFilters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.SearchFilters)`  
  
  
## Properties 

### DependencyTypes
    
    
    public RepeatedField<DependencyType> DependencyTypes { get; }

Optional. Types of dependencies between entities to retrieve. If unspecified, all dependency types are returned.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[DependencyType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.DependencyType)` |   
  
### EntitySet
    
    
    public SearchLineageStreamingRequest.Types.EntitySet EntitySet { get; set; }

Optional. Entity set restriction. If unspecified, the method returns all entities.

**Property Value**  
---  
**Type** | **Description**  
`[SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types)[EntitySet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.EntitySet)` |   
  
### TimeRange
    
    
    public Interval TimeRange { get; set; }

Optional. Time interval to search for lineage. If unspecified, all lineage is returned. Currently, at most one of `start_time` and `end_time` can be set.

**Property Value**  
---  
**Type** | **Description**  
`[Interval](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Interval.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
