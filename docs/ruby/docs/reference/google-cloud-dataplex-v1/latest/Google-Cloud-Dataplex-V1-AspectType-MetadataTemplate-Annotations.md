---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-AspectType-MetadataTemplate-Annotations/
title: Dataplex V1 API - Class Google::Cloud::Dataplex::V1::AspectType::MetadataTemplate::Annotations (v2.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:09:53.270710+00:00
---

# Dataplex V1 API - Class Google::Cloud::Dataplex::V1::AspectType::MetadataTemplate::Annotations (v2.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-AspectType-MetadataTemplate-Annotations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataplex V1 API - Class Google::Cloud::Dataplex::V1::AspectType::MetadataTemplate::Annotations (v2.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.1 (latest)  2.10.0  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.2  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.1  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataplex V1 API class Google::Cloud::Dataplex::V1::AspectType::MetadataTemplate::Annotations.

Definition of the annotations of a field.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #deprecated
    
    
    def deprecated() -> ::String

**Returns**

  * (::String) — Optional. Marks a field as deprecated. You can include a deprecation message. 



### #deprecated=
    
    
    def deprecated=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Marks a field as deprecated. You can include a deprecation message. 



**Returns**

  * (::String) — Optional. Marks a field as deprecated. You can include a deprecation message. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. Description for a field. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Description for a field. 



**Returns**

  * (::String) — Optional. Description for a field. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Optional. Display name for a field. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Display name for a field. 



**Returns**

  * (::String) — Optional. Display name for a field. 



### #display_order
    
    
    def display_order() -> ::Integer

**Returns**

  * (::Integer) — Optional. Display order for a field. You can use this to reorder where a field is rendered. 



### #display_order=
    
    
    def display_order=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Display order for a field. You can use this to reorder where a field is rendered. 



**Returns**

  * (::Integer) — Optional. Display order for a field. You can use this to reorder where a field is rendered. 



### #string_type
    
    
    def string_type() -> ::String

**Returns**

  * (::String) — 

Optional. You can use String Type annotations to specify special meaning to string fields. The following values are supported:

    * richText: The field must be interpreted as a rich text field.
    * url: A fully qualified URL link.
    * resource: A service qualified resource reference.



### #string_type=
    
    
    def string_type=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optional. You can use String Type annotations to specify special meaning to string fields. The following values are supported:

    * richText: The field must be interpreted as a rich text field.
    * url: A fully qualified URL link.
    * resource: A service qualified resource reference.



**Returns**

  * (::String) — 

Optional. You can use String Type annotations to specify special meaning to string fields. The following values are supported:

    * richText: The field must be interpreted as a rich text field.
    * url: A fully qualified URL link.
    * resource: A service qualified resource reference.



### #string_values
    
    
    def string_values() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. Suggested hints for string fields. You can use them to suggest values to users through console. 



### #string_values=
    
    
    def string_values=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. Suggested hints for string fields. You can use them to suggest values to users through console. 



**Returns**

  * (::Array<::String>) — Optional. Suggested hints for string fields. You can use them to suggest values to users through console. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
