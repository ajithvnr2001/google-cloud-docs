---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-SearchIndexEndpointRequest/
title: Vision AI V1 API - Class Google::Cloud::VisionAI::V1::SearchIndexEndpointRequest (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:00.460062+00:00
---

# Vision AI V1 API - Class Google::Cloud::VisionAI::V1::SearchIndexEndpointRequest (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-SearchIndexEndpointRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vision AI V1 API - Class Google::Cloud::VisionAI::V1::SearchIndexEndpointRequest (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.1  1.2.0  1.1.1  1.0.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vision AI V1 API class Google::Cloud::VisionAI::V1::SearchIndexEndpointRequest.

Request message for SearchIndexEndpoint.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #criteria
    
    
    def criteria() -> ::Array<::Google::Cloud::VisionAI::V1::Criteria>

**Returns**

  * (::Array<[::Google::Cloud::VisionAI::V1::Criteria](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-Criteria)>) — Criteria applied to search results. 



### #criteria=
    
    
    def criteria=(value) -> ::Array<::Google::Cloud::VisionAI::V1::Criteria>

**Parameter**

  * **value** (::Array<[::Google::Cloud::VisionAI::V1::Criteria](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-Criteria)>) — Criteria applied to search results. 



**Returns**

  * (::Array<[::Google::Cloud::VisionAI::V1::Criteria](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-Criteria)>) — Criteria applied to search results. 



### #exclusion_criteria
    
    
    def exclusion_criteria() -> ::Array<::Google::Cloud::VisionAI::V1::Criteria>

**Returns**

  * (::Array<[::Google::Cloud::VisionAI::V1::Criteria](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-Criteria)>) — Criteria to exclude from search results. Note that `fetch_matched_annotations` will be ignored. 



### #exclusion_criteria=
    
    
    def exclusion_criteria=(value) -> ::Array<::Google::Cloud::VisionAI::V1::Criteria>

**Parameter**

  * **value** (::Array<[::Google::Cloud::VisionAI::V1::Criteria](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-Criteria)>) — Criteria to exclude from search results. Note that `fetch_matched_annotations` will be ignored. 



**Returns**

  * (::Array<[::Google::Cloud::VisionAI::V1::Criteria](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-Criteria)>) — Criteria to exclude from search results. Note that `fetch_matched_annotations` will be ignored. 



### #image_query
    
    
    def image_query() -> ::Google::Cloud::VisionAI::V1::ImageQuery

**Returns**

  * ([::Google::Cloud::VisionAI::V1::ImageQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-ImageQuery)) — An image-only query.

Note: The following fields are mutually exclusive: `image_query`, `text_query`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #image_query=
    
    
    def image_query=(value) -> ::Google::Cloud::VisionAI::V1::ImageQuery

**Parameter**

  * **value** ([::Google::Cloud::VisionAI::V1::ImageQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-ImageQuery)) — An image-only query.

Note: The following fields are mutually exclusive: `image_query`, `text_query`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::VisionAI::V1::ImageQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-ImageQuery)) — An image-only query.

Note: The following fields are mutually exclusive: `image_query`, `text_query`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #index_endpoint
    
    
    def index_endpoint() -> ::String

**Returns**

  * (::String) — Required. The index endpoint to search. Format: `projects/{project_id}/locations/{location_id}/indexEndpoints/{index_endpoint_id}`



### #index_endpoint=
    
    
    def index_endpoint=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The index endpoint to search. Format: `projects/{project_id}/locations/{location_id}/indexEndpoints/{index_endpoint_id}`



**Returns**

  * (::String) — Required. The index endpoint to search. Format: `projects/{project_id}/locations/{location_id}/indexEndpoints/{index_endpoint_id}`



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Requested page size. API may return fewer results than requested. If negative, INVALID_ARGUMENT error will be returned. If unspecified or 0, API will pick a default size, which is 10. If the requested page size is larger than the maximum size, API will pick the maximum size, which is 200. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Requested page size. API may return fewer results than requested. If negative, INVALID_ARGUMENT error will be returned. If unspecified or 0, API will pick a default size, which is 10. If the requested page size is larger than the maximum size, API will pick the maximum size, which is 200. 



**Returns**

  * (::Integer) — Requested page size. API may return fewer results than requested. If negative, INVALID_ARGUMENT error will be returned. If unspecified or 0, API will pick a default size, which is 10. If the requested page size is larger than the maximum size, API will pick the maximum size, which is 200. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — The continuation token to fetch the next page. If empty, it means it is fetching the first page. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — The continuation token to fetch the next page. If empty, it means it is fetching the first page. 



**Returns**

  * (::String) — The continuation token to fetch the next page. If empty, it means it is fetching the first page. 



### #text_query
    
    
    def text_query() -> ::String

**Returns**

  * (::String) — A text-only query.

Note: The following fields are mutually exclusive: `text_query`, `image_query`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #text_query=
    
    
    def text_query=(value) -> ::String

**Parameter**

  * **value** (::String) — A text-only query.

Note: The following fields are mutually exclusive: `text_query`, `image_query`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — A text-only query.

Note: The following fields are mutually exclusive: `text_query`, `image_query`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
