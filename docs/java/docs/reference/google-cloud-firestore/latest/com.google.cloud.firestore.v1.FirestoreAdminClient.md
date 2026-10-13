---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.FirestoreAdminClient
title: Class FirestoreAdminClient (3.49.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:31.902157+00:00
---

# Class FirestoreAdminClient (3.49.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.FirestoreAdminClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class FirestoreAdminClient (3.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.49.0 (latest)  3.45.0  3.44.0  3.43.1  3.41.0  3.38.0  3.37.0  3.36.0  3.35.1  3.33.4  3.32.2  3.31.9  3.30.11  3.28.0  3.27.2  3.26.5  3.25.1  3.24.3  3.22.0  3.21.4  3.20.0  3.17.0  3.16.3  3.15.7  3.14.4  3.13.2  3.12.1  3.11.0  3.10.0  3.9.6  3.8.2  3.7.10  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.1.0  3.0.21 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-firestore/google-cloud-firestore-admin/src/main/java/com/google/cloud/firestore/v1/FirestoreAdminClient.java)| [Product Reference](https://cloud.google.com/firestore)  
---|---  
  
Service Description: The Cloud Firestore Admin API.

This API provides several administrative services for Cloud Firestore.

Project, Database, Namespace, Collection, Collection Group, and Document are used as defined in the Google Cloud Firestore API.

Operation: An Operation represents work being performed in the background.

The index service manages Cloud Firestore indexes.

Index creation is performed asynchronously. An Operation resource is created for each such asynchronous operation. The state of the operation (including any errors encountered) may be queried via the Operation resource.

The Operations collection provides a record of actions performed for the specified Project (including any Operations in progress). Operations are not created directly but through calls on other collections or resources.

An Operation that is done may be deleted so that it is no longer listed as part of the Operation collection. Operations are garbage collected after 30 days. By default, ListOperations will only return in progress and failed operations. To list completed operation, issue a ListOperations request with the filter `done: true`.

Operations are created by service `FirestoreAdmin`, but are accessed via service `google.longrunning.Operations`.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       IndexName name = IndexName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]", "[INDEX]");
       Index response = firestoreAdminClient.getIndex(name);
     }
     

Note: close() needs to be called on the FirestoreAdminClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateIndex |  Creates a composite index. This returns a google.longrunning.Operation which may be used to track the status of the creation. The metadata for the operation will be the type IndexOperationMetadata. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createIndexAsync(CreateIndexRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createIndexAsync(CollectionGroupName parent, Index index) 
  * createIndexAsync(String parent, Index index) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createIndexOperationCallable() 
  * createIndexCallable() 

  
ListIndexes |  Lists composite indexes. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listIndexes(ListIndexesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listIndexes(CollectionGroupName parent) 
  * listIndexes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listIndexesPagedCallable() 
  * listIndexesCallable() 

  
GetIndex |  Gets a composite index. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIndex(GetIndexRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIndex(IndexName name) 
  * getIndex(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIndexCallable() 

  
DeleteIndex |  Deletes a composite index. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteIndex(DeleteIndexRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteIndex(IndexName name) 
  * deleteIndex(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteIndexCallable() 

  
GetField |  Gets the metadata and configuration for a Field. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getField(GetFieldRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getField(FieldName name) 
  * getField(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getFieldCallable() 

  
UpdateField |  Updates a field configuration. Currently, field updates apply only to single field index configuration. However, calls to FirestoreAdmin.UpdateField should provide a field mask to avoid changing any configuration that the caller isn't aware of. The field mask should be specified as: `{ paths: "index_config" }`.  This call returns a google.longrunning.Operation which may be used to track the status of the field update. The metadata for the operation will be the type FieldOperationMetadata.  To configure the default field settings for the database, use the special `Field` with resource name: `projects/{project_id}/databases/{database_id}/collectionGroups/**default** /fields/*`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateFieldAsync(UpdateFieldRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateFieldAsync(Field field) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateFieldOperationCallable() 
  * updateFieldCallable() 

  
ListFields |  Lists the field configuration and metadata for this database.  Currently, FirestoreAdmin.ListFields only supports listing fields that have been explicitly overridden. To issue this query, call FirestoreAdmin.ListFields with the filter set to `indexConfig.usesAncestorConfig:false` or `ttlConfig:*`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listFields(ListFieldsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listFields(CollectionGroupName parent) 
  * listFields(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listFieldsPagedCallable() 
  * listFieldsCallable() 

  
ExportDocuments |  Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. Recent updates to documents may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage.  For more details on export behavior and output format, refer to: <https://cloud.google.com/firestore/docs/manage-data/export-import> |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportDocumentsAsync(ExportDocumentsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * exportDocumentsAsync(DatabaseName name) 
  * exportDocumentsAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportDocumentsOperationCallable() 
  * exportDocumentsCallable() 

  
ImportDocuments |  Imports documents into Google Cloud Firestore. Existing documents with the same name are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportDocuments operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Firestore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importDocumentsAsync(ImportDocumentsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * importDocumentsAsync(DatabaseName name) 
  * importDocumentsAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importDocumentsOperationCallable() 
  * importDocumentsCallable() 

  
BulkDeleteDocuments |  Bulk deletes a subset of documents from Google Cloud Firestore. Documents created or updated after the underlying system starts to process the request will not be deleted. The bulk delete occurs in the background and its progress can be monitored and managed via the Operation resource that is created.  For more details on bulk delete behavior, refer to: <https://cloud.google.com/firestore/docs/manage-data/bulk-delete> |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * bulkDeleteDocumentsAsync(BulkDeleteDocumentsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * bulkDeleteDocumentsAsync(DatabaseName name) 
  * bulkDeleteDocumentsAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * bulkDeleteDocumentsOperationCallable() 
  * bulkDeleteDocumentsCallable() 

  
CreateDatabase |  Create a database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDatabaseAsync(CreateDatabaseRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createDatabaseAsync(ProjectName parent, Database database, String databaseId) 
  * createDatabaseAsync(String parent, Database database, String databaseId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDatabaseOperationCallable() 
  * createDatabaseCallable() 

  
GetDatabase |  Gets information about a database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDatabase(GetDatabaseRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDatabase(DatabaseName name) 
  * getDatabase(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDatabaseCallable() 

  
ListDatabases |  List all the databases in the project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDatabases(ListDatabasesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDatabases(ProjectName parent) 
  * listDatabases(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDatabasesCallable() 

  
UpdateDatabase |  Updates a database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDatabaseAsync(UpdateDatabaseRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateDatabaseAsync(Database database, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDatabaseOperationCallable() 
  * updateDatabaseCallable() 

  
DeleteDatabase |  Deletes a database. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDatabaseAsync(DeleteDatabaseRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteDatabaseAsync(DatabaseName name) 
  * deleteDatabaseAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDatabaseOperationCallable() 
  * deleteDatabaseCallable() 

  
CreateUserCreds |  Create a user creds. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createUserCreds(CreateUserCredsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createUserCreds(DatabaseName parent, UserCreds userCreds, String userCredsId) 
  * createUserCreds(String parent, UserCreds userCreds, String userCredsId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createUserCredsCallable() 

  
GetUserCreds |  Gets a user creds resource. Note that the returned resource does not contain the secret value itself. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getUserCreds(GetUserCredsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getUserCreds(UserCredsName name) 
  * getUserCreds(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getUserCredsCallable() 

  
ListUserCreds |  List all user creds in the database. Note that the returned resource does not contain the secret value itself. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listUserCreds(ListUserCredsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listUserCreds(DatabaseName parent) 
  * listUserCreds(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listUserCredsCallable() 

  
EnableUserCreds |  Enables a user creds. No-op if the user creds are already enabled. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * enableUserCreds(EnableUserCredsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * enableUserCreds(UserCredsName name) 
  * enableUserCreds(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * enableUserCredsCallable() 

  
DisableUserCreds |  Disables a user creds. No-op if the user creds are already disabled. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * disableUserCreds(DisableUserCredsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * disableUserCreds(UserCredsName name) 
  * disableUserCreds(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * disableUserCredsCallable() 

  
ResetUserPassword |  Resets the password of a user creds. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resetUserPassword(ResetUserPasswordRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * resetUserPassword(UserCredsName name) 
  * resetUserPassword(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resetUserPasswordCallable() 

  
DeleteUserCreds |  Deletes a user creds. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteUserCreds(DeleteUserCredsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteUserCreds(UserCredsName name) 
  * deleteUserCreds(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteUserCredsCallable() 

  
GetBackup |  Gets information about a backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBackup(GetBackupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBackup(BackupName name) 
  * getBackup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBackupCallable() 

  
ListBackups |  Lists all the backups. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBackups(ListBackupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBackups(LocationName parent) 
  * listBackups(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBackupsCallable() 

  
DeleteBackup |  Deletes a backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBackup(DeleteBackupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteBackup(BackupName name) 
  * deleteBackup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBackupCallable() 

  
RestoreDatabase |  Creates a new database by restoring from an existing backup.  The new database must be in the same cloud region or multi-region location as the existing backup. This behaves similar to FirestoreAdmin.CreateDatabase except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing backup.  The long-running operation can be used to track the progress of the restore, with the Operation's metadata field type being the RestoreDatabaseMetadata. The response type is the Database if the restore was successful. The new database is not readable or writeable until the LRO has completed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * restoreDatabaseAsync(RestoreDatabaseRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * restoreDatabaseOperationCallable() 
  * restoreDatabaseCallable() 

  
CreateBackupSchedule |  Creates a backup schedule on a database. At most two backup schedules can be configured on a database, one daily backup schedule and one weekly backup schedule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createBackupSchedule(CreateBackupScheduleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createBackupSchedule(DatabaseName parent, BackupSchedule backupSchedule) 
  * createBackupSchedule(String parent, BackupSchedule backupSchedule) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createBackupScheduleCallable() 

  
GetBackupSchedule |  Gets information about a backup schedule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBackupSchedule(GetBackupScheduleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBackupSchedule(BackupScheduleName name) 
  * getBackupSchedule(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBackupScheduleCallable() 

  
ListBackupSchedules |  List backup schedules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBackupSchedules(ListBackupSchedulesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBackupSchedules(DatabaseName parent) 
  * listBackupSchedules(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBackupSchedulesCallable() 

  
UpdateBackupSchedule |  Updates a backup schedule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateBackupSchedule(UpdateBackupScheduleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateBackupSchedule(BackupSchedule backupSchedule, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateBackupScheduleCallable() 

  
DeleteBackupSchedule |  Deletes a backup schedule. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBackupSchedule(DeleteBackupScheduleRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteBackupSchedule(BackupScheduleName name) 
  * deleteBackupSchedule(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBackupScheduleCallable() 

  
CloneDatabase |  Creates a new database by cloning an existing one.  The new database must be in the same cloud region or multi-region location as the existing database. This behaves similar to FirestoreAdmin.CreateDatabase except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing database.  The long-running operation can be used to track the progress of the clone, with the Operation's metadata field type being the CloneDatabaseMetadata. The response type is the Database if the clone was successful. The new database is not readable or writeable until the LRO has completed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cloneDatabaseAsync(CloneDatabaseRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cloneDatabaseOperationCallable() 
  * cloneDatabaseCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of FirestoreAdminSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FirestoreAdminSettings firestoreAdminSettings =
         FirestoreAdminSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create(firestoreAdminSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FirestoreAdminSettings firestoreAdminSettings =
         FirestoreAdminSettings.newBuilder().setEndpoint(myEndpoint).build();
     FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create(firestoreAdminSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FirestoreAdminSettings firestoreAdminSettings =
         FirestoreAdminSettings.newHttpJsonBuilder().build();
     FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create(firestoreAdminSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FirestoreAdminClient

## Static Methods 

### create()
    
    
    public static final FirestoreAdminClient create()

Constructs an instance of FirestoreAdminClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[FirestoreAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.FirestoreAdminClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FirestoreAdminSettings settings)
    
    
    public static final FirestoreAdminClient create(FirestoreAdminSettings settings)

Constructs an instance of FirestoreAdminClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FirestoreAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.FirestoreAdminSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FirestoreAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.FirestoreAdminClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FirestoreAdminStub stub)
    
    
    public static final FirestoreAdminClient create(FirestoreAdminStub stub)

Constructs an instance of FirestoreAdminClient, using the given stub for making calls. This is for advanced usage - prefer using create(FirestoreAdminSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FirestoreAdminStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.stub.FirestoreAdminStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FirestoreAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.FirestoreAdminClient)` |   
  
## Constructors 

### FirestoreAdminClient(FirestoreAdminSettings settings)
    
    
    protected FirestoreAdminClient(FirestoreAdminSettings settings)

Constructs an instance of FirestoreAdminClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FirestoreAdminSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.FirestoreAdminSettings)`  
  
  
### FirestoreAdminClient(FirestoreAdminStub stub)
    
    
    protected FirestoreAdminClient(FirestoreAdminStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FirestoreAdminStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.stub.FirestoreAdminStub)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### bulkDeleteDocumentsAsync(@Nullable DatabaseName name)
    
    
    public final OperationFuture<BulkDeleteDocumentsResponse,BulkDeleteDocumentsMetadata> bulkDeleteDocumentsAsync(@Nullable DatabaseName name)

Bulk deletes a subset of documents from Google Cloud Firestore. Documents created or updated after the underlying system starts to process the request will not be deleted. The bulk delete occurs in the background and its progress can be monitored and managed via the Operation resource that is created.

For more details on bulk delete behavior, refer to: <https://cloud.google.com/firestore/docs/manage-data/bulk-delete>

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DatabaseName name = DatabaseName.of("[PROJECT]", "[DATABASE]");
       BulkDeleteDocumentsResponse response =
           firestoreAdminClient.bulkDeleteDocumentsAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.DatabaseName`  
Required. Database to operate. Should be of the form: `projects/{project_id}/databases/{database_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BulkDeleteDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BulkDeleteDocumentsResponse),[BulkDeleteDocumentsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BulkDeleteDocumentsMetadata)>` |   
  
### bulkDeleteDocumentsAsync(BulkDeleteDocumentsRequest request)
    
    
    public final OperationFuture<BulkDeleteDocumentsResponse,BulkDeleteDocumentsMetadata> bulkDeleteDocumentsAsync(BulkDeleteDocumentsRequest request)

Bulk deletes a subset of documents from Google Cloud Firestore. Documents created or updated after the underlying system starts to process the request will not be deleted. The bulk delete occurs in the background and its progress can be monitored and managed via the Operation resource that is created.

For more details on bulk delete behavior, refer to: <https://cloud.google.com/firestore/docs/manage-data/bulk-delete>

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       BulkDeleteDocumentsRequest request =
           BulkDeleteDocumentsRequest.newBuilder()
               .setName(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .addAllCollectionIds(new ArrayList<String>())
               .addAllNamespaceIds(new ArrayList<String>())
               .build();
       BulkDeleteDocumentsResponse response =
           firestoreAdminClient.bulkDeleteDocumentsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BulkDeleteDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BulkDeleteDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BulkDeleteDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BulkDeleteDocumentsResponse),[BulkDeleteDocumentsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BulkDeleteDocumentsMetadata)>` |   
  
### bulkDeleteDocumentsAsync(String name)
    
    
    public final OperationFuture<BulkDeleteDocumentsResponse,BulkDeleteDocumentsMetadata> bulkDeleteDocumentsAsync(String name)

Bulk deletes a subset of documents from Google Cloud Firestore. Documents created or updated after the underlying system starts to process the request will not be deleted. The bulk delete occurs in the background and its progress can be monitored and managed via the Operation resource that is created.

For more details on bulk delete behavior, refer to: <https://cloud.google.com/firestore/docs/manage-data/bulk-delete>

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name = DatabaseName.of("[PROJECT]", "[DATABASE]").toString();
       BulkDeleteDocumentsResponse response =
           firestoreAdminClient.bulkDeleteDocumentsAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Database to operate. Should be of the form: `projects/{project_id}/databases/{database_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BulkDeleteDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BulkDeleteDocumentsResponse),[BulkDeleteDocumentsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BulkDeleteDocumentsMetadata)>` |   
  
### bulkDeleteDocumentsCallable()
    
    
    public final UnaryCallable<BulkDeleteDocumentsRequest,Operation> bulkDeleteDocumentsCallable()

Bulk deletes a subset of documents from Google Cloud Firestore. Documents created or updated after the underlying system starts to process the request will not be deleted. The bulk delete occurs in the background and its progress can be monitored and managed via the Operation resource that is created.

For more details on bulk delete behavior, refer to: <https://cloud.google.com/firestore/docs/manage-data/bulk-delete>

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       BulkDeleteDocumentsRequest request =
           BulkDeleteDocumentsRequest.newBuilder()
               .setName(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .addAllCollectionIds(new ArrayList<String>())
               .addAllNamespaceIds(new ArrayList<String>())
               .build();
       ApiFuture<Operation> future =
           firestoreAdminClient.bulkDeleteDocumentsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BulkDeleteDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BulkDeleteDocumentsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### bulkDeleteDocumentsOperationCallable()
    
    
    public final OperationCallable<BulkDeleteDocumentsRequest,BulkDeleteDocumentsResponse,BulkDeleteDocumentsMetadata> bulkDeleteDocumentsOperationCallable()

Bulk deletes a subset of documents from Google Cloud Firestore. Documents created or updated after the underlying system starts to process the request will not be deleted. The bulk delete occurs in the background and its progress can be monitored and managed via the Operation resource that is created.

For more details on bulk delete behavior, refer to: <https://cloud.google.com/firestore/docs/manage-data/bulk-delete>

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       BulkDeleteDocumentsRequest request =
           BulkDeleteDocumentsRequest.newBuilder()
               .setName(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .addAllCollectionIds(new ArrayList<String>())
               .addAllNamespaceIds(new ArrayList<String>())
               .build();
       OperationFuture<BulkDeleteDocumentsResponse, BulkDeleteDocumentsMetadata> future =
           firestoreAdminClient.bulkDeleteDocumentsOperationCallable().futureCall(request);
       // Do something.
       BulkDeleteDocumentsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BulkDeleteDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BulkDeleteDocumentsRequest),[BulkDeleteDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BulkDeleteDocumentsResponse),[BulkDeleteDocumentsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BulkDeleteDocumentsMetadata)>` |   
  
### cloneDatabaseAsync(CloneDatabaseRequest request)
    
    
    public final OperationFuture<Database,CloneDatabaseMetadata> cloneDatabaseAsync(CloneDatabaseRequest request)

Creates a new database by cloning an existing one.

The new database must be in the same cloud region or multi-region location as the existing database. This behaves similar to FirestoreAdmin.CreateDatabase except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing database.

The long-running operation can be used to track the progress of the clone, with the Operation's metadata field type being the CloneDatabaseMetadata. The response type is the Database if the clone was successful. The new database is not readable or writeable until the LRO has completed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       CloneDatabaseRequest request =
           CloneDatabaseRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setDatabaseId("databaseId1688905718")
               .setPitrSnapshot(PitrSnapshot.newBuilder().build())
               .setEncryptionConfig(Database.EncryptionConfig.newBuilder().build())
               .putAllTags(new HashMap<String, String>())
               .build();
       Database response = firestoreAdminClient.cloneDatabaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CloneDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CloneDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database),[CloneDatabaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CloneDatabaseMetadata)>` |   
  
### cloneDatabaseCallable()
    
    
    public final UnaryCallable<CloneDatabaseRequest,Operation> cloneDatabaseCallable()

Creates a new database by cloning an existing one.

The new database must be in the same cloud region or multi-region location as the existing database. This behaves similar to FirestoreAdmin.CreateDatabase except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing database.

The long-running operation can be used to track the progress of the clone, with the Operation's metadata field type being the CloneDatabaseMetadata. The response type is the Database if the clone was successful. The new database is not readable or writeable until the LRO has completed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       CloneDatabaseRequest request =
           CloneDatabaseRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setDatabaseId("databaseId1688905718")
               .setPitrSnapshot(PitrSnapshot.newBuilder().build())
               .setEncryptionConfig(Database.EncryptionConfig.newBuilder().build())
               .putAllTags(new HashMap<String, String>())
               .build();
       ApiFuture<Operation> future =
           firestoreAdminClient.cloneDatabaseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CloneDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CloneDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### cloneDatabaseOperationCallable()
    
    
    public final OperationCallable<CloneDatabaseRequest,Database,CloneDatabaseMetadata> cloneDatabaseOperationCallable()

Creates a new database by cloning an existing one.

The new database must be in the same cloud region or multi-region location as the existing database. This behaves similar to FirestoreAdmin.CreateDatabase except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing database.

The long-running operation can be used to track the progress of the clone, with the Operation's metadata field type being the CloneDatabaseMetadata. The response type is the Database if the clone was successful. The new database is not readable or writeable until the LRO has completed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       CloneDatabaseRequest request =
           CloneDatabaseRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setDatabaseId("databaseId1688905718")
               .setPitrSnapshot(PitrSnapshot.newBuilder().build())
               .setEncryptionConfig(Database.EncryptionConfig.newBuilder().build())
               .putAllTags(new HashMap<String, String>())
               .build();
       OperationFuture<Database, CloneDatabaseMetadata> future =
           firestoreAdminClient.cloneDatabaseOperationCallable().futureCall(request);
       // Do something.
       Database response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CloneDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CloneDatabaseRequest),[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database),[CloneDatabaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CloneDatabaseMetadata)>` |   
  
### close()
    
    
    public final void close()

### createBackupSchedule(@Nullable DatabaseName parent, BackupSchedule backupSchedule)
    
    
    public final BackupSchedule createBackupSchedule(@Nullable DatabaseName parent, BackupSchedule backupSchedule)

Creates a backup schedule on a database. At most two backup schedules can be configured on a database, one daily backup schedule and one weekly backup schedule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DatabaseName parent = DatabaseName.of("[PROJECT]", "[DATABASE]");
       BackupSchedule backupSchedule = BackupSchedule.newBuilder().build();
       BackupSchedule response = firestoreAdminClient.createBackupSchedule(parent, backupSchedule);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.DatabaseName`  
Required. The parent database. Format `projects/{project}/databases/{database}`  
`backupSchedule` | `[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)`  
Required. The backup schedule to create.  
**Returns**  
---  
**Type** | **Description**  
`[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)` |   
  
### createBackupSchedule(CreateBackupScheduleRequest request)
    
    
    public final BackupSchedule createBackupSchedule(CreateBackupScheduleRequest request)

Creates a backup schedule on a database. At most two backup schedules can be configured on a database, one daily backup schedule and one weekly backup schedule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       CreateBackupScheduleRequest request =
           CreateBackupScheduleRequest.newBuilder()
               .setParent(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .setBackupSchedule(BackupSchedule.newBuilder().build())
               .build();
       BackupSchedule response = firestoreAdminClient.createBackupSchedule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateBackupScheduleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)` |   
  
### createBackupSchedule(String parent, BackupSchedule backupSchedule)
    
    
    public final BackupSchedule createBackupSchedule(String parent, BackupSchedule backupSchedule)

Creates a backup schedule on a database. At most two backup schedules can be configured on a database, one daily backup schedule and one weekly backup schedule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String parent = DatabaseName.of("[PROJECT]", "[DATABASE]").toString();
       BackupSchedule backupSchedule = BackupSchedule.newBuilder().build();
       BackupSchedule response = firestoreAdminClient.createBackupSchedule(parent, backupSchedule);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent database. Format `projects/{project}/databases/{database}`  
`backupSchedule` | `[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)`  
Required. The backup schedule to create.  
**Returns**  
---  
**Type** | **Description**  
`[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)` |   
  
### createBackupScheduleCallable()
    
    
    public final UnaryCallable<CreateBackupScheduleRequest,BackupSchedule> createBackupScheduleCallable()

Creates a backup schedule on a database. At most two backup schedules can be configured on a database, one daily backup schedule and one weekly backup schedule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       CreateBackupScheduleRequest request =
           CreateBackupScheduleRequest.newBuilder()
               .setParent(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .setBackupSchedule(BackupSchedule.newBuilder().build())
               .build();
       ApiFuture<BackupSchedule> future =
           firestoreAdminClient.createBackupScheduleCallable().futureCall(request);
       // Do something.
       BackupSchedule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateBackupScheduleRequest),[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)>` |   
  
### createDatabaseAsync(@Nullable ProjectName parent, Database database, String databaseId)
    
    
    public final OperationFuture<Database,CreateDatabaseMetadata> createDatabaseAsync(@Nullable ProjectName parent, Database database, String databaseId)

Create a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       Database database = Database.newBuilder().build();
       String databaseId = "databaseId1688905718";
       Database response =
           firestoreAdminClient.createDatabaseAsync(parent, database, databaseId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.ProjectName`  
Required. A parent name of the form `projects/{project_id}`  
`database` | `[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database)`  
Required. The Database to create.  
`databaseId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the database, which will become the final component of the database's resource name. This value should be 4-63 characters. Valid characters are /a-z-/ with first character a letter and the last a letter or a number. Must not be UUID-like /[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}/. "(default)" database ID is also valid if the database is Standard edition.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database),[CreateDatabaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateDatabaseMetadata)>` |   
  
### createDatabaseAsync(CreateDatabaseRequest request)
    
    
    public final OperationFuture<Database,CreateDatabaseMetadata> createDatabaseAsync(CreateDatabaseRequest request)

Create a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       CreateDatabaseRequest request =
           CreateDatabaseRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setDatabase(Database.newBuilder().build())
               .setDatabaseId("databaseId1688905718")
               .build();
       Database response = firestoreAdminClient.createDatabaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database),[CreateDatabaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateDatabaseMetadata)>` |   
  
### createDatabaseAsync(String parent, Database database, String databaseId)
    
    
    public final OperationFuture<Database,CreateDatabaseMetadata> createDatabaseAsync(String parent, Database database, String databaseId)

Create a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       Database database = Database.newBuilder().build();
       String databaseId = "databaseId1688905718";
       Database response =
           firestoreAdminClient.createDatabaseAsync(parent, database, databaseId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A parent name of the form `projects/{project_id}`  
`database` | `[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database)`  
Required. The Database to create.  
`databaseId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the database, which will become the final component of the database's resource name. This value should be 4-63 characters. Valid characters are /a-z-/ with first character a letter and the last a letter or a number. Must not be UUID-like /[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}/. "(default)" database ID is also valid if the database is Standard edition.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database),[CreateDatabaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateDatabaseMetadata)>` |   
  
### createDatabaseCallable()
    
    
    public final UnaryCallable<CreateDatabaseRequest,Operation> createDatabaseCallable()

Create a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       CreateDatabaseRequest request =
           CreateDatabaseRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setDatabase(Database.newBuilder().build())
               .setDatabaseId("databaseId1688905718")
               .build();
       ApiFuture<Operation> future =
           firestoreAdminClient.createDatabaseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDatabaseOperationCallable()
    
    
    public final OperationCallable<CreateDatabaseRequest,Database,CreateDatabaseMetadata> createDatabaseOperationCallable()

Create a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       CreateDatabaseRequest request =
           CreateDatabaseRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setDatabase(Database.newBuilder().build())
               .setDatabaseId("databaseId1688905718")
               .build();
       OperationFuture<Database, CreateDatabaseMetadata> future =
           firestoreAdminClient.createDatabaseOperationCallable().futureCall(request);
       // Do something.
       Database response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateDatabaseRequest),[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database),[CreateDatabaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateDatabaseMetadata)>` |   
  
### createIndexAsync(@Nullable CollectionGroupName parent, Index index)
    
    
    public final OperationFuture<Index,IndexOperationMetadata> createIndexAsync(@Nullable CollectionGroupName parent, Index index)

Creates a composite index. This returns a google.longrunning.Operation which may be used to track the status of the creation. The metadata for the operation will be the type IndexOperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       CollectionGroupName parent =
           CollectionGroupName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]");
       Index index = Index.newBuilder().build();
       Index response = firestoreAdminClient.createIndexAsync(parent, index).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.CollectionGroupName`  
Required. A parent name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}`  
`index` | `[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index)`  
Required. The composite index to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index),[IndexOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.IndexOperationMetadata)>` |   
  
### createIndexAsync(CreateIndexRequest request)
    
    
    public final OperationFuture<Index,IndexOperationMetadata> createIndexAsync(CreateIndexRequest request)

Creates a composite index. This returns a google.longrunning.Operation which may be used to track the status of the creation. The metadata for the operation will be the type IndexOperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       CreateIndexRequest request =
           CreateIndexRequest.newBuilder()
               .setParent(
                   CollectionGroupName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]").toString())
               .setIndex(Index.newBuilder().build())
               .build();
       Index response = firestoreAdminClient.createIndexAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateIndexRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index),[IndexOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.IndexOperationMetadata)>` |   
  
### createIndexAsync(String parent, Index index)
    
    
    public final OperationFuture<Index,IndexOperationMetadata> createIndexAsync(String parent, Index index)

Creates a composite index. This returns a google.longrunning.Operation which may be used to track the status of the creation. The metadata for the operation will be the type IndexOperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String parent = CollectionGroupName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]").toString();
       Index index = Index.newBuilder().build();
       Index response = firestoreAdminClient.createIndexAsync(parent, index).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A parent name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}`  
`index` | `[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index)`  
Required. The composite index to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index),[IndexOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.IndexOperationMetadata)>` |   
  
### createIndexCallable()
    
    
    public final UnaryCallable<CreateIndexRequest,Operation> createIndexCallable()

Creates a composite index. This returns a google.longrunning.Operation which may be used to track the status of the creation. The metadata for the operation will be the type IndexOperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       CreateIndexRequest request =
           CreateIndexRequest.newBuilder()
               .setParent(
                   CollectionGroupName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]").toString())
               .setIndex(Index.newBuilder().build())
               .build();
       ApiFuture<Operation> future = firestoreAdminClient.createIndexCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateIndexRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createIndexOperationCallable()
    
    
    public final OperationCallable<CreateIndexRequest,Index,IndexOperationMetadata> createIndexOperationCallable()

Creates a composite index. This returns a google.longrunning.Operation which may be used to track the status of the creation. The metadata for the operation will be the type IndexOperationMetadata.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       CreateIndexRequest request =
           CreateIndexRequest.newBuilder()
               .setParent(
                   CollectionGroupName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]").toString())
               .setIndex(Index.newBuilder().build())
               .build();
       OperationFuture<Index, IndexOperationMetadata> future =
           firestoreAdminClient.createIndexOperationCallable().futureCall(request);
       // Do something.
       Index response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateIndexRequest),[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index),[IndexOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.IndexOperationMetadata)>` |   
  
### createUserCreds(@Nullable DatabaseName parent, UserCreds userCreds, String userCredsId)
    
    
    public final UserCreds createUserCreds(@Nullable DatabaseName parent, UserCreds userCreds, String userCredsId)

Create a user creds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DatabaseName parent = DatabaseName.of("[PROJECT]", "[DATABASE]");
       UserCreds userCreds = UserCreds.newBuilder().build();
       String userCredsId = "userCredsId726775445";
       UserCreds response = firestoreAdminClient.createUserCreds(parent, userCreds, userCredsId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.DatabaseName`  
Required. A parent name of the form `projects/{project_id}/databases/{database_id}`  
`userCreds` | `[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)`  
Required. The user creds to create.  
`userCredsId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the user creds, which will become the final component of the user creds's resource name. This value should be 4-63 characters. Valid characters are /a-z-/ with first character a letter and the last a letter or a number. Must not be UUID-like /[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}/.  
**Returns**  
---  
**Type** | **Description**  
`[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)` |   
  
### createUserCreds(CreateUserCredsRequest request)
    
    
    public final UserCreds createUserCreds(CreateUserCredsRequest request)

Create a user creds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       CreateUserCredsRequest request =
           CreateUserCredsRequest.newBuilder()
               .setParent(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .setUserCreds(UserCreds.newBuilder().build())
               .setUserCredsId("userCredsId726775445")
               .build();
       UserCreds response = firestoreAdminClient.createUserCreds(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateUserCredsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)` |   
  
### createUserCreds(String parent, UserCreds userCreds, String userCredsId)
    
    
    public final UserCreds createUserCreds(String parent, UserCreds userCreds, String userCredsId)

Create a user creds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String parent = DatabaseName.of("[PROJECT]", "[DATABASE]").toString();
       UserCreds userCreds = UserCreds.newBuilder().build();
       String userCredsId = "userCredsId726775445";
       UserCreds response = firestoreAdminClient.createUserCreds(parent, userCreds, userCredsId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A parent name of the form `projects/{project_id}/databases/{database_id}`  
`userCreds` | `[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)`  
Required. The user creds to create.  
`userCredsId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the user creds, which will become the final component of the user creds's resource name. This value should be 4-63 characters. Valid characters are /a-z-/ with first character a letter and the last a letter or a number. Must not be UUID-like /[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}/.  
**Returns**  
---  
**Type** | **Description**  
`[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)` |   
  
### createUserCredsCallable()
    
    
    public final UnaryCallable<CreateUserCredsRequest,UserCreds> createUserCredsCallable()

Create a user creds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       CreateUserCredsRequest request =
           CreateUserCredsRequest.newBuilder()
               .setParent(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .setUserCreds(UserCreds.newBuilder().build())
               .setUserCredsId("userCredsId726775445")
               .build();
       ApiFuture<UserCreds> future =
           firestoreAdminClient.createUserCredsCallable().futureCall(request);
       // Do something.
       UserCreds response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.CreateUserCredsRequest),[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)>` |   
  
### deleteBackup(@Nullable BackupName name)
    
    
    public final void deleteBackup(@Nullable BackupName name)

Deletes a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       BackupName name = BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]");
       firestoreAdminClient.deleteBackup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.BackupName`  
Required. Name of the backup to delete. format is `projects/{project}/locations/{location}/backups/{backup}`.  
  
### deleteBackup(DeleteBackupRequest request)
    
    
    public final void deleteBackup(DeleteBackupRequest request)

Deletes a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DeleteBackupRequest request =
           DeleteBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]").toString())
               .build();
       firestoreAdminClient.deleteBackup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteBackupRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteBackup(String name)
    
    
    public final void deleteBackup(String name)

Deletes a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name = BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]").toString();
       firestoreAdminClient.deleteBackup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the backup to delete. format is `projects/{project}/locations/{location}/backups/{backup}`.  
  
### deleteBackupCallable()
    
    
    public final UnaryCallable<DeleteBackupRequest,Empty> deleteBackupCallable()

Deletes a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DeleteBackupRequest request =
           DeleteBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]").toString())
               .build();
       ApiFuture<Empty> future = firestoreAdminClient.deleteBackupCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteBackupRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteBackupSchedule(@Nullable BackupScheduleName name)
    
    
    public final void deleteBackupSchedule(@Nullable BackupScheduleName name)

Deletes a backup schedule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       BackupScheduleName name =
           BackupScheduleName.of("[PROJECT]", "[DATABASE]", "[BACKUP_SCHEDULE]");
       firestoreAdminClient.deleteBackupSchedule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.BackupScheduleName`  
Required. The name of the backup schedule. Format `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`  
  
### deleteBackupSchedule(DeleteBackupScheduleRequest request)
    
    
    public final void deleteBackupSchedule(DeleteBackupScheduleRequest request)

Deletes a backup schedule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DeleteBackupScheduleRequest request =
           DeleteBackupScheduleRequest.newBuilder()
               .setName(
                   BackupScheduleName.of("[PROJECT]", "[DATABASE]", "[BACKUP_SCHEDULE]").toString())
               .build();
       firestoreAdminClient.deleteBackupSchedule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteBackupScheduleRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteBackupSchedule(String name)
    
    
    public final void deleteBackupSchedule(String name)

Deletes a backup schedule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name =
           BackupScheduleName.of("[PROJECT]", "[DATABASE]", "[BACKUP_SCHEDULE]").toString();
       firestoreAdminClient.deleteBackupSchedule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the backup schedule. Format `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`  
  
### deleteBackupScheduleCallable()
    
    
    public final UnaryCallable<DeleteBackupScheduleRequest,Empty> deleteBackupScheduleCallable()

Deletes a backup schedule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DeleteBackupScheduleRequest request =
           DeleteBackupScheduleRequest.newBuilder()
               .setName(
                   BackupScheduleName.of("[PROJECT]", "[DATABASE]", "[BACKUP_SCHEDULE]").toString())
               .build();
       ApiFuture<Empty> future =
           firestoreAdminClient.deleteBackupScheduleCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteBackupScheduleRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteDatabaseAsync(@Nullable DatabaseName name)
    
    
    public final OperationFuture<Database,DeleteDatabaseMetadata> deleteDatabaseAsync(@Nullable DatabaseName name)

Deletes a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DatabaseName name = DatabaseName.of("[PROJECT]", "[DATABASE]");
       Database response = firestoreAdminClient.deleteDatabaseAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.DatabaseName`  
Required. A name of the form `projects/{project_id}/databases/{database_id}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database),[DeleteDatabaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteDatabaseMetadata)>` |   
  
### deleteDatabaseAsync(DeleteDatabaseRequest request)
    
    
    public final OperationFuture<Database,DeleteDatabaseMetadata> deleteDatabaseAsync(DeleteDatabaseRequest request)

Deletes a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DeleteDatabaseRequest request =
           DeleteDatabaseRequest.newBuilder()
               .setName(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .setEtag("etag3123477")
               .build();
       Database response = firestoreAdminClient.deleteDatabaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database),[DeleteDatabaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteDatabaseMetadata)>` |   
  
### deleteDatabaseAsync(String name)
    
    
    public final OperationFuture<Database,DeleteDatabaseMetadata> deleteDatabaseAsync(String name)

Deletes a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name = DatabaseName.of("[PROJECT]", "[DATABASE]").toString();
       Database response = firestoreAdminClient.deleteDatabaseAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the form `projects/{project_id}/databases/{database_id}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database),[DeleteDatabaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteDatabaseMetadata)>` |   
  
### deleteDatabaseCallable()
    
    
    public final UnaryCallable<DeleteDatabaseRequest,Operation> deleteDatabaseCallable()

Deletes a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DeleteDatabaseRequest request =
           DeleteDatabaseRequest.newBuilder()
               .setName(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future =
           firestoreAdminClient.deleteDatabaseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDatabaseOperationCallable()
    
    
    public final OperationCallable<DeleteDatabaseRequest,Database,DeleteDatabaseMetadata> deleteDatabaseOperationCallable()

Deletes a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DeleteDatabaseRequest request =
           DeleteDatabaseRequest.newBuilder()
               .setName(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .setEtag("etag3123477")
               .build();
       OperationFuture<Database, DeleteDatabaseMetadata> future =
           firestoreAdminClient.deleteDatabaseOperationCallable().futureCall(request);
       // Do something.
       Database response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteDatabaseRequest),[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database),[DeleteDatabaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteDatabaseMetadata)>` |   
  
### deleteIndex(@Nullable IndexName name)
    
    
    public final void deleteIndex(@Nullable IndexName name)

Deletes a composite index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       IndexName name = IndexName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]", "[INDEX]");
       firestoreAdminClient.deleteIndex(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.IndexName`  
Required. A name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{index_id}`  
  
### deleteIndex(DeleteIndexRequest request)
    
    
    public final void deleteIndex(DeleteIndexRequest request)

Deletes a composite index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DeleteIndexRequest request =
           DeleteIndexRequest.newBuilder()
               .setName(
                   IndexName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]", "[INDEX]").toString())
               .build();
       firestoreAdminClient.deleteIndex(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteIndexRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteIndex(String name)
    
    
    public final void deleteIndex(String name)

Deletes a composite index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name = IndexName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]", "[INDEX]").toString();
       firestoreAdminClient.deleteIndex(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{index_id}`  
  
### deleteIndexCallable()
    
    
    public final UnaryCallable<DeleteIndexRequest,Empty> deleteIndexCallable()

Deletes a composite index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DeleteIndexRequest request =
           DeleteIndexRequest.newBuilder()
               .setName(
                   IndexName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]", "[INDEX]").toString())
               .build();
       ApiFuture<Empty> future = firestoreAdminClient.deleteIndexCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteIndexRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteUserCreds(@Nullable UserCredsName name)
    
    
    public final void deleteUserCreds(@Nullable UserCredsName name)

Deletes a user creds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       UserCredsName name = UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]");
       firestoreAdminClient.deleteUserCreds(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.UserCredsName`  
Required. A name of the form `projects/{project_id}/databases/{database_id}/userCreds/{user_creds_id}`  
  
### deleteUserCreds(DeleteUserCredsRequest request)
    
    
    public final void deleteUserCreds(DeleteUserCredsRequest request)

Deletes a user creds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DeleteUserCredsRequest request =
           DeleteUserCredsRequest.newBuilder()
               .setName(UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]").toString())
               .build();
       firestoreAdminClient.deleteUserCreds(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteUserCredsRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteUserCreds(String name)
    
    
    public final void deleteUserCreds(String name)

Deletes a user creds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name = UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]").toString();
       firestoreAdminClient.deleteUserCreds(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the form `projects/{project_id}/databases/{database_id}/userCreds/{user_creds_id}`  
  
### deleteUserCredsCallable()
    
    
    public final UnaryCallable<DeleteUserCredsRequest,Empty> deleteUserCredsCallable()

Deletes a user creds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DeleteUserCredsRequest request =
           DeleteUserCredsRequest.newBuilder()
               .setName(UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]").toString())
               .build();
       ApiFuture<Empty> future = firestoreAdminClient.deleteUserCredsCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DeleteUserCredsRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### disableUserCreds(@Nullable UserCredsName name)
    
    
    public final UserCreds disableUserCreds(@Nullable UserCredsName name)

Disables a user creds. No-op if the user creds are already disabled.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       UserCredsName name = UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]");
       UserCreds response = firestoreAdminClient.disableUserCreds(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.UserCredsName`  
Required. A name of the form `projects/{project_id}/databases/{database_id}/userCreds/{user_creds_id}`  
**Returns**  
---  
**Type** | **Description**  
`[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)` |   
  
### disableUserCreds(DisableUserCredsRequest request)
    
    
    public final UserCreds disableUserCreds(DisableUserCredsRequest request)

Disables a user creds. No-op if the user creds are already disabled.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DisableUserCredsRequest request =
           DisableUserCredsRequest.newBuilder()
               .setName(UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]").toString())
               .build();
       UserCreds response = firestoreAdminClient.disableUserCreds(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DisableUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DisableUserCredsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)` |   
  
### disableUserCreds(String name)
    
    
    public final UserCreds disableUserCreds(String name)

Disables a user creds. No-op if the user creds are already disabled.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name = UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]").toString();
       UserCreds response = firestoreAdminClient.disableUserCreds(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the form `projects/{project_id}/databases/{database_id}/userCreds/{user_creds_id}`  
**Returns**  
---  
**Type** | **Description**  
`[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)` |   
  
### disableUserCredsCallable()
    
    
    public final UnaryCallable<DisableUserCredsRequest,UserCreds> disableUserCredsCallable()

Disables a user creds. No-op if the user creds are already disabled.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DisableUserCredsRequest request =
           DisableUserCredsRequest.newBuilder()
               .setName(UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]").toString())
               .build();
       ApiFuture<UserCreds> future =
           firestoreAdminClient.disableUserCredsCallable().futureCall(request);
       // Do something.
       UserCreds response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DisableUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.DisableUserCredsRequest),[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)>` |   
  
### enableUserCreds(@Nullable UserCredsName name)
    
    
    public final UserCreds enableUserCreds(@Nullable UserCredsName name)

Enables a user creds. No-op if the user creds are already enabled.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       UserCredsName name = UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]");
       UserCreds response = firestoreAdminClient.enableUserCreds(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.UserCredsName`  
Required. A name of the form `projects/{project_id}/databases/{database_id}/userCreds/{user_creds_id}`  
**Returns**  
---  
**Type** | **Description**  
`[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)` |   
  
### enableUserCreds(EnableUserCredsRequest request)
    
    
    public final UserCreds enableUserCreds(EnableUserCredsRequest request)

Enables a user creds. No-op if the user creds are already enabled.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       EnableUserCredsRequest request =
           EnableUserCredsRequest.newBuilder()
               .setName(UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]").toString())
               .build();
       UserCreds response = firestoreAdminClient.enableUserCreds(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EnableUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.EnableUserCredsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)` |   
  
### enableUserCreds(String name)
    
    
    public final UserCreds enableUserCreds(String name)

Enables a user creds. No-op if the user creds are already enabled.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name = UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]").toString();
       UserCreds response = firestoreAdminClient.enableUserCreds(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the form `projects/{project_id}/databases/{database_id}/userCreds/{user_creds_id}`  
**Returns**  
---  
**Type** | **Description**  
`[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)` |   
  
### enableUserCredsCallable()
    
    
    public final UnaryCallable<EnableUserCredsRequest,UserCreds> enableUserCredsCallable()

Enables a user creds. No-op if the user creds are already enabled.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       EnableUserCredsRequest request =
           EnableUserCredsRequest.newBuilder()
               .setName(UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]").toString())
               .build();
       ApiFuture<UserCreds> future =
           firestoreAdminClient.enableUserCredsCallable().futureCall(request);
       // Do something.
       UserCreds response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[EnableUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.EnableUserCredsRequest),[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)>` |   
  
### exportDocumentsAsync(@Nullable DatabaseName name)
    
    
    public final OperationFuture<ExportDocumentsResponse,ExportDocumentsMetadata> exportDocumentsAsync(@Nullable DatabaseName name)

Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. Recent updates to documents may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage.

For more details on export behavior and output format, refer to: <https://cloud.google.com/firestore/docs/manage-data/export-import>

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DatabaseName name = DatabaseName.of("[PROJECT]", "[DATABASE]");
       ExportDocumentsResponse response = firestoreAdminClient.exportDocumentsAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.DatabaseName`  
Required. Database to export. Should be of the form: `projects/{project_id}/databases/{database_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ExportDocumentsResponse),[ExportDocumentsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ExportDocumentsMetadata)>` |   
  
### exportDocumentsAsync(ExportDocumentsRequest request)
    
    
    public final OperationFuture<ExportDocumentsResponse,ExportDocumentsMetadata> exportDocumentsAsync(ExportDocumentsRequest request)

Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. Recent updates to documents may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage.

For more details on export behavior and output format, refer to: <https://cloud.google.com/firestore/docs/manage-data/export-import>

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ExportDocumentsRequest request =
           ExportDocumentsRequest.newBuilder()
               .setName(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .addAllCollectionIds(new ArrayList<String>())
               .setOutputUriPrefix("outputUriPrefix499858205")
               .addAllNamespaceIds(new ArrayList<String>())
               .setSnapshotTime(Timestamp.newBuilder().build())
               .build();
       ExportDocumentsResponse response = firestoreAdminClient.exportDocumentsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ExportDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ExportDocumentsResponse),[ExportDocumentsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ExportDocumentsMetadata)>` |   
  
### exportDocumentsAsync(String name)
    
    
    public final OperationFuture<ExportDocumentsResponse,ExportDocumentsMetadata> exportDocumentsAsync(String name)

Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. Recent updates to documents may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage.

For more details on export behavior and output format, refer to: <https://cloud.google.com/firestore/docs/manage-data/export-import>

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name = DatabaseName.of("[PROJECT]", "[DATABASE]").toString();
       ExportDocumentsResponse response = firestoreAdminClient.exportDocumentsAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Database to export. Should be of the form: `projects/{project_id}/databases/{database_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ExportDocumentsResponse),[ExportDocumentsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ExportDocumentsMetadata)>` |   
  
### exportDocumentsCallable()
    
    
    public final UnaryCallable<ExportDocumentsRequest,Operation> exportDocumentsCallable()

Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. Recent updates to documents may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage.

For more details on export behavior and output format, refer to: <https://cloud.google.com/firestore/docs/manage-data/export-import>

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ExportDocumentsRequest request =
           ExportDocumentsRequest.newBuilder()
               .setName(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .addAllCollectionIds(new ArrayList<String>())
               .setOutputUriPrefix("outputUriPrefix499858205")
               .addAllNamespaceIds(new ArrayList<String>())
               .setSnapshotTime(Timestamp.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           firestoreAdminClient.exportDocumentsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ExportDocumentsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportDocumentsOperationCallable()
    
    
    public final OperationCallable<ExportDocumentsRequest,ExportDocumentsResponse,ExportDocumentsMetadata> exportDocumentsOperationCallable()

Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. Recent updates to documents may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage.

For more details on export behavior and output format, refer to: <https://cloud.google.com/firestore/docs/manage-data/export-import>

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ExportDocumentsRequest request =
           ExportDocumentsRequest.newBuilder()
               .setName(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .addAllCollectionIds(new ArrayList<String>())
               .setOutputUriPrefix("outputUriPrefix499858205")
               .addAllNamespaceIds(new ArrayList<String>())
               .setSnapshotTime(Timestamp.newBuilder().build())
               .build();
       OperationFuture<ExportDocumentsResponse, ExportDocumentsMetadata> future =
           firestoreAdminClient.exportDocumentsOperationCallable().futureCall(request);
       // Do something.
       ExportDocumentsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ExportDocumentsRequest),[ExportDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ExportDocumentsResponse),[ExportDocumentsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ExportDocumentsMetadata)>` |   
  
### getBackup(@Nullable BackupName name)
    
    
    public final Backup getBackup(@Nullable BackupName name)

Gets information about a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       BackupName name = BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]");
       Backup response = firestoreAdminClient.getBackup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.BackupName`  
Required. Name of the backup to fetch. Format is `projects/{project}/locations/{location}/backups/{backup}`.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Backup)` |   
  
### getBackup(GetBackupRequest request)
    
    
    public final Backup getBackup(GetBackupRequest request)

Gets information about a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       GetBackupRequest request =
           GetBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]").toString())
               .build();
       Backup response = firestoreAdminClient.getBackup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Backup)` |   
  
### getBackup(String name)
    
    
    public final Backup getBackup(String name)

Gets information about a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name = BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]").toString();
       Backup response = firestoreAdminClient.getBackup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the backup to fetch. Format is `projects/{project}/locations/{location}/backups/{backup}`.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Backup)` |   
  
### getBackupCallable()
    
    
    public final UnaryCallable<GetBackupRequest,Backup> getBackupCallable()

Gets information about a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       GetBackupRequest request =
           GetBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]").toString())
               .build();
       ApiFuture<Backup> future = firestoreAdminClient.getBackupCallable().futureCall(request);
       // Do something.
       Backup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Backup)>` |   
  
### getBackupSchedule(@Nullable BackupScheduleName name)
    
    
    public final BackupSchedule getBackupSchedule(@Nullable BackupScheduleName name)

Gets information about a backup schedule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       BackupScheduleName name =
           BackupScheduleName.of("[PROJECT]", "[DATABASE]", "[BACKUP_SCHEDULE]");
       BackupSchedule response = firestoreAdminClient.getBackupSchedule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.BackupScheduleName`  
Required. The name of the backup schedule. Format `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`  
**Returns**  
---  
**Type** | **Description**  
`[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)` |   
  
### getBackupSchedule(GetBackupScheduleRequest request)
    
    
    public final BackupSchedule getBackupSchedule(GetBackupScheduleRequest request)

Gets information about a backup schedule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       GetBackupScheduleRequest request =
           GetBackupScheduleRequest.newBuilder()
               .setName(
                   BackupScheduleName.of("[PROJECT]", "[DATABASE]", "[BACKUP_SCHEDULE]").toString())
               .build();
       BackupSchedule response = firestoreAdminClient.getBackupSchedule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetBackupScheduleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)` |   
  
### getBackupSchedule(String name)
    
    
    public final BackupSchedule getBackupSchedule(String name)

Gets information about a backup schedule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name =
           BackupScheduleName.of("[PROJECT]", "[DATABASE]", "[BACKUP_SCHEDULE]").toString();
       BackupSchedule response = firestoreAdminClient.getBackupSchedule(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the backup schedule. Format `projects/{project}/databases/{database}/backupSchedules/{backup_schedule}`  
**Returns**  
---  
**Type** | **Description**  
`[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)` |   
  
### getBackupScheduleCallable()
    
    
    public final UnaryCallable<GetBackupScheduleRequest,BackupSchedule> getBackupScheduleCallable()

Gets information about a backup schedule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       GetBackupScheduleRequest request =
           GetBackupScheduleRequest.newBuilder()
               .setName(
                   BackupScheduleName.of("[PROJECT]", "[DATABASE]", "[BACKUP_SCHEDULE]").toString())
               .build();
       ApiFuture<BackupSchedule> future =
           firestoreAdminClient.getBackupScheduleCallable().futureCall(request);
       // Do something.
       BackupSchedule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetBackupScheduleRequest),[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)>` |   
  
### getDatabase(@Nullable DatabaseName name)
    
    
    public final Database getDatabase(@Nullable DatabaseName name)

Gets information about a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DatabaseName name = DatabaseName.of("[PROJECT]", "[DATABASE]");
       Database response = firestoreAdminClient.getDatabase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.DatabaseName`  
Required. A name of the form `projects/{project_id}/databases/{database_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database)` |   
  
### getDatabase(GetDatabaseRequest request)
    
    
    public final Database getDatabase(GetDatabaseRequest request)

Gets information about a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       GetDatabaseRequest request =
           GetDatabaseRequest.newBuilder()
               .setName(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .build();
       Database response = firestoreAdminClient.getDatabase(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database)` |   
  
### getDatabase(String name)
    
    
    public final Database getDatabase(String name)

Gets information about a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name = DatabaseName.of("[PROJECT]", "[DATABASE]").toString();
       Database response = firestoreAdminClient.getDatabase(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the form `projects/{project_id}/databases/{database_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database)` |   
  
### getDatabaseCallable()
    
    
    public final UnaryCallable<GetDatabaseRequest,Database> getDatabaseCallable()

Gets information about a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       GetDatabaseRequest request =
           GetDatabaseRequest.newBuilder()
               .setName(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .build();
       ApiFuture<Database> future = firestoreAdminClient.getDatabaseCallable().futureCall(request);
       // Do something.
       Database response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetDatabaseRequest),[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database)>` |   
  
### getField(@Nullable FieldName name)
    
    
    public final Field getField(@Nullable FieldName name)

Gets the metadata and configuration for a Field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       FieldName name = FieldName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]", "[FIELD]");
       Field response = firestoreAdminClient.getField(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.FieldName`  
Required. A name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/fields/{field_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Field](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Field)` |   
  
### getField(GetFieldRequest request)
    
    
    public final Field getField(GetFieldRequest request)

Gets the metadata and configuration for a Field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       GetFieldRequest request =
           GetFieldRequest.newBuilder()
               .setName(
                   FieldName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]", "[FIELD]").toString())
               .build();
       Field response = firestoreAdminClient.getField(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFieldRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetFieldRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Field](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Field)` |   
  
### getField(String name)
    
    
    public final Field getField(String name)

Gets the metadata and configuration for a Field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name = FieldName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]", "[FIELD]").toString();
       Field response = firestoreAdminClient.getField(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/fields/{field_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Field](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Field)` |   
  
### getFieldCallable()
    
    
    public final UnaryCallable<GetFieldRequest,Field> getFieldCallable()

Gets the metadata and configuration for a Field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       GetFieldRequest request =
           GetFieldRequest.newBuilder()
               .setName(
                   FieldName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]", "[FIELD]").toString())
               .build();
       ApiFuture<Field> future = firestoreAdminClient.getFieldCallable().futureCall(request);
       // Do something.
       Field response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFieldRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetFieldRequest),[Field](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Field)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getIndex(@Nullable IndexName name)
    
    
    public final Index getIndex(@Nullable IndexName name)

Gets a composite index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       IndexName name = IndexName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]", "[INDEX]");
       Index response = firestoreAdminClient.getIndex(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.IndexName`  
Required. A name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{index_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index)` |   
  
### getIndex(GetIndexRequest request)
    
    
    public final Index getIndex(GetIndexRequest request)

Gets a composite index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       GetIndexRequest request =
           GetIndexRequest.newBuilder()
               .setName(
                   IndexName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]", "[INDEX]").toString())
               .build();
       Index response = firestoreAdminClient.getIndex(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetIndexRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index)` |   
  
### getIndex(String name)
    
    
    public final Index getIndex(String name)

Gets a composite index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name = IndexName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]", "[INDEX]").toString();
       Index response = firestoreAdminClient.getIndex(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{index_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index)` |   
  
### getIndexCallable()
    
    
    public final UnaryCallable<GetIndexRequest,Index> getIndexCallable()

Gets a composite index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       GetIndexRequest request =
           GetIndexRequest.newBuilder()
               .setName(
                   IndexName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]", "[INDEX]").toString())
               .build();
       ApiFuture<Index> future = firestoreAdminClient.getIndexCallable().futureCall(request);
       // Do something.
       Index response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetIndexRequest),[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index)>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable FirestoreAdminSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.firestore.v1.FirestoreAdminSettings` |   
  
### getStub()
    
    
    public FirestoreAdminStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[FirestoreAdminStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.stub.FirestoreAdminStub)` |   
  
### getUserCreds(@Nullable UserCredsName name)
    
    
    public final UserCreds getUserCreds(@Nullable UserCredsName name)

Gets a user creds resource. Note that the returned resource does not contain the secret value itself.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       UserCredsName name = UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]");
       UserCreds response = firestoreAdminClient.getUserCreds(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.UserCredsName`  
Required. A name of the form `projects/{project_id}/databases/{database_id}/userCreds/{user_creds_id}`  
**Returns**  
---  
**Type** | **Description**  
`[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)` |   
  
### getUserCreds(GetUserCredsRequest request)
    
    
    public final UserCreds getUserCreds(GetUserCredsRequest request)

Gets a user creds resource. Note that the returned resource does not contain the secret value itself.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       GetUserCredsRequest request =
           GetUserCredsRequest.newBuilder()
               .setName(UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]").toString())
               .build();
       UserCreds response = firestoreAdminClient.getUserCreds(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetUserCredsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)` |   
  
### getUserCreds(String name)
    
    
    public final UserCreds getUserCreds(String name)

Gets a user creds resource. Note that the returned resource does not contain the secret value itself.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name = UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]").toString();
       UserCreds response = firestoreAdminClient.getUserCreds(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the form `projects/{project_id}/databases/{database_id}/userCreds/{user_creds_id}`  
**Returns**  
---  
**Type** | **Description**  
`[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)` |   
  
### getUserCredsCallable()
    
    
    public final UnaryCallable<GetUserCredsRequest,UserCreds> getUserCredsCallable()

Gets a user creds resource. Note that the returned resource does not contain the secret value itself.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       GetUserCredsRequest request =
           GetUserCredsRequest.newBuilder()
               .setName(UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]").toString())
               .build();
       ApiFuture<UserCreds> future = firestoreAdminClient.getUserCredsCallable().futureCall(request);
       // Do something.
       UserCreds response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.GetUserCredsRequest),[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)>` |   
  
### importDocumentsAsync(@Nullable DatabaseName name)
    
    
    public final OperationFuture<Empty,ImportDocumentsMetadata> importDocumentsAsync(@Nullable DatabaseName name)

Imports documents into Google Cloud Firestore. Existing documents with the same name are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportDocuments operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Firestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DatabaseName name = DatabaseName.of("[PROJECT]", "[DATABASE]");
       firestoreAdminClient.importDocumentsAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.DatabaseName`  
Required. Database to import into. Should be of the form: `projects/{project_id}/databases/{database_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[ImportDocumentsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ImportDocumentsMetadata)>` |   
  
### importDocumentsAsync(ImportDocumentsRequest request)
    
    
    public final OperationFuture<Empty,ImportDocumentsMetadata> importDocumentsAsync(ImportDocumentsRequest request)

Imports documents into Google Cloud Firestore. Existing documents with the same name are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportDocuments operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Firestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ImportDocumentsRequest request =
           ImportDocumentsRequest.newBuilder()
               .setName(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .addAllCollectionIds(new ArrayList<String>())
               .setInputUriPrefix("inputUriPrefix-97481100")
               .addAllNamespaceIds(new ArrayList<String>())
               .build();
       firestoreAdminClient.importDocumentsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ImportDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[ImportDocumentsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ImportDocumentsMetadata)>` |   
  
### importDocumentsAsync(String name)
    
    
    public final OperationFuture<Empty,ImportDocumentsMetadata> importDocumentsAsync(String name)

Imports documents into Google Cloud Firestore. Existing documents with the same name are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportDocuments operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Firestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name = DatabaseName.of("[PROJECT]", "[DATABASE]").toString();
       firestoreAdminClient.importDocumentsAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Database to import into. Should be of the form: `projects/{project_id}/databases/{database_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[ImportDocumentsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ImportDocumentsMetadata)>` |   
  
### importDocumentsCallable()
    
    
    public final UnaryCallable<ImportDocumentsRequest,Operation> importDocumentsCallable()

Imports documents into Google Cloud Firestore. Existing documents with the same name are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportDocuments operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Firestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ImportDocumentsRequest request =
           ImportDocumentsRequest.newBuilder()
               .setName(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .addAllCollectionIds(new ArrayList<String>())
               .setInputUriPrefix("inputUriPrefix-97481100")
               .addAllNamespaceIds(new ArrayList<String>())
               .build();
       ApiFuture<Operation> future =
           firestoreAdminClient.importDocumentsCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ImportDocumentsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importDocumentsOperationCallable()
    
    
    public final OperationCallable<ImportDocumentsRequest,Empty,ImportDocumentsMetadata> importDocumentsOperationCallable()

Imports documents into Google Cloud Firestore. Existing documents with the same name are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportDocuments operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Firestore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ImportDocumentsRequest request =
           ImportDocumentsRequest.newBuilder()
               .setName(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .addAllCollectionIds(new ArrayList<String>())
               .setInputUriPrefix("inputUriPrefix-97481100")
               .addAllNamespaceIds(new ArrayList<String>())
               .build();
       OperationFuture<Empty, ImportDocumentsMetadata> future =
           firestoreAdminClient.importDocumentsOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ImportDocumentsRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[ImportDocumentsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ImportDocumentsMetadata)>` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listBackupSchedules(@Nullable DatabaseName parent)
    
    
    public final ListBackupSchedulesResponse listBackupSchedules(@Nullable DatabaseName parent)

List backup schedules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DatabaseName parent = DatabaseName.of("[PROJECT]", "[DATABASE]");
       ListBackupSchedulesResponse response = firestoreAdminClient.listBackupSchedules(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.DatabaseName`  
Required. The parent database. Format is `projects/{project}/databases/{database}`.  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupSchedulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListBackupSchedulesResponse)` |   
  
### listBackupSchedules(ListBackupSchedulesRequest request)
    
    
    public final ListBackupSchedulesResponse listBackupSchedules(ListBackupSchedulesRequest request)

List backup schedules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ListBackupSchedulesRequest request =
           ListBackupSchedulesRequest.newBuilder()
               .setParent(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .build();
       ListBackupSchedulesResponse response = firestoreAdminClient.listBackupSchedules(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupSchedulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListBackupSchedulesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupSchedulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListBackupSchedulesResponse)` |   
  
### listBackupSchedules(String parent)
    
    
    public final ListBackupSchedulesResponse listBackupSchedules(String parent)

List backup schedules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String parent = DatabaseName.of("[PROJECT]", "[DATABASE]").toString();
       ListBackupSchedulesResponse response = firestoreAdminClient.listBackupSchedules(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent database. Format is `projects/{project}/databases/{database}`.  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupSchedulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListBackupSchedulesResponse)` |   
  
### listBackupSchedulesCallable()
    
    
    public final UnaryCallable<ListBackupSchedulesRequest,ListBackupSchedulesResponse> listBackupSchedulesCallable()

List backup schedules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ListBackupSchedulesRequest request =
           ListBackupSchedulesRequest.newBuilder()
               .setParent(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .build();
       ApiFuture<ListBackupSchedulesResponse> future =
           firestoreAdminClient.listBackupSchedulesCallable().futureCall(request);
       // Do something.
       ListBackupSchedulesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupSchedulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListBackupSchedulesRequest),[ListBackupSchedulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListBackupSchedulesResponse)>` |   
  
### listBackups(@Nullable LocationName parent)
    
    
    public final ListBackupsResponse listBackups(@Nullable LocationName parent)

Lists all the backups.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ListBackupsResponse response = firestoreAdminClient.listBackups(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.LocationName`  
Required. The location to list backups from. Format is `projects/{project}/locations/{location}`. Use `{location} = '-'` to list backups from all locations for the given project. This allows listing backups from a single location or from all locations.  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListBackupsResponse)` |   
  
### listBackups(ListBackupsRequest request)
    
    
    public final ListBackupsResponse listBackups(ListBackupsRequest request)

Lists all the backups.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .build();
       ListBackupsResponse response = firestoreAdminClient.listBackups(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListBackupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListBackupsResponse)` |   
  
### listBackups(String parent)
    
    
    public final ListBackupsResponse listBackups(String parent)

Lists all the backups.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ListBackupsResponse response = firestoreAdminClient.listBackups(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The location to list backups from. Format is `projects/{project}/locations/{location}`. Use `{location} = '-'` to list backups from all locations for the given project. This allows listing backups from a single location or from all locations.  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListBackupsResponse)` |   
  
### listBackupsCallable()
    
    
    public final UnaryCallable<ListBackupsRequest,ListBackupsResponse> listBackupsCallable()

Lists all the backups.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<ListBackupsResponse> future =
           firestoreAdminClient.listBackupsCallable().futureCall(request);
       // Do something.
       ListBackupsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListBackupsRequest),[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListBackupsResponse)>` |   
  
### listDatabases(@Nullable ProjectName parent)
    
    
    public final ListDatabasesResponse listDatabases(@Nullable ProjectName parent)

List all the databases in the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       ListDatabasesResponse response = firestoreAdminClient.listDatabases(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.ProjectName`  
Required. A parent name of the form `projects/{project_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ListDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListDatabasesResponse)` |   
  
### listDatabases(ListDatabasesRequest request)
    
    
    public final ListDatabasesResponse listDatabases(ListDatabasesRequest request)

List all the databases in the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ListDatabasesRequest request =
           ListDatabasesRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setShowDeleted(true)
               .build();
       ListDatabasesResponse response = firestoreAdminClient.listDatabases(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListDatabasesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ListDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListDatabasesResponse)` |   
  
### listDatabases(String parent)
    
    
    public final ListDatabasesResponse listDatabases(String parent)

List all the databases in the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       ListDatabasesResponse response = firestoreAdminClient.listDatabases(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A parent name of the form `projects/{project_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ListDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListDatabasesResponse)` |   
  
### listDatabasesCallable()
    
    
    public final UnaryCallable<ListDatabasesRequest,ListDatabasesResponse> listDatabasesCallable()

List all the databases in the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ListDatabasesRequest request =
           ListDatabasesRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setShowDeleted(true)
               .build();
       ApiFuture<ListDatabasesResponse> future =
           firestoreAdminClient.listDatabasesCallable().futureCall(request);
       // Do something.
       ListDatabasesResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDatabasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListDatabasesRequest),[ListDatabasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListDatabasesResponse)>` |   
  
### listFields(@Nullable CollectionGroupName parent)
    
    
    public final FirestoreAdminClient.ListFieldsPagedResponse listFields(@Nullable CollectionGroupName parent)

Lists the field configuration and metadata for this database.

Currently, FirestoreAdmin.ListFields only supports listing fields that have been explicitly overridden. To issue this query, call FirestoreAdmin.ListFields with the filter set to `indexConfig.usesAncestorConfig:false` or `ttlConfig:*`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       CollectionGroupName parent =
           CollectionGroupName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]");
       for (Field element : firestoreAdminClient.listFields(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.CollectionGroupName`  
Required. A parent name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}`  
**Returns**  
---  
**Type** | **Description**  
`[FirestoreAdminClient.ListFieldsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.FirestoreAdminClient.ListFieldsPagedResponse)` |   
  
### listFields(ListFieldsRequest request)
    
    
    public final FirestoreAdminClient.ListFieldsPagedResponse listFields(ListFieldsRequest request)

Lists the field configuration and metadata for this database.

Currently, FirestoreAdmin.ListFields only supports listing fields that have been explicitly overridden. To issue this query, call FirestoreAdmin.ListFields with the filter set to `indexConfig.usesAncestorConfig:false` or `ttlConfig:*`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ListFieldsRequest request =
           ListFieldsRequest.newBuilder()
               .setParent(
                   CollectionGroupName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Field element : firestoreAdminClient.listFields(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFieldsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListFieldsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirestoreAdminClient.ListFieldsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.FirestoreAdminClient.ListFieldsPagedResponse)` |   
  
### listFields(String parent)
    
    
    public final FirestoreAdminClient.ListFieldsPagedResponse listFields(String parent)

Lists the field configuration and metadata for this database.

Currently, FirestoreAdmin.ListFields only supports listing fields that have been explicitly overridden. To issue this query, call FirestoreAdmin.ListFields with the filter set to `indexConfig.usesAncestorConfig:false` or `ttlConfig:*`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String parent = CollectionGroupName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]").toString();
       for (Field element : firestoreAdminClient.listFields(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A parent name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}`  
**Returns**  
---  
**Type** | **Description**  
`[FirestoreAdminClient.ListFieldsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.FirestoreAdminClient.ListFieldsPagedResponse)` |   
  
### listFieldsCallable()
    
    
    public final UnaryCallable<ListFieldsRequest,ListFieldsResponse> listFieldsCallable()

Lists the field configuration and metadata for this database.

Currently, FirestoreAdmin.ListFields only supports listing fields that have been explicitly overridden. To issue this query, call FirestoreAdmin.ListFields with the filter set to `indexConfig.usesAncestorConfig:false` or `ttlConfig:*`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ListFieldsRequest request =
           ListFieldsRequest.newBuilder()
               .setParent(
                   CollectionGroupName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListFieldsResponse response = firestoreAdminClient.listFieldsCallable().call(request);
         for (Field element : response.getFieldsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFieldsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListFieldsRequest),[ListFieldsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListFieldsResponse)>` |   
  
### listFieldsPagedCallable()
    
    
    public final UnaryCallable<ListFieldsRequest,FirestoreAdminClient.ListFieldsPagedResponse> listFieldsPagedCallable()

Lists the field configuration and metadata for this database.

Currently, FirestoreAdmin.ListFields only supports listing fields that have been explicitly overridden. To issue this query, call FirestoreAdmin.ListFields with the filter set to `indexConfig.usesAncestorConfig:false` or `ttlConfig:*`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ListFieldsRequest request =
           ListFieldsRequest.newBuilder()
               .setParent(
                   CollectionGroupName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Field> future = firestoreAdminClient.listFieldsPagedCallable().futureCall(request);
       // Do something.
       for (Field element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFieldsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListFieldsRequest),[ListFieldsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.FirestoreAdminClient.ListFieldsPagedResponse)>` |   
  
### listIndexes(@Nullable CollectionGroupName parent)
    
    
    public final FirestoreAdminClient.ListIndexesPagedResponse listIndexes(@Nullable CollectionGroupName parent)

Lists composite indexes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       CollectionGroupName parent =
           CollectionGroupName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]");
       for (Index element : firestoreAdminClient.listIndexes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.CollectionGroupName`  
Required. A parent name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}`  
**Returns**  
---  
**Type** | **Description**  
`[FirestoreAdminClient.ListIndexesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.FirestoreAdminClient.ListIndexesPagedResponse)` |   
  
### listIndexes(ListIndexesRequest request)
    
    
    public final FirestoreAdminClient.ListIndexesPagedResponse listIndexes(ListIndexesRequest request)

Lists composite indexes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ListIndexesRequest request =
           ListIndexesRequest.newBuilder()
               .setParent(
                   CollectionGroupName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Index element : firestoreAdminClient.listIndexes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListIndexesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListIndexesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FirestoreAdminClient.ListIndexesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.FirestoreAdminClient.ListIndexesPagedResponse)` |   
  
### listIndexes(String parent)
    
    
    public final FirestoreAdminClient.ListIndexesPagedResponse listIndexes(String parent)

Lists composite indexes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String parent = CollectionGroupName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]").toString();
       for (Index element : firestoreAdminClient.listIndexes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A parent name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}`  
**Returns**  
---  
**Type** | **Description**  
`[FirestoreAdminClient.ListIndexesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.FirestoreAdminClient.ListIndexesPagedResponse)` |   
  
### listIndexesCallable()
    
    
    public final UnaryCallable<ListIndexesRequest,ListIndexesResponse> listIndexesCallable()

Lists composite indexes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ListIndexesRequest request =
           ListIndexesRequest.newBuilder()
               .setParent(
                   CollectionGroupName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListIndexesResponse response = firestoreAdminClient.listIndexesCallable().call(request);
         for (Index element : response.getIndexesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListIndexesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListIndexesRequest),[ListIndexesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListIndexesResponse)>` |   
  
### listIndexesPagedCallable()
    
    
    public final UnaryCallable<ListIndexesRequest,FirestoreAdminClient.ListIndexesPagedResponse> listIndexesPagedCallable()

Lists composite indexes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ListIndexesRequest request =
           ListIndexesRequest.newBuilder()
               .setParent(
                   CollectionGroupName.of("[PROJECT]", "[DATABASE]", "[COLLECTION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Index> future = firestoreAdminClient.listIndexesPagedCallable().futureCall(request);
       // Do something.
       for (Index element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListIndexesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListIndexesRequest),[ListIndexesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.cloud.firestore.v1.FirestoreAdminClient.ListIndexesPagedResponse)>` |   
  
### listUserCreds(@Nullable DatabaseName parent)
    
    
    public final ListUserCredsResponse listUserCreds(@Nullable DatabaseName parent)

List all user creds in the database. Note that the returned resource does not contain the secret value itself.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       DatabaseName parent = DatabaseName.of("[PROJECT]", "[DATABASE]");
       ListUserCredsResponse response = firestoreAdminClient.listUserCreds(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.DatabaseName`  
Required. A parent database name of the form `projects/{project_id}/databases/{database_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ListUserCredsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListUserCredsResponse)` |   
  
### listUserCreds(ListUserCredsRequest request)
    
    
    public final ListUserCredsResponse listUserCreds(ListUserCredsRequest request)

List all user creds in the database. Note that the returned resource does not contain the secret value itself.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ListUserCredsRequest request =
           ListUserCredsRequest.newBuilder()
               .setParent(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .build();
       ListUserCredsResponse response = firestoreAdminClient.listUserCreds(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListUserCredsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ListUserCredsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListUserCredsResponse)` |   
  
### listUserCreds(String parent)
    
    
    public final ListUserCredsResponse listUserCreds(String parent)

List all user creds in the database. Note that the returned resource does not contain the secret value itself.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String parent = DatabaseName.of("[PROJECT]", "[DATABASE]").toString();
       ListUserCredsResponse response = firestoreAdminClient.listUserCreds(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A parent database name of the form `projects/{project_id}/databases/{database_id}`  
**Returns**  
---  
**Type** | **Description**  
`[ListUserCredsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListUserCredsResponse)` |   
  
### listUserCredsCallable()
    
    
    public final UnaryCallable<ListUserCredsRequest,ListUserCredsResponse> listUserCredsCallable()

List all user creds in the database. Note that the returned resource does not contain the secret value itself.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ListUserCredsRequest request =
           ListUserCredsRequest.newBuilder()
               .setParent(DatabaseName.of("[PROJECT]", "[DATABASE]").toString())
               .build();
       ApiFuture<ListUserCredsResponse> future =
           firestoreAdminClient.listUserCredsCallable().futureCall(request);
       // Do something.
       ListUserCredsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUserCredsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListUserCredsRequest),[ListUserCredsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ListUserCredsResponse)>` |   
  
### resetUserPassword(@Nullable UserCredsName name)
    
    
    public final UserCreds resetUserPassword(@Nullable UserCredsName name)

Resets the password of a user creds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       UserCredsName name = UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]");
       UserCreds response = firestoreAdminClient.resetUserPassword(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.firestore.admin.v1.UserCredsName`  
Required. A name of the form `projects/{project_id}/databases/{database_id}/userCreds/{user_creds_id}`  
**Returns**  
---  
**Type** | **Description**  
`[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)` |   
  
### resetUserPassword(ResetUserPasswordRequest request)
    
    
    public final UserCreds resetUserPassword(ResetUserPasswordRequest request)

Resets the password of a user creds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ResetUserPasswordRequest request =
           ResetUserPasswordRequest.newBuilder()
               .setName(UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]").toString())
               .build();
       UserCreds response = firestoreAdminClient.resetUserPassword(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResetUserPasswordRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ResetUserPasswordRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)` |   
  
### resetUserPassword(String name)
    
    
    public final UserCreds resetUserPassword(String name)

Resets the password of a user creds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       String name = UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]").toString();
       UserCreds response = firestoreAdminClient.resetUserPassword(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A name of the form `projects/{project_id}/databases/{database_id}/userCreds/{user_creds_id}`  
**Returns**  
---  
**Type** | **Description**  
`[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)` |   
  
### resetUserPasswordCallable()
    
    
    public final UnaryCallable<ResetUserPasswordRequest,UserCreds> resetUserPasswordCallable()

Resets the password of a user creds.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       ResetUserPasswordRequest request =
           ResetUserPasswordRequest.newBuilder()
               .setName(UserCredsName.of("[PROJECT]", "[DATABASE]", "[USER_CREDS]").toString())
               .build();
       ApiFuture<UserCreds> future =
           firestoreAdminClient.resetUserPasswordCallable().futureCall(request);
       // Do something.
       UserCreds response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResetUserPasswordRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.ResetUserPasswordRequest),[UserCreds](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UserCreds)>` |   
  
### restoreDatabaseAsync(RestoreDatabaseRequest request)
    
    
    public final OperationFuture<Database,RestoreDatabaseMetadata> restoreDatabaseAsync(RestoreDatabaseRequest request)

Creates a new database by restoring from an existing backup.

The new database must be in the same cloud region or multi-region location as the existing backup. This behaves similar to FirestoreAdmin.CreateDatabase except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing backup.

The long-running operation can be used to track the progress of the restore, with the Operation's metadata field type being the RestoreDatabaseMetadata. The response type is the Database if the restore was successful. The new database is not readable or writeable until the LRO has completed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       RestoreDatabaseRequest request =
           RestoreDatabaseRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setDatabaseId("databaseId1688905718")
               .setBackup(BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]").toString())
               .setEncryptionConfig(Database.EncryptionConfig.newBuilder().build())
               .putAllTags(new HashMap<String, String>())
               .build();
       Database response = firestoreAdminClient.restoreDatabaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestoreDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.RestoreDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database),[RestoreDatabaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.RestoreDatabaseMetadata)>` |   
  
### restoreDatabaseCallable()
    
    
    public final UnaryCallable<RestoreDatabaseRequest,Operation> restoreDatabaseCallable()

Creates a new database by restoring from an existing backup.

The new database must be in the same cloud region or multi-region location as the existing backup. This behaves similar to FirestoreAdmin.CreateDatabase except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing backup.

The long-running operation can be used to track the progress of the restore, with the Operation's metadata field type being the RestoreDatabaseMetadata. The response type is the Database if the restore was successful. The new database is not readable or writeable until the LRO has completed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       RestoreDatabaseRequest request =
           RestoreDatabaseRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setDatabaseId("databaseId1688905718")
               .setBackup(BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]").toString())
               .setEncryptionConfig(Database.EncryptionConfig.newBuilder().build())
               .putAllTags(new HashMap<String, String>())
               .build();
       ApiFuture<Operation> future =
           firestoreAdminClient.restoreDatabaseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RestoreDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.RestoreDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### restoreDatabaseOperationCallable()
    
    
    public final OperationCallable<RestoreDatabaseRequest,Database,RestoreDatabaseMetadata> restoreDatabaseOperationCallable()

Creates a new database by restoring from an existing backup.

The new database must be in the same cloud region or multi-region location as the existing backup. This behaves similar to FirestoreAdmin.CreateDatabase except instead of creating a new empty database, a new database is created with the database type, index configuration, and documents from an existing backup.

The long-running operation can be used to track the progress of the restore, with the Operation's metadata field type being the RestoreDatabaseMetadata. The response type is the Database if the restore was successful. The new database is not readable or writeable until the LRO has completed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       RestoreDatabaseRequest request =
           RestoreDatabaseRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setDatabaseId("databaseId1688905718")
               .setBackup(BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP]").toString())
               .setEncryptionConfig(Database.EncryptionConfig.newBuilder().build())
               .putAllTags(new HashMap<String, String>())
               .build();
       OperationFuture<Database, RestoreDatabaseMetadata> future =
           firestoreAdminClient.restoreDatabaseOperationCallable().futureCall(request);
       // Do something.
       Database response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RestoreDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.RestoreDatabaseRequest),[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database),[RestoreDatabaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.RestoreDatabaseMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateBackupSchedule(BackupSchedule backupSchedule, FieldMask updateMask)
    
    
    public final BackupSchedule updateBackupSchedule(BackupSchedule backupSchedule, FieldMask updateMask)

Updates a backup schedule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       BackupSchedule backupSchedule = BackupSchedule.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       BackupSchedule response =
           firestoreAdminClient.updateBackupSchedule(backupSchedule, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`backupSchedule` | `[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)`  
Required. The backup schedule to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields to be updated.  
**Returns**  
---  
**Type** | **Description**  
`[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)` |   
  
### updateBackupSchedule(UpdateBackupScheduleRequest request)
    
    
    public final BackupSchedule updateBackupSchedule(UpdateBackupScheduleRequest request)

Updates a backup schedule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       UpdateBackupScheduleRequest request =
           UpdateBackupScheduleRequest.newBuilder()
               .setBackupSchedule(BackupSchedule.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       BackupSchedule response = firestoreAdminClient.updateBackupSchedule(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UpdateBackupScheduleRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)` |   
  
### updateBackupScheduleCallable()
    
    
    public final UnaryCallable<UpdateBackupScheduleRequest,BackupSchedule> updateBackupScheduleCallable()

Updates a backup schedule.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       UpdateBackupScheduleRequest request =
           UpdateBackupScheduleRequest.newBuilder()
               .setBackupSchedule(BackupSchedule.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<BackupSchedule> future =
           firestoreAdminClient.updateBackupScheduleCallable().futureCall(request);
       // Do something.
       BackupSchedule response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateBackupScheduleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UpdateBackupScheduleRequest),[BackupSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.BackupSchedule)>` |   
  
### updateDatabaseAsync(Database database, FieldMask updateMask)
    
    
    public final OperationFuture<Database,UpdateDatabaseMetadata> updateDatabaseAsync(Database database, FieldMask updateMask)

Updates a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       Database database = Database.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Database response = firestoreAdminClient.updateDatabaseAsync(database, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`database` | `[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database)`  
Required. The database to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields to be updated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database),[UpdateDatabaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UpdateDatabaseMetadata)>` |   
  
### updateDatabaseAsync(UpdateDatabaseRequest request)
    
    
    public final OperationFuture<Database,UpdateDatabaseMetadata> updateDatabaseAsync(UpdateDatabaseRequest request)

Updates a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       UpdateDatabaseRequest request =
           UpdateDatabaseRequest.newBuilder()
               .setDatabase(Database.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Database response = firestoreAdminClient.updateDatabaseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UpdateDatabaseRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database),[UpdateDatabaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UpdateDatabaseMetadata)>` |   
  
### updateDatabaseCallable()
    
    
    public final UnaryCallable<UpdateDatabaseRequest,Operation> updateDatabaseCallable()

Updates a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       UpdateDatabaseRequest request =
           UpdateDatabaseRequest.newBuilder()
               .setDatabase(Database.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           firestoreAdminClient.updateDatabaseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UpdateDatabaseRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateDatabaseOperationCallable()
    
    
    public final OperationCallable<UpdateDatabaseRequest,Database,UpdateDatabaseMetadata> updateDatabaseOperationCallable()

Updates a database.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       UpdateDatabaseRequest request =
           UpdateDatabaseRequest.newBuilder()
               .setDatabase(Database.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<Database, UpdateDatabaseMetadata> future =
           firestoreAdminClient.updateDatabaseOperationCallable().futureCall(request);
       // Do something.
       Database response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateDatabaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UpdateDatabaseRequest),[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Database),[UpdateDatabaseMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UpdateDatabaseMetadata)>` |   
  
### updateFieldAsync(Field field)
    
    
    public final OperationFuture<Field,FieldOperationMetadata> updateFieldAsync(Field field)

Updates a field configuration. Currently, field updates apply only to single field index configuration. However, calls to FirestoreAdmin.UpdateField should provide a field mask to avoid changing any configuration that the caller isn't aware of. The field mask should be specified as: `{ paths: "index_config" }`.

This call returns a google.longrunning.Operation which may be used to track the status of the field update. The metadata for the operation will be the type FieldOperationMetadata.

To configure the default field settings for the database, use the special `Field` with resource name: `projects/{project_id}/databases/{database_id}/collectionGroups/**default** /fields/*`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       Field field = Field.newBuilder().build();
       Field response = firestoreAdminClient.updateFieldAsync(field).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`field` | `[Field](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Field)`  
Required. The field to be updated.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Field](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Field),[FieldOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.FieldOperationMetadata)>` |   
  
### updateFieldAsync(UpdateFieldRequest request)
    
    
    public final OperationFuture<Field,FieldOperationMetadata> updateFieldAsync(UpdateFieldRequest request)

Updates a field configuration. Currently, field updates apply only to single field index configuration. However, calls to FirestoreAdmin.UpdateField should provide a field mask to avoid changing any configuration that the caller isn't aware of. The field mask should be specified as: `{ paths: "index_config" }`.

This call returns a google.longrunning.Operation which may be used to track the status of the field update. The metadata for the operation will be the type FieldOperationMetadata.

To configure the default field settings for the database, use the special `Field` with resource name: `projects/{project_id}/databases/{database_id}/collectionGroups/**default** /fields/*`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       UpdateFieldRequest request =
           UpdateFieldRequest.newBuilder()
               .setField(Field.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Field response = firestoreAdminClient.updateFieldAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFieldRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UpdateFieldRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Field](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Field),[FieldOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.FieldOperationMetadata)>` |   
  
### updateFieldCallable()
    
    
    public final UnaryCallable<UpdateFieldRequest,Operation> updateFieldCallable()

Updates a field configuration. Currently, field updates apply only to single field index configuration. However, calls to FirestoreAdmin.UpdateField should provide a field mask to avoid changing any configuration that the caller isn't aware of. The field mask should be specified as: `{ paths: "index_config" }`.

This call returns a google.longrunning.Operation which may be used to track the status of the field update. The metadata for the operation will be the type FieldOperationMetadata.

To configure the default field settings for the database, use the special `Field` with resource name: `projects/{project_id}/databases/{database_id}/collectionGroups/**default** /fields/*`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       UpdateFieldRequest request =
           UpdateFieldRequest.newBuilder()
               .setField(Field.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future = firestoreAdminClient.updateFieldCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateFieldRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UpdateFieldRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateFieldOperationCallable()
    
    
    public final OperationCallable<UpdateFieldRequest,Field,FieldOperationMetadata> updateFieldOperationCallable()

Updates a field configuration. Currently, field updates apply only to single field index configuration. However, calls to FirestoreAdmin.UpdateField should provide a field mask to avoid changing any configuration that the caller isn't aware of. The field mask should be specified as: `{ paths: "index_config" }`.

This call returns a google.longrunning.Operation which may be used to track the status of the field update. The metadata for the operation will be the type FieldOperationMetadata.

To configure the default field settings for the database, use the special `Field` with resource name: `projects/{project_id}/databases/{database_id}/collectionGroups/**default** /fields/*`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FirestoreAdminClient firestoreAdminClient = FirestoreAdminClient.create()) {
       UpdateFieldRequest request =
           UpdateFieldRequest.newBuilder()
               .setField(Field.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<Field, FieldOperationMetadata> future =
           firestoreAdminClient.updateFieldOperationCallable().futureCall(request);
       // Do something.
       Field response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateFieldRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.UpdateFieldRequest),[Field](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Field),[FieldOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.FieldOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
