---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig/
title: RestoreConfig \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:02.686758+00:00
---

# RestoreConfig  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ APIs & Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest)



Send feedback 

#  RestoreConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ClusterResourceConflictPolicy
  * NamespacedResourceRestoreMode
  * ClusterResourceRestoreScope
    * JSON representation
  * SubstitutionRule
    * JSON representation
  * TransformationRule
    * JSON representation
  * TransformationRuleAction
    * JSON representation
  * Op
  * ResourceFilter
    * JSON representation
  * VolumeDataRestorePolicyBinding
    * JSON representation
  * VolumeType
  * RestoreOrder
    * JSON representation
  * GroupKindDependency
    * JSON representation



Configuration of a restore.

JSON representation  
---  
      
    
    {
      "volumeDataRestorePolicy": enum ([VolumeDataRestorePolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/VolumeDataRestorePolicy)),
      "clusterResourceConflictPolicy": enum ([ClusterResourceConflictPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#ClusterResourceConflictPolicy)),
      "namespacedResourceRestoreMode": enum ([NamespacedResourceRestoreMode](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#NamespacedResourceRestoreMode)),
      "clusterResourceRestoreScope": {
        object ([ClusterResourceRestoreScope](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#ClusterResourceRestoreScope))
      },
      "substitutionRules": [
        {
          object ([SubstitutionRule](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#SubstitutionRule))
        }
      ],
      "transformationRules": [
        {
          object ([TransformationRule](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#TransformationRule))
        }
      ],
      "volumeDataRestorePolicyBindings": [
        {
          object ([VolumeDataRestorePolicyBinding](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#VolumeDataRestorePolicyBinding))
        }
      ],
      "restoreOrder": {
        object ([RestoreOrder](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#RestoreOrder))
      },
    
      // Union field namespaced_resource_restore_scope can be only one of the
      // following:
      "allNamespaces": boolean,
      "selectedNamespaces": {
        object ([Namespaces](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/Namespaces))
      },
      "selectedApplications": {
        object ([NamespacedNames](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/NamespacedNames))
      },
      "noNamespaces": boolean,
      "excludedNamespaces": {
        object ([Namespaces](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/Namespaces))
      }
      // End of list of possible types for union field
      // namespaced_resource_restore_scope.
    }  
  
Fields  
---  
`volumeDataRestorePolicy` |  `enum (`[VolumeDataRestorePolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/VolumeDataRestorePolicy)`)` Optional. Specifies the mechanism to be used to restore volume data. Default: VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED (will be treated as NO_VOLUME_DATA_RESTORATION).  
`clusterResourceConflictPolicy` |  `enum (`[ClusterResourceConflictPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#ClusterResourceConflictPolicy)`)` Optional. Defines the behavior for handling the situation where cluster-scoped resources being restored already exist in the target cluster. This MUST be set to a value other than CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED if `[clusterResourceRestoreScope](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#FIELDS.cluster_resource_restore_scope)` is not empty.  
`namespacedResourceRestoreMode` |  `enum (`[NamespacedResourceRestoreMode](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#NamespacedResourceRestoreMode)`)` Optional. Defines the behavior for handling the situation where sets of namespaced resources being restored already exist in the target cluster. This MUST be set to a value other than NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED.  
`clusterResourceRestoreScope` |  `object (`[ClusterResourceRestoreScope](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#ClusterResourceRestoreScope)`)` Optional. Identifies the cluster-scoped resources to restore from the Backup. Not specifying it means NO cluster resource will be restored.  
`substitutionRules[]` |  `object (`[SubstitutionRule](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#SubstitutionRule)`)` Optional. A list of transformation rules to be applied against Kubernetes resources as they are selected for restoration from a Backup. Rules are executed in order defined - this order matters, as changes made by a rule may impact the filtering logic of subsequent rules. An empty list means no substitution will occur.  
`transformationRules[]` |  `object (`[TransformationRule](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#TransformationRule)`)` Optional. A list of transformation rules to be applied against Kubernetes resources as they are selected for restoration from a Backup. Rules are executed in order defined - this order matters, as changes made by a rule may impact the filtering logic of subsequent rules. An empty list means no transformation will occur.  
`volumeDataRestorePolicyBindings[]` |  `object (`[VolumeDataRestorePolicyBinding](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#VolumeDataRestorePolicyBinding)`)` Optional. A table that binds volumes by their scope to a restore policy. Bindings must have a unique scope. Any volumes not scoped in the bindings are subject to the policy defined in volumeDataRestorePolicy.  
`restoreOrder` |  `object (`[RestoreOrder](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#RestoreOrder)`)` Optional. RestoreOrder contains custom ordering to use on a Restore.  
Union field `namespaced_resource_restore_scope`. Specifies the namespaced resources to restore from the Backup. Only one of the entries may be specified. If not specified, NO namespaced resources will be restored.Note: Resources will never be restored into _managed_ namespaces such as `kube-system`, `kube-public`, or `kube-node-lease`. These namespaces are silently skipped when `[all_namespaces](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#FIELDS.all_namespaces)` is selected. Listing them explicitly will result in an error. `namespaced_resource_restore_scope` can be only one of the following:  
`allNamespaces` |  `boolean` Restore all namespaced resources in the Backup if set to "True". Specifying this field to "False" is an error.  
`selectedNamespaces` |  `object (`[Namespaces](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/Namespaces)`)` A list of selected Namespaces to restore from the Backup. The listed Namespaces and all resources contained in them will be restored.  
`selectedApplications` |  `object (`[NamespacedNames](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/NamespacedNames)`)` A list of selected ProtectedApplications to restore. The listed ProtectedApplications and all the resources to which they refer will be restored.  
`noNamespaces` |  `boolean` Do not restore any namespaced resources if set to "True". Specifying this field to "False" is not allowed.  
`excludedNamespaces` |  `object (`[Namespaces](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/Namespaces)`)` A list of selected namespaces excluded from restoration. All namespaces except those in this list will be restored.  
  
## ClusterResourceConflictPolicy

Defines the behavior for handling the situation where cluster-scoped resources being restored already exist in the target cluster.

Enums  
---  
`CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED` | Unspecified. Only allowed if no cluster-scoped resources will be restored.  
`USE_EXISTING_VERSION` | Do not attempt to restore the conflicting resource.  
`USE_BACKUP_VERSION` | Delete the existing version before re-creating it from the Backup. This is a dangerous option which could cause unintentional data loss if used inappropriately. For example, deleting a CRD will cause Kubernetes to delete all CRs of that type.  
  
## NamespacedResourceRestoreMode

Defines the behavior for handling the situation where sets of namespaced resources being restored already exist in the target cluster.

Enums  
---  
`NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED` | Unspecified (invalid).  
`DELETE_AND_RESTORE` | When conflicting top-level resources (either Namespaces or ProtectedApplications, depending upon the scope) are encountered, this will first trigger a delete of the conflicting resource AND ALL OF ITS REFERENCED RESOURCES (e.g., all resources in the Namespace or all resources referenced by the ProtectedApplication) before restoring the resources from the Backup. This mode should only be used when you are intending to revert some portion of a cluster to an earlier state.  
`FAIL_ON_CONFLICT` | If conflicting top-level resources (either Namespaces or ProtectedApplications, depending upon the scope) are encountered at the beginning of a restore process, the Restore will fail. If a conflict occurs during the restore process itself (e.g., because an out of band process creates conflicting resources), a conflict will be reported.  
`MERGE_SKIP_ON_CONFLICT` | This mode merges the backup and the target cluster and skips the conflicting resources. If a single resource to restore exists in the cluster before restoration, the resource will be skipped, otherwise it will be restored.  
`MERGE_REPLACE_VOLUME_ON_CONFLICT` | This mode merges the backup and the target cluster and skips the conflicting resources except volume data. If a PVC to restore already exists, this mode will restore/reconnect the volume without overwriting the PVC. It is similar to MERGE_SKIP_ON_CONFLICT except that it will apply the volume data policy for the conflicting PVCs: - RESTORE_VOLUME_DATA_FROM_BACKUP: restore data only and respect the reclaim policy of the original PV; - REUSE_VOLUME_HANDLE_FROM_BACKUP: reconnect and respect the reclaim policy of the original PV; - NO_VOLUME_DATA_RESTORATION: new provision and respect the reclaim policy of the original PV. Note that this mode could cause data loss as the original PV can be retained or deleted depending on its reclaim policy.  
`MERGE_REPLACE_ON_CONFLICT` | This mode merges the backup and the target cluster and replaces the conflicting resources with the ones in the backup. If a single resource to restore exists in the cluster before restoration, the resource will be replaced with the one from the backup. To replace an existing resource, the first attempt is to update the resource to match the one from the backup; if the update fails, the second attempt is to delete the resource and restore it from the backup. Note that this mode could cause data loss as it replaces the existing resources in the target cluster, and the original PV can be retained or deleted depending on its reclaim policy.  
  
## ClusterResourceRestoreScope

Defines the scope of cluster-scoped resources to restore.

Some group kinds are not reasonable choices for a restore, and will cause an error if selected here. Any scope selection that would restore "all valid" resources automatically excludes these group kinds. - Node - ComponentStatus - gkebackup.gke.io/BackupJob - gkebackup.gke.io/RestoreJob - metrics.k8s.io/NodeMetrics - migration.k8s.io/StorageState - migration.k8s.io/StorageVersionMigration - snapshot.storage.k8s.io/VolumeSnapshotContent - storage.k8s.io/CSINode - storage.k8s.io/VolumeAttachment

Some group kinds are driven by restore configuration elsewhere, and will cause an error if selected here. - Namespace - PersistentVolume

JSON representation  
---  
      
    
    {
      "selectedGroupKinds": [
        {
          object ([GroupKind](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/GroupKind))
        }
      ],
      "excludedGroupKinds": [
        {
          object ([GroupKind](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/GroupKind))
        }
      ],
      "allGroupKinds": boolean,
      "noGroupKinds": boolean
    }  
  
Fields  
---  
`selectedGroupKinds[]` |  `object (`[GroupKind](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/GroupKind)`)` Optional. A list of cluster-scoped resource group kinds to restore from the backup. If specified, only the selected resources will be restored. Mutually exclusive to any other field in the message.  
`excludedGroupKinds[]` |  `object (`[GroupKind](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/GroupKind)`)` Optional. A list of cluster-scoped resource group kinds to NOT restore from the backup. If specified, all valid cluster-scoped resources will be restored except for those specified in the list. Mutually exclusive to any other field in the message.  
`allGroupKinds` |  `boolean` Optional. If True, all valid cluster-scoped resources will be restored. Mutually exclusive to any other field in the message.  
`noGroupKinds` |  `boolean` Optional. If True, no cluster-scoped resources will be restored. This has the same restore scope as if the message is not defined. Mutually exclusive to any other field in the message.  
  
## SubstitutionRule

A transformation rule to be applied against Kubernetes resources as they are selected for restoration from a Backup. A rule contains both filtering logic (which resources are subject to substitution) and substitution logic.

JSON representation  
---  
      
    
    {
      "targetNamespaces": [
        string
      ],
      "targetGroupKinds": [
        {
          object ([GroupKind](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/GroupKind))
        }
      ],
      "targetJsonPath": string,
      "originalValuePattern": string,
      "newValue": string
    }  
  
Fields  
---  
`targetNamespaces[]` |  `string` Optional. (Filtering parameter) Any resource subject to substitution must be contained within one of the listed Kubernetes Namespace in the Backup. If this field is not provided, no namespace filtering will be performed (all resources in all Namespaces, including all cluster-scoped resources, will be candidates for substitution). To mix cluster-scoped and namespaced resources in the same rule, use an empty string ("") as one of the target namespaces.  
`targetGroupKinds[]` |  `object (`[GroupKind](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/GroupKind)`)` Optional. (Filtering parameter) Any resource subject to substitution must belong to one of the listed "types". If this field is not provided, no type filtering will be performed (all resources of all types matching previous filtering parameters will be candidates for substitution).  
`targetJsonPath` |  `string` Required. This is a [JSONPath](https://kubernetes.io/docs/reference/kubectl/jsonpath/) expression that matches specific fields of candidate resources and it operates as both a filtering parameter (resources that are not matched with this expression will not be candidates for substitution) as well as a field identifier (identifies exactly which fields out of the candidate resources will be modified).  
`originalValuePattern` |  `string` Optional. (Filtering parameter) This is a [regular expression](https://en.wikipedia.org/wiki/Regular_expression) that is compared against the fields matched by the targetJsonPath expression (and must also have passed the previous filters). Substitution will not be performed against fields whose value does not match this expression. If this field is NOT specified, then ALL fields matched by the targetJsonPath expression will undergo substitution. Note that an empty (e.g., "", rather than unspecified) value for this field will only match empty fields.  
`newValue` |  `string` Optional. This is the new value to set for any fields that pass the filtering and selection criteria. To remove a value from a Kubernetes resource, either leave this field unspecified, or set it to the empty string ("").  
  
## TransformationRule

A transformation rule to be applied against Kubernetes resources as they are selected for restoration from a Backup. A rule contains both filtering logic (which resources are subject to transform) and transformation logic.

JSON representation  
---  
      
    
    {
      "fieldActions": [
        {
          object ([TransformationRuleAction](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#TransformationRuleAction))
        }
      ],
      "resourceFilter": {
        object ([ResourceFilter](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#ResourceFilter))
      },
      "description": string
    }  
  
Fields  
---  
`fieldActions[]` |  `object (`[TransformationRuleAction](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#TransformationRuleAction)`)` Required. A list of transformation rule actions to take against candidate resources. Actions are executed in order defined - this order matters, as they could potentially interfere with each other and the first operation could affect the outcome of the second operation.  
`resourceFilter` |  `object (`[ResourceFilter](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#ResourceFilter)`)` Optional. This field is used to specify a set of fields that should be used to determine which resources in backup should be acted upon by the supplied transformation rule actions, and this will ensure that only specific resources are affected by transformation rule actions.  
`description` |  `string` Optional. The description is a user specified string description of the transformation rule.  
  
## TransformationRuleAction

TransformationRuleAction defines a TransformationRule action based on the JSON Patch RFC (<https://www.rfc-editor.org/rfc/rfc6902>)

JSON representation  
---  
      
    
    {
      "op": enum ([Op](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#Op)),
      "fromPath": string,
      "path": string,
      "value": string
    }  
  
Fields  
---  
`op` |  `enum (`[Op](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#Op)`)` Required. op specifies the operation to perform.  
`fromPath` |  `string` Optional. A string containing a JSON Pointer value that references the location in the target document to move the value from.  
`path` |  `string` Optional. A string containing a JSON-Pointer value that references a location within the target document where the operation is performed.  
`value` |  `string` Optional. A string that specifies the desired value in string format to use for transformation.  
  
## Op

Possible values for operations of a transformation rule action.

Enums  
---  
`OP_UNSPECIFIED` | Unspecified operation  
`REMOVE` | The "remove" operation removes the value at the target location.  
`MOVE` | The "move" operation removes the value at a specified location and adds it to the target location.  
`COPY` | The "copy" operation copies the value at a specified location to the target location.  
`ADD` | The "add" operation performs one of the following functions, depending upon what the target location references: 1. If the target location specifies an array index, a new value is inserted into the array at the specified index. 2. If the target location specifies an object member that does not already exist, a new member is added to the object. 3. If the target location specifies an object member that does exist, that member's value is replaced.  
`TEST` | The "test" operation tests that a value at the target location is equal to a specified value.  
`REPLACE` | The "replace" operation replaces the value at the target location with a new value. The operation object MUST contain a "value" member whose content specifies the replacement value.  
  
## ResourceFilter

ResourceFilter specifies matching criteria to limit the scope of a change to a specific set of kubernetes resources that are selected for restoration from a backup.

JSON representation  
---  
      
    
    {
      "namespaces": [
        string
      ],
      "groupKinds": [
        {
          object ([GroupKind](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/GroupKind))
        }
      ],
      "jsonPath": string
    }  
  
Fields  
---  
`namespaces[]` |  `string` Optional. (Filtering parameter) Any resource subject to transformation must be contained within one of the listed Kubernetes Namespace in the Backup. If this field is not provided, no namespace filtering will be performed (all resources in all Namespaces, including all cluster-scoped resources, will be candidates for transformation).  
`groupKinds[]` |  `object (`[GroupKind](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/GroupKind)`)` Optional. (Filtering parameter) Any resource subject to transformation must belong to one of the listed "types". If this field is not provided, no type filtering will be performed (all resources of all types matching previous filtering parameters will be candidates for transformation).  
`jsonPath` |  `string` Optional. This is a [JSONPath](https://github.com/json-path/JsonPath/blob/master/README.md) expression that matches specific fields of candidate resources and it operates as a filtering parameter (resources that are not matched with this expression will not be candidates for transformation).  
  
## VolumeDataRestorePolicyBinding

Binds resources in the scope to the given VolumeDataRestorePolicy.

JSON representation  
---  
      
    
    {
      "policy": enum ([VolumeDataRestorePolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/VolumeDataRestorePolicy)),
    
      // Union field scope can be only one of the following:
      "volumeType": enum ([VolumeType](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#VolumeType))
      // End of list of possible types for union field scope.
    }  
  
Fields  
---  
`policy` |  `enum (`[VolumeDataRestorePolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/VolumeDataRestorePolicy)`)` Required. The VolumeDataRestorePolicy to apply when restoring volumes in scope.  
Union field `scope`.`scope` can be only one of the following:  
`volumeType` |  `enum (`[VolumeType](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#VolumeType)`)` The volume type, as determined by the PVC's bound PV, to apply the policy to.  
  
## VolumeType

Supported volume types.

Enums  
---  
`VOLUME_TYPE_UNSPECIFIED` | Default  
`GCE_PERSISTENT_DISK` | Compute Engine Persistent Disk volume  
  
## RestoreOrder

Allows customers to specify dependencies between resources that Backup for GKE can use to compute a resasonable restore order.

JSON representation  
---  
      
    
    {
      "groupKindDependencies": [
        {
          object ([GroupKindDependency](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#GroupKindDependency))
        }
      ]
    }  
  
Fields  
---  
`groupKindDependencies[]` |  `object (`[GroupKindDependency](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/RestoreConfig#GroupKindDependency)`)` Optional. Contains a list of group kind dependency pairs provided by the customer, that is used by Backup for GKE to generate a group kind restore order.  
  
## GroupKindDependency

Defines a dependency between two group kinds.

JSON representation  
---  
      
    
    {
      "satisfying": {
        object ([GroupKind](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/GroupKind))
      },
      "requiring": {
        object ([GroupKind](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/GroupKind))
      }
    }  
  
Fields  
---  
`satisfying` |  `object (`[GroupKind](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/GroupKind)`)` Required. The satisfying group kind must be restored first in order to satisfy the dependency.  
`requiring` |  `object (`[GroupKind](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/GroupKind)`)` Required. The requiring group kind requires that the other group kind be restored first.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
