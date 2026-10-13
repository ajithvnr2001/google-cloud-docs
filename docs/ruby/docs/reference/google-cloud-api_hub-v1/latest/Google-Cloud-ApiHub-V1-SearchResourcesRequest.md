---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-SearchResourcesRequest/
title: API hub V1 API - Class Google::Cloud::ApiHub::V1::SearchResourcesRequest (v1.0.3) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:06.818444+00:00
---

# API hub V1 API - Class Google::Cloud::ApiHub::V1::SearchResourcesRequest (v1.0.3)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-SearchResourcesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  API hub V1 API - Class Google::Cloud::ApiHub::V1::SearchResourcesRequest (v1.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.3 (latest)  1.0.2  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the API hub V1 API class Google::Cloud::ApiHub::V1::SearchResourcesRequest.

The [SearchResources](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHub-Rest-Client#Google__Cloud__ApiHub__V1__ApiHub__Rest__Client_search_resources_instance_ "Google::Cloud::ApiHub::V1::ApiHub::Rest::Client#search_resources \(method\)") method's request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — 

Optional. An expression that filters the list of search results.

A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be `=`. Filters are not case sensitive.

The following field names are eligible for filtering:

    * `resource_type` \- The type of resource in the search results. Must be one of the following: `Api`, `ApiOperation`, `Deployment`, `Definition`, `Spec` or `Version`. This field can only be specified once in the filter.

Here are is an example:

    * `resource_type = Api` \- The resource_type is _Api_.



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. An expression that filters the list of search results.

A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be `=`. Filters are not case sensitive.

The following field names are eligible for filtering:

    * `resource_type` \- The type of resource in the search results. Must be one of the following: `Api`, `ApiOperation`, `Deployment`, `Definition`, `Spec` or `Version`. This field can only be specified once in the filter.

Here are is an example:

    * `resource_type = Api` \- The resource_type is _Api_.



**Returns**

  * (::String) — 

Optional. An expression that filters the list of search results.

A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be `=`. Filters are not case sensitive.

The following field names are eligible for filtering:

    * `resource_type` \- The type of resource in the search results. Must be one of the following: `Api`, `ApiOperation`, `Deployment`, `Definition`, `Spec` or `Version`. This field can only be specified once in the filter.

Here are is an example:

    * `resource_type = Api` \- The resource_type is _Api_.



### #location
    
    
    def location() -> ::String

**Returns**

  * (::String) — Required. The resource name of the location which will be of the type `projects/{project_id}/locations/{location_id}`. This field is used to identify the instance of API-Hub in which resources should be searched. 



### #location=
    
    
    def location=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the location which will be of the type `projects/{project_id}/locations/{location_id}`. This field is used to identify the instance of API-Hub in which resources should be searched. 



**Returns**

  * (::String) — Required. The resource name of the location which will be of the type `projects/{project_id}/locations/{location_id}`. This field is used to identify the instance of API-Hub in which resources should be searched. 



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of search results to return. The service may return fewer than this value. If unspecified at most 10 search results will be returned. If value is negative then `INVALID_ARGUMENT` error is returned. The maximum value is 25; values above 25 will be coerced to 25. While paginating, you can specify a new page size parameter for each page of search results to be listed. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of search results to return. The service may return fewer than this value. If unspecified at most 10 search results will be returned. If value is negative then `INVALID_ARGUMENT` error is returned. The maximum value is 25; values above 25 will be coerced to 25. While paginating, you can specify a new page size parameter for each page of search results to be listed. 



**Returns**

  * (::Integer) — Optional. The maximum number of search results to return. The service may return fewer than this value. If unspecified at most 10 search results will be returned. If value is negative then `INVALID_ARGUMENT` error is returned. The maximum value is 25; values above 25 will be coerced to 25. While paginating, you can specify a new page size parameter for each page of search results to be listed. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A page token, received from a previous [SearchResources][SearchResources] call. Specify this parameter to retrieve the next page of transactions.

When paginating, you must specify the `page_token` parameter and all the other parameters except [page_size](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-SearchResourcesRequest#Google__Cloud__ApiHub__V1__SearchResourcesRequest_page_size_instance_ "Google::Cloud::ApiHub::V1::SearchResourcesRequest#page_size \(method\)") should be specified with the same value which was used in the previous call. If the other fields are set with a different value than the previous call then `INVALID_ARGUMENT` error is returned. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A page token, received from a previous [SearchResources][SearchResources] call. Specify this parameter to retrieve the next page of transactions.

When paginating, you must specify the `page_token` parameter and all the other parameters except [page_size](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-SearchResourcesRequest#Google__Cloud__ApiHub__V1__SearchResourcesRequest_page_size_instance_ "Google::Cloud::ApiHub::V1::SearchResourcesRequest#page_size \(method\)") should be specified with the same value which was used in the previous call. If the other fields are set with a different value than the previous call then `INVALID_ARGUMENT` error is returned. 




**Returns**

  * (::String) — Optional. A page token, received from a previous [SearchResources][SearchResources] call. Specify this parameter to retrieve the next page of transactions.

When paginating, you must specify the `page_token` parameter and all the other parameters except [page_size](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-SearchResourcesRequest#Google__Cloud__ApiHub__V1__SearchResourcesRequest_page_size_instance_ "Google::Cloud::ApiHub::V1::SearchResourcesRequest#page_size \(method\)") should be specified with the same value which was used in the previous call. If the other fields are set with a different value than the previous call then `INVALID_ARGUMENT` error is returned. 




### #query
    
    
    def query() -> ::String

**Returns**

  * (::String) — Required. The free text search query. This query can contain keywords which could be related to any detail of the API-Hub resources such display names, descriptions, attributes etc. 



### #query=
    
    
    def query=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The free text search query. This query can contain keywords which could be related to any detail of the API-Hub resources such display names, descriptions, attributes etc. 



**Returns**

  * (::String) — Required. The free text search query. This query can contain keywords which could be related to any detail of the API-Hub resources such display names, descriptions, attributes etc. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
