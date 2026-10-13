---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.FirestoreAdminGrpc.FirestoreAdminStub
title: Class FirestoreAdminGrpc.FirestoreAdminStub (3.49.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:22.098529+00:00
---

# Class FirestoreAdminGrpc.FirestoreAdminStub (3.49.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.FirestoreAdminGrpc.FirestoreAdminStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class FirestoreAdminGrpc.FirestoreAdminStub (3.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.49.0 (latest)  3.45.0  3.44.0  3.43.1  3.41.0  3.38.0  3.37.0  3.36.0  3.35.1  3.33.4  3.32.2  3.31.9  3.30.11  3.28.0  3.27.2  3.26.5  3.25.1  3.24.3  3.22.0  3.21.4  3.20.0  3.17.0  3.16.3  3.15.7  3.14.4  3.13.2  3.12.1  3.11.0  3.10.0  3.9.6  3.8.2  3.7.10  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.1.0  3.0.21 
    
    
    public static final class FirestoreAdminGrpc.FirestoreAdminStub extends AbstractAsyncStub<FirestoreAdminGrpc.FirestoreAdminStub>

A stub to allow clients to do asynchronous rpc calls to service FirestoreAdmin.

The Cloud Firestore Admin API. This API provides several administrative services for Cloud Firestore. Project, Database, Namespace, Collection, Collection Group, and Document are used as defined in the Google Cloud Firestore API. Operation: An Operation represents work being performed in the background. The index service manages Cloud Firestore indexes. Index creation is performed asynchronously. An Operation resource is created for each such asynchronous operation. The state of the operation (including any errors encountered) may be queried via the Operation resource. The Operations collection provides a record of actions performed for the specified Project (including any Operations in progress). Operations are not created directly but through calls on other collections or resources. An Operation that is done may be deleted so that it is no longer listed as part of the Operation collection. Operations are garbage collected after 30 days. By default, ListOperations will only return in progress and failed operations. To list completed operation, issue a ListOperations request with the filter `done: true`. Operations are created by service `FirestoreAdmin`, but are accessed via service `google.longrunning.Operations`.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > FirestoreAdminGrpc.FirestoreAdminStub

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
    
    
    protected FirestoreAdminGrpc.FirestoreAdminStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[FirestoreAdminGrpc.FirestoreAdminStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.FirestoreAdminGrpc.FirestoreAdminStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### bulkDeleteDocuments(BulkDeleteDocumentsRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void bulkDeleteDocuments(BulkDeleteDocumentsRequest request, StreamObserver<Operation> responseObserver)

Bulk deletes a subset of documents from Google Cloud Firestore. Documents created or updated after the underlying system starts to process the request will not be deleted. The bulk delete occurs in the background and its progress can be monitored and managed via the Operation resource that is created. For more details on bulk delete behavior, refer to: <https://cloud.google.com/firestore/docs/manage-data/bulk-delete>

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BulkDeleteDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BulkDeleteDocumentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### cloneDatabase(CloneDatabaseRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void cloneDatabase(CloneDatabaseRequest request, StreamObserver<Operation> responseObserver)

Creates a new database by cloning an existing one. The new database must be in the same cloud region or multi-region location as the existing database. This behaves similar to FirestoreAdmin.CreateDatabase except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing database. The long-running operation can be used to track the progress of the clone, with the Operation's metadata field type being the CloneDatabaseMetadata. The response type is the Database if the clone was successful. The new database is not readable or writeable until the LRO has completed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CloneDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CloneDatabaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createBackupSchedule(CreateBackupScheduleRequest request, StreamObserver<BackupSchedule> responseObserver)
    
    
    public void createBackupSchedule(CreateBackupScheduleRequest request, StreamObserver<BackupSchedule> responseObserver)

Creates a backup schedule on a database. At most two backup schedules can be configured on a database, one daily backup schedule and one weekly backup schedule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateBackupScheduleRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)>`  
  
  
### createDatabase(CreateDatabaseRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createDatabase(CreateDatabaseRequest request, StreamObserver<Operation> responseObserver)

Create a database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateDatabaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createIndex(CreateIndexRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createIndex(CreateIndexRequest request, StreamObserver<Operation> responseObserver)

Creates a composite index. This returns a google.longrunning.Operation which may be used to track the status of the creation. The metadata for the operation will be the type IndexOperationMetadata.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateIndexRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createUserCreds(CreateUserCredsRequest request, StreamObserver<UserCreds> responseObserver)
    
    
    public void createUserCreds(CreateUserCredsRequest request, StreamObserver<UserCreds> responseObserver)

Create a user creds.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateUserCredsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)>`  
  
  
### deleteBackup(DeleteBackupRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteBackup(DeleteBackupRequest request, StreamObserver<Empty> responseObserver)

Deletes a backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteBackupSchedule(DeleteBackupScheduleRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteBackupSchedule(DeleteBackupScheduleRequest request, StreamObserver<Empty> responseObserver)

Deletes a backup schedule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteBackupScheduleRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteDatabase(DeleteDatabaseRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteDatabase(DeleteDatabaseRequest request, StreamObserver<Operation> responseObserver)

Deletes a database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteDatabaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteIndex(DeleteIndexRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteIndex(DeleteIndexRequest request, StreamObserver<Empty> responseObserver)

Deletes a composite index.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteIndexRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteUserCreds(DeleteUserCredsRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteUserCreds(DeleteUserCredsRequest request, StreamObserver<Empty> responseObserver)

Deletes a user creds.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteUserCredsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### disableUserCreds(DisableUserCredsRequest request, StreamObserver<UserCreds> responseObserver)
    
    
    public void disableUserCreds(DisableUserCredsRequest request, StreamObserver<UserCreds> responseObserver)

Disables a user creds. No-op if the user creds are already disabled.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisableUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DisableUserCredsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)>`  
  
  
### enableUserCreds(EnableUserCredsRequest request, StreamObserver<UserCreds> responseObserver)
    
    
    public void enableUserCreds(EnableUserCredsRequest request, StreamObserver<UserCreds> responseObserver)

Enables a user creds. No-op if the user creds are already enabled.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EnableUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.EnableUserCredsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)>`  
  
  
### exportDocuments(ExportDocumentsRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void exportDocuments(ExportDocumentsRequest request, StreamObserver<Operation> responseObserver)

Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. Recent updates to documents may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage. For more details on export behavior and output format, refer to: <https://cloud.google.com/firestore/docs/manage-data/export-import>

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ExportDocumentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getBackup(GetBackupRequest request, StreamObserver<Backup> responseObserver)
    
    
    public void getBackup(GetBackupRequest request, StreamObserver<Backup> responseObserver)

Gets information about a backup.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetBackupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Backup)>`  
  
  
### getBackupSchedule(GetBackupScheduleRequest request, StreamObserver<BackupSchedule> responseObserver)
    
    
    public void getBackupSchedule(GetBackupScheduleRequest request, StreamObserver<BackupSchedule> responseObserver)

Gets information about a backup schedule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetBackupScheduleRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)>`  
  
  
### getDatabase(GetDatabaseRequest request, StreamObserver<Database> responseObserver)
    
    
    public void getDatabase(GetDatabaseRequest request, StreamObserver<Database> responseObserver)

Gets information about a database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetDatabaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database)>`  
  
  
### getField(GetFieldRequest request, StreamObserver<Field> responseObserver)
    
    
    public void getField(GetFieldRequest request, StreamObserver<Field> responseObserver)

Gets the metadata and configuration for a Field.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFieldRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetFieldRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Field](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Field)>`  
  
  
### getIndex(GetIndexRequest request, StreamObserver<Index> responseObserver)
    
    
    public void getIndex(GetIndexRequest request, StreamObserver<Index> responseObserver)

Gets a composite index.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetIndexRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index)>`  
  
  
### getUserCreds(GetUserCredsRequest request, StreamObserver<UserCreds> responseObserver)
    
    
    public void getUserCreds(GetUserCredsRequest request, StreamObserver<UserCreds> responseObserver)

Gets a user creds resource. Note that the returned resource does not contain the secret value itself.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetUserCredsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)>`  
  
  
### importDocuments(ImportDocumentsRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void importDocuments(ImportDocumentsRequest request, StreamObserver<Operation> responseObserver)

Imports documents into Google Cloud Firestore. Existing documents with the same name are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportDocuments operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Firestore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ImportDocumentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### listBackupSchedules(ListBackupSchedulesRequest request, StreamObserver<ListBackupSchedulesResponse> responseObserver)
    
    
    public void listBackupSchedules(ListBackupSchedulesRequest request, StreamObserver<ListBackupSchedulesResponse> responseObserver)

List backup schedules.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupSchedulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListBackupSchedulesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBackupSchedulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListBackupSchedulesResponse)>`  
  
  
### listBackups(ListBackupsRequest request, StreamObserver<ListBackupsResponse> responseObserver)
    
    
    public void listBackups(ListBackupsRequest request, StreamObserver<ListBackupsResponse> responseObserver)

Lists all the backups.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListBackupsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListBackupsResponse)>`  
  
  
### listDatabases(ListDatabasesRequest request, StreamObserver<ListDatabasesResponse> responseObserver)
    
    
    public void listDatabases(ListDatabasesRequest request, StreamObserver<ListDatabasesResponse> responseObserver)

List all the databases in the project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListDatabasesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListDatabasesResponse)>`  
  
  
### listFields(ListFieldsRequest request, StreamObserver<ListFieldsResponse> responseObserver)
    
    
    public void listFields(ListFieldsRequest request, StreamObserver<ListFieldsResponse> responseObserver)

Lists the field configuration and metadata for this database. Currently, FirestoreAdmin.ListFields only supports listing fields that have been explicitly overridden. To issue this query, call FirestoreAdmin.ListFields with the filter set to `indexConfig.usesAncestorConfig:false` or `ttlConfig:*`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFieldsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListFieldsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListFieldsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListFieldsResponse)>`  
  
  
### listIndexes(ListIndexesRequest request, StreamObserver<ListIndexesResponse> responseObserver)
    
    
    public void listIndexes(ListIndexesRequest request, StreamObserver<ListIndexesResponse> responseObserver)

Lists composite indexes.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListIndexesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListIndexesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListIndexesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListIndexesResponse)>`  
  
  
### listUserCreds(ListUserCredsRequest request, StreamObserver<ListUserCredsResponse> responseObserver)
    
    
    public void listUserCreds(ListUserCredsRequest request, StreamObserver<ListUserCredsResponse> responseObserver)

List all user creds in the database. Note that the returned resource does not contain the secret value itself.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListUserCredsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListUserCredsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListUserCredsResponse)>`  
  
  
### resetUserPassword(ResetUserPasswordRequest request, StreamObserver<UserCreds> responseObserver)
    
    
    public void resetUserPassword(ResetUserPasswordRequest request, StreamObserver<UserCreds> responseObserver)

Resets the password of a user creds.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResetUserPasswordRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ResetUserPasswordRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)>`  
  
  
### restoreDatabase(RestoreDatabaseRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void restoreDatabase(RestoreDatabaseRequest request, StreamObserver<Operation> responseObserver)

Creates a new database by restoring from an existing backup. The new database must be in the same cloud region or multi-region location as the existing backup. This behaves similar to FirestoreAdmin.CreateDatabase except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing backup. The long-running operation can be used to track the progress of the restore, with the Operation's metadata field type being the RestoreDatabaseMetadata. The response type is the Database if the restore was successful. The new database is not readable or writeable until the LRO has completed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.RestoreDatabaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateBackupSchedule(UpdateBackupScheduleRequest request, StreamObserver<BackupSchedule> responseObserver)
    
    
    public void updateBackupSchedule(UpdateBackupScheduleRequest request, StreamObserver<BackupSchedule> responseObserver)

Updates a backup schedule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UpdateBackupScheduleRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)>`  
  
  
### updateDatabase(UpdateDatabaseRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateDatabase(UpdateDatabaseRequest request, StreamObserver<Operation> responseObserver)

Updates a database.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UpdateDatabaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateField(UpdateFieldRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateField(UpdateFieldRequest request, StreamObserver<Operation> responseObserver)

Updates a field configuration. Currently, field updates apply only to single field index configuration. However, calls to FirestoreAdmin.UpdateField should provide a field mask to avoid changing any configuration that the caller isn't aware of. The field mask should be specified as: `{ paths: "index_config" }`. This call returns a google.longrunning.Operation which may be used to track the status of the field update. The metadata for the operation will be the type FieldOperationMetadata. To configure the default field settings for the database, use the special `Field` with resource name: `projects/{project_id}/databases/{database_id}/collectionGroups/**default** /fields/*`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFieldRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UpdateFieldRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
