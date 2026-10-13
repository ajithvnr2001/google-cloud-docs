---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::SearchResponse (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:36.291883+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::SearchResponse (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::SearchResponse (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::SearchResponse.

Response message for [SearchService.Search](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchService-Client#Google__Cloud__DiscoveryEngine__V1beta__SearchService__Client_search_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchService::Client#search \(method\)") method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #applied_controls
    
    
    def applied_controls() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Controls applied as part of the Control service. 



### #applied_controls=
    
    
    def applied_controls=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Controls applied as part of the Control service. 



**Returns**

  * (::Array<::String>) — Controls applied as part of the Control service. 



### #attribution_token
    
    
    def attribution_token() -> ::String

**Returns**

  * (::String) — A unique search token. This should be included in the [UserEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent "Google::Cloud::DiscoveryEngine::V1beta::UserEvent \(class\)") logs resulting from this search, which enables accurate attribution of search model performance. This also helps to identify a request during the customer support scenarios. 



### #attribution_token=
    
    
    def attribution_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A unique search token. This should be included in the [UserEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent "Google::Cloud::DiscoveryEngine::V1beta::UserEvent \(class\)") logs resulting from this search, which enables accurate attribution of search model performance. This also helps to identify a request during the customer support scenarios. 



**Returns**

  * (::String) — A unique search token. This should be included in the [UserEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UserEvent "Google::Cloud::DiscoveryEngine::V1beta::UserEvent \(class\)") logs resulting from this search, which enables accurate attribution of search model performance. This also helps to identify a request during the customer support scenarios. 



### #corrected_query
    
    
    def corrected_query() -> ::String

**Returns**

  * (::String) — Contains the spell corrected query, if found. If the spell correction type is AUTOMATIC, then the search results are based on corrected_query. Otherwise the original query is used for search. 



### #corrected_query=
    
    
    def corrected_query=(value) -> ::String

**Parameter**

  * **value** (::String) — Contains the spell corrected query, if found. If the spell correction type is AUTOMATIC, then the search results are based on corrected_query. Otherwise the original query is used for search. 



**Returns**

  * (::String) — Contains the spell corrected query, if found. If the spell correction type is AUTOMATIC, then the search results are based on corrected_query. Otherwise the original query is used for search. 



### #facets
    
    
    def facets() -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::Facet>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::Facet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-Facet)>) — Results of facets requested by user. 



### #facets=
    
    
    def facets=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::Facet>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::Facet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-Facet)>) — Results of facets requested by user. 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::Facet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-Facet)>) — Results of facets requested by user. 



### #geo_search_debug_info
    
    
    def geo_search_debug_info() -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::GeoSearchDebugInfo>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::GeoSearchDebugInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-GeoSearchDebugInfo)>) 



### #geo_search_debug_info=
    
    
    def geo_search_debug_info=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::GeoSearchDebugInfo>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::GeoSearchDebugInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-GeoSearchDebugInfo)>) 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::GeoSearchDebugInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-GeoSearchDebugInfo)>) 



### #guided_search_result
    
    
    def guided_search_result() -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::GuidedSearchResult

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::GuidedSearchResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-GuidedSearchResult)) — Guided search result. 



### #guided_search_result=
    
    
    def guided_search_result=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::GuidedSearchResult

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::GuidedSearchResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-GuidedSearchResult)) — Guided search result. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::GuidedSearchResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-GuidedSearchResult)) — Guided search result. 



### #natural_language_query_understanding_info
    
    
    def natural_language_query_understanding_info() -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::NaturalLanguageQueryUnderstandingInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-NaturalLanguageQueryUnderstandingInfo)) — Output only. Natural language query understanding information for the returned results. 



### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — A token that can be sent as [SearchRequest.page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_page_token_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#page_token \(method\)") to retrieve the next page. If this field is omitted, there are no subsequent pages. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token that can be sent as [SearchRequest.page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_page_token_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#page_token \(method\)") to retrieve the next page. If this field is omitted, there are no subsequent pages. 



**Returns**

  * (::String) — A token that can be sent as [SearchRequest.page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_page_token_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#page_token \(method\)") to retrieve the next page. If this field is omitted, there are no subsequent pages. 



### #one_box_results
    
    
    def one_box_results() -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::OneBoxResult>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::OneBoxResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-OneBoxResult)>) — A list of One Box results. There can be multiple One Box results of different types. 



### #one_box_results=
    
    
    def one_box_results=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::OneBoxResult>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::OneBoxResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-OneBoxResult)>) — A list of One Box results. There can be multiple One Box results of different types. 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::OneBoxResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-OneBoxResult)>) — A list of One Box results. There can be multiple One Box results of different types. 



### #query_expansion_info
    
    
    def query_expansion_info() -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::QueryExpansionInfo

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::QueryExpansionInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-QueryExpansionInfo)) — Query expansion information for the returned results. 



### #query_expansion_info=
    
    
    def query_expansion_info=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::QueryExpansionInfo

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::QueryExpansionInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-QueryExpansionInfo)) — Query expansion information for the returned results. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::QueryExpansionInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-QueryExpansionInfo)) — Query expansion information for the returned results. 



### #redirect_uri
    
    
    def redirect_uri() -> ::String

**Returns**

  * (::String) — The URI of a customer-defined redirect page. If redirect action is triggered, no search is performed, and only [redirect_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse_redirect_uri_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse#redirect_uri \(method\)") and [attribution_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse_attribution_token_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse#attribution_token \(method\)") are set in the response. 



### #redirect_uri=
    
    
    def redirect_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — The URI of a customer-defined redirect page. If redirect action is triggered, no search is performed, and only [redirect_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse_redirect_uri_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse#redirect_uri \(method\)") and [attribution_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse_attribution_token_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse#attribution_token \(method\)") are set in the response. 



**Returns**

  * (::String) — The URI of a customer-defined redirect page. If redirect action is triggered, no search is performed, and only [redirect_uri](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse_redirect_uri_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse#redirect_uri \(method\)") and [attribution_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse_attribution_token_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse#attribution_token \(method\)") are set in the response. 



### #results
    
    
    def results() -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::SearchResult>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::SearchResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-SearchResult)>) — A list of matched documents. The order represents the ranking. 



### #results=
    
    
    def results=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::SearchResult>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::SearchResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-SearchResult)>) — A list of matched documents. The order represents the ranking. 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::SearchResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-SearchResult)>) — A list of matched documents. The order represents the ranking. 



### #search_link_promotions
    
    
    def search_link_promotions() -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::SearchLinkPromotion>

**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::SearchLinkPromotion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchLinkPromotion)>) — Promotions for site search. 



### #search_link_promotions=
    
    
    def search_link_promotions=(value) -> ::Array<::Google::Cloud::DiscoveryEngine::V1beta::SearchLinkPromotion>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::SearchLinkPromotion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchLinkPromotion)>) — Promotions for site search. 



**Returns**

  * (::Array<[::Google::Cloud::DiscoveryEngine::V1beta::SearchLinkPromotion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchLinkPromotion)>) — Promotions for site search. 



### #semantic_state
    
    
    def semantic_state() -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::SemanticState

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::SemanticState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-SemanticState)) — Output only. Indicates the semantic state of the search response. 



### #session_info
    
    
    def session_info() -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::SessionInfo

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::SessionInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-SessionInfo)) — Session information.

Only set if [SearchRequest.session](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_session_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#session \(method\)") is provided. See its description for more details. 




### #session_info=
    
    
    def session_info=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::SessionInfo

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::SessionInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-SessionInfo)) — Session information.

Only set if [SearchRequest.session](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_session_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#session \(method\)") is provided. See its description for more details. 




**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::SessionInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-SessionInfo)) — Session information.

Only set if [SearchRequest.session](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest_session_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest#session \(method\)") is provided. See its description for more details. 




### #suggested_query
    
    
    def suggested_query() -> ::String

**Returns**

  * (::String) — Corrected query with low confidence, AKA did you mean query. Compared with corrected_query, this field is set when SpellCorrector returned a response, but FPR(full page replacement) is not triggered because the corrction is of low confidence(eg, reversed because there are matches of the original query in document corpus). 



### #suggested_query=
    
    
    def suggested_query=(value) -> ::String

**Parameter**

  * **value** (::String) — Corrected query with low confidence, AKA did you mean query. Compared with corrected_query, this field is set when SpellCorrector returned a response, but FPR(full page replacement) is not triggered because the corrction is of low confidence(eg, reversed because there are matches of the original query in document corpus). 



**Returns**

  * (::String) — Corrected query with low confidence, AKA did you mean query. Compared with corrected_query, this field is set when SpellCorrector returned a response, but FPR(full page replacement) is not triggered because the corrction is of low confidence(eg, reversed because there are matches of the original query in document corpus). 



### #summary
    
    
    def summary() -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::Summary

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::Summary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-Summary)) — A summary as part of the search results. This field is only returned if [SearchRequest.ContentSearchSpec.summary_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest-ContentSearchSpec#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest__ContentSearchSpec_summary_spec_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::ContentSearchSpec#summary_spec \(method\)") is set. 



### #summary=
    
    
    def summary=(value) -> ::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::Summary

**Parameter**

  * **value** ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::Summary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-Summary)) — A summary as part of the search results. This field is only returned if [SearchRequest.ContentSearchSpec.summary_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest-ContentSearchSpec#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest__ContentSearchSpec_summary_spec_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::ContentSearchSpec#summary_spec \(method\)") is set. 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SearchResponse::Summary](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse-Summary)) — A summary as part of the search results. This field is only returned if [SearchRequest.ContentSearchSpec.summary_spec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchRequest-ContentSearchSpec#Google__Cloud__DiscoveryEngine__V1beta__SearchRequest__ContentSearchSpec_summary_spec_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchRequest::ContentSearchSpec#summary_spec \(method\)") is set. 



### #total_size
    
    
    def total_size() -> ::Integer

**Returns**

  * (::Integer) — The estimated total count of matched items irrespective of pagination. The count of [results](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse_results_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse#results \(method\)") returned by pagination may be less than the [total_size](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse_total_size_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse#total_size \(method\)") that matches. 



### #total_size=
    
    
    def total_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The estimated total count of matched items irrespective of pagination. The count of [results](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse_results_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse#results \(method\)") returned by pagination may be less than the [total_size](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse_total_size_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse#total_size \(method\)") that matches. 



**Returns**

  * (::Integer) — The estimated total count of matched items irrespective of pagination. The count of [results](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse_results_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse#results \(method\)") returned by pagination may be less than the [total_size](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SearchResponse#Google__Cloud__DiscoveryEngine__V1beta__SearchResponse_total_size_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SearchResponse#total_size \(method\)") that matches. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
