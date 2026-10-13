---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupDRGrpc.BackupDRStub
title: Class BackupDRGrpc.BackupDRStub (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:25.508607+00:00
---

# Class BackupDRGrpc.BackupDRStub (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupDRGrpc.BackupDRStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BackupDRGrpc.BackupDRStub (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class BackupDRGrpc.BackupDRStub extends AbstractAsyncStub<BackupDRGrpc.BackupDRStub>

A stub to allow clients to do asynchronous rpc calls to service BackupDR.

The BackupDR Service

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > BackupDRGrpc.BackupDRStub

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
    
    
    protected BackupDRGrpc.BackupDRStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRGrpc.BackupDRStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupDRGrpc.BackupDRStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createAutoProtectionPolicy(CreateAutoProtectionPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createAutoProtectionPolicy(CreateAutoProtectionPolicyRequest request, StreamObserver<Operation> responseObserver)

Creates a new AutoProtectionPolicy in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAutoProtectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.CreateAutoProtectionPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createAutoProtectionPolicyBinding(CreateAutoProtectionPolicyBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createAutoProtectionPolicyBinding(CreateAutoProtectionPolicyBindingRequest request, StreamObserver<Operation> responseObserver)

Creates a new AutoProtectionPolicyBinding in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.CreateAutoProtectionPolicyBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createBackupPlan(CreateBackupPlanRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createBackupPlan(CreateBackupPlanRequest request, StreamObserver<Operation> responseObserver)

Create a BackupPlan

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.CreateBackupPlanRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createBackupPlanAssociation(CreateBackupPlanAssociationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createBackupPlanAssociation(CreateBackupPlanAssociationRequest request, StreamObserver<Operation> responseObserver)

Create a BackupPlanAssociation

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.CreateBackupPlanAssociationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createBackupVault(CreateBackupVaultRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createBackupVault(CreateBackupVaultRequest request, StreamObserver<Operation> responseObserver)

Creates a new BackupVault in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.CreateBackupVaultRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createManagementServer(CreateManagementServerRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createManagementServer(CreateManagementServerRequest request, StreamObserver<Operation> responseObserver)

Creates a new ManagementServer in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateManagementServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.CreateManagementServerRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteAutoProtectionPolicy(DeleteAutoProtectionPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteAutoProtectionPolicy(DeleteAutoProtectionPolicyRequest request, StreamObserver<Operation> responseObserver)

Deletes a single AutoProtectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAutoProtectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DeleteAutoProtectionPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteBackup(DeleteBackupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteBackup(DeleteBackupRequest request, StreamObserver<Operation> responseObserver)

Deletes a Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DeleteBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteBackupPlan(DeleteBackupPlanRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteBackupPlan(DeleteBackupPlanRequest request, StreamObserver<Operation> responseObserver)

Deletes a single BackupPlan.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DeleteBackupPlanRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteBackupPlanAssociation(DeleteBackupPlanAssociationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteBackupPlanAssociation(DeleteBackupPlanAssociationRequest request, StreamObserver<Operation> responseObserver)

Deletes a single BackupPlanAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DeleteBackupPlanAssociationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteBackupVault(DeleteBackupVaultRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteBackupVault(DeleteBackupVaultRequest request, StreamObserver<Operation> responseObserver)

Deletes a BackupVault.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DeleteBackupVaultRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteManagementServer(DeleteManagementServerRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteManagementServer(DeleteManagementServerRequest request, StreamObserver<Operation> responseObserver)

Deletes a single ManagementServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteManagementServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DeleteManagementServerRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### fetchBackupPlanAssociationsForResourceType(FetchBackupPlanAssociationsForResourceTypeRequest request, StreamObserver<FetchBackupPlanAssociationsForResourceTypeResponse> responseObserver)
    
    
    public void fetchBackupPlanAssociationsForResourceType(FetchBackupPlanAssociationsForResourceTypeRequest request, StreamObserver<FetchBackupPlanAssociationsForResourceTypeResponse> responseObserver)

List BackupPlanAssociations for a given resource type.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchBackupPlanAssociationsForResourceTypeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchBackupPlanAssociationsForResourceTypeResponse)>`  
  
  
### fetchBackupsForResourceType(FetchBackupsForResourceTypeRequest request, StreamObserver<FetchBackupsForResourceTypeResponse> responseObserver)
    
    
    public void fetchBackupsForResourceType(FetchBackupsForResourceTypeRequest request, StreamObserver<FetchBackupsForResourceTypeResponse> responseObserver)

Fetch Backups for a given resource type.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchBackupsForResourceTypeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchBackupsForResourceTypeResponse)>`  
  
  
### fetchDataSourceReferencesForResourceType(FetchDataSourceReferencesForResourceTypeRequest request, StreamObserver<FetchDataSourceReferencesForResourceTypeResponse> responseObserver)
    
    
    public void fetchDataSourceReferencesForResourceType(FetchDataSourceReferencesForResourceTypeRequest request, StreamObserver<FetchDataSourceReferencesForResourceTypeResponse> responseObserver)

Fetch DataSourceReferences for a given project, location and resource type.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchDataSourceReferencesForResourceTypeRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchDataSourceReferencesForResourceTypeResponse)>`  
  
  
### fetchUsableBackupVaults(FetchUsableBackupVaultsRequest request, StreamObserver<FetchUsableBackupVaultsResponse> responseObserver)
    
    
    public void fetchUsableBackupVaults(FetchUsableBackupVaultsRequest request, StreamObserver<FetchUsableBackupVaultsResponse> responseObserver)

FetchUsableBackupVaults lists usable BackupVaults in a given project and location. Usable BackupVault are the ones that user has backupdr.backupVaults.get permission.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchUsableBackupVaultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchUsableBackupVaultsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchUsableBackupVaultsResponse)>`  
  
  
### getAutoProtectionPolicy(GetAutoProtectionPolicyRequest request, StreamObserver<AutoProtectionPolicy> responseObserver)
    
    
    public void getAutoProtectionPolicy(GetAutoProtectionPolicyRequest request, StreamObserver<AutoProtectionPolicy> responseObserver)

Gets details of a single AutoProtectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutoProtectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetAutoProtectionPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AutoProtectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.AutoProtectionPolicy)>`  
  
  
### getAutoProtectionPolicyBinding(GetAutoProtectionPolicyBindingRequest request, StreamObserver<AutoProtectionPolicyBinding> responseObserver)
    
    
    public void getAutoProtectionPolicyBinding(GetAutoProtectionPolicyBindingRequest request, StreamObserver<AutoProtectionPolicyBinding> responseObserver)

Returns the auto protection policy binding read from the CCFE tables.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetAutoProtectionPolicyBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AutoProtectionPolicyBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.AutoProtectionPolicyBinding)>`  
  
  
### getBackup(GetBackupRequest request, StreamObserver<Backup> responseObserver)
    
    
    public void getBackup(GetBackupRequest request, StreamObserver<Backup> responseObserver)

Gets details of a Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.Backup)>`  
  
  
### getBackupPlan(GetBackupPlanRequest request, StreamObserver<BackupPlan> responseObserver)
    
    
    public void getBackupPlan(GetBackupPlanRequest request, StreamObserver<BackupPlan> responseObserver)

Gets details of a single BackupPlan.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetBackupPlanRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupPlan)>`  
  
  
### getBackupPlanAssociation(GetBackupPlanAssociationRequest request, StreamObserver<BackupPlanAssociation> responseObserver)
    
    
    public void getBackupPlanAssociation(GetBackupPlanAssociationRequest request, StreamObserver<BackupPlanAssociation> responseObserver)

Gets details of a single BackupPlanAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetBackupPlanAssociationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupPlanAssociation)>`  
  
  
### getBackupPlanRevision(GetBackupPlanRevisionRequest request, StreamObserver<BackupPlanRevision> responseObserver)
    
    
    public void getBackupPlanRevision(GetBackupPlanRevisionRequest request, StreamObserver<BackupPlanRevision> responseObserver)

Gets details of a single BackupPlanRevision.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupPlanRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetBackupPlanRevisionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BackupPlanRevision](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupPlanRevision)>`  
  
  
### getBackupVault(GetBackupVaultRequest request, StreamObserver<BackupVault> responseObserver)
    
    
    public void getBackupVault(GetBackupVaultRequest request, StreamObserver<BackupVault> responseObserver)

Gets details of a BackupVault.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetBackupVaultRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupVault)>`  
  
  
### getBindingMatchingResource(GetBindingMatchingResourceRequest request, StreamObserver<BindingMatchingResource> responseObserver)
    
    
    public void getBindingMatchingResource(GetBindingMatchingResourceRequest request, StreamObserver<BindingMatchingResource> responseObserver)

Gets details of a single Binding Matching Resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBindingMatchingResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetBindingMatchingResourceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BindingMatchingResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BindingMatchingResource)>`  
  
  
### getDataSource(GetDataSourceRequest request, StreamObserver<DataSource> responseObserver)
    
    
    public void getDataSource(GetDataSourceRequest request, StreamObserver<DataSource> responseObserver)

Gets details of a DataSource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetDataSourceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DataSource)>`  
  
  
### getDataSourceReference(GetDataSourceReferenceRequest request, StreamObserver<DataSourceReference> responseObserver)
    
    
    public void getDataSourceReference(GetDataSourceReferenceRequest request, StreamObserver<DataSourceReference> responseObserver)

Gets details of a single DataSourceReference.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDataSourceReferenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetDataSourceReferenceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DataSourceReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DataSourceReference)>`  
  
  
### getManagementServer(GetManagementServerRequest request, StreamObserver<ManagementServer> responseObserver)
    
    
    public void getManagementServer(GetManagementServerRequest request, StreamObserver<ManagementServer> responseObserver)

Gets details of a single ManagementServer.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetManagementServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetManagementServerRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ManagementServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ManagementServer)>`  
  
  
### initializeService(InitializeServiceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void initializeService(InitializeServiceRequest request, StreamObserver<Operation> responseObserver)

Initializes the service related config for a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InitializeServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.InitializeServiceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### initiateDeleteAutoProtectionPolicyBinding(InitiateDeleteAutoProtectionPolicyBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void initiateDeleteAutoProtectionPolicyBinding(InitiateDeleteAutoProtectionPolicyBindingRequest request, StreamObserver<Operation> responseObserver)

InitiateDeleteAutoProtectionPolicyBinding initiates delete for AutoProtectionPolicy Binding

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InitiateDeleteAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.InitiateDeleteAutoProtectionPolicyBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### listAppliedAutoProtectionPolicies(ListAppliedAutoProtectionPoliciesRequest request, StreamObserver<ListAppliedAutoProtectionPoliciesResponse> responseObserver)
    
    
    public void listAppliedAutoProtectionPolicies(ListAppliedAutoProtectionPoliciesRequest request, StreamObserver<ListAppliedAutoProtectionPoliciesResponse> responseObserver)

Lists AppliedAutoProtectionPolicies in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAppliedAutoProtectionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListAppliedAutoProtectionPoliciesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAppliedAutoProtectionPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListAppliedAutoProtectionPoliciesResponse)>`  
  
  
### listAutoProtectionPolicies(ListAutoProtectionPoliciesRequest request, StreamObserver<ListAutoProtectionPoliciesResponse> responseObserver)
    
    
    public void listAutoProtectionPolicies(ListAutoProtectionPoliciesRequest request, StreamObserver<ListAutoProtectionPoliciesResponse> responseObserver)

Lists AutoProtectionPolicies for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutoProtectionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListAutoProtectionPoliciesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAutoProtectionPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListAutoProtectionPoliciesResponse)>`  
  
  
### listAutoProtectionPolicyBindings(ListAutoProtectionPolicyBindingsRequest request, StreamObserver<ListAutoProtectionPolicyBindingsResponse> responseObserver)
    
    
    public void listAutoProtectionPolicyBindings(ListAutoProtectionPolicyBindingsRequest request, StreamObserver<ListAutoProtectionPolicyBindingsResponse> responseObserver)

Returns the auto protection policy bindings read from the CCFE tables.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAutoProtectionPolicyBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListAutoProtectionPolicyBindingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAutoProtectionPolicyBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListAutoProtectionPolicyBindingsResponse)>`  
  
  
### listBackupPlanAssociations(ListBackupPlanAssociationsRequest request, StreamObserver<ListBackupPlanAssociationsResponse> responseObserver)
    
    
    public void listBackupPlanAssociations(ListBackupPlanAssociationsRequest request, StreamObserver<ListBackupPlanAssociationsResponse> responseObserver)

Lists BackupPlanAssociations in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupPlanAssociationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupPlanAssociationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupPlanAssociationsResponse)>`  
  
  
### listBackupPlanRevisions(ListBackupPlanRevisionsRequest request, StreamObserver<ListBackupPlanRevisionsResponse> responseObserver)
    
    
    public void listBackupPlanRevisions(ListBackupPlanRevisionsRequest request, StreamObserver<ListBackupPlanRevisionsResponse> responseObserver)

Lists BackupPlanRevisions in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupPlanRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupPlanRevisionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupPlanRevisionsResponse)>`  
  
  
### listBackupPlans(ListBackupPlansRequest request, StreamObserver<ListBackupPlansResponse> responseObserver)
    
    
    public void listBackupPlans(ListBackupPlansRequest request, StreamObserver<ListBackupPlansResponse> responseObserver)

Lists BackupPlans in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupPlansRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupPlansRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBackupPlansResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupPlansResponse)>`  
  
  
### listBackupVaults(ListBackupVaultsRequest request, StreamObserver<ListBackupVaultsResponse> responseObserver)
    
    
    public void listBackupVaults(ListBackupVaultsRequest request, StreamObserver<ListBackupVaultsResponse> responseObserver)

Lists BackupVaults in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupVaultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupVaultsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBackupVaultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupVaultsResponse)>`  
  
  
### listBackups(ListBackupsRequest request, StreamObserver<ListBackupsResponse> responseObserver)
    
    
    public void listBackups(ListBackupsRequest request, StreamObserver<ListBackupsResponse> responseObserver)

Lists Backups in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupsResponse)>`  
  
  
### listBindingMatchingResources(ListBindingMatchingResourcesRequest request, StreamObserver<ListBindingMatchingResourcesResponse> responseObserver)
    
    
    public void listBindingMatchingResources(ListBindingMatchingResourcesRequest request, StreamObserver<ListBindingMatchingResourcesResponse> responseObserver)

Lists Binding Matching Resources for a given AutoProtectionPolicyBinding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBindingMatchingResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBindingMatchingResourcesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBindingMatchingResourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBindingMatchingResourcesResponse)>`  
  
  
### listDataSourceReferences(ListDataSourceReferencesRequest request, StreamObserver<ListDataSourceReferencesResponse> responseObserver)
    
    
    public void listDataSourceReferences(ListDataSourceReferencesRequest request, StreamObserver<ListDataSourceReferencesResponse> responseObserver)

Lists DataSourceReferences for a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataSourceReferencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListDataSourceReferencesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListDataSourceReferencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListDataSourceReferencesResponse)>`  
  
  
### listDataSources(ListDataSourcesRequest request, StreamObserver<ListDataSourcesResponse> responseObserver)
    
    
    public void listDataSources(ListDataSourcesRequest request, StreamObserver<ListDataSourcesResponse> responseObserver)

Lists DataSources in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListDataSourcesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListDataSourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListDataSourcesResponse)>`  
  
  
### listManagementServers(ListManagementServersRequest request, StreamObserver<ListManagementServersResponse> responseObserver)
    
    
    public void listManagementServers(ListManagementServersRequest request, StreamObserver<ListManagementServersResponse> responseObserver)

Lists ManagementServers in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListManagementServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListManagementServersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListManagementServersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListManagementServersResponse)>`  
  
  
### restoreBackup(RestoreBackupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void restoreBackup(RestoreBackupRequest request, StreamObserver<Operation> responseObserver)

Restore from a Backup

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.RestoreBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### triggerBackup(TriggerBackupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void triggerBackup(TriggerBackupRequest request, StreamObserver<Operation> responseObserver)

Triggers a new Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TriggerBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.TriggerBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateAutoProtectionPolicy(UpdateAutoProtectionPolicyRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateAutoProtectionPolicy(UpdateAutoProtectionPolicyRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single AutoProtectionPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAutoProtectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.UpdateAutoProtectionPolicyRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateBackup(UpdateBackupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateBackup(UpdateBackupRequest request, StreamObserver<Operation> responseObserver)

Updates the settings of a Backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.UpdateBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateBackupPlan(UpdateBackupPlanRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateBackupPlan(UpdateBackupPlanRequest request, StreamObserver<Operation> responseObserver)

Update a BackupPlan.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.UpdateBackupPlanRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateBackupPlanAssociation(UpdateBackupPlanAssociationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateBackupPlanAssociation(UpdateBackupPlanAssociationRequest request, StreamObserver<Operation> responseObserver)

Update a BackupPlanAssociation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.UpdateBackupPlanAssociationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateBackupVault(UpdateBackupVaultRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateBackupVault(UpdateBackupVaultRequest request, StreamObserver<Operation> responseObserver)

Updates the settings of a BackupVault.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.UpdateBackupVaultRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateDataSource(UpdateDataSourceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateDataSource(UpdateDataSourceRequest request, StreamObserver<Operation> responseObserver)

Updates the settings of a DataSource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.UpdateDataSourceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
