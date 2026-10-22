---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/artifactregistry/v1/artifactregistry-v1/
title: KRM API artifactregistry.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:13.156120+00:00
---

# KRM API artifactregistry.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/artifactregistry/v1/artifactregistry-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API artifactregistry.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## artifactregistry.gdc.goog/v1

Contains API Schema definitions for the Artifact Registry group.

### BackupConfig

Represents an inner message type that defines the configuration of creating a backup from this backup plan.

_Appears in:_ \- HarborInstanceBackupPlanSpec \- HarborInstanceBackupSpec

Field | Description  
---|---  
`backupRepository` _string_ | The name of the BackupRepository resource identifying the secondary storage for this BackupPlan resource.  
`backupScope` _BackupScope_ | The resource selection scope of a backup.  
  
### BackupPlanState

_Underlying type:_ `string` The various states a backup plan can be in.

_Appears in:_ \- HarborInstanceBackupPlanStatus

### BackupRepositoryState

_Underlying type:_ `string` The various states a backup repository can be in.

_Appears in:_ \- HarborInstanceBackupRepositoryStatus

### BackupScope

Defines the Harbor Instance to back up.

_Appears in:_ \- BackupConfig

Field | Description  
---|---  
`harborInstance` _string_ | Harbor Instance name to backup in the same namespace.  
  
### BackupState

_Underlying type:_ `string` The various states a backup can be in.

_Appears in:_ \- HarborInstanceBackupStatus

### HarborInstance

Represents an instance of a Harbor container registry.

_Appears in:_ \- HarborInstanceList

Field | Description  
---|---  
`apiVersion` _string_ | `artifactregistry.gdc.goog/v1`  
`kind` _string_ | `HarborInstance`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _HarborInstanceSpec_ | The desired state of the Harbor instance.  
`status` _HarborInstanceStatus_ | The most recently observed status of the Harbor instance.  
  
### HarborInstanceAdminAccessReference

HarborInstanceAdminAccessReference represents an Admin Access Reference to HarborInstance.

_Appears in:_ \- HarborInstanceSpec

Field | Description  
---|---  
`adminRobotSecretRef` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#localobjectreference-v1-core)_ | AdminRobotSecretRef is the reference of the secret which contains the credentials for system-level Harbor robot account. The secret must contain the following key-value pair: - `secret`: the secret of the Harbor robot account.  
  
### HarborInstanceBackup

Defines the schema for the `Backup` API for HarborInstance.

_Appears in:_ \- HarborInstanceBackupList

Field | Description  
---|---  
`apiVersion` _string_ | `artifactregistry.gdc.goog/v1`  
`kind` _string_ | `HarborInstanceBackup`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _HarborInstanceBackupSpec_ | The desired state of the backup.  
`status` _HarborInstanceBackupStatus_ | The most recently observed status of the backup.  
  
### HarborInstanceBackupList

Represents a collection of backup for Harbor instance.

Field | Description  
---|---  
`apiVersion` _string_ | `artifactregistry.gdc.goog/v1`  
`kind` _string_ | `HarborInstanceBackupList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _HarborInstanceBackup array_ |   
  
### HarborInstanceBackupPlan

Defines the schema for the `BackupPlan` API for HarborInstance.

_Appears in:_ \- HarborInstanceBackupPlanList

Field | Description  
---|---  
`apiVersion` _string_ | `artifactregistry.gdc.goog/v1`  
`kind` _string_ | `HarborInstanceBackupPlan`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _HarborInstanceBackupPlanSpec_ | The desired state of the backup plan.  
`status` _HarborInstanceBackupPlanStatus_ | The most recently observed status of the backup plan.  
  
### HarborInstanceBackupPlanList

Represents a collection of backup plans for Harbor instance.

Field | Description  
---|---  
`apiVersion` _string_ | `artifactregistry.gdc.goog/v1`  
`kind` _string_ | `HarborInstanceBackupPlanList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _HarborInstanceBackupPlan array_ |   
  
### HarborInstanceBackupPlanSpec

Defines the desired state of a backup plan.

_Appears in:_ \- HarborInstanceBackupPlan

Field | Description  
---|---  
`backupSchedule` _Schedule_ | The scheduled backup creation under this backup plan.  
`backupConfig` _BackupConfig_ | The backup configuration of this backup plan.  
`retentionPolicy` _RetentionPolicy_ | The lifecycle of backups created under this plan.  
`description` _string_ | A user-specified descriptive string for this backup plan.  
  
### HarborInstanceBackupPlanStatus

Defines the observed state of a backup plan.

_Appears in:_ \- HarborInstanceBackupPlan

Field | Description  
---|---  
`lastBackupTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp for the most recently executed backup.  
`nextBackupTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp for the next scheduled backup.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions: - Ready: readiness of the backup plan, any error when reconciling embedded object will be surfaced here.  
`state` _BackupPlanState_ | The current state of the backup plan.  
`reason` _string_ | A human-readable description of why the backup plan is in the current state.  
  
### HarborInstanceBackupReference

HarborInstanceBackupReference represents a Backup Reference to HarborInstanceBackup.

_Appears in:_ \- HarborInstanceStatus

Field | Description  
---|---  
`name` _string_ | name is unique within a namespace to reference a HarborInstanceBackup resource.  
`namespace` _string_ | namespace defines the space within which the HarborInstanceBackup name must be unique.  
  
### HarborInstanceBackupRepository

Represents an instance of a backup repository for Harbor instance.

_Appears in:_ \- HarborInstanceBackupRepositoryList

Field | Description  
---|---  
`apiVersion` _string_ | `artifactregistry.gdc.goog/v1`  
`kind` _string_ | `HarborInstanceBackupRepository`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _HarborInstanceBackupRepositorySpec_ | The desired state of the backup repository.  
`status` _HarborInstanceBackupRepositoryStatus_ | The most recently observed status of the backup repository.  
  
### HarborInstanceBackupRepositoryList

Represents a collection of backup repositories for Harbor instance.

Field | Description  
---|---  
`apiVersion` _string_ | `artifactregistry.gdc.goog/v1`  
`kind` _string_ | `HarborInstanceBackupRepositoryList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _HarborInstanceBackupRepository array_ |   
  
### HarborInstanceBackupRepositorySpec

Defines the desired state of the Harbor backup repository.

_Appears in:_ \- HarborInstanceBackupRepository

Field | Description  
---|---  
`secretReference` _[SecretReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#secretreference-v1-core)_ | A reference to an Access Secret to access s3 bucket. The secret should contain 2 data from the S3 access granting flow: - access-key-id - access-key  
`endpoint` _string_ | The endpoint used to access the Harbor backup repository. In the case of Google Private Cloud, this is the S3 endpoint that provides access to the Tenant project.  
`region` _string_ | The region of a given endpoint for the bucket.  
`bucket` _string_ | The bucket within the endpoint to upload backups to.  
`description` _string_ | A user-specified descriptive string for this backup repository.  
  
### HarborInstanceBackupRepositoryStatus

Defines the observed state of a Harbor backup repository.

_Appears in:_ \- HarborInstanceBackupRepository

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions: - Ready: readiness of the backup repository, any error when reconciling embedded object will be surfaced here.  
`state` _BackupRepositoryState_ | The current state of the backup repository.  
`reason` _string_ | A human-readable description of why the backup repository is in the current state.  
  
### HarborInstanceBackupSpec

Defines the desired state of the backup.

_Appears in:_ \- HarborInstanceBackup

Field | Description  
---|---  
`backupPlanName` _string_ | The name of the backup plan from which this backup was created.  
`backupConfig` _BackupConfig_ | Configuration for a backup This field is expected: 1. to be set by the user for manual customized backup explicitly. 2. to be unset with backupPlanName filled for automated scheduled backup or manual backup. The Backup reconciler will get the config from the Backup Plan.  
`description` _string_ | An optional string description of the Backup. This field has no impact on functionality.  
`manual` _boolean_ | Specifies whether the backup resource was created manually. If True, this backup has been created manually, If False, this backup has been created automatically from the backup plan schedule.  
`retainDays` _integer_ | The number of days to keep this backup for, after which it is automatically deleted. This is calculated from the create_time of the backup. If this field is not specified or set to 0, it means the backup is not automatically deleted. For backups automatically created from a a backup schedule, this field is assigned the value of BackupPlan.RetentionPolicy.backup_retain_days. For backups created manually that leave this field unspecified, the service assigns the value of BackupPlan.RetentionPolicy.backup_retain_days. Default to 0.  
  
### HarborInstanceBackupStatus

Defines the observed state of a backup.

_Appears in:_ \- HarborInstanceBackup

Field | Description  
---|---  
`state` _BackupState_ | The current state of the backup.  
`reason` _string_ | A human-readable description of why the backup is in the current state.  
`createTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The timestamp of when this backup resource was created. This can be converted to and from [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt).  
`completeTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The completion time of the backup.  
`retainExpireTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The time when the backup is automatically deleted. It's an output only field calculated from the combined value of create_time and retain_days, and is updated accordingly when the retain_days field of a backup has been updated.  
`totalSizeBytes` _integer_ | The total size for backup measured in bytes.  
`registrySizeBytes` _integer_ | The total size for registry backup handled by data transfer service, measured in bytes.  
`databaseSizeBytes` _integer_ | The total size for database backup handled by Dbcluster export, measured in bytes.  
`exportSubDirectory` _string_ | Subdirectory appended to the Database export location. This will be used when running import during restoration.  
  
### HarborInstanceList

Represents a collection of Harbor container registry instances.

Field | Description  
---|---  
`apiVersion` _string_ | `artifactregistry.gdc.goog/v1`  
`kind` _string_ | `HarborInstanceList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _HarborInstance array_ |   
  
### HarborInstanceProject

Represents a harbor project in a harbor instance. A custom resource establishes the expectation that a project must exist. Namespace is the GDCH project name that the harbor instance and its harbor projects belong to.

_Appears in:_ \- HarborInstanceProjectList

Field | Description  
---|---  
`apiVersion` _string_ | `artifactregistry.gdc.goog/v1`  
`kind` _string_ | `HarborInstanceProject`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _HarborInstanceProjectSpec_ |   
`status` _HarborInstanceProjectStatus_ |   
  
### HarborInstanceProjectList

Contains a list of `HarborInstanceProject` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `artifactregistry.gdc.goog/v1`  
`kind` _string_ | `HarborInstanceProjectList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _HarborInstanceProject array_ |   
  
### HarborInstanceProjectSpec

Defines the specification or expected state of the `HarborProject` object.

_Appears in:_ \- HarborInstanceProject

Field | Description  
---|---  
`projectName` _string_ | The name of the harbor project. Has to match harbor's naming rules.  
`harborInstanceRef` _[LocalObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#localobjectreference-v1-core)_ | The harbor instance that the harbor project belongs to.  
`creatorSubject` _[Subject](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#subject-v1-rbac)_ | The user or group that creates the harbor project, and the subject will be granted as the first harbor Project Admin to manage the harbor project, and grant more users access, at harbor UI. It only represents individual users for now.  
`autoScan` _boolean_ | Whether a project will scan images automatically on push. Defaults to false if not specified.  
  
### HarborInstanceProjectStatus

Defines the observed state of the `HarborInstanceProject` object.

_Appears in:_ \- HarborInstanceProject

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions include `ProjectCreated`, `ProjectDeleted` and `ProjectSubjectAssigned` `ProjectCreated` means that the harbor project is created in the harbor instance with true or false status. `ProjectDeleted` means that the harbor project is deleted in the harbor instance with true or false status. `ProjectSubjectAssigned` means that the user or group who initiates the custom resource creation is granted as first Harbor Admin role in harbor, with true or false status.  
  
### HarborInstanceRestore

Defines the schema for the `Restore` API for HarborInstance.

_Appears in:_ \- HarborInstanceRestoreList

Field | Description  
---|---  
`apiVersion` _string_ | `artifactregistry.gdc.goog/v1`  
`kind` _string_ | `HarborInstanceRestore`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _HarborInstanceRestoreSpec_ | The desired state of the Restore.  
`status` _HarborInstanceRestoreStatus_ | The most recently observed status of the Restore.  
  
### HarborInstanceRestoreList

Represents a collection of Restore for HaaS instance.

Field | Description  
---|---  
`apiVersion` _string_ | `artifactregistry.gdc.goog/v1`  
`kind` _string_ | `HarborInstanceRestoreList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _HarborInstanceRestore array_ |   
  
### HarborInstanceRestoreReference

HarborInstanceRestoreReference represents a Restore Reference to HarborInstanceRestore.

_Appears in:_ \- HarborInstanceSpec

Field | Description  
---|---  
`name` _string_ | name is unique within a namespace to reference a HarborInstanceRestore resource.  
`namespace` _string_ | namespace defines the space within which the HarborInstanceRestore name must be unique.  
  
### HarborInstanceRestoreSpec

Defines the desired state of a restore..

_Appears in:_ \- HarborInstanceRestore

Field | Description  
---|---  
`backupName` _string_ | The full name of the Harbor instance backup resource that this Restore resource uses to restore from.  
`description` _string_ | An optional description of the backup. This has no impact on functionality.  
  
### HarborInstanceRestoreStatus

Defines the observed state of a restore.

_Appears in:_ \- HarborInstanceRestore

Field | Description  
---|---  
`state` _RestoreState_ | The current state of the restore.  
`stateReason` _string_ | A human-readable description of why the restore is in the current state.  
`startTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The create time of the restore process.  
`completeTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The end time of the restore process.  
  
### HarborInstanceSpec

Represents the specification or the desired state of a Harbor instance.

_Appears in:_ \- HarborInstance

Field | Description  
---|---  
`restoreRef` _HarborInstanceRestoreReference_ | The reference of which restore resource this instance is restored by. The field is filled by restore reconciliation and immutable once created.  
`adminAccessRef` _HarborInstanceAdminAccessReference_ | The reference of which credentials provide administrative access to this instance.  
  
### HarborInstanceStatus

Represents the current status of a Harbor instance.

_Appears in:_ \- HarborInstance

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The current state of the HarborInstance. A state of 'Ready` indicates that the HarborInstance is ready.  
`version` _string_ | The version of the Harbor instance.  
`url` _string_ | The URL of Harbor instance's web UI.  
`restoreTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | Restore related status will be empty if the instance is not created by restore flow. The timestamp of when this instance is restored.  
`restoreBackupReference` _HarborInstanceBackupReference_ | The reference of which backup resource this instance is restored from.  
`errorStatus` _ErrorStatus_ | ErrorStatus holds the most recent errors with the observed times included.  
`timeSinceLastReady` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | TimeSinceLastReady holds the time since the last time HarborInstance was ready.  
  
### RestoreState

_Underlying type:_ `string`

_Appears in:_ \- HarborInstanceRestoreStatus

### RetentionPolicy

Defines a policy that determines when to automatically delete backups created under this backup plan, a plan-level minimum number of backup retain days, and a lock to disallow any policy updates.

_Appears in:_ \- HarborInstanceBackupPlanSpec

Field | Description  
---|---  
`backupRetainDays` _integer_ | The number of days after which the service deletes a backup. If specified, a backup created under this backup plan is automatically deleted when it reaches the backup_retain_days after the create_time. If not specified, backups created under this backup plan is not subject to automatic deletion. Updating this field does not affect existing backups under it. Backups created after a successful update automatically inherit the new value.  
  
### Schedule

Represents an inner message type that defines a cron schedule.

_Appears in:_ \- HarborInstanceBackupPlanSpec

Field | Description  
---|---  
`cronSchedule` _string_ | A cron string schedule on which an operation is executed.  
`paused` _boolean_ | Specifies whether the scheduled operation is paused or unpaused. If set to True, the scheduled operation will be paused and no automated backup will be created. Default to False.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
