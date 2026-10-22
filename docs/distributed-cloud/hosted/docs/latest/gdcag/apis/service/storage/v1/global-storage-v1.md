---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/storage/v1/global-storage-v1/
title: KRM API storage.global.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:59.931472+00:00
---

# KRM API storage.global.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/storage/v1/global-storage-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API storage.global.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## storage.global.gdc.goog/v1

Contains API Schema definitions for the storage.global.gdc.goog v1 API group.

### FileShareSource

_Appears in:_ \- VolumeReplicationSource

Field | Description  
---|---  
`fileShareRef` _string_ | A name reference to the `FileShare` resource to be replicated.  
  
### LocalVolume

Represents a volume within the local storage system.

_Appears in:_ \- VolumeReplicationRelationshipReplicaStatus

Field | Description  
---|---  
`storageClassName` _string_ | The name of the storage class defined by the `PersistentVolumeClaim`.  
`storageClusterName` _string_ | The storage cluster on which the Volume was allocated, as used inside of the peering between zones.  
`internalVolumeName` _string_ | The name of the internal volume on the storage appliance.  
`requestedStorageSize` _string_ | The storage size of the volume requested by the `PersistentVolumeClaim`.  
`volumeMode` _[PersistentVolumeMode](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#persistentvolumemode-v1-core)_ | The mode of the internal volume on the storage appliance.  
`isDeleted` _boolean_ | Specifies whether PVC has been deleted  
  
### PVCVolumeDestination

_Appears in:_ \- VolumeReplicationDestination

Field | Description  
---|---  
`clusterRef` _string_ | A reference to the `Cluster` custom resource where the destination PVC is created.  
  
### PVCVolumeSource

_Appears in:_ \- VolumeReplicationSource

Field | Description  
---|---  
`clusterRef` _string_ | A reference to the `Cluster` custom resource where the PVC to be replicated exists.  
`pvcRef` _string_ | A name reference to the `PersistentVolumeClaim` resource to be replicated.  
  
### VirtualMachineDiskVolumeSource

_Appears in:_ \- VolumeReplicationSource

Field | Description  
---|---  
`virtualMachineDiskRef` _string_ | A name reference to the `VirtualMachineDisk` resource to be replicated.  
  
### VolumeReplicationDestination

Defines the target location for a volume replication operation.

_Appears in:_ \- VolumeReplicationRelationshipSpec

Field | Description  
---|---  
`zoneRef` _string_ | A reference to the `Zone` custom resource.  
`pvc` _PVCVolumeDestination_ | A reference to a `PersistentVolumeClaim` resource.  
`volumeOverrideName` _string_ | The desired name for the destination volume. The default is to use the same name as the source volume.  
  
### VolumeReplicationRelationship

Defines the Schema for the 'VolumeReplicationRelationship' API.

_Appears in:_ \- VolumeReplicationRelationshipList

Field | Description  
---|---  
`apiVersion` _string_ | `storage.global.gdc.goog/v1`  
`kind` _string_ | `VolumeReplicationRelationship`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VolumeReplicationRelationshipSpec_ |   
`status` _VolumeReplicationRelationshipStatus_ |   
  
### VolumeReplicationRelationshipList

Represents a list of 'VolumeReplicationRelationship'

Field | Description  
---|---  
`apiVersion` _string_ | `storage.global.gdc.goog/v1`  
`kind` _string_ | `VolumeReplicationRelationshipList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VolumeReplicationRelationship array_ |   
  
### VolumeReplicationRelationshipReplica

Defines the Schema for the `VolumeReplicationRelationshipReplica` API.

_Appears in:_ \- VolumeReplicationRelationshipReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `storage.global.gdc.goog/v1`  
`kind` _string_ | `VolumeReplicationRelationshipReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VolumeReplicationRelationshipSpec_ |   
`status` _VolumeReplicationRelationshipReplicaStatus_ |   
  
### VolumeReplicationRelationshipReplicaList

Contains a list of `VolumeReplicationRelationshipReplica` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `storage.global.gdc.goog/v1`  
`kind` _string_ | `VolumeReplicationRelationshipReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VolumeReplicationRelationshipReplica array_ |   
  
### VolumeReplicationRelationshipReplicaStatus

Defines the observed state of the `VolumeReplicationRelationshipReplica`.

_Appears in:_ \- VolumeReplicationRelationshipReplica \- VolumeReplicationRelationshipZoneStatus

Field | Description  
---|---  
`state` _VolumeReplicationState_ | The current status of the volume replication relationship.  
`message` _string_ | A human-readable message indicating details about why the volume replication relationship is in this state.  
`replicationID` _UUID_ | The unique UUID identifying a SnapMirror relationship  
`sourceVolume` _LocalVolume_ | The cached information about the source volume. This information is only populated by the source zone.  
`destinationVolume` _LocalVolume_ | The cached information about the destination volume. This information is only populated by the destination zone.  
`lagTime` _string_ | The timestamp of when the last snapshot was exported  
`exportedSnapshotName` _string_ | The name of the last exported snapshot  
`lastTransferType` _string_ | The type of the last transfer operation, such as a snapshot.  
`lastTransferTime` _string_ | The timestamp of when the last transfer operation occurred  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The information on the overall state of the `VolumeReplicationRelationshipReplica`.  
  
### VolumeReplicationRelationshipSpec

Defines the desired state of VolumeReplicationRelationship.

_Appears in:_ \- VolumeReplicationRelationship \- VolumeReplicationRelationshipReplica

Field | Description  
---|---  
`source` _VolumeReplicationSource_ |   
`destination` _VolumeReplicationDestination_ |   
  
### VolumeReplicationRelationshipStatus

Defines the observed state of the 'VolumeReplicationRelationship'.

_Appears in:_ \- VolumeReplicationRelationship

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _VolumeReplicationRelationshipZoneStatus array_ | The list of zone status' where this resource is rolled out to.  
  
### VolumeReplicationRelationshipZoneStatus

Defines the observed state of the `VolumeReplicationRelationshipReplica` of a particular zone.

_Appears in:_ \- VolumeReplicationRelationshipStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _VolumeReplicationRelationshipReplicaStatus_ | The reconciliation status of the replica collected from the zone.  
  
### VolumeReplicationSource

Defines the origin of a volume replication operation.

_Appears in:_ \- VolumeReplicationRelationshipSpec

Field | Description  
---|---  
`zoneRef` _string_ | A reference to the 'Zone' custom resource.  
`pvc` _PVCVolumeSource_ | A reference to a `PersistentVolumeClaim` resource.  
`virtualMachineDisk` _VirtualMachineDiskVolumeSource_ | A reference to a `VirtualMachineDisk` resource.  
`fileShare` _FileShareSource_ | A reference to a `FileShare` resource.  
  
### VolumeReplicationState

_Underlying type:_ `string` Defines the state of the volume replication used in the `VolumeReplicationRelationshipStatus`.

_Appears in:_ \- VolumeReplicationRelationshipReplicaStatus

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
