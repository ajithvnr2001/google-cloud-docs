---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.RootCriteria
title: Data Lineage v1 API - Class SearchLineageStreamingRequest.Types.RootCriteria (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:39.213106+00:00
---

# Data Lineage v1 API - Class SearchLineageStreamingRequest.Types.RootCriteria (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.RootCriteria

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Lineage v1 API - Class SearchLineageStreamingRequest.Types.RootCriteria (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class SearchLineageStreamingRequest.Types.RootCriteria : IMessage<SearchLineageStreamingRequest.Types.RootCriteria>, IEquatable<SearchLineageStreamingRequest.Types.RootCriteria>, IDeepCloneable<SearchLineageStreamingRequest.Types.RootCriteria>, IBufferMessage, IMessage

Reference documentation and code samples for the Data Lineage v1 API class SearchLineageStreamingRequest.Types.RootCriteria.

Criteria for the root of the search.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SearchLineageStreamingRequest.Types.RootCriteria

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types)[RootCriteria](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.RootCriteria), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types)[RootCriteria](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.RootCriteria), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types)[RootCriteria](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.RootCriteria), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DataCatalog.Lineage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1)

## Assembly

Google.Cloud.DataCatalog.Lineage.V1.dll

## Constructors 

### RootCriteria()
    
    
    public RootCriteria()

### RootCriteria(RootCriteria)
    
    
    public RootCriteria(SearchLineageStreamingRequest.Types.RootCriteria other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types)[RootCriteria](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.RootCriteria)`  
  
  
## Properties 

### CriteriaCase
    
    
    public SearchLineageStreamingRequest.Types.RootCriteria.CriteriaOneofCase CriteriaCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[SearchLineageStreamingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types)[RootCriteria](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.RootCriteria)[CriteriaOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.SearchLineageStreamingRequest.Types.RootCriteria.CriteriaOneofCase)` |   
  
### Entities
    
    
    public MultipleEntityReference Entities { get; set; }

Optional. The entities to initiate the search from. Entities can be specified by FQN only, or by FQN and field. To search by FQN and all available fields for that FQN, use the wildcard `*` as the field value.

**Property Value**  
---  
**Type** | **Description**  
`[MultipleEntityReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataCatalog.Lineage.V1/latest/Google.Cloud.DataCatalog.Lineage.V1.MultipleEntityReference)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
