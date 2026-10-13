---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse
title: Discovery Engine v1 API - Class SearchResponse (1.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:01.137029+00:00
---

# Discovery Engine v1 API - Class SearchResponse (1.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1 API - Class SearchResponse (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0-beta06 
    
    
    public sealed class SearchResponse : IMessage<SearchResponse>, IEquatable<SearchResponse>, IDeepCloneable<SearchResponse>, IBufferMessage, IMessage, IPageResponse<SearchResponse.Types.SearchResult>, IEnumerable<SearchResponse.Types.SearchResult>, IEnumerable

Reference documentation and code samples for the Discovery Engine v1 API class SearchResponse.

Response message for [SearchService.Search][google.cloud.discoveryengine.v1.SearchService.Search] method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SearchResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types)[SearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.SearchResult), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types)[SearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.SearchResult), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1)

## Assembly

Google.Cloud.DiscoveryEngine.V1.dll

## Constructors 

### SearchResponse()
    
    
    public SearchResponse()

### SearchResponse(SearchResponse)
    
    
    public SearchResponse(SearchResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)`  
  
  
## Properties 

### AppliedControls
    
    
    public RepeatedField<string> AppliedControls { get; }

Optional. Controls applied as part of the Control service.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AppliedControlsAsControlNames
    
    
    public ResourceNameList<ControlName> AppliedControlsAsControlNames { get; }

[ControlName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ControlName)-typed view over the [AppliedControls](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse#Google_Cloud_DiscoveryEngine_V1_SearchResponse_AppliedControls) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceNameList](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNameList-1.html)[ControlName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ControlName)` |   
  
### AttributionToken
    
    
    public string AttributionToken { get; set; }

A unique search token. This should be included in the [UserEvent][google.cloud.discoveryengine.v1.UserEvent] logs resulting from this search, which enables accurate attribution of search model performance. This also helps to identify a request during the customer support scenarios.

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
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types)[Facet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.Facet)` |   
  
### NaturalLanguageQueryUnderstandingInfo
    
    
    public SearchResponse.Types.NaturalLanguageQueryUnderstandingInfo NaturalLanguageQueryUnderstandingInfo { get; set; }

Output only. Natural language query understanding information for the returned results.

**Property Value**  
---  
**Type** | **Description**  
`[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types)[NaturalLanguageQueryUnderstandingInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.NaturalLanguageQueryUnderstandingInfo)` |   
  
### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token that can be sent as [SearchRequest.page_token][google.cloud.discoveryengine.v1.SearchRequest.page_token] to retrieve the next page. If this field is omitted, there are no subsequent pages.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### QueryExpansionInfo
    
    
    public SearchResponse.Types.QueryExpansionInfo QueryExpansionInfo { get; set; }

Query expansion information for the returned results.

**Property Value**  
---  
**Type** | **Description**  
`[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types)[QueryExpansionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.QueryExpansionInfo)` |   
  
### RedirectUri
    
    
    public string RedirectUri { get; set; }

The URI of a customer-defined redirect page. If redirect action is triggered, no search is performed, and only [redirect_uri][google.cloud.discoveryengine.v1.SearchResponse.redirect_uri] and [attribution_token][google.cloud.discoveryengine.v1.SearchResponse.attribution_token] are set in the response.

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
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types)[SearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.SearchResult)` |   
  
### SearchLinkPromotions
    
    
    public RepeatedField<SearchLinkPromotion> SearchLinkPromotions { get; }

Promotions for site search.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SearchLinkPromotion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchLinkPromotion)` |   
  
### SemanticState
    
    
    public SearchResponse.Types.SemanticState SemanticState { get; set; }

Output only. Indicates the semantic state of the search response.

**Property Value**  
---  
**Type** | **Description**  
`[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types)[SemanticState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.SemanticState)` |   
  
### SessionInfo
    
    
    public SearchResponse.Types.SessionInfo SessionInfo { get; set; }

Session information.

Only set if [SearchRequest.session][google.cloud.discoveryengine.v1.SearchRequest.session] is provided. See its description for more details.

**Property Value**  
---  
**Type** | **Description**  
`[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types)[SessionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.SessionInfo)` |   
  
### Summary
    
    
    public SearchResponse.Types.Summary Summary { get; set; }

A summary as part of the search results. This field is only returned if [SearchRequest.ContentSearchSpec.summary_spec][google.cloud.discoveryengine.v1.SearchRequest.ContentSearchSpec.summary_spec] is set.

**Property Value**  
---  
**Type** | **Description**  
`[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types)[Summary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.Summary)` |   
  
### TotalSize
    
    
    public int TotalSize { get; set; }

The estimated total count of matched items irrespective of pagination. The count of [results][google.cloud.discoveryengine.v1.SearchResponse.results] returned by pagination may be less than the [total_size][google.cloud.discoveryengine.v1.SearchResponse.total_size] that matches.

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
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[SearchResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types)[SearchResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SearchResponse.Types.SearchResult)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
