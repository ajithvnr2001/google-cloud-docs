---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.NetAppGrpc.NetAppBlockingStub
title: Class NetAppGrpc.NetAppBlockingStub (0.78.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:26.515526+00:00
---

# Class NetAppGrpc.NetAppBlockingStub (0.78.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.NetAppGrpc.NetAppBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NetAppGrpc.NetAppBlockingStub (0.78.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.78.0 (latest)  0.74.0  0.73.0  0.72.0  0.70.0  0.67.0  0.66.0  0.64.0  0.62.0  0.61.0  0.59.0  0.57.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.43.0  0.42.0  0.41.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class NetAppGrpc.NetAppBlockingStub extends AbstractBlockingStub<NetAppGrpc.NetAppBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service NetApp.

NetApp Files Google Cloud Service

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > NetAppGrpc.NetAppBlockingStub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected NetAppGrpc.NetAppBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetAppGrpc.NetAppBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.NetAppGrpc.NetAppBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createActiveDirectory(CreateActiveDirectoryRequest request)
    
    
    public Operation createActiveDirectory(CreateActiveDirectoryRequest request)

CreateActiveDirectory Creates the active directory specified in the request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateActiveDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateActiveDirectoryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createBackup(CreateBackupRequest request)
    
    
    public Operation createBackup(CreateBackupRequest request)

Creates a backup from the volume specified in the request The backup can be created from the given snapshot if specified in the request. If no snapshot specified, there'll be a new snapshot taken to initiate the backup creation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createBackupPolicy(CreateBackupPolicyRequest request)
    
    
    public Operation createBackupPolicy(CreateBackupPolicyRequest request)

Creates new backup policy

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBackupPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateBackupPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createBackupVault(CreateBackupVaultRequest request)
    
    
    public Operation createBackupVault(CreateBackupVaultRequest request)

Creates new backup vault

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateBackupVaultRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createHostGroup(CreateHostGroupRequest request)
    
    
    public Operation createHostGroup(CreateHostGroupRequest request)

Creates a new host group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateHostGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateHostGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createKmsConfig(CreateKmsConfigRequest request)
    
    
    public Operation createKmsConfig(CreateKmsConfigRequest request)

Creates a new KMS config.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateKmsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateKmsConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createQuotaRule(CreateQuotaRuleRequest request)
    
    
    public Operation createQuotaRule(CreateQuotaRuleRequest request)

Creates a new quota rule.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateQuotaRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateQuotaRuleRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createReplication(CreateReplicationRequest request)
    
    
    public Operation createReplication(CreateReplicationRequest request)

Create a new replication for a volume.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateReplicationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createSnapshot(CreateSnapshotRequest request)
    
    
    public Operation createSnapshot(CreateSnapshotRequest request)

Create a new snapshot for a volume.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateSnapshotRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createStoragePool(CreateStoragePoolRequest request)
    
    
    public Operation createStoragePool(CreateStoragePoolRequest request)

Creates a new storage pool.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateStoragePoolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createVolume(CreateVolumeRequest request)
    
    
    public Operation createVolume(CreateVolumeRequest request)

Creates a new Volume in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateVolumeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateVolumeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteActiveDirectory(DeleteActiveDirectoryRequest request)
    
    
    public Operation deleteActiveDirectory(DeleteActiveDirectoryRequest request)

Delete the active directory specified in the request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteActiveDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteActiveDirectoryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteBackup(DeleteBackupRequest request)
    
    
    public Operation deleteBackup(DeleteBackupRequest request)

Warning! This operation will permanently delete the backup.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteBackupPolicy(DeleteBackupPolicyRequest request)
    
    
    public Operation deleteBackupPolicy(DeleteBackupPolicyRequest request)

Warning! This operation will permanently delete the backup policy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteBackupPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteBackupVault(DeleteBackupVaultRequest request)
    
    
    public Operation deleteBackupVault(DeleteBackupVaultRequest request)

Warning! This operation will permanently delete the backup vault.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteBackupVaultRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteHostGroup(DeleteHostGroupRequest request)
    
    
    public Operation deleteHostGroup(DeleteHostGroupRequest request)

Deletes a host group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteHostGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteHostGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteKmsConfig(DeleteKmsConfigRequest request)
    
    
    public Operation deleteKmsConfig(DeleteKmsConfigRequest request)

Warning! This operation will permanently delete the Kms config.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteKmsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteKmsConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteQuotaRule(DeleteQuotaRuleRequest request)
    
    
    public Operation deleteQuotaRule(DeleteQuotaRuleRequest request)

Deletes a quota rule.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteQuotaRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteQuotaRuleRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteReplication(DeleteReplicationRequest request)
    
    
    public Operation deleteReplication(DeleteReplicationRequest request)

Deletes a replication.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteReplicationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteSnapshot(DeleteSnapshotRequest request)
    
    
    public Operation deleteSnapshot(DeleteSnapshotRequest request)

Deletes a snapshot.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteSnapshotRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteStoragePool(DeleteStoragePoolRequest request)
    
    
    public Operation deleteStoragePool(DeleteStoragePoolRequest request)

Warning! This operation will permanently delete the storage pool.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteStoragePoolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteVolume(DeleteVolumeRequest request)
    
    
    public Operation deleteVolume(DeleteVolumeRequest request)

Deletes a single Volume.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteVolumeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteVolumeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### encryptVolumes(EncryptVolumesRequest request)
    
    
    public Operation encryptVolumes(EncryptVolumesRequest request)

Encrypt the existing volumes without CMEK encryption with the desired the KMS config for the whole region.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EncryptVolumesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.EncryptVolumesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### establishPeering(EstablishPeeringRequest request)
    
    
    public Operation establishPeering(EstablishPeeringRequest request)

Establish replication peering.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EstablishPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.EstablishPeeringRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### establishVolumePeering(EstablishVolumePeeringRequest request)
    
    
    public Operation establishVolumePeering(EstablishVolumePeeringRequest request)

Establish volume peering. This is used to establish cluster and svm peerings between the GCNV and OnPrem clusters.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EstablishVolumePeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.EstablishVolumePeeringRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### executeOntapDelete(ExecuteOntapDeleteRequest request)
    
    
    public ExecuteOntapDeleteResponse executeOntapDelete(ExecuteOntapDeleteRequest request)

`ExecuteOntapDelete` dispatches the ONTAP `DELETE` request to the `StoragePool` cluster.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExecuteOntapDeleteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ExecuteOntapDeleteRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteOntapDeleteResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ExecuteOntapDeleteResponse)` |   
  
### executeOntapGet(ExecuteOntapGetRequest request)
    
    
    public ExecuteOntapGetResponse executeOntapGet(ExecuteOntapGetRequest request)

`ExecuteOntapGet` dispatches the ONTAP `GET` request to the `StoragePool` cluster.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExecuteOntapGetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ExecuteOntapGetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteOntapGetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ExecuteOntapGetResponse)` |   
  
### executeOntapPatch(ExecuteOntapPatchRequest request)
    
    
    public ExecuteOntapPatchResponse executeOntapPatch(ExecuteOntapPatchRequest request)

`ExecuteOntapPatch` dispatches the ONTAP `PATCH` request to the `StoragePool` cluster.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExecuteOntapPatchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ExecuteOntapPatchRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteOntapPatchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ExecuteOntapPatchResponse)` |   
  
### executeOntapPost(ExecuteOntapPostRequest request)
    
    
    public ExecuteOntapPostResponse executeOntapPost(ExecuteOntapPostRequest request)

`ExecuteOntapPost` dispatches the ONTAP `POST` request to the `StoragePool` cluster.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExecuteOntapPostRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ExecuteOntapPostRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExecuteOntapPostResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ExecuteOntapPostResponse)` |   
  
### getActiveDirectory(GetActiveDirectoryRequest request)
    
    
    public ActiveDirectory getActiveDirectory(GetActiveDirectoryRequest request)

Describes a specified active directory.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetActiveDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetActiveDirectoryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ActiveDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ActiveDirectory)` |   
  
### getBackup(GetBackupRequest request)
    
    
    public Backup getBackup(GetBackupRequest request)

Returns the description of the specified backup

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.Backup)` |   
  
### getBackupPolicy(GetBackupPolicyRequest request)
    
    
    public BackupPolicy getBackupPolicy(GetBackupPolicyRequest request)

Returns the description of the specified backup policy by backup_policy_id.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetBackupPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.BackupPolicy)` |   
  
### getBackupVault(GetBackupVaultRequest request)
    
    
    public BackupVault getBackupVault(GetBackupVaultRequest request)

Returns the description of the specified backup vault

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetBackupVaultRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.BackupVault)` |   
  
### getHostGroup(GetHostGroupRequest request)
    
    
    public HostGroup getHostGroup(GetHostGroupRequest request)

Returns details of the specified host group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHostGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetHostGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HostGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.HostGroup)` |   
  
### getKmsConfig(GetKmsConfigRequest request)
    
    
    public KmsConfig getKmsConfig(GetKmsConfigRequest request)

Returns the description of the specified KMS config by kms_config_id.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetKmsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetKmsConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[KmsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.KmsConfig)` |   
  
### getQuotaRule(GetQuotaRuleRequest request)
    
    
    public QuotaRule getQuotaRule(GetQuotaRuleRequest request)

Returns details of the specified quota rule.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetQuotaRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetQuotaRuleRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QuotaRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.QuotaRule)` |   
  
### getReplication(GetReplicationRequest request)
    
    
    public Replication getReplication(GetReplicationRequest request)

Describe a replication for a volume.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetReplicationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Replication](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.Replication)` |   
  
### getSnapshot(GetSnapshotRequest request)
    
    
    public Snapshot getSnapshot(GetSnapshotRequest request)

Describe a snapshot for a volume.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetSnapshotRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.Snapshot)` |   
  
### getStoragePool(GetStoragePoolRequest request)
    
    
    public StoragePool getStoragePool(GetStoragePoolRequest request)

Returns the description of the specified storage pool by poolId.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetStoragePoolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StoragePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.StoragePool)` |   
  
### getVolume(GetVolumeRequest request)
    
    
    public Volume getVolume(GetVolumeRequest request)

Gets details of a single Volume.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetVolumeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetVolumeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.Volume)` |   
  
### listActiveDirectories(ListActiveDirectoriesRequest request)
    
    
    public ListActiveDirectoriesResponse listActiveDirectories(ListActiveDirectoriesRequest request)

Lists active directories.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListActiveDirectoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListActiveDirectoriesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListActiveDirectoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListActiveDirectoriesResponse)` |   
  
### listBackupPolicies(ListBackupPoliciesRequest request)
    
    
    public ListBackupPoliciesResponse listBackupPolicies(ListBackupPoliciesRequest request)

Returns list of all available backup policies.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListBackupPoliciesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListBackupPoliciesResponse)` |   
  
### listBackupVaults(ListBackupVaultsRequest request)
    
    
    public ListBackupVaultsResponse listBackupVaults(ListBackupVaultsRequest request)

Returns list of all available backup vaults.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupVaultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListBackupVaultsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupVaultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListBackupVaultsResponse)` |   
  
### listBackups(ListBackupsRequest request)
    
    
    public ListBackupsResponse listBackups(ListBackupsRequest request)

Returns descriptions of all backups for a backupVault.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListBackupsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListBackupsResponse)` |   
  
### listHostGroups(ListHostGroupsRequest request)
    
    
    public ListHostGroupsResponse listHostGroups(ListHostGroupsRequest request)

Returns a list of host groups in a `location`. Use `-` as location to list host groups across all locations.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListHostGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListHostGroupsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListHostGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListHostGroupsResponse)` |   
  
### listKmsConfigs(ListKmsConfigsRequest request)
    
    
    public ListKmsConfigsResponse listKmsConfigs(ListKmsConfigsRequest request)

Returns descriptions of all KMS configs owned by the caller.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListKmsConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListKmsConfigsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListKmsConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListKmsConfigsResponse)` |   
  
### listQuotaRules(ListQuotaRulesRequest request)
    
    
    public ListQuotaRulesResponse listQuotaRules(ListQuotaRulesRequest request)

Returns list of all quota rules in a location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListQuotaRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListQuotaRulesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListQuotaRulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListQuotaRulesResponse)` |   
  
### listReplications(ListReplicationsRequest request)
    
    
    public ListReplicationsResponse listReplications(ListReplicationsRequest request)

Returns descriptions of all replications for a volume.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReplicationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListReplicationsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListReplicationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListReplicationsResponse)` |   
  
### listSnapshots(ListSnapshotsRequest request)
    
    
    public ListSnapshotsResponse listSnapshots(ListSnapshotsRequest request)

Returns descriptions of all snapshots for a volume.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListSnapshotsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListSnapshotsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListSnapshotsResponse)` |   
  
### listStoragePools(ListStoragePoolsRequest request)
    
    
    public ListStoragePoolsResponse listStoragePools(ListStoragePoolsRequest request)

Returns descriptions of all storage pools owned by the caller.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListStoragePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListStoragePoolsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListStoragePoolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListStoragePoolsResponse)` |   
  
### listVolumes(ListVolumesRequest request)
    
    
    public ListVolumesResponse listVolumes(ListVolumesRequest request)

Lists Volumes in a given project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListVolumesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListVolumesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListVolumesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListVolumesResponse)` |   
  
### restoreBackupFiles(RestoreBackupFilesRequest request)
    
    
    public Operation restoreBackupFiles(RestoreBackupFilesRequest request)

Restore files from a backup to a volume.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestoreBackupFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.RestoreBackupFilesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### resumeReplication(ResumeReplicationRequest request)
    
    
    public Operation resumeReplication(ResumeReplicationRequest request)

Resume Cross Region Replication.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResumeReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ResumeReplicationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### reverseReplicationDirection(ReverseReplicationDirectionRequest request)
    
    
    public Operation reverseReplicationDirection(ReverseReplicationDirectionRequest request)

Reverses direction of replication. Source becomes destination and destination becomes source.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReverseReplicationDirectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ReverseReplicationDirectionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### revertVolume(RevertVolumeRequest request)
    
    
    public Operation revertVolume(RevertVolumeRequest request)

Revert an existing volume to a specified snapshot. Warning! This operation will permanently revert all changes made after the snapshot was created.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RevertVolumeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.RevertVolumeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### stopReplication(StopReplicationRequest request)
    
    
    public Operation stopReplication(StopReplicationRequest request)

Stop Cross Region Replication.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.StopReplicationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### switchActiveReplicaZone(SwitchActiveReplicaZoneRequest request)
    
    
    public Operation switchActiveReplicaZone(SwitchActiveReplicaZoneRequest request)

This operation will switch the active/replica zone for a regional storagePool.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SwitchActiveReplicaZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.SwitchActiveReplicaZoneRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### syncReplication(SyncReplicationRequest request)
    
    
    public Operation syncReplication(SyncReplicationRequest request)

Syncs the replication. This will invoke one time volume data transfer from source to destination.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SyncReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.SyncReplicationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateActiveDirectory(UpdateActiveDirectoryRequest request)
    
    
    public Operation updateActiveDirectory(UpdateActiveDirectoryRequest request)

Update the parameters of an active directories.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateActiveDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateActiveDirectoryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateBackup(UpdateBackupRequest request)
    
    
    public Operation updateBackup(UpdateBackupRequest request)

Update backup with full spec.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateBackupPolicy(UpdateBackupPolicyRequest request)
    
    
    public Operation updateBackupPolicy(UpdateBackupPolicyRequest request)

Updates settings of a specific backup policy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateBackupPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateBackupVault(UpdateBackupVaultRequest request)
    
    
    public Operation updateBackupVault(UpdateBackupVaultRequest request)

Updates the settings of a specific backup vault.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateBackupVaultRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateHostGroup(UpdateHostGroupRequest request)
    
    
    public Operation updateHostGroup(UpdateHostGroupRequest request)

Updates an existing host group.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateHostGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateHostGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateKmsConfig(UpdateKmsConfigRequest request)
    
    
    public Operation updateKmsConfig(UpdateKmsConfigRequest request)

Updates the Kms config properties with the full spec

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateKmsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateKmsConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateQuotaRule(UpdateQuotaRuleRequest request)
    
    
    public Operation updateQuotaRule(UpdateQuotaRuleRequest request)

Updates a quota rule.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateQuotaRuleRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateReplication(UpdateReplicationRequest request)
    
    
    public Operation updateReplication(UpdateReplicationRequest request)

Updates the settings of a specific replication.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateReplicationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateSnapshot(UpdateSnapshotRequest request)
    
    
    public Operation updateSnapshot(UpdateSnapshotRequest request)

Updates the settings of a specific snapshot.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateSnapshotRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateStoragePool(UpdateStoragePoolRequest request)
    
    
    public Operation updateStoragePool(UpdateStoragePoolRequest request)

Updates the storage pool properties with the full spec

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateStoragePoolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateVolume(UpdateVolumeRequest request)
    
    
    public Operation updateVolume(UpdateVolumeRequest request)

Updates the parameters of a single Volume.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateVolumeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateVolumeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### validateDirectoryService(ValidateDirectoryServiceRequest request)
    
    
    public Operation validateDirectoryService(ValidateDirectoryServiceRequest request)

ValidateDirectoryService does a connectivity check for a directory service policy attached to the storage pool.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ValidateDirectoryServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ValidateDirectoryServiceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### verifyKmsConfig(VerifyKmsConfigRequest request)
    
    
    public VerifyKmsConfigResponse verifyKmsConfig(VerifyKmsConfigRequest request)

Verifies KMS config reachability.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[VerifyKmsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.VerifyKmsConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VerifyKmsConfigResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.VerifyKmsConfigResponse)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
