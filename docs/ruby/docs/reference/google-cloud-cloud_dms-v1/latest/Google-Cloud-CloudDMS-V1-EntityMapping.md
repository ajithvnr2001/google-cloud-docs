---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityMapping/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::EntityMapping (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:29.339239+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::EntityMapping (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityMapping/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::EntityMapping (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::EntityMapping.

Details of the mappings of a database entity.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #draft_entity
    
    
    def draft_entity() -> ::String

**Returns**

  * (::String) — Target entity full name. The draft entity can also include a column, index or constraint using the same naming notation schema.table.column. 



### #draft_entity=
    
    
    def draft_entity=(value) -> ::String

**Parameter**

  * **value** (::String) — Target entity full name. The draft entity can also include a column, index or constraint using the same naming notation schema.table.column. 



**Returns**

  * (::String) — Target entity full name. The draft entity can also include a column, index or constraint using the same naming notation schema.table.column. 



### #draft_type
    
    
    def draft_type() -> ::Google::Cloud::CloudDMS::V1::DatabaseEntityType

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — Type of draft entity. 



### #draft_type=
    
    
    def draft_type=(value) -> ::Google::Cloud::CloudDMS::V1::DatabaseEntityType

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — Type of draft entity. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — Type of draft entity. 



### #mapping_log
    
    
    def mapping_log() -> ::Array<::Google::Cloud::CloudDMS::V1::EntityMappingLogEntry>

**Returns**

  * (::Array<[::Google::Cloud::CloudDMS::V1::EntityMappingLogEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityMappingLogEntry)>) — Entity mapping log entries. Multiple rules can be effective and contribute changes to a converted entity, such as a rule can handle the entity name, another rule can handle an entity type. In addition, rules which did not change the entity are also logged along with the reason preventing them to do so. 



### #mapping_log=
    
    
    def mapping_log=(value) -> ::Array<::Google::Cloud::CloudDMS::V1::EntityMappingLogEntry>

**Parameter**

  * **value** (::Array<[::Google::Cloud::CloudDMS::V1::EntityMappingLogEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityMappingLogEntry)>) — Entity mapping log entries. Multiple rules can be effective and contribute changes to a converted entity, such as a rule can handle the entity name, another rule can handle an entity type. In addition, rules which did not change the entity are also logged along with the reason preventing them to do so. 



**Returns**

  * (::Array<[::Google::Cloud::CloudDMS::V1::EntityMappingLogEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityMappingLogEntry)>) — Entity mapping log entries. Multiple rules can be effective and contribute changes to a converted entity, such as a rule can handle the entity name, another rule can handle an entity type. In addition, rules which did not change the entity are also logged along with the reason preventing them to do so. 



### #source_entity
    
    
    def source_entity() -> ::String

**Returns**

  * (::String) — Source entity full name. The source entity can also be a column, index or constraint using the same naming notation schema.table.column. 



### #source_entity=
    
    
    def source_entity=(value) -> ::String

**Parameter**

  * **value** (::String) — Source entity full name. The source entity can also be a column, index or constraint using the same naming notation schema.table.column. 



**Returns**

  * (::String) — Source entity full name. The source entity can also be a column, index or constraint using the same naming notation schema.table.column. 



### #source_type
    
    
    def source_type() -> ::Google::Cloud::CloudDMS::V1::DatabaseEntityType

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — Type of source entity. 



### #source_type=
    
    
    def source_type=(value) -> ::Google::Cloud::CloudDMS::V1::DatabaseEntityType

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — Type of source entity. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — Type of source entity. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
