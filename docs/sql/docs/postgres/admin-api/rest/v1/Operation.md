---
url: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation/
title: Operation \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:38:24.721749+00:00
---

# Operation  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)



Send feedback 

#  Operation Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SqlOperationStatus
  * OperationErrors
    * JSON representation
  * OperationError
    * JSON representation
  * SqlOperationType
  * ImportContext
    * JSON representation
      * JSON representation
  * SqlFileType
  * ExportContext
    * JSON representation
      * JSON representation
  * BackupContext
    * JSON representation



An Operation resource. For successful operations that return an Operation resource, only the fields relevant to the operation are populated in the resource.

JSON representation  
---  
      
    
    {
      "kind": string,
      "targetLink": string,
      "status": enum ([SqlOperationStatus](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#SqlOperationStatus)),
      "user": string,
      "insertTime": string,
      "startTime": string,
      "endTime": string,
      "error": {
        object ([OperationErrors](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#OperationErrors))
      },
      "operationType": enum ([SqlOperationType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#SqlOperationType)),
      "importContext": {
        object ([ImportContext](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#ImportContext))
      },
      "exportContext": {
        object ([ExportContext](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#ExportContext))
      },
      "backupContext": {
        object ([BackupContext](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#BackupContext))
      },
      "name": string,
      "targetId": string,
      "selfLink": string,
      "targetProject": string
    }  
  
Fields  
---  
`kind` |  `string` This is always **sql#operation**.  
`targetLink` |  `string`  
`status` |  `enum (`[SqlOperationStatus](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#SqlOperationStatus)`)` The status of an operation. Valid values are:   
**PENDING**   
**RUNNING**   
**DONE**   
**SQL_OPERATION_STATUS_UNSPECIFIED**  
`user` |  `string` The email address of the user who initiated this operation.  
`insertTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The time this operation was enqueued in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example **2012-11-15T16:19:00.094Z**.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`startTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The time this operation actually started in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example **2012-11-15T16:19:00.094Z**.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`endTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The time this operation finished in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example **2012-11-15T16:19:00.094Z**.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`error` |  `object (`[OperationErrors](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#OperationErrors)`)` If errors occurred during processing of this operation, this field will be populated.  
`operationType` |  `enum (`[SqlOperationType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#SqlOperationType)`)` The type of the operation. Valid values are:   
**CREATE**   
**DELETE**   
**UPDATE**   
**RESTART**   
**IMPORT**   
**EXPORT**   
**BACKUP_VOLUME**   
**RESTORE_VOLUME**   
**CREATE_USER**   
**DELETE_USER**   
**CREATE_DATABASE**   
**DELETE_DATABASE**  
`importContext` |  `object (`[ImportContext](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#ImportContext)`)` The context for import operation, if applicable.  
`exportContext` |  `object (`[ExportContext](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#ExportContext)`)` The context for export operation, if applicable.  
`backupContext` |  `object (`[BackupContext](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#BackupContext)`)` The context for backup operation, if applicable.  
`name` |  `string` An identifier that uniquely identifies the operation. You can use this identifier to retrieve the Operations resource that has information about the operation.  
`targetId` |  `string` Name of the database instance related to this operation.  
`selfLink` |  `string` The URI of this resource.  
`targetProject` |  `string` The project ID of the target instance related to this operation.  
  
## SqlOperationStatus

The status of an operation.

Enums  
---  
`SQL_OPERATION_STATUS_UNSPECIFIED` | The state of the operation is unknown.  
`PENDING` | The operation has been queued, but has not started yet.  
`RUNNING` | The operation is running.  
`DONE` | The operation completed.  
  
## OperationErrors

Database instance operation errors list wrapper.

JSON representation  
---  
      
    
    {
      "kind": string,
      "errors": [
        {
          object ([OperationError](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#OperationError))
        }
      ]
    }  
  
Fields  
---  
`kind` |  `string` This is always **sql#operationErrors**.  
`errors[]` |  `object (`[OperationError](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#OperationError)`)` The list of errors encountered while processing this operation.  
  
## OperationError

Database instance operation error.

JSON representation  
---  
      
    
    {
      "kind": string,
      "code": string,
      "message": string
    }  
  
Fields  
---  
`kind` |  `string` This is always **sql#operationError**.  
`code` |  `string` Identifies the specific error that occurred.  
`message` |  `string` Additional information about the error encountered.  
  
## SqlOperationType

The type of Cloud SQL operation.

Enums  
---  
`SQL_OPERATION_TYPE_UNSPECIFIED` | Unknown operation type.  
`IMPORT` | Imports data into a Cloud SQL instance.  
`EXPORT` | Exports data from a Cloud SQL instance to a Cloud Storage bucket.  
`CREATE` | Creates a new Cloud SQL instance.  
`UPDATE` | Updates the settings of a Cloud SQL instance.  
`DELETE` | Deletes a Cloud SQL instance.  
`RESTART` | Restarts the Cloud SQL instance.  
`BACKUP` | This item is deprecated!  
`SNAPSHOT` | This item is deprecated!  
`BACKUP_VOLUME` | Performs instance backup.  
`DELETE_VOLUME` | Deletes an instance backup.  
`RESTORE_VOLUME` | Restores an instance backup.  
`INJECT_USER` | Injects a privileged user in mysql for MOB instances.  
`CLONE` | Clones a Cloud SQL instance.  
`STOP_REPLICA` | Stops replication on a Cloud SQL read replica instance.  
`START_REPLICA` | Starts replication on a Cloud SQL read replica instance.  
`PROMOTE_REPLICA` | Promotes a Cloud SQL replica instance.  
`CREATE_REPLICA` | Creates a Cloud SQL replica instance.  
`CREATE_USER` | Creates a new user in a Cloud SQL instance.  
`DELETE_USER` | Deletes a user from a Cloud SQL instance.  
`UPDATE_USER` | Updates an existing user in a Cloud SQL instance.  
`CREATE_DATABASE` | Creates a database in the Cloud SQL instance.  
`DELETE_DATABASE` | Deletes a database in the Cloud SQL instance.  
`UPDATE_DATABASE` | Updates a database in the Cloud SQL instance.  
`FAILOVER` | Performs failover of an HA-enabled Cloud SQL failover replica.  
`DELETE_BACKUP` | Deletes the backup taken by a backup run.  
`RECREATE_REPLICA` |   
`TRUNCATE_LOG` | Truncates a general or slow log table in MySQL.  
`DEMOTE_MASTER` | Demotes the stand-alone instance to be a Cloud SQL read replica for an external database server.  
`MAINTENANCE` | Indicates that the instance is currently in maintenance. Maintenance typically causes the instance to be unavailable for 1-3 minutes.  
`ENABLE_PRIVATE_IP` | This field is deprecated, and will be removed in future version of API.This item is deprecated!  
`DEFER_MAINTENANCE` | This item is deprecated!  
`CREATE_CLONE` | Creates clone instance.This item is deprecated!  
`RESCHEDULE_MAINTENANCE` | Reschedule maintenance to another time.  
`START_EXTERNAL_SYNC` | Starts external sync of a Cloud SQL EM replica to an external primary instance.  
  
## ImportContext

Database instance import context.

JSON representation  
---  
      
    
    {
      "uri": string,
      "database": string,
      "kind": string,
      "fileType": enum ([SqlFileType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#SqlFileType)),
      "csvImportOptions": {
        "table": string,
        "columns": [
          string
        ]
      },
      "importUser": string,
      "bakImportOptions": {
        "encryptionOptions": {
          "certPath": string,
          "pvkPath": string,
          "pvkPassword": string
        }
      }
    }  
  
Fields  
---  
`uri` |  `string` Path to the import file in Cloud Storage, in the form **<gs://bucketName/fileName**>. Compressed gzip files (.gz) are supported when **fileType** is **SQL**. The instance must have write permissions to the bucket and read access to the file.  
`database` |  `string` The target database for the import. If **fileType** is **SQL** , this field is required only if the import file does not specify a database, and is overridden by any database specification in the import file. If **fileType** is **CSV** , one database must be specified.  
`kind` |  `string` This is always **sql#importContext**.  
`fileType` |  `enum (`[SqlFileType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#SqlFileType)`)` The file type for the specified uri.   
**SQL**: The file contains SQL statements.   
**CSV**: The file contains CSV data.  
`csvImportOptions` |  `object` Options for importing data as CSV.  
`csvImportOptions.table` |  `string` The table to which CSV data is imported.  
`csvImportOptions.columns[]` |  `string` The columns to which CSV data is imported. If not specified, all columns of the database table are loaded with CSV data.  
`importUser` |  `string` The PostgreSQL user for this import operation. PostgreSQL instances only.  
`bakImportOptions` |  `object` instances.import parameters specific to SQL Server .BAK files  
`bakImportOptions.encryptionOptions` |  `object`  
`bakImportOptions.encryptionOptions.certPath` |  `string` Path to the Certificate (.cer) in Cloud Storage, in the form **<gs://bucketName/fileName**>. The instance must have write permissions to the bucket and read access to the file.  
`bakImportOptions.encryptionOptions.pvkPath` |  `string` Path to the Certificate Private Key (.pvk) in Cloud Storage, in the form **<gs://bucketName/fileName**>. The instance must have write permissions to the bucket and read access to the file.  
`bakImportOptions.encryptionOptions.pvkPassword` |  `string` Password that encrypts the private key  
  
## SqlFileType

Enums  
---  
`SQL_FILE_TYPE_UNSPECIFIED` | Unknown file type.  
`SQL` | File containing SQL statements.  
`CSV` | File in CSV format.  
`BAK` |   
  
## ExportContext

Database instance export context.

JSON representation  
---  
      
    
    {
      "uri": string,
      "databases": [
        string
      ],
      "kind": string,
      "sqlExportOptions": {
        "tables": [
          string
        ],
        "schemaOnly": boolean,
        "mysqlExportOptions": {
          "masterData": integer
        }
      },
      "csvExportOptions": {
        "selectQuery": string
      },
      "fileType": enum ([SqlFileType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#SqlFileType)),
      "offload": boolean
    }  
  
Fields  
---  
`uri` |  `string` The path to the file in Google Cloud Storage where the export will be stored. The URI is in the form **<gs://bucketName/fileName**>. If the file already exists, the request succeeds, but the operation fails.   
If **fileType** is **SQL** and the filename ends with .gz, the contents are compressed.  
`databases[]` |  `string` Databases to be exported.   
**MySQL instances:** If **fileType** is **SQL** and no database is specified, all databases are exported, except for the **mysql** system database. If **fileType** is **CSV** , you can specify one database, either by using this property or by using the **csvExportOptions.selectQuery** property, which takes precedence over this property.   
**PostgreSQL instances:** You must specify one database to be exported. If **fileType** is **CSV** , this database must match the one specified in the **csvExportOptions.selectQuery** property.   
**SQL Server instances:** You must specify one database to be exported, and the **fileType** must be **BAK**.  
`kind` |  `string` This is always **sql#exportContext**.  
`sqlExportOptions` |  `object` Options for exporting data as SQL statements.  
`sqlExportOptions.tables[]` |  `string` Tables to export, or that were exported, from the specified database. If you specify tables, specify one and only one database. For PostgreSQL instances, you can specify only one table.  
`sqlExportOptions.schemaOnly` |  `boolean` instances.export only schemas.  
`sqlExportOptions.mysqlExportOptions` |  `object`  
`sqlExportOptions.mysqlExportOptions.masterData` |  `integer` Option to include SQL statement required to set up replication.   
If set to **1** , the dump file includes a CHANGE MASTER TO statement with the binary log coordinates, and --set-gtid-purged is set to ON.   
If set to **2** , the CHANGE MASTER TO statement is written as a SQL comment and has no effect.   
If set to any value other than **1** , --set-gtid-purged is set to OFF.  
`csvExportOptions` |  `object` Options for exporting data as CSV. **MySQL** and **PostgreSQL** instances only.  
`csvExportOptions.selectQuery` |  `string` The select query used to extract the data.  
`fileType` |  `enum (`[SqlFileType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/Operation#SqlFileType)`)` The file type for the specified uri.   
**SQL**: The file contains SQL statements.   
**CSV**: The file contains CSV data.   
**BAK**: The file contains backup data for a SQL Server instance.  
`offload` |  `boolean` Option for export offload.  
  
## BackupContext

Backup context.

JSON representation  
---  
      
    
    {
      "backupId": string,
      "kind": string
    }  
  
Fields  
---  
`backupId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The identifier of the backup.  
`kind` |  `string` This is always **sql#backupContext**.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
