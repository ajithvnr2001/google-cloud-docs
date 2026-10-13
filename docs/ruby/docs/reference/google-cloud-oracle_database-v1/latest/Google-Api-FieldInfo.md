---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Api-FieldInfo/
title: Oracle Database@Google Cloud V1 API - Class Google::Api::FieldInfo (v1.1.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:11.184902+00:00
---

# Oracle Database@Google Cloud V1 API - Class Google::Api::FieldInfo (v1.1.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Api-FieldInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud V1 API - Class Google::Api::FieldInfo (v1.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.1 (latest)  1.1.0  1.0.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Oracle Database@Google Cloud V1 API class Google::Api::FieldInfo.

Rich semantic information of an API field beyond basic typing.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #format
    
    
    def format() -> ::Google::Api::FieldInfo::Format

**Returns**

  * ([::Google::Api::FieldInfo::Format](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Api-FieldInfo-Format)) — The standard format of a field value. This does not explicitly configure any API consumer, just documents the API's format for the field it is applied to. 



### #format=
    
    
    def format=(value) -> ::Google::Api::FieldInfo::Format

**Parameter**

  * **value** ([::Google::Api::FieldInfo::Format](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Api-FieldInfo-Format)) — The standard format of a field value. This does not explicitly configure any API consumer, just documents the API's format for the field it is applied to. 



**Returns**

  * ([::Google::Api::FieldInfo::Format](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Api-FieldInfo-Format)) — The standard format of a field value. This does not explicitly configure any API consumer, just documents the API's format for the field it is applied to. 



### #referenced_types
    
    
    def referenced_types() -> ::Array<::Google::Api::TypeReference>

**Returns**

  * (::Array<[::Google::Api::TypeReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Api-TypeReference)>) — The type(s) that the annotated, generic field may represent.

Currently, this must only be used on fields of type `google.protobuf.Any`. Supporting other generic types may be considered in the future. 




### #referenced_types=
    
    
    def referenced_types=(value) -> ::Array<::Google::Api::TypeReference>

**Parameter**

  * **value** (::Array<[::Google::Api::TypeReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Api-TypeReference)>) — The type(s) that the annotated, generic field may represent.

Currently, this must only be used on fields of type `google.protobuf.Any`. Supporting other generic types may be considered in the future. 




**Returns**

  * (::Array<[::Google::Api::TypeReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Api-TypeReference)>) — The type(s) that the annotated, generic field may represent.

Currently, this must only be used on fields of type `google.protobuf.Any`. Supporting other generic types may be considered in the future. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
