---
url: https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications
title: REST Resource: projects.locations.volumes.replications \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:55:16.859910+00:00
---

# REST Resource: projects.locations.volumes.replications  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Reference ](https://docs.cloud.google.com/netapp/volumes/docs/apis)



Send feedback 

#  REST Resource: projects.locations.volumes.replications Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Replication
    * JSON representation
  * State
  * ReplicationRole
  * ReplicationSchedule
  * MirrorState
  * TransferStats
    * JSON representation
  * DestinationVolumeParameters
    * JSON representation
  * HybridPeeringDetails
    * JSON representation
  * HybridReplicationType
  * UserCommands
    * JSON representation
  * Methods



## Resource: Replication

Replication is a nested resource under Volume, that describes a cross-region replication relationship between 2 volumes in different regions.

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum ([State](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#State)),
      "stateDetails": string,
      "role": enum ([ReplicationRole](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#ReplicationRole)),
      "replicationSchedule": enum ([ReplicationSchedule](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#ReplicationSchedule)),
      "mirrorState": enum ([MirrorState](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#MirrorState)),
      "createTime": string,
      "destinationVolume": string,
      "transferStats": {
        object ([TransferStats](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#TransferStats))
      },
      "labels": {
        string: string,
        ...
      },
      "destinationVolumeParameters": {
        object ([DestinationVolumeParameters](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#DestinationVolumeParameters))
      },
      "sourceVolume": string,
      "hybridPeeringDetails": {
        object ([HybridPeeringDetails](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#HybridPeeringDetails))
      },
      "clusterLocation": string,
      "hybridReplicationType": enum ([HybridReplicationType](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#HybridReplicationType)),
      "hybridReplicationUserCommands": {
        object ([UserCommands](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#UserCommands))
      },
      "healthy": boolean,
      "description": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the Replication. Format: `projects/{projectId}/locations/{location}/volumes/{volumeId}/replications/{replicationId}`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#State)`)` Output only. State of the replication.  
`stateDetails` |  `string` Output only. State details of the replication.  
`role` |  `enum (`[ReplicationRole](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#ReplicationRole)`)` Output only. Indicates whether this points to source or destination.  
`replicationSchedule` |  `enum (`[ReplicationSchedule](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#ReplicationSchedule)`)` Required. Indicates the schedule for replication.  
`mirrorState` |  `enum (`[MirrorState](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#MirrorState)`)` Output only. Indicates the state of mirroring.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Replication create time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`destinationVolume` |  `string` Output only. Full name of destination volume resource. Example : "projects/{project}/locations/{location}/volumes/{volumeId}"  
`transferStats` |  `object (`[TransferStats](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#TransferStats)`)` Output only. Replication transfer statistics.  
`labels` |  `map (key: string, value: string)` Resource labels to represent user provided metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`destinationVolumeParameters` |  `object (`[DestinationVolumeParameters](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#DestinationVolumeParameters)`)` Required. Input only. Destination volume parameters  
`sourceVolume` |  `string` Output only. Full name of source volume resource. Example : "projects/{project}/locations/{location}/volumes/{volumeId}"  
`hybridPeeringDetails` |  `object (`[HybridPeeringDetails](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#HybridPeeringDetails)`)` Output only. Hybrid peering details.  
`clusterLocation` |  `string` Optional. Location of the user cluster.  
`hybridReplicationType` |  `enum (`[HybridReplicationType](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#HybridReplicationType)`)` Output only. Type of the hybrid replication.  
`hybridReplicationUserCommands` |  `object (`[UserCommands](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications#UserCommands)`)` Output only. Copy pastable snapmirror commands to be executed on onprem cluster by the customer.  
`healthy` |  `boolean` Output only. Condition of the relationship. Can be one of the following: - true: The replication relationship is healthy. It has not missed the most recent scheduled transfer. - false: The replication relationship is not healthy. It has missed the most recent scheduled transfer.  
`description` |  `string` A description about this replication relationship.  
  
## State

The replication states New enum values may be added in future to indicate possible new states.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified replication State  
`CREATING` | Replication is creating.  
`READY` | Replication is ready.  
`UPDATING` | Replication is updating.  
`DELETING` | Replication is deleting.  
`ERROR` | Replication is in error state.  
`PENDING_CLUSTER_PEERING` | Replication is waiting for cluster peering to be established.  
`PENDING_SVM_PEERING` | Replication is waiting for SVM peering to be established.  
`PENDING_REMOTE_RESYNC` | Replication is waiting for Commands to be executed on Onprem ONTAP.  
`EXTERNALLY_MANAGED_REPLICATION` | Onprem ONTAP is destination and Replication can only be managed from Onprem.  
  
## ReplicationRole

New enum values may be added in future to support different replication topology.

Enums  
---  
`REPLICATION_ROLE_UNSPECIFIED` | Unspecified replication role  
`SOURCE` | Indicates Source volume.  
`DESTINATION` | Indicates Destination volume.  
  
## ReplicationSchedule

Schedule for Replication. New enum values may be added in future to support different frequency of replication.

Enums  
---  
`REPLICATION_SCHEDULE_UNSPECIFIED` | Unspecified ReplicationSchedule  
`EVERY_10_MINUTES` | Replication happens once every 10 minutes.  
`HOURLY` | Replication happens once every hour.  
`DAILY` | Replication happens once every day.  
  
## MirrorState

Mirroring states. No new value is expected to be added in future.

Enums  
---  
`MIRROR_STATE_UNSPECIFIED` | Unspecified MirrorState  
`PREPARING` | Destination volume is being prepared.  
`MIRRORED` | Destination volume has been initialized and is ready to receive replication transfers.  
`STOPPED` | Destination volume is not receiving replication transfers.  
`TRANSFERRING` | Incremental replication is in progress.  
`BASELINE_TRANSFERRING` | Baseline replication is in progress.  
`ABORTED` | Replication is aborted.  
`EXTERNALLY_MANAGED` | Replication is being managed from Onprem ONTAP.  
`PENDING_PEERING` | Peering is yet to be established.  
  
## TransferStats

TransferStats reports all statistics related to replication transfer.

JSON representation  
---  
      
    
    {
      "transferBytes": string,
      "totalTransferDuration": string,
      "lastTransferBytes": string,
      "lastTransferDuration": string,
      "lagDuration": string,
      "updateTime": string,
      "lastTransferEndTime": string,
      "lastTransferError": string
    }  
  
Fields  
---  
`transferBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Cumulative bytes transferred so far for the replication relationship.  
`totalTransferDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Cumulative time taken across all transfers for the replication relationship.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`lastTransferBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Last transfer size in bytes.  
`lastTransferDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Time taken during last transfer.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`lagDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Lag duration indicates the duration by which Destination region volume content lags behind the primary region volume content.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time when progress was updated last.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastTransferEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time when last transfer completed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastTransferError` |  `string` A message describing the cause of the last transfer failure.  
  
## DestinationVolumeParameters

DestinationVolumeParameters specify input parameters used for creating destination volume.

JSON representation  
---  
      
    
    {
      "storagePool": string,
      "volumeId": string,
      "shareName": string,
      "description": string,
      "tieringPolicy": {
        object ([TieringPolicy](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/TieringPolicy))
      }
    }  
  
Fields  
---  
`storagePool` |  `string` Required. Existing destination StoragePool name.  
`volumeId` |  `string` Desired destination volume resource id. If not specified, source volume's resource id will be used. This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens, and cannot end with a hyphen.  
`shareName` |  `string` Destination volume's share name. If not specified, source volume's share name will be used.  
`description` |  `string` Description for the destination volume.  
`tieringPolicy` |  `object (`[TieringPolicy](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/TieringPolicy)`)` Optional. Tiering policy for the volume.  
  
## HybridPeeringDetails

HybridPeeringDetails contains details about the hybrid peering.

JSON representation  
---  
      
    
    {
      "subnetIp": string,
      "command": string,
      "commandExpiryTime": string,
      "passphrase": string,
      "peerVolumeName": string,
      "peerClusterName": string,
      "peerSvmName": string
    }  
  
Fields  
---  
`subnetIp` |  `string` Output only. IP address of the subnet.  
`command` |  `string` Output only. Copy-paste-able commands to be used on user's ONTAP to accept peering requests.  
`commandExpiryTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Expiration time for the peering command to be executed on user's ONTAP.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`passphrase` |  `string` Output only. Temporary passphrase generated to accept cluster peering command.  
`peerVolumeName` |  `string` Output only. Name of the user's local source volume to be peered with the destination volume.  
`peerClusterName` |  `string` Output only. Name of the user's local source cluster to be peered with the destination cluster.  
`peerSvmName` |  `string` Output only. Name of the user's local source vserver svm to be peered with the destination vserver svm.  
  
## HybridReplicationType

Hybrid replication type.

Enums  
---  
`HYBRID_REPLICATION_TYPE_UNSPECIFIED` | Unspecified hybrid replication type.  
`MIGRATION` | Hybrid replication type for migration.  
`CONTINUOUS_REPLICATION` | Hybrid replication type for continuous replication.  
`ONPREM_REPLICATION` | New field for reversible OnPrem replication, to be used for data protection.  
`REVERSE_ONPREM_REPLICATION` | Hybrid replication type for incremental Transfer in the reverse direction (GCNV is source and Onprem is destination)  
  
## UserCommands

UserCommands contains the commands to be executed by the customer.

JSON representation  
---  
      
    
    {
      "commands": [
        string
      ]
    }  
  
Fields  
---  
`commands[]` |  `string` Output only. List of commands to be executed by the customer.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications/create)`

|  Create a new replication for a volume.  
  
### `[delete](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications/delete)`

|  Deletes a replication.  
  
### `[establishPeering](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications/establishPeering)`

|  Establish replication peering.  
  
### `[get](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications/get)`

|  Describe a replication for a volume.  
  
### `[list](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications/list)`

|  Returns descriptions of all replications for a volume.  
  
### `[patch](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications/patch)`

|  Updates the settings of a specific replication.  
  
### `[resume](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications/resume)`

|  Resume Cross Region Replication.  
  
### `[reverseDirection](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications/reverseDirection)`

|  Reverses direction of replication.  
  
### `[stop](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications/stop)`

|  Stop Cross Region Replication.  
  
### `[sync](https://docs.cloud.google.com/netapp/volumes/docs/reference/rest/v1/projects.locations.volumes.replications/sync)`

|  Syncs the replication.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-04 UTC."],[],[]] 
