---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse
title: Discovery Engine v1beta API - Class SearchResponse (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:31.591051+00:00
---

# Discovery Engine v1beta API - Class SearchResponse (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class SearchResponse (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public sealed class SearchResponse : IMessage<SearchResponse>, IEquatable<SearchResponse>, IDeepCloneable<SearchResponse>, IBufferMessage, IMessage, IPageResponse<SearchResponse.Types.SearchResult>, IEnumerable<SearchResponse.Types.SearchResult>, IEnumerable

Reference documentation and code samples for the Discovery Engine v1beta API class SearchResponse.

Response message for [SearchService.Search][google.cloud.discoveryengine.v1beta.SearchService.Search] method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SearchResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types)[SearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types.SearchResult), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types)[SearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types.SearchResult), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Constructors 

### SearchResponse()
    
    
    public SearchResponse()

### SearchResponse(SearchResponse)
    
    
    public SearchResponse(SearchResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse)`  
  
  
## Properties 

### AppliedControls
    
    
    public RepeatedField<string> AppliedControls { get; }

Controls applied as part of the Control service.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AttributionToken
    
    
    public string AttributionToken { get; set; }

A unique search token. This should be included in the [UserEvent][google.cloud.discoveryengine.v1beta.UserEvent] logs resulting from this search, which enables accurate attribution of search model performance. This also helps to identify a request during the customer support scenarios.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CorrectedQuery
    
    
    public string CorrectedQuery { get; set; }

Contains the spell corrected query, if found. If the spell correction type is AUTOMATIC, then the search results are based on corrected_query. Otherwise the original query is used for search.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Facets
    
    
    public RepeatedField<SearchResponse.Types.Facet> Facets { get; }

Results of facets requested by user.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types)[Facet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types.Facet)` |   
  
### GeoSearchDebugInfo
    
    
    public RepeatedField<SearchResponse.Types.GeoSearchDebugInfo> GeoSearchDebugInfo { get; }

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types)[GeoSearchDebugInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types.GeoSearchDebugInfo)` |   
  
### GuidedSearchResult
    
    
    public SearchResponse.Types.GuidedSearchResult GuidedSearchResult { get; set; }

Guided search result.

**Property Value**  
---  
**Type** | **Description**  
`[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types)[GuidedSearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types.GuidedSearchResult)` |   
  
### NaturalLanguageQueryUnderstandingInfo
    
    
    public SearchResponse.Types.NaturalLanguageQueryUnderstandingInfo NaturalLanguageQueryUnderstandingInfo { get; set; }

Output only. Natural language query understanding information for the returned results.

**Property Value**  
---  
**Type** | **Description**  
`[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types)[NaturalLanguageQueryUnderstandingInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types.NaturalLanguageQueryUnderstandingInfo)` |   
  
### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token that can be sent as [SearchRequest.page_token][google.cloud.discoveryengine.v1beta.SearchRequest.page_token] to retrieve the next page. If this field is omitted, there are no subsequent pages.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OneBoxResults
    
    
    public RepeatedField<SearchResponse.Types.OneBoxResult> OneBoxResults { get; }

A list of One Box results. There can be multiple One Box results of different types.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types)[OneBoxResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types.OneBoxResult)` |   
  
### QueryExpansionInfo
    
    
    public SearchResponse.Types.QueryExpansionInfo QueryExpansionInfo { get; set; }

Query expansion information for the returned results.

**Property Value**  
---  
**Type** | **Description**  
`[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types)[QueryExpansionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types.QueryExpansionInfo)` |   
  
### RedirectUri
    
    
    public string RedirectUri { get; set; }

The URI of a customer-defined redirect page. If redirect action is triggered, no search is performed, and only [redirect_uri][google.cloud.discoveryengine.v1beta.SearchResponse.redirect_uri] and [attribution_token][google.cloud.discoveryengine.v1beta.SearchResponse.attribution_token] are set in the response.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Results
    
    
    public RepeatedField<SearchResponse.Types.SearchResult> Results { get; }

A list of matched documents. The order represents the ranking.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types)[SearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types.SearchResult)` |   
  
### SearchLinkPromotions
    
    
    public RepeatedField<SearchLinkPromotion> SearchLinkPromotions { get; }

Promotions for site search.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SearchLinkPromotion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchLinkPromotion)` |   
  
### SemanticState
    
    
    public SearchResponse.Types.SemanticState SemanticState { get; set; }

Output only. Indicates the semantic state of the search response.

**Property Value**  
---  
**Type** | **Description**  
`[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types)[SemanticState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types.SemanticState)` |   
  
### SessionInfo
    
    
    public SearchResponse.Types.SessionInfo SessionInfo { get; set; }

Session information.

Only set if [SearchRequest.session][google.cloud.discoveryengine.v1beta.SearchRequest.session] is provided. See its description for more details.

**Property Value**  
---  
**Type** | **Description**  
`[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types)[SessionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types.SessionInfo)` |   
  
### SuggestedQuery
    
    
    public string SuggestedQuery { get; set; }

Corrected query with low confidence, AKA did you mean query. Compared with corrected_query, this field is set when SpellCorrector returned a response, but FPR(full page replacement) is not triggered because the corrction is of low confidence(eg, reversed because there are matches of the original query in document corpus).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Summary
    
    
    public SearchResponse.Types.Summary Summary { get; set; }

A summary as part of the search results. This field is only returned if [SearchRequest.ContentSearchSpec.summary_spec][google.cloud.discoveryengine.v1beta.SearchRequest.ContentSearchSpec.summary_spec] is set.

**Property Value**  
---  
**Type** | **Description**  
`[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types)[Summary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types.Summary)` |   
  
### TotalSize
    
    
    public int TotalSize { get; set; }

The estimated total count of matched items irrespective of pagination. The count of [results][google.cloud.discoveryengine.v1beta.SearchResponse.results] returned by pagination may be less than the [total_size][google.cloud.discoveryengine.v1beta.SearchResponse.total_size] that matches.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<SearchResponse.Types.SearchResult> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types)[SearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.SearchResponse.Types.SearchResult)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
