---
url: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query/
title: Method: projects.locations.repositories.compilationResults.query \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:42:20.927363+00:00
---

# Method: projects.locations.repositories.compilationResults.query  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  Method: projects.locations.repositories.compilationResults.query Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * CompilationResultAction
    * JSON representation
  * Relation
    * JSON representation
  * RelationDescriptor
    * JSON representation
  * ColumnDescriptor
    * JSON representation
  * RelationType
  * IncrementalTableConfig
    * JSON representation
  * TableFormat
  * FileFormat
  * Operations
    * JSON representation
  * Assertion
    * JSON representation
  * Declaration
    * JSON representation
  * Notebook
    * JSON representation
  * DataPreparation
    * JSON representation
  * SqlDefinition
    * JSON representation
  * ErrorTable
    * JSON representation
  * LoadConfig
    * JSON representation
  * SimpleLoadMode
  * IncrementalLoadMode
    * JSON representation
  * Try it!



Returns CompilationResultActions in a given CompilationResult.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4

  
`GET https://dataform.googleapis.com/v1beta1/{name=projects/*/locations/*/repositories/*/compilationResults/*}:query`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The compilation result's name. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dataform.compilationResults.query`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum number of compilation results to return. The server may return fewer items than requested. If unspecified, the server will pick an appropriate default.  
`pageToken` |  `string` Optional. Page token received from a previous `compilationResults.query` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `compilationResults.query`, with the exception of `pageSize`, must match the call that provided the page token.  
`filter` |  `string` Optional. Optional filter for the returned list. Filtering is only currently supported on the `filePath` field.  
  
### Request body

The request body must be empty.

### Response body

`compilationResults.query` response message.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "compilationResultActions": [
        {
          object ([CompilationResultAction](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#CompilationResultAction))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`compilationResultActions[]` |  `object (`[CompilationResultAction](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#CompilationResultAction)`)` List of compilation result actions.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/bigquery`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `dataform.compilationResults.query`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## CompilationResultAction

Represents a single Dataform action in a compilation result.

JSON representation  
---  
      
    
    {
      "target": {
        object ([Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target))
      },
      "canonicalTarget": {
        object ([Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target))
      },
      "filePath": string,
    
      // Union field compiled_object can be only one of the following:
      "relation": {
        object ([Relation](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#Relation))
      },
      "operations": {
        object ([Operations](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#Operations))
      },
      "assertion": {
        object ([Assertion](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#Assertion))
      },
      "declaration": {
        object ([Declaration](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#Declaration))
      },
      "notebook": {
        object ([Notebook](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#Notebook))
      },
      "dataPreparation": {
        object ([DataPreparation](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#DataPreparation))
      }
      // End of list of possible types for union field compiled_object.
      "internalMetadata": string
    }  
  
Fields  
---  
`target` |  `object (`[Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target)`)` This action's identifier. Unique within the compilation result.  
`canonicalTarget` |  `object (`[Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target)`)` The action's identifier if the project had been compiled without any overrides configured. Unique within the compilation result.  
`filePath` |  `string` The full path including filename in which this action is located, relative to the workspace root.  
Union field `compiled_object`. The compiled object. `compiled_object` can be only one of the following:  
`relation` |  `object (`[Relation](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#Relation)`)` The database relation created/updated by this action.  
`operations` |  `object (`[Operations](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#Operations)`)` The database operations executed by this action.  
`assertion` |  `object (`[Assertion](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#Assertion)`)` The assertion executed by this action.  
`declaration` |  `object (`[Declaration](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#Declaration)`)` The declaration declared by this action.  
`notebook` |  `object (`[Notebook](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#Notebook)`)` The notebook executed by this action.  
`dataPreparation` |  `object (`[DataPreparation](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#DataPreparation)`)` The data preparation executed by this action.  
`internalMetadata` |  `string` Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.  
  
## Relation

Represents a database relation.

JSON representation  
---  
      
    
    {
      "dependencyTargets": [
        {
          object ([Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target))
        }
      ],
      "disabled": boolean,
      "tags": [
        string
      ],
      "relationDescriptor": {
        object ([RelationDescriptor](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#RelationDescriptor))
      },
      "relationType": enum ([RelationType](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#RelationType)),
      "selectQuery": string,
      "preOperations": [
        string
      ],
      "postOperations": [
        string
      ],
      "incrementalTableConfig": {
        object ([IncrementalTableConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#IncrementalTableConfig))
      },
      "partitionExpression": string,
      "clusterExpressions": [
        string
      ],
      "partitionExpirationDays": integer,
      "requirePartitionFilter": boolean,
      "additionalOptions": {
        string: string,
        ...
      },
      "connection": string,
      "tableFormat": enum ([TableFormat](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#TableFormat)),
      "fileFormat": enum ([FileFormat](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#FileFormat)),
      "storageUri": string
    }  
  
Fields  
---  
`dependencyTargets[]` |  `object (`[Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target)`)` A list of actions that this action depends on.  
`disabled` |  `boolean` Whether this action is disabled (i.e. should not be run).  
`tags[]` |  `string` Arbitrary, user-defined tags on this action.  
`relationDescriptor` |  `object (`[RelationDescriptor](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#RelationDescriptor)`)` Descriptor for the relation and its columns.  
`relationType` |  `enum (`[RelationType](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#RelationType)`)` The type of this relation.  
`selectQuery` |  `string` The SELECT query which returns rows which this relation should contain.  
`preOperations[]` |  `string` SQL statements to be executed before creating the relation.  
`postOperations[]` |  `string` SQL statements to be executed after creating the relation.  
`incrementalTableConfig` |  `object (`[IncrementalTableConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#IncrementalTableConfig)`)` Configures `INCREMENTAL_TABLE` settings for this relation. Only set if `relationType` is `INCREMENTAL_TABLE`.  
`partitionExpression` |  `string` The SQL expression used to partition the relation.  
`clusterExpressions[]` |  `string` A list of columns or SQL expressions used to cluster the table.  
`partitionExpirationDays` |  `integer` Sets the partition expiration in days.  
`requirePartitionFilter` |  `boolean` Specifies whether queries on this table must include a predicate filter that filters on the partitioning column.  
`additionalOptions` |  `map (key: string, value: string)` Additional options that will be provided as key/value pairs into the options clause of a create table/view statement. See <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language> for more information on which options are supported.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`connection` |  `string` Optional. The connection specifying the credentials to be used to read and write to external storage, such as Cloud Storage. The connection can have the form `{project}.{location}.{connection_id}` or `projects/{project}/locations/{location}/connections/{connection_id}`, or be set to DEFAULT.  
`tableFormat` |  `enum (`[TableFormat](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#TableFormat)`)` Optional. The table format for the BigQuery table.  
`fileFormat` |  `enum (`[FileFormat](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#FileFormat)`)` Optional. The file format for the BigQuery table.  
`storageUri` |  `string` Optional. The fully qualified location prefix of the external folder where table data is stored. The URI should be in the format `gs://bucket/path_to_table/`.  
  
## RelationDescriptor

Describes a relation and its columns.

JSON representation  
---  
      
    
    {
      "description": string,
      "columns": [
        {
          object ([ColumnDescriptor](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#ColumnDescriptor))
        }
      ],
      "bigqueryLabels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`description` |  `string` A text description of the relation.  
`columns[]` |  `object (`[ColumnDescriptor](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#ColumnDescriptor)`)` A list of descriptions of columns within the relation.  
`bigqueryLabels` |  `map (key: string, value: string)` A set of BigQuery labels that should be applied to the relation.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## ColumnDescriptor

Describes a column.

JSON representation  
---  
      
    
    {
      "path": [
        string
      ],
      "description": string,
      "bigqueryPolicyTags": [
        string
      ]
    }  
  
Fields  
---  
`path[]` |  `string` The identifier for the column. Each entry in `path` represents one level of nesting.  
`description` |  `string` A textual description of the column.  
`bigqueryPolicyTags[]` |  `string` A list of BigQuery policy tags that will be applied to the column.  
  
## RelationType

Indicates the type of this relation.

Enums  
---  
`RELATION_TYPE_UNSPECIFIED` | Default value. This value is unused.  
`TABLE` | The relation is a table.  
`VIEW` | The relation is a view.  
`INCREMENTAL_TABLE` | The relation is an incrementalized table.  
`MATERIALIZED_VIEW` | The relation is a materialized view.  
  
## IncrementalTableConfig

Contains settings for relations of type `INCREMENTAL_TABLE`.

JSON representation  
---  
      
    
    {
      "incrementalSelectQuery": string,
      "refreshDisabled": boolean,
      "uniqueKeyParts": [
        string
      ],
      "updatePartitionFilter": string,
      "incrementalPreOperations": [
        string
      ],
      "incrementalPostOperations": [
        string
      ]
    }  
  
Fields  
---  
`incrementalSelectQuery` |  `string` The SELECT query which returns rows which should be inserted into the relation if it already exists and is not being refreshed.  
`refreshDisabled` |  `boolean` Whether this table should be protected from being refreshed.  
`uniqueKeyParts[]` |  `string` A set of columns or SQL expressions used to define row uniqueness. If any duplicates are discovered (as defined by `uniqueKeyParts`), only the newly selected rows (as defined by `incrementalSelectQuery`) will be included in the relation.  
`updatePartitionFilter` |  `string` A SQL expression conditional used to limit the set of existing rows considered for a merge operation (see `uniqueKeyParts` for more information).  
`incrementalPreOperations[]` |  `string` SQL statements to be executed before inserting new rows into the relation.  
`incrementalPostOperations[]` |  `string` SQL statements to be executed after inserting new rows into the relation.  
  
## TableFormat

Supported table formats for BigQuery tables.

Enums  
---  
`TABLE_FORMAT_UNSPECIFIED` | Default value.  
`ICEBERG` | Apache Iceberg format.  
  
## FileFormat

Supported file formats for BigQuery tables.

Enums  
---  
`FILE_FORMAT_UNSPECIFIED` | Default value.  
`PARQUET` | Apache Parquet format.  
  
## Operations

Represents a list of arbitrary database operations.

JSON representation  
---  
      
    
    {
      "dependencyTargets": [
        {
          object ([Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target))
        }
      ],
      "disabled": boolean,
      "tags": [
        string
      ],
      "relationDescriptor": {
        object ([RelationDescriptor](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#RelationDescriptor))
      },
      "queries": [
        string
      ],
      "hasOutput": boolean
    }  
  
Fields  
---  
`dependencyTargets[]` |  `object (`[Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target)`)` A list of actions that this action depends on.  
`disabled` |  `boolean` Whether this action is disabled (i.e. should not be run).  
`tags[]` |  `string` Arbitrary, user-defined tags on this action.  
`relationDescriptor` |  `object (`[RelationDescriptor](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#RelationDescriptor)`)` Descriptor for any output relation and its columns. Only set if `hasOutput` is true.  
`queries[]` |  `string` A list of arbitrary SQL statements that will be executed without alteration.  
`hasOutput` |  `boolean` Whether these operations produce an output relation.  
  
## Assertion

Represents an assertion upon a SQL query which is required return zero rows.

JSON representation  
---  
      
    
    {
      "dependencyTargets": [
        {
          object ([Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target))
        }
      ],
      "parentAction": {
        object ([Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target))
      },
      "disabled": boolean,
      "tags": [
        string
      ],
      "selectQuery": string,
      "relationDescriptor": {
        object ([RelationDescriptor](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#RelationDescriptor))
      }
    }  
  
Fields  
---  
`dependencyTargets[]` |  `object (`[Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target)`)` A list of actions that this action depends on.  
`parentAction` |  `object (`[Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target)`)` The parent action of this assertion. Only set if this assertion was automatically generated.  
`disabled` |  `boolean` Whether this action is disabled (i.e. should not be run).  
`tags[]` |  `string` Arbitrary, user-defined tags on this action.  
`selectQuery` |  `string` The SELECT query which must return zero rows in order for this assertion to succeed.  
`relationDescriptor` |  `object (`[RelationDescriptor](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#RelationDescriptor)`)` Descriptor for the assertion's automatically-generated view and its columns.  
  
## Declaration

Represents a relation which is not managed by Dataform but which may be referenced by Dataform actions.

JSON representation  
---  
      
    
    {
      "relationDescriptor": {
        object ([RelationDescriptor](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#RelationDescriptor))
      }
    }  
  
Fields  
---  
`relationDescriptor` |  `object (`[RelationDescriptor](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#RelationDescriptor)`)` Descriptor for the relation and its columns. Used as documentation only, i.e. values here will result in no changes to the relation's metadata.  
  
## Notebook

Represents a notebook.

JSON representation  
---  
      
    
    {
      "dependencyTargets": [
        {
          object ([Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target))
        }
      ],
      "disabled": boolean,
      "contents": string,
      "tags": [
        string
      ]
    }  
  
Fields  
---  
`dependencyTargets[]` |  `object (`[Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target)`)` A list of actions that this action depends on.  
`disabled` |  `boolean` Whether this action is disabled (i.e. should not be run).  
`contents` |  `string` The contents of the notebook.  
`tags[]` |  `string` Arbitrary, user-defined tags on this action.  
  
## DataPreparation

Defines a compiled Data Preparation entity

JSON representation  
---  
      
    
    {
      "dependencyTargets": [
        {
          object ([Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target))
        }
      ],
      "disabled": boolean,
      "tags": [
        string
      ],
    
      // Union field definition can be only one of the following:
      "contentsYaml": string,
      "contentsSql": {
        object ([SqlDefinition](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#SqlDefinition))
      }
      // End of list of possible types for union field definition.
    }  
  
Fields  
---  
`dependencyTargets[]` |  `object (`[Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target)`)` A list of actions that this action depends on.  
`disabled` |  `boolean` Whether this action is disabled (i.e. should not be run).  
`tags[]` |  `string` Arbitrary, user-defined tags on this action.  
Union field `definition`. The definition for the data preparation. `definition` can be only one of the following:  
`contentsYaml` |  `string` The data preparation definition, stored as a YAML string.  
`contentsSql` |  `object (`[SqlDefinition](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#SqlDefinition)`)` SQL definition for a Data Preparation. Contains a SQL query and additional context information.  
  
## SqlDefinition

Definition of a SQL Data Preparation

JSON representation  
---  
      
    
    {
      "query": string,
      "errorTable": {
        object ([ErrorTable](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#ErrorTable))
      },
      "load": {
        object ([LoadConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#LoadConfig))
      }
    }  
  
Fields  
---  
`query` |  `string` The SQL query representing the data preparation steps. Formatted as a Pipe SQL query statement.  
`errorTable` |  `object (`[ErrorTable](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#ErrorTable)`)` Error table configuration,  
`load` |  `object (`[LoadConfig](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#LoadConfig)`)` Load configuration.  
  
## ErrorTable

Error table information, used to write error data into a BigQuery table.

JSON representation  
---  
      
    
    {
      "target": {
        object ([Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target))
      },
      "retentionDays": integer
    }  
  
Fields  
---  
`target` |  `object (`[Target](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/Target)`)` Error Table target.  
`retentionDays` |  `integer` Error table partition expiration in days. Only positive values are allowed.  
  
## LoadConfig

Simplified load configuration for actions

JSON representation  
---  
      
    
    {
    
      // Union field mode can be only one of the following:
      "replace": {
        object ([SimpleLoadMode](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#SimpleLoadMode))
      },
      "append": {
        object ([SimpleLoadMode](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#SimpleLoadMode))
      },
      "maximum": {
        object ([IncrementalLoadMode](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#IncrementalLoadMode))
      },
      "unique": {
        object ([IncrementalLoadMode](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#IncrementalLoadMode))
      }
      // End of list of possible types for union field mode.
    }  
  
Fields  
---  
Union field `mode`. Load mode `mode` can be only one of the following:  
`replace` |  `object (`[SimpleLoadMode](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#SimpleLoadMode)`)` Replace destination table  
`append` |  `object (`[SimpleLoadMode](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#SimpleLoadMode)`)` Append into destination table  
`maximum` |  `object (`[IncrementalLoadMode](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#IncrementalLoadMode)`)` Insert records where the value exceeds the previous maximum value for a column in the destination table  
`unique` |  `object (`[IncrementalLoadMode](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults/query#IncrementalLoadMode)`)` Insert records where the value of a column is not already present in the destination table  
  
## SimpleLoadMode

This type has no fields.

Simple load definition

## IncrementalLoadMode

Load definition for incremental load modes

JSON representation  
---  
      
    
    {
      "column": string
    }  
  
Fields  
---  
`column` |  `string` Column name for incremental load modes  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-27 UTC."],[],[]] 
