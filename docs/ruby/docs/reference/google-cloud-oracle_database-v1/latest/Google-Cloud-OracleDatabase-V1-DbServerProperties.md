---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-DbServerProperties/
title: Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::DbServerProperties (v1.1.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:15.437889+00:00
---

# Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::DbServerProperties (v1.1.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-DbServerProperties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::DbServerProperties (v1.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.1 (latest)  1.1.0  1.0.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Oracle Database@Google Cloud V1 API class Google::Cloud::OracleDatabase::V1::DbServerProperties.

Various properties and settings associated with Exadata database server.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #db_node_ids
    
    
    def db_node_ids() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. OCID of database nodes associated with the database server. 



### #db_node_storage_size_gb
    
    
    def db_node_storage_size_gb() -> ::Integer

**Returns**

  * (::Integer) — Optional. Local storage per VM. 



### #db_node_storage_size_gb=
    
    
    def db_node_storage_size_gb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Local storage per VM. 



**Returns**

  * (::Integer) — Optional. Local storage per VM. 



### #max_db_node_storage_size_gb
    
    
    def max_db_node_storage_size_gb() -> ::Integer

**Returns**

  * (::Integer) — Optional. Maximum local storage per VM. 



### #max_db_node_storage_size_gb=
    
    
    def max_db_node_storage_size_gb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Maximum local storage per VM. 



**Returns**

  * (::Integer) — Optional. Maximum local storage per VM. 



### #max_memory_size_gb
    
    
    def max_memory_size_gb() -> ::Integer

**Returns**

  * (::Integer) — Optional. Maximum memory allocated in GBs. 



### #max_memory_size_gb=
    
    
    def max_memory_size_gb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Maximum memory allocated in GBs. 



**Returns**

  * (::Integer) — Optional. Maximum memory allocated in GBs. 



### #max_ocpu_count
    
    
    def max_ocpu_count() -> ::Integer

**Returns**

  * (::Integer) — Optional. Maximum OCPU count per database. 



### #max_ocpu_count=
    
    
    def max_ocpu_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Maximum OCPU count per database. 



**Returns**

  * (::Integer) — Optional. Maximum OCPU count per database. 



### #memory_size_gb
    
    
    def memory_size_gb() -> ::Integer

**Returns**

  * (::Integer) — Optional. Memory allocated in GBs. 



### #memory_size_gb=
    
    
    def memory_size_gb=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Memory allocated in GBs. 



**Returns**

  * (::Integer) — Optional. Memory allocated in GBs. 



### #ocid
    
    
    def ocid() -> ::String

**Returns**

  * (::String) — Output only. OCID of database server. 



### #ocpu_count
    
    
    def ocpu_count() -> ::Integer

**Returns**

  * (::Integer) — Optional. OCPU count per database. 



### #ocpu_count=
    
    
    def ocpu_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. OCPU count per database. 



**Returns**

  * (::Integer) — Optional. OCPU count per database. 



### #state
    
    
    def state() -> ::Google::Cloud::OracleDatabase::V1::DbServerProperties::State

**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::DbServerProperties::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-DbServerProperties-State)) — Output only. State of the database server. 



### #vm_count
    
    
    def vm_count() -> ::Integer

**Returns**

  * (::Integer) — Optional. Vm count per database. 



### #vm_count=
    
    
    def vm_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. Vm count per database. 



**Returns**

  * (::Integer) — Optional. Vm count per database. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
