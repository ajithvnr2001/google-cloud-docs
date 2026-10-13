---
url: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system/
title: MCP Tools Reference: oracledatabase.googleapis.com \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:52.365086+00:00
---

# MCP Tools Reference: oracledatabase.googleapis.com  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  MCP Tools Reference: oracledatabase.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_db_system`

Get details for a Db system in a Google Cloud project in the given location.

The following sample demonstrate how to use `curl` to invoke the `get_db_system` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://oracledatabase.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_db_system",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request for `DbSystem.Get`.

### GetDbSystemRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the DbSystem in the following format: projects/{project}/locations/{location}/dbSystems/{db_system}.  
  
## Output Schema

Details of the DbSystem (BaseDB) resource. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/DbSystem/>

### DbSystem

JSON representation  
---  
      
    
    {
      "name": string,
      "properties": {
        object ([DbSystemProperties](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.DbSystemProperties))
      },
      "gcpOracleZone": string,
      "labels": {
        string: string,
        ...
      },
      "odbNetwork": string,
      "odbSubnet": string,
      "entitlementId": string,
      "displayName": string,
      "createTime": string,
      "ociUrl": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the DbSystem resource in the following format: projects/{project}/locations/{region}/dbSystems/{db_system}  
`properties` |  `object (`[DbSystemProperties](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.DbSystemProperties)`)` Optional. The properties of the DbSystem.  
`gcpOracleZone` |  `string` Optional. The GCP Oracle zone where Oracle DbSystem is hosted. Example: us-east4-b-r2. If not specified, the system will pick a zone based on availability.  
`labels` |  `map (key: string, value: string)` Optional. The labels or tags associated with the DbSystem.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`odbNetwork` |  `string` Optional. The name of the OdbNetwork associated with the DbSystem. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network} It is optional but if specified, this should match the parent ODBNetwork of the OdbSubnet.  
`odbSubnet` |  `string` Required. The name of the OdbSubnet associated with the DbSystem for IP allocation. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}  
`entitlementId` |  `string` Output only. The ID of the subscription entitlement associated with the DbSystem  
`displayName` |  `string` Required. The display name for the System db. The name does not have to be unique within your project.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the DbSystem was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`ociUrl` |  `string` Output only. HTTPS link to OCI resources exposed to Customer via UI Interface.  
  
### DbSystemProperties

JSON representation  
---  
      
    
    {
      "shape": string,
      "computeCount": integer,
      "initialDataStorageSizeGb": integer,
      "databaseEdition": enum (DbSystemDatabaseEdition),
      "licenseModel": enum (LicenseModel),
      "sshPublicKeys": [
        string
      ],
      "hostnamePrefix": string,
      "hostname": string,
      "privateIp": string,
      "dataCollectionOptions": {
        object ([DataCollectionOptionsDbSystem](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.DataCollectionOptionsDbSystem))
      },
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_cloud_vm_cluster#Input.Schema.TimeZone))
      },
      "lifecycleState": enum (DbSystemLifecycleState),
      "dbHome": {
        object ([DbHome](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.DbHome))
      },
      "ocid": string,
      "memorySizeGb": integer,
      "computeModel": enum (ComputeModel),
      "dataStorageSizeGb": integer,
      "recoStorageSizeGb": integer,
      "domain": string,
      "nodeCount": integer,
      "dbSystemOptions": {
        object ([DbSystemOptions](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.DbSystemOptions))
      }
    }  
  
Fields  
---  
`shape` |  `string` Required. Shape of DB System.  
`computeCount` |  `integer` Required. The number of CPU cores to enable for the DbSystem.  
`initialDataStorageSizeGb` |  `integer` Required. The initial data storage size in GB.  
`databaseEdition` |  `enum (`DbSystemDatabaseEdition`)` Required. The database edition of the DbSystem.  
`licenseModel` |  `enum (`LicenseModel`)` Required. The license model of the DbSystem.  
`sshPublicKeys[]` |  `string` Required. SSH public keys to be stored with the DbSystem.  
`hostnamePrefix` |  `string` Optional. Prefix for DB System host names.  
`hostname` |  `string` Output only. The hostname of the DbSystem.  
`privateIp` |  `string` Optional. The private IP address of the DbSystem.  
`dataCollectionOptions` |  `object (`[DataCollectionOptionsDbSystem](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.DataCollectionOptionsDbSystem)`)` Optional. Data collection options for diagnostics.  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/create_cloud_vm_cluster#Input.Schema.TimeZone)`)` Optional. Time zone of the DbSystem.  
`lifecycleState` |  `enum (`DbSystemLifecycleState`)` Output only. State of the DbSystem.  
`dbHome` |  `object (`[DbHome](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.DbHome)`)` Optional. Details for creating a Database Home.  
`ocid` |  `string` Output only. OCID of the DbSystem.  
`memorySizeGb` |  `integer` Optional. The memory size in GB.  
`computeModel` |  `enum (`ComputeModel`)` Optional. The compute model of the DbSystem.  
`dataStorageSizeGb` |  `integer` Optional. The data storage size in GB that is currently available to DbSystems.  
`recoStorageSizeGb` |  `integer` Optional. The reco/redo storage size in GB.  
`domain` |  `string` Optional. The host domain name of the DbSystem.  
`nodeCount` |  `integer` Optional. The number of nodes in the DbSystem.  
`dbSystemOptions` |  `object (`[DbSystemOptions](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.DbSystemOptions)`)` Optional. The options for the DbSystem.  
  
### DataCollectionOptionsDbSystem

JSON representation  
---  
      
    
    {
      "isDiagnosticsEventsEnabled": boolean,
      "isIncidentLogsEnabled": boolean
    }  
  
Fields  
---  
`isDiagnosticsEventsEnabled` |  `boolean` Optional. Indicates whether to enable data collection for diagnostics.  
`isIncidentLogsEnabled` |  `boolean` Optional. Indicates whether to enable incident logs and trace collection.  
  
### TimeZone

JSON representation  
---  
      
    
    {
      "id": string,
      "version": string
    }  
  
Fields  
---  
`id` |  `string` IANA Time Zone Database time zone. For example "America/New_York".  
`version` |  `string` Optional. IANA Time Zone Database version number. For example "2019a".  
  
### DbHome

JSON representation  
---  
      
    
    {
      "displayName": string,
      "dbVersion": string,
      "database": {
        object ([Database](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.Database))
      },
      "isUnifiedAuditingEnabled": boolean
    }  
  
Fields  
---  
`displayName` |  `string` Optional. The display name for the Database Home. The name does not have to be unique within your project.  
`dbVersion` |  `string` Required. A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation.  
`database` |  `object (`[Database](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.Database)`)` Required. The Database resource.  
`isUnifiedAuditingEnabled` |  `boolean` Optional. Whether unified auditing is enabled for the Database Home.  
  
### Database

JSON representation  
---  
      
    
    {
      "name": string,
      "dbName": string,
      "dbUniqueName": string,
      "adminPassword": string,
      "adminPasswordSecretVersion": string,
      "tdeWalletPassword": string,
      "tdeWalletPasswordSecretVersion": string,
      "characterSet": string,
      "ncharacterSet": string,
      "ociUrl": string,
      "createTime": string,
      "properties": {
        object ([DatabaseProperties](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.DatabaseProperties))
      },
      "databaseId": string,
      "dbHomeName": string,
      "gcpOracleZone": string,
      "opsInsightsStatus": enum (OperationsInsightsStatus),
      "pluggableDatabaseId": string,
      "pluggableDatabaseName": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the Database resource in the following format: projects/{project}/locations/{region}/databases/{database}  
`dbName` |  `string` Optional. The database name. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.  
`dbUniqueName` |  `string` Optional. The DB_UNIQUE_NAME of the Oracle Database being backed up.  
`adminPassword` |  `string` Optional. The password for the default ADMIN user. Note: Only one of `admin_password_secret_version` or `admin_password` can be populated.  
`adminPasswordSecretVersion` |  `string` Optional. The resource name of a secret version in Secret Manager which contains the database admin user's password. Format: projects/{project}/secrets/{secret}/versions/{version}. Note: Only one of `admin_password_secret_version` or `admin_password` can be populated.  
`tdeWalletPassword` |  `string` Optional. The TDE wallet password for the database. Note: Only one of `tde_wallet_password_secret_version` or `tde_wallet_password` can be populated.  
`tdeWalletPasswordSecretVersion` |  `string` Optional. The resource name of a secret version in Secret Manager which contains the TDE wallet password for the database. Format: projects/{project}/secrets/{secret}/versions/{version}. Note: Only one of `tde_wallet_password_secret_version` or `tde_wallet_password` can be populated.  
`characterSet` |  `string` Optional. The character set for the database. The default is AL32UTF8.  
`ncharacterSet` |  `string` Optional. The national character set for the database. The default is AL16UTF16.  
`ociUrl` |  `string` Output only. HTTPS link to OCI resources exposed to Customer via UI Interface.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the Database was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`properties` |  `object (`[DatabaseProperties](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.DatabaseProperties)`)` Optional. The properties of the Database.  
`databaseId` |  `string` Optional. The database ID of the Database.  
`dbHomeName` |  `string` Optional. The name of the DbHome resource associated with the Database.  
`gcpOracleZone` |  `string` Output only. The GCP Oracle zone where the Database is created.  
`opsInsightsStatus` |  `enum (`OperationsInsightsStatus`)` Output only. The Status of Operations Insights for this Database.  
`pluggableDatabaseId` |  `string` Optional. The ID of the pluggable database associated with the Database. The ID must be unique within the project and location.  
`pluggableDatabaseName` |  `string` Optional. The pluggable database associated with the Database. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### DatabaseProperties

JSON representation  
---  
      
    
    {
      "state": enum (DatabaseLifecycleState),
      "dbVersion": string,
      "dbBackupConfig": {
        object ([DbBackupConfig](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.DbBackupConfig))
      },
      "databaseManagementConfig": {
        object ([DatabaseManagementConfig](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.DatabaseManagementConfig))
      }
    }  
  
Fields  
---  
`state` |  `enum (`DatabaseLifecycleState`)` Output only. State of the Database.  
`dbVersion` |  `string` Required. The Oracle Database version.  
`dbBackupConfig` |  `object (`[DbBackupConfig](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.DbBackupConfig)`)` Optional. Backup options for the Database.  
`databaseManagementConfig` |  `object (`[DatabaseManagementConfig](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.DatabaseManagementConfig)`)` Output only. The Database Management config.  
  
### DbBackupConfig

JSON representation  
---  
      
    
    {
      "autoBackupEnabled": boolean,
      "backupDestinationDetails": [
        {
          object ([BackupDestinationDetails](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.BackupDestinationDetails))
        }
      ],
      "retentionPeriodDays": integer,
      "backupDeletionPolicy": enum (BackupDeletionPolicy),
      "autoFullBackupDay": enum (google.type.DayOfWeek),
      "autoFullBackupWindow": enum (BackupWindow),
      "autoIncrementalBackupWindow": enum (BackupWindow)
    }  
  
Fields  
---  
`autoBackupEnabled` |  `boolean` Optional. If set to true, enables automatic backups on the database.  
`backupDestinationDetails[]` |  `object (`[BackupDestinationDetails](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/get_db_system#Output.Schema.BackupDestinationDetails)`)` Optional. Details of the database backup destinations.  
`retentionPeriodDays` |  `integer` Optional. The number of days an automatic backup is retained before being automatically deleted. This value determines the earliest point in time to which a database can be restored. Min: 1, Max: 60.  
`backupDeletionPolicy` |  `enum (`BackupDeletionPolicy`)` Optional. This defines when the backups will be deleted after Database termination.  
`autoFullBackupDay` |  `enum (`google.type.DayOfWeek`)` Optional. The day of the week on which the full backup should be performed on the database. If no value is provided, it will default to Sunday.  
`autoFullBackupWindow` |  `enum (`BackupWindow`)` Optional. The window in which the full backup should be performed on the database. If no value is provided, the default is anytime.  
`autoIncrementalBackupWindow` |  `enum (`BackupWindow`)` Optional. The window in which the incremental backup should be performed on the database. If no value is provided, the default is anytime except the auto full backup day.  
  
### BackupDestinationDetails

JSON representation  
---  
      
    
    {
      "type": enum (BackupDestinationType)
    }  
  
Fields  
---  
`type` |  `enum (`BackupDestinationType`)` Optional. The type of the database backup destination.  
  
### DatabaseManagementConfig

JSON representation  
---  
      
    
    {
      "managementState": enum (ManagementState),
      "managementType": enum (ManagementType)
    }  
  
Fields  
---  
`managementState` |  `enum (`ManagementState`)` Output only. The status of the Database Management service.  
`managementType` |  `enum (`ManagementType`)` Output only. The Database Management type.  
  
### DbSystemOptions

JSON representation  
---  
      
    
    {
      "storageManagement": enum (StorageManagement)
    }  
  
Fields  
---  
`storageManagement` |  `enum (`StorageManagement`)` Optional. The storage option used in DB system.  
  
### LabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-17 UTC."],[],[]] 
