---
url: https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails/
title: DatabaseDetails \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:18.801806+00:00
---

# DatabaseDetails  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Reference ](https://docs.cloud.google.com/migration-center/docs/api)



Send feedback 

#  DatabaseDetails Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ParentDatabaseDeployment
    * JSON representation
  * DatabaseSchema
    * JSON representation
  * DatabaseObjects
    * JSON representation
  * Category
  * SqlServerSchemaDetails
    * JSON representation
  * MySqlSchemaDetails
    * JSON representation
  * MySqlStorageEngineDetails
    * JSON representation
  * Engine
  * PostgreSqlSchemaDetails
    * JSON representation
  * PostgreSqlExtension
    * JSON representation



Details of a logical database.

JSON representation  
---  
      
    
    {
      "databaseName": string,
      "parentDatabaseDeployment": {
        object ([ParentDatabaseDeployment](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#ParentDatabaseDeployment))
      },
      "allocatedStorageBytes": string,
      "schemas": [
        {
          object ([DatabaseSchema](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#DatabaseSchema))
        }
      ]
    }  
  
Fields  
---  
`databaseName` |  `string` The name of the database.  
`parentDatabaseDeployment` |  `object (`[ParentDatabaseDeployment](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#ParentDatabaseDeployment)`)` The parent database deployment that contains the logical database.  
`allocatedStorageBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The allocated storage for the database in bytes.  
`schemas[]` |  `object (`[DatabaseSchema](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#DatabaseSchema)`)` The database schemas.  
  
## ParentDatabaseDeployment

The identifiers of the parent database deployment.

JSON representation  
---  
      
    
    {
      "generatedId": string,
      "manualUniqueId": string
    }  
  
Fields  
---  
`generatedId` |  `string` The parent database deployment generated ID.  
`manualUniqueId` |  `string` The parent database deployment optional manual unique ID set by the user.  
  
## DatabaseSchema

Details of a database schema.

JSON representation  
---  
      
    
    {
      "schemaName": string,
      "tablesSizeBytes": string,
      "objects": [
        {
          object ([DatabaseObjects](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#DatabaseObjects))
        }
      ],
    
      // Union field engine_details can be only one of the following:
      "sqlServer": {
        object ([SqlServerSchemaDetails](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#SqlServerSchemaDetails))
      },
      "mysql": {
        object ([MySqlSchemaDetails](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#MySqlSchemaDetails))
      },
      "postgresql": {
        object ([PostgreSqlSchemaDetails](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#PostgreSqlSchemaDetails))
      }
      // End of list of possible types for union field engine_details.
    }  
  
Fields  
---  
`schemaName` |  `string` The name of the schema.  
`tablesSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total size of tables in bytes.  
`objects[]` |  `object (`[DatabaseObjects](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#DatabaseObjects)`)` List of details of objects by category.  
Union field `engine_details`. Engine-specific details. `engine_details` can be only one of the following:  
`sqlServer` |  `object (`[SqlServerSchemaDetails](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#SqlServerSchemaDetails)`)` Details of a SqlServer schema.  
`mysql` |  `object (`[MySqlSchemaDetails](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#MySqlSchemaDetails)`)` Details of a Mysql schema.  
`postgresql` |  `object (`[PostgreSqlSchemaDetails](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#PostgreSqlSchemaDetails)`)` Details of a PostgreSql schema.  
  
## DatabaseObjects

Details of a group of database objects.

JSON representation  
---  
      
    
    {
      "category": enum ([Category](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#Category)),
      "count": string
    }  
  
Fields  
---  
`category` |  `enum (`[Category](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#Category)`)` The category of the objects.  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of objects.  
  
## Category

The category of a database object.

Enums  
---  
`CATEGORY_UNSPECIFIED` | Unspecified type.  
`TABLE` | Table.  
`INDEX` | Index.  
`CONSTRAINTS` | Constraints.  
`VIEWS` | Views.  
`SOURCE_CODE` | Source code, e.g. procedures.  
`OTHER` | Uncategorized objects.  
  
## SqlServerSchemaDetails

Specific details for a SqlServer database.

JSON representation  
---  
      
    
    {
      "clrObjectCount": integer
    }  
  
Fields  
---  
`clrObjectCount` |  `integer` Optional. SqlServer number of CLR objects.  
  
## MySqlSchemaDetails

Specific details for a Mysql database.

JSON representation  
---  
      
    
    {
      "storageEngines": [
        {
          object ([MySqlStorageEngineDetails](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#MySqlStorageEngineDetails))
        }
      ]
    }  
  
Fields  
---  
`storageEngines[]` |  `object (`[MySqlStorageEngineDetails](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#MySqlStorageEngineDetails)`)` Optional. Mysql storage engine tables.  
  
## MySqlStorageEngineDetails

Mysql storage engine tables.

JSON representation  
---  
      
    
    {
      "engine": enum ([Engine](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#Engine)),
      "tableCount": integer,
      "encryptedTableCount": integer
    }  
  
Fields  
---  
`engine` |  `enum (`[Engine](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#Engine)`)` Required. The storage engine.  
`tableCount` |  `integer` Optional. The number of tables.  
`encryptedTableCount` |  `integer` Optional. The number of encrypted tables.  
  
## Engine

Storage engines.

Enums  
---  
`ENGINE_UNSPECIFIED` | Unspecified storage engine.  
`INNODB` | InnoDB.  
`MYISAM` | MyISAM.  
`MEMORY` | Memory.  
`CSV` | CSV.  
`ARCHIVE` | Archive.  
`BLACKHOLE` | Blackhole.  
`NDB` | NDB.  
`MERGE` | Merge.  
`FEDERATED` | Federated.  
`EXAMPLE` | Example.  
`OTHER` | Other.  
  
## PostgreSqlSchemaDetails

Specific details for a PostgreSql schema.

JSON representation  
---  
      
    
    {
      "foreignTablesCount": integer,
      "postgresqlExtensions": [
        {
          object ([PostgreSqlExtension](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#PostgreSqlExtension))
        }
      ]
    }  
  
Fields  
---  
`foreignTablesCount` |  `integer` Optional. PostgreSql foreign tables.  
`postgresqlExtensions[]` |  `object (`[PostgreSqlExtension](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1alpha1/DatabaseDetails#PostgreSqlExtension)`)` Optional. PostgreSql extensions.  
  
## PostgreSqlExtension

PostgreSql extension.

JSON representation  
---  
      
    
    {
      "extension": string,
      "version": string
    }  
  
Fields  
---  
`extension` |  `string` Required. The extension name.  
`version` |  `string` Required. The extension version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-17 UTC."],[],[]] 
