---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchMode/
title: SearchMode \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:54:50.095243+00:00
---

# SearchMode  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchMode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  SearchMode Stay organized with collections  Save and categorize content based on your preferences. 

The search mode of each search request.

Enums  
---  
`SEARCH_MODE_UNSPECIFIED` | Default value. In this case both product search and faceted search will be performed. Both `[SearchResponse.SearchResult](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchResponse#SearchResult)` and `[SearchResponse.Facet](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/Facet)` will be returned.  
`PRODUCT_SEARCH_ONLY` | Only product search will be performed. The faceted search will be disabled.Only `[SearchResponse.SearchResult](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchResponse#SearchResult)` will be returned. `[SearchResponse.Facet](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/Facet)` will not be returned, even if `[SearchRequest.facet_specs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.facet_specs)` or `[SearchRequest.dynamic_facet_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.dynamic_facet_spec)` is set.  
`FACETED_SEARCH_ONLY` | Only faceted search will be performed. The product search will be disabled.When in this mode, one or both of `[SearchRequest.facet_specs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.facet_specs)` and `[SearchRequest.dynamic_facet_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.dynamic_facet_spec)` should be set. Otherwise, an INVALID_ARGUMENT error is returned. Only `[SearchResponse.Facet](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/Facet)` will be returned. `[SearchResponse.SearchResult](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchResponse#SearchResult)` will not be returned.  
`CONVERSATIONAL_SEARCH_ONLY` | Only conversational search will be performed. Product search and other search modes will be disabled.Only `[SearchResponse.ConversationalSearchResult](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchResponse#ConversationalSearchResult)` and `[SearchResponse.SearchResult](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/SearchResponse#SearchResult)` will be returned. `[SearchResponse.Facet](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/Facet)` will not be returned even if `[SearchRequest.facet_specs](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.facet_specs)` or `[SearchRequest.dynamic_facet_spec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2alpha/projects.locations.catalogs.placements/search#body.request_body.FIELDS.dynamic_facet_spec)` is set.This item is deprecated!  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
