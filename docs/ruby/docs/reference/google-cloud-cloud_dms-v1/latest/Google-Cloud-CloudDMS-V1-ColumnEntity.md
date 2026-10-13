---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ColumnEntity/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::ColumnEntity (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:21.684656+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::ColumnEntity (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ColumnEntity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::ColumnEntity (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::ColumnEntity.

Column is not used as an independent entity, it is retrieved as part of a Table entity.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #array
    
    
    def array() -> ::Boolean

**Returns**

  * (::Boolean) — Is the column of array type. 



### #array=
    
    
    def array=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Is the column of array type. 



**Returns**

  * (::Boolean) — Is the column of array type. 



### #array_length
    
    
    def array_length() -> ::Integer

**Returns**

  * (::Integer) — If the column is array, of which length. 



### #array_length=
    
    
    def array_length=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — If the column is array, of which length. 



**Returns**

  * (::Integer) — If the column is array, of which length. 



### #auto_generated
    
    
    def auto_generated() -> ::Boolean

**Returns**

  * (::Boolean) — Is the column auto-generated/identity. 



### #auto_generated=
    
    
    def auto_generated=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Is the column auto-generated/identity. 



**Returns**

  * (::Boolean) — Is the column auto-generated/identity. 



### #charset
    
    
    def charset() -> ::String

**Returns**

  * (::String) — Charset override - instead of table level charset. 



### #charset=
    
    
    def charset=(value) -> ::String

**Parameter**

  * **value** (::String) — Charset override - instead of table level charset. 



**Returns**

  * (::String) — Charset override - instead of table level charset. 



### #collation
    
    
    def collation() -> ::String

**Returns**

  * (::String) — Collation override - instead of table level collation. 



### #collation=
    
    
    def collation=(value) -> ::String

**Parameter**

  * **value** (::String) — Collation override - instead of table level collation. 



**Returns**

  * (::String) — Collation override - instead of table level collation. 



### #comment
    
    
    def comment() -> ::String

**Returns**

  * (::String) — Comment associated with the column. 



### #comment=
    
    
    def comment=(value) -> ::String

**Parameter**

  * **value** (::String) — Comment associated with the column. 



**Returns**

  * (::String) — Comment associated with the column. 



### #custom_features
    
    
    def custom_features() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Struct)) — Custom engine specific features. 



### #custom_features=
    
    
    def custom_features=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Struct)) — Custom engine specific features. 



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Struct)) — Custom engine specific features. 



### #data_type
    
    
    def data_type() -> ::String

**Returns**

  * (::String) — Column data type. 



### #data_type=
    
    
    def data_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Column data type. 



**Returns**

  * (::String) — Column data type. 



### #default_value
    
    
    def default_value() -> ::String

**Returns**

  * (::String) — Default value of the column. 



### #default_value=
    
    
    def default_value=(value) -> ::String

**Parameter**

  * **value** (::String) — Default value of the column. 



**Returns**

  * (::String) — Default value of the column. 



### #fractional_seconds_precision
    
    
    def fractional_seconds_precision() -> ::Integer

**Returns**

  * (::Integer) — Column fractional second precision - used for timestamp based datatypes. 



### #fractional_seconds_precision=
    
    
    def fractional_seconds_precision=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Column fractional second precision - used for timestamp based datatypes. 



**Returns**

  * (::Integer) — Column fractional second precision - used for timestamp based datatypes. 



### #length
    
    
    def length() -> ::Integer

**Returns**

  * (::Integer) — Column length - e.g. varchar (50). 



### #length=
    
    
    def length=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Column length - e.g. varchar (50). 



**Returns**

  * (::Integer) — Column length - e.g. varchar (50). 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Column name. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Column name. 



**Returns**

  * (::String) — Column name. 



### #nullable
    
    
    def nullable() -> ::Boolean

**Returns**

  * (::Boolean) — Is the column nullable. 



### #nullable=
    
    
    def nullable=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Is the column nullable. 



**Returns**

  * (::Boolean) — Is the column nullable. 



### #ordinal_position
    
    
    def ordinal_position() -> ::Integer

**Returns**

  * (::Integer) — Column order in the table. 



### #ordinal_position=
    
    
    def ordinal_position=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Column order in the table. 



**Returns**

  * (::Integer) — Column order in the table. 



### #precision
    
    
    def precision() -> ::Integer

**Returns**

  * (::Integer) — Column precision - when relevant. 



### #precision=
    
    
    def precision=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Column precision - when relevant. 



**Returns**

  * (::Integer) — Column precision - when relevant. 



### #scale
    
    
    def scale() -> ::Integer

**Returns**

  * (::Integer) — Column scale - when relevant. 



### #scale=
    
    
    def scale=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Column scale - when relevant. 



**Returns**

  * (::Integer) — Column scale - when relevant. 



### #set_values
    
    
    def set_values() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Specifies the list of values allowed in the column. Only used for set data type. 



### #set_values=
    
    
    def set_values=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Specifies the list of values allowed in the column. Only used for set data type. 



**Returns**

  * (::Array<::String>) — Specifies the list of values allowed in the column. Only used for set data type. 



### #udt
    
    
    def udt() -> ::Boolean

**Returns**

  * (::Boolean) — Is the column a UDT. 



### #udt=
    
    
    def udt=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Is the column a UDT. 



**Returns**

  * (::Boolean) — Is the column a UDT. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
