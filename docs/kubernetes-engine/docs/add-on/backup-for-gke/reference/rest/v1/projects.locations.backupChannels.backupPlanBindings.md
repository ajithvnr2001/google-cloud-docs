---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels.backupPlanBindings
title: REST Resource: projects.locations.backupChannels.backupPlanBindings \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:18.210924+00:00
---

# REST Resource: projects.locations.backupChannels.backupPlanBindings  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels.backupPlanBindings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ APIs & Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest)



Send feedback 

#  REST Resource: projects.locations.backupChannels.backupPlanBindings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: BackupPlanBinding
    * JSON representation
  * BackupPlanDetails
    * JSON representation
  * State
  * BackupConfigDetails
    * JSON representation
  * RetentionPolicyDetails
    * JSON representation
  * Methods



## Resource: BackupPlanBinding

A BackupPlanBinding binds a BackupPlan with a BackupChannel. This resource is created automatically when a BackupPlan is created using a BackupChannel. This also serves as a holder for cross-project fields that need to be displayed in the current project.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "createTime": string,
      "updateTime": string,
      "backupPlan": string,
      "cluster": string,
      "backupPlanDetails": {
        object ([BackupPlanDetails](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels.backupPlanBindings#BackupPlanDetails))
      },
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The fully qualified name of the BackupPlanBinding. `projects/*/locations/*/backupChannels/*/backupPlanBindings/*`  
`uid` |  `string` Output only. Server generated global unique identifier of [UUID4](https://en.wikipedia.org/wiki/Universally_unique_identifier)  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this binding was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this binding was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`backupPlan` |  `string` Output only. Immutable. The fully qualified name of the BackupPlan bound with the parent BackupChannel. `projects/*/locations/*/backupPlans/{backupPlan}`  
`cluster` |  `string` Output only. Immutable. The fully qualified name of the cluster that is being backed up Valid formats:

  * `projects/*/locations/*/clusters/*`
  * `projects/*/zones/*/clusters/*`

  
`backupPlanDetails` |  `object (`[BackupPlanDetails](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels.backupPlanBindings#BackupPlanDetails)`)` Output only. Contains details about the backup plan/backup.  
`etag` |  `string` Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a BackupPlanBinding from overwriting each other. It is strongly suggested that systems make use of the 'etag' in the read-modify-write cycle to perform BackupPlanBinding updates in order to avoid race conditions: An `etag` is returned in the response to `backupPlanBindings.get`, and systems are expected to put that etag in the request to `UpdateBackupPlanBinding` or `DeleteBackupPlanBinding` to ensure that their change will be applied to the same version of the resource.  
  
## BackupPlanDetails

Contains metadata about the backup plan/backup.

JSON representation  
---  
      
    
    {
      "protectedPodCount": integer,
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels.backupPlanBindings#State)),
      "lastSuccessfulBackupTime": string,
      "nextScheduledBackupTime": string,
      "rpoRiskLevel": integer,
      "lastSuccessfulBackup": string,
      "backupConfigDetails": {
        object ([BackupConfigDetails](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels.backupPlanBindings#BackupConfigDetails))
      },
      "retentionPolicyDetails": {
        object ([RetentionPolicyDetails](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels.backupPlanBindings#RetentionPolicyDetails))
      }
    }  
  
Fields  
---  
`protectedPodCount` |  `integer` Output only. The number of Kubernetes Pods backed up in the last successful Backup created via this BackupPlan.  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels.backupPlanBindings#State)`)` Output only. State of the BackupPlan.  
`lastSuccessfulBackupTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Completion time of the last successful Backup. This is sourced from a successful Backup's completeTime field.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`nextScheduledBackupTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Start time of next scheduled backup under this BackupPlan by either cronSchedule or rpo config. This is sourced from BackupPlan.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`rpoRiskLevel` |  `integer` Output only. A number that represents the current risk level of this BackupPlan from RPO perspective with 1 being no risk and 5 being highest risk.  
`lastSuccessfulBackup` |  `string` Output only. The fully qualified name of the last successful Backup created under this BackupPlan. `projects/*/locations/*/backupPlans/*/backups/*`  
`backupConfigDetails` |  `object (`[BackupConfigDetails](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels.backupPlanBindings#BackupConfigDetails)`)` Output only. Contains details about the BackupConfig of Backups created via this BackupPlan.  
`retentionPolicyDetails` |  `object (`[RetentionPolicyDetails](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels.backupPlanBindings#RetentionPolicyDetails)`)` Output only. Contains details about the RetentionPolicy of Backups created via this BackupPlan.  
  
## State

State

Enums  
---  
`STATE_UNSPECIFIED` | Default first value for Enums.  
`CLUSTER_PENDING` | Waiting for cluster state to be RUNNING.  
`PROVISIONING` | The BackupPlan is in the process of being created.  
`READY` | The BackupPlan has successfully been created and is ready for Backups.  
`FAILED` | BackupPlan creation has failed.  
`DEACTIVATED` | The BackupPlan has been deactivated.  
`DELETING` | The BackupPlan is in the process of being deleted.  
  
## BackupConfigDetails

BackupConfigDetails defines the configuration of Backups created via this BackupPlan.

JSON representation  
---  
      
    
    {
      "includeVolumeData": boolean,
      "includeSecrets": boolean,
      "encryptionKey": {
        object ([EncryptionKey](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/EncryptionKey))
      },
    
      // Union field backup_scope can be only one of the following:
      "allNamespaces": boolean,
      "selectedNamespaces": {
        object ([Namespaces](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/Namespaces))
      },
      "selectedApplications": {
        object ([NamespacedNames](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/NamespacedNames))
      }
      // End of list of possible types for union field backup_scope.
    }  
  
Fields  
---  
`includeVolumeData` |  `boolean` Output only. This flag specifies whether volume data should be backed up when PVCs are included in the scope of a Backup.Default: False  
`includeSecrets` |  `boolean` Output only. This flag specifies whether Kubernetes Secret resources should be included when they fall into the scope of Backups.Default: False  
`encryptionKey` |  `object (`[EncryptionKey](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/EncryptionKey)`)` Output only. This defines a customer managed encryption key that will be used to encrypt the "config" portion (the Kubernetes resources) of Backups created via this plan.Default (empty): Config backup artifacts will not be encrypted.  
Union field `backup_scope`. This defines the "scope" of the Backup - which namespaced resources in the cluster will be included in a Backup. Exactly one of the fields of backup_scope MUST be specified. `backup_scope` can be only one of the following:  
`allNamespaces` |  `boolean` Output only. If True, include all namespaced resources  
`selectedNamespaces` |  `object (`[Namespaces](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/Namespaces)`)` Output only. If set, include just the resources in the listed namespaces.  
`selectedApplications` |  `object (`[NamespacedNames](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/NamespacedNames)`)` Output only. If set, include just the resources referenced by the listed ProtectedApplications.  
  
## RetentionPolicyDetails

RetentionPolicyDetails defines a Backup retention policy for a BackupPlan.

JSON representation  
---  
      
    
    {
      "backupDeleteLockDays": integer,
      "backupRetainDays": integer
    }  
  
Fields  
---  
`backupDeleteLockDays` |  `integer` Optional. Minimum age for Backups created via this BackupPlan (in days). This field MUST be an integer value between 0-90 (inclusive). A Backup created under this BackupPlan will NOT be deletable until it reaches Backup's (createTime + backupDeleteLockDays). Updating this field of a BackupPlan does NOT affect existing Backups under it. Backups created AFTER a successful update will inherit the new value.Default: 0 (no delete blocking)  
`backupRetainDays` |  `integer` Optional. The default maximum age of a Backup created via this BackupPlan. This field MUST be an integer value >= 0 and <= 365. If specified, a Backup created under this BackupPlan will be automatically deleted after its age reaches (createTime + backupRetainDays). If not specified, Backups created under this BackupPlan will NOT be subject to automatic deletion. Default: 0 (no automatic deletion)  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels.backupPlanBindings/get)`

|  Retrieve the details of a single BackupPlanBinding.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels.backupPlanBindings/list)`

|  Lists BackupPlanBindings in a given location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
