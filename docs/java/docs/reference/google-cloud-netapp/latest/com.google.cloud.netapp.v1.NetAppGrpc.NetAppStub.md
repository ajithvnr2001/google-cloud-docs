---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.NetAppGrpc.NetAppStub
title: Class NetAppGrpc.NetAppStub (0.78.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:39:21.412298+00:00
---

# Class NetAppGrpc.NetAppStub (0.78.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.NetAppGrpc.NetAppStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NetAppGrpc.NetAppStub (0.78.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.78.0 (latest)  0.74.0  0.73.0  0.72.0  0.70.0  0.67.0  0.66.0  0.64.0  0.62.0  0.61.0  0.59.0  0.57.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.43.0  0.42.0  0.41.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class NetAppGrpc.NetAppStub extends AbstractAsyncStub<NetAppGrpc.NetAppStub>

A stub to allow clients to do asynchronous rpc calls to service NetApp.

NetApp Files Google Cloud Service

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > NetAppGrpc.NetAppStub

## Inherited Members

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected NetAppGrpc.NetAppStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetAppGrpc.NetAppStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.NetAppGrpc.NetAppStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createActiveDirectory(CreateActiveDirectoryRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createActiveDirectory(CreateActiveDirectoryRequest request, StreamObserver<Operation> responseObserver)

CreateActiveDirectory Creates the active directory specified in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateActiveDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateActiveDirectoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createBackup(CreateBackupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createBackup(CreateBackupRequest request, StreamObserver<Operation> responseObserver)

Creates a backup from the volume specified in the request The backup can be created from the given snapshot if specified in the request. If no snapshot specified, there'll be a new snapshot taken to initiate the backup creation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createBackupPolicy(CreateBackupPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createBackupPolicy(CreateBackupPolicyRequest request, StreamObserver<Operation> responseObserver)

Creates new backup policy

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackupPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateBackupPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createBackupVault(CreateBackupVaultRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createBackupVault(CreateBackupVaultRequest request, StreamObserver<Operation> responseObserver)

Creates new backup vault

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateBackupVaultRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createHostGroup(CreateHostGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createHostGroup(CreateHostGroupRequest request, StreamObserver<Operation> responseObserver)

Creates a new host group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateHostGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateHostGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createKmsConfig(CreateKmsConfigRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createKmsConfig(CreateKmsConfigRequest request, StreamObserver<Operation> responseObserver)

Creates a new KMS config.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateKmsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateKmsConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createQuotaRule(CreateQuotaRuleRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createQuotaRule(CreateQuotaRuleRequest request, StreamObserver<Operation> responseObserver)

Creates a new quota rule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateQuotaRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateQuotaRuleRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createReplication(CreateReplicationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createReplication(CreateReplicationRequest request, StreamObserver<Operation> responseObserver)

Create a new replication for a volume.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateReplicationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createSnapshot(CreateSnapshotRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createSnapshot(CreateSnapshotRequest request, StreamObserver<Operation> responseObserver)

Create a new snapshot for a volume.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateSnapshotRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createStoragePool(CreateStoragePoolRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createStoragePool(CreateStoragePoolRequest request, StreamObserver<Operation> responseObserver)

Creates a new storage pool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateStoragePoolRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createVolume(CreateVolumeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createVolume(CreateVolumeRequest request, StreamObserver<Operation> responseObserver)

Creates a new Volume in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateVolumeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.CreateVolumeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteActiveDirectory(DeleteActiveDirectoryRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteActiveDirectory(DeleteActiveDirectoryRequest request, StreamObserver<Operation> responseObserver)

Delete the active directory specified in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteActiveDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteActiveDirectoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteBackup(DeleteBackupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteBackup(DeleteBackupRequest request, StreamObserver<Operation> responseObserver)

Warning! This operation will permanently delete the backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteBackupPolicy(DeleteBackupPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteBackupPolicy(DeleteBackupPolicyRequest request, StreamObserver<Operation> responseObserver)

Warning! This operation will permanently delete the backup policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteBackupPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteBackupVault(DeleteBackupVaultRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteBackupVault(DeleteBackupVaultRequest request, StreamObserver<Operation> responseObserver)

Warning! This operation will permanently delete the backup vault.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteBackupVaultRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteHostGroup(DeleteHostGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteHostGroup(DeleteHostGroupRequest request, StreamObserver<Operation> responseObserver)

Deletes a host group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteHostGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteHostGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteKmsConfig(DeleteKmsConfigRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteKmsConfig(DeleteKmsConfigRequest request, StreamObserver<Operation> responseObserver)

Warning! This operation will permanently delete the Kms config.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteKmsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteKmsConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteQuotaRule(DeleteQuotaRuleRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteQuotaRule(DeleteQuotaRuleRequest request, StreamObserver<Operation> responseObserver)

Deletes a quota rule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteQuotaRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteQuotaRuleRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteReplication(DeleteReplicationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteReplication(DeleteReplicationRequest request, StreamObserver<Operation> responseObserver)

Deletes a replication.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteReplicationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteSnapshot(DeleteSnapshotRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteSnapshot(DeleteSnapshotRequest request, StreamObserver<Operation> responseObserver)

Deletes a snapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteSnapshotRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteStoragePool(DeleteStoragePoolRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteStoragePool(DeleteStoragePoolRequest request, StreamObserver<Operation> responseObserver)

Warning! This operation will permanently delete the storage pool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteStoragePoolRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteVolume(DeleteVolumeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteVolume(DeleteVolumeRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Volume.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteVolumeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.DeleteVolumeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### encryptVolumes(EncryptVolumesRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void encryptVolumes(EncryptVolumesRequest request, StreamObserver<Operation> responseObserver)

Encrypt the existing volumes without CMEK encryption with the desired the KMS config for the whole region.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EncryptVolumesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.EncryptVolumesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### establishPeering(EstablishPeeringRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void establishPeering(EstablishPeeringRequest request, StreamObserver<Operation> responseObserver)

Establish replication peering.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EstablishPeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.EstablishPeeringRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### establishVolumePeering(EstablishVolumePeeringRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void establishVolumePeering(EstablishVolumePeeringRequest request, StreamObserver<Operation> responseObserver)

Establish volume peering. This is used to establish cluster and svm peerings between the GCNV and OnPrem clusters.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EstablishVolumePeeringRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.EstablishVolumePeeringRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### executeOntapDelete(ExecuteOntapDeleteRequest request, StreamObserver<ExecuteOntapDeleteResponse> responseObserver)
    
    
    public void executeOntapDelete(ExecuteOntapDeleteRequest request, StreamObserver<ExecuteOntapDeleteResponse> responseObserver)

`ExecuteOntapDelete` dispatches the ONTAP `DELETE` request to the `StoragePool` cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteOntapDeleteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ExecuteOntapDeleteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ExecuteOntapDeleteResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ExecuteOntapDeleteResponse)>`  
  
  
### executeOntapGet(ExecuteOntapGetRequest request, StreamObserver<ExecuteOntapGetResponse> responseObserver)
    
    
    public void executeOntapGet(ExecuteOntapGetRequest request, StreamObserver<ExecuteOntapGetResponse> responseObserver)

`ExecuteOntapGet` dispatches the ONTAP `GET` request to the `StoragePool` cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteOntapGetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ExecuteOntapGetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ExecuteOntapGetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ExecuteOntapGetResponse)>`  
  
  
### executeOntapPatch(ExecuteOntapPatchRequest request, StreamObserver<ExecuteOntapPatchResponse> responseObserver)
    
    
    public void executeOntapPatch(ExecuteOntapPatchRequest request, StreamObserver<ExecuteOntapPatchResponse> responseObserver)

`ExecuteOntapPatch` dispatches the ONTAP `PATCH` request to the `StoragePool` cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteOntapPatchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ExecuteOntapPatchRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ExecuteOntapPatchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ExecuteOntapPatchResponse)>`  
  
  
### executeOntapPost(ExecuteOntapPostRequest request, StreamObserver<ExecuteOntapPostResponse> responseObserver)
    
    
    public void executeOntapPost(ExecuteOntapPostRequest request, StreamObserver<ExecuteOntapPostResponse> responseObserver)

`ExecuteOntapPost` dispatches the ONTAP `POST` request to the `StoragePool` cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteOntapPostRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ExecuteOntapPostRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ExecuteOntapPostResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ExecuteOntapPostResponse)>`  
  
  
### getActiveDirectory(GetActiveDirectoryRequest request, StreamObserver<ActiveDirectory> responseObserver)
    
    
    public void getActiveDirectory(GetActiveDirectoryRequest request, StreamObserver<ActiveDirectory> responseObserver)

Describes a specified active directory.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetActiveDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetActiveDirectoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ActiveDirectory](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ActiveDirectory)>`  
  
  
### getBackup(GetBackupRequest request, StreamObserver<Backup> responseObserver)
    
    
    public void getBackup(GetBackupRequest request, StreamObserver<Backup> responseObserver)

Returns the description of the specified backup

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.Backup)>`  
  
  
### getBackupPolicy(GetBackupPolicyRequest request, StreamObserver<BackupPolicy> responseObserver)
    
    
    public void getBackupPolicy(GetBackupPolicyRequest request, StreamObserver<BackupPolicy> responseObserver)

Returns the description of the specified backup policy by backup_policy_id.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetBackupPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BackupPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.BackupPolicy)>`  
  
  
### getBackupVault(GetBackupVaultRequest request, StreamObserver<BackupVault> responseObserver)
    
    
    public void getBackupVault(GetBackupVaultRequest request, StreamObserver<BackupVault> responseObserver)

Returns the description of the specified backup vault

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetBackupVaultRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.BackupVault)>`  
  
  
### getHostGroup(GetHostGroupRequest request, StreamObserver<HostGroup> responseObserver)
    
    
    public void getHostGroup(GetHostGroupRequest request, StreamObserver<HostGroup> responseObserver)

Returns details of the specified host group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetHostGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetHostGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[HostGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.HostGroup)>`  
  
  
### getKmsConfig(GetKmsConfigRequest request, StreamObserver<KmsConfig> responseObserver)
    
    
    public void getKmsConfig(GetKmsConfigRequest request, StreamObserver<KmsConfig> responseObserver)

Returns the description of the specified KMS config by kms_config_id.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetKmsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetKmsConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[KmsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.KmsConfig)>`  
  
  
### getQuotaRule(GetQuotaRuleRequest request, StreamObserver<QuotaRule> responseObserver)
    
    
    public void getQuotaRule(GetQuotaRuleRequest request, StreamObserver<QuotaRule> responseObserver)

Returns details of the specified quota rule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetQuotaRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetQuotaRuleRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QuotaRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.QuotaRule)>`  
  
  
### getReplication(GetReplicationRequest request, StreamObserver<Replication> responseObserver)
    
    
    public void getReplication(GetReplicationRequest request, StreamObserver<Replication> responseObserver)

Describe a replication for a volume.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetReplicationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Replication](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.Replication)>`  
  
  
### getSnapshot(GetSnapshotRequest request, StreamObserver<Snapshot> responseObserver)
    
    
    public void getSnapshot(GetSnapshotRequest request, StreamObserver<Snapshot> responseObserver)

Describe a snapshot for a volume.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetSnapshotRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.Snapshot)>`  
  
  
### getStoragePool(GetStoragePoolRequest request, StreamObserver<StoragePool> responseObserver)
    
    
    public void getStoragePool(GetStoragePoolRequest request, StreamObserver<StoragePool> responseObserver)

Returns the description of the specified storage pool by poolId.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetStoragePoolRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[StoragePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.StoragePool)>`  
  
  
### getVolume(GetVolumeRequest request, StreamObserver<Volume> responseObserver)
    
    
    public void getVolume(GetVolumeRequest request, StreamObserver<Volume> responseObserver)

Gets details of a single Volume.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetVolumeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.GetVolumeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Volume](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.Volume)>`  
  
  
### listActiveDirectories(ListActiveDirectoriesRequest request, StreamObserver<ListActiveDirectoriesResponse> responseObserver)
    
    
    public void listActiveDirectories(ListActiveDirectoriesRequest request, StreamObserver<ListActiveDirectoriesResponse> responseObserver)

Lists active directories.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListActiveDirectoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListActiveDirectoriesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListActiveDirectoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListActiveDirectoriesResponse)>`  
  
  
### listBackupPolicies(ListBackupPoliciesRequest request, StreamObserver<ListBackupPoliciesResponse> responseObserver)
    
    
    public void listBackupPolicies(ListBackupPoliciesRequest request, StreamObserver<ListBackupPoliciesResponse> responseObserver)

Returns list of all available backup policies.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListBackupPoliciesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBackupPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListBackupPoliciesResponse)>`  
  
  
### listBackupVaults(ListBackupVaultsRequest request, StreamObserver<ListBackupVaultsResponse> responseObserver)
    
    
    public void listBackupVaults(ListBackupVaultsRequest request, StreamObserver<ListBackupVaultsResponse> responseObserver)

Returns list of all available backup vaults.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupVaultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListBackupVaultsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBackupVaultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListBackupVaultsResponse)>`  
  
  
### listBackups(ListBackupsRequest request, StreamObserver<ListBackupsResponse> responseObserver)
    
    
    public void listBackups(ListBackupsRequest request, StreamObserver<ListBackupsResponse> responseObserver)

Returns descriptions of all backups for a backupVault.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListBackupsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListBackupsResponse)>`  
  
  
### listHostGroups(ListHostGroupsRequest request, StreamObserver<ListHostGroupsResponse> responseObserver)
    
    
    public void listHostGroups(ListHostGroupsRequest request, StreamObserver<ListHostGroupsResponse> responseObserver)

Returns a list of host groups in a `location`. Use `-` as location to list host groups across all locations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListHostGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListHostGroupsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListHostGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListHostGroupsResponse)>`  
  
  
### listKmsConfigs(ListKmsConfigsRequest request, StreamObserver<ListKmsConfigsResponse> responseObserver)
    
    
    public void listKmsConfigs(ListKmsConfigsRequest request, StreamObserver<ListKmsConfigsResponse> responseObserver)

Returns descriptions of all KMS configs owned by the caller.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListKmsConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListKmsConfigsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListKmsConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListKmsConfigsResponse)>`  
  
  
### listQuotaRules(ListQuotaRulesRequest request, StreamObserver<ListQuotaRulesResponse> responseObserver)
    
    
    public void listQuotaRules(ListQuotaRulesRequest request, StreamObserver<ListQuotaRulesResponse> responseObserver)

Returns list of all quota rules in a location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListQuotaRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListQuotaRulesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListQuotaRulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListQuotaRulesResponse)>`  
  
  
### listReplications(ListReplicationsRequest request, StreamObserver<ListReplicationsResponse> responseObserver)
    
    
    public void listReplications(ListReplicationsRequest request, StreamObserver<ListReplicationsResponse> responseObserver)

Returns descriptions of all replications for a volume.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReplicationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListReplicationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListReplicationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListReplicationsResponse)>`  
  
  
### listSnapshots(ListSnapshotsRequest request, StreamObserver<ListSnapshotsResponse> responseObserver)
    
    
    public void listSnapshots(ListSnapshotsRequest request, StreamObserver<ListSnapshotsResponse> responseObserver)

Returns descriptions of all snapshots for a volume.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListSnapshotsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSnapshotsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListSnapshotsResponse)>`  
  
  
### listStoragePools(ListStoragePoolsRequest request, StreamObserver<ListStoragePoolsResponse> responseObserver)
    
    
    public void listStoragePools(ListStoragePoolsRequest request, StreamObserver<ListStoragePoolsResponse> responseObserver)

Returns descriptions of all storage pools owned by the caller.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListStoragePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListStoragePoolsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListStoragePoolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListStoragePoolsResponse)>`  
  
  
### listVolumes(ListVolumesRequest request, StreamObserver<ListVolumesResponse> responseObserver)
    
    
    public void listVolumes(ListVolumesRequest request, StreamObserver<ListVolumesResponse> responseObserver)

Lists Volumes in a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListVolumesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListVolumesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListVolumesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ListVolumesResponse)>`  
  
  
### restoreBackupFiles(RestoreBackupFilesRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void restoreBackupFiles(RestoreBackupFilesRequest request, StreamObserver<Operation> responseObserver)

Restore files from a backup to a volume.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreBackupFilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.RestoreBackupFilesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### resumeReplication(ResumeReplicationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void resumeReplication(ResumeReplicationRequest request, StreamObserver<Operation> responseObserver)

Resume Cross Region Replication.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ResumeReplicationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### reverseReplicationDirection(ReverseReplicationDirectionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void reverseReplicationDirection(ReverseReplicationDirectionRequest request, StreamObserver<Operation> responseObserver)

Reverses direction of replication. Source becomes destination and destination becomes source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReverseReplicationDirectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ReverseReplicationDirectionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### revertVolume(RevertVolumeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void revertVolume(RevertVolumeRequest request, StreamObserver<Operation> responseObserver)

Revert an existing volume to a specified snapshot. Warning! This operation will permanently revert all changes made after the snapshot was created.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RevertVolumeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.RevertVolumeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### stopReplication(StopReplicationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void stopReplication(StopReplicationRequest request, StreamObserver<Operation> responseObserver)

Stop Cross Region Replication.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StopReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.StopReplicationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### switchActiveReplicaZone(SwitchActiveReplicaZoneRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void switchActiveReplicaZone(SwitchActiveReplicaZoneRequest request, StreamObserver<Operation> responseObserver)

This operation will switch the active/replica zone for a regional storagePool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SwitchActiveReplicaZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.SwitchActiveReplicaZoneRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### syncReplication(SyncReplicationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void syncReplication(SyncReplicationRequest request, StreamObserver<Operation> responseObserver)

Syncs the replication. This will invoke one time volume data transfer from source to destination.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SyncReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.SyncReplicationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateActiveDirectory(UpdateActiveDirectoryRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateActiveDirectory(UpdateActiveDirectoryRequest request, StreamObserver<Operation> responseObserver)

Update the parameters of an active directories.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateActiveDirectoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateActiveDirectoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateBackup(UpdateBackupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateBackup(UpdateBackupRequest request, StreamObserver<Operation> responseObserver)

Update backup with full spec.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateBackupPolicy(UpdateBackupPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateBackupPolicy(UpdateBackupPolicyRequest request, StreamObserver<Operation> responseObserver)

Updates settings of a specific backup policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateBackupPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateBackupVault(UpdateBackupVaultRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateBackupVault(UpdateBackupVaultRequest request, StreamObserver<Operation> responseObserver)

Updates the settings of a specific backup vault.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateBackupVaultRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateHostGroup(UpdateHostGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateHostGroup(UpdateHostGroupRequest request, StreamObserver<Operation> responseObserver)

Updates an existing host group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateHostGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateHostGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateKmsConfig(UpdateKmsConfigRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateKmsConfig(UpdateKmsConfigRequest request, StreamObserver<Operation> responseObserver)

Updates the Kms config properties with the full spec

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateKmsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateKmsConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateQuotaRule(UpdateQuotaRuleRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateQuotaRule(UpdateQuotaRuleRequest request, StreamObserver<Operation> responseObserver)

Updates a quota rule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateQuotaRuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateQuotaRuleRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateReplication(UpdateReplicationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateReplication(UpdateReplicationRequest request, StreamObserver<Operation> responseObserver)

Updates the settings of a specific replication.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateReplicationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateSnapshot(UpdateSnapshotRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateSnapshot(UpdateSnapshotRequest request, StreamObserver<Operation> responseObserver)

Updates the settings of a specific snapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateSnapshotRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateStoragePool(UpdateStoragePoolRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateStoragePool(UpdateStoragePoolRequest request, StreamObserver<Operation> responseObserver)

Updates the storage pool properties with the full spec

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateStoragePoolRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateVolume(UpdateVolumeRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateVolume(UpdateVolumeRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single Volume.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateVolumeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.UpdateVolumeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### validateDirectoryService(ValidateDirectoryServiceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void validateDirectoryService(ValidateDirectoryServiceRequest request, StreamObserver<Operation> responseObserver)

ValidateDirectoryService does a connectivity check for a directory service policy attached to the storage pool.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ValidateDirectoryServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.ValidateDirectoryServiceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### verifyKmsConfig(VerifyKmsConfigRequest request, StreamObserver<VerifyKmsConfigResponse> responseObserver)
    
    
    public void verifyKmsConfig(VerifyKmsConfigRequest request, StreamObserver<VerifyKmsConfigResponse> responseObserver)

Verifies KMS config reachability.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[VerifyKmsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.VerifyKmsConfigRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[VerifyKmsConfigResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-netapp/latest/com.google.cloud.netapp.v1.VerifyKmsConfigResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
