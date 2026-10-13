---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs
title: REST Resource: projects.locations.migrationJobs \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:35.047685+00:00
---

# REST Resource: projects.locations.migrationJobs  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  REST Resource: projects.locations.migrationJobs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MigrationJob
    * JSON representation
  * State
  * Phase
  * Type
  * DumpFlags
    * JSON representation
  * DumpFlag
    * JSON representation
  * ReverseSshConnectivity
    * JSON representation
  * VpcPeeringConnectivity
    * JSON representation
  * DatabaseType
    * JSON representation
  * ConversionWorkspaceInfo
    * JSON representation
  * PerformanceConfig
    * JSON representation
  * DumpParallelLevel
  * PostgresHomogeneousConfig
    * JSON representation
  * MySqlHomogeneousConfig
    * JSON representation
  * SqlServerHomogeneousMigrationJobConfig
    * JSON representation
  * SqlServerDatabaseBackup
    * JSON representation
  * SqlServerEncryptionOptions
    * JSON representation
  * SqlServerDagConfig
    * JSON representation
  * DumpType
  * OracleToPostgresConfig
    * JSON representation
  * OracleSourceConfig
    * JSON representation
  * LogMiner
  * BinaryLogParser
    * JSON representation
  * OracleAsmLogFileAccess
  * LogFileDirectories
    * JSON representation
  * PostgresDestinationConfig
    * JSON representation
  * SqlServerToPostgresConfig
    * JSON representation
  * SqlServerSourceConfig
    * JSON representation
  * PostgresToSqlServerConfig
    * JSON representation
  * PostgresSourceConfig
    * JSON representation
  * SqlServerDestinationConfig
    * JSON representation
  * MigrationJobObjectsConfig
    * JSON representation
  * SourceObjectsConfig
    * JSON representation
  * SourceObjectConfig
    * JSON representation
  * ObjectsSelectionType
  * Purpose
  * Methods



## Resource: MigrationJob

Represents a Database Migration Service migration job object.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "displayName": string,
      "state": enum ([State](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#State)),
      "phase": enum ([Phase](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#Phase)),
      "type": enum ([Type](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#Type)),
      "dumpPath": string,
      "dumpFlags": {
        object ([DumpFlags](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#DumpFlags))
      },
      "source": string,
      "destination": string,
      "duration": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/database-migration/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "sourceDatabase": {
        object ([DatabaseType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#DatabaseType))
      },
      "destinationDatabase": {
        object ([DatabaseType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#DatabaseType))
      },
      "endTime": string,
      "conversionWorkspace": {
        object ([ConversionWorkspaceInfo](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#ConversionWorkspaceInfo))
      },
      "filter": string,
      "cmekKeyName": string,
      "performanceConfig": {
        object ([PerformanceConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#PerformanceConfig))
      },
      "postgresHomogeneousConfig": {
        object ([PostgresHomogeneousConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#PostgresHomogeneousConfig))
      },
      "mysqlHomogeneousConfig": {
        object ([MySqlHomogeneousConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#MySqlHomogeneousConfig))
      },
      "sqlserverHomogeneousMigrationJobConfig": {
        object ([SqlServerHomogeneousMigrationJobConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SqlServerHomogeneousMigrationJobConfig))
      },
      "dumpType": enum ([DumpType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#DumpType)),
      "objectsConfig": {
        object ([MigrationJobObjectsConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#MigrationJobObjectsConfig))
      },
      "purpose": enum ([Purpose](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#Purpose)),
      "originalMigrationName": string,
    
      // Union field connectivity can be only one of the following:
      "reverseSshConnectivity": {
        object ([ReverseSshConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#ReverseSshConnectivity))
      },
      "vpcPeeringConnectivity": {
        object ([VpcPeeringConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#VpcPeeringConnectivity))
      },
      "staticIpConnectivity": {
        object ([StaticIpConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/StaticIpConnectivity))
      }
      // End of list of possible types for union field connectivity.
    
      // Union field config can be only one of the following:
      "oracleToPostgresConfig": {
        object ([OracleToPostgresConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#OracleToPostgresConfig))
      },
      "sqlserverToPostgresConfig": {
        object ([SqlServerToPostgresConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SqlServerToPostgresConfig))
      },
      "postgresToSqlserverConfig": {
        object ([PostgresToSqlServerConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#PostgresToSqlServerConfig))
      }
      // End of list of possible types for union field config.
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean
    }  
  
Fields  
---  
`name` |  `string` The name (URI) of this migration job resource, in the form of: projects/{project}/locations/{location}/migrationJobs/{migrationJob}.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the migration job resource was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the migration job resource was last updated. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` The resource labels for migration job to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs.Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`displayName` |  `string` The migration job display name.  
`state` |  `enum (`[State](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#State)`)` The current migration job state.  
`phase` |  `enum (`[Phase](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#Phase)`)` Output only. The current migration job phase.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#Type)`)` Required. The migration job type.  
`dumpPath` |  `string` The path to the dump file in Google Cloud Storage, in the format: (gs://[BUCKET_NAME]/[OBJECT_NAME]). This field and the "dumpFlags" field are mutually exclusive.  
`dumpFlags` |  `object (`[DumpFlags](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#DumpFlags)`)` The initial dump flags. This field and the "dumpPath" field are mutually exclusive.  
`source` |  `string` Required. The resource name (URI) of the source connection profile.  
`destination` |  `string` Required. The resource name (URI) of the destination connection profile.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The duration of the migration job (in seconds). A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`error` |  `object (`[Status](https://docs.cloud.google.com/database-migration/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Output only. The error details in case of state FAILED.  
`sourceDatabase` |  `object (`[DatabaseType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#DatabaseType)`)` The database engine type and provider of the source.  
`destinationDatabase` |  `object (`[DatabaseType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#DatabaseType)`)` The database engine type and provider of the destination.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. If the migration job is completed, the time when it was completed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`conversionWorkspace` |  `object (`[ConversionWorkspaceInfo](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#ConversionWorkspaceInfo)`)` The conversion workspace used by the migration.  
`filter` |  `string` This field can be used to select the entities to migrate as part of the migration job. It uses AIP-160 notation to select a subset of the entities configured on the associated conversion-workspace. This field should not be set on migration-jobs that are not associated with a conversion workspace.  
`cmekKeyName` |  `string` The CMEK (customer-managed encryption key) fully qualified key name used for the migration job. This field supports all migration jobs types except for: * Mysql to Mysql (use the cmek field in the cloudsql connection profile instead). * PostrgeSQL to PostgreSQL (use the cmek field in the cloudsql connection profile instead). * PostgreSQL to AlloyDB (use the kmsKeyName field in the alloydb connection profile instead). Each Cloud CMEK key has the following format: projects/[PROJECT]/locations/[REGION]/keyRings/[RING]/cryptoKeys/[KEY_NAME]  
`performanceConfig` |  `object (`[PerformanceConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#PerformanceConfig)`)` Optional. Data dump parallelism settings used by the migration.  
`postgresHomogeneousConfig` |  `object (`[PostgresHomogeneousConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#PostgresHomogeneousConfig)`)` Optional. Configuration for PostgreSQL homogeneous migration.  
`mysqlHomogeneousConfig` |  `object (`[MySqlHomogeneousConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#MySqlHomogeneousConfig)`)` Optional. Configuration for MySQL homogeneous migration.  
`sqlserverHomogeneousMigrationJobConfig` |  `object (`[SqlServerHomogeneousMigrationJobConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SqlServerHomogeneousMigrationJobConfig)`)` Optional. Configuration for SQL Server homogeneous migration.  
`dumpType` |  `enum (`[DumpType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#DumpType)`)` Optional. The type of the data dump. Supported for MySQL to CloudSQL for MySQL migrations only.  
`objectsConfig` |  `object (`[MigrationJobObjectsConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#MigrationJobObjectsConfig)`)` Optional. The objects that need to be migrated.  
`purpose` |  `enum (`[Purpose](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#Purpose)`)` Output only. Migration job mode. Migration jobs can be standard forward jobs or failback migration jobs.  
`originalMigrationName` |  `string` Optional. A failback replication pointer to the resource name (URI) of the original migration job.  
Union field `connectivity`. The connectivity method. `connectivity` can be only one of the following:  
`reverseSshConnectivity` |  `object (`[ReverseSshConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#ReverseSshConnectivity)`)` The details needed to communicate to the source over Reverse SSH tunnel connectivity.  
`vpcPeeringConnectivity` |  `object (`[VpcPeeringConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#VpcPeeringConnectivity)`)` The details of the VPC network that the source database is located in.  
`staticIpConnectivity` |  `object (`[StaticIpConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/StaticIpConnectivity)`)` static ip connectivity data (default, no additional details needed).  
Union field `config`. Configuration for migration. `config` can be only one of the following:  
`oracleToPostgresConfig` |  `object (`[OracleToPostgresConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#OracleToPostgresConfig)`)` Configuration for heterogeneous **Oracle to Cloud SQL for PostgreSQL** and **Oracle to AlloyDB for PostgreSQL** migrations.  
`sqlserverToPostgresConfig` |  `object (`[SqlServerToPostgresConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SqlServerToPostgresConfig)`)` Configuration for heterogeneous **SQL Server to Cloud SQL for PostgreSQL** migrations.  
`postgresToSqlserverConfig` |  `object (`[PostgresToSqlServerConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#PostgresToSqlServerConfig)`)` Configuration for heterogeneous failback migrations from **PostgreSQL to SQL Server**.  
`satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`satisfiesPzi` |  `boolean` Output only. Reserved for future use.  
  
## State

The current migration job states.

Enums  
---  
`STATE_UNSPECIFIED` | The state of the migration job is unknown.  
`MAINTENANCE` | The migration job is down for maintenance.  
`DRAFT` | The migration job is in draft mode and no resources are created.  
`CREATING` | The migration job is being created.  
`NOT_STARTED` | The migration job is created and not started.  
`RUNNING` | The migration job is running.  
`FAILED` | The migration job failed.  
`COMPLETED` | The migration job has been completed.  
`DELETING` | The migration job is being deleted.  
`STOPPING` | The migration job is being stopped.  
`STOPPED` | The migration job is currently stopped.  
`DELETED` | The migration job has been deleted.  
`UPDATING` | The migration job is being updated.  
`STARTING` | The migration job is starting.  
`RESTARTING` | The migration job is restarting.  
`RESUMING` | The migration job is resuming.  
  
## Phase

The current migration job phase.

Enums  
---  
`PHASE_UNSPECIFIED` | The phase of the migration job is unknown.  
`FULL_DUMP` | The migration job is in the full dump phase.  
`CDC` | The migration job is CDC phase.  
`PROMOTE_IN_PROGRESS` | The migration job is running the promote phase.  
`WAITING_FOR_SOURCE_WRITES_TO_STOP` | Only RDS flow - waiting for source writes to stop  
`PREPARING_THE_DUMP` | Only RDS flow - the sources writes stopped, waiting for dump to begin  
`READY_FOR_PROMOTE` | The migration job is ready to be promoted.  
  
## Type

The type of migration job (one-time or continuous).

Enums  
---  
`TYPE_UNSPECIFIED` | The type of the migration job is unknown.  
`ONE_TIME` | The migration job is a one time migration.  
`CONTINUOUS` | The migration job is a continuous migration.  
  
## DumpFlags

Dump flags definition.

JSON representation  
---  
      
    
    {
      "dumpFlags": [
        {
          object ([DumpFlag](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#DumpFlag))
        }
      ]
    }  
  
Fields  
---  
`dumpFlags[]` |  `object (`[DumpFlag](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#DumpFlag)`)` The flags for the initial dump.  
  
## DumpFlag

Dump flag definition.

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string
    }  
  
Fields  
---  
`name` |  `string` The name of the flag  
`value` |  `string` The value of the flag.  
  
## ReverseSshConnectivity

The details needed to configure a reverse SSH tunnel between the source and destination databases. These details will be used when calling the generateSshScript method (see <https://cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/generateSshScript>) to produce the script that will help set up the reverse SSH tunnel, and to set up the VPC peering between the Cloud SQL private network and the VPC.

JSON representation  
---  
      
    
    {
      "vmIp": string,
      "vmPort": integer,
      "vm": string,
      "vpc": string
    }  
  
Fields  
---  
`vmIp` |  `string` Required. The IP of the virtual machine (Compute Engine) used as the bastion server for the SSH tunnel.  
`vmPort` |  `integer` Required. The forwarding port of the virtual machine (Compute Engine) used as the bastion server for the SSH tunnel.  
`vm` |  `string` The name of the virtual machine (Compute Engine) used as the bastion server for the SSH tunnel.  
`vpc` |  `string` The name of the VPC to peer with the Cloud SQL private network.  
  
## VpcPeeringConnectivity

The details of the VPC where the source database is located in Google Cloud. We will use this information to set up the VPC peering connection between Cloud SQL and this VPC.

JSON representation  
---  
      
    
    {
      "vpc": string
    }  
  
Fields  
---  
`vpc` |  `string` The name of the VPC network to peer with the Cloud SQL private network.  
  
## DatabaseType

A message defining the database engine and provider.

JSON representation  
---  
      
    
    {
      "provider": enum ([DatabaseProvider](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/DatabaseProvider)),
      "engine": enum ([DatabaseEngine](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/DatabaseEngine))
    }  
  
Fields  
---  
`provider` |  `enum (`[DatabaseProvider](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/DatabaseProvider)`)` The database provider.  
`engine` |  `enum (`[DatabaseEngine](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/DatabaseEngine)`)` The database engine.  
  
## ConversionWorkspaceInfo

A conversion workspace's version.

JSON representation  
---  
      
    
    {
      "name": string,
      "commitId": string
    }  
  
Fields  
---  
`name` |  `string` The resource name (URI) of the conversion workspace.  
`commitId` |  `string` The commit ID of the conversion workspace.  
  
## PerformanceConfig

Performance configuration definition.

JSON representation  
---  
      
    
    {
      "dumpParallelLevel": enum ([DumpParallelLevel](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#DumpParallelLevel))
    }  
  
Fields  
---  
`dumpParallelLevel` |  `enum (`[DumpParallelLevel](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#DumpParallelLevel)`)` Initial dump parallelism level.  
  
## DumpParallelLevel

Describes the parallelism level during initial dump.

Enums  
---  
`DUMP_PARALLEL_LEVEL_UNSPECIFIED` | Unknown dump parallel level. Will be defaulted to OPTIMAL.  
`MIN` | Minimal parallel level.  
`OPTIMAL` | Optimal parallel level.  
`MAX` | Maximum parallel level.  
  
## PostgresHomogeneousConfig

Configuration for PostgreSQL to PostgreSQL migrations.

JSON representation  
---  
      
    
    {
      "isNativeLogical": boolean,
      "maxAdditionalSubscriptions": integer
    }  
  
Fields  
---  
`isNativeLogical` |  `boolean` Required. Whether the migration is native logical.  
`maxAdditionalSubscriptions` |  `integer` Optional. Maximum number of additional subscriptions to use for the migration job.  
  
## MySqlHomogeneousConfig

Configuration for MySQL to MySQL migrations.

JSON representation  
---  
      
    
    {
      "isPrimaryDestination": boolean
    }  
  
Fields  
---  
`isPrimaryDestination` |  `boolean` Optional. Whether the destination for the migration job is a primary instance.  
  
## SqlServerHomogeneousMigrationJobConfig

Configuration for homogeneous migration to Cloud SQL for SQL Server.

JSON representation  
---  
      
    
    {
      "backupFilePattern": string,
      "databaseBackups": [
        {
          object ([SqlServerDatabaseBackup](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SqlServerDatabaseBackup))
        }
      ],
      "useDiffBackup": boolean,
      "promoteWhenReady": boolean,
      "dagConfig": {
        object ([SqlServerDagConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SqlServerDagConfig))
      }
    }  
  
Fields  
---  
`backupFilePattern` |  `string` Required. Pattern that describes the default backup naming strategy. The specified pattern should ensure lexicographical order of backups. The pattern must define one of the following capture group sets: Capture group set #1 yy/yyyy - year, 2 or 4 digits mm - month number, 1-12 dd - day of month, 1-31 hh - hour of day, 00-23 mi - minutes, 00-59 ss - seconds, 00-59 Example: For backup file TestDB_20230802_155400.trn, use pattern: (?.*)_backup_(?\d{4})(?\d{2})(?    \d{2})_(?\d{2})(?\d{2})(?\d{2}).trn Capture group set #2 timestamp - unix timestamp Example: For backup file TestDB.1691448254.trn, use pattern: (?.*).(?\d*).trn or (?.*).(?\d*).trn  
`databaseBackups[]` |  `object (`[SqlServerDatabaseBackup](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SqlServerDatabaseBackup)`)` Required. Backup details per database in Cloud Storage.  
`useDiffBackup` |  `boolean` Optional. Enable differential backups.  
`promoteWhenReady` |  `boolean` Optional. Promote databases when ready.  
`dagConfig` |  `object (`[SqlServerDagConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SqlServerDagConfig)`)` Optional. Configuration for distributed availability group (DAG) for the SQL Server homogeneous migration.  
  
## SqlServerDatabaseBackup

Specifies the backup details for a single database in Cloud Storage for homogeneous migration to Cloud SQL for SQL Server.

JSON representation  
---  
      
    
    {
      "database": string,
      "encryptionOptions": {
        object ([SqlServerEncryptionOptions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SqlServerEncryptionOptions))
      }
    }  
  
Fields  
---  
`database` |  `string` Required. Name of a SQL Server database for which to define backup configuration.  
`encryptionOptions` |  `object (`[SqlServerEncryptionOptions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SqlServerEncryptionOptions)`)` Optional. Encryption settings for the database. Required if provided database backups are encrypted. Encryption settings include path to certificate, path to certificate private key, and key password.  
  
## SqlServerEncryptionOptions

Encryption settings for the SQL Server database.

JSON representation  
---  
      
    
    {
      "certPath": string,
      "pvkPath": string,
      "pvkPassword": string
    }  
  
Fields  
---  
`certPath` |  `string` Required. Path to the Certificate (.cer) in Cloud Storage, in the form `gs://bucketName/fileName`. The instance must have write permissions to the bucket and read access to the file.  
`pvkPath` |  `string` Required. Path to the Certificate Private Key (.pvk) in Cloud Storage, in the form `gs://bucketName/fileName`. The instance must have write permissions to the bucket and read access to the file.  
`pvkPassword` |  `string` Required. Input only. Password that encrypts the private key.  
  
## SqlServerDagConfig

Configuration for distributed availability group (DAG) for the SQL Server homogeneous migration.

JSON representation  
---  
      
    
    {
      "sourceAg": string,
      "linkedServer": string
    }  
  
Fields  
---  
`sourceAg` |  `string` Required. The name of the source availability group. Only used by DAG migrations.  
`linkedServer` |  `string` Required. The name of the linked server that points to the source SQL Server instance. Only used by DAG migrations.  
  
## DumpType

The type of the data dump.

Enums  
---  
`DUMP_TYPE_UNSPECIFIED` | If not specified, defaults to LOGICAL  
`LOGICAL` | Logical dump.  
`PHYSICAL` | Physical file-based dump. Supported for MySQL to CloudSQL for MySQL migrations only.  
  
## OracleToPostgresConfig

Configuration for heterogeneous **Oracle to Cloud SQL for PostgreSQL** and **Oracle to AlloyDB for PostgreSQL** migrations.

JSON representation  
---  
      
    
    {
      "oracleSourceConfig": {
        object ([OracleSourceConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#OracleSourceConfig))
      },
      "postgresDestinationConfig": {
        object ([PostgresDestinationConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#PostgresDestinationConfig))
      }
    }  
  
Fields  
---  
`oracleSourceConfig` |  `object (`[OracleSourceConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#OracleSourceConfig)`)` Optional. Configuration for Oracle source.  
`postgresDestinationConfig` |  `object (`[PostgresDestinationConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#PostgresDestinationConfig)`)` Optional. Configuration for Postgres destination.  
  
## OracleSourceConfig

Configuration for Oracle as a source in a migration.

JSON representation  
---  
      
    
    {
      "maxConcurrentFullDumpConnections": integer,
      "maxConcurrentCdcConnections": integer,
      "skipFullDump": boolean,
      "cdcStartPosition": string,
    
      // Union field cdc_method can be only one of the following:
      "logMiner": {
        object ([LogMiner](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#LogMiner))
      },
      "binaryLogParser": {
        object ([BinaryLogParser](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#BinaryLogParser))
      }
      // End of list of possible types for union field cdc_method.
    }  
  
Fields  
---  
`maxConcurrentFullDumpConnections` |  `integer` Optional. Maximum number of connections Database Migration Service will open to the source for full dump phase.  
`maxConcurrentCdcConnections` |  `integer` Optional. Maximum number of connections Database Migration Service will open to the source for CDC phase.  
`skipFullDump` |  `boolean` Optional. Whether to skip full dump or not.  
`cdcStartPosition` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The schema change number (SCN) to start CDC data migration from.  
Union field `cdc_method`. Configuration to select the CDC method. `cdc_method` can be only one of the following:  
`logMiner` |  `object (`[LogMiner](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#LogMiner)`)` Use LogMiner.  
`binaryLogParser` |  `object (`[BinaryLogParser](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#BinaryLogParser)`)` Use Binary Log Parser.  
  
## LogMiner

This type has no fields.

Configuration to use LogMiner CDC method.

## BinaryLogParser

Configuration to use Binary Log Parser CDC technique.

JSON representation  
---  
      
    
    {
    
      // Union field log_file_access can be only one of the following:
      "oracleAsmLogFileAccess": {
        object ([OracleAsmLogFileAccess](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#OracleAsmLogFileAccess))
      },
      "logFileDirectories": {
        object ([LogFileDirectories](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#LogFileDirectories))
      }
      // End of list of possible types for union field log_file_access.
    }  
  
Fields  
---  
Union field `log_file_access`. Configuration to specify how the log file should be accessed. `log_file_access` can be only one of the following:  
`oracleAsmLogFileAccess` |  `object (`[OracleAsmLogFileAccess](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#OracleAsmLogFileAccess)`)` Use Oracle ASM.  
`logFileDirectories` |  `object (`[LogFileDirectories](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#LogFileDirectories)`)` Use Oracle directories.  
  
## OracleAsmLogFileAccess

This type has no fields.

Configuration to use Oracle ASM to access the log files.

## LogFileDirectories

Configuration to specify the Oracle directories to access the log files.

JSON representation  
---  
      
    
    {
      "onlineLogDirectory": string,
      "archivedLogDirectory": string
    }  
  
Fields  
---  
`onlineLogDirectory` |  `string` Required. Oracle directory for online logs.  
`archivedLogDirectory` |  `string` Required. Oracle directory for archived logs.  
  
## PostgresDestinationConfig

Configuration for Postgres as a destination in a migration.

JSON representation  
---  
      
    
    {
      "maxConcurrentConnections": integer,
      "transactionTimeout": string
    }  
  
Fields  
---  
`maxConcurrentConnections` |  `integer` Optional. Maximum number of connections Database Migration Service will open to the destination for data migration.  
`transactionTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Timeout for data migration transactions.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## SqlServerToPostgresConfig

Configuration for heterogeneous **SQL Server to Cloud SQL for PostgreSQL** migrations.

JSON representation  
---  
      
    
    {
      "sqlserverSourceConfig": {
        object ([SqlServerSourceConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SqlServerSourceConfig))
      },
      "postgresDestinationConfig": {
        object ([PostgresDestinationConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#PostgresDestinationConfig))
      }
    }  
  
Fields  
---  
`sqlserverSourceConfig` |  `object (`[SqlServerSourceConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SqlServerSourceConfig)`)` Optional. Configuration for SQL Server source.  
`postgresDestinationConfig` |  `object (`[PostgresDestinationConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#PostgresDestinationConfig)`)` Optional. Configuration for Postgres destination.  
  
## SqlServerSourceConfig

Configuration for SQL Server as a source in a migration.

JSON representation  
---  
      
    
    {
      "maxConcurrentFullDumpConnections": integer,
      "maxConcurrentCdcConnections": integer,
      "skipFullDump": boolean,
      "cdcStartPosition": string
    }  
  
Fields  
---  
`maxConcurrentFullDumpConnections` |  `integer` Optional. Maximum number of connections Database Migration Service will open to the source for full dump phase.  
`maxConcurrentCdcConnections` |  `integer` Optional. Maximum number of connections Database Migration Service will open to the source for CDC phase.  
`skipFullDump` |  `boolean` Optional. Whether to skip full dump or not.  
`cdcStartPosition` |  `string` Optional. The log sequence number (LSN) to start CDC data migration from.  
  
## PostgresToSqlServerConfig

Configuration for heterogeneous failback migrations from **PostgreSQL to SQL Server**.

JSON representation  
---  
      
    
    {
      "postgresSourceConfig": {
        object ([PostgresSourceConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#PostgresSourceConfig))
      },
      "sqlserverDestinationConfig": {
        object ([SqlServerDestinationConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SqlServerDestinationConfig))
      }
    }  
  
Fields  
---  
`postgresSourceConfig` |  `object (`[PostgresSourceConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#PostgresSourceConfig)`)` Optional. Configuration for PostgreSQL source.  
`sqlserverDestinationConfig` |  `object (`[SqlServerDestinationConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SqlServerDestinationConfig)`)` Optional. Configuration for SQL Server destination.  
  
## PostgresSourceConfig

Configuration for Postgres as a source in a migration.

JSON representation  
---  
      
    
    {
      "skipFullDump": boolean
    }  
  
Fields  
---  
`skipFullDump` |  `boolean` Optional. Whether to skip full dump or not.  
  
## SqlServerDestinationConfig

Configuration for SQL Server as a destination in a migration.

JSON representation  
---  
      
    
    {
      "maxConcurrentConnections": integer,
      "transactionTimeout": string
    }  
  
Fields  
---  
`maxConcurrentConnections` |  `integer` Optional. Maximum number of connections Database Migration Service will open to the destination for data migration.  
`transactionTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Timeout for data migration transactions.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## MigrationJobObjectsConfig

Configuration for the objects to be migrated.

JSON representation  
---  
      
    
    {
    
      // Union field migration_job_object_config can be only one of the following:
      "sourceObjectsConfig": {
        object ([SourceObjectsConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SourceObjectsConfig))
      }
      // End of list of possible types for union field migration_job_object_config.
    }  
  
Fields  
---  
Union field `migration_job_object_config`. The config for the objects to be migrated. `migration_job_object_config` can be only one of the following:  
`sourceObjectsConfig` |  `object (`[SourceObjectsConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SourceObjectsConfig)`)` The list of the migration job objects.  
  
## SourceObjectsConfig

List of configurations for the source objects to be migrated.

JSON representation  
---  
      
    
    {
      "objectConfigs": [
        {
          object ([SourceObjectConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SourceObjectConfig))
        }
      ],
      "objectsSelectionType": enum ([ObjectsSelectionType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#ObjectsSelectionType))
    }  
  
Fields  
---  
`objectConfigs[]` |  `object (`[SourceObjectConfig](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#SourceObjectConfig)`)` Optional. The list of the objects to be migrated.  
`objectsSelectionType` |  `enum (`[ObjectsSelectionType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs#ObjectsSelectionType)`)` Optional. The objects selection type of the migration job.  
  
## SourceObjectConfig

Config for a single migration job object.

JSON representation  
---  
      
    
    {
      "objectIdentifier": {
        object ([SourceObjectIdentifier](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/SourceObjectIdentifier))
      }
    }  
  
Fields  
---  
`objectIdentifier` |  `object (`[SourceObjectIdentifier](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/SourceObjectIdentifier)`)` Optional. The object identifier.  
  
## ObjectsSelectionType

The objects selection type of the migration job.

Enums  
---  
`OBJECTS_SELECTION_TYPE_UNSPECIFIED` | The type of the objects selection is unknown, indicating that the migration job is at instance level.  
`ALL_OBJECTS` | Migrate all of the objects.  
`SPECIFIED_OBJECTS` | Migrate specific objects.  
  
## Purpose

The purpose of the migration job.

Enums  
---  
`PURPOSE_UNSPECIFIED` | Unknown purpose. Will be defaulted to MIGRATE.  
`MIGRATE` | Standard migration job.  
`FAILBACK` | Failback replication job.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/create)`

|  Creates a new migration job in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/delete)`

|  Deletes a single migration job.  
  
### `[demoteDestination](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/demoteDestination)`

|  Demotes the destination database to become a read replica of the source.  
  
### `[fetchSourceObjects](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/fetchSourceObjects)`

|  Retrieves objects from the source database that can be selected for data migration.  
  
### `[generateSshScript](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/generateSshScript)`

|  Generate a SSH configuration script to configure the reverse SSH connectivity.  
  
### `[generateTcpProxyScript](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/generateTcpProxyScript)`

|  Generate a TCP Proxy configuration script to configure a cloud-hosted VM running a TCP Proxy.  
  
### `[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/get)`

|  Gets details of a single migration job.  
  
### `[getIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/list)`

|  Lists migration jobs in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/patch)`

|  Updates the parameters of a single migration job.  
  
### `[promote](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/promote)`

|  Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database.  
  
### `[restart](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/restart)`

|  Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch.  
  
### `[resume](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/resume)`

|  Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase).  
  
### `[setIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[start](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/start)`

|  Start an already created migration job.  
  
### `[stop](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/stop)`

|  Stops a running migration job.  
  
### `[testIamPermissions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[verify](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/verify)`

|  Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
