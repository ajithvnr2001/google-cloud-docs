---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreGrpc.MemorystoreStub
title: Class MemorystoreGrpc.MemorystoreStub (0.45.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:49:28.489802+00:00
---

# Class MemorystoreGrpc.MemorystoreStub (0.45.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreGrpc.MemorystoreStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MemorystoreGrpc.MemorystoreStub (0.45.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.45.0 (latest)  0.41.0  0.40.0  0.39.0  0.37.0  0.34.0  0.33.0  0.31.0  0.29.0  0.28.0  0.26.0  0.24.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class MemorystoreGrpc.MemorystoreStub extends AbstractAsyncStub<MemorystoreGrpc.MemorystoreStub>

A stub to allow clients to do asynchronous rpc calls to service Memorystore.

Service describing handlers for resources

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > MemorystoreGrpc.MemorystoreStub

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

### addAuthToken(AddAuthTokenRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void addAuthToken(AddAuthTokenRequest request, StreamObserver<Operation> responseObserver)

Adds a token for a user of a token based auth enabled instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddAuthTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AddAuthTokenRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### addTokenAuthUser(AddTokenAuthUserRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void addTokenAuthUser(AddTokenAuthUserRequest request, StreamObserver<Operation> responseObserver)

Adds a token auth user for a token based auth enabled instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddTokenAuthUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AddTokenAuthUserRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### backupInstance(BackupInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void backupInstance(BackupInstanceRequest request, StreamObserver<Operation> responseObserver)

Backup Instance. If this is the first time a backup is being created, a backup collection will be created at the backend, and this backup belongs to this collection. Both collection and backup will have a resource name. Backup will be executed for each shard. A replica (primary if nonHA) will be selected to perform the execution. Backup call will be rejected if there is an ongoing backup or update operation. Be aware that during preview, if the instance's internal software version is too old, critical update will be performed before actual backup. Once the internal software version is updated to the minimum version required by the backup feature, subsequent backups will not require critical update. After preview, there will be no critical update needed for backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BackupInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.BackupInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected MemorystoreGrpc.MemorystoreStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreGrpc.MemorystoreStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreGrpc.MemorystoreStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createInstance(CreateInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createInstance(CreateInstanceRequest request, StreamObserver<Operation> responseObserver)

Creates a new Instance in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CreateInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteAuthToken(DeleteAuthTokenRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteAuthToken(DeleteAuthTokenRequest request, StreamObserver<Operation> responseObserver)

Deletes a token for a user of a token based auth enabled instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteAuthTokenRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteBackup(DeleteBackupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteBackup(DeleteBackupRequest request, StreamObserver<Operation> responseObserver)

Deletes a specific backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteInstance(DeleteInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteInstance(DeleteInstanceRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteTokenAuthUser(DeleteTokenAuthUserRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteTokenAuthUser(DeleteTokenAuthUserRequest request, StreamObserver<Operation> responseObserver)

Deletes a token auth user for a token based auth enabled instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTokenAuthUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteTokenAuthUserRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### exportBackup(ExportBackupRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void exportBackup(ExportBackupRequest request, StreamObserver<Operation> responseObserver)

Exports a specific backup to a customer target Cloud Storage URI.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ExportBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### finishMigration(FinishMigrationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void finishMigration(FinishMigrationRequest request, StreamObserver<Operation> responseObserver)

Finalizes the migration process. After the successful completion of this operation, the target instance will:

  1. Stop replicating from the source instance.
  2. Allow both reads and writes.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[FinishMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.FinishMigrationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getAuthToken(GetAuthTokenRequest request, StreamObserver<AuthToken> responseObserver)
    
    
    public void getAuthToken(GetAuthTokenRequest request, StreamObserver<AuthToken> responseObserver)

Gets a token based auth enabled instance's auth token for a given user.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAuthTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetAuthTokenRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AuthToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AuthToken)>`  
  
  
### getBackup(GetBackupRequest request, StreamObserver<Backup> responseObserver)
    
    
    public void getBackup(GetBackupRequest request, StreamObserver<Backup> responseObserver)

Gets the details of a specific backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Backup)>`  
  
  
### getBackupCollection(GetBackupCollectionRequest request, StreamObserver<BackupCollection> responseObserver)
    
    
    public void getBackupCollection(GetBackupCollectionRequest request, StreamObserver<BackupCollection> responseObserver)

Get a backup collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupCollectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetBackupCollectionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BackupCollection](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.BackupCollection)>`  
  
  
### getCertificateAuthority(GetCertificateAuthorityRequest request, StreamObserver<CertificateAuthority> responseObserver)
    
    
    public void getCertificateAuthority(GetCertificateAuthorityRequest request, StreamObserver<CertificateAuthority> responseObserver)

Gets details about the certificate authority for an Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetCertificateAuthorityRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CertificateAuthority)>`  
  
  
### getInstance(GetInstanceRequest request, StreamObserver<Instance> responseObserver)
    
    
    public void getInstance(GetInstanceRequest request, StreamObserver<Instance> responseObserver)

Gets details of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance)>`  
  
  
### getSharedRegionalCertificateAuthority(GetSharedRegionalCertificateAuthorityRequest request, StreamObserver<SharedRegionalCertificateAuthority> responseObserver)
    
    
    public void getSharedRegionalCertificateAuthority(GetSharedRegionalCertificateAuthorityRequest request, StreamObserver<SharedRegionalCertificateAuthority> responseObserver)

Gets the details of shared regional certificate authority information for Memorystore instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetSharedRegionalCertificateAuthorityRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.SharedRegionalCertificateAuthority)>`  
  
  
### getTokenAuthUser(GetTokenAuthUserRequest request, StreamObserver<TokenAuthUser> responseObserver)
    
    
    public void getTokenAuthUser(GetTokenAuthUserRequest request, StreamObserver<TokenAuthUser> responseObserver)

Gets a specific token auth user for a token based auth enabled instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTokenAuthUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetTokenAuthUserRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[TokenAuthUser](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.TokenAuthUser)>`  
  
  
### listAuthTokens(ListAuthTokensRequest request, StreamObserver<ListAuthTokensResponse> responseObserver)
    
    
    public void listAuthTokens(ListAuthTokensRequest request, StreamObserver<ListAuthTokensResponse> responseObserver)

Lists all the auth tokens for a specific token auth user.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAuthTokensRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListAuthTokensRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAuthTokensResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListAuthTokensResponse)>`  
  
  
### listBackupCollections(ListBackupCollectionsRequest request, StreamObserver<ListBackupCollectionsResponse> responseObserver)
    
    
    public void listBackupCollections(ListBackupCollectionsRequest request, StreamObserver<ListBackupCollectionsResponse> responseObserver)

Lists all backup collections owned by a consumer project in either the specified location (region) or all locations. If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupCollectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListBackupCollectionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBackupCollectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListBackupCollectionsResponse)>`  
  
  
### listBackups(ListBackupsRequest request, StreamObserver<ListBackupsResponse> responseObserver)
    
    
    public void listBackups(ListBackupsRequest request, StreamObserver<ListBackupsResponse> responseObserver)

Lists all backups owned by a backup collection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListBackupsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListBackupsResponse)>`  
  
  
### listInstances(ListInstancesRequest request, StreamObserver<ListInstancesResponse> responseObserver)
    
    
    public void listInstances(ListInstancesRequest request, StreamObserver<ListInstancesResponse> responseObserver)

Lists Instances in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListInstancesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListInstancesResponse)>`  
  
  
### listTokenAuthUsers(ListTokenAuthUsersRequest request, StreamObserver<ListTokenAuthUsersResponse> responseObserver)
    
    
    public void listTokenAuthUsers(ListTokenAuthUsersRequest request, StreamObserver<ListTokenAuthUsersResponse> responseObserver)

Lists all the token auth users for a token based auth enabled instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTokenAuthUsersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListTokenAuthUsersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListTokenAuthUsersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListTokenAuthUsersResponse)>`  
  
  
### rescheduleMaintenance(RescheduleMaintenanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void rescheduleMaintenance(RescheduleMaintenanceRequest request, StreamObserver<Operation> responseObserver)

Reschedules upcoming maintenance event.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.RescheduleMaintenanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### startMigration(StartMigrationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void startMigration(StartMigrationRequest request, StreamObserver<Operation> responseObserver)

Initiates the migration of a source instance to the target Memorystore instance. After the successful completion of this operation, the target instance will:

  1. Set up replication with the source instance and replicate any writes to the source instance.
  2. Only allow reads.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[StartMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.StartMigrationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateInstance(UpdateInstanceRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateInstance(UpdateInstanceRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single Instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.UpdateInstanceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
