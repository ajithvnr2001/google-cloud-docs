---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntity/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::DatabaseEntity (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:26.140476+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::DatabaseEntity (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::DatabaseEntity (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::DatabaseEntity.

The base entity type for all the database related entities. The message contains the entity name, the name of its parent, the entity type, and the specific details per entity type.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #database
    
    
    def database() -> ::Google::Cloud::CloudDMS::V1::DatabaseInstanceEntity

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseInstanceEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseInstanceEntity)) — Database.

Note: The following fields are mutually exclusive: `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #database=
    
    
    def database=(value) -> ::Google::Cloud::CloudDMS::V1::DatabaseInstanceEntity

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::DatabaseInstanceEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseInstanceEntity)) — Database.

Note: The following fields are mutually exclusive: `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseInstanceEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseInstanceEntity)) — Database.

Note: The following fields are mutually exclusive: `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #database_function
    
    
    def database_function() -> ::Google::Cloud::CloudDMS::V1::FunctionEntity

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::FunctionEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-FunctionEntity)) — Function.

Note: The following fields are mutually exclusive: `database_function`, `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #database_function=
    
    
    def database_function=(value) -> ::Google::Cloud::CloudDMS::V1::FunctionEntity

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::FunctionEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-FunctionEntity)) — Function.

Note: The following fields are mutually exclusive: `database_function`, `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::FunctionEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-FunctionEntity)) — Function.

Note: The following fields are mutually exclusive: `database_function`, `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #database_package
    
    
    def database_package() -> ::Google::Cloud::CloudDMS::V1::PackageEntity

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::PackageEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-PackageEntity)) — Package.

Note: The following fields are mutually exclusive: `database_package`, `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #database_package=
    
    
    def database_package=(value) -> ::Google::Cloud::CloudDMS::V1::PackageEntity

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::PackageEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-PackageEntity)) — Package.

Note: The following fields are mutually exclusive: `database_package`, `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::PackageEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-PackageEntity)) — Package.

Note: The following fields are mutually exclusive: `database_package`, `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #entity_ddl
    
    
    def entity_ddl() -> ::Array<::Google::Cloud::CloudDMS::V1::EntityDdl>

**Returns**

  * (::Array<[::Google::Cloud::CloudDMS::V1::EntityDdl](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityDdl)>) — Details about the entity DDL script. Multiple DDL scripts are provided for child entities such as a table entity will have one DDL for the table with additional DDLs for each index, constraint and such. 



### #entity_ddl=
    
    
    def entity_ddl=(value) -> ::Array<::Google::Cloud::CloudDMS::V1::EntityDdl>

**Parameter**

  * **value** (::Array<[::Google::Cloud::CloudDMS::V1::EntityDdl](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityDdl)>) — Details about the entity DDL script. Multiple DDL scripts are provided for child entities such as a table entity will have one DDL for the table with additional DDLs for each index, constraint and such. 



**Returns**

  * (::Array<[::Google::Cloud::CloudDMS::V1::EntityDdl](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityDdl)>) — Details about the entity DDL script. Multiple DDL scripts are provided for child entities such as a table entity will have one DDL for the table with additional DDLs for each index, constraint and such. 



### #entity_type
    
    
    def entity_type() -> ::Google::Cloud::CloudDMS::V1::DatabaseEntityType

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — The type of the database entity (table, view, index, ...). 



### #entity_type=
    
    
    def entity_type=(value) -> ::Google::Cloud::CloudDMS::V1::DatabaseEntityType

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — The type of the database entity (table, view, index, ...). 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — The type of the database entity (table, view, index, ...). 



### #issues
    
    
    def issues() -> ::Array<::Google::Cloud::CloudDMS::V1::EntityIssue>

**Returns**

  * (::Array<[::Google::Cloud::CloudDMS::V1::EntityIssue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityIssue)>) — Details about the various issues found for the entity. 



### #issues=
    
    
    def issues=(value) -> ::Array<::Google::Cloud::CloudDMS::V1::EntityIssue>

**Parameter**

  * **value** (::Array<[::Google::Cloud::CloudDMS::V1::EntityIssue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityIssue)>) — Details about the various issues found for the entity. 



**Returns**

  * (::Array<[::Google::Cloud::CloudDMS::V1::EntityIssue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityIssue)>) — Details about the various issues found for the entity. 



### #mappings
    
    
    def mappings() -> ::Array<::Google::Cloud::CloudDMS::V1::EntityMapping>

**Returns**

  * (::Array<[::Google::Cloud::CloudDMS::V1::EntityMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityMapping)>) — Details about entity mappings. For source tree entities, this holds the draft entities which were generated by the mapping rules. For draft tree entities, this holds the source entities which were converted to form the draft entity. Destination entities will have no mapping details. 



### #mappings=
    
    
    def mappings=(value) -> ::Array<::Google::Cloud::CloudDMS::V1::EntityMapping>

**Parameter**

  * **value** (::Array<[::Google::Cloud::CloudDMS::V1::EntityMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityMapping)>) — Details about entity mappings. For source tree entities, this holds the draft entities which were generated by the mapping rules. For draft tree entities, this holds the source entities which were converted to form the draft entity. Destination entities will have no mapping details. 



**Returns**

  * (::Array<[::Google::Cloud::CloudDMS::V1::EntityMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityMapping)>) — Details about entity mappings. For source tree entities, this holds the draft entities which were generated by the mapping rules. For draft tree entities, this holds the source entities which were converted to form the draft entity. Destination entities will have no mapping details. 



### #materialized_view
    
    
    def materialized_view() -> ::Google::Cloud::CloudDMS::V1::MaterializedViewEntity

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MaterializedViewEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MaterializedViewEntity)) — Materialized view.

Note: The following fields are mutually exclusive: `materialized_view`, `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #materialized_view=
    
    
    def materialized_view=(value) -> ::Google::Cloud::CloudDMS::V1::MaterializedViewEntity

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::MaterializedViewEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MaterializedViewEntity)) — Materialized view.

Note: The following fields are mutually exclusive: `materialized_view`, `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MaterializedViewEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MaterializedViewEntity)) — Materialized view.

Note: The following fields are mutually exclusive: `materialized_view`, `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #parent_entity
    
    
    def parent_entity() -> ::String

**Returns**

  * (::String) — The full name of the parent entity (e.g. schema name). 



### #parent_entity=
    
    
    def parent_entity=(value) -> ::String

**Parameter**

  * **value** (::String) — The full name of the parent entity (e.g. schema name). 



**Returns**

  * (::String) — The full name of the parent entity (e.g. schema name). 



### #schema
    
    
    def schema() -> ::Google::Cloud::CloudDMS::V1::SchemaEntity

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SchemaEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SchemaEntity)) — Schema.

Note: The following fields are mutually exclusive: `schema`, `database`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #schema=
    
    
    def schema=(value) -> ::Google::Cloud::CloudDMS::V1::SchemaEntity

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::SchemaEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SchemaEntity)) — Schema.

Note: The following fields are mutually exclusive: `schema`, `database`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SchemaEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SchemaEntity)) — Schema.

Note: The following fields are mutually exclusive: `schema`, `database`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sequence
    
    
    def sequence() -> ::Google::Cloud::CloudDMS::V1::SequenceEntity

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SequenceEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SequenceEntity)) — Sequence.

Note: The following fields are mutually exclusive: `sequence`, `database`, `schema`, `table`, `view`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sequence=
    
    
    def sequence=(value) -> ::Google::Cloud::CloudDMS::V1::SequenceEntity

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::SequenceEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SequenceEntity)) — Sequence.

Note: The following fields are mutually exclusive: `sequence`, `database`, `schema`, `table`, `view`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SequenceEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SequenceEntity)) — Sequence.

Note: The following fields are mutually exclusive: `sequence`, `database`, `schema`, `table`, `view`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #short_name
    
    
    def short_name() -> ::String

**Returns**

  * (::String) — The short name (e.g. table name) of the entity. 



### #short_name=
    
    
    def short_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The short name (e.g. table name) of the entity. 



**Returns**

  * (::String) — The short name (e.g. table name) of the entity. 



### #stored_procedure
    
    
    def stored_procedure() -> ::Google::Cloud::CloudDMS::V1::StoredProcedureEntity

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::StoredProcedureEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-StoredProcedureEntity)) — Stored procedure.

Note: The following fields are mutually exclusive: `stored_procedure`, `database`, `schema`, `table`, `view`, `sequence`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #stored_procedure=
    
    
    def stored_procedure=(value) -> ::Google::Cloud::CloudDMS::V1::StoredProcedureEntity

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::StoredProcedureEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-StoredProcedureEntity)) — Stored procedure.

Note: The following fields are mutually exclusive: `stored_procedure`, `database`, `schema`, `table`, `view`, `sequence`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::StoredProcedureEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-StoredProcedureEntity)) — Stored procedure.

Note: The following fields are mutually exclusive: `stored_procedure`, `database`, `schema`, `table`, `view`, `sequence`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #synonym
    
    
    def synonym() -> ::Google::Cloud::CloudDMS::V1::SynonymEntity

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SynonymEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SynonymEntity)) — Synonym.

Note: The following fields are mutually exclusive: `synonym`, `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #synonym=
    
    
    def synonym=(value) -> ::Google::Cloud::CloudDMS::V1::SynonymEntity

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::SynonymEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SynonymEntity)) — Synonym.

Note: The following fields are mutually exclusive: `synonym`, `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SynonymEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SynonymEntity)) — Synonym.

Note: The following fields are mutually exclusive: `synonym`, `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #table
    
    
    def table() -> ::Google::Cloud::CloudDMS::V1::TableEntity

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::TableEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-TableEntity)) — Table.

Note: The following fields are mutually exclusive: `table`, `database`, `schema`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #table=
    
    
    def table=(value) -> ::Google::Cloud::CloudDMS::V1::TableEntity

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::TableEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-TableEntity)) — Table.

Note: The following fields are mutually exclusive: `table`, `database`, `schema`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::TableEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-TableEntity)) — Table.

Note: The following fields are mutually exclusive: `table`, `database`, `schema`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #tree
    
    
    def tree() -> ::Google::Cloud::CloudDMS::V1::DatabaseEntity::TreeType

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEntity::TreeType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntity-TreeType)) — The type of tree the entity belongs to. 



### #tree=
    
    
    def tree=(value) -> ::Google::Cloud::CloudDMS::V1::DatabaseEntity::TreeType

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::DatabaseEntity::TreeType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntity-TreeType)) — The type of tree the entity belongs to. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEntity::TreeType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntity-TreeType)) — The type of tree the entity belongs to. 



### #udt
    
    
    def udt() -> ::Google::Cloud::CloudDMS::V1::UDTEntity

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::UDTEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-UDTEntity)) — UDT.

Note: The following fields are mutually exclusive: `udt`, `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #udt=
    
    
    def udt=(value) -> ::Google::Cloud::CloudDMS::V1::UDTEntity

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::UDTEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-UDTEntity)) — UDT.

Note: The following fields are mutually exclusive: `udt`, `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::UDTEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-UDTEntity)) — UDT.

Note: The following fields are mutually exclusive: `udt`, `database`, `schema`, `table`, `view`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #view
    
    
    def view() -> ::Google::Cloud::CloudDMS::V1::ViewEntity

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::ViewEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ViewEntity)) — View.

Note: The following fields are mutually exclusive: `view`, `database`, `schema`, `table`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #view=
    
    
    def view=(value) -> ::Google::Cloud::CloudDMS::V1::ViewEntity

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::ViewEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ViewEntity)) — View.

Note: The following fields are mutually exclusive: `view`, `database`, `schema`, `table`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::ViewEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ViewEntity)) — View.

Note: The following fields are mutually exclusive: `view`, `database`, `schema`, `table`, `sequence`, `stored_procedure`, `database_function`, `synonym`, `database_package`, `udt`, `materialized_view`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
