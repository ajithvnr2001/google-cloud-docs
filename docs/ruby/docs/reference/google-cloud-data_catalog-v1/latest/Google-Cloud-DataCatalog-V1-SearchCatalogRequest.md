---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-SearchCatalogRequest/
title: Data Catalog V1 API - Class Google::Cloud::DataCatalog::V1::SearchCatalogRequest (v2.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:30.664159+00:00
---

# Data Catalog V1 API - Class Google::Cloud::DataCatalog::V1::SearchCatalogRequest (v2.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-SearchCatalogRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Catalog V1 API - Class Google::Cloud::DataCatalog::V1::SearchCatalogRequest (v2.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.1 (latest)  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.1  2.2.2  2.1.1  2.0.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.2  0.20.1  0.19.0  0.18.1  0.17.0  0.16.1  0.15.0  0.14.0  0.13.0  0.12.1  0.11.0  0.10.0  0.9.1 

Reference documentation and code samples for the Data Catalog V1 API class Google::Cloud::DataCatalog::V1::SearchCatalogRequest.

Request message for [SearchCatalog](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-DataCatalog-Client#Google__Cloud__DataCatalog__V1__DataCatalog__Client_search_catalog_instance_ "Google::Cloud::DataCatalog::V1::DataCatalog::Client#search_catalog \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #admin_search
    
    
    def admin_search() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If set, use searchAll permission granted on organizations from `include_org_ids` and projects from `include_project_ids` instead of the fine grained per resource permissions when filtering the search results. The only allowed `order_by` criteria for admin_search mode is `default`. Using this flags guarantees a full recall of the search results. 



### #admin_search=
    
    
    def admin_search=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If set, use searchAll permission granted on organizations from `include_org_ids` and projects from `include_project_ids` instead of the fine grained per resource permissions when filtering the search results. The only allowed `order_by` criteria for admin_search mode is `default`. Using this flags guarantees a full recall of the search results. 



**Returns**

  * (::Boolean) — Optional. If set, use searchAll permission granted on organizations from `include_org_ids` and projects from `include_project_ids` instead of the fine grained per resource permissions when filtering the search results. The only allowed `order_by` criteria for admin_search mode is `default`. Using this flags guarantees a full recall of the search results. 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Specifies the order of results.

Currently supported case-sensitive values are:

    * `relevance` that can only be descending
    * `last_modified_timestamp [asc|desc]` with descending (`desc`) as default
    * `default` that can only be descending

Search queries don't guarantee full recall. Results that match your query might not be returned, even in subsequent result pages. Additionally, returned (and not returned) results can vary if you repeat search queries. If you are experiencing recall issues and you don't have to fetch the results in any specific order, consider setting this parameter to `default`.

If this parameter is omitted, it defaults to the descending `relevance`. 




### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Specifies the order of results.

Currently supported case-sensitive values are:

    * `relevance` that can only be descending
    * `last_modified_timestamp [asc|desc]` with descending (`desc`) as default
    * `default` that can only be descending

Search queries don't guarantee full recall. Results that match your query might not be returned, even in subsequent result pages. Additionally, returned (and not returned) results can vary if you repeat search queries. If you are experiencing recall issues and you don't have to fetch the results in any specific order, consider setting this parameter to `default`.

If this parameter is omitted, it defaults to the descending `relevance`. 




**Returns**

  * (::String) — Specifies the order of results.

Currently supported case-sensitive values are:

    * `relevance` that can only be descending
    * `last_modified_timestamp [asc|desc]` with descending (`desc`) as default
    * `default` that can only be descending

Search queries don't guarantee full recall. Results that match your query might not be returned, even in subsequent result pages. Additionally, returned (and not returned) results can vary if you repeat search queries. If you are experiencing recall issues and you don't have to fetch the results in any specific order, consider setting this parameter to `default`.

If this parameter is omitted, it defaults to the descending `relevance`. 




### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Upper bound on the number of results you can get in a single response.

Can't be negative or 0, defaults to 10 in this case. The maximum number is 1000. If exceeded, throws an "invalid argument" exception. 




### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Upper bound on the number of results you can get in a single response.

Can't be negative or 0, defaults to 10 in this case. The maximum number is 1000. If exceeded, throws an "invalid argument" exception. 




**Returns**

  * (::Integer) — Upper bound on the number of results you can get in a single response.

Can't be negative or 0, defaults to 10 in this case. The maximum number is 1000. If exceeded, throws an "invalid argument" exception. 




### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. Pagination token that, if specified, returns the next page of search results. If empty, returns the first page.

This token is returned in the [SearchCatalogResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-SearchCatalogResponse#Google__Cloud__DataCatalog__V1__SearchCatalogResponse_next_page_token_instance_ "Google::Cloud::DataCatalog::V1::SearchCatalogResponse#next_page_token \(method\)") field of the response to a previous [SearchCatalogRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-DataCatalog-Client#Google__Cloud__DataCatalog__V1__DataCatalog__Client_search_catalog_instance_ "Google::Cloud::DataCatalog::V1::DataCatalog::Client#search_catalog \(method\)") call. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Pagination token that, if specified, returns the next page of search results. If empty, returns the first page.

This token is returned in the [SearchCatalogResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-SearchCatalogResponse#Google__Cloud__DataCatalog__V1__SearchCatalogResponse_next_page_token_instance_ "Google::Cloud::DataCatalog::V1::SearchCatalogResponse#next_page_token \(method\)") field of the response to a previous [SearchCatalogRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-DataCatalog-Client#Google__Cloud__DataCatalog__V1__DataCatalog__Client_search_catalog_instance_ "Google::Cloud::DataCatalog::V1::DataCatalog::Client#search_catalog \(method\)") call. 




**Returns**

  * (::String) — Optional. Pagination token that, if specified, returns the next page of search results. If empty, returns the first page.

This token is returned in the [SearchCatalogResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-SearchCatalogResponse#Google__Cloud__DataCatalog__V1__SearchCatalogResponse_next_page_token_instance_ "Google::Cloud::DataCatalog::V1::SearchCatalogResponse#next_page_token \(method\)") field of the response to a previous [SearchCatalogRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-DataCatalog-Client#Google__Cloud__DataCatalog__V1__DataCatalog__Client_search_catalog_instance_ "Google::Cloud::DataCatalog::V1::DataCatalog::Client#search_catalog \(method\)") call. 




### #query
    
    
    def query() -> ::String

**Returns**

  * (::String) — 

Optional. The query string with a minimum of 3 characters and specific syntax. For more information, see [Data Catalog search syntax](https://cloud.google.com/data-catalog/docs/how-to/search-reference).

An empty query string returns all data assets (in the specified scope) that you have access to.

A query string can be a simple `xyz` or qualified by predicates:

    * `name:x`
    * `column:y`
    * `description:z`



### #query=
    
    
    def query=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. The query string with a minimum of 3 characters and specific syntax. For more information, see [Data Catalog search syntax](https://cloud.google.com/data-catalog/docs/how-to/search-reference).

An empty query string returns all data assets (in the specified scope) that you have access to.

A query string can be a simple `xyz` or qualified by predicates:

    * `name:x`
    * `column:y`
    * `description:z`



**Returns**

  * (::String) — 

Optional. The query string with a minimum of 3 characters and specific syntax. For more information, see [Data Catalog search syntax](https://cloud.google.com/data-catalog/docs/how-to/search-reference).

An empty query string returns all data assets (in the specified scope) that you have access to.

A query string can be a simple `xyz` or qualified by predicates:

    * `name:x`
    * `column:y`
    * `description:z`



### #scope
    
    
    def scope() -> ::Google::Cloud::DataCatalog::V1::SearchCatalogRequest::Scope

**Returns**

  * ([::Google::Cloud::DataCatalog::V1::SearchCatalogRequest::Scope](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-SearchCatalogRequest-Scope)) — Required. The scope of this search request.

The `scope` is invalid if `include_org_ids`, `include_project_ids` are empty AND `include_gcp_public_datasets` is set to `false`. In this case, the request returns an error. 




### #scope=
    
    
    def scope=(value) -> ::Google::Cloud::DataCatalog::V1::SearchCatalogRequest::Scope

**Parameter**

  * **value** ([::Google::Cloud::DataCatalog::V1::SearchCatalogRequest::Scope](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-SearchCatalogRequest-Scope)) — Required. The scope of this search request.

The `scope` is invalid if `include_org_ids`, `include_project_ids` are empty AND `include_gcp_public_datasets` is set to `false`. In this case, the request returns an error. 




**Returns**

  * ([::Google::Cloud::DataCatalog::V1::SearchCatalogRequest::Scope](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-v1/latest/Google-Cloud-DataCatalog-V1-SearchCatalogRequest-Scope)) — Required. The scope of this search request.

The `scope` is invalid if `include_org_ids`, `include_project_ids` are empty AND `include_gcp_public_datasets` is set to `false`. In this case, the request returns an error. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
