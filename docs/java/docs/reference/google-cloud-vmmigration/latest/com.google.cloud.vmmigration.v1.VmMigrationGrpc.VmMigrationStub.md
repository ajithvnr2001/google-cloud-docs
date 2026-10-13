---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.VmMigrationGrpc.VmMigrationStub
title: Class VmMigrationGrpc.VmMigrationStub (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:41:44.085141+00:00
---

# Class VmMigrationGrpc.VmMigrationStub (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.VmMigrationGrpc.VmMigrationStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class VmMigrationGrpc.VmMigrationStub (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.5  1.2.0  1.1.1  1.0.5 
    
    
    public static final class VmMigrationGrpc.VmMigrationStub extends AbstractAsyncStub<VmMigrationGrpc.VmMigrationStub>

A stub to allow clients to do asynchronous rpc calls to service VmMigration.

VM Migration Service

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > VmMigrationGrpc.VmMigrationStub

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

### addGroupMigration(AddGroupMigrationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void addGroupMigration(AddGroupMigrationRequest request, StreamObserver<Operation> responseObserver)

Adds a MigratingVm to a Group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddGroupMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.AddGroupMigrationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected VmMigrationGrpc.VmMigrationStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[VmMigrationGrpc.VmMigrationStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.VmMigrationGrpc.VmMigrationStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### cancelCloneJob(CancelCloneJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void cancelCloneJob(CancelCloneJobRequest request, StreamObserver<Operation> responseObserver)

Initiates the cancellation of a running clone job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelCloneJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CancelCloneJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### cancelCutoverJob(CancelCutoverJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void cancelCutoverJob(CancelCutoverJobRequest request, StreamObserver<Operation> responseObserver)

Initiates the cancellation of a running cutover job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelCutoverJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CancelCutoverJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### cancelDiskMigrationJob(CancelDiskMigrationJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void cancelDiskMigrationJob(CancelDiskMigrationJobRequest request, StreamObserver<Operation> responseObserver)

Cancels the disk migration job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelDiskMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CancelDiskMigrationJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### cancelImageImportJob(CancelImageImportJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void cancelImageImportJob(CancelImageImportJobRequest request, StreamObserver<Operation> responseObserver)

Initiates the cancellation of a running ImageImportJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelImageImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CancelImageImportJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createCloneJob(CreateCloneJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createCloneJob(CreateCloneJobRequest request, StreamObserver<Operation> responseObserver)

Initiates a Clone of a specific migrating VM.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCloneJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CreateCloneJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createCutoverJob(CreateCutoverJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createCutoverJob(CreateCutoverJobRequest request, StreamObserver<Operation> responseObserver)

Initiates a Cutover of a specific migrating VM. The returned LRO is completed when the cutover job resource is created and the job is initiated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCutoverJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CreateCutoverJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createDatacenterConnector(CreateDatacenterConnectorRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createDatacenterConnector(CreateDatacenterConnectorRequest request, StreamObserver<Operation> responseObserver)

Creates a new DatacenterConnector in a given Source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDatacenterConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CreateDatacenterConnectorRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createDiskMigrationJob(CreateDiskMigrationJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createDiskMigrationJob(CreateDiskMigrationJobRequest request, StreamObserver<Operation> responseObserver)

Creates a new disk migration job in a given Source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDiskMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CreateDiskMigrationJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createGroup(CreateGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createGroup(CreateGroupRequest request, StreamObserver<Operation> responseObserver)

Creates a new Group in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CreateGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createImageImport(CreateImageImportRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createImageImport(CreateImageImportRequest request, StreamObserver<Operation> responseObserver)

Creates a new ImageImport in a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateImageImportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CreateImageImportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createMigratingVm(CreateMigratingVmRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createMigratingVm(CreateMigratingVmRequest request, StreamObserver<Operation> responseObserver)

Creates a new MigratingVm in a given Source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMigratingVmRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CreateMigratingVmRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createSource(CreateSourceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createSource(CreateSourceRequest request, StreamObserver<Operation> responseObserver)

Creates a new Source in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CreateSourceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createTargetProject(CreateTargetProjectRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createTargetProject(CreateTargetProjectRequest request, StreamObserver<Operation> responseObserver)

Creates a new TargetProject in a given project. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTargetProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CreateTargetProjectRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createUtilizationReport(CreateUtilizationReportRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createUtilizationReport(CreateUtilizationReportRequest request, StreamObserver<Operation> responseObserver)

Creates a new UtilizationReport.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUtilizationReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CreateUtilizationReportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteDatacenterConnector(DeleteDatacenterConnectorRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteDatacenterConnector(DeleteDatacenterConnectorRequest request, StreamObserver<Operation> responseObserver)

Deletes a single DatacenterConnector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDatacenterConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.DeleteDatacenterConnectorRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteDiskMigrationJob(DeleteDiskMigrationJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteDiskMigrationJob(DeleteDiskMigrationJobRequest request, StreamObserver<Operation> responseObserver)

Deletes a single DiskMigrationJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDiskMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.DeleteDiskMigrationJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteGroup(DeleteGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteGroup(DeleteGroupRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.DeleteGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteImageImport(DeleteImageImportRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteImageImport(DeleteImageImportRequest request, StreamObserver<Operation> responseObserver)

Deletes a single ImageImport.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteImageImportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.DeleteImageImportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteMigratingVm(DeleteMigratingVmRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteMigratingVm(DeleteMigratingVmRequest request, StreamObserver<Operation> responseObserver)

Deletes a single MigratingVm.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMigratingVmRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.DeleteMigratingVmRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteSource(DeleteSourceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteSource(DeleteSourceRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.DeleteSourceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteTargetProject(DeleteTargetProjectRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteTargetProject(DeleteTargetProjectRequest request, StreamObserver<Operation> responseObserver)

Deletes a single TargetProject. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTargetProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.DeleteTargetProjectRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteUtilizationReport(DeleteUtilizationReportRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteUtilizationReport(DeleteUtilizationReportRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Utilization Report.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUtilizationReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.DeleteUtilizationReportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### extendMigration(ExtendMigrationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void extendMigration(ExtendMigrationRequest request, StreamObserver<Operation> responseObserver)

Extend the migrating VM time to live.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExtendMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ExtendMigrationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### fetchInventory(FetchInventoryRequest request, StreamObserver<FetchInventoryResponse> responseObserver)
    
    
    public void fetchInventory(FetchInventoryRequest request, StreamObserver<FetchInventoryResponse> responseObserver)

List remote source's inventory of VMs. The remote source is the onprem vCenter (remote in the sense it's not in Compute Engine). The inventory describes the list of existing VMs in that source. Note that this operation lists the VMs on the remote source, as opposed to listing the MigratingVms resources in the vmmigration service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.FetchInventoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchInventoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.FetchInventoryResponse)>`  
  
  
### fetchStorageInventory(FetchStorageInventoryRequest request, StreamObserver<FetchStorageInventoryResponse> responseObserver)
    
    
    public void fetchStorageInventory(FetchStorageInventoryRequest request, StreamObserver<FetchStorageInventoryResponse> responseObserver)

List remote source's inventory of storage resources. The remote source is another cloud vendor (e.g. AWS, Azure). The inventory describes the list of existing storage resources in that source. Note that this operation lists the resources on the remote source, as opposed to listing the MigratingVms resources in the vmmigration service.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchStorageInventoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.FetchStorageInventoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchStorageInventoryResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.FetchStorageInventoryResponse)>`  
  
  
### finalizeMigration(FinalizeMigrationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void finalizeMigration(FinalizeMigrationRequest request, StreamObserver<Operation> responseObserver)

Marks a migration as completed, deleting migration resources that are no longer being used. Only applicable after cutover is done.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FinalizeMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.FinalizeMigrationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getCloneJob(GetCloneJobRequest request, StreamObserver<CloneJob> responseObserver)
    
    
    public void getCloneJob(GetCloneJobRequest request, StreamObserver<CloneJob> responseObserver)

Gets details of a single CloneJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCloneJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.GetCloneJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CloneJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CloneJob)>`  
  
  
### getCutoverJob(GetCutoverJobRequest request, StreamObserver<CutoverJob> responseObserver)
    
    
    public void getCutoverJob(GetCutoverJobRequest request, StreamObserver<CutoverJob> responseObserver)

Gets details of a single CutoverJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCutoverJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.GetCutoverJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CutoverJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.CutoverJob)>`  
  
  
### getDatacenterConnector(GetDatacenterConnectorRequest request, StreamObserver<DatacenterConnector> responseObserver)
    
    
    public void getDatacenterConnector(GetDatacenterConnectorRequest request, StreamObserver<DatacenterConnector> responseObserver)

Gets details of a single DatacenterConnector.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDatacenterConnectorRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.GetDatacenterConnectorRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DatacenterConnector](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.DatacenterConnector)>`  
  
  
### getDiskMigrationJob(GetDiskMigrationJobRequest request, StreamObserver<DiskMigrationJob> responseObserver)
    
    
    public void getDiskMigrationJob(GetDiskMigrationJobRequest request, StreamObserver<DiskMigrationJob> responseObserver)

Gets details of a single DiskMigrationJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDiskMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.GetDiskMigrationJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DiskMigrationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.DiskMigrationJob)>`  
  
  
### getGroup(GetGroupRequest request, StreamObserver<Group> responseObserver)
    
    
    public void getGroup(GetGroupRequest request, StreamObserver<Group> responseObserver)

Gets details of a single Group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.GetGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Group](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.Group)>`  
  
  
### getImageImport(GetImageImportRequest request, StreamObserver<ImageImport> responseObserver)
    
    
    public void getImageImport(GetImageImportRequest request, StreamObserver<ImageImport> responseObserver)

Gets details of a single ImageImport.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetImageImportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.GetImageImportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ImageImport](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ImageImport)>`  
  
  
### getImageImportJob(GetImageImportJobRequest request, StreamObserver<ImageImportJob> responseObserver)
    
    
    public void getImageImportJob(GetImageImportJobRequest request, StreamObserver<ImageImportJob> responseObserver)

Gets details of a single ImageImportJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetImageImportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.GetImageImportJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ImageImportJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ImageImportJob)>`  
  
  
### getMigratingVm(GetMigratingVmRequest request, StreamObserver<MigratingVm> responseObserver)
    
    
    public void getMigratingVm(GetMigratingVmRequest request, StreamObserver<MigratingVm> responseObserver)

Gets details of a single MigratingVm.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMigratingVmRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.GetMigratingVmRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[MigratingVm](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.MigratingVm)>`  
  
  
### getReplicationCycle(GetReplicationCycleRequest request, StreamObserver<ReplicationCycle> responseObserver)
    
    
    public void getReplicationCycle(GetReplicationCycleRequest request, StreamObserver<ReplicationCycle> responseObserver)

Gets details of a single ReplicationCycle.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReplicationCycleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.GetReplicationCycleRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ReplicationCycle](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ReplicationCycle)>`  
  
  
### getSource(GetSourceRequest request, StreamObserver<Source> responseObserver)
    
    
    public void getSource(GetSourceRequest request, StreamObserver<Source> responseObserver)

Gets details of a single Source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.GetSourceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.Source)>`  
  
  
### getTargetProject(GetTargetProjectRequest request, StreamObserver<TargetProject> responseObserver)
    
    
    public void getTargetProject(GetTargetProjectRequest request, StreamObserver<TargetProject> responseObserver)

Gets details of a single TargetProject. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTargetProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.GetTargetProjectRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[TargetProject](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.TargetProject)>`  
  
  
### getUtilizationReport(GetUtilizationReportRequest request, StreamObserver<UtilizationReport> responseObserver)
    
    
    public void getUtilizationReport(GetUtilizationReportRequest request, StreamObserver<UtilizationReport> responseObserver)

Gets a single Utilization Report.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUtilizationReportRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.GetUtilizationReportRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UtilizationReport](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.UtilizationReport)>`  
  
  
### listCloneJobs(ListCloneJobsRequest request, StreamObserver<ListCloneJobsResponse> responseObserver)
    
    
    public void listCloneJobs(ListCloneJobsRequest request, StreamObserver<ListCloneJobsResponse> responseObserver)

Lists the CloneJobs of a migrating VM. Only 25 most recent CloneJobs are listed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCloneJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListCloneJobsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListCloneJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListCloneJobsResponse)>`  
  
  
### listCutoverJobs(ListCutoverJobsRequest request, StreamObserver<ListCutoverJobsResponse> responseObserver)
    
    
    public void listCutoverJobs(ListCutoverJobsRequest request, StreamObserver<ListCutoverJobsResponse> responseObserver)

Lists the CutoverJobs of a migrating VM. Only 25 most recent CutoverJobs are listed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCutoverJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListCutoverJobsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListCutoverJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListCutoverJobsResponse)>`  
  
  
### listDatacenterConnectors(ListDatacenterConnectorsRequest request, StreamObserver<ListDatacenterConnectorsResponse> responseObserver)
    
    
    public void listDatacenterConnectors(ListDatacenterConnectorsRequest request, StreamObserver<ListDatacenterConnectorsResponse> responseObserver)

Lists DatacenterConnectors in a given Source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDatacenterConnectorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListDatacenterConnectorsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListDatacenterConnectorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListDatacenterConnectorsResponse)>`  
  
  
### listDiskMigrationJobs(ListDiskMigrationJobsRequest request, StreamObserver<ListDiskMigrationJobsResponse> responseObserver)
    
    
    public void listDiskMigrationJobs(ListDiskMigrationJobsRequest request, StreamObserver<ListDiskMigrationJobsResponse> responseObserver)

Lists DiskMigrationJobs in a given Source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDiskMigrationJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListDiskMigrationJobsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListDiskMigrationJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListDiskMigrationJobsResponse)>`  
  
  
### listGroups(ListGroupsRequest request, StreamObserver<ListGroupsResponse> responseObserver)
    
    
    public void listGroups(ListGroupsRequest request, StreamObserver<ListGroupsResponse> responseObserver)

Lists Groups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListGroupsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListGroupsResponse)>`  
  
  
### listImageImportJobs(ListImageImportJobsRequest request, StreamObserver<ListImageImportJobsResponse> responseObserver)
    
    
    public void listImageImportJobs(ListImageImportJobsRequest request, StreamObserver<ListImageImportJobsResponse> responseObserver)

Lists ImageImportJobs in a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListImageImportJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListImageImportJobsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListImageImportJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListImageImportJobsResponse)>`  
  
  
### listImageImports(ListImageImportsRequest request, StreamObserver<ListImageImportsResponse> responseObserver)
    
    
    public void listImageImports(ListImageImportsRequest request, StreamObserver<ListImageImportsResponse> responseObserver)

Lists ImageImports in a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListImageImportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListImageImportsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListImageImportsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListImageImportsResponse)>`  
  
  
### listMigratingVms(ListMigratingVmsRequest request, StreamObserver<ListMigratingVmsResponse> responseObserver)
    
    
    public void listMigratingVms(ListMigratingVmsRequest request, StreamObserver<ListMigratingVmsResponse> responseObserver)

Lists MigratingVms in a given Source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMigratingVmsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListMigratingVmsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMigratingVmsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListMigratingVmsResponse)>`  
  
  
### listReplicationCycles(ListReplicationCyclesRequest request, StreamObserver<ListReplicationCyclesResponse> responseObserver)
    
    
    public void listReplicationCycles(ListReplicationCyclesRequest request, StreamObserver<ListReplicationCyclesResponse> responseObserver)

Lists ReplicationCycles in a given MigratingVM.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReplicationCyclesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListReplicationCyclesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListReplicationCyclesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListReplicationCyclesResponse)>`  
  
  
### listSources(ListSourcesRequest request, StreamObserver<ListSourcesResponse> responseObserver)
    
    
    public void listSources(ListSourcesRequest request, StreamObserver<ListSourcesResponse> responseObserver)

Lists Sources in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListSourcesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListSourcesResponse)>`  
  
  
### listTargetProjects(ListTargetProjectsRequest request, StreamObserver<ListTargetProjectsResponse> responseObserver)
    
    
    public void listTargetProjects(ListTargetProjectsRequest request, StreamObserver<ListTargetProjectsResponse> responseObserver)

Lists TargetProjects in a given project. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTargetProjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListTargetProjectsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListTargetProjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListTargetProjectsResponse)>`  
  
  
### listUtilizationReports(ListUtilizationReportsRequest request, StreamObserver<ListUtilizationReportsResponse> responseObserver)
    
    
    public void listUtilizationReports(ListUtilizationReportsRequest request, StreamObserver<ListUtilizationReportsResponse> responseObserver)

Lists Utilization Reports of the given Source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUtilizationReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListUtilizationReportsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListUtilizationReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ListUtilizationReportsResponse)>`  
  
  
### pauseMigration(PauseMigrationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void pauseMigration(PauseMigrationRequest request, StreamObserver<Operation> responseObserver)

Pauses a migration for a VM. If cycle tasks are running they will be cancelled, preserving source task data. Further replication cycles will not be triggered while the VM is paused.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.PauseMigrationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### removeGroupMigration(RemoveGroupMigrationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void removeGroupMigration(RemoveGroupMigrationRequest request, StreamObserver<Operation> responseObserver)

Removes a MigratingVm from a Group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveGroupMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.RemoveGroupMigrationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### resumeMigration(ResumeMigrationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void resumeMigration(ResumeMigrationRequest request, StreamObserver<Operation> responseObserver)

Resumes a migration for a VM. When called on a paused migration, will start the process of uploading data and creating snapshots; when called on a completed cut-over migration, will update the migration to active state and start the process of uploading data and creating snapshots.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ResumeMigrationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### runDiskMigrationJob(RunDiskMigrationJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void runDiskMigrationJob(RunDiskMigrationJobRequest request, StreamObserver<Operation> responseObserver)

Runs the disk migration job.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunDiskMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.RunDiskMigrationJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### startMigration(StartMigrationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void startMigration(StartMigrationRequest request, StreamObserver<Operation> responseObserver)

Starts migration for a VM. Starts the process of uploading data and creating snapshots, in replication cycles scheduled by the policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.StartMigrationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateDiskMigrationJob(UpdateDiskMigrationJobRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateDiskMigrationJob(UpdateDiskMigrationJobRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single DiskMigrationJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDiskMigrationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.UpdateDiskMigrationJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateGroup(UpdateGroupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateGroup(UpdateGroupRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single Group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.UpdateGroupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateMigratingVm(UpdateMigratingVmRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateMigratingVm(UpdateMigratingVmRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single MigratingVm.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMigratingVmRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.UpdateMigratingVmRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateSource(UpdateSourceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateSource(UpdateSourceRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single Source.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.UpdateSourceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateTargetProject(UpdateTargetProjectRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateTargetProject(UpdateTargetProjectRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single TargetProject. NOTE: TargetProject is a global resource; hence the only supported value for location is `global`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTargetProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.UpdateTargetProjectRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### upgradeAppliance(UpgradeApplianceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void upgradeAppliance(UpgradeApplianceRequest request, StreamObserver<Operation> responseObserver)

Upgrades the appliance relate to this DatacenterConnector to the in-place updateable version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpgradeApplianceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.UpgradeApplianceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
