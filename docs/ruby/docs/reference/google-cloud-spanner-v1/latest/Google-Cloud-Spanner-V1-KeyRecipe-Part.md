---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-KeyRecipe-Part/
title: Cloud Spanner V1 API - Class Google::Cloud::Spanner::V1::KeyRecipe::Part (v1.19.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:07.348317+00:00
---

# Cloud Spanner V1 API - Class Google::Cloud::Spanner::V1::KeyRecipe::Part (v1.19.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-KeyRecipe-Part/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Spanner V1 API - Class Google::Cloud::Spanner::V1::KeyRecipe::Part (v1.19.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.2 (latest)  1.19.1  1.18.0  1.17.1  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.1  1.9.1  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.2  0.21.0  0.20.1  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.4 

Reference documentation and code samples for the Cloud Spanner V1 API class Google::Cloud::Spanner::V1::KeyRecipe::Part.

An ssformat key is composed of a sequence of tag numbers and key column values. `Part` represents a single tag or key column value.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #identifier
    
    
    def identifier() -> ::String

**Returns**

  * (::String) — `identifier` is the name of the column or query parameter.

Note: The following fields are mutually exclusive: `identifier`, `value`, `random`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #identifier=
    
    
    def identifier=(value) -> ::String

**Parameter**

  * **value** (::String) — `identifier` is the name of the column or query parameter.

Note: The following fields are mutually exclusive: `identifier`, `value`, `random`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — `identifier` is the name of the column or query parameter.

Note: The following fields are mutually exclusive: `identifier`, `value`, `random`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #null_order
    
    
    def null_order() -> ::Google::Cloud::Spanner::V1::KeyRecipe::Part::NullOrder

**Returns**

  * ([::Google::Cloud::Spanner::V1::KeyRecipe::Part::NullOrder](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-KeyRecipe-Part-NullOrder)) — How NULLs are represented in the encoded key part. Only present if `tag` is zero. 



### #null_order=
    
    
    def null_order=(value) -> ::Google::Cloud::Spanner::V1::KeyRecipe::Part::NullOrder

**Parameter**

  * **value** ([::Google::Cloud::Spanner::V1::KeyRecipe::Part::NullOrder](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-KeyRecipe-Part-NullOrder)) — How NULLs are represented in the encoded key part. Only present if `tag` is zero. 



**Returns**

  * ([::Google::Cloud::Spanner::V1::KeyRecipe::Part::NullOrder](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-KeyRecipe-Part-NullOrder)) — How NULLs are represented in the encoded key part. Only present if `tag` is zero. 



### #order
    
    
    def order() -> ::Google::Cloud::Spanner::V1::KeyRecipe::Part::Order

**Returns**

  * ([::Google::Cloud::Spanner::V1::KeyRecipe::Part::Order](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-KeyRecipe-Part-Order)) — Whether the key column is sorted ascending or descending. Only present if `tag` is zero. 



### #order=
    
    
    def order=(value) -> ::Google::Cloud::Spanner::V1::KeyRecipe::Part::Order

**Parameter**

  * **value** ([::Google::Cloud::Spanner::V1::KeyRecipe::Part::Order](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-KeyRecipe-Part-Order)) — Whether the key column is sorted ascending or descending. Only present if `tag` is zero. 



**Returns**

  * ([::Google::Cloud::Spanner::V1::KeyRecipe::Part::Order](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-KeyRecipe-Part-Order)) — Whether the key column is sorted ascending or descending. Only present if `tag` is zero. 



### #random
    
    
    def random() -> ::Boolean

**Returns**

  * (::Boolean) — If true, the client is responsible to fill in the value randomly. It's relevant only for the INT64 type.

Note: The following fields are mutually exclusive: `random`, `identifier`, `value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #random=
    
    
    def random=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If true, the client is responsible to fill in the value randomly. It's relevant only for the INT64 type.

Note: The following fields are mutually exclusive: `random`, `identifier`, `value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Boolean) — If true, the client is responsible to fill in the value randomly. It's relevant only for the INT64 type.

Note: The following fields are mutually exclusive: `random`, `identifier`, `value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #struct_identifiers
    
    
    def struct_identifiers() -> ::Array<::Integer>

**Returns**

  * (::Array<::Integer>) — It is a repeated field to support fetching key columns from nested structs, such as `STRUCT` query parameters. 



### #struct_identifiers=
    
    
    def struct_identifiers=(value) -> ::Array<::Integer>

**Parameter**

  * **value** (::Array<::Integer>) — It is a repeated field to support fetching key columns from nested structs, such as `STRUCT` query parameters. 



**Returns**

  * (::Array<::Integer>) — It is a repeated field to support fetching key columns from nested structs, such as `STRUCT` query parameters. 



### #tag
    
    
    def tag() -> ::Integer

**Returns**

  * (::Integer) — If non-zero, `tag` is the only field present in this `Part`. The part is encoded by appending `tag` to the ssformat key. 



### #tag=
    
    
    def tag=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — If non-zero, `tag` is the only field present in this `Part`. The part is encoded by appending `tag` to the ssformat key. 



**Returns**

  * (::Integer) — If non-zero, `tag` is the only field present in this `Part`. The part is encoded by appending `tag` to the ssformat key. 



### #type
    
    
    def type() -> ::Google::Cloud::Spanner::V1::Type

**Returns**

  * ([::Google::Cloud::Spanner::V1::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Type)) — The type of the key part. Only present if `tag` is zero. 



### #type=
    
    
    def type=(value) -> ::Google::Cloud::Spanner::V1::Type

**Parameter**

  * **value** ([::Google::Cloud::Spanner::V1::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Type)) — The type of the key part. Only present if `tag` is zero. 



**Returns**

  * ([::Google::Cloud::Spanner::V1::Type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Type)) — The type of the key part. Only present if `tag` is zero. 



### #value
    
    
    def value() -> ::Google::Protobuf::Value

**Returns**

  * ([::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Protobuf-Value)) — The constant value of the key part. It is present when query uses a constant as a part of the key.

Note: The following fields are mutually exclusive: `value`, `identifier`, `random`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #value=
    
    
    def value=(value) -> ::Google::Protobuf::Value

**Parameter**

  * **value** ([::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Protobuf-Value)) — The constant value of the key part. It is present when query uses a constant as a part of the key.

Note: The following fields are mutually exclusive: `value`, `identifier`, `random`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Protobuf-Value)) — The constant value of the key part. It is present when query uses a constant as a part of the key.

Note: The following fields are mutually exclusive: `value`, `identifier`, `random`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
