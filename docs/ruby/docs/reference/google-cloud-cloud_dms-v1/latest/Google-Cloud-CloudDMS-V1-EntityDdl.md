---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityDdl/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::EntityDdl (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:28.777525+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::EntityDdl (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityDdl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::EntityDdl (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::EntityDdl.

A single DDL statement for a specific entity

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #ddl
    
    
    def ddl() -> ::String

**Returns**

  * (::String) — The actual ddl code. 



### #ddl=
    
    
    def ddl=(value) -> ::String

**Parameter**

  * **value** (::String) — The actual ddl code. 



**Returns**

  * (::String) — The actual ddl code. 



### #ddl_type
    
    
    def ddl_type() -> ::String

**Returns**

  * (::String) — Type of DDL (Create, Alter). 



### #ddl_type=
    
    
    def ddl_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Type of DDL (Create, Alter). 



**Returns**

  * (::String) — Type of DDL (Create, Alter). 



### #entity
    
    
    def entity() -> ::String

**Returns**

  * (::String) — The name of the database entity the ddl refers to. 



### #entity=
    
    
    def entity=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the database entity the ddl refers to. 



**Returns**

  * (::String) — The name of the database entity the ddl refers to. 



### #entity_type
    
    
    def entity_type() -> ::Google::Cloud::CloudDMS::V1::DatabaseEntityType

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — The entity type (if the DDL is for a sub entity). 



### #entity_type=
    
    
    def entity_type=(value) -> ::Google::Cloud::CloudDMS::V1::DatabaseEntityType

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — The entity type (if the DDL is for a sub entity). 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — The entity type (if the DDL is for a sub entity). 



### #issue_id
    
    
    def issue_id() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — EntityIssues found for this ddl. 



### #issue_id=
    
    
    def issue_id=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — EntityIssues found for this ddl. 



**Returns**

  * (::Array<::String>) — EntityIssues found for this ddl. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
