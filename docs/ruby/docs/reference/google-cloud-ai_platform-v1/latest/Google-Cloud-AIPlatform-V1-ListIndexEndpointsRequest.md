---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListIndexEndpointsRequest/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::ListIndexEndpointsRequest (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:43.253023+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::ListIndexEndpointsRequest (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListIndexEndpointsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::ListIndexEndpointsRequest (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::ListIndexEndpointsRequest.

Request message for [IndexEndpointService.ListIndexEndpoints](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-IndexEndpointService-Client#Google__Cloud__AIPlatform__V1__IndexEndpointService__Client_list_index_endpoints_instance_ "Google::Cloud::AIPlatform::V1::IndexEndpointService::Client#list_index_endpoints \(method\)").

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

Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported.

    * `index_endpoint` supports = and !=. `index_endpoint` represents the IndexEndpoint ID, ie. the last segment of the IndexEndpoint's [resourcename](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-IndexEndpoint#Google__Cloud__AIPlatform__V1__IndexEndpoint_name_instance_ "Google::Cloud::AIPlatform::V1::IndexEndpoint#name \(method\)").
    * `display_name` supports =, != and regex() (uses [re2](https://github.com/google/re2/wiki/Syntax) syntax)
    * `labels` supports general map functions that is: `labels.key=value` \- key:value equality `labels.key:* or labels:key - key existence A key including a space must be quoted.`labels."a key"`.

Some examples:

    * `index_endpoint="1"`
    * `display_name="myDisplayName"`
    * `regex(display_name, "^A") -> The display name starts with an A.
    * `labels.myKey="myValue"`



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported.

    * `index_endpoint` supports = and !=. `index_endpoint` represents the IndexEndpoint ID, ie. the last segment of the IndexEndpoint's [resourcename](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-IndexEndpoint#Google__Cloud__AIPlatform__V1__IndexEndpoint_name_instance_ "Google::Cloud::AIPlatform::V1::IndexEndpoint#name \(method\)").
    * `display_name` supports =, != and regex() (uses [re2](https://github.com/google/re2/wiki/Syntax) syntax)
    * `labels` supports general map functions that is: `labels.key=value` \- key:value equality `labels.key:* or labels:key - key existence A key including a space must be quoted.`labels."a key"`.

Some examples:

    * `index_endpoint="1"`
    * `display_name="myDisplayName"`
    * `regex(display_name, "^A") -> The display name starts with an A.
    * `labels.myKey="myValue"`



**Returns**

  * (::String) — 

Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported.

    * `index_endpoint` supports = and !=. `index_endpoint` represents the IndexEndpoint ID, ie. the last segment of the IndexEndpoint's [resourcename](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-IndexEndpoint#Google__Cloud__AIPlatform__V1__IndexEndpoint_name_instance_ "Google::Cloud::AIPlatform::V1::IndexEndpoint#name \(method\)").
    * `display_name` supports =, != and regex() (uses [re2](https://github.com/google/re2/wiki/Syntax) syntax)
    * `labels` supports general map functions that is: `labels.key=value` \- key:value equality `labels.key:* or labels:key - key existence A key including a space must be quoted.`labels."a key"`.

Some examples:

    * `index_endpoint="1"`
    * `display_name="myDisplayName"`
    * `regex(display_name, "^A") -> The display name starts with an A.
    * `labels.myKey="myValue"`



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The standard list page size. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The standard list page size. 



**Returns**

  * (::Integer) — Optional. The standard list page size. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. The standard list page token. Typically obtained via [ListIndexEndpointsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListIndexEndpointsResponse#Google__Cloud__AIPlatform__V1__ListIndexEndpointsResponse_next_page_token_instance_ "Google::Cloud::AIPlatform::V1::ListIndexEndpointsResponse#next_page_token \(method\)") of the previous [IndexEndpointService.ListIndexEndpoints](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-IndexEndpointService-Client#Google__Cloud__AIPlatform__V1__IndexEndpointService__Client_list_index_endpoints_instance_ "Google::Cloud::AIPlatform::V1::IndexEndpointService::Client#list_index_endpoints \(method\)") call. 



### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The standard list page token. Typically obtained via [ListIndexEndpointsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListIndexEndpointsResponse#Google__Cloud__AIPlatform__V1__ListIndexEndpointsResponse_next_page_token_instance_ "Google::Cloud::AIPlatform::V1::ListIndexEndpointsResponse#next_page_token \(method\)") of the previous [IndexEndpointService.ListIndexEndpoints](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-IndexEndpointService-Client#Google__Cloud__AIPlatform__V1__IndexEndpointService__Client_list_index_endpoints_instance_ "Google::Cloud::AIPlatform::V1::IndexEndpointService::Client#list_index_endpoints \(method\)") call. 



**Returns**

  * (::String) — Optional. The standard list page token. Typically obtained via [ListIndexEndpointsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListIndexEndpointsResponse#Google__Cloud__AIPlatform__V1__ListIndexEndpointsResponse_next_page_token_instance_ "Google::Cloud::AIPlatform::V1::ListIndexEndpointsResponse#next_page_token \(method\)") of the previous [IndexEndpointService.ListIndexEndpoints](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-IndexEndpointService-Client#Google__Cloud__AIPlatform__V1__IndexEndpointService__Client_list_index_endpoints_instance_ "Google::Cloud::AIPlatform::V1::IndexEndpointService::Client#list_index_endpoints \(method\)") call. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the Location from which to list the IndexEndpoints. Format: `projects/{project}/locations/{location}`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the Location from which to list the IndexEndpoints. Format: `projects/{project}/locations/{location}`



**Returns**

  * (::String) — Required. The resource name of the Location from which to list the IndexEndpoints. Format: `projects/{project}/locations/{location}`



### #read_mask
    
    
    def read_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask)) — Optional. Mask specifying which fields to read. 



### #read_mask=
    
    
    def read_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask)) — Optional. Mask specifying which fields to read. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask)) — Optional. Mask specifying which fields to read. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
