---
url: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types
title: Package types (0.10.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:10.281923+00:00
---

# Package types (0.10.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (0.10.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.2 (latest)  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.24  0.2.0  0.1.0 

API documentation for `netapp_v1.types` package.

## Classes 

### [AccessType](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.AccessType)

AccessType is an enum of all the supported access types for a volume.

### [ActiveDirectory](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ActiveDirectory)

ActiveDirectory is the public representation of the active directory config.

### [Backup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Backup)

A NetApp Backup.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupConfig](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupConfig)

BackupConfig contains backup related config on a volume.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupPolicy](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupPolicy)

Backup Policy.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupVault](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupVault)

A NetApp BackupVault.

### [BlockDevice](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BlockDevice)

Block device represents the device(s) which are stored in the block volume.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CacheConfig](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CacheConfig)

Configuration of the cache volume.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CacheParameters](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CacheParameters)

Cache Parameters for the volume.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CachePrePopulate](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CachePrePopulate)

Pre-populate cache volume with data from the origin volume.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CreateActiveDirectoryRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateActiveDirectoryRequest)

CreateActiveDirectoryRequest for creating an active directory.

### [CreateBackupPolicyRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateBackupPolicyRequest)

CreateBackupPolicyRequest creates a backupPolicy.

### [CreateBackupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateBackupRequest)

CreateBackupRequest creates a backup.

### [CreateBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateBackupVaultRequest)

CreateBackupVaultRequest creates a backup vault.

### [CreateHostGroupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateHostGroupRequest)

CreateHostGroupRequest for creating a host group.

### [CreateKmsConfigRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateKmsConfigRequest)

CreateKmsConfigRequest creates a KMS Config.

### [CreateQuotaRuleRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateQuotaRuleRequest)

CreateQuotaRuleRequest for creating a quota rule.

### [CreateReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateReplicationRequest)

CreateReplicationRequest creates a replication.

### [CreateSnapshotRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateSnapshotRequest)

CreateSnapshotRequest creates a snapshot.

### [CreateStoragePoolRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateStoragePoolRequest)

CreateStoragePoolRequest creates a Storage Pool.

### [CreateVolumeRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.CreateVolumeRequest)

Message for creating a Volume

### [DailySchedule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DailySchedule)

Make a snapshot every day e.g. at 04:00, 05:20, 23:50

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DeleteActiveDirectoryRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteActiveDirectoryRequest)

DeleteActiveDirectoryRequest for deleting a single active directory.

### [DeleteBackupPolicyRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteBackupPolicyRequest)

DeleteBackupPolicyRequest deletes a backup policy.

### [DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteBackupRequest)

DeleteBackupRequest deletes a backup.

### [DeleteBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteBackupVaultRequest)

DeleteBackupVaultRequest deletes a backupVault.

### [DeleteHostGroupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteHostGroupRequest)

DeleteHostGroupRequest for deleting a single host group.

### [DeleteKmsConfigRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteKmsConfigRequest)

DeleteKmsConfigRequest deletes a KMS Config.

### [DeleteQuotaRuleRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteQuotaRuleRequest)

DeleteQuotaRuleRequest for deleting a single quota rule.

### [DeleteReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteReplicationRequest)

DeleteReplicationRequest deletes a replication.

### [DeleteSnapshotRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteSnapshotRequest)

DeleteSnapshotRequest deletes a snapshot.

### [DeleteStoragePoolRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteStoragePoolRequest)

DeleteStoragePoolRequest deletes a Storage Pool.

### [DeleteVolumeRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DeleteVolumeRequest)

Message for deleting a Volume

### [DestinationVolumeParameters](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DestinationVolumeParameters)

DestinationVolumeParameters specify input parameters used for creating destination volume.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DirectoryServiceType](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.DirectoryServiceType)

Type of directory service

### [EncryptVolumesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.EncryptVolumesRequest)

EncryptVolumesRequest specifies the KMS config to encrypt existing volumes.

### [EncryptionType](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.EncryptionType)

The volume encryption key source.

### [EstablishPeeringRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.EstablishPeeringRequest)

EstablishPeeringRequest establishes cluster and svm peerings between the source and the destination replications.

### [EstablishVolumePeeringRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.EstablishVolumePeeringRequest)

EstablishVolumePeeringRequest establishes cluster and svm peerings between the source and destination clusters.

### [ExecuteOntapDeleteRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapDeleteRequest)

Request message for `ExecuteOntapDelete` API.

### [ExecuteOntapDeleteResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapDeleteResponse)

Response message for `ExecuteOntapDelete` API.

### [ExecuteOntapGetRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapGetRequest)

Request message for `ExecuteOntapGet` API.

### [ExecuteOntapGetResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapGetResponse)

Response message for `ExecuteOntapGet` API.

### [ExecuteOntapPatchRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapPatchRequest)

Request message for `ExecuteOntapPatch` API.

### [ExecuteOntapPatchResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapPatchResponse)

Response message for `ExecuteOntapPatch` API.

### [ExecuteOntapPostRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapPostRequest)

Request message for `ExecuteOntapPost` API.

### [ExecuteOntapPostResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExecuteOntapPostResponse)

Response message for `ExecuteOntapPost` API.

### [ExportPolicy](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ExportPolicy)

Defines the export policy for the volume.

### [FlexPerformance](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.FlexPerformance)

Flex Storage Pool performance.

### [GetActiveDirectoryRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetActiveDirectoryRequest)

GetActiveDirectory for getting a single active directory.

### [GetBackupPolicyRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetBackupPolicyRequest)

GetBackupPolicyRequest gets the state of a backupPolicy.

### [GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetBackupRequest)

GetBackupRequest gets the state of a backup.

### [GetBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetBackupVaultRequest)

GetBackupVaultRequest gets the state of a backupVault.

### [GetHostGroupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetHostGroupRequest)

GetHostGroupRequest for getting a host group.

### [GetKmsConfigRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetKmsConfigRequest)

GetKmsConfigRequest gets a KMS Config.

### [GetQuotaRuleRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetQuotaRuleRequest)

GetQuotaRuleRequest for getting a quota rule.

### [GetReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetReplicationRequest)

GetReplicationRequest gets the state of a replication.

### [GetSnapshotRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetSnapshotRequest)

GetSnapshotRequest gets the state of a snapshot.

### [GetStoragePoolRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetStoragePoolRequest)

GetStoragePoolRequest gets a Storage Pool.

### [GetVolumeRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.GetVolumeRequest)

Message for getting a Volume

### [HostGroup](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.HostGroup)

Host group is a collection of hosts that can be used for accessing a Block Volume.

### [HourlySchedule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.HourlySchedule)

Make a snapshot every hour e.g. at 04:00, 05:00, 06:00.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [HybridPeeringDetails](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.HybridPeeringDetails)

HybridPeeringDetails contains details about the hybrid peering.

### [HybridReplicationParameters](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.HybridReplicationParameters)

The Hybrid Replication parameters for the volume.

### [HybridReplicationSchedule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.HybridReplicationSchedule)

Schedule for Hybrid Replication. New enum values may be added in future to support different frequency of replication.

### [KmsConfig](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.KmsConfig)

KmsConfig is the customer-managed encryption key(CMEK) configuration.

### [LargeCapacityConfig](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.LargeCapacityConfig)

Configuration for a Large Capacity Volume. A Large Capacity Volume supports sizes ranging from 4.8 TiB to 20 PiB, it is composed of multiple internal constituents, and must be created in a large capacity pool.

### [ListActiveDirectoriesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListActiveDirectoriesRequest)

ListActiveDirectoriesRequest for requesting multiple active directories.

### [ListActiveDirectoriesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListActiveDirectoriesResponse)

ListActiveDirectoriesResponse contains all the active directories requested.

### [ListBackupPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupPoliciesRequest)

ListBackupPoliciesRequest for requesting multiple backup policies.

### [ListBackupPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupPoliciesResponse)

ListBackupPoliciesResponse contains all the backup policies requested.

### [ListBackupVaultsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupVaultsRequest)

ListBackupVaultsRequest lists backupVaults.

### [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupVaultsResponse)

ListBackupVaultsResponse is the result of ListBackupVaultsRequest.

### [ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupsRequest)

ListBackupsRequest lists backups.

### [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupsResponse)

ListBackupsResponse is the result of ListBackupsRequest.

### [ListHostGroupsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListHostGroupsRequest)

ListHostGroupsRequest for listing host groups.

### [ListHostGroupsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListHostGroupsResponse)

ListHostGroupsResponse is the response to a ListHostGroupsRequest.

### [ListKmsConfigsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListKmsConfigsRequest)

ListKmsConfigsRequest lists KMS Configs.

### [ListKmsConfigsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListKmsConfigsResponse)

ListKmsConfigsResponse is the response to a ListKmsConfigsRequest.

### [ListQuotaRulesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListQuotaRulesRequest)

ListQuotaRulesRequest for listing quota rules.

### [ListQuotaRulesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListQuotaRulesResponse)

ListQuotaRulesResponse is the response to a ListQuotaRulesRequest.

### [ListReplicationsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListReplicationsRequest)

ListReplications lists replications.

### [ListReplicationsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListReplicationsResponse)

ListReplicationsResponse is the result of ListReplicationsRequest.

### [ListSnapshotsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListSnapshotsRequest)

ListSnapshotsRequest lists snapshots.

### [ListSnapshotsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListSnapshotsResponse)

ListSnapshotsResponse is the result of ListSnapshotsRequest.

### [ListStoragePoolsRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListStoragePoolsRequest)

ListStoragePoolsRequest lists Storage Pools.

### [ListStoragePoolsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListStoragePoolsResponse)

ListStoragePoolsResponse is the response to a ListStoragePoolsRequest.

### [ListVolumesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListVolumesRequest)

Message for requesting list of Volumes

### [ListVolumesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListVolumesResponse)

Message for response to listing Volumes

### [LocationMetadata](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.LocationMetadata)

Metadata for a given google.cloud.location.Location.

### [Mode](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Mode)

`Mode` of the storage pool or volume. This field is used to control whether the resource is managed by the GCNV APIs or the GCNV ONTAP Mode APIs.

### [MonthlySchedule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.MonthlySchedule)

Make a snapshot once a month e.g. at 2nd 04:00, 7th 05:20, 24th 23:50

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [MountOption](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.MountOption)

View only mount options for a volume.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [OsType](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.OsType)

OS types for the host group

### [Protocols](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Protocols)

Protocols is an enum of all the supported network protocols for a volume.

### [QosType](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.QosType)

QoS (Quality of Service) Types of the storage pool

### [QuotaRule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.QuotaRule)

QuotaRule specifies the maximum disk space a user or group can use within a volume. They can be used for creating default and individual quota rules.

### [Replication](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Replication)

Replication is a nested resource under Volume, that describes a cross-region replication relationship between 2 volumes in different regions.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RestoreBackupFilesRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.RestoreBackupFilesRequest)

RestoreBackupFilesRequest restores files from a backup to a volume.

### [RestoreBackupFilesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.RestoreBackupFilesResponse)

RestoreBackupFilesResponse is the result of RestoreBackupFilesRequest.

### [RestoreParameters](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.RestoreParameters)

The RestoreParameters if volume is created from a snapshot or backup.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RestrictedAction](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.RestrictedAction)

Actions to be restricted for a volume.

### [ResumeReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ResumeReplicationRequest)

ResumeReplicationRequest resumes a stopped replication.

### [ReverseReplicationDirectionRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ReverseReplicationDirectionRequest)

ReverseReplicationDirectionRequest reverses direction of replication. Source becomes destination and destination becomes source.

### [RevertVolumeRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.RevertVolumeRequest)

RevertVolumeRequest reverts the given volume to the specified snapshot.

### [SMBSettings](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.SMBSettings)

Modifies the behaviour of a SMB volume.

### [ScaleType](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ScaleType)

Defines the scale-type of a UNIFIED Storage Pool.

### [SecurityStyle](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.SecurityStyle)

The security style of the volume, can be either UNIX or NTFS.

### [ServiceLevel](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ServiceLevel)

The service level of a storage pool and its volumes.

### [SimpleExportPolicyRule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.SimpleExportPolicyRule)

An export policy rule describing various export options.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Snapshot](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Snapshot)

Snapshot is a point-in-time version of a Volume's content.

### [SnapshotPolicy](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.SnapshotPolicy)

Snapshot Policy for a volume.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [StopReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.StopReplicationRequest)

StopReplicationRequest stops a replication until resumed.

### [StoragePool](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.StoragePool)

StoragePool is a container for volumes with a service level and capacity. Volumes can be created in a pool of sufficient available capacity. StoragePool capacity is what you are billed for.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [StoragePoolType](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.StoragePoolType)

Type of storage pool

### [SwitchActiveReplicaZoneRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.SwitchActiveReplicaZoneRequest)

SwitchActiveReplicaZoneRequest switch the active/replica zone for a regional storagePool.

### [SyncReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.SyncReplicationRequest)

SyncReplicationRequest syncs the replication from source to destination.

### [TieringPolicy](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.TieringPolicy)

Defines tiering policy for the volume.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TransferStats](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.TransferStats)

TransferStats reports all statistics related to replication transfer.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UpdateActiveDirectoryRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateActiveDirectoryRequest)

UpdateActiveDirectoryRequest for updating an active directory.

### [UpdateBackupPolicyRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateBackupPolicyRequest)

UpdateBackupPolicyRequest for updating a backup policy.

### [UpdateBackupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateBackupRequest)

UpdateBackupRequest updates description and/or labels for a backup.

### [UpdateBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateBackupVaultRequest)

UpdateBackupVaultRequest updates description and/or labels for a backupVault.

### [UpdateHostGroupRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateHostGroupRequest)

UpdateHostGroupRequest for updating a host group.

### [UpdateKmsConfigRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateKmsConfigRequest)

UpdateKmsConfigRequest updates a KMS Config.

### [UpdateQuotaRuleRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateQuotaRuleRequest)

UpdateQuotaRuleRequest for updating a quota rule.

### [UpdateReplicationRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateReplicationRequest)

UpdateReplicationRequest updates description and/or labels for a replication.

### [UpdateSnapshotRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateSnapshotRequest)

UpdateSnapshotRequest updates description and/or labels for a snapshot.

### [UpdateStoragePoolRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateStoragePoolRequest)

UpdateStoragePoolRequest updates a Storage Pool.

### [UpdateVolumeRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UpdateVolumeRequest)

Message for updating a Volume

### [UserCommands](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.UserCommands)

UserCommands contains the commands to be executed by the customer.

### [ValidateDirectoryServiceRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ValidateDirectoryServiceRequest)

ValidateDirectoryServiceRequest validates the directory service policy attached to the storage pool.

### [VerifyKmsConfigRequest](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.VerifyKmsConfigRequest)

VerifyKmsConfigRequest specifies the KMS config to be validated.

### [VerifyKmsConfigResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.VerifyKmsConfigResponse)

VerifyKmsConfigResponse contains the information if the config is correctly and error message.

### [Volume](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Volume)

Volume provides a filesystem that you can mount.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [WeeklySchedule](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.WeeklySchedule)

Make a snapshot every week e.g. at Monday 04:00, Wednesday 05:20, Sunday 23:50

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
