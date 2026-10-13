---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRule/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::MappingRule (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:49.410570+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::MappingRule (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::MappingRule (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::MappingRule.

Definition of a transformation that is to be applied to a group of entities in the source schema. Several such transformations can be applied to an entity sequentially to define the corresponding entity in the target schema.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #conditional_column_set_value
    
    
    def conditional_column_set_value() -> ::Google::Cloud::CloudDMS::V1::ConditionalColumnSetValue

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::ConditionalColumnSetValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConditionalColumnSetValue)) — Optional. Rule to specify how the data contained in a column should be transformed (such as trimmed, rounded, etc) provided that the data meets certain criteria.

Note: The following fields are mutually exclusive: `conditional_column_set_value`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #conditional_column_set_value=
    
    
    def conditional_column_set_value=(value) -> ::Google::Cloud::CloudDMS::V1::ConditionalColumnSetValue

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::ConditionalColumnSetValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConditionalColumnSetValue)) — Optional. Rule to specify how the data contained in a column should be transformed (such as trimmed, rounded, etc) provided that the data meets certain criteria.

Note: The following fields are mutually exclusive: `conditional_column_set_value`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::ConditionalColumnSetValue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConditionalColumnSetValue)) — Optional. Rule to specify how the data contained in a column should be transformed (such as trimmed, rounded, etc) provided that the data meets certain criteria.

Note: The following fields are mutually exclusive: `conditional_column_set_value`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #convert_rowid_column
    
    
    def convert_rowid_column() -> ::Google::Cloud::CloudDMS::V1::ConvertRowIdToColumn

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::ConvertRowIdToColumn](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConvertRowIdToColumn)) — Optional. Rule to specify how multiple tables should be converted with an additional rowid column.

Note: The following fields are mutually exclusive: `convert_rowid_column`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #convert_rowid_column=
    
    
    def convert_rowid_column=(value) -> ::Google::Cloud::CloudDMS::V1::ConvertRowIdToColumn

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::ConvertRowIdToColumn](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConvertRowIdToColumn)) — Optional. Rule to specify how multiple tables should be converted with an additional rowid column.

Note: The following fields are mutually exclusive: `convert_rowid_column`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::ConvertRowIdToColumn](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConvertRowIdToColumn)) — Optional. Rule to specify how multiple tables should be converted with an additional rowid column.

Note: The following fields are mutually exclusive: `convert_rowid_column`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Optional. A human readable name 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A human readable name 



**Returns**

  * (::String) — Optional. A human readable name 



### #entity_move
    
    
    def entity_move() -> ::Google::Cloud::CloudDMS::V1::EntityMove

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::EntityMove](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityMove)) — Optional. Rule to specify how multiple entities should be relocated into a different schema.

Note: The following fields are mutually exclusive: `entity_move`, `single_entity_rename`, `multi_entity_rename`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #entity_move=
    
    
    def entity_move=(value) -> ::Google::Cloud::CloudDMS::V1::EntityMove

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::EntityMove](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityMove)) — Optional. Rule to specify how multiple entities should be relocated into a different schema.

Note: The following fields are mutually exclusive: `entity_move`, `single_entity_rename`, `multi_entity_rename`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::EntityMove](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-EntityMove)) — Optional. Rule to specify how multiple entities should be relocated into a different schema.

Note: The following fields are mutually exclusive: `entity_move`, `single_entity_rename`, `multi_entity_rename`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #filter
    
    
    def filter() -> ::Google::Cloud::CloudDMS::V1::MappingRuleFilter

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MappingRuleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRuleFilter)) — Required. The rule filter 



### #filter=
    
    
    def filter=(value) -> ::Google::Cloud::CloudDMS::V1::MappingRuleFilter

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::MappingRuleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRuleFilter)) — Required. The rule filter 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MappingRuleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRuleFilter)) — Required. The rule filter 



### #filter_table_columns
    
    
    def filter_table_columns() -> ::Google::Cloud::CloudDMS::V1::FilterTableColumns

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::FilterTableColumns](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-FilterTableColumns)) — Optional. Rule to specify the list of columns to include or exclude from a table.

Note: The following fields are mutually exclusive: `filter_table_columns`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #filter_table_columns=
    
    
    def filter_table_columns=(value) -> ::Google::Cloud::CloudDMS::V1::FilterTableColumns

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::FilterTableColumns](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-FilterTableColumns)) — Optional. Rule to specify the list of columns to include or exclude from a table.

Note: The following fields are mutually exclusive: `filter_table_columns`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::FilterTableColumns](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-FilterTableColumns)) — Optional. Rule to specify the list of columns to include or exclude from a table.

Note: The following fields are mutually exclusive: `filter_table_columns`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #multi_column_data_type_change
    
    
    def multi_column_data_type_change() -> ::Google::Cloud::CloudDMS::V1::MultiColumnDatatypeChange

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MultiColumnDatatypeChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MultiColumnDatatypeChange)) — Optional. Rule to specify how multiple columns should be converted to a different data type.

Note: The following fields are mutually exclusive: `multi_column_data_type_change`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #multi_column_data_type_change=
    
    
    def multi_column_data_type_change=(value) -> ::Google::Cloud::CloudDMS::V1::MultiColumnDatatypeChange

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::MultiColumnDatatypeChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MultiColumnDatatypeChange)) — Optional. Rule to specify how multiple columns should be converted to a different data type.

Note: The following fields are mutually exclusive: `multi_column_data_type_change`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MultiColumnDatatypeChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MultiColumnDatatypeChange)) — Optional. Rule to specify how multiple columns should be converted to a different data type.

Note: The following fields are mutually exclusive: `multi_column_data_type_change`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #multi_entity_rename
    
    
    def multi_entity_rename() -> ::Google::Cloud::CloudDMS::V1::MultiEntityRename

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MultiEntityRename](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MultiEntityRename)) — Optional. Rule to specify how multiple entities should be renamed.

Note: The following fields are mutually exclusive: `multi_entity_rename`, `single_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #multi_entity_rename=
    
    
    def multi_entity_rename=(value) -> ::Google::Cloud::CloudDMS::V1::MultiEntityRename

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::MultiEntityRename](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MultiEntityRename)) — Optional. Rule to specify how multiple entities should be renamed.

Note: The following fields are mutually exclusive: `multi_entity_rename`, `single_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MultiEntityRename](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MultiEntityRename)) — Optional. Rule to specify how multiple entities should be renamed.

Note: The following fields are mutually exclusive: `multi_entity_rename`, `single_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Full name of the mapping rule resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{set}/mappingRule/{rule}. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Full name of the mapping rule resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{set}/mappingRule/{rule}. 



**Returns**

  * (::String) — Full name of the mapping rule resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{set}/mappingRule/{rule}. 



### #revision_create_time
    
    
    def revision_create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Timestamp)) — Output only. The timestamp that the revision was created. 



### #revision_id
    
    
    def revision_id() -> ::String

**Returns**

  * (::String) — Output only. The revision ID of the mapping rule. A new revision is committed whenever the mapping rule is changed in any way. The format is an 8-character hexadecimal string. 



### #rule_order
    
    
    def rule_order() -> ::Integer

**Returns**

  * (::Integer) — Required. The order in which the rule is applied. Lower order rules are applied before higher value rules so they may end up being overridden. 



### #rule_order=
    
    
    def rule_order=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Required. The order in which the rule is applied. Lower order rules are applied before higher value rules so they may end up being overridden. 



**Returns**

  * (::Integer) — Required. The order in which the rule is applied. Lower order rules are applied before higher value rules so they may end up being overridden. 



### #rule_scope
    
    
    def rule_scope() -> ::Google::Cloud::CloudDMS::V1::DatabaseEntityType

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — Required. The rule scope 



### #rule_scope=
    
    
    def rule_scope=(value) -> ::Google::Cloud::CloudDMS::V1::DatabaseEntityType

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — Required. The rule scope 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseEntityType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityType)) — Required. The rule scope 



### #set_table_primary_key
    
    
    def set_table_primary_key() -> ::Google::Cloud::CloudDMS::V1::SetTablePrimaryKey

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SetTablePrimaryKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SetTablePrimaryKey)) — Optional. Rule to specify the primary key for a table

Note: The following fields are mutually exclusive: `set_table_primary_key`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #set_table_primary_key=
    
    
    def set_table_primary_key=(value) -> ::Google::Cloud::CloudDMS::V1::SetTablePrimaryKey

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::SetTablePrimaryKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SetTablePrimaryKey)) — Optional. Rule to specify the primary key for a table

Note: The following fields are mutually exclusive: `set_table_primary_key`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SetTablePrimaryKey](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SetTablePrimaryKey)) — Optional. Rule to specify the primary key for a table

Note: The following fields are mutually exclusive: `set_table_primary_key`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #single_column_change
    
    
    def single_column_change() -> ::Google::Cloud::CloudDMS::V1::SingleColumnChange

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SingleColumnChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SingleColumnChange)) — Optional. Rule to specify how a single column is converted.

Note: The following fields are mutually exclusive: `single_column_change`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #single_column_change=
    
    
    def single_column_change=(value) -> ::Google::Cloud::CloudDMS::V1::SingleColumnChange

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::SingleColumnChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SingleColumnChange)) — Optional. Rule to specify how a single column is converted.

Note: The following fields are mutually exclusive: `single_column_change`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SingleColumnChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SingleColumnChange)) — Optional. Rule to specify how a single column is converted.

Note: The following fields are mutually exclusive: `single_column_change`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #single_entity_rename
    
    
    def single_entity_rename() -> ::Google::Cloud::CloudDMS::V1::SingleEntityRename

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SingleEntityRename](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SingleEntityRename)) — Optional. Rule to specify how a single entity should be renamed.

Note: The following fields are mutually exclusive: `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #single_entity_rename=
    
    
    def single_entity_rename=(value) -> ::Google::Cloud::CloudDMS::V1::SingleEntityRename

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::SingleEntityRename](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SingleEntityRename)) — Optional. Rule to specify how a single entity should be renamed.

Note: The following fields are mutually exclusive: `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SingleEntityRename](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SingleEntityRename)) — Optional. Rule to specify how a single entity should be renamed.

Note: The following fields are mutually exclusive: `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #single_package_change
    
    
    def single_package_change() -> ::Google::Cloud::CloudDMS::V1::SinglePackageChange

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SinglePackageChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SinglePackageChange)) — Optional. Rule to specify how a single package is converted.

Note: The following fields are mutually exclusive: `single_package_change`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #single_package_change=
    
    
    def single_package_change=(value) -> ::Google::Cloud::CloudDMS::V1::SinglePackageChange

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::SinglePackageChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SinglePackageChange)) — Optional. Rule to specify how a single package is converted.

Note: The following fields are mutually exclusive: `single_package_change`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SinglePackageChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SinglePackageChange)) — Optional. Rule to specify how a single package is converted.

Note: The following fields are mutually exclusive: `single_package_change`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `source_sql_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #source_sql_change
    
    
    def source_sql_change() -> ::Google::Cloud::CloudDMS::V1::SourceSqlChange

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SourceSqlChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SourceSqlChange)) — Optional. Rule to change the sql code for an entity, for example, function, procedure.

Note: The following fields are mutually exclusive: `source_sql_change`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #source_sql_change=
    
    
    def source_sql_change=(value) -> ::Google::Cloud::CloudDMS::V1::SourceSqlChange

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::SourceSqlChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SourceSqlChange)) — Optional. Rule to change the sql code for an entity, for example, function, procedure.

Note: The following fields are mutually exclusive: `source_sql_change`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SourceSqlChange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SourceSqlChange)) — Optional. Rule to change the sql code for an entity, for example, function, procedure.

Note: The following fields are mutually exclusive: `source_sql_change`, `single_entity_rename`, `multi_entity_rename`, `entity_move`, `single_column_change`, `multi_column_data_type_change`, `conditional_column_set_value`, `convert_rowid_column`, `set_table_primary_key`, `single_package_change`, `filter_table_columns`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #state
    
    
    def state() -> ::Google::Cloud::CloudDMS::V1::MappingRule::State

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MappingRule::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRule-State)) — Optional. The mapping rule state 



### #state=
    
    
    def state=(value) -> ::Google::Cloud::CloudDMS::V1::MappingRule::State

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::MappingRule::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRule-State)) — Optional. The mapping rule state 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MappingRule::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRule-State)) — Optional. The mapping rule state 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
