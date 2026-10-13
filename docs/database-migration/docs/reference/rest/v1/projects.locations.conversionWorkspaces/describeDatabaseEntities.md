---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities/
title: Method: projects.locations.conversionWorkspaces.describeDatabaseEntities \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:31.520558+00:00
---

# Method: projects.locations.conversionWorkspaces.describeDatabaseEntities  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  Method: projects.locations.conversionWorkspaces.describeDatabaseEntities Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * DBTreeType
  * DatabaseEntityView
  * DatabaseEntity
    * JSON representation
  * TreeType
  * EntityMapping
    * JSON representation
  * EntityMappingLogEntry
    * JSON representation
  * EntityDdl
    * JSON representation
  * DdlKind
  * EntityIssue
    * JSON representation
  * IssueType
  * IssueSeverity
  * Position
    * JSON representation
  * DatabaseInstanceEntity
    * JSON representation
  * SchemaEntity
    * JSON representation
  * TableEntity
    * JSON representation
  * ColumnEntity
    * JSON representation
  * ConstraintEntity
    * JSON representation
  * IndexEntity
    * JSON representation
  * TriggerEntity
    * JSON representation
  * ViewEntity
    * JSON representation
  * SequenceEntity
    * JSON representation
  * StoredProcedureEntity
    * JSON representation
  * FunctionEntity
    * JSON representation
  * SynonymEntity
    * JSON representation
  * PackageEntity
    * JSON representation
  * UDTEntity
    * JSON representation
  * MaterializedViewEntity
    * JSON representation
  * Examples
  * Try it!



Describes the database entities tree for a specific conversion workspace and a specific tree type.

Database entities are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are simple data objects describing the structure of the client database.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 asia-southeast3 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west15 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-central2 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8

  
`GET https://datamigration.googleapis.com/v1/{conversionWorkspace}:describeDatabaseEntities`

### Path parameters

Parameters  
---  
`conversionWorkspace` |  `string` Required. Name of the conversion workspace resource whose database entities are described. Must be in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversionWorkspace}.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of entities to return. The service may return fewer entities than the value specifies.  
`pageToken` |  `string` Optional. The nextPageToken value received in the previous call to conversionWorkspace.describeDatabaseEntities, used in the subsequent request to retrieve the next page of results. On first call this should be left blank. When paginating, all other parameters provided to conversionWorkspace.describeDatabaseEntities must match the call that provided the page token.  
`tree` |  `enum (`[DBTreeType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#DBTreeType)`)` Required. The tree to fetch.  
`uncommitted` |  `boolean` Optional. Whether to retrieve the latest committed version of the entities or the latest version. This field is ignored if a specific commitId is specified.  
`commitId` |  `string` Optional. Request a specific commit ID. If not specified, the entities from the latest commit are returned.  
`filter` |  `string` Optional. Filter the returned entities based on AIP-160 standard.  
`view` |  `enum (`[DatabaseEntityView](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#DatabaseEntityView)`)` Optional. Results view based on AIP-157  
  
### Request body

The request body must be empty.

### Response body

Response message for 'conversionWorkspaces.describeDatabaseEntities' request.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "databaseEntities": [
        {
          object ([DatabaseEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#DatabaseEntity))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`databaseEntities[]` |  `object (`[DatabaseEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#DatabaseEntity)`)` The list of database entities for the conversion workspace.  
`nextPageToken` |  `string` A token which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-datamigration `



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `conversionWorkspace` resource:

  * `datamigration.conversionworkspaces.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## DBTreeType

The type of a tree to return

Enums  
---  
`DB_TREE_TYPE_UNSPECIFIED` | Unspecified tree type.  
`SOURCE_TREE` | The source database tree.  
`DRAFT_TREE` | The draft database tree.  
`DESTINATION_TREE` | The destination database tree.  
  
## DatabaseEntityView

AIP-157 Partial Response view for Database Entity.

Enums  
---  
`DATABASE_ENTITY_VIEW_UNSPECIFIED` | Unspecified view. Defaults to basic view.  
`DATABASE_ENTITY_VIEW_BASIC` | Default view. Does not return DDLs or Issues.  
`DATABASE_ENTITY_VIEW_FULL` | Return full entity details including mappings, ddl and issues.  
`DATABASE_ENTITY_VIEW_ROOT_SUMMARY` | Top-most (Database, Schema) nodes which are returned contains summary details for their descendants such as the number of entities per type and issues rollups. When this view is used, only a single page of result is returned and the pageSize property of the request is ignored. The returned page will only include the top-most node types.  
`DATABASE_ENTITY_VIEW_FULL_COMPACT` | Returns full entity details except for ddls and schema custom features.  
  
## DatabaseEntity

The base entity type for all the database related entities. The message contains the entity name, the name of its parent, the entity type, and the specific details per entity type.

JSON representation  
---  
      
    
    {
      "shortName": string,
      "parentEntity": string,
      "tree": enum ([TreeType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#TreeType)),
      "entityType": enum ([DatabaseEntityType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#DatabaseEntityType)),
      "mappings": [
        {
          object ([EntityMapping](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#EntityMapping))
        }
      ],
      "entityDdl": [
        {
          object ([EntityDdl](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#EntityDdl))
        }
      ],
      "issues": [
        {
          object ([EntityIssue](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#EntityIssue))
        }
      ],
    
      // Union field entity_body can be only one of the following:
      "database": {
        object ([DatabaseInstanceEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#DatabaseInstanceEntity))
      },
      "schema": {
        object ([SchemaEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#SchemaEntity))
      },
      "table": {
        object ([TableEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#TableEntity))
      },
      "view": {
        object ([ViewEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#ViewEntity))
      },
      "sequence": {
        object ([SequenceEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#SequenceEntity))
      },
      "storedProcedure": {
        object ([StoredProcedureEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#StoredProcedureEntity))
      },
      "databaseFunction": {
        object ([FunctionEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#FunctionEntity))
      },
      "synonym": {
        object ([SynonymEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#SynonymEntity))
      },
      "databasePackage": {
        object ([PackageEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#PackageEntity))
      },
      "udt": {
        object ([UDTEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#UDTEntity))
      },
      "materializedView": {
        object ([MaterializedViewEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#MaterializedViewEntity))
      }
      // End of list of possible types for union field entity_body.
    }  
  
Fields  
---  
`shortName` |  `string` The short name (e.g. table name) of the entity.  
`parentEntity` |  `string` The full name of the parent entity (e.g. schema name).  
`tree` |  `enum (`[TreeType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#TreeType)`)` The type of tree the entity belongs to.  
`entityType` |  `enum (`[DatabaseEntityType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#DatabaseEntityType)`)` The type of the database entity (table, view, index, ...).  
`mappings[]` |  `object (`[EntityMapping](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#EntityMapping)`)` Details about entity mappings. For source tree entities, this holds the draft entities which were generated by the mapping rules. For draft tree entities, this holds the source entities which were converted to form the draft entity. Destination entities will have no mapping details.  
`entityDdl[]` |  `object (`[EntityDdl](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#EntityDdl)`)` Details about the entity DDL script. Multiple DDL scripts are provided for child entities such as a table entity will have one DDL for the table with additional DDLs for each index, constraint and such.  
`issues[]` |  `object (`[EntityIssue](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#EntityIssue)`)` Details about the various issues found for the entity.  
Union field `entity_body`. The specific body for each entity type. `entity_body` can be only one of the following:  
`database` |  `object (`[DatabaseInstanceEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#DatabaseInstanceEntity)`)` Database.  
`schema` |  `object (`[SchemaEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#SchemaEntity)`)` Schema.  
`table` |  `object (`[TableEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#TableEntity)`)` Table.  
`view` |  `object (`[ViewEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#ViewEntity)`)` View.  
`sequence` |  `object (`[SequenceEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#SequenceEntity)`)` Sequence.  
`storedProcedure` |  `object (`[StoredProcedureEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#StoredProcedureEntity)`)` Stored procedure.  
`databaseFunction` |  `object (`[FunctionEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#FunctionEntity)`)` Function.  
`synonym` |  `object (`[SynonymEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#SynonymEntity)`)` Synonym.  
`databasePackage` |  `object (`[PackageEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#PackageEntity)`)` Package.  
`udt` |  `object (`[UDTEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#UDTEntity)`)` UDT.  
`materializedView` |  `object (`[MaterializedViewEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#MaterializedViewEntity)`)` Materialized view.  
  
## TreeType

The type of database entities tree.

Enums  
---  
`TREE_TYPE_UNSPECIFIED` | Tree type unspecified.  
`SOURCE` | Tree of entities loaded from a source database.  
`DRAFT` | Tree of entities converted from the source tree using the mapping rules.  
`DESTINATION` | Tree of entities observed on the destination database.  
  
## EntityMapping

Details of the mappings of a database entity.

JSON representation  
---  
      
    
    {
      "sourceEntity": string,
      "draftEntity": string,
      "sourceType": enum ([DatabaseEntityType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#DatabaseEntityType)),
      "draftType": enum ([DatabaseEntityType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#DatabaseEntityType)),
      "mappingLog": [
        {
          object ([EntityMappingLogEntry](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#EntityMappingLogEntry))
        }
      ]
    }  
  
Fields  
---  
`sourceEntity` |  `string` Source entity full name. The source entity can also be a column, index or constraint using the same naming notation schema.table.column.  
`draftEntity` |  `string` Target entity full name. The draft entity can also include a column, index or constraint using the same naming notation schema.table.column.  
`sourceType` |  `enum (`[DatabaseEntityType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#DatabaseEntityType)`)` Type of source entity.  
`draftType` |  `enum (`[DatabaseEntityType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#DatabaseEntityType)`)` Type of draft entity.  
`mappingLog[]` |  `object (`[EntityMappingLogEntry](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#EntityMappingLogEntry)`)` Entity mapping log entries. Multiple rules can be effective and contribute changes to a converted entity, such as a rule can handle the entity name, another rule can handle an entity type. In addition, rules which did not change the entity are also logged along with the reason preventing them to do so.  
  
## EntityMappingLogEntry

A single record of a rule which was used for a mapping.

JSON representation  
---  
      
    
    {
      "ruleId": string,
      "ruleRevisionId": string,
      "mappingComment": string
    }  
  
Fields  
---  
`ruleId` |  `string` Which rule caused this log entry.  
`ruleRevisionId` |  `string` Rule revision ID.  
`mappingComment` |  `string` Comment.  
  
## EntityDdl

A single DDL statement for a specific entity

JSON representation  
---  
      
    
    {
      "ddlType": string,
      "entity": string,
      "ddl": string,
      "entityType": enum ([DatabaseEntityType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#DatabaseEntityType)),
      "ddlKind": enum ([DdlKind](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#DdlKind)),
      "editedDdlKind": enum ([DdlKind](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#DdlKind)),
      "issueId": [
        string
      ]
    }  
  
Fields  
---  
`ddlType` |  `string` Type of DDL (Create, Alter).  
`entity` |  `string` The name of the database entity the ddl refers to.  
`ddl` |  `string` The actual ddl code.  
`entityType` |  `enum (`[DatabaseEntityType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#DatabaseEntityType)`)` The entity type (if the DDL is for a sub entity).  
`ddlKind` |  `enum (`[DdlKind](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#DdlKind)`)` The DDL Kind selected for apply, or UNSPECIFIED if the entity wasn't converted yet.  
`editedDdlKind` |  `enum (`[DdlKind](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#DdlKind)`)` If ddlKind is USER_EDIT, this holds the DDL kind of the original content - DETERMINISTIC or AI. Otherwise, this is DDL_KIND_UNSPECIFIED.  
`issueId[]` |  `string` EntityIssues found for this ddl.  
  
## DdlKind

The type of DDL

Enums  
---  
`DDL_KIND_UNSPECIFIED` | The kind of the DDL is unknown.  
`SOURCE` | DDL of the source entity  
`DETERMINISTIC` | Deterministic converted DDL  
`AI` | Gemini AI converted DDL  
`USER_EDIT` | User edited DDL  
  
## EntityIssue

Issue related to the entity.

JSON representation  
---  
      
    
    {
      "id": string,
      "type": enum ([IssueType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#IssueType)),
      "severity": enum ([IssueSeverity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#IssueSeverity)),
      "message": string,
      "code": string,
      "entityType": enum ([DatabaseEntityType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#DatabaseEntityType)),
      "ddl": string,
      "position": {
        object ([Position](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#Position))
      }
    }  
  
Fields  
---  
`id` |  `string` Unique Issue ID.  
`type` |  `enum (`[IssueType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#IssueType)`)` The type of the issue.  
`severity` |  `enum (`[IssueSeverity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#IssueSeverity)`)` Severity of the issue  
`message` |  `string` Issue detailed message  
`code` |  `string` Error/Warning code  
`entityType` |  `enum (`[DatabaseEntityType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#DatabaseEntityType)`)` The entity type (if the DDL is for a sub entity).  
`ddl` |  `string` The ddl which caused the issue, if relevant.  
`position` |  `object (`[Position](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#Position)`)` The position of the issue found, if relevant.  
  
## IssueType

Type of issue.

Enums  
---  
`ISSUE_TYPE_UNSPECIFIED` | Unspecified issue type.  
`ISSUE_TYPE_DDL` | Issue originated from the DDL  
`ISSUE_TYPE_APPLY` | Issue originated during the apply process  
`ISSUE_TYPE_CONVERT` | Issue originated during the convert process  
`ISSUE_TYPE_PULL_SCHEMA` | Issue originated during the pull schema process  
  
## IssueSeverity

Severity of issue.

Enums  
---  
`ISSUE_SEVERITY_UNSPECIFIED` | Unspecified issue severity  
`ISSUE_SEVERITY_INFO` | Info  
`ISSUE_SEVERITY_WARNING` | Warning  
`ISSUE_SEVERITY_ERROR` | Error  
  
## Position

Issue position.

JSON representation  
---  
      
    
    {
      "line": integer,
      "column": integer,
      "offset": integer,
      "length": integer
    }  
  
Fields  
---  
`line` |  `integer` Issue line number  
`column` |  `integer` Issue column number  
`offset` |  `integer` Issue offset  
`length` |  `integer` Issue length  
  
## DatabaseInstanceEntity

DatabaseInstance acts as a parent entity to other database entities.

JSON representation  
---  
      
    
    {
      "customFeatures": {
        object
      }
    }  
  
Fields  
---  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom engine specific features.  
  
## SchemaEntity

Schema typically has no parent entity, but can have a parent entity DatabaseInstance (for database engines which support it). For some database engines, the terms schema and user can be used interchangeably when they refer to a namespace or a collection of other database entities. Can store additional information which is schema specific.

JSON representation  
---  
      
    
    {
      "customFeatures": {
        object
      }
    }  
  
Fields  
---  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom engine specific features.  
  
## TableEntity

Table's parent is a schema.

JSON representation  
---  
      
    
    {
      "columns": [
        {
          object ([ColumnEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#ColumnEntity))
        }
      ],
      "constraints": [
        {
          object ([ConstraintEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#ConstraintEntity))
        }
      ],
      "indices": [
        {
          object ([IndexEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#IndexEntity))
        }
      ],
      "triggers": [
        {
          object ([TriggerEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#TriggerEntity))
        }
      ],
      "customFeatures": {
        object
      },
      "comment": string
    }  
  
Fields  
---  
`columns[]` |  `object (`[ColumnEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#ColumnEntity)`)` Table columns.  
`constraints[]` |  `object (`[ConstraintEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#ConstraintEntity)`)` Table constraints.  
`indices[]` |  `object (`[IndexEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#IndexEntity)`)` Table indices.  
`triggers[]` |  `object (`[TriggerEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#TriggerEntity)`)` Table triggers.  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom engine specific features.  
`comment` |  `string` Comment associated with the table.  
  
## ColumnEntity

Column is not used as an independent entity, it is retrieved as part of a Table entity.

JSON representation  
---  
      
    
    {
      "name": string,
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
      "comment": string,
      "ordinalPosition": integer,
      "defaultValue": string,
      "computed": boolean
    }  
  
Fields  
---  
`name` |  `string` Column name.  
`dataType` |  `string` Column data type.  
`charset` |  `string` Charset override - instead of table level charset.  
`collation` |  `string` Collation override - instead of table level collation.  
`length` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Column length - e.g. varchar (50).  
`precision` |  `integer` Column precision - when relevant.  
`scale` |  `integer` Column scale - when relevant.  
`fractionalSecondsPrecision` |  `integer` Column fractional second precision - used for timestamp based datatypes.  
`array` |  `boolean` Is the column of array type.  
`arrayLength` |  `integer` If the column is array, of which length.  
`nullable` |  `boolean` Is the column nullable.  
`autoGenerated` |  `boolean` Is the column auto-generated/identity.  
`udt` |  `boolean` Is the column a UDT.  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom engine specific features.  
`setValues[]` |  `string` Specifies the list of values allowed in the column. Only used for set data type.  
`comment` |  `string` Comment associated with the column.  
`ordinalPosition` |  `integer` Column order in the table.  
`defaultValue` |  `string` Default value of the column.  
`computed` |  `boolean` Is the column a computed column.  
  
## ConstraintEntity

Constraint is not used as an independent entity, it is retrieved as part of another entity such as Table or View.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string,
      "tableColumns": [
        string
      ],
      "customFeatures": {
        object
      },
      "referenceColumns": [
        string
      ],
      "referenceTable": string,
      "tableName": string
    }  
  
Fields  
---  
`name` |  `string` The name of the table constraint.  
`type` |  `string` Type of constraint, for example unique, primary key, foreign key (currently only primary key is supported).  
`tableColumns[]` |  `string` Table columns used as part of the Constraint, for example primary key constraint should list the columns which constitutes the key.  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom engine specific features.  
`referenceColumns[]` |  `string` Reference columns which may be associated with the constraint. For example, if the constraint is a FOREIGN_KEY, this represents the list of full names of referenced columns by the foreign key.  
`referenceTable` |  `string` Reference table which may be associated with the constraint. For example, if the constraint is a FOREIGN_KEY, this represents the list of full name of the referenced table by the foreign key.  
`tableName` |  `string` Table which is associated with the constraint. In case the constraint is defined on a table, this field is left empty as this information is stored in parentName. However, if constraint is defined on a view, this field stores the table name on which the view is defined.  
  
## IndexEntity

Index is not used as an independent entity, it is retrieved as part of a Table entity.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string,
      "tableColumns": [
        string
      ],
      "tableColumnsDescending": [
        boolean
      ],
      "unique": boolean,
      "customFeatures": {
        object
      }
    }  
  
Fields  
---  
`name` |  `string` The name of the index.  
`type` |  `string` Type of index, for example B-TREE.  
`tableColumns[]` |  `string` Table columns used as part of the Index, for example B-TREE index should list the columns which constitutes the index.  
`tableColumnsDescending[]` |  `boolean` For each table_column, mark whether it's sorting order is ascending (false) or descending (true). If no value is defined, assume all columns are sorted in ascending order. Otherwise, the number of items must match that of tableColumns with each value specifying the direction of the matched column by its index.  
`unique` |  `boolean` Boolean value indicating whether the index is unique.  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom engine specific features.  
  
## TriggerEntity

Trigger is not used as an independent entity, it is retrieved as part of a Table entity.

JSON representation  
---  
      
    
    {
      "name": string,
      "triggeringEvents": [
        string
      ],
      "triggerType": string,
      "sqlCode": string,
      "customFeatures": {
        object
      }
    }  
  
Fields  
---  
`name` |  `string` The name of the trigger.  
`triggeringEvents[]` |  `string` The DML, DDL, or database events that fire the trigger, for example INSERT, UPDATE.  
`triggerType` |  `string` Indicates when the trigger fires, for example BEFORE STATEMENT, AFTER EACH ROW.  
`sqlCode` |  `string` The SQL code which creates the trigger.  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom engine specific features.  
  
## ViewEntity

View's parent is a schema.

JSON representation  
---  
      
    
    {
      "sqlCode": string,
      "customFeatures": {
        object
      },
      "constraints": [
        {
          object ([ConstraintEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#ConstraintEntity))
        }
      ]
    }  
  
Fields  
---  
`sqlCode` |  `string` The SQL code which creates the view.  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom engine specific features.  
`constraints[]` |  `object (`[ConstraintEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#ConstraintEntity)`)` View constraints.  
  
## SequenceEntity

Sequence's parent is a schema.

JSON representation  
---  
      
    
    {
      "increment": string,
      "startValue": string,
      "maxValue": string,
      "minValue": string,
      "cycle": boolean,
      "cache": string,
      "customFeatures": {
        object
      }
    }  
  
Fields  
---  
`increment` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Increment value for the sequence.  
`startValue` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Start number for the sequence represented as bytes to accommodate large. numbersA base64-encoded string.  
`maxValue` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Maximum number for the sequence represented as bytes to accommodate large. numbersA base64-encoded string.  
`minValue` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Minimum number for the sequence represented as bytes to accommodate large. numbersA base64-encoded string.  
`cycle` |  `boolean` Indicates whether the sequence value should cycle through.  
`cache` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Indicates number of entries to cache / precreate.  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom engine specific features.  
  
## StoredProcedureEntity

Stored procedure's parent is a schema.

JSON representation  
---  
      
    
    {
      "sqlCode": string,
      "customFeatures": {
        object
      }
    }  
  
Fields  
---  
`sqlCode` |  `string` The SQL code which creates the stored procedure.  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom engine specific features.  
  
## FunctionEntity

Function's parent is a schema.

JSON representation  
---  
      
    
    {
      "sqlCode": string,
      "customFeatures": {
        object
      }
    }  
  
Fields  
---  
`sqlCode` |  `string` The SQL code which creates the function.  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom engine specific features.  
  
## SynonymEntity

Synonym's parent is a schema.

JSON representation  
---  
      
    
    {
      "sourceEntity": string,
      "sourceType": enum ([DatabaseEntityType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#DatabaseEntityType)),
      "customFeatures": {
        object
      }
    }  
  
Fields  
---  
`sourceEntity` |  `string` The name of the entity for which the synonym is being created (the source).  
`sourceType` |  `enum (`[DatabaseEntityType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules#DatabaseEntityType)`)` The type of the entity for which the synonym is being created (usually a table or a sequence).  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom engine specific features.  
  
## PackageEntity

Package's parent is a schema.

JSON representation  
---  
      
    
    {
      "packageSqlCode": string,
      "packageBody": string,
      "customFeatures": {
        object
      }
    }  
  
Fields  
---  
`packageSqlCode` |  `string` The SQL code which creates the package.  
`packageBody` |  `string` The SQL code which creates the package body. If the package specification has cursors or subprograms, then the package body is mandatory.  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom engine specific features.  
  
## UDTEntity

UDT's parent is a schema.

JSON representation  
---  
      
    
    {
      "udtSqlCode": string,
      "udtBody": string,
      "customFeatures": {
        object
      }
    }  
  
Fields  
---  
`udtSqlCode` |  `string` The SQL code which creates the udt.  
`udtBody` |  `string` The SQL code which creates the udt body.  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom engine specific features.  
  
## MaterializedViewEntity

MaterializedView's parent is a schema.

JSON representation  
---  
      
    
    {
      "sqlCode": string,
      "indices": [
        {
          object ([IndexEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#IndexEntity))
        }
      ],
      "customFeatures": {
        object
      }
    }  
  
Fields  
---  
`sqlCode` |  `string` The SQL code which creates the view.  
`indices[]` |  `object (`[IndexEntity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities#IndexEntity)`)` View indices.  
`customFeatures` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom engine specific features.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
