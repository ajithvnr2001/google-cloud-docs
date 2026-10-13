---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vector_search-v1/latest/Google-Cloud-VectorSearch-V1-ListCollectionsResponse/
title: Vector Search V1 API - Class Google::Cloud::VectorSearch::V1::ListCollectionsResponse (v0.3.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:17.423262+00:00
---

# Vector Search V1 API - Class Google::Cloud::VectorSearch::V1::ListCollectionsResponse (v0.3.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vector_search-v1/latest/Google-Cloud-VectorSearch-V1-ListCollectionsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vector Search V1 API - Class Google::Cloud::VectorSearch::V1::ListCollectionsResponse (v0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.1.1 

Reference documentation and code samples for the Vector Search V1 API class Google::Cloud::VectorSearch::V1::ListCollectionsResponse.

Message for response to listing Collections

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #collections
    
    
    def collections() -> ::Array<::Google::Cloud::VectorSearch::V1::Collection>

**Returns**

  * (::Array<[::Google::Cloud::VectorSearch::V1::Collection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vector_search-v1/latest/Google-Cloud-VectorSearch-V1-Collection)>) — The list of Collection 



### #collections=
    
    
    def collections=(value) -> ::Array<::Google::Cloud::VectorSearch::V1::Collection>

**Parameter**

  * **value** (::Array<[::Google::Cloud::VectorSearch::V1::Collection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vector_search-v1/latest/Google-Cloud-VectorSearch-V1-Collection)>) — The list of Collection 



**Returns**

  * (::Array<[::Google::Cloud::VectorSearch::V1::Collection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vector_search-v1/latest/Google-Cloud-VectorSearch-V1-Collection)>) — The list of Collection 



### #next_page_token
    
    
    def next_page_token() -> ::String

**Returns**

  * (::String) — A token identifying a page of results the server should return. 



### #next_page_token=
    
    
    def next_page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A token identifying a page of results the server should return. 



**Returns**

  * (::String) — A token identifying a page of results the server should return. 



### #unreachable
    
    
    def unreachable() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Unordered list. Locations that could not be reached. 



### #unreachable=
    
    
    def unreachable=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Unordered list. Locations that could not be reached. 



**Returns**

  * (::Array<::String>) — Unordered list. Locations that could not be reached. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
