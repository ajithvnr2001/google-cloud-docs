---
url: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations/
title: REST Resource: operations \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:34:13.461737+00:00
---

# REST Resource: operations  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/sqlserver/apis)



Send feedback 

#  REST Resource: operations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Operation
    * JSON representation
  * SqlOperationStatus
  * OperationErrors
    * JSON representation
  * ApiWarning
    * JSON representation
  * SqlApiWarningCode
  * SqlOperationType
  * ImportContext
    * JSON representation
      * JSON representation
      * JSON representation
  * SqlFileType
  * ExportContext
    * JSON representation
      * JSON representation
      * JSON representation
  * BackupContext
    * JSON representation
  * PreCheckMajorVersionUpgradeContext
    * JSON representation
  * PreCheckResponse
    * JSON representation
  * MessageType
  * AcquireSsrsLeaseContext
    * JSON representation
  * SqlSubOperationType
    * JSON representation
  * SqlMaintenanceType
  * Methods



## Resource: Operation

An Operation resource. For successful operations that return an Operation resource, only the fields relevant to the operation are populated in the resource.

JSON representation  
---  
      
    
    {
      "kind": string,
      "targetLink": string,
      "status": enum ([SqlOperationStatus](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#SqlOperationStatus)),
      "user": string,
      "insertTime": string,
      "startTime": string,
      "endTime": string,
      "error": {
        object ([OperationErrors](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#OperationErrors))
      },
      "apiWarning": {
        object ([ApiWarning](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#ApiWarning))
      },
      "operationType": enum ([SqlOperationType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#SqlOperationType)),
      "importContext": {
        object ([ImportContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#ImportContext))
      },
      "exportContext": {
        object ([ExportContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#ExportContext))
      },
      "backupContext": {
        object ([BackupContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#BackupContext))
      },
      "preCheckMajorVersionUpgradeContext": {
        object ([PreCheckMajorVersionUpgradeContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#PreCheckMajorVersionUpgradeContext))
      },
      "name": string,
      "targetId": string,
      "selfLink": string,
      "targetProject": string,
      "acquireSsrsLeaseContext": {
        object ([AcquireSsrsLeaseContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#AcquireSsrsLeaseContext))
      },
      "subOperationType": {
        object ([SqlSubOperationType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#SqlSubOperationType))
      }
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#operation`.  
`targetLink` |  `string`  
`status` |  `enum (`[SqlOperationStatus](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#SqlOperationStatus)`)` The status of an operation.  
`user` |  `string` The email address of the user who initiated this operation.  
`insertTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time this operation was enqueued in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time this operation actually started in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time this operation finished in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`error` |  `object (`[OperationErrors](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#OperationErrors)`)` If errors occurred during processing of this operation, this field will be populated.  
`apiWarning` |  `object (`[ApiWarning](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#ApiWarning)`)` An Admin API warning message.  
`operationType` |  `enum (`[SqlOperationType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#SqlOperationType)`)` The type of the operation. Valid values are: * `CREATE` * `DELETE` * `UPDATE` * `RESTART` * `IMPORT` * `EXPORT` * `BACKUP_VOLUME` * `RESTORE_VOLUME` * `CREATE_USER` * `DELETE_USER` * `CREATE_DATABASE` * `DELETE_DATABASE`  
`importContext` |  `object (`[ImportContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#ImportContext)`)` The context for import operation, if applicable.  
`exportContext` |  `object (`[ExportContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#ExportContext)`)` The context for export operation, if applicable.  
`backupContext` |  `object (`[BackupContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#BackupContext)`)` The context for backup operation, if applicable.  
`preCheckMajorVersionUpgradeContext` |  `object (`[PreCheckMajorVersionUpgradeContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#PreCheckMajorVersionUpgradeContext)`)` The context for pre-check major version upgrade operation, if applicable. This field is only populated when the operationType is PRE_CHECK_MAJOR_VERSION_UPGRADE. The PreCheckMajorVersionUpgradeContext message itself contains the details for that pre-check, such as the target database version for the upgrade and the results of the check (including any warnings or errors found).  
`name` |  `string` An identifier that uniquely identifies the operation. You can use this identifier to retrieve the Operations resource that has information about the operation.  
`targetId` |  `string` Name of the resource on which this operation runs.  
`selfLink` |  `string` The URI of this resource.  
`targetProject` |  `string` The project ID of the target instance related to this operation.  
`acquireSsrsLeaseContext` |  `object (`[AcquireSsrsLeaseContext](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#AcquireSsrsLeaseContext)`)` The context for acquire SSRS lease operation, if applicable.  
`subOperationType` |  `object (`[SqlSubOperationType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#SqlSubOperationType)`)` Optional. The sub operation based on the operation type.  
  
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
          object ([OperationError](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/OperationError))
        }
      ]
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#operationErrors`.  
`errors[]` |  `object (`[OperationError](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/OperationError)`)` The list of errors encountered while processing this operation.  
  
## ApiWarning

An Admin API warning message.

JSON representation  
---  
      
    
    {
      "code": enum ([SqlApiWarningCode](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#SqlApiWarningCode)),
      "message": string,
      "region": string
    }  
  
Fields  
---  
`code` |  `enum (`[SqlApiWarningCode](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#SqlApiWarningCode)`)` Code to uniquely identify the warning type.  
`message` |  `string` The warning message.  
`region` |  `string` The region name for REGION_UNREACHABLE warning.  
  
## SqlApiWarningCode

Enums  
---  
`SQL_API_WARNING_CODE_UNSPECIFIED` | An unknown or unset warning type from Cloud SQL API.  
`REGION_UNREACHABLE` | Warning when one or more regions are not reachable. The returned result set may be incomplete.  
`MAX_RESULTS_EXCEEDS_LIMIT` | Warning when user provided maxResults parameter exceeds the limit. The returned result set may be incomplete.  
`COMPROMISED_CREDENTIALS` | Warning when user tries to create/update a user with credentials that have previously been compromised by a public data breach.  
`INTERNAL_STATE_FAILURE` | Warning when the operation succeeds but some non-critical workflow state failed.  
  
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
`UPDATE_USER` | Updates an existing user in a Cloud SQL instance. If a user with the specified username doesn't exist, a new user is created.  
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
`LOG_CLEANUP` | Recovers logs from an instance's old data disk.  
`AUTO_RESTART` | Performs auto-restart of an HA-enabled Cloud SQL database for auto recovery.  
`REENCRYPT` | Re-encrypts CMEK instances with latest key version.  
`SWITCHOVER` | Switches the roles of the primary and replica pair. The target instance should be the replica.  
`UPDATE_BACKUP` | Update a backup.  
`ACQUIRE_SSRS_LEASE` | Acquire a lease for the setup of SQL Server Reporting Services (SSRS).  
`RELEASE_SSRS_LEASE` | Release a lease for the setup of SQL Server Reporting Services (SSRS).  
`RECONFIGURE_OLD_PRIMARY` | Reconfigures old primary after a promote replica operation. Effect of a promote operation to the old primary is executed in this operation, asynchronously from the promote replica operation executed to the replica.  
`CLUSTER_MAINTENANCE` | Indicates that the instance, its read replicas, and its cascading replicas are in maintenance. Maintenance typically gets initiated on groups of replicas first, followed by the primary instance. For each instance, maintenance typically causes the instance to be unavailable for 1-3 minutes.This item is deprecated!  
`SELF_SERVICE_MAINTENANCE` | Indicates that the instance (and any of its replicas) are currently in maintenance. This is initiated as a self-service request by using SSM. Maintenance typically causes the instance to be unavailable for 1-3 minutes.This item is deprecated!  
`SWITCHOVER_TO_REPLICA` | Switches a primary instance to a replica. This operation runs as part of a switchover operation to the original primary instance.  
`MAJOR_VERSION_UPGRADE` | Updates the major version of a Cloud SQL instance.  
`ADVANCED_BACKUP` | Deprecated: ADVANCED_BACKUP is deprecated. Use ENHANCED_BACKUP instead.This item is deprecated!  
`MANAGE_BACKUP` | Changes the BackupTier of a Cloud SQL instance.  
`ENHANCED_BACKUP` | Creates a backup for an Enhanced BackupTier Cloud SQL instance.  
`REPAIR_READ_POOL` | Repairs entire read pool or specified read pool nodes in the read pool.  
`CREATE_READ_POOL` | Creates a Cloud SQL read pool instance.  
`PRE_CHECK_MAJOR_VERSION_UPGRADE` | Pre-checks for major version upgrade.  
`SETUP_MIGRATION` | This operation type represents individual steps in a multi-step setup migration workflow: including configuration, replication, switchover/back, and data reseeding, as defined by operation's intent.  
`AGENT_SEND_MESSAGE` | Sends a message to a Cloud SQL agent.  
  
## ImportContext

Database instance import context.

JSON representation  
---  
      
    
    {
      "uri": string,
      "database": string,
      "kind": string,
      "fileType": enum ([SqlFileType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#SqlFileType)),
      "csvImportOptions": {
        "table": string,
        "columns": [
          string
        ],
        "escapeCharacter": string,
        "quoteCharacter": string,
        "fieldsTerminatedBy": string,
        "linesTerminatedBy": string
      },
      "importUser": string,
      "bakImportOptions": {
        "encryptionOptions": {
          "certPath": string,
          "pvkPath": string,
          "pvkPassword": string,
          "keepEncrypted": boolean
        },
        "striped": boolean,
        "noRecovery": boolean,
        "recoveryOnly": boolean,
        "bakType": enum ([BakType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/BakType)),
        "stopAt": string,
        "stopAtMark": string
      },
      "sqlImportOptions": {
        "threads": integer,
        "parallel": boolean,
        "postgresImportOptions": {
          "clean": boolean,
          "ifExists": boolean
        }
      },
      "tdeImportOptions": {
        "certificatePath": string,
        "privateKeyPath": string,
        "privateKeyPassword": string,
        "name": string
      }
    }  
  
Fields  
---  
`uri` |  `string` Path to the import file in Cloud Storage, in the form `gs://bucketName/fileName`. Compressed gzip files (.gz) are supported when `fileType` is `SQL`. The instance must have write permissions to the bucket and read access to the file.  
`database` |  `string` The target database for the import. If `fileType` is `SQL`, this field is required only if the import file does not specify a database, and is overridden by any database specification in the import file. For entire instance parallel import operations, the database is overridden by the database name stored in subdirectory name. If `fileType` is `CSV`, one database must be specified.  
`kind` |  `string` This is always `sql#importContext`.  
`fileType` |  `enum (`[SqlFileType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#SqlFileType)`)` The file type for the specified uri. * `SQL`: The file contains SQL statements. * `CSV`: The file contains CSV data. * `BAK`: The file contains backup data for a SQL Server instance.  
`csvImportOptions` |  `object` Options for importing data as CSV.  
`csvImportOptions.table` |  `string` The table to which CSV data is imported.  
`csvImportOptions.columns[]` |  `string` The columns to which CSV data is imported. If not specified, all columns of the database table are loaded with CSV data.  
`csvImportOptions.escapeCharacter` |  `string` Specifies the character that should appear before a data character that needs to be escaped.  
`csvImportOptions.quoteCharacter` |  `string` Specifies the quoting character to be used when a data value is quoted.  
`csvImportOptions.fieldsTerminatedBy` |  `string` Specifies the character that separates columns within each row (line) of the file.  
`csvImportOptions.linesTerminatedBy` |  `string` This is used to separate lines. If a line does not contain all fields, the rest of the columns are set to their default values.  
`importUser` |  `string` The PostgreSQL user for this import operation. PostgreSQL instances only.  
`bakImportOptions` |  `object` Import parameters specific to SQL Server .BAK files  
`bakImportOptions.encryptionOptions` |  `object`  
`bakImportOptions.encryptionOptions.certPath` |  `string` Path to the Certificate (.cer) in Cloud Storage, in the form `gs://bucketName/fileName`. The instance must have write permissions to the bucket and read access to the file.  
`bakImportOptions.encryptionOptions.pvkPath` |  `string` Path to the Certificate Private Key (.pvk) in Cloud Storage, in the form `gs://bucketName/fileName`. The instance must have write permissions to the bucket and read access to the file.  
`bakImportOptions.encryptionOptions.pvkPassword` |  `string` Password that encrypts the private key  
`bakImportOptions.encryptionOptions.keepEncrypted` |  `boolean` Optional. Whether the imported file remains encrypted.  
`bakImportOptions.striped` |  `boolean` Whether or not the backup set being restored is striped. Applies only to Cloud SQL for SQL Server.  
`bakImportOptions.noRecovery` |  `boolean` Whether or not the backup importing will restore database with NORECOVERY option. Applies only to Cloud SQL for SQL Server.  
`bakImportOptions.recoveryOnly` |  `boolean` Whether or not the backup importing request will just bring database online without downloading Bak content only one of "noRecovery" and "recoveryOnly" can be true otherwise error will return. Applies only to Cloud SQL for SQL Server.  
`bakImportOptions.bakType` |  `enum (`[BakType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/BakType)`)` Type of the bak content, FULL or DIFF.  
`bakImportOptions.stopAt` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The timestamp when the import should stop. This timestamp is in the [RFC 3339](https://tools.ietf.org/html/rfc3339) format (for example, `2023-10-01T16:19:00.094`). This field is equivalent to the STOPAT keyword and applies to Cloud SQL for SQL Server only.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`bakImportOptions.stopAtMark` |  `string` Optional. The marked transaction where the import should stop. This field is equivalent to the STOPATMARK keyword and applies to Cloud SQL for SQL Server only.  
`sqlImportOptions` |  `object` Optional. Options for importing data from SQL statements.  
`sqlImportOptions.threads` |  `integer` Optional. The number of threads to use for parallel import.  
`sqlImportOptions.parallel` |  `boolean` Optional. Whether or not the import should be parallel.  
`sqlImportOptions.postgresImportOptions` |  `object` Optional. Options for importing from a Cloud SQL for PostgreSQL instance.  
`sqlImportOptions.postgresImportOptions.clean` |  `boolean` Optional. The --clean flag for the pg_restore utility. This flag applies only if you enabled Cloud SQL to import files in parallel.  
`sqlImportOptions.postgresImportOptions.ifExists` |  `boolean` Optional. The --if-exists flag for the pg_restore utility. This flag applies only if you enabled Cloud SQL to import files in parallel.  
`tdeImportOptions` |  `object` Optional. Import parameters specific to SQL Server .TDE files Import parameters specific to SQL Server TDE certificates  
`tdeImportOptions.certificatePath` |  `string` Required. Path to the TDE certificate public key in the form gs://bucketName/fileName. The instance must have read access to the file. Applicable only for SQL Server instances.  
`tdeImportOptions.privateKeyPath` |  `string` Required. Path to the TDE certificate private key in the form gs://bucketName/fileName. The instance must have read access to the file. Applicable only for SQL Server instances.  
`tdeImportOptions.privateKeyPassword` |  `string` Required. Password that encrypts the private key.  
`tdeImportOptions.name` |  `string` Required. Certificate name. Applicable only for SQL Server instances.  
  
## SqlFileType

Enums  
---  
`SQL_FILE_TYPE_UNSPECIFIED` | Unknown file type.  
`SQL` | File containing SQL statements.  
`CSV` | File in CSV format.  
`BAK` |   
`TDE` | TDE certificate.  
  
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
        },
        "threads": integer,
        "parallel": boolean,
        "postgresExportOptions": {
          "clean": boolean,
          "ifExists": boolean
        }
      },
      "csvExportOptions": {
        "selectQuery": string,
        "escapeCharacter": string,
        "quoteCharacter": string,
        "fieldsTerminatedBy": string,
        "linesTerminatedBy": string
      },
      "fileType": enum ([SqlFileType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#SqlFileType)),
      "offload": boolean,
      "bakExportOptions": {
        "striped": boolean,
        "stripeCount": integer,
        "bakType": enum ([BakType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/BakType)),
        "copyOnly": boolean,
        "differentialBase": boolean,
        "exportLogStartTime": string,
        "exportLogEndTime": string
      },
      "tdeExportOptions": {
        "certificatePath": string,
        "privateKeyPath": string,
        "privateKeyPassword": string,
        "name": string
      }
    }  
  
Fields  
---  
`uri` |  `string` The path to the file in Google Cloud Storage where the export will be stored. The URI is in the form `gs://bucketName/fileName`. If the file already exists, the request succeeds, but the operation fails. If `fileType` is `SQL` and the filename ends with .gz, the contents are compressed.  
`databases[]` |  `string` Databases to be exported.   
`MySQL instances:` If `fileType` is `SQL` and no database is specified, all databases are exported, except for the `mysql` system database. If `fileType` is `CSV`, you can specify one database, either by using this property or by using the `csvExportOptions.selectQuery` property, which takes precedence over this property.   
`PostgreSQL instances:` If you don't specify a database by name, all user databases in the instance are exported. This excludes system databases and Cloud SQL databases used to manage internal operations. Exporting all user databases is only available for directory-formatted parallel export. If `fileType` is `CSV`, this database must match the one specified in the `csvExportOptions.selectQuery` property.   
`SQL Server instances:` You must specify one database to be exported, and the `fileType` must be `BAK`.  
`kind` |  `string` This is always `sql#exportContext`.  
`sqlExportOptions` |  `object` Options for exporting data as SQL statements.  
`sqlExportOptions.tables[]` |  `string` Tables to export, or that were exported, from the specified database. If you specify tables, specify one and only one database. For PostgreSQL instances, you can specify only one table.  
`sqlExportOptions.schemaOnly` |  `boolean` Export only schemas.  
`sqlExportOptions.mysqlExportOptions` |  `object`  
`sqlExportOptions.mysqlExportOptions.masterData` |  `integer` Option to include SQL statement required to set up replication. If set to `1`, the dump file includes a CHANGE MASTER TO statement with the binary log coordinates, and --set-gtid-purged is set to ON. If set to `2`, the CHANGE MASTER TO statement is written as a SQL comment and has no effect. If set to any value other than `1`, --set-gtid-purged is set to OFF.  
`sqlExportOptions.threads` |  `integer` Optional. The number of threads to use for parallel export.  
`sqlExportOptions.parallel` |  `boolean` Optional. Whether or not the export should be parallel.  
`sqlExportOptions.postgresExportOptions` |  `object` Optional. Options for exporting from a Cloud SQL for PostgreSQL instance.  
`sqlExportOptions.postgresExportOptions.clean` |  `boolean` Optional. Use this option to include DROP  `<object>` SQL statements. Use these statements to delete database objects before running the import operation.  
`sqlExportOptions.postgresExportOptions.ifExists` |  `boolean` Optional. Option to include an IF EXISTS SQL statement with each DROP statement produced by clean.  
`csvExportOptions` |  `object` Options for exporting data as CSV. `MySQL` and `PostgreSQL` instances only.  
`csvExportOptions.selectQuery` |  `string` The select query used to extract the data.  
`csvExportOptions.escapeCharacter` |  `string` Specifies the character that should appear before a data character that needs to be escaped.  
`csvExportOptions.quoteCharacter` |  `string` Specifies the quoting character to be used when a data value is quoted.  
`csvExportOptions.fieldsTerminatedBy` |  `string` Specifies the character that separates columns within each row (line) of the file.  
`csvExportOptions.linesTerminatedBy` |  `string` This is used to separate lines. If a line does not contain all fields, the rest of the columns are set to their default values.  
`fileType` |  `enum (`[SqlFileType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#SqlFileType)`)` The file type for the specified uri.  
`offload` |  `boolean` Whether to perform a serverless export.  
`bakExportOptions` |  `object` Options for exporting data as BAK files.  
`bakExportOptions.striped` |  `boolean` Whether or not the export should be striped.  
`bakExportOptions.stripeCount` |  `integer` Option for specifying how many stripes to use for the export. If blank, and the value of the striped field is true, the number of stripes is automatically chosen.  
`bakExportOptions.bakType` |  `enum (`[BakType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/BakType)`)` Type of this bak file will be export, FULL or DIFF, SQL Server only  
`bakExportOptions.copyOnly  
**(deprecated)**` |  `boolean` Deprecated: copyOnly is deprecated. Use differentialBase instead  
`bakExportOptions.differentialBase` |  `boolean` Whether or not the backup can be used as a differential base copyOnly backup can not be served as differential base  
`bakExportOptions.exportLogStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The begin timestamp when transaction log will be included in the export operation. [RFC 3339](https://tools.ietf.org/html/rfc3339) format (for example, `2023-10-01T16:19:00.094`) in UTC. When omitted, all available logs from the beginning of retention period will be included. Only applied to Cloud SQL for SQL Server.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`bakExportOptions.exportLogEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The end timestamp when transaction log will be included in the export operation. [RFC 3339](https://tools.ietf.org/html/rfc3339) format (for example, `2023-10-01T16:19:00.094`) in UTC. When omitted, all available logs until current time will be included. Only applied to Cloud SQL for SQL Server.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`tdeExportOptions` |  `object` Optional. Export parameters specific to SQL Server TDE certificates  
`tdeExportOptions.certificatePath` |  `string` Required. Path to the TDE certificate public key in the form gs://bucketName/fileName. The instance must have write access to the location. Applicable only for SQL Server instances.  
`tdeExportOptions.privateKeyPath` |  `string` Required. Path to the TDE certificate private key in the form gs://bucketName/fileName. The instance must have write access to the location. Applicable only for SQL Server instances.  
`tdeExportOptions.privateKeyPassword` |  `string` Required. Password that encrypts the private key.  
`tdeExportOptions.name` |  `string` Required. Certificate name. Applicable only for SQL Server instances.  
  
## BackupContext

Backup context.

JSON representation  
---  
      
    
    {
      "backupId": string,
      "kind": string,
      "name": string
    }  
  
Fields  
---  
`backupId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The identifier of the backup.  
`kind` |  `string` This is always `sql#backupContext`.  
`name` |  `string` The name of the backup. Format: projects/{project}/backups/{backup}  
  
## PreCheckMajorVersionUpgradeContext

Pre-check major version upgrade context.

JSON representation  
---  
      
    
    {
      "targetDatabaseVersion": enum ([SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/SqlDatabaseVersion)),
      "preCheckResponse": [
        {
          object ([PreCheckResponse](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#PreCheckResponse))
        }
      ],
      "kind": string
    }  
  
Fields  
---  
`targetDatabaseVersion` |  `enum (`[SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/SqlDatabaseVersion)`)` Required. The target database version to upgrade to.  
`preCheckResponse[]` |  `object (`[PreCheckResponse](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#PreCheckResponse)`)` Output only. The responses from the precheck operation.  
`kind` |  `string` Optional. This is always `sql#preCheckMajorVersionUpgradeContext`.  
  
## PreCheckResponse

Structured PreCheckResponse containing message, type, and required actions.

JSON representation  
---  
      
    
    {
      "actionsRequired": [
        string
      ],
      "message": string,
      "messageType": enum ([MessageType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#MessageType))
    }  
  
Fields  
---  
`actionsRequired[]` |  `string` The actions that the user needs to take. Use repeated for multiple actions.  
`message` |  `string` The message to be displayed to the user.  
`messageType` |  `enum (`[MessageType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#MessageType)`)` The type of message whether it is an info, warning, or error.  
  
## MessageType

The type of message which can be an info, a warning, or an error that requires user intervention.

Enums  
---  
`MESSAGE_TYPE_UNSPECIFIED` | Default unspecified value to prevent unintended behavior changes.  
`INFO` | General informational messages that don't require action.  
`WARNING` | Warnings that might impact the upgrade but don't block it.  
`ERROR` | Errors that a user must resolve before proceeding with the upgrade.  
  
## AcquireSsrsLeaseContext

Acquire SSRS lease context.

JSON representation  
---  
      
    
    {
      "setupLogin": string,
      "serviceLogin": string,
      "reportDatabase": string,
      "duration": string
    }  
  
Fields  
---  
`setupLogin` |  `string` The username to be used as the setup login to connect to the database server for SSRS setup.  
`serviceLogin` |  `string` The username to be used as the service login to connect to the report database for SSRS setup.  
`reportDatabase` |  `string` The report database to be used for the SSRS setup.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Lease duration needed for the SSRS setup.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## SqlSubOperationType

The sub operation type based on the operation type.

JSON representation  
---  
      
    
    {
    
      // Union field sub_operation_details can be only one of the following:
      "maintenanceType": enum ([SqlMaintenanceType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#SqlMaintenanceType))
      // End of list of possible types for union field sub_operation_details.
    }  
  
Fields  
---  
Union field `sub_operation_details`. Sub operation details corresponding to the operation type. `sub_operation_details` can be only one of the following:  
`maintenanceType` |  `enum (`[SqlMaintenanceType](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations#SqlMaintenanceType)`)` The type of maintenance to be performed on the instance.  
  
## SqlMaintenanceType

The type of maintenance to be performed on the instance.

Enums  
---  
`SQL_MAINTENANCE_TYPE_UNSPECIFIED` | Maintenance type is unspecified.  
`INSTANCE_MAINTENANCE` | Indicates that a standalone instance is undergoing maintenance. The instance can be either a primary instance or a replica.  
`REPLICA_INCLUDED_MAINTENANCE` | Indicates that the primary instance and all of its replicas, including cascading replicas, are undergoing maintenance. Maintenance is performed on groups of replicas first, followed by the primary instance.  
`INSTANCE_SELF_SERVICE_MAINTENANCE` | Indicates that the standalone instance is undergoing maintenance, initiated by self-service. The instance can be either a primary instance or a replica.  
`REPLICA_INCLUDED_SELF_SERVICE_MAINTENANCE` | Indicates that the primary instance and all of its replicas are undergoing maintenance, initiated by self-service. Maintenance is performed on groups of replicas first, followed by the primary instance.  
  
## Methods  
  
---  
  
### `[cancel](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations/cancel)`

|  Cancels an instance operation that has been performed on an instance.  
  
### `[get](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations/get)`

|  Retrieves an instance operation that has been performed on an instance.  
  
### `[list](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/operations/list)`

|  Lists all instance operations that have been performed on the given Cloud SQL instance in the reverse chronological order of the start time.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
