---
url: https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups
title: REST Resource: projects.instances.clusters.backups \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:32.003102+00:00
---

# REST Resource: projects.instances.clusters.backups  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Reference ](https://docs.cloud.google.com/bigtable/docs/apis)



Send feedback 

#  REST Resource: projects.instances.clusters.backups Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: Backup

A backup of a Cloud Bigtable table.

JSON representation  
---  
      
    
    {
      "name": string,
      "sourceTable": string,
      "sourceBackup": string,
      "expireTime": string,
      "startTime": string,
      "endTime": string,
      "sizeBytes": string,
      "state": enum ([State](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups#State)),
      "encryptionInfo": {
        object ([EncryptionInfo](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/EncryptionInfo))
      },
      "backupType": enum ([BackupType](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups#BackupType)),
      "hotToStandardTime": string
    }  
  
Fields  
---  
`name` |  `string` A globally unique identifier for the backup which cannot be changed. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/ backups/[_a-zA-Z0-9][-_.a-zA-Z0-9]*` The final segment of the name must be between 1 and 50 characters in length.The backup is stored in the cluster identified by the prefix of the backup name of the form `projects/{project}/instances/{instance}/clusters/{cluster}`.  
`sourceTable` |  `string` Required. Immutable. Name of the table from which this backup was created. This needs to be in the same instance as the backup. Values are of the form `projects/{project}/instances/{instance}/tables/{sourceTable}`.  
`sourceBackup` |  `string` Output only. Name of the backup from which this backup was copied. If a backup is not created by copying a backup, this field will be empty. Values are of the form: projects//instances//clusters//backups/  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The expiration time of the backup. When creating a backup or updating its `expireTime`, the value must be greater than the backup creation time by: - At least 6 hours - At most 90 daysOnce the `expireTime` has passed, Cloud Bigtable will delete the backup.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. `startTime` is the time that the backup was started (i.e. approximately the time the `[backups.create](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups/create#google.bigtable.admin.v2.BigtableTableAdmin.CreateBackup)` request is received). The row data in this backup will be no older than this timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. `endTime` is the time that the backup was finished. The row data in the backup will be no newer than this timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Size of the backup in bytes.  
`state` |  `enum (`[State](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups#State)`)` Output only. The current state of the backup.  
`encryptionInfo` |  `object (`[EncryptionInfo](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/EncryptionInfo)`)` Output only. The encryption information for the backup.  
`backupType` |  `enum (`[BackupType](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups#BackupType)`)` Indicates the backup type of the backup.  
`hotToStandardTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which the hot backup will be converted to a standard backup. Once the `hotToStandardTime` has passed, Cloud Bigtable will convert the hot backup to a standard backup. This value must be greater than the backup creation time by: - At least 24 hoursThis field only applies for hot backups. When creating or updating a standard backup, attempting to set this field will fail the request.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## State

Indicates the current state of the backup.

Enums  
---  
`STATE_UNSPECIFIED` | Not specified.  
`CREATING` | The pending backup is still being created. Operations on the backup may fail with `FAILED_PRECONDITION` in this state.  
`READY` | The backup is complete and ready for use.  
  
## BackupType

The type of the backup.

Enums  
---  
`BACKUP_TYPE_UNSPECIFIED` | Not specified.  
`STANDARD` | The default type for Cloud Bigtable managed backups. Supported for backups created in both HDD and SSD instances. Requires optimization when restored to a table in an SSD instance.  
`HOT` | A backup type with faster restore to SSD performance. Only supported for backups created in SSD instances. A new SSD table restored from a hot backup reaches production performance more quickly than a standard backup.  
  
## Methods  
  
---  
  
### `[copy](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups/copy)`

|  Copy a Cloud Bigtable backup to a new backup in the destination cluster located in the destination instance and project.  
  
### `[create](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups/create)`

|  Starts creating a new Cloud Bigtable Backup.  
  
### `[delete](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups/delete)`

|  Deletes a pending or completed Cloud Bigtable backup.  
  
### `[get](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups/get)`

|  Gets metadata on a pending or completed Cloud Bigtable Backup.  
  
### `[getIamPolicy](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups/getIamPolicy)`

|  Gets the access control policy for a Bigtable resource.  
  
### `[list](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups/list)`

|  Lists Cloud Bigtable backups.  
  
### `[patch](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups/patch)`

|  Updates a pending or completed Cloud Bigtable Backup.  
  
### `[setIamPolicy](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups/setIamPolicy)`

|  Sets the access control policy on a Bigtable resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/bigtable/docs/reference/admin/rest/v2/projects.instances.clusters.backups/testIamPermissions)`

|  Returns permissions that the caller has on the specified Bigtable resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-06 UTC."],[],[]] 
