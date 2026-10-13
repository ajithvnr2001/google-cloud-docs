---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-RuntimeEntitySchema-Field/
title: Connectors V1 API - Class Google::Cloud::Connectors::V1::RuntimeEntitySchema::Field (v1.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:42.838015+00:00
---

# Connectors V1 API - Class Google::Cloud::Connectors::V1::RuntimeEntitySchema::Field (v1.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-RuntimeEntitySchema-Field/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Connectors V1 API - Class Google::Cloud::Connectors::V1::RuntimeEntitySchema::Field (v1.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.1 (latest)  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Connectors V1 API class Google::Cloud::Connectors::V1::RuntimeEntitySchema::Field.

Metadata of an entity field.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #additional_details
    
    
    def additional_details() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Protobuf-Struct)) — The following map contains fields that are not explicitly mentioned above,this give connectors the flexibility to add new metadata fields. 



### #additional_details=
    
    
    def additional_details=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Protobuf-Struct)) — The following map contains fields that are not explicitly mentioned above,this give connectors the flexibility to add new metadata fields. 



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Protobuf-Struct)) — The following map contains fields that are not explicitly mentioned above,this give connectors the flexibility to add new metadata fields. 



### #data_type
    
    
    def data_type() -> ::Google::Cloud::Connectors::V1::DataType

**Returns**

  * ([::Google::Cloud::Connectors::V1::DataType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-DataType)) — The data type of the Field. 



### #data_type=
    
    
    def data_type=(value) -> ::Google::Cloud::Connectors::V1::DataType

**Parameter**

  * **value** ([::Google::Cloud::Connectors::V1::DataType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-DataType)) — The data type of the Field. 



**Returns**

  * ([::Google::Cloud::Connectors::V1::DataType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-DataType)) — The data type of the Field. 



### #default_value
    
    
    def default_value() -> ::Google::Protobuf::Value

**Returns**

  * ([::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Protobuf-Value)) — The following field specifies the default value of the Field provided by the external system if a value is not provided. 



### #default_value=
    
    
    def default_value=(value) -> ::Google::Protobuf::Value

**Parameter**

  * **value** ([::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Protobuf-Value)) — The following field specifies the default value of the Field provided by the external system if a value is not provided. 



**Returns**

  * ([::Google::Protobuf::Value](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Protobuf-Value)) — The following field specifies the default value of the Field provided by the external system if a value is not provided. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — A brief description of the Field. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — A brief description of the Field. 



**Returns**

  * (::String) — A brief description of the Field. 



### #field
    
    
    def field() -> ::String

**Returns**

  * (::String) — Name of the Field. 



### #field=
    
    
    def field=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the Field. 



**Returns**

  * (::String) — Name of the Field. 



### #key
    
    
    def key() -> ::Boolean

**Returns**

  * (::Boolean) — The following boolean field specifies if the current Field acts as a primary key or id if the parent is of type entity. 



### #key=
    
    
    def key=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — The following boolean field specifies if the current Field acts as a primary key or id if the parent is of type entity. 



**Returns**

  * (::Boolean) — The following boolean field specifies if the current Field acts as a primary key or id if the parent is of type entity. 



### #nullable
    
    
    def nullable() -> ::Boolean

**Returns**

  * (::Boolean) — Specifies whether a null value is allowed. 



### #nullable=
    
    
    def nullable=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Specifies whether a null value is allowed. 



**Returns**

  * (::Boolean) — Specifies whether a null value is allowed. 



### #readonly
    
    
    def readonly() -> ::Boolean

**Returns**

  * (::Boolean) — Specifies if the Field is readonly. 



### #readonly=
    
    
    def readonly=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Specifies if the Field is readonly. 



**Returns**

  * (::Boolean) — Specifies if the Field is readonly. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
