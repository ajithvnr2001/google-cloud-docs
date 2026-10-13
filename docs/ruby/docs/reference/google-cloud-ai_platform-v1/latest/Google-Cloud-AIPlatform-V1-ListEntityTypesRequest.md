---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListEntityTypesRequest/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::ListEntityTypesRequest (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:33.664502+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::ListEntityTypesRequest (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListEntityTypesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::ListEntityTypesRequest (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::ListEntityTypesRequest.

Request message for [FeaturestoreService.ListEntityTypes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_list_entity_types_instance_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client#list_entity_types \(method\)").

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

Lists the EntityTypes that match the filter expression. The following filters are supported:

    * `create_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format.
    * `update_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format.
    * `labels`: Supports key-value equality as well as key presence.

Examples:

    * `create_time > \"2020-01-31T15:30:00.000000Z\" OR update_time > \"2020-01-31T15:30:00.000000Z\"` \--> EntityTypes created or updated after 2020-01-31T15:30:00.000000Z.
    * `labels.active = yes AND labels.env = prod` \--> EntityTypes having both (active: yes) and (env: prod) labels.
    * `labels.env: *` \--> Any EntityType which has a label with 'env' as the key.



### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Lists the EntityTypes that match the filter expression. The following filters are supported:

    * `create_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format.
    * `update_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format.
    * `labels`: Supports key-value equality as well as key presence.

Examples:

    * `create_time > \"2020-01-31T15:30:00.000000Z\" OR update_time > \"2020-01-31T15:30:00.000000Z\"` \--> EntityTypes created or updated after 2020-01-31T15:30:00.000000Z.
    * `labels.active = yes AND labels.env = prod` \--> EntityTypes having both (active: yes) and (env: prod) labels.
    * `labels.env: *` \--> Any EntityType which has a label with 'env' as the key.



**Returns**

  * (::String) — 

Lists the EntityTypes that match the filter expression. The following filters are supported:

    * `create_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format.
    * `update_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format.
    * `labels`: Supports key-value equality as well as key presence.

Examples:

    * `create_time > \"2020-01-31T15:30:00.000000Z\" OR update_time > \"2020-01-31T15:30:00.000000Z\"` \--> EntityTypes created or updated after 2020-01-31T15:30:00.000000Z.
    * `labels.active = yes AND labels.env = prod` \--> EntityTypes having both (active: yes) and (env: prod) labels.
    * `labels.env: *` \--> Any EntityType which has a label with 'env' as the key.



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — 

A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

Supported fields:

    * `entity_type_id`
    * `create_time`
    * `update_time`



### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — 

A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

Supported fields:

    * `entity_type_id`
    * `create_time`
    * `update_time`



**Returns**

  * (::String) — 

A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

Supported fields:

    * `entity_type_id`
    * `create_time`
    * `update_time`



### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of EntityTypes to return. The service may return fewer than this value. If unspecified, at most 1000 EntityTypes will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000\. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of EntityTypes to return. The service may return fewer than this value. If unspecified, at most 1000 EntityTypes will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000\. 



**Returns**

  * (::Integer) — The maximum number of EntityTypes to return. The service may return fewer than this value. If unspecified, at most 1000 EntityTypes will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000\. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — A page token, received from a previous [FeaturestoreService.ListEntityTypes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_list_entity_types_instance_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client#list_entity_types \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [FeaturestoreService.ListEntityTypes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_list_entity_types_instance_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client#list_entity_types \(method\)") must match the call that provided the page token. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A page token, received from a previous [FeaturestoreService.ListEntityTypes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_list_entity_types_instance_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client#list_entity_types \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [FeaturestoreService.ListEntityTypes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_list_entity_types_instance_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client#list_entity_types \(method\)") must match the call that provided the page token. 




**Returns**

  * (::String) — A page token, received from a previous [FeaturestoreService.ListEntityTypes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_list_entity_types_instance_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client#list_entity_types \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [FeaturestoreService.ListEntityTypes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client#Google__Cloud__AIPlatform__V1__FeaturestoreService__Client_list_entity_types_instance_ "Google::Cloud::AIPlatform::V1::FeaturestoreService::Client#list_entity_types \(method\)") must match the call that provided the page token. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the Featurestore to list EntityTypes. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the Featurestore to list EntityTypes. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`



**Returns**

  * (::String) — Required. The resource name of the Featurestore to list EntityTypes. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`



### #read_mask
    
    
    def read_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask)) — Mask specifying which fields to read. 



### #read_mask=
    
    
    def read_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask)) — Mask specifying which fields to read. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask)) — Mask specifying which fields to read. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
