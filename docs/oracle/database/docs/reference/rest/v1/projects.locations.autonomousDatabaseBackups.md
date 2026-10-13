---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseBackups
title: REST Resource: projects.locations.autonomousDatabaseBackups \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:36.848616+00:00
---

# REST Resource: projects.locations.autonomousDatabaseBackups  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseBackups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  REST Resource: projects.locations.autonomousDatabaseBackups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AutonomousDatabaseBackup
    * JSON representation
  * AutonomousDatabaseBackupProperties
    * JSON representation
  * State
  * Type
  * Methods



## Resource: AutonomousDatabaseBackup

Details of the Autonomous Database Backup resource. <https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabaseBackup/>

JSON representation  
---  
      
    
    {
      "name": string,
      "autonomousDatabase": string,
      "displayName": string,
      "properties": {
        object ([AutonomousDatabaseBackupProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseBackups#AutonomousDatabaseBackupProperties))
      },
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the Autonomous Database Backup resource with the format: projects/{project}/locations/{region}/autonomousDatabaseBackups/{autonomousDatabaseBackup}  
`autonomousDatabase` |  `string` Required. The name of the Autonomous Database resource for which the backup is being created. Format: projects/{project}/locations/{region}/autonomousDatabases/{autonomousDatabase}  
`displayName` |  `string` Optional. User friendly name for the Backup. The name does not have to be unique.  
`properties` |  `object (`[AutonomousDatabaseBackupProperties](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseBackups#AutonomousDatabaseBackupProperties)`)` Optional. Various properties of the backup.  
`labels` |  `map (key: string, value: string)` Optional. labels or tags associated with the resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## AutonomousDatabaseBackupProperties

Properties of the Autonomous Database Backup resource.

JSON representation  
---  
      
    
    {
      "ocid": string,
      "retentionPeriodDays": integer,
      "compartmentId": string,
      "databaseSizeTb": number,
      "dbVersion": string,
      "isLongTermBackup": boolean,
      "isAutomaticBackup": boolean,
      "isRestorable": boolean,
      "keyStoreId": string,
      "keyStoreWallet": string,
      "kmsKeyId": string,
      "kmsKeyVersionId": string,
      "lifecycleDetails": string,
      "lifecycleState": enum ([State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseBackups#State)),
      "sizeTb": number,
      "availableTillTime": string,
      "endTime": string,
      "startTime": string,
      "type": enum ([Type](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseBackups#Type)),
      "vaultId": string
    }  
  
Fields  
---  
`ocid` |  `string` Output only. OCID of the Autonomous Database backup. <https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Oracle>  
`retentionPeriodDays` |  `integer` Optional. Retention period in days for the backup.  
`compartmentId` |  `string` Output only. The OCID of the compartment.  
`databaseSizeTb` |  `number` Output only. The quantity of data in the database, in terabytes.  
`dbVersion` |  `string` Output only. A valid Oracle Database version for Autonomous Database.  
`isLongTermBackup` |  `boolean` Output only. Indicates if the backup is long term backup.  
`isAutomaticBackup` |  `boolean` Output only. Indicates if the backup is automatic or user initiated.  
`isRestorable` |  `boolean` Output only. Indicates if the backup can be used to restore the Autonomous Database.  
`keyStoreId` |  `string` Optional. The OCID of the key store of Oracle Vault.  
`keyStoreWallet` |  `string` Optional. The wallet name for Oracle Key Vault.  
`kmsKeyId` |  `string` Optional. The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.  
`kmsKeyVersionId` |  `string` Optional. The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation. Autonomous Database Serverless does not use key versions, hence is not applicable for Autonomous Database Serverless instances.  
`lifecycleDetails` |  `string` Output only. Additional information about the current lifecycle state.  
`lifecycleState` |  `enum (`[State](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseBackups#State)`)` Output only. The lifecycle state of the backup.  
`sizeTb` |  `number` Output only. The backup size in terabytes.  
`availableTillTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp until when the backup will be available.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time the backup completed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The date and time the backup started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseBackups#Type)`)` Output only. The type of the backup.  
`vaultId` |  `string` Optional. The OCID of the vault.  
  
## State

// The various lifecycle states of the Autonomous Database Backup.

Enums  
---  
`STATE_UNSPECIFIED` | Default unspecified value.  
`CREATING` | Indicates that the resource is in creating state.  
`ACTIVE` | Indicates that the resource is in active state.  
`DELETING` | Indicates that the resource is in deleting state.  
`DELETED` | Indicates that the resource is in deleted state.  
`FAILED` | Indicates that the resource is in failed state.  
`UPDATING` | Indicates that the resource is in updating state.  
  
## Type

The type of the backup.

Enums  
---  
`TYPE_UNSPECIFIED` | Default unspecified value.  
`INCREMENTAL` | Incremental backups.  
`FULL` | Full backups.  
`LONG_TERM` | Long term backups.  
  
## Methods  
  
---  
  
### `[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseBackups/list)`

|  Lists the long-term and automatic backups of an Autonomous Database.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
