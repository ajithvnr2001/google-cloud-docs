---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/backup/v1/gkebackup-agent-v1/
title: KRM API gkebackup.gke.io/v1 API \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:59.989245+00:00
---

# KRM API gkebackup.gke.io/v1 API  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/backup/v1/gkebackup-agent-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API gkebackup.gke.io/v1 API Stay organized with collections  Save and categorize content based on your preferences. 

## gkebackup.gke.io/v1

Contains the API schema definitions for the gkebackup.gke.io v1 API group.

### BackupAllRestoreAll

Defines a strategy that backs up everything selected in this component, and restores everything during restoration.

_Appears in:_ \- Strategy

Field | Description  
---|---  
`backupPreHooks` _HookSpec array_ | A list of hooks that are executed before backing up all selected volumes of this component. These are usually the quiesce steps. The execution target Pods are all Pods within this component.  
`backupPostHooks` _HookSpec array_ | A list of hooks that are executed after all volumes of this component are backed up. These are usually the un-quiesce steps. The execution target Pods are all Pods within this component.  
`volumeSelector` _[LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#labelselector-v1-meta)_ | A label selector that is used to select persistent volumes that are backed up and restored within this component. All persistent volumes are selected if this is not provided.  
  
### BackupJobList

Contains a list of backup jobs.

Field | Description  
---|---  
`apiVersion` _string_ | `gkebackup.gke.io/v1`  
`kind` _string_ | `BackupJobList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BackupJob array_ |   
  
### BackupJobSpec

Defines the desired state of the backup job.

_Appears in:_ \- BackupJob

Field | Description  
---|---  
`backupName` _string_ | The control plane backup name that the backup job is executing against. The name is immutable.  
  
### BackupJobStatus

Defines the observed state of the backup job.

_Appears in:_ \- BackupJob

Field | Description  
---|---  
`phase` _BackupJobPhase_ | The current phase of the backup.  
`message` _string_ | A human-readable message indicating details about why the backup is in this state.  
`reason` _string_ | A brief camel case string that describes any update and is used for machine parsing and tidy display.  
  
### BackupOneRestoreAll

Defines a strategy that only backs up volumes from one Pod within this component, and these volumes are restored to all other Pods during restoration. This strategy is used for applications that are deployed in a high-availability configuration of one primary and one or more secondaries. This strategy is exclusively applicable to `StatefulSet` components that use a defined `volumeClaimTemplate` resource to provision volumes.

If a component consists of multiple `Deployment` resources, all deployments must have exactly one replica, all replicas must have the same number of persistent volumes, and all persistent volumes must be defined in the same order. These volumes are defined in the `.spec.template.spec.volumes` field, and non-persistent volumes will be skipped.

If a component consists of multiple `StatefulSet` resources, all `StatefulSet` resources must have the same number of volume claim templates, and all volume claim templates must follow the same order. They are defined in the `.spec.volumeClaimTemplates` field.

_Appears in:_ \- Strategy

Field | Description  
---|---  
`backupTargetName` _string_ | The name of the preferred `Deployment` or `StatefulSet` resource that is used for backup. We selectthe target Pod based on how this component is composed. For multi-`Deployment`, pick the only Pod created by this `Deployment` resource. For multi-`StatefulSet`, pick the first Pod created by the target `StatefulSet` resource. For single-`StatefulSet`, pick the second Pod created by the target `StatefulSet` resource.  
`backupPreHooks` _HookSpec array_ | A list of hooks that are executed before backing up all selected volumes of this component. These are usually the quiesce steps. Hooks are only executed on the selected backup Pod.  
`backupPostHooks` _HookSpec array_ | A list of hooks that are executed after all volumes of this component are backed up. These are usually the un-quiesce steps. Hooks are only executed on selected backup Pod.  
`volumeSelector` _[LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#labelselector-v1-meta)_ | A label selector that is used to select all persistent volumes that are backed up within the target Pod. It is possible that the selector will select volumes outside of the target Pod, but only volumes belonging to the target Pod are backed up. Those volume backups are restored to all other volumes selected by the selector during restoration. All persistent volumes are selected if this is not provided.  
  
### Component

Defines a subset of application resources and their backup and restore strategies. An individual component is represented either by a list of `StatefulSet` or `Deployment` resources.

_Appears in:_ \- ProtectedApplicationSpec

Field | Description  
---|---  
`name` _string_ | The unique name of this component.  
`resourceKind` _ResourceKind_ | The kind of resources included in this component. The resource kind can only be `Deployment` or `StatefulSet` or `Pod`. The `Pod` resource kind only supports the `BackupAllRestoreAll` strategy at this time.  
`resourceNames` _string array_ | The names of resources which belong to this component. It must be a list of names of `Deployment`, `StatefulSet`, or `Pod` resources based on what is defined in the `resourceKind` field.  
`strategy` _Strategy_ | The details of how to back up and restore this component.  
  
### DumpAndLoad

Defines a strategy where backup and restore of a component is achieved using application specific tools for dumping and loading data, like `mysqldump` for MySQL or `pg_dump` for PostgreSQL. Dump files are stored in a dedicated volume. Only the dedicated volumes are selected to be backed up for this strategy. The dump target and load target could be different. This strategy is exclusively applicable to `StatefulSet` components that use a defined `volumeClaimTemplate` resource to provision volumes.

_Appears in:_ \- Strategy

Field | Description  
---|---  
`dumpTarget` _string_ | The name of a preferred `Deployment` or `StatefulSet` resource that is used to dump the component data. We select the target Pod based on how this component is composed. For `Deployment`, pick the only Pod created by the target `Deployment` resource. For single-`StatefulSet`, pick the second Pod created by the target `StatefulSet` resource if the replica number is greater than two. Otherwise, pick the only Pod. For multi-`StatefulSet`, pick the first Pod created by the target `StatefulSet` resource.  
`loadTarget` _string_ | The name of the preferred `Deployment` or `StatefulSet` resource that is used to load the component data. We select the target Pod based on how this component is composed. For `Deployment`, pick the only Pod created by target `Deployment` resource. For `StatefulSet`, always pick the first Pod created by target `StatefulSet` resource.  
`dumpHooks` _HookSpec array_ | A list of hooks that are used to dump the data of this component into a dedicated volume. The execution target Pod is one of the Pods selected from the `DumpTarget` field.  
`backupPostHooks` _HookSpec array_ | A list of hooks that are executed after a dedicated dump volume is backed up. These are usually clean up steps.  
`loadHooks` _HookSpec array_ | A list of hooks that are used to load the data of this component from a dedicated volume. It might include clean up steps after the load is completed. The execution target Pod is one of the Pods selected from the `LoadTarget` field.  
`volumeSelector` _[LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#labelselector-v1-meta)_ | A label selector that must select dedicated volumes that are used to dump and load the application data. Only one volume must be selected in both the `DumpTarget` and `LoadTarget` fields.  
  
### HookFailurePolicy

_Underlying type:_ `string` The desired behavior to take if hook execution runs into error.

_Appears in:_ \- HookSpec

### HookSpec

Defines how a hook is executed in a selected container, assuming the target Pod has been selected.

_Appears in:_ \- BackupAllRestoreAll \- BackupOneRestoreAll \- DumpAndLoad

Field | Description  
---|---  
`name` _string_ | The name of this hook. This field is used to identify the status of hook execution, and any errors that are encountered.  
`container` _string_ | The container that this hook executes on. If unspecified, it executes on the first container of the Pod.  
`command` _string array_ | The command to execute. The hook command to run. For example, `["/sbin/fsfreeze", "--freeze"]`.  
`timeoutSeconds` _integer_ | The timeout of the hook in seconds. If unspecified, the default value is `30`.  
`onError` _HookFailurePolicy_ | The desired behavior to follow when the hook execution runs into an error. Valid values are `Ignore` or `Fail`. If unspecified, the value will be `Fail`.  
  
### ProtectedApplication

Defines the schema for the `Protectedapplication` API.

_Appears in:_ \- ProtectedApplicationList

Field | Description  
---|---  
`apiVersion` _string_ | `gkebackup.gke.io/v1`  
`kind` _string_ | `ProtectedApplication`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ProtectedApplicationSpec_ |   
`status` _ProtectedApplicationStatus_ |   
  
### ProtectedApplicationError

Contains detailed error information for this `ProtectedApplication` resource.

_Appears in:_ \- ProtectedApplicationStatus

Field | Description  
---|---  
`reason` _string_ | A camel case string that describes any error and is used for machine parsing and tidy display.  
`message` _string_ | A human-readable message indicating details about the error.  
  
### ProtectedApplicationList

Contains a list of `ProtectedApplication` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `gkebackup.gke.io/v1`  
`kind` _string_ | `ProtectedApplicationList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ProtectedApplication array_ |   
  
### ProtectedApplicationSpec

Defines relevant resources that belong to a `ProtectedApplication`, and how the given application must be backed up or restored.

_Appears in:_ \- ProtectedApplication

Field | Description  
---|---  
`resourceSelection` _ResourceSelection_ | The resources that belong to this `ProtectedApplication`.  
`components` _Component array_ | The components of this protected application.  
  
### ProtectedApplicationStatus

Defines the status of this `ProtectedApplication` resource.

_Appears in:_ \- ProtectedApplication

Field | Description  
---|---  
`readyToBackup` _boolean_ | Specifies whether this `ProtectedApplication` resource is ready to backup. A `ProtectedApplication` resource is not ready if it contains any errors.  
`error` _ProtectedApplicationError array_ | The errors relating to this protected application. For example, one component configuration is invalid.  
  
### ResourceKind

_Underlying type:_ `string` Defines the kind of the resource.

_Appears in:_ \- Component

### ResourceSelection

Defines how to identify the resources belonging to this application.

_Appears in:_ \- ProtectedApplicationSpec

Field | Description  
---|---  
`type` _ResourceSelectionType_ | The type of application source. The `Type` field must be `ApplicationName` or `Selector`. This is the union discriminator.  
`applicationName` _string_ | The name of a sig-apps application within the same namespace. This is the application the data protection specification applies to.  
`selector` _[LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#labelselector-v1-meta)_ | The resources in the same namespace as the `ProtectedApplication` resource that are selected. The data protection specification is applied to these resources.  
  
### ResourceSelectionType

_Underlying type:_ `string` The types of selection.

_Appears in:_ \- ResourceSelection

### RestoreJob

Defines the schema for the `RestoreJob` API

_Appears in:_ \- RestoreJobList

Field | Description  
---|---  
`apiVersion` _string_ | `gkebackup.gke.io/v1`  
`kind` _string_ | `RestoreJob`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _RestoreJobSpec_ |   
`status` _RestoreJobStatus_ |   
  
### RestoreJobList

Contains a list of `RestoreJob` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `gkebackup.gke.io/v1`  
`kind` _string_ | `RestoreJobList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _RestoreJob array_ |   
  
### RestoreJobSpec

Defines the desired state of a restoration.

_Appears in:_ \- RestoreJob

Field | Description  
---|---  
`restoreName` _string_ | RestoreName is the control plane Restore name that the RestoreJob is executing against. The name is immutable.  
  
### RestoreJobStatus

Defines the observed state of a restore job.

_Appears in:_ \- RestoreJob

Field | Description  
---|---  
`phase` _RestoreJobPhase_ | The current status of a restore.  
`message` _string_ | A human-readable message indicating details about why the backup restoration is in this state.  
`reason` _string_ | A camel case string that describes any update and is used for machine parsing and tidy display.  
  
### Strategy

Defines how to back up and restore for a particular component. It must be one of `BackupAllRestoreAll`, `BackupOneRestoreAll`, or `DumpAndLoad`.

_Appears in:_ \- Component

Field | Description  
---|---  
`type` _StrategyType_ | The type of backup and restore strategy. The value can only be either `BackupAllRestoreAll`, `BackupOneRestoreAll`, or `DumpAndLoad`. Note, the `Pod` resource kind only supports the `BackupAllRestoreAll` strategy. This is the union discriminator.  
`backupAllRestoreAll` _BackupAllRestoreAll_ | A strategy that backs up everything selected in this component, and restores everything during restoration.  
`backupOneRestoreAll` _BackupOneRestoreAll_ | A strategy that only backs up volumes from one Pod within this component, and are restored to all other Pods during restoration. This strategy is used for applications that are deployed in a high availability configuration of one primary and one or more secondaries. This strategy is exclusively applicable to `StatefulSet` components that use a defined `volumeClaimTemplate` resource to provision volumes.  
`dumpAndLoad` _DumpAndLoad_ | A strategy where the backup and restore of a component is achieved using application specific tools for dumping and loading data, like `mysqldump` for MySQL or `pg_dump` for PostgreSQL. Dump files are stored in a dedicated volume. Only the dedicated volume must be selected to be backed up for this strategy. The dump target and load target could be different. This strategy is exclusively applicable to `StatefulSet` components that use a defined `volumeClaimTemplate` resource to provision volumes.  
  
### StrategyType

_Underlying type:_ `string` Defines the backup and restore strategies of a component.

_Appears in:_ \- Strategy

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
