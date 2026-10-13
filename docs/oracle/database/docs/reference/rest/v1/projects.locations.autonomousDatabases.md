---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases
title: REST Resource: projects.locations.autonomousDatabases \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:40.401696+00:00
---

# REST Resource: projects.locations.autonomousDatabases  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.autonomousDatabases Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AutonomousDatabase
    * JSON representation
  * AutonomousDatabaseProperties
    * JSON representation
  * DatabaseEdition
  * LicenseType
  * MaintenanceScheduleType
  * AutonomousDatabaseApex
    * JSON representation
  * State
  * AutonomousDatabaseConnectionStrings
    * JSON representation
  * AllConnectionStrings
    * JSON representation
  * DatabaseConnectionStringProfile
    * JSON representation
  * ConsumerGroup
  * HostFormat
  * Protocol
  * SessionMode
  * SyntaxFormat
  * TLSAuthentication
  * AutonomousDatabaseConnectionUrls
    * JSON representation
  * AutonomousDatabaseStandbySummary
    * JSON representation
  * LocalDisasterRecoveryType
  * DataSafeState
  * DatabaseManagementState
  * OpenMode
  * OperationsInsightsState
  * PermissionLevel
  * RefreshableMode
  * RefreshableState
  * Role
  * ScheduledOperationDetails
    * JSON representation
  * TimeOfDay
    * JSON representation
  * EncryptionKey
    * JSON representation
  * Provider
  * EncryptionKeyHistoryEntry
    * JSON representation
  * SourceConfig
    * JSON representation
  * SourceType
  * CloneType
  * RefreshableMode
  * Methods



## Resource: AutonomousDatabase

Details of the Autonomous Database resource. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabase/>

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
        object ([AutonomousDatabaseProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#AutonomousDatabaseProperties))
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
        object ([SourceConfig](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#SourceConfig))
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
`name` |  `string` Identifier. The name of the Autonomous Database resource in the following format: projects/{project}/locations/{region}/autonomousDatabases/{autonomousDatabase}  
`database` |  `string` Optional. Immutable. The name of the Autonomous Database. The database name must be unique in the project. The name must begin with a letter and can contain a maximum of 30 alphanumeric characters.  
`displayName` |  `string` Optional. Immutable. The display name for the Autonomous Database. The name does not have to be unique within your project.  
`entitlementId` |  `string` Output only. The ID of the subscription entitlement associated with the Autonomous Database.  
`adminPassword` |  `string` Optional. Immutable. The password for the default ADMIN user. Note: Only one of `adminPasswordSecretVersion` or `adminPassword` can be populated.  
`adminPasswordSecretVersion` |  `string` Optional. Immutable. The resource name of a secret version in Secret Manager which contains the database admin user's password. Format: projects/{project}/secrets/{secret}/versions/{version}. Note: Only one of `adminPasswordSecretVersion` or `adminPassword` can be populated.  
`properties` |  `object (`[AutonomousDatabaseProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#AutonomousDatabaseProperties)`)` Optional. The properties of the Autonomous Database.  
`labels` |  `map (key: string, value: string)` Optional. The labels or tags associated with the Autonomous Database.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`network` |  `string` Optional. Immutable. The name of the VPC network used by the Autonomous Database in the following format: projects/{project}/global/networks/{network}  
`cidr` |  `string` Optional. Immutable. The subnet CIDR range for the Autonomous Database.  
`odbNetwork` |  `string` Optional. Immutable. The name of the OdbNetwork associated with the Autonomous Database. Format: projects/{project}/locations/{location}/odbNetworks/{odbNetwork} It is optional but if specified, this should match the parent ODBNetwork of the OdbSubnet.  
`odbSubnet` |  `string` Optional. Immutable. The name of the OdbSubnet associated with the Autonomous Database. Format: projects/{project}/locations/{location}/odbNetworks/{odbNetwork}/odbSubnets/{odbSubnet}  
`sourceConfig` |  `object (`[SourceConfig](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#SourceConfig)`)` Optional. Immutable. The source Autonomous Database configuration for the standby Autonomous Database. The source Autonomous Database is configured while creating the Peer Autonomous Database and can't be updated after creation.  
`peerAutonomousDatabases[]` |  `string` Output only. The peer Autonomous Database names of the given Autonomous Database.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the Autonomous Database was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`disasterRecoverySupportedLocations[]` |  `string` Output only. List of supported GCP region to clone the Autonomous Database for disaster recovery. Format: `project/{project}/locations/{location}`.  
  
## AutonomousDatabaseProperties

The properties of an Autonomous Database.

JSON representation  
---  
      
    
    {
      "ocid": string,
      "computeCount": number,
      "cpuCoreCount": integer,
      "dataStorageSizeTb": integer,
      "dataStorageSizeGb": integer,
      "dbWorkload": enum ([DBWorkload](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DBWorkload)),
      "dbEdition": enum ([DatabaseEdition](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#DatabaseEdition)),
      "characterSet": string,
      "nCharacterSet": string,
      "privateEndpointIp": string,
      "privateEndpointLabel": string,
      "dbVersion": string,
      "isAutoScalingEnabled": boolean,
      "isStorageAutoScalingEnabled": boolean,
      "licenseType": enum ([LicenseType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#LicenseType)),
      "customerContacts": [
        {
          object ([CustomerContact](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/CustomerContact))
        }
      ],
      "secretId": string,
      "vaultId": string,
      "maintenanceScheduleType": enum ([MaintenanceScheduleType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#MaintenanceScheduleType)),
      "mtlsConnectionRequired": boolean,
      "backupRetentionPeriodDays": integer,
      "actualUsedDataStorageSizeTb": number,
      "allocatedStorageSizeTb": number,
      "apexDetails": {
        object ([AutonomousDatabaseApex](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#AutonomousDatabaseApex))
      },
      "lifecycleDetails": string,
      "state": enum ([State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#State)),
      "autonomousContainerDatabaseId": string,
      "availableUpgradeVersions": [
        string
      ],
      "connectionStrings": {
        object ([AutonomousDatabaseConnectionStrings](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#AutonomousDatabaseConnectionStrings))
      },
      "connectionUrls": {
        object ([AutonomousDatabaseConnectionUrls](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#AutonomousDatabaseConnectionUrls))
      },
      "failedDataRecoveryDuration": string,
      "memoryTableGbs": integer,
      "isLocalDataGuardEnabled": boolean,
      "localAdgAutoFailoverMaxDataLossLimit": integer,
      "localStandbyDb": {
        object ([AutonomousDatabaseStandbySummary](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#AutonomousDatabaseStandbySummary))
      },
      "memoryPerOracleComputeUnitGbs": integer,
      "localDisasterRecoveryType": enum ([LocalDisasterRecoveryType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#LocalDisasterRecoveryType)),
      "dataSafeState": enum ([DataSafeState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#DataSafeState)),
      "databaseManagementState": enum ([DatabaseManagementState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#DatabaseManagementState)),
      "openMode": enum ([OpenMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#OpenMode)),
      "operationsInsightsState": enum ([OperationsInsightsState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#OperationsInsightsState)),
      "peerDbIds": [
        string
      ],
      "permissionLevel": enum ([PermissionLevel](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#PermissionLevel)),
      "privateEndpoint": string,
      "refreshableMode": enum ([RefreshableMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#RefreshableMode)),
      "refreshableState": enum ([RefreshableState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#RefreshableState)),
      "role": enum ([Role](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#Role)),
      "scheduledOperationDetails": [
        {
          object ([ScheduledOperationDetails](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#ScheduledOperationDetails))
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
        object ([EncryptionKey](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#EncryptionKey))
      },
      "encryptionKeyHistoryEntries": [
        {
          object ([EncryptionKeyHistoryEntry](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#EncryptionKeyHistoryEntry))
        }
      ],
      "serviceAgentEmail": string,
      "arePrimaryAllowlistedIpsUsed": boolean,
      "localDataGuardEnabled": boolean,
      "localAdgAutoFailoverMaxDataLossLimitDuration": integer,
      "refreshableClone": boolean
    }  
  
Fields  
---  
`ocid` |  `string` Output only. OCID of the Autonomous Database. <https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Oracle>  
`computeCount` |  `number` Optional. Immutable. The number of compute servers for the Autonomous Database.  
`cpuCoreCount` |  `integer` Optional. Immutable. The number of CPU cores to be made available to the database.  
`dataStorageSizeTb` |  `integer` Optional. Immutable. The size of the data stored in the database, in terabytes.  
`dataStorageSizeGb` |  `integer` Optional. Immutable. The size of the data stored in the database, in gigabytes.  
`dbWorkload` |  `enum (`[DBWorkload](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DBWorkload)`)` Required. Immutable. The workload type of the Autonomous Database.  
`dbEdition` |  `enum (`[DatabaseEdition](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#DatabaseEdition)`)` Optional. Immutable. The edition of the Autonomous Databases.  
`characterSet` |  `string` Optional. Immutable. The character set for the Autonomous Database. The default is AL32UTF8.  
`nCharacterSet` |  `string` Optional. Immutable. The national character set for the Autonomous Database. The default is AL16UTF16.  
`privateEndpointIp` |  `string` Optional. Immutable. The private endpoint IP address for the Autonomous Database.  
`privateEndpointLabel` |  `string` Optional. Immutable. The private endpoint label for the Autonomous Database.  
`dbVersion` |  `string` Optional. Immutable. The Oracle Database version for the Autonomous Database.  
`isAutoScalingEnabled` |  `boolean` Optional. Immutable. This field indicates if auto scaling is enabled for the Autonomous Database CPU core count.  
`isStorageAutoScalingEnabled` |  `boolean` Optional. Immutable. This field indicates if auto scaling is enabled for the Autonomous Database storage.  
`licenseType` |  `enum (`[LicenseType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#LicenseType)`)` Required. Immutable. The license type used for the Autonomous Database.  
`customerContacts[]` |  `object (`[CustomerContact](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/CustomerContact)`)` Optional. Immutable. The list of customer contacts.  
`secretId` |  `string` Optional. Immutable. The ID of the Oracle Cloud Infrastructure vault secret.  
`vaultId` |  `string` Optional. Immutable. The ID of the Oracle Cloud Infrastructure vault.  
`maintenanceScheduleType` |  `enum (`[MaintenanceScheduleType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#MaintenanceScheduleType)`)` Optional. Immutable. The maintenance schedule of the Autonomous Database.  
`mtlsConnectionRequired` |  `boolean` Optional. Immutable. This field specifies if the Autonomous Database requires mTLS connections.  
`backupRetentionPeriodDays` |  `integer` Optional. Immutable. The retention period for the Autonomous Database. This field is specified in days, can range from 1 day to 60 days, and has a default value of 60 days.  
`actualUsedDataStorageSizeTb` |  `number` Output only. The amount of storage currently being used for user and system data, in terabytes.  
`allocatedStorageSizeTb` |  `number` Output only. The amount of storage currently allocated for the database tables and billed for, rounded up in terabytes.  
`apexDetails` |  `object (`[AutonomousDatabaseApex](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#AutonomousDatabaseApex)`)` Output only. The details for the Oracle APEX Application Development.  
`lifecycleDetails` |  `string` Output only. The details of the current lifestyle state of the Autonomous Database.  
`state` |  `enum (`[State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#State)`)` Output only. The current lifecycle state of the Autonomous Database.  
`autonomousContainerDatabaseId` |  `string` Output only. The Autonomous Container Database OCID.  
`availableUpgradeVersions[]` |  `string` Output only. The list of available Oracle Database upgrade versions for an Autonomous Database.  
`connectionStrings` |  `object (`[AutonomousDatabaseConnectionStrings](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#AutonomousDatabaseConnectionStrings)`)` Output only. The connection strings used to connect to an Autonomous Database.  
`connectionUrls` |  `object (`[AutonomousDatabaseConnectionUrls](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#AutonomousDatabaseConnectionUrls)`)` Output only. The Oracle Connection URLs for an Autonomous Database.  
`failedDataRecoveryDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. This field indicates the number of seconds of data loss during a Data Guard failover.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`memoryTableGbs` |  `integer` Output only. The memory assigned to in-memory tables in an Autonomous Database.  
`isLocalDataGuardEnabled  
**(deprecated)**` |  `boolean` This item is deprecated!Output only. Deprecated: Please use `localDataGuardEnabled` instead. This field indicates whether the Autonomous Database has local (in-region) Data Guard enabled.  
`localAdgAutoFailoverMaxDataLossLimit  
**(deprecated)**` |  `integer` This item is deprecated!Output only. Deprecated: Please use `localAdgAutoFailoverMaxDataLossLimitDuration` instead. This field indicates the maximum data loss limit for an Autonomous Database, in seconds.  
`localStandbyDb` |  `object (`[AutonomousDatabaseStandbySummary](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#AutonomousDatabaseStandbySummary)`)` Output only. The details of the Autonomous Data Guard standby database.  
`memoryPerOracleComputeUnitGbs` |  `integer` Output only. The amount of memory enabled per ECPU, in gigabytes.  
`localDisasterRecoveryType` |  `enum (`[LocalDisasterRecoveryType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#LocalDisasterRecoveryType)`)` Output only. This field indicates the local disaster recovery (DR) type of an Autonomous Database.  
`dataSafeState` |  `enum (`[DataSafeState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#DataSafeState)`)` Output only. The current state of the Data Safe registration for the Autonomous Database.  
`databaseManagementState` |  `enum (`[DatabaseManagementState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#DatabaseManagementState)`)` Output only. The current state of database management for the Autonomous Database.  
`openMode` |  `enum (`[OpenMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#OpenMode)`)` Output only. This field indicates the current mode of the Autonomous Database.  
`operationsInsightsState` |  `enum (`[OperationsInsightsState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#OperationsInsightsState)`)` Output only. This field indicates the state of Operations Insights for the Autonomous Database.  
`peerDbIds[]` |  `string` Output only. The list of OCIDs of standby databases located in Autonomous Data Guard remote regions that are associated with the source database.  
`permissionLevel` |  `enum (`[PermissionLevel](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#PermissionLevel)`)` Output only. The permission level of the Autonomous Database.  
`privateEndpoint` |  `string` Output only. The private endpoint for the Autonomous Database.  
`refreshableMode` |  `enum (`[RefreshableMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#RefreshableMode)`)` Output only. The refresh mode of the cloned Autonomous Database.  
`refreshableState` |  `enum (`[RefreshableState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#RefreshableState)`)` Output only. The refresh State of the clone.  
`role` |  `enum (`[Role](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#Role)`)` Output only. The Data Guard role of the Autonomous Database.  
`scheduledOperationDetails[]` |  `object (`[ScheduledOperationDetails](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#ScheduledOperationDetails)`)` Output only. The list and details of the scheduled operations of the Autonomous Database.  
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
`encryptionKey` |  `object (`[EncryptionKey](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#EncryptionKey)`)` Optional. The encryption key used to encrypt the Autonomous Database. Updating this field will add a new entry in the `encryptionKeyHistoryEntries` field with the former version.  
`encryptionKeyHistoryEntries[]` |  `object (`[EncryptionKeyHistoryEntry](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#EncryptionKeyHistoryEntry)`)` Output only. The history of the encryption keys used to encrypt the Autonomous Database.  
`serviceAgentEmail` |  `string` Output only. An Oracle-managed Google Cloud service account on which customers can grant roles to access resources in the customer project.  
`arePrimaryAllowlistedIpsUsed` |  `boolean` Output only. This field indicates the status of Data Guard and Access control for the Autonomous Database. The field's value is null if Data Guard is disabled or Access Control is disabled. The field's value is TRUE if both Data Guard and Access Control are enabled, and the Autonomous Database is using primary IP access control list (ACL) for standby. The field's value is FALSE if both Data Guard and Access Control are enabled, and the Autonomous Database is using a different IP access control list (ACL) for standby compared to primary.  
`localDataGuardEnabled` |  `boolean` Optional. Indicates whether the Autonomous Database has a local (in-region) standby database. Not applicable to cross-region Data Guard or dedicated Exadata infrastructure.  
`localAdgAutoFailoverMaxDataLossLimitDuration` |  `integer` Optional. This field indicates the maximum data loss limit for an Autonomous Database, in seconds.  
`refreshableClone` |  `boolean` Optional. Indicates if the Autonomous Database is a refreshable clone. This field is used in update flow to connect / disconnect a refreshable clone from its source database.  
  
## DatabaseEdition

The editions available for the Autonomous Database.

Enums  
---  
`DATABASE_EDITION_UNSPECIFIED` | Default unspecified value.  
`STANDARD_EDITION` | Standard Database Edition  
`ENTERPRISE_EDITION` | Enterprise Database Edition  
  
## LicenseType

The license types available for the Autonomous Database.

Enums  
---  
`LICENSE_TYPE_UNSPECIFIED` | Unspecified  
`LICENSE_INCLUDED` | License included part of offer  
`BRING_YOUR_OWN_LICENSE` | Bring your own license  
  
## MaintenanceScheduleType

The available maintenance schedules for the Autonomous Database.

Enums  
---  
`MAINTENANCE_SCHEDULE_TYPE_UNSPECIFIED` | Default unspecified value.  
`EARLY` | An EARLY maintenance schedule patches the database before the regular scheduled maintenance.  
`REGULAR` | A REGULAR maintenance schedule follows the normal maintenance cycle.  
  
## AutonomousDatabaseApex

Oracle APEX Application Development. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/AutonomousDatabaseApex>

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
  
## State

The various lifecycle states of the Autonomous Database.

Enums  
---  
`STATE_UNSPECIFIED` | Default unspecified value.  
`PROVISIONING` | Indicates that the Autonomous Database is in provisioning state.  
`AVAILABLE` | Indicates that the Autonomous Database is in available state.  
`STOPPING` | Indicates that the Autonomous Database is in stopping state.  
`STOPPED` | Indicates that the Autonomous Database is in stopped state.  
`STARTING` | Indicates that the Autonomous Database is in starting state.  
`TERMINATING` | Indicates that the Autonomous Database is in terminating state.  
`TERMINATED` | Indicates that the Autonomous Database is in terminated state.  
`UNAVAILABLE` | Indicates that the Autonomous Database is in unavailable state.  
`RESTORE_IN_PROGRESS` | Indicates that the Autonomous Database restore is in progress.  
`RESTORE_FAILED` | Indicates that the Autonomous Database failed to restore.  
`BACKUP_IN_PROGRESS` | Indicates that the Autonomous Database backup is in progress.  
`SCALE_IN_PROGRESS` | Indicates that the Autonomous Database scale is in progress.  
`AVAILABLE_NEEDS_ATTENTION` | Indicates that the Autonomous Database is available but needs attention state.  
`UPDATING` | Indicates that the Autonomous Database is in updating state.  
`MAINTENANCE_IN_PROGRESS` | Indicates that the Autonomous Database's maintenance is in progress state.  
`RESTARTING` | Indicates that the Autonomous Database is in restarting state.  
`RECREATING` | Indicates that the Autonomous Database is in recreating state.  
`ROLE_CHANGE_IN_PROGRESS` | Indicates that the Autonomous Database's role change is in progress state.  
`UPGRADING` | Indicates that the Autonomous Database is in upgrading state.  
`INACCESSIBLE` | Indicates that the Autonomous Database is in inaccessible state.  
`STANDBY` | Indicates that the Autonomous Database is in standby state.  
  
## AutonomousDatabaseConnectionStrings

The connection string used to connect to the Autonomous Database. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/AutonomousDatabaseConnectionStrings>

JSON representation  
---  
      
    
    {
      "allConnectionStrings": {
        object ([AllConnectionStrings](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#AllConnectionStrings))
      },
      "dedicated": string,
      "high": string,
      "low": string,
      "medium": string,
      "profiles": [
        {
          object ([DatabaseConnectionStringProfile](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#DatabaseConnectionStringProfile))
        }
      ]
    }  
  
Fields  
---  
`allConnectionStrings` |  `object (`[AllConnectionStrings](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#AllConnectionStrings)`)` Output only. Returns all connection strings that can be used to connect to the Autonomous Database.  
`dedicated` |  `string` Output only. The database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL statements.  
`high` |  `string` Output only. The database service provides the highest level of resources to each SQL statement.  
`low` |  `string` Output only. The database service provides the least level of resources to each SQL statement.  
`medium` |  `string` Output only. The database service provides a lower level of resources to each SQL statement.  
`profiles[]` |  `object (`[DatabaseConnectionStringProfile](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#DatabaseConnectionStringProfile)`)` Output only. A list of connection string profiles to allow clients to group, filter, and select values based on the structured metadata.  
  
## AllConnectionStrings

A list of all connection strings that can be used to connect to the Autonomous Database.

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
  
## DatabaseConnectionStringProfile

The connection string profile to allow clients to group. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/DatabaseConnectionStringProfile>

JSON representation  
---  
      
    
    {
      "consumerGroup": enum ([ConsumerGroup](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#ConsumerGroup)),
      "displayName": string,
      "hostFormat": enum ([HostFormat](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#HostFormat)),
      "isRegional": boolean,
      "protocol": enum ([Protocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#Protocol)),
      "sessionMode": enum ([SessionMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#SessionMode)),
      "syntaxFormat": enum ([SyntaxFormat](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#SyntaxFormat)),
      "tlsAuthentication": enum ([TLSAuthentication](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#TLSAuthentication)),
      "value": string
    }  
  
Fields  
---  
`consumerGroup` |  `enum (`[ConsumerGroup](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#ConsumerGroup)`)` Output only. The current consumer group being used by the connection.  
`displayName` |  `string` Output only. The display name for the database connection.  
`hostFormat` |  `enum (`[HostFormat](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#HostFormat)`)` Output only. The host name format being currently used in connection string.  
`isRegional` |  `boolean` Output only. This field indicates if the connection string is regional and is only applicable for cross-region Data Guard.  
`protocol` |  `enum (`[Protocol](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#Protocol)`)` Output only. The protocol being used by the connection.  
`sessionMode` |  `enum (`[SessionMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#SessionMode)`)` Output only. The current session mode of the connection.  
`syntaxFormat` |  `enum (`[SyntaxFormat](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#SyntaxFormat)`)` Output only. The syntax of the connection string.  
`tlsAuthentication` |  `enum (`[TLSAuthentication](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#TLSAuthentication)`)` Output only. This field indicates the TLS authentication type of the connection.  
`value` |  `string` Output only. The value of the connection string.  
  
## ConsumerGroup

The various consumer groups available in the connection string profile.

Enums  
---  
`CONSUMER_GROUP_UNSPECIFIED` | Default unspecified value.  
`HIGH` | High consumer group.  
`MEDIUM` | Medium consumer group.  
`LOW` | Low consumer group.  
`TP` | TP consumer group.  
`TPURGENT` | TPURGENT consumer group.  
  
## HostFormat

The host name format being used in the connection string.

Enums  
---  
`HOST_FORMAT_UNSPECIFIED` | Default unspecified value.  
`FQDN` | FQDN  
`IP` | IP  
  
## Protocol

The protocol being used by the connection.

Enums  
---  
`PROTOCOL_UNSPECIFIED` | Default unspecified value.  
`TCP` | Tcp  
`TCPS` | Tcps  
  
## SessionMode

The session mode of the connection.

Enums  
---  
`SESSION_MODE_UNSPECIFIED` | Default unspecified value.  
`DIRECT` | Direct  
`INDIRECT` | Indirect  
  
## SyntaxFormat

Specifies syntax of the connection string.

Enums  
---  
`SYNTAX_FORMAT_UNSPECIFIED` | Default unspecified value.  
`LONG` | Long  
`EZCONNECT` | Ezconnect  
`EZCONNECTPLUS` | Ezconnectplus  
  
## TLSAuthentication

This field indicates the TLS authentication type of the connection.

Enums  
---  
`TLS_AUTHENTICATION_UNSPECIFIED` | Default unspecified value.  
`SERVER` | Server  
`MUTUAL` | Mutual  
  
## AutonomousDatabaseConnectionUrls

The URLs for accessing Oracle Application Express (APEX) and SQL Developer Web with a browser from a Compute instance. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/AutonomousDatabaseConnectionUrls>

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
  
## AutonomousDatabaseStandbySummary

Autonomous Data Guard standby database details. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/AutonomousDatabaseStandbySummary>

JSON representation  
---  
      
    
    {
      "lagTimeDuration": string,
      "lifecycleDetails": string,
      "state": enum ([State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#State)),
      "dataGuardRoleChangedTime": string,
      "disasterRecoveryRoleChangedTime": string
    }  
  
Fields  
---  
`lagTimeDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The amount of time, in seconds, that the data of the standby database lags in comparison to the data of the primary database.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`lifecycleDetails` |  `string` Output only. The additional details about the current lifecycle state of the Autonomous Database.  
`state` |  `enum (`[State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#State)`)` Output only. The current lifecycle state of the Autonomous Database.  
`dataGuardRoleChangedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time the Autonomous Data Guard role was switched for the standby Autonomous Database.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`disasterRecoveryRoleChangedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time the Disaster Recovery role was switched for the standby Autonomous Database.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## LocalDisasterRecoveryType

The types of local disaster recovery available for an Autonomous Database.

Enums  
---  
`LOCAL_DISASTER_RECOVERY_TYPE_UNSPECIFIED` | Default unspecified value.  
`ADG` | Autonomous Data Guard recovery.  
`BACKUP_BASED` | Backup based recovery.  
`NOT_AVAILABLE` | Local disaster recovery is not available.  
  
## DataSafeState

Varies states of the Data Safe registration for the Autonomous Database.

Enums  
---  
`DATA_SAFE_STATE_UNSPECIFIED` | Default unspecified value.  
`REGISTERING` | Registering data safe state.  
`REGISTERED` | Registered data safe state.  
`DEREGISTERING` | Deregistering data safe state.  
`NOT_REGISTERED` | Not registered data safe state.  
`FAILED` | Failed data safe state.  
  
## DatabaseManagementState

The different states of database management for an Autonomous Database.

Enums  
---  
`DATABASE_MANAGEMENT_STATE_UNSPECIFIED` | Default unspecified value.  
`ENABLING` | Enabling Database Management state  
`ENABLED` | Enabled Database Management state  
`DISABLING` | Disabling Database Management state  
`NOT_ENABLED` | Not Enabled Database Management state  
`FAILED_ENABLING` | Failed enabling Database Management state  
`FAILED_DISABLING` | Failed disabling Database Management state  
  
## OpenMode

This field indicates the modes of an Autonomous Database.

Enums  
---  
`OPEN_MODE_UNSPECIFIED` | Default unspecified value.  
`READ_ONLY` | Read Only Mode  
`READ_WRITE` | Read Write Mode  
  
## OperationsInsightsState

The state of the Operations Insights for this Autonomous Database.

Enums  
---  
`OPERATIONS_INSIGHTS_STATE_UNSPECIFIED` | Default unspecified value.  
`ENABLING` | Enabling status for operation insights.  
`ENABLED` | Enabled status for operation insights.  
`DISABLING` | Disabling status for operation insights.  
`NOT_ENABLED` | Not Enabled status for operation insights.  
`FAILED_ENABLING` | Failed enabling status for operation insights.  
`FAILED_DISABLING` | Failed disabling status for operation insights.  
  
## PermissionLevel

The types of permission levels for an Autonomous Database.

Enums  
---  
`PERMISSION_LEVEL_UNSPECIFIED` | Default unspecified value.  
`RESTRICTED` | Restricted mode allows access only by admin users.  
`UNRESTRICTED` | Normal access.  
  
## RefreshableMode

The refresh mode of the cloned Autonomous Database.

Enums  
---  
`REFRESHABLE_MODE_UNSPECIFIED` | The default unspecified value.  
`AUTOMATIC` | AUTOMATIC indicates that the cloned database is automatically refreshed with data from the source Autonomous Database.  
`MANUAL` | MANUAL indicates that the cloned database is manually refreshed with data from the source Autonomous Database.  
  
## RefreshableState

The refresh state of the cloned Autonomous Database.

Enums  
---  
`REFRESHABLE_STATE_UNSPECIFIED` | Default unspecified value.  
`REFRESHING` | Refreshing  
`NOT_REFRESHING` | Not refreshed  
  
## Role

The Data Guard role of the Autonomous Database.

Enums  
---  
`ROLE_UNSPECIFIED` | Default unspecified value.  
`PRIMARY` | Primary role  
`STANDBY` | Standby role  
`DISABLED_STANDBY` | Disabled standby role  
`BACKUP_COPY` | Backup copy role  
`SNAPSHOT_STANDBY` | Snapshot standby role  
  
## ScheduledOperationDetails

Details of scheduled operation. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/datatypes/ScheduledOperationDetails>

JSON representation  
---  
      
    
    {
      "dayOfWeek": enum ([DayOfWeek](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DayOfWeek)),
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#TimeOfDay))
      },
      "stopTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#TimeOfDay))
      }
    }  
  
Fields  
---  
`dayOfWeek` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DayOfWeek)`)` Output only. Day of week.  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#TimeOfDay)`)` Output only. Auto start time.  
`stopTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#TimeOfDay)`)` Output only. Auto stop time.  
  
## TimeOfDay

Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are `google.type.Date` and `google.protobuf.Timestamp`.

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
  
## EncryptionKey

The encryption key used to encrypt the Autonomous Database.

JSON representation  
---  
      
    
    {
      "provider": enum ([Provider](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#Provider)),
      "kmsKey": string
    }  
  
Fields  
---  
`provider` |  `enum (`[Provider](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#Provider)`)` Optional. The provider of the encryption key.  
`kmsKey` |  `string` Optional. The KMS key used to encrypt the Autonomous Database. This field is required if the provider is GOOGLE_MANAGED. The name of the KMS key resource in the following format: `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`.  
  
## Provider

The provider of the encryption key.

Enums  
---  
`PROVIDER_UNSPECIFIED` | Default unspecified value.  
`GOOGLE_MANAGED` | Google Managed KMS key, if selected, please provide the KMS key name.  
`ORACLE_MANAGED` | Oracle Managed.  
  
## EncryptionKeyHistoryEntry

The history of the encryption keys used to encrypt the Autonomous Database.

JSON representation  
---  
      
    
    {
      "encryptionKey": {
        object ([EncryptionKey](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#EncryptionKey))
      },
      "activationTime": string
    }  
  
Fields  
---  
`encryptionKey` |  `object (`[EncryptionKey](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#EncryptionKey)`)` Output only. The encryption key used to encrypt the Autonomous Database.  
`activationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time when the encryption key was activated on the Autonomous Database..Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## SourceConfig

The source configuration for the standby Autonomous Database.

JSON representation  
---  
      
    
    {
      "autonomousDatabase": string,
      "automaticBackupsReplicationEnabled": boolean,
      "sourceType": enum ([SourceType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#SourceType)),
      "cloneType": enum ([CloneType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#CloneType)),
      "refreshableMode": enum ([RefreshableMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#RefreshableMode_1)),
      "autoRefreshFrequencySeconds": integer,
      "autoRefreshStartTime": string,
      "autonomousDatabaseBackup": string,
      "backupTime": string,
      "useLatestAvailableBackup": boolean,
      "autoRefreshPointLagSeconds": integer
    }  
  
Fields  
---  
`autonomousDatabase` |  `string` Optional. The name of the primary Autonomous Database that is used to create a Peer Autonomous Database from a source.  
`automaticBackupsReplicationEnabled` |  `boolean` Optional. This field specifies if the replication of automatic backups is enabled when creating a Data Guard.  
`sourceType` |  `enum (`[SourceType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#SourceType)`)` Optional. The source type of the Autonomous Database.  
`cloneType` |  `enum (`[CloneType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#CloneType)`)` Optional. The clone type of the Autonomous Database. This field is only applicable in case of cloning  
`refreshableMode` |  `enum (`[RefreshableMode](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases#RefreshableMode_1)`)` Optional. The refresh mode of the clone.  
`autoRefreshFrequencySeconds` |  `integer` Optional. The frequency in seconds a refreshable clone is refreshed after auto-refresh is enabled.  
`autoRefreshStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The date and time that auto-refreshing will begin for an Autonomous Database refreshable clone. This value controls only the start time for the first refresh operation.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`autonomousDatabaseBackup` |  `string` Optional. The name of the Autonomous Database Backup resource with the format: projects/{project}/locations/{region}/autonomousDatabaseBackups/{autonomousDatabaseBackup} Required when sourceType is BACKUP_FROM_ID.  
`backupTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The timestamp specified for the point-in-time clone of the source Autonomous Database. This field is only applicable in case of BACKUP_FROM_TIMESTAMP source type and when useLatestAvailableBackup is false.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`useLatestAvailableBackup` |  `boolean` Optional. Clone from latest available backup timestamp. This field is only applicable in case of BACKUP_FROM_TIMESTAMP source type.  
`autoRefreshPointLagSeconds` |  `integer` Optional. The time, in seconds, the data of the automatic refreshable clone lags the primary database at the point of refresh.  
  
## SourceType

Specifies the source of the database. For example, a clone or peer from an existing database. This enum may be expanded to include other source types in the future.

Enums  
---  
`SOURCE_TYPE_UNSPECIFIED` | Default unspecified value.  
`CLONE_DATABASE` | Clone database from an existing database specified in autonomousDatabase field.  
`CROSS_REGION_DISASTER_RECOVERY` | Create a cross-region disaster recovery peer adb from an existing adb.  
`CLONE_TO_REFRESHABLE` | Create a refreshable clone from an existing database specified in autonomousDatabase field.  
`BACKUP_FROM_ID` | Create clone from the backup resource.  
`BACKUP_FROM_TIMESTAMP` | Create clone from backup specified by backupTime field, or use latest available backup if useLatestAvailableBackup is true. The autonomousDatabase field must specify the source database to clone from.  
  
## CloneType

The clone type of the Autonomous Database.

Enums  
---  
`CLONE_TYPE_UNSPECIFIED` | Default unspecified value.  
`FULL` | Creates a new database with the source database's data and metadata.  
`METADATA` | Creates a new database that includes all the source database schema metadata, but none of the source database data.  
  
## RefreshableMode

The refresh mode of a refreshable clone.

Enums  
---  
`REFRESHABLE_MODE_UNSPECIFIED` | Default unspecified value.  
`AUTOMATIC` | Automatic refresh.  
`MANUAL` | Manual refresh.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/create)`

|  Creates a new Autonomous Database in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/delete)`

|  Deletes a single Autonomous Database.  
  
### `[failover](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/failover)`

|  Initiates a failover to target autonomous database from the associated primary database.  
  
### `[generateWallet](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/generateWallet)`

|  Generates a wallet for an Autonomous Database.  
  
### `[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/get)`

|  Gets the details of a single Autonomous Database.  
  
### `[getRefreshableClones](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/getRefreshableClones)`

|  Gets the refreshable clones for a given Autonomous Database.  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/list)`

|  Lists the Autonomous Databases in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/patch)`

|  Updates the parameters of a single Autonomous Database.  
  
### `[refresh](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/refresh)`

|  Refreshes the refreshable clone of an Autonomous Database.  
  
### `[restart](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/restart)`

|  Restarts an Autonomous Database.  
  
### `[restore](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/restore)`

|  Restores a single Autonomous Database.  
  
### `[start](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/start)`

|  Starts an Autonomous Database.  
  
### `[stop](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/stop)`

|  Stops an Autonomous Database.  
  
### `[switchover](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/switchover)`

|  Initiates a switchover of specified autonomous database to the associated peer database.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
