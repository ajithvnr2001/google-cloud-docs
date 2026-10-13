---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchAssetsRequest
title: Vision AI v1 API - Class SearchAssetsRequest (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:21.071024+00:00
---

# Vision AI v1 API - Class SearchAssetsRequest (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchAssetsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vision AI v1 API - Class SearchAssetsRequest (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class SearchAssetsRequest : IMessage<SearchAssetsRequest>, IEquatable<SearchAssetsRequest>, IDeepCloneable<SearchAssetsRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Vision AI v1 API class SearchAssetsRequest.

Request message for SearchAssets.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SearchAssetsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SearchAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchAssetsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SearchAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchAssetsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SearchAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchAssetsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VisionAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1)

## Assembly

Google.Cloud.VisionAI.V1.dll

## Constructors 

### SearchAssetsRequest()
    
    
    public SearchAssetsRequest()

### SearchAssetsRequest(SearchAssetsRequest)
    
    
    public SearchAssetsRequest(SearchAssetsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SearchAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchAssetsRequest)`  
  
  
## Properties 

### ContentTimeRanges
    
    
    public DateTimeRangeArray ContentTimeRanges { get; set; }

Time ranges that matching video content must fall within. If no ranges are provided, there will be no time restriction. This field is treated just like the criteria below, but defined separately for convenience as it is used frequently. Note that if the end_time is in the future, it will be clamped to the time the request was received.

**Property Value**  
---  
**Type** | **Description**  
`[DateTimeRangeArray](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.DateTimeRangeArray)` |   
  
### Corpus
    
    
    public string Corpus { get; set; }

Required. The parent corpus to search. Format: `projects/{project_id}/locations/{location_id}/corpora/{corpus_id}'

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CorpusAsCorpusName
    
    
    public CorpusName CorpusAsCorpusName { get; set; }

[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)-typed view over the [Corpus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchAssetsRequest#Google_Cloud_VisionAI_V1_SearchAssetsRequest_Corpus) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CorpusName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.CorpusName)` |   
  
### Criteria
    
    
    public RepeatedField<Criteria> Criteria { get; }

Criteria applied to search results.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Criteria](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.Criteria)` |   
  
### FacetSelections
    
    
    public RepeatedField<FacetGroup> FacetSelections { get; }

Stores most recent facet selection state. Only facet groups with user's selection will be presented here. Selection state is either selected or unselected. Only selected facet buckets will be used as search criteria.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[FacetGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.FacetGroup)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

The number of results to be returned in this page. If it's 0, the server will decide the appropriate page_size.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

The continuation token to fetch the next page. If empty, it means it is fetching the first page.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResultAnnotationKeys
    
    
    public RepeatedField<string> ResultAnnotationKeys { get; }

A list of annotation keys to specify the annotations to be retrieved and returned with each search result. Annotation granularity must be GRANULARITY_ASSET_LEVEL and its search strategy must not be NO_SEARCH.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SchemaKeySortingStrategy
    
    
    public SchemaKeySortingStrategy SchemaKeySortingStrategy { get; set; }

Sort by the value under the data schema key.

**Property Value**  
---  
**Type** | **Description**  
`[SchemaKeySortingStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SchemaKeySortingStrategy)` |   
  
### SearchQuery
    
    
    public string SearchQuery { get; set; }

Global search query. Allows user to search assets without needing to specify which field the value belongs to.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SortSpecCase
    
    
    public SearchAssetsRequest.SortSpecOneofCase SortSpecCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[SearchAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchAssetsRequest)[SortSpecOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SearchAssetsRequest.SortSpecOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
