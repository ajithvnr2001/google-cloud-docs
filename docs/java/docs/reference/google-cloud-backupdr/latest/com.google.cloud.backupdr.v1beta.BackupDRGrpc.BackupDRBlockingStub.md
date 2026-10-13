---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupDRGrpc.BackupDRBlockingStub
title: Class BackupDRGrpc.BackupDRBlockingStub (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:06:57.226577+00:00
---

# Class BackupDRGrpc.BackupDRBlockingStub (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupDRGrpc.BackupDRBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BackupDRGrpc.BackupDRBlockingStub (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class BackupDRGrpc.BackupDRBlockingStub extends AbstractBlockingStub<BackupDRGrpc.BackupDRBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service BackupDR.

The BackupDR Service

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > BackupDRGrpc.BackupDRBlockingStub

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
    
    
    protected BackupDRGrpc.BackupDRBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupDRGrpc.BackupDRBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupDRGrpc.BackupDRBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createAutoProtectionPolicy(CreateAutoProtectionPolicyRequest request)
    
    
    public Operation createAutoProtectionPolicy(CreateAutoProtectionPolicyRequest request)

Creates a new AutoProtectionPolicy in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAutoProtectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.CreateAutoProtectionPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createAutoProtectionPolicyBinding(CreateAutoProtectionPolicyBindingRequest request)
    
    
    public Operation createAutoProtectionPolicyBinding(CreateAutoProtectionPolicyBindingRequest request)

Creates a new AutoProtectionPolicyBinding in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.CreateAutoProtectionPolicyBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createBackupPlan(CreateBackupPlanRequest request)
    
    
    public Operation createBackupPlan(CreateBackupPlanRequest request)

Create a BackupPlan

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.CreateBackupPlanRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createBackupPlanAssociation(CreateBackupPlanAssociationRequest request)
    
    
    public Operation createBackupPlanAssociation(CreateBackupPlanAssociationRequest request)

Create a BackupPlanAssociation

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.CreateBackupPlanAssociationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createBackupVault(CreateBackupVaultRequest request)
    
    
    public Operation createBackupVault(CreateBackupVaultRequest request)

Creates a new BackupVault in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.CreateBackupVaultRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createManagementServer(CreateManagementServerRequest request)
    
    
    public Operation createManagementServer(CreateManagementServerRequest request)

Creates a new ManagementServer in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateManagementServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.CreateManagementServerRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteAutoProtectionPolicy(DeleteAutoProtectionPolicyRequest request)
    
    
    public Operation deleteAutoProtectionPolicy(DeleteAutoProtectionPolicyRequest request)

Deletes a single AutoProtectionPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAutoProtectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DeleteAutoProtectionPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteBackup(DeleteBackupRequest request)
    
    
    public Operation deleteBackup(DeleteBackupRequest request)

Deletes a Backup.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DeleteBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteBackupPlan(DeleteBackupPlanRequest request)
    
    
    public Operation deleteBackupPlan(DeleteBackupPlanRequest request)

Deletes a single BackupPlan.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DeleteBackupPlanRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteBackupPlanAssociation(DeleteBackupPlanAssociationRequest request)
    
    
    public Operation deleteBackupPlanAssociation(DeleteBackupPlanAssociationRequest request)

Deletes a single BackupPlanAssociation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DeleteBackupPlanAssociationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteBackupVault(DeleteBackupVaultRequest request)
    
    
    public Operation deleteBackupVault(DeleteBackupVaultRequest request)

Deletes a BackupVault.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DeleteBackupVaultRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteManagementServer(DeleteManagementServerRequest request)
    
    
    public Operation deleteManagementServer(DeleteManagementServerRequest request)

Deletes a single ManagementServer.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteManagementServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DeleteManagementServerRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### fetchBackupPlanAssociationsForResourceType(FetchBackupPlanAssociationsForResourceTypeRequest request)
    
    
    public FetchBackupPlanAssociationsForResourceTypeResponse fetchBackupPlanAssociationsForResourceType(FetchBackupPlanAssociationsForResourceTypeRequest request)

List BackupPlanAssociations for a given resource type.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchBackupPlanAssociationsForResourceTypeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchBackupPlanAssociationsForResourceTypeResponse)` |   
  
### fetchBackupsForResourceType(FetchBackupsForResourceTypeRequest request)
    
    
    public FetchBackupsForResourceTypeResponse fetchBackupsForResourceType(FetchBackupsForResourceTypeRequest request)

Fetch Backups for a given resource type.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchBackupsForResourceTypeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchBackupsForResourceTypeResponse)` |   
  
### fetchDataSourceReferencesForResourceType(FetchDataSourceReferencesForResourceTypeRequest request)
    
    
    public FetchDataSourceReferencesForResourceTypeResponse fetchDataSourceReferencesForResourceType(FetchDataSourceReferencesForResourceTypeRequest request)

Fetch DataSourceReferences for a given project, location and resource type.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchDataSourceReferencesForResourceTypeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchDataSourceReferencesForResourceTypeResponse)` |   
  
### fetchUsableBackupVaults(FetchUsableBackupVaultsRequest request)
    
    
    public FetchUsableBackupVaultsResponse fetchUsableBackupVaults(FetchUsableBackupVaultsRequest request)

FetchUsableBackupVaults lists usable BackupVaults in a given project and location. Usable BackupVault are the ones that user has backupdr.backupVaults.get permission.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchUsableBackupVaultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchUsableBackupVaultsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.FetchUsableBackupVaultsResponse)` |   
  
### getAutoProtectionPolicy(GetAutoProtectionPolicyRequest request)
    
    
    public AutoProtectionPolicy getAutoProtectionPolicy(GetAutoProtectionPolicyRequest request)

Gets details of a single AutoProtectionPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAutoProtectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetAutoProtectionPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutoProtectionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.AutoProtectionPolicy)` |   
  
### getAutoProtectionPolicyBinding(GetAutoProtectionPolicyBindingRequest request)
    
    
    public AutoProtectionPolicyBinding getAutoProtectionPolicyBinding(GetAutoProtectionPolicyBindingRequest request)

Returns the auto protection policy binding read from the CCFE tables.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetAutoProtectionPolicyBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutoProtectionPolicyBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.AutoProtectionPolicyBinding)` |   
  
### getBackup(GetBackupRequest request)
    
    
    public Backup getBackup(GetBackupRequest request)

Gets details of a Backup.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.Backup)` |   
  
### getBackupPlan(GetBackupPlanRequest request)
    
    
    public BackupPlan getBackupPlan(GetBackupPlanRequest request)

Gets details of a single BackupPlan.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetBackupPlanRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupPlan)` |   
  
### getBackupPlanAssociation(GetBackupPlanAssociationRequest request)
    
    
    public BackupPlanAssociation getBackupPlanAssociation(GetBackupPlanAssociationRequest request)

Gets details of a single BackupPlanAssociation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetBackupPlanAssociationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlanAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupPlanAssociation)` |   
  
### getBackupPlanRevision(GetBackupPlanRevisionRequest request)
    
    
    public BackupPlanRevision getBackupPlanRevision(GetBackupPlanRevisionRequest request)

Gets details of a single BackupPlanRevision.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupPlanRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetBackupPlanRevisionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupPlanRevision](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupPlanRevision)` |   
  
### getBackupVault(GetBackupVaultRequest request)
    
    
    public BackupVault getBackupVault(GetBackupVaultRequest request)

Gets details of a BackupVault.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetBackupVaultRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupVault](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BackupVault)` |   
  
### getBindingMatchingResource(GetBindingMatchingResourceRequest request)
    
    
    public BindingMatchingResource getBindingMatchingResource(GetBindingMatchingResourceRequest request)

Gets details of a single Binding Matching Resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBindingMatchingResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetBindingMatchingResourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BindingMatchingResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.BindingMatchingResource)` |   
  
### getDataSource(GetDataSourceRequest request)
    
    
    public DataSource getDataSource(GetDataSourceRequest request)

Gets details of a DataSource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetDataSourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DataSource)` |   
  
### getDataSourceReference(GetDataSourceReferenceRequest request)
    
    
    public DataSourceReference getDataSourceReference(GetDataSourceReferenceRequest request)

Gets details of a single DataSourceReference.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataSourceReferenceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetDataSourceReferenceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataSourceReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.DataSourceReference)` |   
  
### getManagementServer(GetManagementServerRequest request)
    
    
    public ManagementServer getManagementServer(GetManagementServerRequest request)

Gets details of a single ManagementServer.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetManagementServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.GetManagementServerRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ManagementServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ManagementServer)` |   
  
### initializeService(InitializeServiceRequest request)
    
    
    public Operation initializeService(InitializeServiceRequest request)

Initializes the service related config for a project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InitializeServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.InitializeServiceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### initiateDeleteAutoProtectionPolicyBinding(InitiateDeleteAutoProtectionPolicyBindingRequest request)
    
    
    public Operation initiateDeleteAutoProtectionPolicyBinding(InitiateDeleteAutoProtectionPolicyBindingRequest request)

InitiateDeleteAutoProtectionPolicyBinding initiates delete for AutoProtectionPolicy Binding

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InitiateDeleteAutoProtectionPolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.InitiateDeleteAutoProtectionPolicyBindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### listAppliedAutoProtectionPolicies(ListAppliedAutoProtectionPoliciesRequest request)
    
    
    public ListAppliedAutoProtectionPoliciesResponse listAppliedAutoProtectionPolicies(ListAppliedAutoProtectionPoliciesRequest request)

Lists AppliedAutoProtectionPolicies in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAppliedAutoProtectionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListAppliedAutoProtectionPoliciesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListAppliedAutoProtectionPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListAppliedAutoProtectionPoliciesResponse)` |   
  
### listAutoProtectionPolicies(ListAutoProtectionPoliciesRequest request)
    
    
    public ListAutoProtectionPoliciesResponse listAutoProtectionPolicies(ListAutoProtectionPoliciesRequest request)

Lists AutoProtectionPolicies for a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAutoProtectionPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListAutoProtectionPoliciesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListAutoProtectionPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListAutoProtectionPoliciesResponse)` |   
  
### listAutoProtectionPolicyBindings(ListAutoProtectionPolicyBindingsRequest request)
    
    
    public ListAutoProtectionPolicyBindingsResponse listAutoProtectionPolicyBindings(ListAutoProtectionPolicyBindingsRequest request)

Returns the auto protection policy bindings read from the CCFE tables.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAutoProtectionPolicyBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListAutoProtectionPolicyBindingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListAutoProtectionPolicyBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListAutoProtectionPolicyBindingsResponse)` |   
  
### listBackupPlanAssociations(ListBackupPlanAssociationsRequest request)
    
    
    public ListBackupPlanAssociationsResponse listBackupPlanAssociations(ListBackupPlanAssociationsRequest request)

Lists BackupPlanAssociations in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupPlanAssociationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupPlanAssociationsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupPlanAssociationsResponse)` |   
  
### listBackupPlanRevisions(ListBackupPlanRevisionsRequest request)
    
    
    public ListBackupPlanRevisionsResponse listBackupPlanRevisions(ListBackupPlanRevisionsRequest request)

Lists BackupPlanRevisions in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupPlanRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupPlanRevisionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupPlanRevisionsResponse)` |   
  
### listBackupPlans(ListBackupPlansRequest request)
    
    
    public ListBackupPlansResponse listBackupPlans(ListBackupPlansRequest request)

Lists BackupPlans in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupPlansRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupPlansRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupPlansResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupPlansResponse)` |   
  
### listBackupVaults(ListBackupVaultsRequest request)
    
    
    public ListBackupVaultsResponse listBackupVaults(ListBackupVaultsRequest request)

Lists BackupVaults in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupVaultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupVaultsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupVaultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupVaultsResponse)` |   
  
### listBackups(ListBackupsRequest request)
    
    
    public ListBackupsResponse listBackups(ListBackupsRequest request)

Lists Backups in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBackupsResponse)` |   
  
### listBindingMatchingResources(ListBindingMatchingResourcesRequest request)
    
    
    public ListBindingMatchingResourcesResponse listBindingMatchingResources(ListBindingMatchingResourcesRequest request)

Lists Binding Matching Resources for a given AutoProtectionPolicyBinding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBindingMatchingResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBindingMatchingResourcesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListBindingMatchingResourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListBindingMatchingResourcesResponse)` |   
  
### listDataSourceReferences(ListDataSourceReferencesRequest request)
    
    
    public ListDataSourceReferencesResponse listDataSourceReferences(ListDataSourceReferencesRequest request)

Lists DataSourceReferences for a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataSourceReferencesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListDataSourceReferencesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListDataSourceReferencesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListDataSourceReferencesResponse)` |   
  
### listDataSources(ListDataSourcesRequest request)
    
    
    public ListDataSourcesResponse listDataSources(ListDataSourcesRequest request)

Lists DataSources in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListDataSourcesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListDataSourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListDataSourcesResponse)` |   
  
### listManagementServers(ListManagementServersRequest request)
    
    
    public ListManagementServersResponse listManagementServers(ListManagementServersRequest request)

Lists ManagementServers in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListManagementServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListManagementServersRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListManagementServersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.ListManagementServersResponse)` |   
  
### restoreBackup(RestoreBackupRequest request)
    
    
    public Operation restoreBackup(RestoreBackupRequest request)

Restore from a Backup

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestoreBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.RestoreBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### triggerBackup(TriggerBackupRequest request)
    
    
    public Operation triggerBackup(TriggerBackupRequest request)

Triggers a new Backup.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TriggerBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.TriggerBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateAutoProtectionPolicy(UpdateAutoProtectionPolicyRequest request)
    
    
    public Operation updateAutoProtectionPolicy(UpdateAutoProtectionPolicyRequest request)

Updates the parameters of a single AutoProtectionPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAutoProtectionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.UpdateAutoProtectionPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateBackup(UpdateBackupRequest request)
    
    
    public Operation updateBackup(UpdateBackupRequest request)

Updates the settings of a Backup.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.UpdateBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateBackupPlan(UpdateBackupPlanRequest request)
    
    
    public Operation updateBackupPlan(UpdateBackupPlanRequest request)

Update a BackupPlan.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.UpdateBackupPlanRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateBackupPlanAssociation(UpdateBackupPlanAssociationRequest request)
    
    
    public Operation updateBackupPlanAssociation(UpdateBackupPlanAssociationRequest request)

Update a BackupPlanAssociation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.UpdateBackupPlanAssociationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateBackupVault(UpdateBackupVaultRequest request)
    
    
    public Operation updateBackupVault(UpdateBackupVaultRequest request)

Updates the settings of a BackupVault.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupVaultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.UpdateBackupVaultRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateDataSource(UpdateDataSourceRequest request)
    
    
    public Operation updateDataSource(UpdateDataSourceRequest request)

Updates the settings of a DataSource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDataSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1beta.UpdateDataSourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
