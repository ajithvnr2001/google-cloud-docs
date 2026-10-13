---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TypedValue/
title: BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::TypedValue (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:15.328102+00:00
---

# BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::TypedValue (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TypedValue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::TypedValue (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Cloud::Bigquery::Migration::V2::TypedValue.

A single strongly-typed value.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #bool_value
    
    
    def bool_value() -> ::Boolean

**Returns**

  * (::Boolean) — A Boolean value: `true` or `false`.

Note: The following fields are mutually exclusive: `bool_value`, `int64_value`, `double_value`, `string_value`, `distribution_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #bool_value=
    
    
    def bool_value=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — A Boolean value: `true` or `false`.

Note: The following fields are mutually exclusive: `bool_value`, `int64_value`, `double_value`, `string_value`, `distribution_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Boolean) — A Boolean value: `true` or `false`.

Note: The following fields are mutually exclusive: `bool_value`, `int64_value`, `double_value`, `string_value`, `distribution_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #distribution_value
    
    
    def distribution_value() -> ::Google::Api::Distribution

**Returns**

  * ([::Google::Api::Distribution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution)) — A distribution value.

Note: The following fields are mutually exclusive: `distribution_value`, `bool_value`, `int64_value`, `double_value`, `string_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #distribution_value=
    
    
    def distribution_value=(value) -> ::Google::Api::Distribution

**Parameter**

  * **value** ([::Google::Api::Distribution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution)) — A distribution value.

Note: The following fields are mutually exclusive: `distribution_value`, `bool_value`, `int64_value`, `double_value`, `string_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Api::Distribution](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Api-Distribution)) — A distribution value.

Note: The following fields are mutually exclusive: `distribution_value`, `bool_value`, `int64_value`, `double_value`, `string_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #double_value
    
    
    def double_value() -> ::Float

**Returns**

  * (::Float) — A 64-bit double-precision floating-point number. Its magnitude is approximately `+/-10^(+/-300)` and it has 16 significant digits of precision.

Note: The following fields are mutually exclusive: `double_value`, `bool_value`, `int64_value`, `string_value`, `distribution_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #double_value=
    
    
    def double_value=(value) -> ::Float

**Parameter**

  * **value** (::Float) — A 64-bit double-precision floating-point number. Its magnitude is approximately `+/-10^(+/-300)` and it has 16 significant digits of precision.

Note: The following fields are mutually exclusive: `double_value`, `bool_value`, `int64_value`, `string_value`, `distribution_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Float) — A 64-bit double-precision floating-point number. Its magnitude is approximately `+/-10^(+/-300)` and it has 16 significant digits of precision.

Note: The following fields are mutually exclusive: `double_value`, `bool_value`, `int64_value`, `string_value`, `distribution_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #int64_value
    
    
    def int64_value() -> ::Integer

**Returns**

  * (::Integer) — A 64-bit integer. Its range is approximately `+/-9.2x10^18`.

Note: The following fields are mutually exclusive: `int64_value`, `bool_value`, `double_value`, `string_value`, `distribution_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #int64_value=
    
    
    def int64_value=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — A 64-bit integer. Its range is approximately `+/-9.2x10^18`.

Note: The following fields are mutually exclusive: `int64_value`, `bool_value`, `double_value`, `string_value`, `distribution_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Integer) — A 64-bit integer. Its range is approximately `+/-9.2x10^18`.

Note: The following fields are mutually exclusive: `int64_value`, `bool_value`, `double_value`, `string_value`, `distribution_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #string_value
    
    
    def string_value() -> ::String

**Returns**

  * (::String) — A variable-length string value.

Note: The following fields are mutually exclusive: `string_value`, `bool_value`, `int64_value`, `double_value`, `distribution_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #string_value=
    
    
    def string_value=(value) -> ::String

**Parameter**

  * **value** (::String) — A variable-length string value.

Note: The following fields are mutually exclusive: `string_value`, `bool_value`, `int64_value`, `double_value`, `distribution_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — A variable-length string value.

Note: The following fields are mutually exclusive: `string_value`, `bool_value`, `int64_value`, `double_value`, `distribution_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
