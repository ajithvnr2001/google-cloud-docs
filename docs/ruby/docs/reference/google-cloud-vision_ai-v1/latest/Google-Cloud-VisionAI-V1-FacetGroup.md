---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetGroup/
title: Vision AI V1 API - Class Google::Cloud::VisionAI::V1::FacetGroup (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:00:51.618239+00:00
---

# Vision AI V1 API - Class Google::Cloud::VisionAI::V1::FacetGroup (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetGroup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vision AI V1 API - Class Google::Cloud::VisionAI::V1::FacetGroup (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.1  1.2.0  1.1.1  1.0.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vision AI V1 API class Google::Cloud::VisionAI::V1::FacetGroup.

A group of facet buckets to be passed back and forth between backend & frontend.

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

  * ([::Google::Cloud::VisionAI::V1::FacetBucketType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetBucketType)) — Facet bucket type. 



### #bucket_type=
    
    
    def bucket_type=(value) -> ::Google::Cloud::VisionAI::V1::FacetBucketType

**Parameter**

  * **value** ([::Google::Cloud::VisionAI::V1::FacetBucketType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetBucketType)) — Facet bucket type. 



**Returns**

  * ([::Google::Cloud::VisionAI::V1::FacetBucketType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetBucketType)) — Facet bucket type. 



### #buckets
    
    
    def buckets() -> ::Array<::Google::Cloud::VisionAI::V1::FacetBucket>

**Returns**

  * (::Array<[::Google::Cloud::VisionAI::V1::FacetBucket](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetBucket)>) — Buckets associated with the facet. E.g. for "Team" facet, the bucket can be 49ers, patriots, etc. 



### #buckets=
    
    
    def buckets=(value) -> ::Array<::Google::Cloud::VisionAI::V1::FacetBucket>

**Parameter**

  * **value** (::Array<[::Google::Cloud::VisionAI::V1::FacetBucket](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetBucket)>) — Buckets associated with the facet. E.g. for "Team" facet, the bucket can be 49ers, patriots, etc. 



**Returns**

  * (::Array<[::Google::Cloud::VisionAI::V1::FacetBucket](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-FacetBucket)>) — Buckets associated with the facet. E.g. for "Team" facet, the bucket can be 49ers, patriots, etc. 



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



### #facet_id
    
    
    def facet_id() -> ::String

**Returns**

  * (::String) — Unique id of the facet group. 



### #facet_id=
    
    
    def facet_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Unique id of the facet group. 



**Returns**

  * (::String) — Unique id of the facet group. 



### #fetch_matched_annotations
    
    
    def fetch_matched_annotations() -> ::Boolean

**Returns**

  * (::Boolean) — 

If true, return query matched annotations for this facet group's selection. This option is only applicable for facets based on partition level annotations. It supports the following facet values:

    * INTEGER
    * STRING (DataSchema.SearchStrategy.EXACT_SEARCH only)



### #fetch_matched_annotations=
    
    
    def fetch_matched_annotations=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — 

If true, return query matched annotations for this facet group's selection. This option is only applicable for facets based on partition level annotations. It supports the following facet values:

    * INTEGER
    * STRING (DataSchema.SearchStrategy.EXACT_SEARCH only)



**Returns**

  * (::Boolean) — 

If true, return query matched annotations for this facet group's selection. This option is only applicable for facets based on partition level annotations. It supports the following facet values:

    * INTEGER
    * STRING (DataSchema.SearchStrategy.EXACT_SEARCH only)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
