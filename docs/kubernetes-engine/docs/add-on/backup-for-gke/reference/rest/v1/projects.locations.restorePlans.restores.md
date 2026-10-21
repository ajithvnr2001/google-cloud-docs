---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores
title: REST Resource: projects.locations.restorePlans.restores \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:00.100748+00:00
---

# REST Resource: projects.locations.restorePlans.restores  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ APIs & Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest)



Send feedback 

#  REST Resource: projects.locations.restorePlans.restores Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Restore
    * JSON representation
  * State
  * Filter
    * JSON representation
  * ResourceSelector
    * JSON representation
  * VolumeDataRestorePolicyOverride
    * JSON representation
  * Methods



## Resource: Restore

Represents both a request to Restore some portion of a Backup into a target GKE cluster and a record of the restore operation itself.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "createTime": string,
      "updateTime": string,
      "description": string,
      "backup": string,
      "cluster": string,
      "restoreConfig": {
        object ([RestoreConfig](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig))
      },
      "labels": {
        string: string,
        ...
      },
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores#State)),
      "stateReason": string,
      "troubleshootingInfo": {
        object ([TroubleshootingInfo](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/TroubleshootingInfo))
      },
      "completeTime": string,
      "resourcesRestoredCount": integer,
      "resourcesExcludedCount": integer,
      "resourcesFailedCount": integer,
      "volumesRestoredCount": integer,
      "etag": string,
      "filter": {
        object ([Filter](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores#Filter))
      },
      "volumeDataRestorePolicyOverrides": [
        {
          object ([VolumeDataRestorePolicyOverride](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores#VolumeDataRestorePolicyOverride))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The full name of the Restore resource. Format: `projects/*/locations/*/restorePlans/*/restores/*`  
`uid` |  `string` Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this Restore resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this Restore resource was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`description` |  `string` Optional. User specified descriptive string for this Restore.  
`backup` |  `string` Required. Immutable. A reference to the `[Backup](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups#Backup)` used as the source from which this Restore will restore. Note that this Backup must be a sub-resource of the RestorePlan's `[backupPlan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans#RestorePlan.FIELDS.backup_plan)`. Format: `projects/*/locations/*/backupPlans/*/backups/*`.  
`cluster` |  `string` Output only. The target cluster into which this Restore will restore data. Valid formats:

  * `projects/*/locations/*/clusters/*`
  * `projects/*/zones/*/clusters/*`

Inherited from parent RestorePlan's `[cluster](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans#RestorePlan.FIELDS.cluster)` value.  
`restoreConfig` |  `object (`[RestoreConfig](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig)`)` Output only. Configuration of the Restore. Inherited from parent RestorePlan's `[restoreConfig](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans#RestorePlan.FIELDS.restore_config)`.  
`labels` |  `map (key: string, value: string)` A set of custom labels supplied by user.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores#State)`)` Output only. The current state of the Restore.  
`stateReason` |  `string` Output only. Human-readable description of why the Restore is in its current state. This field is only meant for human readability and should not be used programmatically as this field is not guaranteed to be consistent.  
`troubleshootingInfo` |  `object (`[TroubleshootingInfo](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/TroubleshootingInfo)`)` Output only. Information about the troubleshooting steps which will provide debugging information to the end users.  
`completeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp of when the restore operation completed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`resourcesRestoredCount` |  `integer` Output only. Number of resources restored during the restore execution.  
`resourcesExcludedCount` |  `integer` Output only. Number of resources excluded during the restore execution.  
`resourcesFailedCount` |  `integer` Output only. Number of resources that failed to be restored during the restore execution.  
`volumesRestoredCount` |  `integer` Output only. Number of volumes restored during the restore execution.  
`etag` |  `string` Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a restore from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform restore updates in order to avoid race conditions: An `etag` is returned in the response to `restores.get`, and systems are expected to put that etag in the request to `restores.patch` or `restores.delete` to ensure that their change will be applied to the same version of the resource.  
`filter` |  `object (`[Filter](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores#Filter)`)` Optional. Immutable. Filters resources for `Restore`. If not specified, the scope of the restore will remain the same as defined in the `RestorePlan`. If this is specified and no resources are matched by the `inclusionFilters` or everything is excluded by the `exclusionFilters`, nothing will be restored. This filter can only be specified if the value of `[namespacedResourceRestoreMode](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#FIELDS.namespaced_resource_restore_mode)` is set to `MERGE_SKIP_ON_CONFLICT`, `MERGE_REPLACE_VOLUME_ON_CONFLICT` or `MERGE_REPLACE_ON_CONFLICT`.  
`volumeDataRestorePolicyOverrides[]` |  `object (`[VolumeDataRestorePolicyOverride](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores#VolumeDataRestorePolicyOverride)`)` Optional. Immutable. Overrides the volume data restore policies selected in the Restore Config for override-scoped resources.  
  
## State

Possible values for state of the Restore.

Enums  
---  
`STATE_UNSPECIFIED` | The Restore resource is in the process of being created.  
`CREATING` | The Restore resource has been created and the associated RestoreJob Kubernetes resource has been injected into target cluster.  
`IN_PROGRESS` | The gkebackup agent in the cluster has begun executing the restore operation.  
`SUCCEEDED` | The restore operation has completed successfully. Restored workloads may not yet be operational.  
`FAILED` | The restore operation has failed.  
`DELETING` | This Restore resource is in the process of being deleted.  
`VALIDATING` | The Kubernetes resources created by this Restore are being validated.  
  
## Filter

Defines the filter for `Restore`. This filter can be used to further refine the resource selection of the `Restore` beyond the coarse-grained scope defined in the `RestorePlan`. `exclusionFilters` take precedence over `inclusionFilters`. If a resource matches both `inclusionFilters` and `exclusionFilters`, it will not be restored.

JSON representation  
---  
      
    
    {
      "inclusionFilters": [
        {
          object ([ResourceSelector](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores#ResourceSelector))
        }
      ],
      "exclusionFilters": [
        {
          object ([ResourceSelector](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores#ResourceSelector))
        }
      ]
    }  
  
Fields  
---  
`inclusionFilters[]` |  `object (`[ResourceSelector](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores#ResourceSelector)`)` Optional. Selects resources for restoration. If specified, only resources which match `inclusionFilters` will be selected for restoration. A resource will be selected if it matches any `ResourceSelector` of the `inclusionFilters`.  
`exclusionFilters[]` |  `object (`[ResourceSelector](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores#ResourceSelector)`)` Optional. Excludes resources from restoration. If specified, a resource will not be restored if it matches any `ResourceSelector` of the `exclusionFilters`.  
  
## ResourceSelector

Defines a selector to identify a single or a group of resources. Conditions in the selector are optional, but at least one field should be set to a non-empty value. If a condition is not specified, no restrictions will be applied on that dimension. If more than one condition is specified, a resource will be selected if and only if all conditions are met.

JSON representation  
---  
      
    
    {
      "groupKind": {
        object ([GroupKind](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/GroupKind))
      },
      "name": string,
      "namespace": string,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`groupKind` |  `object (`[GroupKind](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/GroupKind)`)` Optional. Selects resources using their Kubernetes GroupKinds. If specified, only resources of provided GroupKind will be selected.  
`name` |  `string` Optional. Selects resources using their resource names. If specified, only resources with the provided name will be selected.  
`namespace` |  `string` Optional. Selects resources using their namespaces. This only applies to namespace scoped resources and cannot be used for selecting cluster scoped resources. If specified, only resources in the provided namespace will be selected. If not specified, the filter will apply to both cluster scoped and namespace scoped resources (e.g. name or label). The [Namespace](https://pkg.go.dev/k8s.io/api/core/v1#Namespace) resource itself will be restored if and only if any resources within the namespace are restored.  
`labels` |  `map (key: string, value: string)` Optional. Selects resources using Kubernetes [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). If specified, a resource will be selected if and only if the resource has all of the provided labels and all the label values match.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## VolumeDataRestorePolicyOverride

Defines an override to apply a VolumeDataRestorePolicy for scoped resources.

JSON representation  
---  
      
    
    {
      "policy": enum ([VolumeDataRestorePolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/VolumeDataRestorePolicy)),
    
      // Union field scope can be only one of the following:
      "selectedPvcs": {
        object ([NamespacedNames](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/NamespacedNames))
      }
      // End of list of possible types for union field scope.
    }  
  
Fields  
---  
`policy` |  `enum (`[VolumeDataRestorePolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/VolumeDataRestorePolicy)`)` Required. The VolumeDataRestorePolicy to apply when restoring volumes in scope.  
Union field `scope`.`scope` can be only one of the following:  
`selectedPvcs` |  `object (`[NamespacedNames](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/NamespacedNames)`)` A list of PVCs to apply the policy override to.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores/create)`

|  Creates a new Restore for the given RestorePlan.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores/delete)`

|  Deletes an existing Restore.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores/get)`

|  Retrieves the details of a single Restore.  
  
### `[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores/list)`

|  Lists the Restores for a given RestorePlan.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores/patch)`

|  Update a Restore.  
  
### `[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
