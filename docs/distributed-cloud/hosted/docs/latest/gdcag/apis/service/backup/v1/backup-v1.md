---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/backup/v1/backup-v1/
title: KRM API backup.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:13.529898+00:00
---

# KRM API backup.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/backup/v1/backup-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API backup.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## backup.gdc.goog/v1

### Backup

Defines the schema for the `Backup` API.

_Appears in:_ \- BackupList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `Backup`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BackupSpec_ |   
`status` _BackupStatus_ |   
  
### BackupConfig

Represents an inner message type that defines the configuration of creating a backup from this backup plan.

_Appears in:_ \- BackupPlanSpec \- BackupSpec

Field | Description  
---|---  
`backupScope` _BackupScope_ | The resource selection scope of a backup. Examples include `all_namespaces`, selected namespaces, and selected applications. You must specify a single value for `backup_scope`. The `BackupScope` value must be one of the following types: `BackupConfig_AllNamespaces`, `BackupConfig_SelectedNamespaces`, or `BackupConfig_SelectedApplications`.  
`backupRepository` _string_ | The name of the `BackupRepository` resource identifying the secondary storage for this `BackupPlan` resource.  
`includeVolumeData` _boolean_ | Specifies whether volume data is backed up. If unset, the default is `False`.  
`includeSecrets` _boolean_ | Specifies whether secrets are backed up. If unset, the default is `False`.  
`encryptionKey` _EncryptionKey_ | An encryption key. This field is immutable.  
`volumeStrategy` _VolumeStrategy_ | The tradeoffs to use when backing up volumes.  
  
### BackupInfo

Represents the name and state of a backup in the `RecentBackups` field .

_Appears in:_ \- BackupPlanStatus

Field | Description  
---|---  
`name` _string_ | The name of the backup.  
`state` _BackupState_ | The status of the most recently executed backup.  
  
### BackupList

Contains a list of backups.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `BackupList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Backup array_ |   
  
### BackupPlan

Defines the schema for the `BackupPlan` API.

_Appears in:_ \- BackupPlanList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `BackupPlan`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BackupPlanSpec_ |   
`status` _BackupPlanStatus_ |   
  
### BackupPlanList

Contains a list of backup plans.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `BackupPlanList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BackupPlan array_ |   
  
### BackupPlanSpec

Defines the desired state of a backup plan.

_Appears in:_ \- BackupPlan

Field | Description  
---|---  
`clusterName` _string_ | The name of the cluster containing the data this backup plan backs up. By default, it is the cluster in which this backup plan is created.  
`backupSchedule` _Schedule_ | The scheduled backup creation under this backup plan.  
`backupConfig` _BackupConfig_ | The backup configuration of this backup plan.  
`retentionPolicy` _RetentionPolicy_ | The lifecycle of backups created under this plan.  
`description` _string_ | A user-specified descriptive string for this backup plan.  
`deactivated` _boolean_ | Specifies whether the plan has been deactivated. Setting this field to 'True' locks the plan meaning no further updates are allowed, including changes to the deactivated field. It also prevents new backups from being created under this plan, both manually or scheduled. Default to 'False'.  
  
### BackupPlanStatus

Defines the observed state of a backup plan.

_Appears in:_ \- BackupPlan

Field | Description  
---|---  
`lastBackupTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp for the most recently executed backup.  
`nextBackupTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp for the next scheduled backup.  
`state` _State_ | The current state of the backup plan.  
`lastBackupState` _BackupState_ | The state of the most recently created backup.  
`lastBackupStateReason` _string_ | A human-readable description of why the last backup is in the current state.  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the observations of this backup plan's current state.  
`recentBackups` _BackupInfo array_ | The most recent backups created by the backup plan.  
  
### BackupRepository

Defines the schema for the `BackupRepository` API.

_Appears in:_ \- BackupRepositoryList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `BackupRepository`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BackupRepositorySpec_ |   
`status` _BackupRepositoryStatus_ |   
  
### BackupRepositoryList

Contains a list of backup repository resources.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `BackupRepositoryList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BackupRepository array_ |   
  
### BackupRepositoryManager

BackupRepositoryManager is the Schema for the backuprepositorymanagers API

_Appears in:_ \- BackupRepositoryManagerList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `BackupRepositoryManager`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BackupRepositoryManagerSpec_ |   
`status` _BackupRepositoryManagerStatus_ |   
  
### BackupRepositoryManagerList

BackupRepositoryManagerList contains a list of BackupRepositoryManager

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `BackupRepositoryManagerList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BackupRepositoryManager array_ |   
  
### BackupRepositoryManagerSpec

BackupRepositoryManagerSpec defines the desired state of BackupRepositoryManager

_Appears in:_ \- BackupRepositoryManager

Field | Description  
---|---  
`backupRepositorySpec` _BackupRepositorySpec_ | BackupRepositorySpec contains all the details needed to create a backup repository inside a user cluster. Note that the ImportPolicy field of the BackupRepositorySpec will not be honored here. The created BackupRepository will be "ReadWrite" if the cluster it is being created in is the ReadWriteCluster. It will be "ReadOnly" if the cluster it is being created in exists in the ReadOnlyClusters list. This field is immutable.  
`readWriteCluster` _NamespacedName_ | ReadWriteCluster specifies the single cluster (baremetal.cluster.gke.io/Cluster) which has permission to create a ReadWrite backup repository using the data in the BackupRepositorySpec field. A ReadWrite repository can be used to schedule/create Backups, BackupPlans, and Restores, and is effectively owned by the cluster it is created in. NOTE: A BackupRepository can only be used as ReadWrite by at most one k8s cluster. This field is mutable.  
`readOnlyClusters` _NamespacedName array_ | ReadOnlyClusters specifies the list of clusters (baremetal.cluster.gke.io/Cluster) which have permission to create a ReadOnly backup repository using the data in the BackupRepositorySpec field. A ReadOnly repository can only be used to import and view backups. No new backups/resources can be created in this repository, but restores can use and reference read-only backups for restoration. Intended to import backups from another cluster for a cross-cluster restore. There is no restriction on how often a BackupRepository can be used as ReadOnly. This field is mutable.  
  
### BackupRepositoryManagerStatus

BackupRepositoryManagerStatus defines the observed state of BackupRepositoryManager

_Appears in:_ \- BackupRepositoryManager

Field | Description  
---|---  
`backupCount` _integer_ | BackupCount is the total number of backups that have been created inside the storage bucket that the BackupRepositorySpec points to.  
`backupPlanCount` _integer_ | BackupPlanCount is the total number of backup plans that have been created inside the storage bucket that the BackupRepositorySpec points to.  
`restoreCount` _integer_ | RestoreCount is the total number of restores that have been created inside the storage bucket that the BackupRepositorySpec points to.  
`restorePlanCount` _integer_ | RestorePlanCount is the total number of restore plans that have been created inside the storage bucket that the BackupRepositorySpec points to.  
`clusterStatuses` _ClusterStatus array_ | ClusterStatuses contains the current status in regard to creating the desired backup repository in each cluster. The list will contain an entry for all clusters specified in the ReadOnlyClusters list as well as the ReadWriteCluster. The backup repository being successfully created in a cluster is indicated by its entry in the ClusterStatuses array having the "Ready" condition as "True", otherwise it will be "False".  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta)_ | Conditions indicates whether or not the Backup Repository Manager and its created backup repositories are in a healthy state.  
`errorStatus` _ErrorStatus_ | The most recent errors from reconciliation with the observed times included.  
  
### BackupRepositorySpec

Defines the desired state of the backup repository.

_Appears in:_ \- BackupRepository

Field | Description  
---|---  
`secretReference` _[SecretReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#secretreference-v1-core)_ | A reference to an Access Secret which is dependent on your storage system of choice. This Secret is used requests to this endpoint. For example, an S3 Access Secret.  
`endpoint` _string_ | The endpoint used to access the backup repository. In the case of Google Private Cloud, this is the S3 endpoint that provides access to the Tenant project.  
`type` _RepositoryType_ | The type of the backup repository. For example, S3 or Google Cloud Storage. This tells the agent which storage system or API to use.  
`s3Options` _S3Options_ | The data used for configuring access to an S3-compatible `BackupRepo` resource.  
`importPolicy` _ImportPolicy_ | The policy that determines whether this backup repository is read-only or read-write.  
`importSubstitution` _ImportSubstitution_ | This field determines whether to substitute the backup repository name of imported resources with this backup repository name.  
`force` _boolean_ | Specifies the action that a read-write backup repository takes if the storage bucket that it is initialized with has already been claimed by a different backup repository. If `True`, the new backup repository still claims ownership of the storage bucket by replacing the existing sentinel file with its own sentinel file. If `False`, the creation of the new backup repository fails with an error. The default value is `False`. This must only be used if the sentinel file that is overridden no longer has a backup repository, otherwise that backup repository enters an error state which might cause undesired side effects.  
  
### BackupRepositoryStatus

Defines the observed state of a backup repository.

_Appears in:_ \- BackupRepository

Field | Description  
---|---  
`sentinelEtag` _string_ | A field that connects a backup repository to the sentinel file that it owns.  
`reconciliationError` _ReconciliationError_ | The errors that have occurred during the most recent reconciliation attempt for the backup repository.  
`reconciliationErrorMessage` _string_ | The error messages that might have occurred during reconciliation.  
`errorStatus` _ErrorStatus_ | The most recent errors from reconciliation with the observed times included.  
`initialImportDone` _boolean_ | Specifies whether this backup repository has completed the initial import or not.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the observations of this backup repository's current state. Known condition types: Ready.  
  
### BackupRetentionPolicy

Represents the retention policy for a Backup

_Appears in:_ \- ClusterBackupSpec

Field | Description  
---|---  
`deleteLockDays` _integer_ | The number of days from the creation of this backup backup for which deletion is blocked. For backups created automatically from a backup schedule, this field is set to the value of `ClusterBackupPlan.RetentionPolicy.backup_delete_block_days`. For backups created manually that leave this field unspecified, the service assigns the value of `ClusterBackupPlan.RetentionPolicy.backup_delete_block_days`. If a backup is created where the value of this field is less than the value of `ClusterBackupPlan.RetentionPolicy.backup_delete_block_days`, an invalid response is returned from the service. This field must be an integer value between `0-90`. This field must only be increased by an update request, or an invalid response is returned by the service. Note, this field only applies to backups with a `Succeeded` state.  
`retainDays` _integer_ | The number of days to keep this cluster backup for, after which it is automatically deleted. This is calculated from the `create_time` of the cluster backup. If this field is not specified or set to `0`, it means the backup is not automatically deleted. For cluster backups automatically created from a schedule, this field is assigned the value of `ClusterBackupPlan.RetentionPolicy.backup_retain_days`. For backups created manually that leave this field unspecified, the service assigns the value of `ClusterBackupPlan.RetentionPolicy.backup_retain_days`. If a backup is created where the value of this field is less than the value of `delete_lock_days`, an invalid response is returned by the service. This field must only be increased by an update request, or an invalid response is returned by the service.  
  
### BackupScope

Defines which namespaces and applications to back up.

_Appears in:_ \- BackupConfig \- RestoreConfig

Field | Description  
---|---  
`allNamespaces` _boolean_ | Specifies whether all namespaces are backed up. If set to `True`, indicates that all namespaces must be backed up.  
`selectedNamespaces` _Namespaces_ | The list of namespaces to back up.  
`selectedApplications` _NamespacedNames_ | The list of applications to back up.  
  
### BackupSpec

Defines the desired state of the backup.

_Appears in:_ \- Backup

Field | Description  
---|---  
`clusterName` _string_ | The name of the cluster that is backed up. By default, it is the cluster in which this backup is created.  
`backupPlanName` _string_ | The name of the backup plan from which this backup was created.  
`backupConfig` _BackupConfig_ | A configuration that is used when this backup is generated from the given backup plan. This must be copied from the backup plan that this backup was generated by, rather than a reference. This field must not be set by the user, and must only be set by the backup plan scheduler and the `ManualBackupRequest` resource.  
`description` _string_ | An optional string description of the Backup. This field has no impact on functionality.  
`manual` _boolean_ | Specifies whether the backup resource was created manually. If `True`, this backup has been created manually, If `False`, this Backup has been created automatically from the backup plan schedule.  
`deleteLockDays` _integer_ | The number of days from the `create_time` of this backup for which deletion is blocked. For backups created automatically from a backup schedule, this field is set to the value of `BackupPlan.RetentionPolicy.backup_delete_block_days`. For backups created manually that leave this field unspecified, the service assigns the value of `BackupPlan.RetentionPolicy.backup_delete_block_days`. If a backup is created where the value of this field is less than the value of `BackupPlan.RetentionPolicy.backup_delete_block_days`, an invalid response is returned from the service. This field must be an integer value between `0-90`. This field must only be increased by an update request, or an invalid response is returned by the service. Note, this field only applies to backups with a `Succeeded` state. Default to `0`.  
`retainDays` _integer_ | The number of days to keep this backup for, after which it is automatically deleted. This is calculated from the `create_time` of the backup. If this field is not specified or set to `0`, it means the backup is not automatically deleted. For backups automatically created from a a backup schedule, this field is assigned the value of `BackupPlan.RetentionPolicy.backup_retain_days`. For backups created manually that leave this field unspecified, the service assigns the value of `BackupPlan.RetentionPolicy.backup_retain_days`. If a backup is created where the value of this field is less than the value of `delete_lock_days`, an invalid response is returned by the service. This field must only be increased by an update request, or an invalid response is returned by the service. Default to `0`.  
  
### BackupStatus

Defines the observed state of a backup.

_Appears in:_ \- Backup

Field | Description  
---|---  
`clusterMetadata` _ClusterMetadata_ | The metadata of the cluster.  
`jobCreated` _boolean_ | Specifies whether a backup job has been created for this backup.  
`state` _BackupState_ | The current state of the backup.  
`reason` _string_ | A human-readable description of why the backup is in the current state.  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the observations of this backup's current state. Known condition types: Succeeded  
`createTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp of when this backup resource was created. This can be converted to and from [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt).  
`updateTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp of when this backup plan was last updated. This can be converted to and from [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt).  
`resourceCount` _integer_ | The total number of resources backed up.  
`volumeCount` _integer_ | The total number of volumes backed up.  
`sizeBytes` _integer_ | The total size, measured in bytes.  
`podCount` _integer_ | The total number of workload pods backed up.  
`systemPodCount` _integer_ | The total number of system pods backed up. These pods are excluded from billing.  
`vmCount` _integer_ | The total number of virtual machines backed up.  
`deleteLockExpireTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The time when the deletion lock will expire. This is an output only field calculated from the combined value of `create_time` and `delete_lock_days`, and is updated accordingly when the `delete_lock_days` field of a backup is updated. Note, this field only applies to backups with a `Succeeded` state.  
`retainExpireTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The time when the backup is automatically deleted. It's an output only field calculated from the combined value of `create_time` and `retain_days`, and is updated accordingly when the `retain_days` field of a backup has been updated.  
`completeTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The completion time of the backup.  
  
### ClusterBackup

_Appears in:_ \- ClusterBackupList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ClusterBackup`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ClusterBackupSpec_ |   
`status` _ClusterBackupStatus_ |   
  
### ClusterBackupConfig

Represents an inner message type that defines the configuration of creating a backup from this backup plan.

_Appears in:_ \- ClusterBackupPlanSpec \- ClusterBackupSpec

Field | Description  
---|---  
`backupScope` _BackupScope_ | The resource selection scope of a backup. Examples include `all_namespaces`, selected namespaces, and selected applications. You must specify a single value for `backup_scope`. The `BackupScope` value must be one of the following types: `BackupConfig_AllNamespaces`, `BackupConfig_SelectedNamespaces`, or `BackupConfig_SelectedApplications`.  
`backupRepositoryName` _string_ | The name of the `BackupRepositoryRef` resource identifying the secondary storage for this `ClusterBackupPlan` resource.  
`clusterBackupRepositoryName` _string_ | The name of the `ClusterBackupRepositoryRef` resource identifying the secondary storage for this `ClusterBackupPlan` resource.  
`includeVolumeData` _boolean_ | Specifies whether volume data is backed up. If unset, the default is `false`.  
`includeSecrets` _boolean_ | Specifies whether secrets are backed up. If unset, the default is `false`.  
`volumeStrategy` _VolumeStrategy_ | The type of volume backup to perform.  
  
### ClusterBackupList

Represents a list of cluster backups.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ClusterBackupList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ClusterBackup array_ |   
  
### ClusterBackupPlan

_Appears in:_ \- ClusterBackupPlanList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ClusterBackupPlan`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ClusterBackupPlanSpec_ |   
`status` _BackupPlanStatus_ |   
  
### ClusterBackupPlanList

Represents a list of ClusterBackups

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ClusterBackupPlanList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ClusterBackupPlan array_ |   
  
### ClusterBackupPlanSpec

Represents an API that wraps around the backupv1.BackupPlan custom resource. They are mostly identical, but there are some fields that are selectively omitted.

_Appears in:_ \- ClusterBackupPlan

Field | Description  
---|---  
`targetCluster` _TargetCluster_ | The cluster that will backed up.  
`backupSchedule` _Schedule_ | The scheduled backup creation under this backup plan.  
`clusterBackupConfig` _ClusterBackupConfig_ | The backup configuration of this backup plan.  
`retentionPolicy` _RetentionPolicy_ | The lifecycle of backups created under this plan.  
`description` _string_ | A user-specified descriptive string for this backup plan.  
`deactivated` _boolean_ | Specifies whether the plan has been deactivated. Setting this field to 'true' locks the plan meaning no further updates are allowed, including changes to the deactivated field. It also prevents new backups from being created under this plan, both manually or scheduled. Default to 'false'.  
  
### ClusterBackupRepository

Defines the schema for the `ClusterBackupRepository` API.

_Appears in:_ \- ClusterBackupRepositoryList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ClusterBackupRepository`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ClusterBackupRepositorySpec_ |   
`status` _ClusterBackupRepositoryStatus_ |   
  
### ClusterBackupRepositoryList

Contains a list of `ClusterBackupRepository` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ClusterBackupRepositoryList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ClusterBackupRepository array_ |   
  
### ClusterBackupRepositorySpec

Defines the desired state of the `ClusterBackupRepositorySpec` resource.

_Appears in:_ \- ClusterBackupRepository

Field | Description  
---|---  
`secretReference` _[SecretReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#secretreference-v1-core)_ | A reference to an Access Secret which is dependent on your storage system of choice. This Secret is used requests to this endpoint. For example, an S3 Access Secret.  
`endpoint` _string_ | The endpoint used to access the cluster backup repository.  
`type` _RepositoryType_ | The type of the cluster backup repository. For example, S3 or Google Cloud Storage. This tells the agent which storage system or API to use.  
`s3Options` _S3Options_ | The data used for configuring access to an S3-compatible `BackupRepo` resource.  
`importPolicy` _ImportPolicy_ | The policy that determines whether this backup repository is read-only or read-write.  
`force` _boolean_ | Specifies the action that a read-write backup repository takes if the storage bucket that it is initialized with has already been claimed by a different backup repository. If `True`, the new backup repository still claims ownership of the storage bucket by replacing the existing sentinel file with its own sentinel file. If `False`, the creation of the new backup repository fails with an error. The default value is `False`. This must only be used if the sentinel file that is overridden no longer has a backup repository, otherwise that backup repository enters an error state which might cause undesired side effects.  
  
### ClusterBackupRepositoryStatus

Defines the observed state of `ClusterBackupRepository` resource.

_Appears in:_ \- ClusterBackupRepository

Field | Description  
---|---  
`sentinelEtag` _string_ | A field that connects a backup repository to the sentinel file that it owns.  
`reconciliationError` _ReconciliationError_ | The errors that have occurred during the most recent reconciliation attempt for the backup repository.  
`reconciliationErrorMessage` _string_ | The error messages that might have occurred during reconciliation.  
`errorStatus` _ErrorStatus_ | The most recent errors from reconciliation with the observed times included.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Specifies the status of the cluster backup repository. Supported conditions include `InitialImportDone`, `Ready`, `Deprecated`.  
  
### ClusterBackupSpec

Represents an API that wraps around the backupv1.Backup custom resource. They are mostly identical, but there are some fields that are selectively omitted.

_Appears in:_ \- ClusterBackup

Field | Description  
---|---  
`targetCluster` _TargetCluster_ | The name of the cluster that will backed up.  
`clusterBackupPlanName` _string_ | The name of the cluster backup plan from which this backup was created.  
`backupConfig` _ClusterBackupConfig_ | A configuration that is used when this backup is generated from the given backup plan. This must be copied from the cluster backup plan that this cluster backup was generated by, rather than a reference. This field must not be set by the user, and must only be set by the backup plan scheduler and the `ManualBackupRequest` resource.  
`description` _string_ | An optional string description of the backup. This field has no impact on functionality.  
`manual` _boolean_ | Specifies whether the cluster backup resource was created manually. If `True`, this backup has been created manually, If `False`, this cluster backup has been created automatically from the backup plan schedule.  
`retentionPolicy` _BackupRetentionPolicy_ | Retention policy for the Backup.  
  
### ClusterBackupStatus

Defines the observed state of a cluster backup.

_Appears in:_ \- ClusterBackup

Field | Description  
---|---  
`clusterMetadata` _ClusterMetadata_ | The metadata of the cluster.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Specifies the status of the cluster backup. Supported conditions include `JobCreated`, `Succeeded`.  
`jobCreated` _boolean_ | Specifies whether a backup job has been created for this cluster backup.  
`state` _BackupState_ | The current state of the cluster backup.  
`stateReason` _string_ | A human-readable description of why the backup is in the current state.  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
`createTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp of when this backup resource was created. This can be converted to and from [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt).  
`updateTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp of when this cluster backup was last updated. This can be converted to and from [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt).  
`resourceCount` _integer_ | The total number of resources backed up.  
`volumeCount` _integer_ | The total number of volumes backed up.  
`sizeBytes` _integer_ | The total size, measured in bytes.  
`podCount` _integer_ | The total number of workload pods backed up.  
`deleteLockExpireTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The time when the deletion lock will expire. This is an output only field calculated from the combined value of `create_time` and `delete_lock_days`, and is updated accordingly when the `delete_lock_days` field of a cluster backup is updated. Note, this field only applies to cluster backups with a `Succeeded` state.  
`retainExpireTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The time when the cluster backup is automatically deleted. It's an output only field calculated from the combined value of `create_time` and `retain_days`, and is updated accordingly when the `retain_days` field of a cluster backup has been updated.  
`completeTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The completion time of the cluster backup.  
  
### ClusterMetadata

Represents the metadata of the cluster.

_Appears in:_ \- BackupStatus

Field | Description  
---|---  
`clusterName` _string_ | The name of the source cluster from where the backup has been created from.  
`k8sVersion` _string_ | The Kubernetes server version.  
`platformVersion` _PlatformVersion_ | The platform version types that can be assigned to PlatformVersion. For example, `GpcVersion`.  
  
### ClusterResourceConflictPolicy

_Underlying type:_ `string` The restoration behavior for non-namespaced cluster resources to follow when a conflict occurs.

_Appears in:_ \- RestoreConfig \- RestorePolicies

### ClusterResourceSelection

Represents the selection of non-namespaced resources for restoration.

_Appears in:_ \- RestoreConfig \- RestoreResourceSelection

Field | Description  
---|---  
`selectedGroupKinds` _[GroupKind](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#groupkind-v1-meta) array_ | A list of `GroupKind` resources. A non-namespaced resource must be included as one of the `GroupKind` resources specified in the list. Note, even though `PersistentVolume` resources are non-namespaced, these are handled separately. See `VolumeDataRestorePolicy` for details. Specifying a `PersistentVolume` `GroupKind` in this list does not affect whether or not a `PersistentVolume` is restored.  
  
### ClusterRestore

Defines the schema for the `ClusterRestore` API.

_Appears in:_ \- ClusterRestoreList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ClusterRestore`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ClusterRestoreSpec_ |   
`status` _ClusterRestoreStatus_ |   
  
### ClusterRestoreConfig

Defines the configuration of a `ClusterRestore`.

_Appears in:_ \- ClusterRestorePlanSpec \- ClusterRestoreSpec

Field | Description  
---|---  
`volumeDataRestorePolicy` _VolumeDataRestorePolicy_ | The policy to use for volume data restoration. Provides a default value of `NO_VOLUME_DATA_RESTORATION` if no value is specified.  
`clusterResourceConflictPolicy` _ClusterResourceConflictPolicy_ | The policy that resolves conflicts when restoring cluster-scoped resources. This request is invalid if this field has a value of `CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED` and `cluster_resource_restore_scope` is specified.  
`namespacedResourceRestoreMode` _NamespacedResourceRestoreMode_ | The restoration mode to use for namespaced resources. The request is invalid if this field has a value of `NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED` and `namespaced_resource_restore_scope` is specified.  
`clusterResources` _ClusterResourceSelection_ | The non-namespaced resources to be restored. If this field is not specified, no cluster resource is restored. Note, even though `PersistentVolume` resources are non-namespaced, they are handled separately. See the `VolumeDataRestorePolicy` resource for details. Specifying a `PersistentVolume` `GroupKind` in this list does not determine whether a `PersistentVolume` is restored.  
`namespacedResourceAllowlist` _[GroupKind](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#groupkind-v1-meta) array_ | The specific namespaced resources to restore. If defined, only the resources defined in this `allowlist` are restored.  
`namespacedResourceRestoreScope` _BackupScope_ | The selected namespace resources to restore. One of the entries must be specified along with a valid `Type`. The `Type` values that are valid to be assigned to `restoreScope` are `AllNamespaces`, `SelectedNamespaces`, or `SelectedApplications`.  
`substitutionRules` _SubstitutionRule array_ | The rules followed during the substitution of backed-up Kubernetes resources. An empty list means no substitution will occur. Substitution rules are applied sequentially in the order defined. This order matters, as changes made by a rule may impact the matching logic of the subsequent rule. Only one of `SubstitutionRules` or `TransformationRules` can be specified for a given restore operation.  
`transformationRules` _TransformationRule array_ | The rules followed during the transformation of backed-up Kubernetes resources. An empty list means no transformation will happen. Transformation rules are applied sequentially in the order defined. This order matters, as changes made by a rule may impact the matching logic of a subsequent rule. Only one of `SubstitutionRules` or `TransformationRules` can be specified for a given restore operation.  
`clusterBackupRepositoryRef` _string_ | The name of the cluster backup repository which identifies the repository for the restore resource. This field must be attached in read-write mode. If this field is not supplied then it will be selected using the following logic: 1. If the backup that we are performing the restore on points to a read-write repository in the current cluster, this repository is selected. 2. If the backup that we are performing a restore on points to a read-only repository, any read-write repository from the cluster is selected and used.  
  
### ClusterRestoreList

Represents a list of cluster restores.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ClusterRestoreList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ClusterRestore array_ |   
  
### ClusterRestorePlan

Defines the schema for the `ClusterRestorePlan` API.

_Appears in:_ \- ClusterRestorePlanList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ClusterRestorePlan`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ClusterRestorePlanSpec_ |   
`status` _RestorePlanStatus_ |   
  
### ClusterRestorePlanList

Represents a list of `ClusterRestorePlan` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ClusterRestorePlanList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ClusterRestorePlan array_ |   
  
### ClusterRestorePlanSpec

Represents an API that wraps around the backupv1.RestorePlan custom resource. They are mostly identical, but there are some fields that are selectively omitted. Defines the desired state of the 'ClusterRestorePlan'.

_Appears in:_ \- ClusterRestorePlan

Field | Description  
---|---  
`targetCluster` _TargetCluster_ | The cluster where data will be restored.  
`clusterBackupPlanName` _string_ | The name of the cluster backup plan from which cluster backups may be used as the source for cluster restores created using this `ClusterRestorePlan`. This field is required and immutable.  
`clusterRestoreConfig` _ClusterRestoreConfig_ | The cluster restore configuration of this cluster restore plan.  
`description` _string_ | A user-specified descriptive string for this cluster restore plan.  
  
### ClusterRestoreSpec

Represents an API that wraps around the backupv1.Restore custom resource. Defines the desired state of a ClusterRestore.

_Appears in:_ \- ClusterRestore

Field | Description  
---|---  
`targetCluster` _TargetCluster_ | The cluster where data will be restored.  
`clusterBackupName` _string_ | The name of the cluster backup, which must be in the same namespace as the cluster restore.  
`clusterRestorePlanName` _string_ | The name of the cluster restore plan from which this cluster restore inherited its `ClusterRestoreConfig` resource.  
`clusterRestoreConfig` _ClusterRestoreConfig_ | The configuration of the cluster restore.  
`description` _string_ | An optional description of the cluster restore. This has no impact on functionality.  
`filter` _Filter_ | Filter can be used to further refine the resource selection of the cluster restore beyond the coarse-grained scope defined in the `ClusterRestorePlan`.  
  
### ClusterRestoreStatus

Defines the observed state of a cluster restore.

_Appears in:_ \- ClusterRestore

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Specifies the status of the cluster restore. Supported conditions include `JobCreated`, `Succeeded`.  
`state` _RestoreState_ | The current state of the cluster restore.  
`stateReason` _string_ | A human-readable description of why the cluster restore is in the current state.  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
`resourcesRestoredCount` _integer_ | The number of resources restored in this cluster restore action.  
`resourcesExcludedCount` _integer_ | The number of resources excluded in this cluster restore action.  
`resourcesFailedCount` _integer_ | The number of resources that failed to be restored in this cluster restore action.  
`restoredVolumesCount` _integer_ | The number of volumes restored in this cluster restore action.  
`startTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The create time of the cluster restore process.  
`completeTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The end time of the cluster restore process.  
  
### ClusterStatus

ClusterStatus contains backup repository creation status for a given cluster.

_Appears in:_ \- BackupRepositoryManagerStatus

Field | Description  
---|---  
`cluster` _NamespacedName_ |   
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
  
### ClusterVolumeBackup

Defines the schema for the `ClusterVolumeBackup` API.

_Appears in:_ \- ClusterVolumeBackupList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ClusterVolumeBackup`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ClusterVolumeBackupSpec_ |   
`status` _ClusterVolumeBackupStatus_ |   
  
### ClusterVolumeBackupList

Contains a list of `ClusterVolumeBackup` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ClusterVolumeBackupList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ClusterVolumeBackup array_ |   
  
### ClusterVolumeBackupSpec

Defines the desired state of a cluster volume backup.

_Appears in:_ \- ClusterVolumeBackup

Field | Description  
---|---  
`cluster` _TargetCluster_ | The name of the cluster that this cluster volume backup maintains data for.  
`clusterBackupName` _string_ | The name of the associated backup. Each cluster volume backup must be associated with a backup. It will always be in the same namespace.  
`clusterBackupPlanName` _string_ | The name of the backup plan from which the asssociated backup was created. It will always be in the same namespace.  
`sourcePVC` _[TypedObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#typedobjectreference-v1-core)_ | The source persistent volume claim from which the cluster volume backup is taken from.  
  
### ClusterVolumeBackupStatus

Defines the observed state of a cluster volume backup.

_Appears in:_ \- ClusterVolumeBackup

Field | Description  
---|---  
`volumeBackupHandle` _string_ | An underlying cluster volume backup handle, which uniquely identifies a cluster volume backup inside of a backup repository. This handle doesn't have a unified format and is treated as an opaque string.  
`format` _VolumeBackupFormat_ | A cluster volume backup format. For example, `PD`, `Portable`, etc.  
`storageBytes` _integer_ | The size of the cluster volume backup in the backup storage. For incremental backups this value may dynamically change if one of the previous volume backups was deleted.  
`diskSizeBytes` _integer_ | The minimum size of the disk to which this volume backup can be restored.  
`state` _VolumeBackupState_ | The current state of the volume backup.  
`message` _string_ | A human-readable message indicating details about why the backup is in this state.  
`completeTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp when this `ClusterVolumeBackup` resource was completed in the text format of [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt).  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Specifies the status of the cluster volume backup.  
  
### ClusterVolumeRestore

Represents an API that wraps around the backupv1.VolumeRestore custom resource. Defines the schema for the `ClusterVolumeRestore` API.

_Appears in:_ \- ClusterVolumeRestoreList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ClusterVolumeRestore`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ClusterVolumeRestoreSpec_ |   
`status` _VolumeRestoreStatus_ |   
  
### ClusterVolumeRestoreList

Represents a list of `ClusterVolumeRestore` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ClusterVolumeRestoreList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ClusterVolumeRestore array_ |   
  
### ClusterVolumeRestoreSpec

Defines the desired state of a cluster volume restore.

_Appears in:_ \- ClusterVolumeRestore

Field | Description  
---|---  
`targetCluster` _TargetCluster_ | The name of the cluster where volume will be restored.  
`clusterRestoreName` _string_ | The name of the cluster restore resource that created this cluster volume restore.  
`clusterVolumeBackupName` _string_ | The name of the cluster volume backup resource that we are restoring.  
`targetPvc` _NamespacedName_ | The target `PersistentVolumeClaim` resource to be restored.  
  
### DeleteBackupRequest

Defines the schema for the `DeleteBackupRequest` API.

_Appears in:_ \- DeleteBackupRequestList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `DeleteBackupRequest`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _DeleteBackupRequestSpec_ |   
`status` _DeleteBackupRequestStatus_ |   
  
### DeleteBackupRequestList

Contains a list of `DeleteBackupRequest` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `DeleteBackupRequestList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _DeleteBackupRequest array_ |   
  
### DeleteBackupRequestSpec

Defines the desired state of the `DeleteBackupRequest` resource.

_Appears in:_ \- DeleteBackupRequest

Field | Description  
---|---  
`backupName` _string_ | The name of the backup to be deleted. Note, the backup must be exist in the same namespace as the `DeleteBackupRequest` resource.  
  
### DeleteBackupRequestStatus

Defines the observed state of `DeleteBackupRequest` resource.

_Appears in:_ \- DeleteBackupRequest

Field | Description  
---|---  
`timeToExpire` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The time the resource expires.  
`statusField` _StatusFields_ | The status of the observed state of `DeleteBackupRequest` resource.  
  
### DeleteClusterBackupRequest

Defines the schema for the `DeleteClusterBackupRequest` API.

_Appears in:_ \- DeleteClusterBackupRequestList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `DeleteClusterBackupRequest`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _DeleteClusterBackupRequestSpec_ |   
`status` _DeleteClusterBackupRequestStatus_ |   
  
### DeleteClusterBackupRequestList

Contains a list of `DeleteBackupRequest` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `DeleteClusterBackupRequestList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _DeleteClusterBackupRequest array_ |   
  
### DeleteClusterBackupRequestSpec

Defines the desired state of the `DeleteClusterBackupRequest` resource.

_Appears in:_ \- DeleteClusterBackupRequest

Field | Description  
---|---  
`clusterBackupRef` _string_ | The name of the `ClusterBackup` resource to be deleted. Note, the `ClusterBackup` resource must exist in the same namespace as the `DeleteClusterBackupRequest` resource.  
  
### DeleteClusterBackupRequestStatus

Defines the observed state of `DeleteClusterBackupRequest` resource.

_Appears in:_ \- DeleteClusterBackupRequest

Field | Description  
---|---  
`timeToExpire` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The time the resource expires.  
`statusField` _StatusFields_ | The status of the observed state of `DeleteClusterBackupRequest` resource.  
  
### EncryptionKey

Defines an encryption key. For preview, supports Google Cloud Platform KMS only.

_Appears in:_ \- BackupConfig \- RestoreConfig

Field | Description  
---|---  
`gcpKMSEncryptionKey` _string_ | A Google KMS encryption key in the format: `projects/<project>/locations/<location>/keyRings/<key-ring>/cryptoKeys/<key>`.  
  
### Filter

Defines the fine-grained restore Filter

_Appears in:_ \- ManualRestoreRequestSpec \- RestoreSpec

Field | Description  
---|---  
`inclusionFilters` _ResourceSelector array_ | Selects resources for restoration. If specified, only resources which match inclusion_filters will be selected for restoration. A resource will be selected if it matches any ResourceSelector of the inclusion_filters.  
`exclusionFilters` _ResourceSelector array_ | Excludes resources from restoration. If specified, a resource will not be restored if it matches any ResourceSelector of the exclusion_filters.  
  
### ImportPolicy

_Underlying type:_ `string` The policy that determines whether this backup repository is read-only or read-write.

_Appears in:_ \- BackupRepositorySpec

### ImportSubstitution

Represents whether we substitute the backup repository name on imported resources.

_Appears in:_ \- BackupRepositorySpec

Field | Description  
---|---  
`substituteBRName` _boolean_ |   
  
### ManualBackupRequest

Defines the schema for the `ManualBackupRequest` API.

_Appears in:_ \- ManualBackupRequestList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ManualBackupRequest`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ManualBackupRequestSpec_ |   
`status` _ManualBackupRequestStatus_ |   
  
### ManualBackupRequestList

Contains a list of `ManualBackupRequest` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ManualBackupRequestList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ManualBackupRequest array_ |   
  
### ManualBackupRequestSpec

Defines the desired state of a `ManualBackupRequest` resource.

_Appears in:_ \- ManualBackupRequest

Field | Description  
---|---  
`backupName` _string_ | The name of the manual backup to be created.  
`backupPlanName` _string_ | The name of the backup plan from which the `BackupConfig` resource is pulled.  
`description` _string_ | A user-specified descriptive string for the backup created by this `ManualBackupRequest` resource.  
`deleteLockDays` _integer_ | The number of days from the `create_time` of this backup for which deletion is blocked. For backups automatically created from a schedule, this field is given the value of `BackupPlan.RetentionPolicy.backup_delete_block_days`. If a backup is created with this field unspecified, it is given the value of `BackupPlan.RetentionPolicy.backup_delete_block_days`. If this Backup is created with this field set to a value less than the value of `BackupPlan.RetentionPolicy.backup_delete_block_days`, an invalid response is returned from the agent. This field must be a value within `0-90`. This field must only be increased by an update request, or an invalid response is returned by the agent. Note that this field only applies to backups with a `Succeeded` state. Default to `0`.  
`retainDays` _integer_ | The number of days to keep this backup for, after which it is automatically deleted. If this field is not specified or set to `0`, it means the backup is not automatically deleted. For backups automatically created from a backup schedule, this field is assigned the value of `BackupPlan.RetentionPolicy.backup_default_retain_days`. For created backups that leave this field unspecified, the agent to uses the value of `BackupPlan.RetentionPolicy.backup_default_retain_days`. The creation of a backup with this field set to a value less than `delete_lock_days` results in an invalid response from the agent. This field must only be increased in an update request, or an invalid response is returned by the agent immediately. Default to `0`.  
  
### ManualBackupRequestStatus

Defines the observed state of a `ManualBackupRequest` resource.

_Appears in:_ \- ManualBackupRequest

Field | Description  
---|---  
`timeToExpire` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The time the resource should expire.  
`statusField` _StatusFields_ | The status of the observed state of `ManualBackupRequest` resource.  
`statusMessage` _string_ | The statusMessage is any error message for `ManualBackupRequest` resource.  
  
### ManualClusterBackupRequest

Defines the schema for the `ManualClusterBackupRequest` API.

_Appears in:_ \- ManualClusterBackupRequestList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ManualClusterBackupRequest`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ManualClusterBackupRequestSpec_ |   
`status` _ManualClusterBackupRequestStatus_ |   
  
### ManualClusterBackupRequestList

Contains a list of `ManualClusterBackupRequest` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ManualClusterBackupRequestList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ManualClusterBackupRequest array_ |   
  
### ManualClusterBackupRequestSpec

Defines the desired state of a `ManualClusterBackupRequest` resource.

_Appears in:_ \- ManualClusterBackupRequest

Field | Description  
---|---  
`clusterBackupName` _string_ | The name of the cluster backup to be created. It is created inside of the same namespace as the `ManualClusterBackupRequest` resource.  
`clusterBackupPlanRef` _string_ | The name of the cluster backup plan from which the `ClusterBackupConfig` resource is pulled. Note, it is expected that the cluster backup plan exists in the same namespace as the `ManualClusterBackupRequest` resource.  
`description` _string_ | A user-specified descriptive string for the cluster backup created by this `ManualClusterBackupRequest` resource.  
`deleteLockDays` _integer_ | The number of days from the `create_time` of this backup for which deletion is blocked. For backups automatically created from a schedule, this field is given the value of `BackupPlan.RetentionPolicy.backup_delete_block_days`. If a `Backup` is created with this field unspecified, it is given the value of `BackupPlan.RetentionPolicy.backup_delete_block_days`. If this `Backup` is created with this field set to a value less than the value of `ClusterBackupPlan.RetentionPolicy.backup_delete_block_days`, an invalid response is returned from the agent. This field must be a value within `0-90`. This field must only be increased by an update request, or an invalid response is returned by the agent. Note that this field only applies to backups with a `Succeeded` state.  
`retainDays` _integer_ | The number of days to keep this backup for, after which it is automatically deleted. If this field is not specified or set to `0`, it means the backup is not automatically deleted. For backups automatically created from a backup schedule, this field is assigned the value of `BackupPlan.RetentionPolicy.backup_default_retain_days`. For created backups that leave this field unspecified, the agent uses the value of `ClusterBackupPlan.RetentionPolicy.backup_default_retain_days`. The creation of a backup with this field set to a value less than `delete_lock_days` results in an invalid response from the agent. This field must only be increased in an update request, or an invalid response is returned by the agent immediately.  
  
### ManualClusterBackupRequestStatus

Defines the observed state of a `ManualClusterBackupRequest` resource.

_Appears in:_ \- ManualClusterBackupRequest

Field | Description  
---|---  
`timeToExpire` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The time the resource expires.  
`statusField` _StatusFields_ | The status of the observed state a of `ManualClusterBackupRequest` resource.  
  
### ManualClusterRestoreRequest

Defines the schema for the `ManualClusterRestoreRequest` API.

_Appears in:_ \- ManualClusterRestoreRequestList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ManualClusterRestoreRequest`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ManualClusterRestoreRequestSpec_ |   
`status` _ManualRestoreRequestStatus_ |   
  
### ManualClusterRestoreRequestList

Represents a list of `ManualClusterRestoreRequest` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ManualClusterRestoreRequestList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ManualClusterRestoreRequest array_ |   
  
### ManualClusterRestoreRequestSpec

Defines the desired state of a `ManualClusterRestoreRequest` resource.

_Appears in:_ \- ManualClusterRestoreRequest

Field | Description  
---|---  
`clusterRestoreName` _string_ | The name of the cluster restore to be created.  
`clusterRestorePlanName` _string_ | The name of the cluster restore plan to pull the `ClusterRestoreConfig` resource from.  
`clusterBackupName` _string_ | The name of the cluster backup that is being restored. Note, it is expected that the cluster restore plan and cluster backup exist in the same namespace as the `ManualClusterRestoreRequest` resource.  
`description` _string_ | A user-specified descriptive string for the cluster restore created by this `ManualClusterRestoreRequest` resource.  
`filter` _Filter_ | Filter which can be used to further refine the resource selection of the cluster restore beyond the coarse-grained scope defined in the ClusterRestorePlan.  
  
### ManualRestoreRequest

Defines the schema for the `ManualRestoreRequest` API.

_Appears in:_ \- ManualRestoreRequestList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ManualRestoreRequest`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ManualRestoreRequestSpec_ |   
`status` _ManualRestoreRequestStatus_ |   
  
### ManualRestoreRequestList

Contains a list of `ManualRestoreRequest` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ManualRestoreRequestList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ManualRestoreRequest array_ |   
  
### ManualRestoreRequestSpec

Defines the desired state of a `ManualRestoreRequest` resource.

_Appears in:_ \- ManualRestoreRequest

Field | Description  
---|---  
`restoreName` _string_ | The name of the manual restore to be created.  
`restorePlanName` _string_ | The name of the restore plan to pull the `RestoreConfig` resource from.  
`backupName` _string_ | The name of the backup that is being restored.  
`description` _string_ | A user-specified descriptive string for the restore created by this `ManualRestoreRequest` resource.  
`filter` _Filter_ | Filter which can be used to further refine the resource selection of the Restore beyond the coarse-grained scope defined in the RestorePlan.  
  
### ManualRestoreRequestStatus

Defines the observed state of `ManualRestoreRequest` resource.

_Appears in:_ \- ManualRestoreRequest

Field | Description  
---|---  
`timeToExpire` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The time when the resource should expire.  
`statusField` _StatusFields_ | The status of the observed state of a `ManualRestoreRequest` resource.  
  
### NamespacedName

Defines a name in a specific namespace.

_Appears in:_ \- NamespacedNames \- NamespacedResourceSelection \- VolumeBackupSpec \- VolumeRestoreSpec

Field | Description  
---|---  
`namespace` _string_ | The namespace of the resource in Kubernetes.  
`name` _string_ | The name of the resource in Kubernetes.  
  
### NamespacedNames

_Appears in:_ \- BackupScope

Field | Description  
---|---  
`namespacedNames` _NamespacedName array_ | A list of namespaced names.  
  
### NamespacedResourceRestoreMode

_Underlying type:_ `string` The restoration behavior for namespaced resources.

_Appears in:_ \- RestoreConfig \- RestorePolicies

### NamespacedResourceSelection

Defines the selection of namespaced resources for restoration. One of the following values must be specified along with a matching `Type`:
    
    
    `AllNamespaces`, `SelectedNamespaces`, or `SelectedApplications`.
    

_Appears in:_ \- RestoreResourceSelection

Field | Description  
---|---  
`type` _NamespacedResourceSelectionType_ | The type of selection to use.  
`allNamespaces` _boolean_ | Specifies whether or not to restore all namespaced resources in the backup. Leaving this field unspecified, or setting it to `False` with the `Type` set to `NamespacedResourceSelectionType.AllNamespaces` is invalid.  
`selectedNamespaces` _string array_ | A list of the selected namespaces to restore. If a value is provided along with the `Type` set to `NamespacedResourceSelectionType.SelectedNamespaces`, resources with an original namespace that feature in the specified list are restored. Note, specifying an empty string in this list does not restore non-namespaced cluster resources. To restore cluster resources, see `ClusterResourceSelection`.  
`selectedApplications` _NamespacedName array_ | A list of selected `ProtectedApplication` resources to restore. If a value is provided, along with the `Type` set to `NamespacedResourceSelectionType.SelectedApplications`, the resources belonging to one of the listed applications are restored.  
  
### NamespacedResourceSelectionType

_Underlying type:_ `string` The type of namespaced resources selection.

_Appears in:_ \- NamespacedResourceSelection

### Namespaces

_Appears in:_ \- BackupScope

Field | Description  
---|---  
`namespaces` _string array_ | A list of namespaces.  
  
### ObjectStorageBackupConfig

Configures backups of object storage.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `ObjectStorageBackupConfig`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`source` _ObjectStorageEndpoint_ | The source object storage to be backed up.  
`target` _ObjectStorageEndpoint_ | The target to which the backup is written.  
`timestamp` _boolean_ | Specifies whether to store each transfer in a timestamped sub-path of the bucket. If set to `True`, the structure is `YYYY-MM-DD-hh:mm:ss`. This helps to store copies taken from multiple points in time of a backup. Defaults to `False`.  
  
### ObjectStorageEndpoint

Represents an object storage endpoint as well as the credentials to access it.

_Appears in:_ \- ObjectStorageBackupConfig

Field | Description  
---|---  
`endpoint` _string_ | The endpoint used to access object storage. For example, `https://s3.svc`.  
`bucket` _string_ | The bucket within the endpoint to scope reference.  
`secretReference` _[SecretReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#secretreference-v1-core)_ | The reference to S3 access credentials used to access object storage.  
  
### PlatformVersion

Defines the version of the platform.

_Appears in:_ \- ClusterMetadata

Field | Description  
---|---  
`gpcVersion` _string_ | The Google Private Cloud version.  
  
### ReconciliationError

_Underlying type:_ `string` The errors that have occurred during the most recent reconciliation attempt for the backup repository.

_Appears in:_ \- BackupRepositoryStatus

### RepositoryType

_Underlying type:_ `string` The type of endpoint being written to.

_Appears in:_ \- BackupRepositorySpec

### ResourceFilter

Defines the rules to filter down the list of candidate resources to provide transformation rules against. All fields with `ResourceFilter` are optional, so not specifying any of the `ResourceFilter` fields results in matching on all resources.

_Appears in:_ \- TransformationRule

Field | Description  
---|---  
`namespaces` _string array_ | A list of target namespaces a transformation rule will apply to. A resource's original namespace must match one of the names in the list to be considered as a transformation candidate. An empty string is expected in the list for any non-namespaced resource to be considered. If empty, all namespaces are considered.  
`groupKinds` _[GroupKind](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#groupkind-v1-meta) array_ | A list of target `GroupKind` resources a transformation rule will apply to. A resource's original `GroupKind` resource must match one of the `GroupKind` resources specified in the list to be considered as a transformation candidate. If empty, all `GroupKind` resources are considered. Note, a resource needs to satisfy both the `Namespaces` requirement and `GroupKinds` requirement to be considered as a transformation candidate.  
`jsonPath` _string_ | The string representation of the path in the JSON which leads to the fields in the target resource for filtering. `JSONPath` documentation can be viewed here: https://github.com/json-path/JsonPath/blob/master/README.md. `JSONPath` formats can be tested online (e.g. https://jsonpath.com/).  
  
### ResourceSelector

Defines ResourceSelector for fine-grained restore Filter

_Appears in:_ \- Filter

Field | Description  
---|---  
`groupKind` _[GroupKind](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#groupkind-v1-meta)_ | Selects resources using their Kubernetes GroupKinds. If specified, only resources of provided GroupKind will be selected.  
`name` _string_ | Selects resources using their resource names. If specified, only resources with the provided name will be selected.  
`namespace` _string_ | Selects resources using their namespaces. This only applies to namespace scoped resources and cannot be used for selecting cluster scoped resources. If specified, only resources in the provided namespace will be selected. If not specified, the filter will apply to both cluster scoped and namespace scoped resources (e.g. name or label). The Namespace resource itself will be restored if and only if any resources within the namespace are restored.  
`labels` _object (keys:string, values:string)_ | Selects resources using Kubernetes labels. If specified, a resource will be selected if and only if the resource has all of the provided labels and all the label values match.  
  
### Restore

Defines the schema for the `Restore` API.

_Appears in:_ \- RestoreList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `Restore`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _RestoreSpec_ |   
`status` _RestoreStatus_ |   
  
### RestoreConfig

Defines the configuration of a restore.

_Appears in:_ \- RestorePlanSpec \- RestoreSpec

Field | Description  
---|---  
`volumeDataRestorePolicy` _VolumeDataRestorePolicy_ | The policy to use for volume data restoration. Provides a default value of `NO_VOLUME_DATA_RESTORATION` if no value is specified.  
`clusterResourceConflictPolicy` _ClusterResourceConflictPolicy_ | The policy that resolves conflicts when restoring cluster-scoped resources. The request is invalid if this field is not specified. This request is invalid if this field has a value of `CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED` and `cluster_resource_restore_scope` is specified.  
`namespacedResourceRestoreMode` _NamespacedResourceRestoreMode_ | The restoration mode to use for namespaced resources. The request is invalid if this field is not specified. The request is invalid if this field has a value of `NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED` and `namespaced_resource_restore_scope` is specified.  
`clusterResources` _ClusterResourceSelection_ | The non-namespaced resources to be restored. If this field is not specified, no cluster resource is restored. Note, even though `PersistentVolume` resources are non-namespaced, they are handled separately. See the `VolumeDataRestorePolicy` resource for details. Specifying a `PersistentVolume` `GroupKind` in this list does not determine whether a `PersistentVolume` is restored.  
`namespacedResourceAllowlist` _[GroupKind](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#groupkind-v1-meta) array_ | The specific namespaced resources to restore. If defined, only the resources defined in this `allowlist` are restored.  
`restoreScope` _BackupScope_ | The selected namespace resources to restore. One of the entries must be specified along with a valid `Type`. The `Type` values that are valid to be assigned to `restoreScope` are `AllNamespaces`, `SelectedNamespaces`, or `SelectedApplications`.  
`substitutionRules` _SubstitutionRule array_ | The rules followed during the substitution of backed-up Kubernetes resources. An empty list means no substitution will occur. Substitution rules are applied sequentially in the order defined. This order matters, as changes made by a rule may impact the matching logic of the subsequent rule. Only one of `SubstitutionRules` or `TransformationRules` can be specified for a given restore operation.  
`transformationRules` _TransformationRule array_ | The rules followed during the transformation of backed-up Kubernetes resources. An empty list means no transformation will happen. Transformation rules are applied sequentially in the order defined. This order matters, as changes made by a rule may impact the matching logic of a subsequent rule. Only one of `SubstitutionRules` or `TransformationRules` can be specified for a given restore operation.  
`backupRepository` _string_ | T name of the backup repository which identifies the repository for the restore resource. This field must be attached in read-write mode. Note, this backup repository might differ from the backup repository for the backup this restore references. If this field is not supplied then it will be selected using the following logic: 1. If the backup that we are performing the restore on points to a read-write repository in the current cluster, this repository is selected. 2. If the backup that we are performing a restore on points to a read-only repository, any read-write repository from the cluster is selected and used.  
`encryptionKey` _EncryptionKey_ | An encryption key. This field is immutable.  
  
### RestoreList

Contains a list of `Restore` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `RestoreList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Restore array_ |   
  
### RestorePlan

Defines the schema for the `RestorePlan` API.

_Appears in:_ \- RestorePlanList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `RestorePlan`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _RestorePlanSpec_ |   
`status` _RestorePlanStatus_ |   
  
### RestorePlanList

Contains a list of `RestorePlan` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `RestorePlanList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _RestorePlan array_ |   
  
### RestorePlanSpec

Defines the desired state of the restore plan.

_Appears in:_ \- RestorePlan

Field | Description  
---|---  
`backupPlanName` _string_ | The name of the backup plan from which backups may be used as the source for restores created using this restore plan. This field is required and immutable.  
`restoreConfig` _RestoreConfig_ | The restore configuration of this restore plan.  
`clusterName` _string_ | The name of the cluster that will contain the data restored by this restore plan. By default, it is the cluster in which the restore plan is created.  
`description` _string_ | A user-specified descriptive string for this restore plan.  
  
### RestorePlanStatus

Defines the observed state of a restore plan.

_Appears in:_ \- RestorePlan

Field | Description  
---|---  
`lastRestoreTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp for the most recently executed restore.  
`state` _StatusFields_ | The current state of the restore plan.  
  
### RestoreSpec

Defines the desired state of a restore.

_Appears in:_ \- Restore

Field | Description  
---|---  
`backupName` _string_ | The full name of the backup resource that this `Restore` resource uses to restore from.  
`restorePlanName` _string_ | The name of the restore plan from which this restore inherited its `RestoreConfig` resource.  
`clusterName` _string_ | The name of the cluster that contains the data restored by this restore. By default, it is the cluster in which the restore was created.  
`restoreConfig` _RestoreConfig_ | The configuration of the restore.  
`description` _string_ | An optional description of the backup. This has no impact on functionality.  
`filter` _Filter_ | Filter can be used to further refine the resource selection of the Restore beyond the coarse-grained scope defined in the RestorePlan.  
  
### RestoreState

_Underlying type:_ `string`

_Appears in:_ \- RestoreStatus

### RestoreStatus

Defines the observed state of a restore.

_Appears in:_ \- Restore

Field | Description  
---|---  
`state` _RestoreState_ | The current state of the restore.  
`stateReason` _string_ | A human-readable description of why the restore is in the current state.  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the observations of this restore's current state. Known condition types: Succeeded  
`jobCreated` _boolean_ | Specifies whether a restore job has been created for this restore.  
`resourcesRestoredCount` _integer_ | The number of resources restored in this restore action.  
`resourcesExcludedCount` _integer_ | The number of resources excluded in this restore action.  
`resourcesFailedCount` _integer_ | The number of resources that failed to be restored in this restore action.  
`restoredVolumesCount` _integer_ | The number of volumes restored in this restore action.  
`startTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The create time of the restore process.  
`completeTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The end time of the restore process.  
  
### RetentionPolicy

Defines a policy that determines when to automatically delete backups created under this backup plan, a plan-level minimum number of backup retain days, plan-level minimum number of backups to be retained, and a lock to disallow any policy updates.

_Appears in:_ \- BackupPlanSpec

Field | Description  
---|---  
`backupDeleteLockDays` _integer_ | The number of days during for which the deletion of a backup created under this backup plan is blocked. Default to `0`. This field must be an integer value between `0-90`. A backup created under this backup plan is not deletable until it reaches the combined value of the backup's `create_time` and `backup_delete_lock_days`. Updating this backup plan field does not affect existing backups under it. Backups created after a successful update automatically inherit the new value.  
`backupRetainDays` _integer_ | The number of days after which the service deletes a backup. If specified, a backup created under this backup plan are automatically deleted after it reaches the the combined value of `create_time` and `backup_retain_days`. If not specified, backups created under this backup plan are not subject to automatic deletion. Updating this field does not affect existing backups under it. Backups created after a successful update automatically inherit the new value. Note, specifying a value for `backup_retain_days` that is less than `backup_delete_lock_days` at the time of the creation or update is considered invalid, and the request is rejected immediately.  
`locked` _boolean_ | Specifies whether the retention policy of this backup plan is locked. If set to `True`, no further update is allowed on this policy, including the `locked` field itself. Default to `False`.  
`numBackupsToRetain` _integer_ | The number of backups to retain. If specified, oldest backups of backup plan which reached its combined value of `create_time` and `backup_delete_lock_days are automatically deleted after the total number of backups under this backup plan reaches the value of`num_backups_to_retain`. If not specified, backups created under this backup plan may or may not subject to automatic deletion based on 'backup_retain_days'. Updating this field does affect existing backups under the backup plan. Note, num_backups_to_retain must be greater than or equal to the number of backups that can be created within backup_delete_lock_days.  
  
### S3Options

Defines the options for calling to an S3 endpoint for the backup repository.

_Appears in:_ \- BackupRepositorySpec

Field | Description  
---|---  
`bucket` _string_ | The bucket within the endpoint to upload backups to.  
`region` _string_ | The region of a given endpoint. Formatting is storage system dependent.  
`forcePathStyle` _boolean_ | Specifies whether to force path style URLs for objects. For example, `https://s3.amazonaws.com//` instead of `https://.s3.amazonaws.com/`.  
`serverSideEncryption` _string_ | The server-side encryption algorithm used when storing objects. For example, `AES256 or`aws:kms`.  
`kmsKeyId` _string_ | The KMS key ID to use for object storage if server-side encryption is using KMS.  
  
### Schedule

Represents an inner message type that defines a cron schedule.

_Appears in:_ \- BackupPlanSpec

Field | Description  
---|---  
`cronSchedule` _string_ | A cron string schedule on which an operation is executed.  
`paused` _boolean_ | Specifies whether the scheduled operaction is inactive or active. If set to `True`, the scheduled operation will be inactive. Default to `True`.  
`maxConcurrency` _integer_ | Specifies the maximum number of active scheduled backups that can exist under a backup plan at the same time. If specified, no more than this number of scheduled backups from this backup plan can be in the active state at any given time. If not specified, it defaults to 2.  
  
### State

_Underlying type:_ `string` A value specifying what state the backup plan is currently in.

_Appears in:_ \- BackupPlanStatus

### SubstitutionRule

Defines the rules for substitution.

_Appears in:_ \- RestoreConfig

Field | Description  
---|---  
`target` _SubstitutionTarget_ | The matching criteria that checks whether a resource is a substitution candidate and has fields that match the supplied `JSONPath` value.  
`originValuePattern` _string_ | A regular expression pattern string which is applied to the JSON value matched from the supplied `Target` value. If not specified, the original value is always substituted using the specified `NewValue` value. Note, an empty string is a legitimate regex pattern, and is treated like any other string.  
`newValue` _string_ | The desired value in string format to substitute to.  
  
### SubstitutionTarget

Defines the rules of target candidates for substitution.

_Appears in:_ \- SubstitutionRule

Field | Description  
---|---  
`namespaces` _string array_ | A list of target namespaces a substitution rule is applied to. A resource's original namespace must match one of the names in the list to be considered as a substitution candidate. For any non-namespaced resource to be considered, an empty string must be provided. If empty, all namespaces are considered.  
`groupKinds` _[GroupKind](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#groupkind-v1-meta) array_ | A list of target `GroupKind` resources a substitution rule applies to. A resource's original `GroupKind` resource must match one of the `GroupKind` resources specified in the list to be considered as a substitution candidate. If empty, all `GroupKind` resources are considered. Note, a resource needs to satisfy both namespace requirements and the `GroupKind` requirements to be considered as a substitution candidate.  
`jsonPath` _string_ | The string representation of the JSON Path which leads to the fields in the target resource, which are in the JSON format for substitution.  
  
### TargetCluster

Represents a Cluster whose data will be backed up or restored.

_Appears in:_ \- ClusterBackupPlanSpec \- ClusterBackupSpec \- ClusterRestorePlanSpec \- ClusterRestoreSpec \- ClusterVolumeBackupSpec \- ClusterVolumeRestoreSpec

Field | Description  
---|---  
`targetClusterType` _TargetClusterType_ | The type of Cluster  
`targetClusterName` _[TypedLocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#typedlocalobjectreference-v1-core)_ | In case of a UserCluster, the name refers to a GDC Cluster inside of the same namespace under the `clusters.cluster.gdc.goog` Group Kind. For the Managemnet API, this field should be left empty.  
  
### TargetClusterType

_Underlying type:_ `string`

_Appears in:_ \- TargetCluster

### TransformationRule

Defines rules of transformation utilizing `jsonPatch`.

_Appears in:_ \- RestoreConfig

Field | Description  
---|---  
`fieldActions` _TransformationRuleAction array_ | A list of operations to take against candidate resources based on the JSON Patch RFC.  
`resourceFilter` _ResourceFilter_ | The matching criteria to check that determines whether a resource is a transformation candidate. Note, an empty or blank `resourceFilter` value results in a match on all resources.  
  
### TransformationRuleAction

Represents the action the user wants to perform as part of transforming a resource.

_Appears in:_ \- TransformationRule

Field | Description  
---|---  
`op` _TransformationRuleOperation_ | The type of action the user wants to perform as part of transforming resources upon a restore operation. The list of valid operations can be viewed at https://www.rfc-editor.org/rfc/rfc6902#section-4.4.  
`from` _string_ | The JSON patch representation of a path within the JSON which leads to the fields in the target resource for move and copy operations.  
`path` _string_ | The JSON patch representation of a path within the JSON which leads to the fields in the target resource for some operations.  
`value` _string_ | The desired value in string format to use for transformation.  
  
### TransformationRuleOperation

_Underlying type:_ `string` The intended operation for a transformation rule.

_Appears in:_ \- TransformationRuleAction

### VMBackupJobList

Contains a list of backups.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `VMBackupJobList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VMBackupJob array_ |   
  
### VMBackupJobSpec

Defines the desired state of the backup.

_Appears in:_ \- VMBackupJob

Field | Description  
---|---  
`backupRef` _NamespacedName_ | The control plane backup name that the vm backup job is related to. The name is immutable.  
`vmRef` _NamespacedName_ | The reference of the VM this CR is backing up This reference could be nil if the backup is a disk backup  
`vmDiskRefs` _VMDisk array_ | List of VM Disks this CR is backing up  
`volumeBackupRefs` _object (keys:string, values:VolumeBackup)_ | map of volume backup name to VolumeBackup struct under this backup This data is embedded into VMBackupJob and not present in the cluster  
`description` _string_ | An optional string description of the Backup. This field has no impact on functionality.  
`manual` _boolean_ | Specifies whether the backup resource was created manually. If `True`, this backup has been created manually, If `False`, this Backup has been created automatically from the backup plan schedule.  
`deleteLockDays` _integer_ | The number of days from the `create_time` of this backup for which deletion is blocked. For backups created automatically from a backup schedule, this field is set to the value of `BackupPlan.RetentionPolicy.backup_delete_block_days`. For backups created manually that leave this field unspecified, the service assigns the value of `BackupPlan.RetentionPolicy.backup_delete_block_days`. If a backup is created where the value of this field is less than the value of `BackupPlan.RetentionPolicy.backup_delete_block_days`, an invalid response is returned from the service. This field must be an integer value between `0-90`. This field must only be increased by an update request, or an invalid response is returned by the service. Note, this field only applies to backups with a `Succeeded` state. Default to `0`.  
`retainDays` _integer_ | The number of days to keep this backup for, after which it is automatically deleted. This is calculated from the `create_time` of the backup. If this field is not specified or set to `0`, it means the backup is not automatically deleted. For backups automatically created from a a backup schedule, this field is assigned the value of `BackupPlan.RetentionPolicy.backup_retain_days`. For backups created manually that leave this field unspecified, the service assigns the value of `BackupPlan.RetentionPolicy.backup_retain_days`. If a backup is created where the value of this field is less than the value of `delete_lock_days`, an invalid response is returned by the service. This field must only be increased by an update request, or an invalid response is returned by the service. Default to `0`.  
  
### VMBackupJobStatus

Defines the observed state of a backup.

_Appears in:_ \- VMBackupJob

Field | Description  
---|---  
`state` _VMBackupJobState_ | The current state of the backup.  
`reason` _string_ | A human-readable description of why the backup is in the current state.  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the observations of this VMBackupJob's current state. Known condition types: Succeeded  
`createTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp of when this VMBackupJob resource was created. This can be converted to and from [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt).  
`snapshotTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp of when all disks in VMBackupJob resource are snapshotted. This can be converted to and from [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt).  
`updateTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp of when this VMBackupJob was last updated. This can be converted to and from [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt).  
`volumeCount` _integer_ | The total number of volumes backed up.  
`retryCount` _integer_ | total number of retries required to backup this VM/VM disk  
`deleteLockExpireTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The time when the deletion lock will expire. This is an output only field calculated from the combined value of `create_time` and `delete_lock_days`, and is updated accordingly when the `delete_lock_days` field of a backup is updated. Note, this field only applies to backups with a `Succeeded` state.  
`retainExpireTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The time when the backup is automatically deleted. It's an output only field calculated from the combined value of `create_time` and `retain_days`, and is updated accordingly when the `retain_days` field of a backup has been updated.  
`completeTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The completion time of the backup.  
  
### VMDisk

_Appears in:_ \- VMBackupJobSpec

Field | Description  
---|---  
`namespace` _string_ | Namespace where the VM Disk resides in  
`name` _string_ | Name of the VM Disk  
`pvcName` _string_ | Name of the underlying PVC  
`uid` _UID_ | UID of the PVC this field is used to get this particular VMBackupJob given the UID of the PVC  
`sizeBytes` _integer_ | The total size, measured in bytes.  
  
### VolumeBackup

Defines the schema for the `VolumeBackup` API.

_Appears in:_ \- VMBackupJobSpec \- VolumeBackupList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `VolumeBackup`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VolumeBackupSpec_ |   
`status` _VolumeBackupStatus_ |   
  
### VolumeBackupFormat

_Underlying type:_ `string` An enum that specifies the format of the volume backup.

_Appears in:_ \- VolumeBackupStatus

### VolumeBackupList

Contains a list of `VolumeBackup` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `VolumeBackupList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VolumeBackup array_ |   
  
### VolumeBackupSpec

Defines the desired state of a volume backup.

_Appears in:_ \- VolumeBackup

Field | Description  
---|---  
`clusterName` _string_ | The name of the cluster that this volume backup maintains data for. By default, it is the cluster in which this volume backup is created.  
`backupName` _string_ | The name of the associated backup. Each volume backup must be associated with a backup.  
`backupPlanName` _string_ | The name of the backup plan from which the asssociated backup was created.  
`sourcePVC` _NamespacedName_ | The source persistent volume claim from which the volume backup is taken from.  
`volumeBackupHandle` _string_ | An underlying volume backup handle which uniquely identifies a volume backup inside of a volume backup repository. This handle doesn't have a unified format and is treated as an opaque string. DEPRECATED: Use the status field instead.  
  
### VolumeBackupState

_Underlying type:_ `string` An enum that suggests the current state of a volume backup.

_Appears in:_ \- VolumeBackupStatus

### VolumeBackupStatus

Defines the observed state of a volume backup.

_Appears in:_ \- VolumeBackup

Field | Description  
---|---  
`volumeBackupHandle` _string_ | An underlying volume backup handle, which uniquely identifies a volume backup inside of a volume backup repository. This handle doesn't have a unified format and is treated as an opaque string.  
`format` _VolumeBackupFormat_ | A volume backup format. For example, `PD`, `Portable`, etc.  
`storageBytes` _integer_ | The size of the volume backup in the backup storage. For incremental backups this value may dynamically change if one of the previous volume backups was deleted.  
`diskSizeBytes` _integer_ | The minimum size of the disk to which this volume backup can be restored.  
`state` _VolumeBackupState_ | The current state of the volume backup.  
`message` _string_ | A human-readable message indicating details about why the backup is in this state.  
`completeTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp when this `VolumeBackup` resource was completed in the text format of [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt).  
`errorStatus` _ErrorStatus_ | The most recent errors with the observed times included.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the observations of this VolumeBackup's current state.  
  
### VolumeDataRestorePolicy

_Underlying type:_ `string` The different volume data restoration policies.

_Appears in:_ \- RestoreConfig \- RestorePolicies

### VolumeRestore

Defines the schema for the `VolumeRestore` API.

_Appears in:_ \- VolumeRestoreList

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `VolumeRestore`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VolumeRestoreSpec_ |   
`status` _VolumeRestoreStatus_ |   
  
### VolumeRestoreList

Contains a list of `VolumeRestore` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `backup.gdc.goog/v1`  
`kind` _string_ | `VolumeRestoreList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VolumeRestore array_ |   
  
### VolumeRestoreSpec

Defines the desired state of a volume restore.

_Appears in:_ \- VolumeRestore

Field | Description  
---|---  
`clusterName` _string_ | The name of the cluster that contains the data from this volume restore. By default, it is the cluster in which this volume restore is created.  
`restoreName` _string_ | The name of the restore resource that created this volume restore.  
`volumeBackupName` _string_ | The name of the volume backup resource that we are restoring.  
`targetPvc` _NamespacedName_ | The target `PersistentVolumeClaim` resource to be restored.  
  
### VolumeRestoreStatus

Defines the observed state of a volume restore.

_Appears in:_ \- VolumeRestore

Field | Description  
---|---  
`volumeBackupHandle` _string_ | An underlying volume backup handle, which uniquely identifies a volume backup inside of a volume backup repository. This handle doesn't have a unified format and is treated as an opaque string.  
`state` _VolumeRestoreState_ | The current state of the volume restoration.  
`stateMessage` _string_ | A human readable description of the current state.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the observations of this Volume Restore's current state. Known condition types: Ready.  
`completeTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The end time of the volume restore process.  
  
### VolumeStrategy

_Underlying type:_ `string` The tradeoffs to use when backing up volumes.

_Appears in:_ \- BackupConfig

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
