---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-lineage-v1/latest/Google-Cloud-DataCatalog-Lineage-V1-UpdateProcessRequest/
title: Data Lineage V1 API - Class Google::Cloud::DataCatalog::Lineage::V1::UpdateProcessRequest (v0.16.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:18.495019+00:00
---

# Data Lineage V1 API - Class Google::Cloud::DataCatalog::Lineage::V1::UpdateProcessRequest (v0.16.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-lineage-v1/latest/Google-Cloud-DataCatalog-Lineage-V1-UpdateProcessRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Lineage V1 API - Class Google::Cloud::DataCatalog::Lineage::V1::UpdateProcessRequest (v0.16.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.16.1 (latest)  0.16.0  0.15.0  0.14.0  0.13.0  0.12.1  0.11.0  0.10.1  0.9.1  0.8.0  0.7.1  0.6.2  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Data Lineage V1 API class Google::Cloud::DataCatalog::Lineage::V1::UpdateProcessRequest.

Request message for [UpdateProcess](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-lineage-v1/latest/Google-Cloud-DataCatalog-Lineage-V1-Lineage-Client#Google__Cloud__DataCatalog__Lineage__V1__Lineage__Client_update_process_instance_ "Google::Cloud::DataCatalog::Lineage::V1::Lineage::Client#update_process \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #allow_missing
    
    
    def allow_missing() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If set to true and the process is not found, the request inserts it. 



### #allow_missing=
    
    
    def allow_missing=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If set to true and the process is not found, the request inserts it. 



**Returns**

  * (::Boolean) — Optional. If set to true and the process is not found, the request inserts it. 



### #process
    
    
    def process() -> ::Google::Cloud::DataCatalog::Lineage::V1::Process

**Returns**

  * ([::Google::Cloud::DataCatalog::Lineage::V1::Process](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-lineage-v1/latest/Google-Cloud-DataCatalog-Lineage-V1-Process)) — Required. The lineage process to update.

The process's `name` field is used to identify the process to update. 




### #process=
    
    
    def process=(value) -> ::Google::Cloud::DataCatalog::Lineage::V1::Process

**Parameter**

  * **value** ([::Google::Cloud::DataCatalog::Lineage::V1::Process](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-lineage-v1/latest/Google-Cloud-DataCatalog-Lineage-V1-Process)) — Required. The lineage process to update.

The process's `name` field is used to identify the process to update. 




**Returns**

  * ([::Google::Cloud::DataCatalog::Lineage::V1::Process](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-lineage-v1/latest/Google-Cloud-DataCatalog-Lineage-V1-Process)) — Required. The lineage process to update.

The process's `name` field is used to identify the process to update. 




### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is idempotent only if a `request_id` is provided. 



### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is idempotent only if a `request_id` is provided. 



**Returns**

  * (::String) — Optional. A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is idempotent only if a `request_id` is provided. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-lineage-v1/latest/Google-Protobuf-FieldMask)) — Optional. The list of fields to update. Currently not used. The whole message is updated. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-lineage-v1/latest/Google-Protobuf-FieldMask)) — Optional. The list of fields to update. Currently not used. The whole message is updated. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_catalog-lineage-v1/latest/Google-Protobuf-FieldMask)) — Optional. The list of fields to update. Currently not used. The whole message is updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
