---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Protobuf-Value/
title: Service Control API V1 API - Class Google::Protobuf::Value (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:28.275364+00:00
---

# Service Control API V1 API - Class Google::Protobuf::Value (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Protobuf-Value/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Service Control API V1 API - Class Google::Protobuf::Value (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.11.0  0.10.0  0.9.2  0.8.0  0.7.1  0.6.0  0.5.0  0.4.6 

Reference documentation and code samples for the Service Control API V1 API class Google::Protobuf::Value.

`Value` represents a dynamically typed value which can be either null, a number, a string, a boolean, a recursive struct value, or a list of values. A producer of value is expected to set one of these variants. Absence of any variant indicates an error.

The JSON representation for `Value` is JSON value.

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

  * (::Boolean) — Represents a boolean value.

Note: The following fields are mutually exclusive: `bool_value`, `null_value`, `number_value`, `string_value`, `struct_value`, `list_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #bool_value=
    
    
    def bool_value=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Represents a boolean value.

Note: The following fields are mutually exclusive: `bool_value`, `null_value`, `number_value`, `string_value`, `struct_value`, `list_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Boolean) — Represents a boolean value.

Note: The following fields are mutually exclusive: `bool_value`, `null_value`, `number_value`, `string_value`, `struct_value`, `list_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #list_value
    
    
    def list_value() -> ::Google::Protobuf::ListValue

**Returns**

  * ([::Google::Protobuf::ListValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Protobuf-ListValue)) — Represents a repeated `Value`.

Note: The following fields are mutually exclusive: `list_value`, `null_value`, `number_value`, `string_value`, `bool_value`, `struct_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #list_value=
    
    
    def list_value=(value) -> ::Google::Protobuf::ListValue

**Parameter**

  * **value** ([::Google::Protobuf::ListValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Protobuf-ListValue)) — Represents a repeated `Value`.

Note: The following fields are mutually exclusive: `list_value`, `null_value`, `number_value`, `string_value`, `bool_value`, `struct_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Protobuf::ListValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Protobuf-ListValue)) — Represents a repeated `Value`.

Note: The following fields are mutually exclusive: `list_value`, `null_value`, `number_value`, `string_value`, `bool_value`, `struct_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #null_value
    
    
    def null_value() -> ::Google::Protobuf::NullValue

**Returns**

  * ([::Google::Protobuf::NullValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Protobuf-NullValue)) — Represents a null value.

Note: The following fields are mutually exclusive: `null_value`, `number_value`, `string_value`, `bool_value`, `struct_value`, `list_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #null_value=
    
    
    def null_value=(value) -> ::Google::Protobuf::NullValue

**Parameter**

  * **value** ([::Google::Protobuf::NullValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Protobuf-NullValue)) — Represents a null value.

Note: The following fields are mutually exclusive: `null_value`, `number_value`, `string_value`, `bool_value`, `struct_value`, `list_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Protobuf::NullValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Protobuf-NullValue)) — Represents a null value.

Note: The following fields are mutually exclusive: `null_value`, `number_value`, `string_value`, `bool_value`, `struct_value`, `list_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #number_value
    
    
    def number_value() -> ::Float

**Returns**

  * (::Float) — Represents a double value.

Note: The following fields are mutually exclusive: `number_value`, `null_value`, `string_value`, `bool_value`, `struct_value`, `list_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #number_value=
    
    
    def number_value=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Represents a double value.

Note: The following fields are mutually exclusive: `number_value`, `null_value`, `string_value`, `bool_value`, `struct_value`, `list_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::Float) — Represents a double value.

Note: The following fields are mutually exclusive: `number_value`, `null_value`, `string_value`, `bool_value`, `struct_value`, `list_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #string_value
    
    
    def string_value() -> ::String

**Returns**

  * (::String) — Represents a string value.

Note: The following fields are mutually exclusive: `string_value`, `null_value`, `number_value`, `bool_value`, `struct_value`, `list_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #string_value=
    
    
    def string_value=(value) -> ::String

**Parameter**

  * **value** (::String) — Represents a string value.

Note: The following fields are mutually exclusive: `string_value`, `null_value`, `number_value`, `bool_value`, `struct_value`, `list_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Represents a string value.

Note: The following fields are mutually exclusive: `string_value`, `null_value`, `number_value`, `bool_value`, `struct_value`, `list_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #struct_value
    
    
    def struct_value() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Protobuf-Struct)) — Represents a structured value.

Note: The following fields are mutually exclusive: `struct_value`, `null_value`, `number_value`, `string_value`, `bool_value`, `list_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #struct_value=
    
    
    def struct_value=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Protobuf-Struct)) — Represents a structured value.

Note: The following fields are mutually exclusive: `struct_value`, `null_value`, `number_value`, `string_value`, `bool_value`, `list_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_control-v1/latest/Google-Protobuf-Struct)) — Represents a structured value.

Note: The following fields are mutually exclusive: `struct_value`, `null_value`, `number_value`, `string_value`, `bool_value`, `list_value`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
