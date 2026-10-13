---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreGrpc.MemorystoreFutureStub
title: Class MemorystoreGrpc.MemorystoreFutureStub (0.45.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:50:03.790514+00:00
---

# Class MemorystoreGrpc.MemorystoreFutureStub (0.45.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreGrpc.MemorystoreFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MemorystoreGrpc.MemorystoreFutureStub (0.45.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.45.0 (latest)  0.41.0  0.40.0  0.39.0  0.37.0  0.34.0  0.33.0  0.31.0  0.29.0  0.28.0  0.26.0  0.24.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class MemorystoreGrpc.MemorystoreFutureStub extends AbstractFutureStub<MemorystoreGrpc.MemorystoreFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service Memorystore.

Service describing handlers for resources

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > MemorystoreGrpc.MemorystoreFutureStub

## Inherited Members

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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

### addAuthToken(AddAuthTokenRequest request)
    
    
    public ListenableFuture<Operation> addAuthToken(AddAuthTokenRequest request)

Adds a token for a user of a token based auth enabled instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddAuthTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AddAuthTokenRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### addTokenAuthUser(AddTokenAuthUserRequest request)
    
    
    public ListenableFuture<Operation> addTokenAuthUser(AddTokenAuthUserRequest request)

Adds a token auth user for a token based auth enabled instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddTokenAuthUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AddTokenAuthUserRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### backupInstance(BackupInstanceRequest request)
    
    
    public ListenableFuture<Operation> backupInstance(BackupInstanceRequest request)

Backup Instance. If this is the first time a backup is being created, a backup collection will be created at the backend, and this backup belongs to this collection. Both collection and backup will have a resource name. Backup will be executed for each shard. A replica (primary if nonHA) will be selected to perform the execution. Backup call will be rejected if there is an ongoing backup or update operation. Be aware that during preview, if the instance's internal software version is too old, critical update will be performed before actual backup. Once the internal software version is updated to the minimum version required by the backup feature, subsequent backups will not require critical update. After preview, there will be no critical update needed for backup.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BackupInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.BackupInstanceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected MemorystoreGrpc.MemorystoreFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreGrpc.MemorystoreFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreGrpc.MemorystoreFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createInstance(CreateInstanceRequest request)
    
    
    public ListenableFuture<Operation> createInstance(CreateInstanceRequest request)

Creates a new Instance in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CreateInstanceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAuthToken(DeleteAuthTokenRequest request)
    
    
    public ListenableFuture<Operation> deleteAuthToken(DeleteAuthTokenRequest request)

Deletes a token for a user of a token based auth enabled instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteAuthTokenRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteBackup(DeleteBackupRequest request)
    
    
    public ListenableFuture<Operation> deleteBackup(DeleteBackupRequest request)

Deletes a specific backup.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteInstance(DeleteInstanceRequest request)
    
    
    public ListenableFuture<Operation> deleteInstance(DeleteInstanceRequest request)

Deletes a single Instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteInstanceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTokenAuthUser(DeleteTokenAuthUserRequest request)
    
    
    public ListenableFuture<Operation> deleteTokenAuthUser(DeleteTokenAuthUserRequest request)

Deletes a token auth user for a token based auth enabled instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTokenAuthUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteTokenAuthUserRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportBackup(ExportBackupRequest request)
    
    
    public ListenableFuture<Operation> exportBackup(ExportBackupRequest request)

Exports a specific backup to a customer target Cloud Storage URI.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ExportBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### finishMigration(FinishMigrationRequest request)
    
    
    public ListenableFuture<Operation> finishMigration(FinishMigrationRequest request)

Finalizes the migration process. After the successful completion of this operation, the target instance will:

  1. Stop replicating from the source instance.
  2. Allow both reads and writes.



**Parameter**  
---  
**Name** | **Description**  
`request` | `[FinishMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.FinishMigrationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getAuthToken(GetAuthTokenRequest request)
    
    
    public ListenableFuture<AuthToken> getAuthToken(GetAuthTokenRequest request)

Gets a token based auth enabled instance's auth token for a given user.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAuthTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetAuthTokenRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AuthToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AuthToken)>` |   
  
### getBackup(GetBackupRequest request)
    
    
    public ListenableFuture<Backup> getBackup(GetBackupRequest request)

Gets the details of a specific backup.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Backup)>` |   
  
### getBackupCollection(GetBackupCollectionRequest request)
    
    
    public ListenableFuture<BackupCollection> getBackupCollection(GetBackupCollectionRequest request)

Get a backup collection.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupCollectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetBackupCollectionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[BackupCollection](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.BackupCollection)>` |   
  
### getCertificateAuthority(GetCertificateAuthorityRequest request)
    
    
    public ListenableFuture<CertificateAuthority> getCertificateAuthority(GetCertificateAuthorityRequest request)

Gets details about the certificate authority for an Instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetCertificateAuthorityRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CertificateAuthority)>` |   
  
### getInstance(GetInstanceRequest request)
    
    
    public ListenableFuture<Instance> getInstance(GetInstanceRequest request)

Gets details of a single Instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetInstanceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance)>` |   
  
### getSharedRegionalCertificateAuthority(GetSharedRegionalCertificateAuthorityRequest request)
    
    
    public ListenableFuture<SharedRegionalCertificateAuthority> getSharedRegionalCertificateAuthority(GetSharedRegionalCertificateAuthorityRequest request)

Gets the details of shared regional certificate authority information for Memorystore instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetSharedRegionalCertificateAuthorityRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.SharedRegionalCertificateAuthority)>` |   
  
### getTokenAuthUser(GetTokenAuthUserRequest request)
    
    
    public ListenableFuture<TokenAuthUser> getTokenAuthUser(GetTokenAuthUserRequest request)

Gets a specific token auth user for a token based auth enabled instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTokenAuthUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetTokenAuthUserRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[TokenAuthUser](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.TokenAuthUser)>` |   
  
### listAuthTokens(ListAuthTokensRequest request)
    
    
    public ListenableFuture<ListAuthTokensResponse> listAuthTokens(ListAuthTokensRequest request)

Lists all the auth tokens for a specific token auth user.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAuthTokensRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListAuthTokensRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListAuthTokensResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListAuthTokensResponse)>` |   
  
### listBackupCollections(ListBackupCollectionsRequest request)
    
    
    public ListenableFuture<ListBackupCollectionsResponse> listBackupCollections(ListBackupCollectionsRequest request)

Lists all backup collections owned by a consumer project in either the specified location (region) or all locations. If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupCollectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListBackupCollectionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListBackupCollectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListBackupCollectionsResponse)>` |   
  
### listBackups(ListBackupsRequest request)
    
    
    public ListenableFuture<ListBackupsResponse> listBackups(ListBackupsRequest request)

Lists all backups owned by a backup collection.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListBackupsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListBackupsResponse)>` |   
  
### listInstances(ListInstancesRequest request)
    
    
    public ListenableFuture<ListInstancesResponse> listInstances(ListInstancesRequest request)

Lists Instances in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListInstancesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListInstancesResponse)>` |   
  
### listTokenAuthUsers(ListTokenAuthUsersRequest request)
    
    
    public ListenableFuture<ListTokenAuthUsersResponse> listTokenAuthUsers(ListTokenAuthUsersRequest request)

Lists all the token auth users for a token based auth enabled instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTokenAuthUsersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListTokenAuthUsersRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListTokenAuthUsersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListTokenAuthUsersResponse)>` |   
  
### rescheduleMaintenance(RescheduleMaintenanceRequest request)
    
    
    public ListenableFuture<Operation> rescheduleMaintenance(RescheduleMaintenanceRequest request)

Reschedules upcoming maintenance event.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.RescheduleMaintenanceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### startMigration(StartMigrationRequest request)
    
    
    public ListenableFuture<Operation> startMigration(StartMigrationRequest request)

Initiates the migration of a source instance to the target Memorystore instance. After the successful completion of this operation, the target instance will:

  1. Set up replication with the source instance and replicate any writes to the source instance.
  2. Only allow reads.



**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.StartMigrationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateInstance(UpdateInstanceRequest request)
    
    
    public ListenableFuture<Operation> updateInstance(UpdateInstanceRequest request)

Updates the parameters of a single Instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.UpdateInstanceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
