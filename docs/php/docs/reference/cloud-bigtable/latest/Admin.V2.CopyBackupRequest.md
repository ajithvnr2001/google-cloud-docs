---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CopyBackupRequest
title: Cloud Bigtable V2 Client - Class CopyBackupRequest (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:36.397092+00:00
---

# Cloud Bigtable V2 Client - Class CopyBackupRequest (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CopyBackupRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class CopyBackupRequest (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class CopyBackupRequest.

The request for [CopyBackup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__copyBackup__).

Generated from protobuf message `google.bigtable.admin.v2.CopyBackupRequest`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. The name of the destination cluster that will contain the backup copy. The cluster must already exist. Values are of the form: `projects/{project}/instances/{instance}/clusters/{cluster}`.  
`↳ backup_id` |  `string`   
Required. The id of the new backup. The `backup_id` along with `parent` are combined as {parent}/backups/{backup_id} to create the full backup name, of the form: `projects/{project}/instances/{instance}/clusters/{cluster}/backups/{backup_id}`. This string must be between 1 and 50 characters in length and match the regex [_a-zA-Z0-9][-_.a-zA-Z0-9]*.  
`↳ source_backup` |  `string`   
Required. The source backup to be copied from. The source backup needs to be in READY state for it to be copied. Copying a copied backup is not allowed. Once CopyBackup is in progress, the source backup cannot be deleted or cleaned up on expiration until CopyBackup is finished. Values are of the form: `projects/<project>/instances/<instance>/clusters/<cluster>/backups/<backup>`.  
`↳ expire_time` |  `Google\Protobuf\Timestamp`   
Required. Required. The expiration time of the copied backup with microsecond granularity that must be at least 6 hours and at most 30 days from the time the request is received. Once the `expire_time` has passed, Cloud Bigtable will delete the backup and free the resources used by the backup.  
  
### getParent

Required. The name of the destination cluster that will contain the backup copy. The cluster must already exist. Values are of the form: `projects/{project}/instances/{instance}/clusters/{cluster}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. The name of the destination cluster that will contain the backup copy. The cluster must already exist. Values are of the form: `projects/{project}/instances/{instance}/clusters/{cluster}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getBackupId

Required. The id of the new backup. The `backup_id` along with `parent` are combined as {parent}/backups/{backup_id} to create the full backup name, of the form: `projects/{project}/instances/{instance}/clusters/{cluster}/backups/{backup_id}`.

This string must be between 1 and 50 characters in length and match the regex [_a-zA-Z0-9][-_.a-zA-Z0-9]*.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setBackupId

Required. The id of the new backup. The `backup_id` along with `parent` are combined as {parent}/backups/{backup_id} to create the full backup name, of the form: `projects/{project}/instances/{instance}/clusters/{cluster}/backups/{backup_id}`.

This string must be between 1 and 50 characters in length and match the regex [_a-zA-Z0-9][-_.a-zA-Z0-9]*.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getSourceBackup

Required. The source backup to be copied from.

The source backup needs to be in READY state for it to be copied. Copying a copied backup is not allowed. Once CopyBackup is in progress, the source backup cannot be deleted or cleaned up on expiration until CopyBackup is finished. Values are of the form: `projects/<project>/instances/<instance>/clusters/<cluster>/backups/<backup>`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setSourceBackup

Required. The source backup to be copied from.

The source backup needs to be in READY state for it to be copied. Copying a copied backup is not allowed. Once CopyBackup is in progress, the source backup cannot be deleted or cleaned up on expiration until CopyBackup is finished. Values are of the form: `projects/<project>/instances/<instance>/clusters/<cluster>/backups/<backup>`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExpireTime

Required. Required. The expiration time of the copied backup with microsecond granularity that must be at least 6 hours and at most 30 days from the time the request is received. Once the `expire_time` has passed, Cloud Bigtable will delete the backup and free the resources used by the backup.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasExpireTime

### clearExpireTime

### setExpireTime

Required. Required. The expiration time of the copied backup with microsecond granularity that must be at least 6 hours and at most 30 days from the time the request is received. Once the `expire_time` has passed, Cloud Bigtable will delete the backup and free the resources used by the backup.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `string`   
Required. The name of the destination cluster that will contain the backup copy. The cluster must already exist. Values are of the form: `projects/{project}/instances/{instance}/clusters/{cluster}`. Please see BigtableTableAdminClient::clusterName() for help formatting this field.  
`backupId` |  `string`   
Required. The id of the new backup. The `backup_id` along with `parent` are combined as {parent}/backups/{backup_id} to create the full backup name, of the form: `projects/{project}/instances/{instance}/clusters/{cluster}/backups/{backup_id}`. This string must be between 1 and 50 characters in length and match the regex [_a-zA-Z0-9][-_.a-zA-Z0-9]*.  
`sourceBackup` |  `string`   
Required. The source backup to be copied from. The source backup needs to be in READY state for it to be copied. Copying a copied backup is not allowed. Once CopyBackup is in progress, the source backup cannot be deleted or cleaned up on expiration until CopyBackup is finished. Values are of the form: `projects/<project>/instances/<instance>/clusters/<cluster>/backups/<backup>`. Please see BigtableTableAdminClient::backupName() for help formatting this field.  
`expireTime` |  `Google\Protobuf\Timestamp`   
Required. Required. The expiration time of the copied backup with microsecond granularity that must be at least 6 hours and at most 30 days from the time the request is received. Once the `expire_time` has passed, Cloud Bigtable will delete the backup and free the resources used by the backup.  
**Returns**  
---  
**Type** | **Description**  
`[CopyBackupRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CopyBackupRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
