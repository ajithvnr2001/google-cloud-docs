---
url: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/projects.instances/verifyExternalSyncSettings/
title: Method: projects.instances.verifyExternalSyncSettings \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:14:23.174961+00:00
---

# Method: projects.instances.verifyExternalSyncSettings  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/projects.instances/verifyExternalSyncSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/postgres/apis)



Send feedback 

#  Method: projects.instances.verifyExternalSyncSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * ExternalSyncSelectedObject
    * JSON representation
  * SqlExternalSyncSettingError
    * JSON representation
  * SqlExternalSyncSettingErrorType
  * Examples
  * Try it!



Verify External primary instance external sync settings.

### HTTP request

`POST https://sqladmin.googleapis.com/v1/projects/{project}/instances/{instance}/verifyExternalSyncSettings`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID of the project that contains the instance.  
`instance` |  `string` Cloud SQL instance ID. This does not include the project ID.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "verifyConnectionOnly": boolean,
      "syncMode": enum ([ExternalSyncMode](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/ExternalSyncMode)),
      "verifyReplicationOnly": boolean,
      "migrationType": enum ([MigrationType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/MigrationType)),
      "syncParallelLevel": enum ([ExternalSyncParallelLevel](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/ExternalSyncParallelLevel)),
      "selectedObjects": [
        {
          object ([ExternalSyncSelectedObject](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/projects.instances/verifyExternalSyncSettings#ExternalSyncSelectedObject))
        }
      ],
    
      // Union field sync_config can be only one of the following:
      "mysqlSyncConfig": {
        object ([MySqlSyncConfig](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/MySqlSyncConfig))
      }
      // End of list of possible types for union field sync_config.
    }  
  
Fields  
---  
`verifyConnectionOnly` |  `boolean` Flag to enable verifying connection only  
`syncMode` |  `enum (`[ExternalSyncMode](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/ExternalSyncMode)`)` External sync mode  
`verifyReplicationOnly` |  `boolean` Optional. Flag to verify settings required by replication setup only  
`migrationType` |  `enum (`[MigrationType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/MigrationType)`)` Optional. MigrationType configures the migration to use physical files or logical dump files. If not set, then the logical dump file configuration is used. Valid values are `LOGICAL` or `PHYSICAL`. Only applicable to MySQL.  
`syncParallelLevel` |  `enum (`[ExternalSyncParallelLevel](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/ExternalSyncParallelLevel)`)` Optional. Parallel level for initial data sync. Only applicable for PostgreSQL.  
`selectedObjects[]` |  `object (`[ExternalSyncSelectedObject](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/projects.instances/verifyExternalSyncSettings#ExternalSyncSelectedObject)`)` Optional. Migrate only the specified objects from the source instance. If this field is empty, then migrate all objects.  
Union field `sync_config`.`sync_config` can be only one of the following:  
`mysqlSyncConfig` |  `object (`[MySqlSyncConfig](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/MySqlSyncConfig)`)` Optional. MySQL-specific settings for start external sync.  
  
### Response body

Instance verify external sync settings response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "errors": [
        {
          object ([SqlExternalSyncSettingError](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/projects.instances/verifyExternalSyncSettings#SqlExternalSyncSettingError))
        }
      ],
      "warnings": [
        {
          object ([SqlExternalSyncSettingError](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/projects.instances/verifyExternalSyncSettings#SqlExternalSyncSettingError))
        }
      ]
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#migrationSettingErrorList`.  
`errors[]` |  `object (`[SqlExternalSyncSettingError](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/projects.instances/verifyExternalSyncSettings#SqlExternalSyncSettingError)`)` List of migration violations.  
`warnings[]` |  `object (`[SqlExternalSyncSettingError](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/projects.instances/verifyExternalSyncSettings#SqlExternalSyncSettingError)`)` List of migration warnings.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ExternalSyncSelectedObject

The selected object that Cloud SQL migrates.

JSON representation  
---  
      
    
    {
      "database": string
    }  
  
Fields  
---  
`database` |  `string` The name of the database that Cloud SQL migrates.  
  
## SqlExternalSyncSettingError

External primary instance migration setting error/warning.

JSON representation  
---  
      
    
    {
      "kind": string,
      "type": enum ([SqlExternalSyncSettingErrorType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/projects.instances/verifyExternalSyncSettings#SqlExternalSyncSettingErrorType)),
      "detail": string
    }  
  
Fields  
---  
`kind` |  `string` Can be `sql#externalSyncSettingError` or `sql#externalSyncSettingWarning`.  
`type` |  `enum (`[SqlExternalSyncSettingErrorType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/projects.instances/verifyExternalSyncSettings#SqlExternalSyncSettingErrorType)`)` Identifies the specific error that occurred.  
`detail` |  `string` Additional information about the error encountered.  
  
## SqlExternalSyncSettingErrorType

Enums  
---  
`SQL_EXTERNAL_SYNC_SETTING_ERROR_TYPE_UNSPECIFIED` |   
`CONNECTION_FAILURE` |   
`BINLOG_NOT_ENABLED` |   
`INCOMPATIBLE_DATABASE_VERSION` |   
`REPLICA_ALREADY_SETUP` |   
`INSUFFICIENT_PRIVILEGE` | The replication user is missing privileges that are required.  
`UNSUPPORTED_MIGRATION_TYPE` | Unsupported migration type.  
`NO_PGLOGICAL_INSTALLED` | No pglogical extension installed on databases, applicable for postgres.  
`PGLOGICAL_NODE_ALREADY_EXISTS` | pglogical node already exists on databases, applicable for postgres.  
`INVALID_WAL_LEVEL` | The value of parameter wal_level is not set to logical.  
`INVALID_SHARED_PRELOAD_LIBRARY` | The value of parameter shared_preload_libraries does not include pglogical.  
`INSUFFICIENT_MAX_REPLICATION_SLOTS` | The value of parameter max_replication_slots is not sufficient.  
`INSUFFICIENT_MAX_WAL_SENDERS` | The value of parameter max_wal_senders is not sufficient.  
`INSUFFICIENT_MAX_WORKER_PROCESSES` | The value of parameter max_worker_processes is not sufficient.  
`UNSUPPORTED_EXTENSIONS` | Extensions installed are either not supported or having unsupported versions.  
`INVALID_RDS_LOGICAL_REPLICATION` | The value of parameter rds.logical_replication is not set to 1.  
`INVALID_LOGGING_SETUP` | The primary instance logging setup doesn't allow EM sync.  
`INVALID_DB_PARAM` | The primary instance database parameter setup doesn't allow EM sync.  
`UNSUPPORTED_GTID_MODE` | The gtid_mode is not supported, applicable for MySQL.  
`SQLSERVER_AGENT_NOT_RUNNING` | SQL Server Agent is not running.  
`UNSUPPORTED_TABLE_DEFINITION` | The table definition is not support due to missing primary key or replica identity, applicable for postgres. Note that this is a warning and won't block the migration.  
`UNSUPPORTED_DEFINER` | The customer has a definer that will break EM setup.  
`SQLSERVER_SERVERNAME_MISMATCH` | SQL Server @@SERVERNAME does not match actual host name.  
`PRIMARY_ALREADY_SETUP` | The primary instance has been setup and will fail the setup.  
`UNSUPPORTED_BINLOG_FORMAT` | The primary instance has unsupported binary log format.  
`BINLOG_RETENTION_SETTING` | The primary instance's binary log retention setting.  
`UNSUPPORTED_STORAGE_ENGINE` | The primary instance has tables with unsupported storage engine.  
`LIMITED_SUPPORT_TABLES` | Source has tables with limited support eg: PostgreSQL tables without primary keys.  
`EXISTING_DATA_IN_REPLICA` | The replica instance contains existing data.  
`MISSING_OPTIONAL_PRIVILEGES` | The replication user is missing privileges that are optional.  
`RISKY_BACKUP_ADMIN_PRIVILEGE` | Additional BACKUP_ADMIN privilege is granted to the replication user which may lock source MySQL 8 instance for DDLs during initial sync.  
`INSUFFICIENT_GCS_PERMISSIONS` | The Cloud Storage bucket is missing necessary permissions.  
`INVALID_FILE_INFO` | The Cloud Storage bucket has an error in the file or contains invalid file information.  
`UNSUPPORTED_DATABASE_SETTINGS` | The source instance has unsupported database settings for migration.  
`MYSQL_PARALLEL_IMPORT_INSUFFICIENT_PRIVILEGE` | The replication user is missing parallel import specific privileges. (e.g. LOCK TABLES) for MySQL.  
`LOCAL_INFILE_OFF` | The global variable local_infile is off on external server replica.  
`TURN_ON_PITR_AFTER_PROMOTE` | This code instructs customers to turn on point-in-time recovery manually for the instance after promoting the Cloud SQL for PostgreSQL instance.  
`INCOMPATIBLE_DATABASE_MINOR_VERSION` | The minor version of replica database is incompatible with the source.  
`SOURCE_MAX_SUBSCRIPTIONS` | This warning message indicates that Cloud SQL uses the maximum number of subscriptions to migrate data from the source to the destination.  
`UNABLE_TO_VERIFY_DEFINERS` | Unable to verify definers on the source for MySQL.  
`SUBSCRIPTION_CALCULATION_STATUS` | If a time out occurs while the subscription counts are calculated, then this value is set to 1. Otherwise, this value is set to 2.  
`PG_SUBSCRIPTION_COUNT` | Count of subscriptions needed to sync source data for PostgreSQL database.  
`PG_SYNC_PARALLEL_LEVEL` | Final parallel level that is used to do migration.  
`INSUFFICIENT_DISK_SIZE` | The disk size of the replica instance is smaller than the data size of the source instance.  
`INSUFFICIENT_MACHINE_TIER` | The data size of the source instance is greater than 1 TB, the number of cores of the replica instance is less than 8, and the memory of the replica is less than 32 GB.  
`UNSUPPORTED_EXTENSIONS_NOT_MIGRATED` | The warning message indicates the unsupported extensions will not be migrated to the destination.  
`EXTENSIONS_NOT_MIGRATED` | The warning message indicates the pg_cron extension and settings will not be migrated to the destination.  
`PG_CRON_FLAG_ENABLED_IN_REPLICA` | The error message indicates that pg_cron flags are enabled on the destination which is not supported during the migration.  
`EXTENSIONS_NOT_ENABLED_IN_REPLICA` | This error message indicates that the specified extensions are not enabled on destination instance. For example, before you can migrate data to the destination instance, you must enable the PGAudit extension on the instance.  
`UNSUPPORTED_COLUMNS` | The source database has generated columns that can't be migrated. Please change them to regular columns before migration.  
`USERS_NOT_CREATED_IN_REPLICA` | The source database has users that aren't created in the replica. First, create all users, which are in the pg_user_mappings table of the source database, in the destination instance. Then, perform the migration.  
`UNSUPPORTED_SYSTEM_OBJECTS` | The selected objects include system objects that aren't supported for migration.  
`UNSUPPORTED_TABLES_WITH_REPLICA_IDENTITY` | The source database has tables with the FULL or NOTHING replica identity. Before starting your migration, either remove the identity or change it to DEFAULT. Note that this is an error and will block the migration.  
`SELECTED_OBJECTS_NOT_EXIST_ON_SOURCE` | The selected objects don't exist on the source instance.  
`PSC_ONLY_INSTANCE_WITH_NO_NETWORK_ATTACHMENT_URI` | PSC only destination instance does not have a network attachment URI.  
`PG_DDL_REPLICATION_INSUFFICIENT_PRIVILEGE` | The replication user is missing specific privileges to setup DDL replication. (e.g. CREATE EVENT TRIGGER, CREATE SCHEMA) for PostgreSQL.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
