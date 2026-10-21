---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups
title: REST Resource: projects.locations.backupPlans.backups \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:17:43.666087+00:00
---

# REST Resource: projects.locations.backupPlans.backups  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ APIs & Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest)



Send feedback 

#  REST Resource: projects.locations.backupPlans.backups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Backup
    * JSON representation
  * ClusterMetadata
    * JSON representation
  * State
  * Methods



## Resource: Backup

Represents a request to perform a single point-in-time capture of some portion of the state of a GKE cluster, the record of the backup operation itself, and an anchor for the underlying artifacts that comprise the Backup (the config backup and VolumeBackups).

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "createTime": string,
      "updateTime": string,
      "manual": boolean,
      "labels": {
        string: string,
        ...
      },
      "deleteLockDays": integer,
      "deleteLockExpireTime": string,
      "retainDays": integer,
      "retainExpireTime": string,
      "encryptionKey": {
        object ([EncryptionKey](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/EncryptionKey))
      },
      "containsVolumeData": boolean,
      "containsSecrets": boolean,
      "clusterMetadata": {
        object ([ClusterMetadata](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups#ClusterMetadata))
      },
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups#State)),
      "stateReason": string,
      "troubleshootingInfo": {
        object ([TroubleshootingInfo](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/TroubleshootingInfo))
      },
      "completeTime": string,
      "resourceCount": integer,
      "volumeCount": integer,
      "sizeBytes": string,
      "etag": string,
      "description": string,
      "podCount": integer,
      "namespaceCount": integer,
      "configBackupSizeBytes": string,
      "permissiveMode": boolean,
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean,
    
      // Union field backup_scope can be only one of the following:
      "allNamespaces": boolean,
      "selectedNamespaces": {
        object ([Namespaces](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/Namespaces))
      },
      "selectedApplications": {
        object ([NamespacedNames](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/NamespacedNames))
      },
      "selectedNamespaceLabels": {
        object ([ResourceLabels](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/ResourceLabels))
      }
      // End of list of possible types for union field backup_scope.
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The fully qualified name of the Backup. `projects/*/locations/*/backupPlans/*/backups/*`  
`uid` |  `string` Output only. Server generated global unique identifier of [UUID4](https://en.wikipedia.org/wiki/Universally_unique_identifier)  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this Backup resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this Backup resource was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`manual` |  `boolean` Output only. This flag indicates whether this Backup resource was created manually by a user or via a schedule in the BackupPlan. A value of True means that the Backup was created manually.  
`labels` |  `map (key: string, value: string)` Optional. A set of custom labels supplied by user.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`deleteLockDays` |  `integer` Optional. Minimum age for this Backup (in days). If this field is set to a non-zero value, the Backup will be "locked" against deletion (either manual or automatic deletion) for the number of days provided (measured from the creation time of the Backup). MUST be an integer value between 0-90 (inclusive).Defaults to parent BackupPlan's `[backupDeleteLockDays](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#RetentionPolicy.FIELDS.backup_delete_lock_days)` setting and may only be increased (either at creation time or in a subsequent update).  
`deleteLockExpireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which an existing delete lock will expire for this backup (calculated from createTime + `[deleteLockDays](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups#Backup.FIELDS.delete_lock_days)`).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`retainDays` |  `integer` Optional. The age (in days) after which this Backup will be automatically deleted. Must be an integer value >= 0:

  * If 0, no automatic deletion will occur for this Backup.
  * If not 0, this must be >= `[deleteLockDays](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups#Backup.FIELDS.delete_lock_days)` and <= 365.

Once a Backup is created, this value may only be increased.Defaults to the parent BackupPlan's `[backupRetainDays](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#RetentionPolicy.FIELDS.backup_retain_days)` value.  
`retainExpireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this Backup will be automatically deleted (calculated from createTime + `[retainDays](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups#Backup.FIELDS.retain_days)`).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`encryptionKey` |  `object (`[EncryptionKey](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/EncryptionKey)`)` Output only. The customer managed encryption key that was used to encrypt the Backup's artifacts. Inherited from the parent BackupPlan's `[encryptionKey](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#BackupConfig.FIELDS.encryption_key)` value.  
`containsVolumeData` |  `boolean` Output only. Whether or not the Backup contains volume data. Controlled by the parent BackupPlan's `[includeVolumeData](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#BackupConfig.FIELDS.include_volume_data)` value.  
`containsSecrets` |  `boolean` Output only. Whether or not the Backup contains Kubernetes Secrets. Controlled by the parent BackupPlan's `[includeSecrets](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#BackupConfig.FIELDS.include_secrets)` value.  
`clusterMetadata` |  `object (`[ClusterMetadata](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups#ClusterMetadata)`)` Output only. Information about the GKE cluster from which this Backup was created.  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups#State)`)` Output only. Current state of the Backup  
`stateReason` |  `string` Output only. Human-readable description of why the backup is in the current `state`. This field is only meant for human readability and should not be used programmatically as this field is not guaranteed to be consistent.  
`troubleshootingInfo` |  `object (`[TroubleshootingInfo](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/TroubleshootingInfo)`)` Output only. Information about the troubleshooting steps which will provide debugging information to the end users.  
`completeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Completion time of the BackupUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`resourceCount` |  `integer` Output only. The total number of Kubernetes resources included in the Backup.  
`volumeCount` |  `integer` Output only. The total number of volume backups contained in the Backup.  
`sizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total size of the Backup in bytes = config backup size + sum(volume backup sizes)  
`etag` |  `string` Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a backup from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform backup updates in order to avoid race conditions: An `etag` is returned in the response to `backups.get`, and systems are expected to put that etag in the request to `backups.patch` or `backups.delete` to ensure that their change will be applied to the same version of the resource.  
`description` |  `string` Optional. User specified descriptive string for this Backup.  
`podCount` |  `integer` Output only. The total number of Kubernetes Pods contained in the Backup.  
`namespaceCount` |  `integer` Output only. The total number of user managed namespaces contained in the Backup.  
`configBackupSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The size of the config backup in bytes.  
`permissiveMode` |  `boolean` Output only. If false, Backup will fail when Backup for GKE detects Kubernetes configuration that is non-standard or requires additional setup to restore.Inherited from the parent BackupPlan's `[permissiveMode](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#BackupConfig.FIELDS.permissive_mode)` value.  
`satisfiesPzs` |  `boolean` Output only. [Output Only] Reserved for future use.  
`satisfiesPzi` |  `boolean` Output only. [Output Only] Reserved for future use.  
Union field `backup_scope`. Defines the "scope" of the Backup - which namespaced resources in the cluster were included in the Backup. Inherited from the parent BackupPlan's [backup_scope][google.cloud.gkebackup.v1.BackupPlan.BackupConfig.backup_scope] value. `backup_scope` can be only one of the following:  
`allNamespaces` |  `boolean` Output only. If True, all namespaces were included in the Backup.  
`selectedNamespaces` |  `object (`[Namespaces](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/Namespaces)`)` Output only. If set, the list of namespaces that were included in the Backup.  
`selectedApplications` |  `object (`[NamespacedNames](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/NamespacedNames)`)` Output only. If set, the list of ProtectedApplications whose resources were included in the Backup.  
`selectedNamespaceLabels` |  `object (`[ResourceLabels](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/ResourceLabels)`)` Output only. If set, the list of labels whose constituent namespaces were included in the Backup.  
  
## ClusterMetadata

Information about the GKE cluster from which this Backup was created.

JSON representation  
---  
      
    
    {
      "cluster": string,
      "k8sVersion": string,
      "backupCrdVersions": {
        string: string,
        ...
      },
    
      // Union field platform_version can be only one of the following:
      "gkeVersion": string,
      "anthosVersion": string
      // End of list of possible types for union field platform_version.
    }  
  
Fields  
---  
`cluster` |  `string` Output only. The source cluster from which this Backup was created. Valid formats:

  * `projects/*/locations/*/clusters/*`
  * `projects/*/zones/*/clusters/*`

This is inherited from the parent BackupPlan's `[cluster](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#BackupPlan.FIELDS.cluster)` field.  
`k8sVersion` |  `string` Output only. The Kubernetes server version of the source cluster.  
`backupCrdVersions` |  `map (key: string, value: string)` Output only. A list of the Backup for GKE CRD versions found in the cluster.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Union field `platform_version`. Platform-specific version `platform_version` can be only one of the following:  
`gkeVersion` |  `string` Output only. GKE version  
`anthosVersion` |  `string` Output only. Anthos version  
  
## State

State

Enums  
---  
`STATE_UNSPECIFIED` | The Backup resource is in the process of being created.  
`CREATING` | The Backup resource has been created and the associated BackupJob Kubernetes resource has been injected into the source cluster.  
`IN_PROGRESS` | The gkebackup agent in the cluster has begun executing the backup operation.  
`SUCCEEDED` | The backup operation has completed successfully.  
`FAILED` | The backup operation has failed.  
`DELETING` | This Backup resource (and its associated artifacts) is in the process of being deleted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/create)`

|  Creates a Backup for the given BackupPlan.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/delete)`

|  Deletes an existing Backup.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/get)`

|  Retrieve the details of a single Backup.  
  
### `[getBackupIndexDownloadUrl](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/getBackupIndexDownloadUrl)`

|  Retrieve the link to the backupIndex.  
  
### `[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/list)`

|  Lists the Backups for a given BackupPlan.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/patch)`

|  Update a Backup.  
  
### `[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-15 UTC."],[],[]] 
