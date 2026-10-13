---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetProperty/
title: Vision AI V1 API - Class Google::Cloud::VisionAI::V1::FacetProperty (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:10.672385+00:00
---

# Vision AI V1 API - Class Google::Cloud::VisionAI::V1::FacetProperty (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetProperty/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vision AI V1 API - Class Google::Cloud::VisionAI::V1::FacetProperty (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.1  1.2.0  1.1.1  1.0.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vision AI V1 API class Google::Cloud::VisionAI::V1::FacetProperty.

Central configuration for a facet.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #bucket_type
    
    
    def bucket_type() -> ::Google::Cloud::VisionAI::V1::FacetBucketType

**Returns**

  * ([::Google::Cloud::VisionAI::V1::FacetBucketType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetBucketType)) — Facet bucket type e.g. value, range. 



### #bucket_type=
    
    
    def bucket_type=(value) -> ::Google::Cloud::VisionAI::V1::FacetBucketType

**Parameter**

  * **value** ([::Google::Cloud::VisionAI::V1::FacetBucketType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetBucketType)) — Facet bucket type e.g. value, range. 



**Returns**

  * ([::Google::Cloud::VisionAI::V1::FacetBucketType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetBucketType)) — Facet bucket type e.g. value, range. 



### #custom_range_bucket_spec
    
    
    def custom_range_bucket_spec() -> ::Google::Cloud::VisionAI::V1::FacetProperty::CustomRangeBucketSpec

**Returns**

  * ([::Google::Cloud::VisionAI::V1::FacetProperty::CustomRangeBucketSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetProperty-CustomRangeBucketSpec)) — Custom range facet bucket config.

Note: The following fields are mutually exclusive: `custom_range_bucket_spec`, `fixed_range_bucket_spec`, `datetime_bucket_spec`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #custom_range_bucket_spec=
    
    
    def custom_range_bucket_spec=(value) -> ::Google::Cloud::VisionAI::V1::FacetProperty::CustomRangeBucketSpec

**Parameter**

  * **value** ([::Google::Cloud::VisionAI::V1::FacetProperty::CustomRangeBucketSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetProperty-CustomRangeBucketSpec)) — Custom range facet bucket config.

Note: The following fields are mutually exclusive: `custom_range_bucket_spec`, `fixed_range_bucket_spec`, `datetime_bucket_spec`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::VisionAI::V1::FacetProperty::CustomRangeBucketSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetProperty-CustomRangeBucketSpec)) — Custom range facet bucket config.

Note: The following fields are mutually exclusive: `custom_range_bucket_spec`, `fixed_range_bucket_spec`, `datetime_bucket_spec`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #datetime_bucket_spec
    
    
    def datetime_bucket_spec() -> ::Google::Cloud::VisionAI::V1::FacetProperty::DateTimeBucketSpec

**Returns**

  * ([::Google::Cloud::VisionAI::V1::FacetProperty::DateTimeBucketSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetProperty-DateTimeBucketSpec)) — Datetime range facet bucket config.

Note: The following fields are mutually exclusive: `datetime_bucket_spec`, `fixed_range_bucket_spec`, `custom_range_bucket_spec`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #datetime_bucket_spec=
    
    
    def datetime_bucket_spec=(value) -> ::Google::Cloud::VisionAI::V1::FacetProperty::DateTimeBucketSpec

**Parameter**

  * **value** ([::Google::Cloud::VisionAI::V1::FacetProperty::DateTimeBucketSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetProperty-DateTimeBucketSpec)) — Datetime range facet bucket config.

Note: The following fields are mutually exclusive: `datetime_bucket_spec`, `fixed_range_bucket_spec`, `custom_range_bucket_spec`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::VisionAI::V1::FacetProperty::DateTimeBucketSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetProperty-DateTimeBucketSpec)) — Datetime range facet bucket config.

Note: The following fields are mutually exclusive: `datetime_bucket_spec`, `fixed_range_bucket_spec`, `custom_range_bucket_spec`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Display name of the facet. To be used by UI for facet rendering. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Display name of the facet. To be used by UI for facet rendering. 



**Returns**

  * (::String) — Display name of the facet. To be used by UI for facet rendering. 



### #fixed_range_bucket_spec
    
    
    def fixed_range_bucket_spec() -> ::Google::Cloud::VisionAI::V1::FacetProperty::FixedRangeBucketSpec

**Returns**

  * ([::Google::Cloud::VisionAI::V1::FacetProperty::FixedRangeBucketSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetProperty-FixedRangeBucketSpec)) — Fixed range facet bucket config.

Note: The following fields are mutually exclusive: `fixed_range_bucket_spec`, `custom_range_bucket_spec`, `datetime_bucket_spec`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #fixed_range_bucket_spec=
    
    
    def fixed_range_bucket_spec=(value) -> ::Google::Cloud::VisionAI::V1::FacetProperty::FixedRangeBucketSpec

**Parameter**

  * **value** ([::Google::Cloud::VisionAI::V1::FacetProperty::FixedRangeBucketSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetProperty-FixedRangeBucketSpec)) — Fixed range facet bucket config.

Note: The following fields are mutually exclusive: `fixed_range_bucket_spec`, `custom_range_bucket_spec`, `datetime_bucket_spec`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::VisionAI::V1::FacetProperty::FixedRangeBucketSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetProperty-FixedRangeBucketSpec)) — Fixed range facet bucket config.

Note: The following fields are mutually exclusive: `fixed_range_bucket_spec`, `custom_range_bucket_spec`, `datetime_bucket_spec`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #mapped_fields
    
    
    def mapped_fields() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Name of the facets, which are the dimensions users want to use to refine search results. `mapped_fields` will match UserSpecifiedDataSchema keys.

For example, user can add a bunch of UGAs with the same key, such as player:adam, player:bob, player:charles. When multiple mapped_fields are specified, will merge their value together as final facet value. E.g. home_team: a, home_team:b, away_team:a, away_team:c, when facet_field = [home_team, away_team], facet_value will be [a, b, c].

UNLESS this is a 1:1 facet dimension (mapped_fields.size() == 1) AND the mapped_field equals the parent SearchConfig.name, the parent must also contain a SearchCriteriaProperty that maps to the same fields. mapped_fields must not be empty. 




### #mapped_fields=
    
    
    def mapped_fields=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Name of the facets, which are the dimensions users want to use to refine search results. `mapped_fields` will match UserSpecifiedDataSchema keys.

For example, user can add a bunch of UGAs with the same key, such as player:adam, player:bob, player:charles. When multiple mapped_fields are specified, will merge their value together as final facet value. E.g. home_team: a, home_team:b, away_team:a, away_team:c, when facet_field = [home_team, away_team], facet_value will be [a, b, c].

UNLESS this is a 1:1 facet dimension (mapped_fields.size() == 1) AND the mapped_field equals the parent SearchConfig.name, the parent must also contain a SearchCriteriaProperty that maps to the same fields. mapped_fields must not be empty. 




**Returns**

  * (::Array<::String>) — Name of the facets, which are the dimensions users want to use to refine search results. `mapped_fields` will match UserSpecifiedDataSchema keys.

For example, user can add a bunch of UGAs with the same key, such as player:adam, player:bob, player:charles. When multiple mapped_fields are specified, will merge their value together as final facet value. E.g. home_team: a, home_team:b, away_team:a, away_team:c, when facet_field = [home_team, away_team], facet_value will be [a, b, c].

UNLESS this is a 1:1 facet dimension (mapped_fields.size() == 1) AND the mapped_field equals the parent SearchConfig.name, the parent must also contain a SearchCriteriaProperty that maps to the same fields. mapped_fields must not be empty. 




### #result_size
    
    
    def result_size() -> ::Integer

**Returns**

  * (::Integer) — Maximum number of unique bucket to return for one facet. Bucket number can be large for high-cardinality facet such as "player". We only return top-n most related ones to user. If it's <= 0, the server will decide the appropriate result_size. 



### #result_size=
    
    
    def result_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Maximum number of unique bucket to return for one facet. Bucket number can be large for high-cardinality facet such as "player". We only return top-n most related ones to user. If it's <= 0, the server will decide the appropriate result_size. 



**Returns**

  * (::Integer) — Maximum number of unique bucket to return for one facet. Bucket number can be large for high-cardinality facet such as "player". We only return top-n most related ones to user. If it's <= 0, the server will decide the appropriate result_size. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
