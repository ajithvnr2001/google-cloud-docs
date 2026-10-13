---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases
title: REST Resource: projects.locations.databases \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:42.728277+00:00
---

# REST Resource: projects.locations.databases  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.databases Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Database
    * JSON representation
    * DatabaseProperties
      * JSON representation
    * DatabaseLifecycleState
    * DbBackupConfig
      * JSON representation
    * BackupDestinationDetails
      * JSON representation
    * BackupDestinationType
    * BackupDeletionPolicy
    * BackupWindow
    * OperationsInsightsStatus
  * Methods



## Resource: Database

Details of the Database resource. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/Database/>

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
        object ([DatabaseProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.DatabaseProperties))
      },
      "databaseId": string,
      "dbHomeName": string,
      "gcpOracleZone": string,
      "opsInsightsStatus": enum ([OperationsInsightsStatus](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.OperationsInsightsStatus)),
      "pluggableDatabaseId": string,
      "pluggableDatabaseName": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the Database resource in the following format: projects/{project}/locations/{region}/databases/{database}  
`dbName` |  `string` Optional. The database name. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.  
`dbUniqueName` |  `string` Optional. The DB_UNIQUE_NAME of the Oracle Database being backed up.  
`adminPassword` |  `string` Optional. The password for the default ADMIN user. Note: Only one of `adminPasswordSecretVersion` or `adminPassword` can be populated.  
`adminPasswordSecretVersion` |  `string` Optional. The resource name of a secret version in Secret Manager which contains the database admin user's password. Format: projects/{project}/secrets/{secret}/versions/{version}. Note: Only one of `adminPasswordSecretVersion` or `adminPassword` can be populated.  
`tdeWalletPassword` |  `string` Optional. The TDE wallet password for the database. Note: Only one of `tdeWalletPasswordSecretVersion` or `tdeWalletPassword` can be populated.  
`tdeWalletPasswordSecretVersion` |  `string` Optional. The resource name of a secret version in Secret Manager which contains the TDE wallet password for the database. Format: projects/{project}/secrets/{secret}/versions/{version}. Note: Only one of `tdeWalletPasswordSecretVersion` or `tdeWalletPassword` can be populated.  
`characterSet` |  `string` Optional. The character set for the database. The default is AL32UTF8.  
`ncharacterSet` |  `string` Optional. The national character set for the database. The default is AL16UTF16.  
`ociUrl` |  `string` Output only. HTTPS link to OCI resources exposed to Customer via UI Interface.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time that the Database was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`properties` |  `object (`[DatabaseProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.DatabaseProperties)`)` Optional. The properties of the Database.  
`databaseId` |  `string` Optional. The database ID of the Database.  
`dbHomeName` |  `string` Optional. The name of the DbHome resource associated with the Database.  
`gcpOracleZone` |  `string` Output only. The GCP Oracle zone where the Database is created.  
`opsInsightsStatus` |  `enum (`[OperationsInsightsStatus](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.OperationsInsightsStatus)`)` Output only. The Status of Operations Insights for this Database.  
`pluggableDatabaseId` |  `string` Optional. The ID of the pluggable database associated with the Database. The ID must be unique within the project and location.  
`pluggableDatabaseName` |  `string` Optional. The pluggable database associated with the Database. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters.  
  
### DatabaseProperties

The properties of a Database.

JSON representation  
---  
      
    
    {
      "state": enum ([DatabaseLifecycleState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.DatabaseLifecycleState)),
      "dbVersion": string,
      "dbBackupConfig": {
        object ([DbBackupConfig](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.DbBackupConfig))
      },
      "databaseManagementConfig": {
        object ([DatabaseManagementConfig](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DatabaseManagementConfig))
      }
    }  
  
Fields  
---  
`state` |  `enum (`[DatabaseLifecycleState](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.DatabaseLifecycleState)`)` Output only. State of the Database.  
`dbVersion` |  `string` Required. The Oracle Database version.  
`dbBackupConfig` |  `object (`[DbBackupConfig](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.DbBackupConfig)`)` Optional. Backup options for the Database.  
`databaseManagementConfig` |  `object (`[DatabaseManagementConfig](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DatabaseManagementConfig)`)` Output only. The Database Management config.  
  
### DatabaseLifecycleState

The various lifecycle states of the Database.

Enums  
---  
`DATABASE_LIFECYCLE_STATE_UNSPECIFIED` | Default unspecified value.  
`PROVISIONING` | Indicates that the resource is in provisioning state.  
`AVAILABLE` | Indicates that the resource is in available state.  
`UPDATING` | Indicates that the resource is in updating state.  
`BACKUP_IN_PROGRESS` | Indicates that the resource is in backup in progress state.  
`UPGRADING` | Indicates that the resource is in upgrading state.  
`CONVERTING` | Indicates that the resource is in converting state.  
`TERMINATING` | Indicates that the resource is in terminating state.  
`TERMINATED` | Indicates that the resource is in terminated state.  
`RESTORE_FAILED` | Indicates that the resource is in restore failed state.  
`FAILED` | Indicates that the resource is in failed state.  
  
### DbBackupConfig

Backup Options for the Database.

JSON representation  
---  
      
    
    {
      "autoBackupEnabled": boolean,
      "backupDestinationDetails": [
        {
          object ([BackupDestinationDetails](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.BackupDestinationDetails))
        }
      ],
      "retentionPeriodDays": integer,
      "backupDeletionPolicy": enum ([BackupDeletionPolicy](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.BackupDeletionPolicy)),
      "autoFullBackupDay": enum ([DayOfWeek](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DayOfWeek)),
      "autoFullBackupWindow": enum ([BackupWindow](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.BackupWindow)),
      "autoIncrementalBackupWindow": enum ([BackupWindow](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.BackupWindow))
    }  
  
Fields  
---  
`autoBackupEnabled` |  `boolean` Optional. If set to true, enables automatic backups on the database.  
`backupDestinationDetails[]` |  `object (`[BackupDestinationDetails](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.BackupDestinationDetails)`)` Optional. Details of the database backup destinations.  
`retentionPeriodDays` |  `integer` Optional. The number of days an automatic backup is retained before being automatically deleted. This value determines the earliest point in time to which a database can be restored. Min: 1, Max: 60.  
`backupDeletionPolicy` |  `enum (`[BackupDeletionPolicy](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.BackupDeletionPolicy)`)` Optional. This defines when the backups will be deleted after Database termination.  
`autoFullBackupDay` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/DayOfWeek)`)` Optional. The day of the week on which the full backup should be performed on the database. If no value is provided, it will default to Sunday.  
`autoFullBackupWindow` |  `enum (`[BackupWindow](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.BackupWindow)`)` Optional. The window in which the full backup should be performed on the database. If no value is provided, the default is anytime.  
`autoIncrementalBackupWindow` |  `enum (`[BackupWindow](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.BackupWindow)`)` Optional. The window in which the incremental backup should be performed on the database. If no value is provided, the default is anytime except the auto full backup day.  
  
### BackupDestinationDetails

The details of the database backup destination.

JSON representation  
---  
      
    
    {
      "type": enum ([BackupDestinationType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.BackupDestinationType))
    }  
  
Fields  
---  
`type` |  `enum (`[BackupDestinationType](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases#Database.BackupDestinationType)`)` Optional. The type of the database backup destination.  
  
### BackupDestinationType

The type of the database backup destination.

Enums  
---  
`BACKUP_DESTINATION_TYPE_UNSPECIFIED` | Default unspecified value.  
`NFS` | Backup destination type is NFS.  
`RECOVERY_APPLIANCE` | Backup destination type is Recovery Appliance.  
`OBJECT_STORE` | Backup destination type is Object Store.  
`LOCAL` | Backup destination type is Local.  
`DBRS` | Backup destination type is DBRS.  
  
### BackupDeletionPolicy

This defines when the backups will be deleted after Database termination.

Enums  
---  
`BACKUP_DELETION_POLICY_UNSPECIFIED` | Default unspecified value.  
`DELETE_IMMEDIATELY` | Keeps the backup for predefined time i.e. 72 hours and then delete permanently.  
`DELETE_AFTER_RETENTION_PERIOD` | Keeps the backups as per the policy defined for database backups.  
  
### BackupWindow

The 2 hour window in which the backup should be performed on the database.

Enums  
---  
`BACKUP_WINDOW_UNSPECIFIED` | Default unspecified value.  
`SLOT_ONE` | 12:00 AM - 2:00 AM  
`SLOT_TWO` | 2:00 AM - 4:00 AM  
`SLOT_THREE` | 4:00 AM - 6:00 AM  
`SLOT_FOUR` | 6:00 AM - 8:00 AM  
`SLOT_FIVE` | 8:00 AM - 10:00 AM  
`SLOT_SIX` | 10:00 AM - 12:00 PM  
`SLOT_SEVEN` | 12:00 PM - 2:00 PM  
`SLOT_EIGHT` | 2:00 PM - 4:00 PM  
`SLOT_NINE` | 4:00 PM - 6:00 PM  
`SLOT_TEN` | 6:00 PM - 8:00 PM  
`SLOT_ELEVEN` | 8:00 PM - 10:00 PM  
`SLOT_TWELVE` | 10:00 PM - 12:00 AM  
  
### OperationsInsightsStatus

The Status of Operations Insights for this Database.

Enums  
---  
`OPERATIONS_INSIGHTS_STATUS_UNSPECIFIED` | Default unspecified value.  
`ENABLING` | Indicates that the operations insights are being enabled.  
`ENABLED` | Indicates that the operations insights are enabled.  
`DISABLING` | Indicates that the operations insights are being disabled.  
`NOT_ENABLED` | Indicates that the operations insights are not enabled.  
`FAILED_ENABLING` | Indicates that the operations insights failed to enable.  
`FAILED_DISABLING` | Indicates that the operations insights failed to disable.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases/get)`

|  Gets details of a single Database.  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases/list)`

|  Lists all the Databases for the given project, location and DbSystem.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
