---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules
title: REST Resource: projects.locations.conversionWorkspaces.mappingRules \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:33.556714+00:00
---

# REST Resource: projects.locations.conversionWorkspaces.mappingRules  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  REST Resource: projects.locations.conversionWorkspaces.mappingRules Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MappingRule
    * JSON representation
  * State
  * DatabaseEntityType
  * MappingRuleFilter
    * JSON representation
  * SingleEntityRename
    * JSON representation
  * MultiEntityRename
    * JSON representation
  * EntityNameTransformation
  * EntityMove
    * JSON representation
  * SingleColumnChange
    * JSON representation
  * MultiColumnDatatypeChange
    * JSON representation
  * SourceTextFilter
    * JSON representation
  * SourceNumericFilter
    * JSON representation
  * NumericFilterOption
  * ConditionalColumnSetValue
    * JSON representation
  * ValueTransformation
    * JSON representation
  * ValueListFilter
    * JSON representation
  * ValuePresentInList
  * IntComparisonFilter
    * JSON representation
  * ValueComparison
  * DoubleComparisonFilter
    * JSON representation
  * AssignSpecificValue
    * JSON representation
  * RoundToScale
    * JSON representation
  * ApplyHash
    * JSON representation
  * ConvertRowIdToColumn
    * JSON representation
  * SetTablePrimaryKey
    * JSON representation
  * SinglePackageChange
    * JSON representation
  * SourceSqlChange
    * JSON representation
  * FilterTableColumns
    * JSON representation
  * Methods



## Resource: MappingRule

Definition of a transformation that is to be applied to a group of entities in the source schema. Several such transformations can be applied to an entity sequentially to define the corresponding entity in the target schema.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "state": enum ([State](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#State)),
      "ruleScope": enum ([DatabaseEntityType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#DatabaseEntityType)),
      "filter": {
        object ([MappingRuleFilter](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#MappingRuleFilter))
      },
      "ruleOrder": string,
      "revisionId": string,
      "revisionCreateTime": string,
    
      // Union field details can be only one of the following:
      "singleEntityRename": {
        object ([SingleEntityRename](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SingleEntityRename))
      },
      "multiEntityRename": {
        object ([MultiEntityRename](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#MultiEntityRename))
      },
      "entityMove": {
        object ([EntityMove](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#EntityMove))
      },
      "singleColumnChange": {
        object ([SingleColumnChange](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SingleColumnChange))
      },
      "multiColumnDataTypeChange": {
        object ([MultiColumnDatatypeChange](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#MultiColumnDatatypeChange))
      },
      "conditionalColumnSetValue": {
        object ([ConditionalColumnSetValue](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#ConditionalColumnSetValue))
      },
      "convertRowidColumn": {
        object ([ConvertRowIdToColumn](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#ConvertRowIdToColumn))
      },
      "setTablePrimaryKey": {
        object ([SetTablePrimaryKey](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SetTablePrimaryKey))
      },
      "singlePackageChange": {
        object ([SinglePackageChange](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SinglePackageChange))
      },
      "sourceSqlChange": {
        object ([SourceSqlChange](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SourceSqlChange))
      },
      "filterTableColumns": {
        object ([FilterTableColumns](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#FilterTableColumns))
      }
      // End of list of possible types for union field details.
    }  
  
Fields  
---  
`name` |  `string` Full name of the mapping rule resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{set}/mappingRule/{rule}.  
`displayName` |  `string` Optional. A human readable name  
`state` |  `enum (`[State](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#State)`)` Optional. The mapping rule state  
`ruleScope` |  `enum (`[DatabaseEntityType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#DatabaseEntityType)`)` Required. The rule scope  
`filter` |  `object (`[MappingRuleFilter](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#MappingRuleFilter)`)` Required. The rule filter  
`ruleOrder` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. The order in which the rule is applied. Lower order rules are applied before higher value rules so they may end up being overridden.  
`revisionId` |  `string` Output only. The revision ID of the mapping rule. A new revision is committed whenever the mapping rule is changed in any way. The format is an 8-character hexadecimal string.  
`revisionCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp that the revision was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `details`. The rule specific details. `details` can be only one of the following:  
`singleEntityRename` |  `object (`[SingleEntityRename](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SingleEntityRename)`)` Optional. Rule to specify how a single entity should be renamed.  
`multiEntityRename` |  `object (`[MultiEntityRename](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#MultiEntityRename)`)` Optional. Rule to specify how multiple entities should be renamed.  
`entityMove` |  `object (`[EntityMove](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#EntityMove)`)` Optional. Rule to specify how multiple entities should be relocated into a different schema.  
`singleColumnChange` |  `object (`[SingleColumnChange](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SingleColumnChange)`)` Optional. Rule to specify how a single column is converted.  
`multiColumnDataTypeChange` |  `object (`[MultiColumnDatatypeChange](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#MultiColumnDatatypeChange)`)` Optional. Rule to specify how multiple columns should be converted to a different data type.  
`conditionalColumnSetValue` |  `object (`[ConditionalColumnSetValue](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#ConditionalColumnSetValue)`)` Optional. Rule to specify how the data contained in a column should be transformed (such as trimmed, rounded, etc) provided that the data meets certain criteria.  
`convertRowidColumn` |  `object (`[ConvertRowIdToColumn](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#ConvertRowIdToColumn)`)` Optional. Rule to specify how multiple tables should be converted with an additional rowid column.  
`setTablePrimaryKey` |  `object (`[SetTablePrimaryKey](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SetTablePrimaryKey)`)` Optional. Rule to specify the primary key for a table  
`singlePackageChange` |  `object (`[SinglePackageChange](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SinglePackageChange)`)` Optional. Rule to specify how a single package is converted.  
`sourceSqlChange` |  `object (`[SourceSqlChange](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SourceSqlChange)`)` Optional. Rule to change the sql code for an entity, for example, function, procedure.  
`filterTableColumns` |  `object (`[FilterTableColumns](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#FilterTableColumns)`)` Optional. Rule to specify the list of columns to include or exclude from a table.  
  
## State

The current mapping rule state such as enabled, disabled or deleted.

Enums  
---  
`STATE_UNSPECIFIED` | The state of the mapping rule is unknown.  
`ENABLED` | The rule is enabled.  
`DISABLED` | The rule is disabled.  
`DELETED` | The rule is logically deleted.  
  
## DatabaseEntityType

The type of database entities supported,

Enums  
---  
`DATABASE_ENTITY_TYPE_UNSPECIFIED` | Unspecified database entity type.  
`DATABASE_ENTITY_TYPE_SCHEMA` | Schema.  
`DATABASE_ENTITY_TYPE_TABLE` | Table.  
`DATABASE_ENTITY_TYPE_COLUMN` | Column.  
`DATABASE_ENTITY_TYPE_CONSTRAINT` | Constraint.  
`DATABASE_ENTITY_TYPE_INDEX` | Index.  
`DATABASE_ENTITY_TYPE_TRIGGER` | Trigger.  
`DATABASE_ENTITY_TYPE_VIEW` | View.  
`DATABASE_ENTITY_TYPE_SEQUENCE` | Sequence.  
`DATABASE_ENTITY_TYPE_STORED_PROCEDURE` | Stored Procedure.  
`DATABASE_ENTITY_TYPE_FUNCTION` | Function.  
`DATABASE_ENTITY_TYPE_SYNONYM` | Synonym.  
`DATABASE_ENTITY_TYPE_DATABASE_PACKAGE` | Package.  
`DATABASE_ENTITY_TYPE_UDT` | UDT.  
`DATABASE_ENTITY_TYPE_MATERIALIZED_VIEW` | Materialized View.  
`DATABASE_ENTITY_TYPE_DATABASE` | Database.  
  
## MappingRuleFilter

A filter defining the entities that a mapping rule should be applied to. When more than one field is specified, the rule is applied only to entities which match all the fields.

JSON representation  
---  
      
    
    {
      "parentEntity": string,
      "entityNamePrefix": string,
      "entityNameSuffix": string,
      "entityNameContains": string,
      "entities": [
        string
      ]
    }  
  
Fields  
---  
`parentEntity` |  `string` Optional. The rule should be applied to entities whose parent entity (fully qualified name) matches the given value. For example, if the rule applies to a table entity, the expected value should be a schema (schema). If the rule applies to a column or index entity, the expected value can be either a schema (schema) or a table (schema.table)  
`entityNamePrefix` |  `string` Optional. The rule should be applied to entities whose non-qualified name starts with the given prefix.  
`entityNameSuffix` |  `string` Optional. The rule should be applied to entities whose non-qualified name ends with the given suffix.  
`entityNameContains` |  `string` Optional. The rule should be applied to entities whose non-qualified name contains the given string.  
`entities[]` |  `string` Optional. The rule should be applied to specific entities defined by their fully qualified names.  
  
## SingleEntityRename

Options to configure rule type SingleEntityRename. The rule is used to rename an entity.

The rule filter field can refer to only one entity.

The rule scope can be one of: Database, Schema, Table, Column, Constraint, Index, View, Function, Stored Procedure, Materialized View, Sequence, UDT, Synonym

JSON representation  
---  
      
    
    {
      "newName": string
    }  
  
Fields  
---  
`newName` |  `string` Required. The new name of the destination entity  
  
## MultiEntityRename

Options to configure rule type MultiEntityRename. The rule is used to rename multiple entities.

The rule filter field can refer to one or more entities.

The rule scope can be one of: Database, Schema, Table, Column, Constraint, Index, View, Function, Stored Procedure, Materialized View, Sequence, UDT

JSON representation  
---  
      
    
    {
      "newNamePattern": string,
      "sourceNameTransformation": enum ([EntityNameTransformation](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#EntityNameTransformation))
    }  
  
Fields  
---  
`newNamePattern` |  `string` Optional. The pattern used to generate the new entity's name. This pattern must include the characters '{name}', which will be replaced with the name of the original entity. For example, the pattern 't_{name}' for an entity name jobs would be converted to 't_jobs'.If unspecified, the default value for this field is '{name}'  
`sourceNameTransformation` |  `enum (`[EntityNameTransformation](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#EntityNameTransformation)`)` Optional. Additional transformation that can be done on the source entity name before it is being used by the newNamePattern, for example lower case. If no transformation is desired, use NO_TRANSFORMATION  
  
## EntityNameTransformation

Entity Name Transformation Types

Enums  
---  
`ENTITY_NAME_TRANSFORMATION_UNSPECIFIED` | Entity name transformation unspecified.  
`ENTITY_NAME_TRANSFORMATION_NO_TRANSFORMATION` | No transformation.  
`ENTITY_NAME_TRANSFORMATION_LOWER_CASE` | Transform to lower case.  
`ENTITY_NAME_TRANSFORMATION_UPPER_CASE` | Transform to upper case.  
`ENTITY_NAME_TRANSFORMATION_CAPITALIZED_CASE` | Transform to capitalized case.  
  
## EntityMove

Options to configure rule type EntityMove. The rule is used to move an entity to a new schema.

The rule filter field can refer to one or more entities.

The rule scope can be one of: Table, Column, Constraint, Index, View, Function, Stored Procedure, Materialized View, Sequence, UDT

JSON representation  
---  
      
    
    {
      "newSchema": string
    }  
  
Fields  
---  
`newSchema` |  `string` Required. The new schema  
  
## SingleColumnChange

Options to configure rule type SingleColumnChange. The rule is used to change the properties of a column.

The rule filter field can refer to one entity.

The rule scope can be one of: Column.

When using this rule, if a field is not specified than the destination column's configuration will be the same as the one in the source column..

JSON representation  
---  
      
    
    {
      "dataType": string,
      "charset": string,
      "collation": string,
      "length": string,
      "precision": integer,
      "scale": integer,
      "fractionalSecondsPrecision": integer,
      "array": boolean,
      "arrayLength": integer,
      "nullable": boolean,
      "autoGenerated": boolean,
      "udt": boolean,
      "customFeatures": {
        object
      },
      "setValues": [
        string
      ],
      "comment": string
    }  
  
Fields  
---  
`dataType` |  `string` Optional. Column data type name.  
`charset` |  `string` Optional. Charset override - instead of table level charset.  
`collation` |  `string` Optional. Collation override - instead of table level collation.  
`length` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Column length - e.g. 50 as in varchar (50) - when relevant.  
`precision` |  `integer` Optional. Column precision - e.g. 8 as in double (8,2) - when relevant.  
`scale` |  `integer` Optional. Column scale - e.g. 2 as in double (8,2) - when relevant.  
`fractionalSecondsPrecision` |  `integer` Optional. Column fractional seconds precision - e.g. 2 as in timestamp (2) - when relevant.  
`array` |  `boolean` Optional. Is the column of array type.  
`arrayLength` |  `integer` Optional. The length of the array, only relevant if the column type is an array.  
`nullable` |  `boolean` Optional. Is the column nullable.  
`autoGenerated` |  `boolean` Optional. Is the column auto-generated/identity.  
`udt` |  `boolean` Optional. Is the column a UDT (User-defined Type).  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Custom engine specific features.  
`setValues[]` |  `string` Optional. Specifies the list of values allowed in the column.  
`comment` |  `string` Optional. Comment associated with the column.  
  
## MultiColumnDatatypeChange

Options to configure rule type MultiColumnDatatypeChange. The rule is used to change the data type and associated properties of multiple columns at once.

The rule filter field can refer to one or more entities.

The rule scope can be one of:Column.

This rule requires additional filters to be specified beyond the basic rule filter field, which is the source data type, but the rule supports additional filtering capabilities such as the minimum and maximum field length. All additional filters which are specified are required to be met in order for the rule to be applied (logical AND between the fields).

JSON representation  
---  
      
    
    {
      "sourceDataTypeFilter": string,
      "newDataType": string,
      "overrideLength": string,
      "overrideScale": integer,
      "overridePrecision": integer,
      "overrideFractionalSecondsPrecision": integer,
      "customFeatures": {
        object
      },
    
      // Union field source_filter can be only one of the following:
      "sourceTextFilter": {
        object ([SourceTextFilter](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SourceTextFilter))
      },
      "sourceNumericFilter": {
        object ([SourceNumericFilter](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SourceNumericFilter))
      }
      // End of list of possible types for union field source_filter.
    }  
  
Fields  
---  
`sourceDataTypeFilter` |  `string` Required. Filter on source data type.  
`newDataType` |  `string` Required. New data type.  
`overrideLength` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Column length - e.g. varchar (50) - if not specified and relevant uses the source column length.  
`overrideScale` |  `integer` Optional. Column scale - when relevant - if not specified and relevant uses the source column scale.  
`overridePrecision` |  `integer` Optional. Column precision - when relevant - if not specified and relevant uses the source column precision.  
`overrideFractionalSecondsPrecision` |  `integer` Optional. Column fractional seconds precision - used only for timestamp based datatypes - if not specified and relevant uses the source column fractional seconds precision.  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Custom engine specific features.  
Union field `source_filter`. Filter on source column parameters. `source_filter` can be only one of the following:  
`sourceTextFilter` |  `object (`[SourceTextFilter](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SourceTextFilter)`)` Optional. Filter for text-based data types like varchar.  
`sourceNumericFilter` |  `object (`[SourceNumericFilter](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SourceNumericFilter)`)` Optional. Filter for fixed point number data types such as NUMERIC/NUMBER.  
  
## SourceTextFilter

Filter for text-based data types like varchar.

JSON representation  
---  
      
    
    {
      "sourceMinLengthFilter": string,
      "sourceMaxLengthFilter": string
    }  
  
Fields  
---  
`sourceMinLengthFilter` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The filter will match columns with length greater than or equal to this number.  
`sourceMaxLengthFilter` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The filter will match columns with length smaller than or equal to this number.  
  
## SourceNumericFilter

Filter for fixed point number data types such as NUMERIC/NUMBER

JSON representation  
---  
      
    
    {
      "sourceMinScaleFilter": integer,
      "sourceMaxScaleFilter": integer,
      "sourceMinPrecisionFilter": integer,
      "sourceMaxPrecisionFilter": integer,
      "numericFilterOption": enum ([NumericFilterOption](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#NumericFilterOption))
    }  
  
Fields  
---  
`sourceMinScaleFilter` |  `integer` Optional. The filter will match columns with scale greater than or equal to this number.  
`sourceMaxScaleFilter` |  `integer` Optional. The filter will match columns with scale smaller than or equal to this number.  
`sourceMinPrecisionFilter` |  `integer` Optional. The filter will match columns with precision greater than or equal to this number.  
`sourceMaxPrecisionFilter` |  `integer` Optional. The filter will match columns with precision smaller than or equal to this number.  
`numericFilterOption` |  `enum (`[NumericFilterOption](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#NumericFilterOption)`)` Required. Enum to set the option defining the datatypes numeric filter has to be applied to  
  
## NumericFilterOption

Specifies the columns on which numeric filter needs to be applied.

Enums  
---  
`NUMERIC_FILTER_OPTION_UNSPECIFIED` | Numeric filter option unspecified  
`NUMERIC_FILTER_OPTION_ALL` | Numeric filter option that matches all numeric columns.  
`NUMERIC_FILTER_OPTION_LIMIT` | Numeric filter option that matches columns having numeric datatypes with specified precision and scale within the limited range of filter.  
`NUMERIC_FILTER_OPTION_LIMITLESS` | Numeric filter option that matches only the numeric columns with no precision and scale specified.  
  
## ConditionalColumnSetValue

Options to configure rule type ConditionalColumnSetValue. The rule is used to transform the data which is being replicated/migrated.

The rule filter field can refer to one or more entities.

The rule scope can be one of: Column.

JSON representation  
---  
      
    
    {
      "valueTransformation": {
        object ([ValueTransformation](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#ValueTransformation))
      },
      "customFeatures": {
        object
      },
    
      // Union field source_filter can be only one of the following:
      "sourceTextFilter": {
        object ([SourceTextFilter](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SourceTextFilter))
      },
      "sourceNumericFilter": {
        object ([SourceNumericFilter](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SourceNumericFilter))
      }
      // End of list of possible types for union field source_filter.
    }  
  
Fields  
---  
`valueTransformation` |  `object (`[ValueTransformation](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#ValueTransformation)`)` Required. Description of data transformation during migration.  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Custom engine specific features.  
Union field `source_filter`.`source_filter` can be only one of the following:  
`sourceTextFilter` |  `object (`[SourceTextFilter](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SourceTextFilter)`)` Optional. Optional filter on source column length. Used for text based data types like varchar.  
`sourceNumericFilter` |  `object (`[SourceNumericFilter](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#SourceNumericFilter)`)` Optional. Optional filter on source column precision and scale. Used for fixed point numbers such as NUMERIC/NUMBER data types.  
  
## ValueTransformation

Description of data transformation during migration as part of the ConditionalColumnSetValue.

JSON representation  
---  
      
    
    {
    
      // Union field filter can be only one of the following:
      "isNull": {
        object
      },
      "valueList": {
        object ([ValueListFilter](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#ValueListFilter))
      },
      "intComparison": {
        object ([IntComparisonFilter](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#IntComparisonFilter))
      },
      "doubleComparison": {
        object ([DoubleComparisonFilter](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#DoubleComparisonFilter))
      }
      // End of list of possible types for union field filter.
    
      // Union field action can be only one of the following:
      "assignNull": {
        object
      },
      "assignSpecificValue": {
        object ([AssignSpecificValue](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#AssignSpecificValue))
      },
      "assignMinValue": {
        object
      },
      "assignMaxValue": {
        object
      },
      "roundScale": {
        object ([RoundToScale](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#RoundToScale))
      },
      "applyHash": {
        object ([ApplyHash](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#ApplyHash))
      }
      // End of list of possible types for union field action.
    }  
  
Fields  
---  
Union field `filter`.`filter` can be only one of the following:  
`isNull` |  `object` Optional. Value is null  
`valueList` |  `object (`[ValueListFilter](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#ValueListFilter)`)` Optional. Value is found in the specified list.  
`intComparison` |  `object (`[IntComparisonFilter](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#IntComparisonFilter)`)` Optional. Filter on relation between source value and compare value of type integer.  
`doubleComparison` |  `object (`[DoubleComparisonFilter](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#DoubleComparisonFilter)`)` Optional. Filter on relation between source value and compare value of type double.  
Union field `action`.`action` can be only one of the following:  
`assignNull` |  `object` Optional. Set to null  
`assignSpecificValue` |  `object (`[AssignSpecificValue](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#AssignSpecificValue)`)` Optional. Set to a specific value (value is converted to fit the target data type)  
`assignMinValue` |  `object` Optional. Set to minValue - if integer or numeric, will use int.minvalue, etc  
`assignMaxValue` |  `object` Optional. Set to maxValue - if integer or numeric, will use int.maxvalue, etc  
`roundScale` |  `object (`[RoundToScale](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#RoundToScale)`)` Optional. Allows the data to change scale  
`applyHash` |  `object (`[ApplyHash](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#ApplyHash)`)` Optional. Applies a hash function on the data  
  
## ValueListFilter

A list of values to filter by in ConditionalColumnSetValue

JSON representation  
---  
      
    
    {
      "valuePresentList": enum ([ValuePresentInList](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#ValuePresentInList)),
      "values": [
        string
      ],
      "ignoreCase": boolean
    }  
  
Fields  
---  
`valuePresentList` |  `enum (`[ValuePresentInList](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#ValuePresentInList)`)` Required. Indicates whether the filter matches rows with values that are present in the list or those with values not present in it.  
`values[]` |  `string` Required. The list to be used to filter by  
`ignoreCase` |  `boolean` Required. Whether to ignore case when filtering by values. Defaults to false  
  
## ValuePresentInList

Enum used by ValueListFilter to indicate whether the source value is in the supplied list

Enums  
---  
`VALUE_PRESENT_IN_LIST_UNSPECIFIED` | Value present in list unspecified  
`VALUE_PRESENT_IN_LIST_IF_VALUE_LIST` | If the source value is in the supplied list at valueList  
`VALUE_PRESENT_IN_LIST_IF_VALUE_NOT_LIST` | If the source value is not in the supplied list at valueList  
  
## IntComparisonFilter

Filter based on relation between source value and compare value of type integer in ConditionalColumnSetValue

JSON representation  
---  
      
    
    {
      "valueComparison": enum ([ValueComparison](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#ValueComparison)),
      "value": string
    }  
  
Fields  
---  
`valueComparison` |  `enum (`[ValueComparison](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#ValueComparison)`)` Required. Relation between source value and compare value  
`value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. Integer compare value to be used  
  
## ValueComparison

Enum used by IntComparisonFilter and DoubleComparisonFilter to indicate the relation between source value and compare value.

Enums  
---  
`VALUE_COMPARISON_UNSPECIFIED` | Value comparison unspecified.  
`VALUE_COMPARISON_IF_VALUE_SMALLER_THAN` | Value is smaller than the Compare value.  
`VALUE_COMPARISON_IF_VALUE_SMALLER_EQUAL_THAN` | Value is smaller or equal than the Compare value.  
`VALUE_COMPARISON_IF_VALUE_LARGER_THAN` | Value is larger than the Compare value.  
`VALUE_COMPARISON_IF_VALUE_LARGER_EQUAL_THAN` | Value is larger or equal than the Compare value.  
  
## DoubleComparisonFilter

Filter based on relation between source value and compare value of type double in ConditionalColumnSetValue

JSON representation  
---  
      
    
    {
      "valueComparison": enum ([ValueComparison](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#ValueComparison)),
      "value": number
    }  
  
Fields  
---  
`valueComparison` |  `enum (`[ValueComparison](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#ValueComparison)`)` Required. Relation between source value and compare value  
`value` |  `number` Required. Double compare value to be used  
  
## AssignSpecificValue

Set to a specific value (value is converted to fit the target data type)

JSON representation  
---  
      
    
    {
      "value": string
    }  
  
Fields  
---  
`value` |  `string` Required. Specific value to be assigned  
  
## RoundToScale

This allows the data to change scale, for example if the source is 2 digits after the decimal point, specify round to scale value = 2. If for example the value needs to be converted to an integer, use round to scale value = 0.

JSON representation  
---  
      
    
    {
      "scale": integer
    }  
  
Fields  
---  
`scale` |  `integer` Required. Scale value to be used  
  
## ApplyHash

Apply a hash function on the value.

JSON representation  
---  
      
    
    {
    
      // Union field hash_function can be only one of the following:
      "uuidFromBytes": {
        object
      }
      // End of list of possible types for union field hash_function.
    }  
  
Fields  
---  
Union field `hash_function`.`hash_function` can be only one of the following:  
`uuidFromBytes` |  `object` Optional. Generate UUID from the data's byte array  
  
## ConvertRowIdToColumn

Options to configure rule type ConvertROWIDToColumn. The rule is used to add column rowid to destination tables based on an Oracle rowid function/property.

The rule filter field can refer to one or more entities.

The rule scope can be one of: Table.

This rule requires additional filter to be specified beyond the basic rule filter field, which is whether or not to work on tables which already have a primary key defined.

JSON representation  
---  
      
    
    {
      "onlyIfNoPrimaryKey": boolean
    }  
  
Fields  
---  
`onlyIfNoPrimaryKey` |  `boolean` Required. Only work on tables without primary key defined  
  
## SetTablePrimaryKey

Options to configure rule type SetTablePrimaryKey. The rule is used to specify the columns and name to configure/alter the primary key of a table.

The rule filter field can refer to one entity.

The rule scope can be one of: Table.

JSON representation  
---  
      
    
    {
      "primaryKeyColumns": [
        string
      ],
      "primaryKey": string
    }  
  
Fields  
---  
`primaryKeyColumns[]` |  `string` Required. List of column names for the primary key  
`primaryKey` |  `string` Optional. Name for the primary key  
  
## SinglePackageChange

Options to configure rule type SinglePackageChange. The rule is used to alter the sql code for a package entities.

The rule filter field can refer to one entity.

The rule scope can be: Package

JSON representation  
---  
      
    
    {
      "packageDescription": string,
      "packageBody": string
    }  
  
Fields  
---  
`packageDescription` |  `string` Optional. Sql code for package description  
`packageBody` |  `string` Optional. Sql code for package body  
  
## SourceSqlChange

Options to configure rule type SourceSqlChange. The rule is used to alter the sql code for database entities.

The rule filter field can refer to one entity.

The rule scope can be: StoredProcedure, Function, Trigger, View

JSON representation  
---  
      
    
    {
      "sqlCode": string
    }  
  
Fields  
---  
`sqlCode` |  `string` Required. Sql code for source (stored procedure, function, trigger or view)  
  
## FilterTableColumns

Options to configure rule type FilterTableColumns. The rule is used to filter the list of columns to include or exclude from a table.

The rule filter field can refer to one entity.

The rule scope can be: Table

Only one of the two lists can be specified for the rule.

JSON representation  
---  
      
    
    {
      "includeColumns": [
        string
      ],
      "excludeColumns": [
        string
      ]
    }  
  
Fields  
---  
`includeColumns[]` |  `string` Optional. List of columns to be included for a particular table.  
`excludeColumns[]` |  `string` Optional. List of columns to be excluded for a particular table.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules/create)`

|  Creates a new mapping rule for a given conversion workspace.  
  
### `[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules/delete)`

|  Deletes a single mapping rule.  
  
### `[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules/get)`

|  Gets the details of a mapping rule.  
  
### `[import](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules/import)`

|  Imports the mapping rules for a given conversion workspace.  
  
### `[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules/list)`

|  Lists the mapping rules for a specific conversion workspace.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-26 UTC."],[],[]] 
