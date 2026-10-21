---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups
title: REST Resource: projects.locations.backupPlans.backups.volumeBackups \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:43:55.849853+00:00
---

# REST Resource: projects.locations.backupPlans.backups.volumeBackups  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ APIs & Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest)



Send feedback 

#  REST Resource: projects.locations.backupPlans.backups.volumeBackups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: VolumeBackup
    * JSON representation
  * VolumeBackupFormat
  * State
  * Methods



## Resource: VolumeBackup

Represents the backup of a specific persistent volume as a component of a Backup - both the record of the operation and a pointer to the underlying storage-specific artifacts.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "createTime": string,
      "updateTime": string,
      "sourcePvc": {
        object ([NamespacedName](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/NamespacedName))
      },
      "volumeBackupHandle": string,
      "format": enum ([VolumeBackupFormat](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups#VolumeBackupFormat)),
      "storageBytes": string,
      "diskSizeBytes": string,
      "completeTime": string,
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups#State)),
      "stateMessage": string,
      "etag": string,
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean
    }  
  
Fields  
---  
`name` |  `string` Output only. The full name of the VolumeBackup resource. Format: `projects/*/locations/*/backupPlans/*/backups/*/volumeBackups/*`.  
`uid` |  `string` Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this VolumeBackup resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this VolumeBackup resource was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sourcePvc` |  `object (`[NamespacedName](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/NamespacedName)`)` Output only. A reference to the source Kubernetes PVC from which this VolumeBackup was created.  
`volumeBackupHandle` |  `string` Output only. A storage system-specific opaque handle to the underlying volume backup.  
`format` |  `enum (`[VolumeBackupFormat](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups#VolumeBackupFormat)`)` Output only. The format used for the volume backup.  
`storageBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The aggregate size of the underlying artifacts associated with this VolumeBackup in the backup storage. This may change over time when multiple backups of the same volume share the same backup storage location. In particular, this is likely to increase in size when the immediately preceding backup of the same volume is deleted.  
`diskSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The minimum size of the disk to which this VolumeBackup can be restored.  
`completeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the associated underlying volume backup operation completed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups#State)`)` Output only. The current state of this VolumeBackup.  
`stateMessage` |  `string` Output only. A human readable message explaining why the VolumeBackup is in its current state. This field is only meant for human consumption and should not be used programmatically as this field is not guaranteed to be consistent.  
`etag` |  `string` Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a volume backup from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform volume backup updates in order to avoid race conditions.  
`satisfiesPzs` |  `boolean` Output only. [Output Only] Reserved for future use.  
`satisfiesPzi` |  `boolean` Output only. [Output Only] Reserved for future use.  
  
## VolumeBackupFormat

Identifies the format used for the volume backup.

Enums  
---  
`VOLUME_BACKUP_FORMAT_UNSPECIFIED` | Default value, not specified.  
`GCE_PERSISTENT_DISK` | Compute Engine Persistent Disk snapshot based volume backup.  
  
## State

The current state of a VolumeBackup

Enums  
---  
`STATE_UNSPECIFIED` | This is an illegal state and should not be encountered.  
`CREATING` | A volume for the backup was identified and backup process is about to start.  
`SNAPSHOTTING` | The volume backup operation has begun and is in the initial "snapshot" phase of the process. Any defined ProtectedApplication "pre" hooks will be executed before entering this state and "post" hooks will be executed upon leaving this state.  
`UPLOADING` | The snapshot phase of the volume backup operation has completed and the snapshot is now being uploaded to backup storage.  
`SUCCEEDED` | The volume backup operation has completed successfully.  
`FAILED` | The volume backup operation has failed.  
`DELETING` | This VolumeBackup resource (and its associated artifacts) is in the process of being deleted.  
`CLEANED_UP` | The underlying artifacts of a volume backup (eg: persistent disk snapshots) are deleted.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups/get)`

|  Retrieve the details of a single VolumeBackup.  
  
### `[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups/list)`

|  Lists the VolumeBackups for a given Backup.  
  
### `[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
