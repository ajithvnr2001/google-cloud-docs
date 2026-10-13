---
url: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases/
title: MCP Tools Reference: oracledatabase.googleapis.com \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:55.272384+00:00
---

# MCP Tools Reference: oracledatabase.googleapis.com  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  MCP Tools Reference: oracledatabase.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_autonomous_databases`

List autonomous databases (ADBs) in a Google Cloud project in the given location.

The following sample demonstrate how to use `curl` to invoke the `list_autonomous_databases` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://oracledatabase.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_autonomous_databases",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

The request for `AutonomousDatabase.List`.

### ListAutonomousDatabasesRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string,
      "filter": string,
      "orderBy": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The parent value for the Autonomous Database in the following format: projects/{project}/locations/{location}.  
`pageSize` |  `integer` Optional. The maximum number of items to return. If unspecified, at most 50 Autonomous Database will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. An expression for filtering the results of the request.  
`orderBy` |  `string` Optional. An expression for ordering the results of the request.  
  
## Output Schema

The response for `AutonomousDatabase.List`.

### ListAutonomousDatabasesResponse

JSON representation  
---  
      
    
    {
      "autonomousDatabases": [
        {
          object ([AutonomousDatabase](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.AutonomousDatabase))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`autonomousDatabases[]` |  `object (`[AutonomousDatabase](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.AutonomousDatabase)`)` The list of Autonomous Databases.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
  
### AutonomousDatabase

JSON representation  
---  
      
    
    {
      "name": string,
      "database": string,
      "displayName": string,
      "entitlementId": string,
      "adminPassword": string,
      "adminPasswordSecretVersion": string,
      "properties": {
        object ([AutonomousDatabaseProperties](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.AutonomousDatabaseProperties))
      },
      "labels": {
        string: string,
        ...
      },
      "network": string,
      "cidr": string,
      "odbNetwork": string,
      "odbSubnet": string,
      "sourceConfig": {
        object ([SourceConfig](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.SourceConfig))
      },
      "peerAutonomousDatabases": [
        string
      ],
      "createTime": string,
      "disasterRecoverySupportedLocations": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the Autonomous Database resource in the following format: projects/{project}/locations/{region}/autonomousDatabases/{autonomous_database}  
`database` |  `string` Optional. Immutable. The name of the Autonomous Database. The database name must be unique in the project. The name must begin with a letter and can contain a maximum of 30 alphanumeric characters.  
`displayName` |  `string` Optional. Immutable. The display name for the Autonomous Database. The name does not have to be unique within your project.  
`entitlementId` |  `string` Output only. The ID of the subscription entitlement associated with the Autonomous Database.  
`adminPassword` |  `string` Optional. Immutable. The password for the default ADMIN user. Note: Only one of `admin_password_secret_version` or `admin_password` can be populated.  
`adminPasswordSecretVersion` |  `string` Optional. Immutable. The resource name of a secret version in Secret Manager which contains the database admin user's password. Format: projects/{project}/secrets/{secret}/versions/{version}. Note: Only one of `admin_password_secret_version` or `admin_password` can be populated.  
`properties` |  `object (`[AutonomousDatabaseProperties](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.AutonomousDatabaseProperties)`)` Optional. The properties of the Autonomous Database.  
`labels` |  `map (key: string, value: string)` Optional. The labels or tags associated with the Autonomous Database.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`network` |  `string` Optional. Immutable. The name of the VPC network used by the Autonomous Database in the following format: projects/{project}/global/networks/{network}  
`cidr` |  `string` Optional. Immutable. The subnet CIDR range for the Autonomous Database.  
`odbNetwork` |  `string` Optional. Immutable. The name of the OdbNetwork associated with the Autonomous Database. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network} It is optional but if specified, this should match the parent ODBNetwork of the OdbSubnet.  
`odbSubnet` |  `string` Optional. Immutable. The name of the OdbSubnet associated with the Autonomous Database. Format: projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}  
`sourceConfig` |  `object (`[SourceConfig](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.SourceConfig)`)` Optional. Immutable. The source Autonomous Database configuration for the standby Autonomous Database. The source Autonomous Database is configured while creating the Peer Autonomous Database and can't be updated after creation.  
`peerAutonomousDatabases[]` |  `string` Output only. The peer Autonomous Database names of the given Autonomous Database.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the Autonomous Database was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`disasterRecoverySupportedLocations[]` |  `string` Output only. List of supported GCP region to clone the Autonomous Database for disaster recovery. Format: `project/{project}/locations/{location}`.  
  
### AutonomousDatabaseProperties

JSON representation  
---  
      
    
    {
      "ocid": string,
      "computeCount": number,
      "cpuCoreCount": integer,
      "dataStorageSizeTb": integer,
      "dataStorageSizeGb": integer,
      "dbWorkload": enum (DBWorkload),
      "dbEdition": enum (DatabaseEdition),
      "characterSet": string,
      "nCharacterSet": string,
      "privateEndpointIp": string,
      "privateEndpointLabel": string,
      "dbVersion": string,
      "isAutoScalingEnabled": boolean,
      "isStorageAutoScalingEnabled": boolean,
      "licenseType": enum (LicenseType),
      "customerContacts": [
        {
          object ([CustomerContact](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.CustomerContact))
        }
      ],
      "secretId": string,
      "vaultId": string,
      "maintenanceScheduleType": enum (MaintenanceScheduleType),
      "mtlsConnectionRequired": boolean,
      "backupRetentionPeriodDays": integer,
      "actualUsedDataStorageSizeTb": number,
      "allocatedStorageSizeTb": number,
      "apexDetails": {
        object ([AutonomousDatabaseApex](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.AutonomousDatabaseApex))
      },
      "lifecycleDetails": string,
      "state": enum (State),
      "autonomousContainerDatabaseId": string,
      "availableUpgradeVersions": [
        string
      ],
      "connectionStrings": {
        object ([AutonomousDatabaseConnectionStrings](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.AutonomousDatabaseConnectionStrings))
      },
      "connectionUrls": {
        object ([AutonomousDatabaseConnectionUrls](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.AutonomousDatabaseConnectionUrls))
      },
      "failedDataRecoveryDuration": string,
      "memoryTableGbs": integer,
      "isLocalDataGuardEnabled": boolean,
      "localAdgAutoFailoverMaxDataLossLimit": integer,
      "localStandbyDb": {
        object ([AutonomousDatabaseStandbySummary](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.AutonomousDatabaseStandbySummary))
      },
      "memoryPerOracleComputeUnitGbs": integer,
      "localDisasterRecoveryType": enum (LocalDisasterRecoveryType),
      "dataSafeState": enum (DataSafeState),
      "databaseManagementState": enum (DatabaseManagementState),
      "openMode": enum (OpenMode),
      "operationsInsightsState": enum (OperationsInsightsState),
      "peerDbIds": [
        string
      ],
      "permissionLevel": enum (PermissionLevel),
      "privateEndpoint": string,
      "refreshableMode": enum (RefreshableMode),
      "refreshableState": enum (RefreshableState),
      "role": enum (Role),
      "scheduledOperationDetails": [
        {
          object ([ScheduledOperationDetails](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.ScheduledOperationDetails))
        }
      ],
      "sqlWebDeveloperUrl": string,
      "supportedCloneRegions": [
        string
      ],
      "usedDataStorageSizeTbs": integer,
      "ociUrl": string,
      "totalAutoBackupStorageSizeGbs": number,
      "nextLongTermBackupTime": string,
      "dataGuardRoleChangedTime": string,
      "disasterRecoveryRoleChangedTime": string,
      "maintenanceBeginTime": string,
      "maintenanceEndTime": string,
      "allowlistedIps": [
        string
      ],
      "encryptionKey": {
        object ([EncryptionKey](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.EncryptionKey))
      },
      "encryptionKeyHistoryEntries": [
        {
          object ([EncryptionKeyHistoryEntry](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.EncryptionKeyHistoryEntry))
        }
      ],
      "serviceAgentEmail": string,
    
      // Union field _are_primary_allowlisted_ips_used can be only one of the
      // following:
      "arePrimaryAllowlistedIpsUsed": boolean
      // End of list of possible types for union field
      // _are_primary_allowlisted_ips_used.
    
      // Union field _local_data_guard_enabled can be only one of the following:
      "localDataGuardEnabled": boolean
      // End of list of possible types for union field _local_data_guard_enabled.
    
      // Union field _local_adg_auto_failover_max_data_loss_limit_duration can be
      // only one of the following:
      "localAdgAutoFailoverMaxDataLossLimitDuration": integer
      // End of list of possible types for union field
      // _local_adg_auto_failover_max_data_loss_limit_duration.
    }  
  
Fields  
---  
`ocid` |  `string` Output only. OCID of the Autonomous Database. <https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Oracle>  
`computeCount` |  `number` Optional. Immutable. The number of compute servers for the Autonomous Database.  
`cpuCoreCount` |  `integer` Optional. Immutable. The number of CPU cores to be made available to the database.  
`dataStorageSizeTb` |  `integer` Optional. Immutable. The size of the data stored in the database, in terabytes.  
`dataStorageSizeGb` |  `integer` Optional. Immutable. The size of the data stored in the database, in gigabytes.  
`dbWorkload` |  `enum (`DBWorkload`)` Required. Immutable. The workload type of the Autonomous Database.  
`dbEdition` |  `enum (`DatabaseEdition`)` Optional. Immutable. The edition of the Autonomous Databases.  
`characterSet` |  `string` Optional. Immutable. The character set for the Autonomous Database. The default is AL32UTF8.  
`nCharacterSet` |  `string` Optional. Immutable. The national character set for the Autonomous Database. The default is AL16UTF16.  
`privateEndpointIp` |  `string` Optional. Immutable. The private endpoint IP address for the Autonomous Database.  
`privateEndpointLabel` |  `string` Optional. Immutable. The private endpoint label for the Autonomous Database.  
`dbVersion` |  `string` Optional. Immutable. The Oracle Database version for the Autonomous Database.  
`isAutoScalingEnabled` |  `boolean` Optional. Immutable. This field indicates if auto scaling is enabled for the Autonomous Database CPU core count.  
`isStorageAutoScalingEnabled` |  `boolean` Optional. Immutable. This field indicates if auto scaling is enabled for the Autonomous Database storage.  
`licenseType` |  `enum (`LicenseType`)` Required. Immutable. The license type used for the Autonomous Database.  
`customerContacts[]` |  `object (`[CustomerContact](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.CustomerContact)`)` Optional. Immutable. The list of customer contacts.  
`secretId` |  `string` Optional. Immutable. The ID of the Oracle Cloud Infrastructure vault secret.  
`vaultId` |  `string` Optional. Immutable. The ID of the Oracle Cloud Infrastructure vault.  
`maintenanceScheduleType` |  `enum (`MaintenanceScheduleType`)` Optional. Immutable. The maintenance schedule of the Autonomous Database.  
`mtlsConnectionRequired` |  `boolean` Optional. Immutable. This field specifies if the Autonomous Database requires mTLS connections.  
`backupRetentionPeriodDays` |  `integer` Optional. Immutable. The retention period for the Autonomous Database. This field is specified in days, can range from 1 day to 60 days, and has a default value of 60 days.  
`actualUsedDataStorageSizeTb` |  `number` Output only. The amount of storage currently being used for user and system data, in terabytes.  
`allocatedStorageSizeTb` |  `number` Output only. The amount of storage currently allocated for the database tables and billed for, rounded up in terabytes.  
`apexDetails` |  `object (`[AutonomousDatabaseApex](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.AutonomousDatabaseApex)`)` Output only. The details for the Oracle APEX Application Development.  
`lifecycleDetails` |  `string` Output only. The details of the current lifestyle state of the Autonomous Database.  
`state` |  `enum (`State`)` Output only. The current lifecycle state of the Autonomous Database.  
`autonomousContainerDatabaseId` |  `string` Output only. The Autonomous Container Database OCID.  
`availableUpgradeVersions[]` |  `string` Output only. The list of available Oracle Database upgrade versions for an Autonomous Database.  
`connectionStrings` |  `object (`[AutonomousDatabaseConnectionStrings](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.AutonomousDatabaseConnectionStrings)`)` Output only. The connection strings used to connect to an Autonomous Database.  
`connectionUrls` |  `object (`[AutonomousDatabaseConnectionUrls](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.AutonomousDatabaseConnectionUrls)`)` Output only. The Oracle Connection URLs for an Autonomous Database.  
`failedDataRecoveryDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. This field indicates the number of seconds of data loss during a Data Guard failover.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`memoryTableGbs` |  `integer` Output only. The memory assigned to in-memory tables in an Autonomous Database.  
`isLocalDataGuardEnabled  
**(deprecated)**` |  `boolean` This item is deprecated!Output only. Deprecated: Please use `local_data_guard_enabled` instead. This field indicates whether the Autonomous Database has local (in-region) Data Guard enabled.  
`localAdgAutoFailoverMaxDataLossLimit  
**(deprecated)**` |  `integer` This item is deprecated!Output only. Deprecated: Please use `local_adg_auto_failover_max_data_loss_limit_duration` instead. This field indicates the maximum data loss limit for an Autonomous Database, in seconds.  
`localStandbyDb` |  `object (`[AutonomousDatabaseStandbySummary](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.AutonomousDatabaseStandbySummary)`)` Output only. The details of the Autonomous Data Guard standby database.  
`memoryPerOracleComputeUnitGbs` |  `integer` Output only. The amount of memory enabled per ECPU, in gigabytes.  
`localDisasterRecoveryType` |  `enum (`LocalDisasterRecoveryType`)` Output only. This field indicates the local disaster recovery (DR) type of an Autonomous Database.  
`dataSafeState` |  `enum (`DataSafeState`)` Output only. The current state of the Data Safe registration for the Autonomous Database.  
`databaseManagementState` |  `enum (`DatabaseManagementState`)` Output only. The current state of database management for the Autonomous Database.  
`openMode` |  `enum (`OpenMode`)` Output only. This field indicates the current mode of the Autonomous Database.  
`operationsInsightsState` |  `enum (`OperationsInsightsState`)` Output only. This field indicates the state of Operations Insights for the Autonomous Database.  
`peerDbIds[]` |  `string` Output only. The list of OCIDs of standby databases located in Autonomous Data Guard remote regions that are associated with the source database.  
`permissionLevel` |  `enum (`PermissionLevel`)` Output only. The permission level of the Autonomous Database.  
`privateEndpoint` |  `string` Output only. The private endpoint for the Autonomous Database.  
`refreshableMode` |  `enum (`RefreshableMode`)` Output only. The refresh mode of the cloned Autonomous Database.  
`refreshableState` |  `enum (`RefreshableState`)` Output only. The refresh State of the clone.  
`role` |  `enum (`Role`)` Output only. The Data Guard role of the Autonomous Database.  
`scheduledOperationDetails[]` |  `object (`[ScheduledOperationDetails](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.ScheduledOperationDetails)`)` Output only. The list and details of the scheduled operations of the Autonomous Database.  
`sqlWebDeveloperUrl` |  `string` Output only. The SQL Web Developer URL for the Autonomous Database.  
`supportedCloneRegions[]` |  `string` Output only. The list of available regions that can be used to create a clone for the Autonomous Database.  
`usedDataStorageSizeTbs` |  `integer` Output only. The storage space used by Autonomous Database, in gigabytes.  
`ociUrl` |  `string` Output only. The Oracle Cloud Infrastructure link for the Autonomous Database.  
`totalAutoBackupStorageSizeGbs` |  `number` Output only. The storage space used by automatic backups of Autonomous Database, in gigabytes.  
`nextLongTermBackupTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The long term backup schedule of the Autonomous Database.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`dataGuardRoleChangedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time the Autonomous Data Guard role was changed for the standby Autonomous Database.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`disasterRecoveryRoleChangedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time the Disaster Recovery role was changed for the standby Autonomous Database.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`maintenanceBeginTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time when maintenance will begin.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`maintenanceEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time when maintenance will end.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`allowlistedIps[]` |  `string` Optional. Immutable. The list of allowlisted IP addresses for the Autonomous Database.  
`encryptionKey` |  `object (`[EncryptionKey](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.EncryptionKey)`)` Optional. The encryption key used to encrypt the Autonomous Database. Updating this field will add a new entry in the `encryption_key_history_entries` field with the former version.  
`encryptionKeyHistoryEntries[]` |  `object (`[EncryptionKeyHistoryEntry](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.EncryptionKeyHistoryEntry)`)` Output only. The history of the encryption keys used to encrypt the Autonomous Database.  
`serviceAgentEmail` |  `string` Output only. An Oracle-managed Google Cloud service account on which customers can grant roles to access resources in the customer project.  
Union field `_are_primary_allowlisted_ips_used`.`_are_primary_allowlisted_ips_used` can be only one of the following:  
`arePrimaryAllowlistedIpsUsed` |  `boolean` Output only. This field indicates the status of Data Guard and Access control for the Autonomous Database. The field's value is null if Data Guard is disabled or Access Control is disabled. The field's value is TRUE if both Data Guard and Access Control are enabled, and the Autonomous Database is using primary IP access control list (ACL) for standby. The field's value is FALSE if both Data Guard and Access Control are enabled, and the Autonomous Database is using a different IP access control list (ACL) for standby compared to primary.  
Union field `_local_data_guard_enabled`.`_local_data_guard_enabled` can be only one of the following:  
`localDataGuardEnabled` |  `boolean` Optional. Indicates whether the Autonomous Database has a local (in-region) standby database. Not applicable to cross-region Data Guard or dedicated Exadata infrastructure.  
Union field `_local_adg_auto_failover_max_data_loss_limit_duration`.`_local_adg_auto_failover_max_data_loss_limit_duration` can be only one of the following:  
`localAdgAutoFailoverMaxDataLossLimitDuration` |  `integer` Optional. This field indicates the maximum data loss limit for an Autonomous Database, in seconds.  
  
### CustomerContact

JSON representation  
---  
      
    
    {
      "email": string
    }  
  
Fields  
---  
`email` |  `string` Required. The email address used by Oracle to send notifications regarding databases and infrastructure.  
  
### AutonomousDatabaseApex

JSON representation  
---  
      
    
    {
      "apexVersion": string,
      "ordsVersion": string
    }  
  
Fields  
---  
`apexVersion` |  `string` Output only. The Oracle APEX Application Development version.  
`ordsVersion` |  `string` Output only. The Oracle REST Data Services (ORDS) version.  
  
### AutonomousDatabaseConnectionStrings

JSON representation  
---  
      
    
    {
      "allConnectionStrings": {
        object ([AllConnectionStrings](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.AllConnectionStrings))
      },
      "dedicated": string,
      "high": string,
      "low": string,
      "medium": string,
      "profiles": [
        {
          object ([DatabaseConnectionStringProfile](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.DatabaseConnectionStringProfile))
        }
      ]
    }  
  
Fields  
---  
`allConnectionStrings` |  `object (`[AllConnectionStrings](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.AllConnectionStrings)`)` Output only. Returns all connection strings that can be used to connect to the Autonomous Database.  
`dedicated` |  `string` Output only. The database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL statements.  
`high` |  `string` Output only. The database service provides the highest level of resources to each SQL statement.  
`low` |  `string` Output only. The database service provides the least level of resources to each SQL statement.  
`medium` |  `string` Output only. The database service provides a lower level of resources to each SQL statement.  
`profiles[]` |  `object (`[DatabaseConnectionStringProfile](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.DatabaseConnectionStringProfile)`)` Output only. A list of connection string profiles to allow clients to group, filter, and select values based on the structured metadata.  
  
### AllConnectionStrings

JSON representation  
---  
      
    
    {
      "high": string,
      "low": string,
      "medium": string
    }  
  
Fields  
---  
`high` |  `string` Output only. The database service provides the highest level of resources to each SQL statement.  
`low` |  `string` Output only. The database service provides the least level of resources to each SQL statement.  
`medium` |  `string` Output only. The database service provides a lower level of resources to each SQL statement.  
  
### DatabaseConnectionStringProfile

JSON representation  
---  
      
    
    {
      "consumerGroup": enum (ConsumerGroup),
      "displayName": string,
      "hostFormat": enum (HostFormat),
      "isRegional": boolean,
      "protocol": enum (Protocol),
      "sessionMode": enum (SessionMode),
      "syntaxFormat": enum (SyntaxFormat),
      "tlsAuthentication": enum (TLSAuthentication),
      "value": string
    }  
  
Fields  
---  
`consumerGroup` |  `enum (`ConsumerGroup`)` Output only. The current consumer group being used by the connection.  
`displayName` |  `string` Output only. The display name for the database connection.  
`hostFormat` |  `enum (`HostFormat`)` Output only. The host name format being currently used in connection string.  
`isRegional` |  `boolean` Output only. This field indicates if the connection string is regional and is only applicable for cross-region Data Guard.  
`protocol` |  `enum (`Protocol`)` Output only. The protocol being used by the connection.  
`sessionMode` |  `enum (`SessionMode`)` Output only. The current session mode of the connection.  
`syntaxFormat` |  `enum (`SyntaxFormat`)` Output only. The syntax of the connection string.  
`tlsAuthentication` |  `enum (`TLSAuthentication`)` Output only. This field indicates the TLS authentication type of the connection.  
`value` |  `string` Output only. The value of the connection string.  
  
### AutonomousDatabaseConnectionUrls

JSON representation  
---  
      
    
    {
      "apexUri": string,
      "databaseTransformsUri": string,
      "graphStudioUri": string,
      "machineLearningNotebookUri": string,
      "machineLearningUserManagementUri": string,
      "mongoDbUri": string,
      "ordsUri": string,
      "sqlDevWebUri": string
    }  
  
Fields  
---  
`apexUri` |  `string` Output only. Oracle Application Express (APEX) URL.  
`databaseTransformsUri` |  `string` Output only. The URL of the Database Transforms for the Autonomous Database.  
`graphStudioUri` |  `string` Output only. The URL of the Graph Studio for the Autonomous Database.  
`machineLearningNotebookUri` |  `string` Output only. The URL of the Oracle Machine Learning (OML) Notebook for the Autonomous Database.  
`machineLearningUserManagementUri` |  `string` Output only. The URL of Machine Learning user management the Autonomous Database.  
`mongoDbUri` |  `string` Output only. The URL of the MongoDB API for the Autonomous Database.  
`ordsUri` |  `string` Output only. The Oracle REST Data Services (ORDS) URL of the Web Access for the Autonomous Database.  
`sqlDevWebUri` |  `string` Output only. The URL of the Oracle SQL Developer Web for the Autonomous Database.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### AutonomousDatabaseStandbySummary

JSON representation  
---  
      
    
    {
      "lagTimeDuration": string,
      "lifecycleDetails": string,
      "state": enum (State),
      "dataGuardRoleChangedTime": string,
      "disasterRecoveryRoleChangedTime": string
    }  
  
Fields  
---  
`lagTimeDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The amount of time, in seconds, that the data of the standby database lags in comparison to the data of the primary database.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`lifecycleDetails` |  `string` Output only. The additional details about the current lifecycle state of the Autonomous Database.  
`state` |  `enum (`State`)` Output only. The current lifecycle state of the Autonomous Database.  
`dataGuardRoleChangedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time the Autonomous Data Guard role was switched for the standby Autonomous Database.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`disasterRecoveryRoleChangedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time the Disaster Recovery role was switched for the standby Autonomous Database.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
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
  
### ScheduledOperationDetails

JSON representation  
---  
      
    
    {
      "dayOfWeek": enum (google.type.DayOfWeek),
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.TimeOfDay))
      },
      "stopTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.TimeOfDay))
      }
    }  
  
Fields  
---  
`dayOfWeek` |  `enum (`google.type.DayOfWeek`)` Output only. Day of week.  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.TimeOfDay)`)` Output only. Auto start time.  
`stopTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.TimeOfDay)`)` Output only. Auto stop time.  
  
### TimeOfDay

JSON representation  
---  
      
    
    {
      "hours": integer,
      "minutes": integer,
      "seconds": integer,
      "nanos": integer
    }  
  
Fields  
---  
`hours` |  `integer` Hours of a day in 24 hour format. Must be greater than or equal to 0 and typically must be less than or equal to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`minutes` |  `integer` Minutes of an hour. Must be greater than or equal to 0 and less than or equal to 59.  
`seconds` |  `integer` Seconds of a minute. Must be greater than or equal to 0 and typically must be less than or equal to 59. An API may allow the value 60 if it allows leap-seconds.  
`nanos` |  `integer` Fractions of seconds, in nanoseconds. Must be greater than or equal to 0 and less than or equal to 999,999,999.  
  
### EncryptionKey

JSON representation  
---  
      
    
    {
      "provider": enum (Provider),
      "kmsKey": string
    }  
  
Fields  
---  
`provider` |  `enum (`Provider`)` Optional. The provider of the encryption key.  
`kmsKey` |  `string` Optional. The KMS key used to encrypt the Autonomous Database. This field is required if the provider is GOOGLE_MANAGED. The name of the KMS key resource in the following format: `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`.  
  
### EncryptionKeyHistoryEntry

JSON representation  
---  
      
    
    {
      "encryptionKey": {
        object ([EncryptionKey](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.EncryptionKey))
      },
      "activationTime": string
    }  
  
Fields  
---  
`encryptionKey` |  `object (`[EncryptionKey](https://docs.cloud.google.com/oracle/database/docs/reference/mcp/tools_list/list_autonomous_databases#Output.Schema.EncryptionKey)`)` Output only. The encryption key used to encrypt the Autonomous Database.  
`activationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time when the encryption key was activated on the Autonomous Database..Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
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
  
### SourceConfig

JSON representation  
---  
      
    
    {
      "autonomousDatabase": string,
      "automaticBackupsReplicationEnabled": boolean
    }  
  
Fields  
---  
`autonomousDatabase` |  `string` Optional. The name of the primary Autonomous Database that is used to create a Peer Autonomous Database from a source.  
`automaticBackupsReplicationEnabled` |  `boolean` Optional. This field specifies if the replication of automatic backups is enabled when creating a Data Guard.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-17 UTC."],[],[]] 
