---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient
title: Class MemorystoreClient (0.45.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:38.269617+00:00
---

# Class MemorystoreClient (0.45.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MemorystoreClient (0.45.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.45.0 (latest)  0.41.0  0.40.0  0.39.0  0.37.0  0.34.0  0.33.0  0.31.0  0.29.0  0.28.0  0.26.0  0.24.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-valkey/google-cloud-valkey/src/main/java/com/google/cloud/memorystore/v1/MemorystoreClient.java)| [Product Reference](https://cloud.google.com/memorystore/docs/valkey)| [REST Documentation](https://cloud.google.com/memorystore/docs/valkey/reference/rest)  
---|---|---  
  
Service Description: Service describing handlers for resources

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       InstanceName name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       Instance response = memorystoreClient.getInstance(name);
     }
     

Note: close() needs to be called on the MemorystoreClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListInstances |  Lists Instances in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listInstances(ListInstancesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listInstances(LocationName parent) 
  * listInstances(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listInstancesPagedCallable() 
  * listInstancesCallable() 

  
GetInstance |  Gets details of a single Instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getInstance(GetInstanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getInstance(InstanceName name) 
  * getInstance(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getInstanceCallable() 

  
CreateInstance |  Creates a new Instance in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createInstanceAsync(CreateInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createInstanceAsync(LocationName parent, Instance instance, String instanceId) 
  * createInstanceAsync(String parent, Instance instance, String instanceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createInstanceOperationCallable() 
  * createInstanceCallable() 

  
UpdateInstance |  Updates the parameters of a single Instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateInstanceAsync(UpdateInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateInstanceAsync(Instance instance, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateInstanceOperationCallable() 
  * updateInstanceCallable() 

  
DeleteInstance |  Deletes a single Instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteInstanceAsync(DeleteInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteInstanceAsync(InstanceName name) 
  * deleteInstanceAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteInstanceOperationCallable() 
  * deleteInstanceCallable() 

  
GetCertificateAuthority |  Gets details about the certificate authority for an Instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCertificateAuthority(GetCertificateAuthorityRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCertificateAuthority(InstanceName name) 
  * getCertificateAuthority(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCertificateAuthorityCallable() 

  
GetSharedRegionalCertificateAuthority |  Gets the details of shared regional certificate authority information for Memorystore instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSharedRegionalCertificateAuthority(GetSharedRegionalCertificateAuthorityRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSharedRegionalCertificateAuthority(SharedRegionalCertificateAuthorityName name) 
  * getSharedRegionalCertificateAuthority(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSharedRegionalCertificateAuthorityCallable() 

  
RescheduleMaintenance |  Reschedules upcoming maintenance event. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * rescheduleMaintenanceAsync(RescheduleMaintenanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * rescheduleMaintenanceAsync(InstanceName name, RescheduleMaintenanceRequest.RescheduleType rescheduleType, Timestamp scheduleTime) 
  * rescheduleMaintenanceAsync(String name, RescheduleMaintenanceRequest.RescheduleType rescheduleType, Timestamp scheduleTime) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * rescheduleMaintenanceOperationCallable() 
  * rescheduleMaintenanceCallable() 

  
ListBackupCollections |  Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.  If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBackupCollections(ListBackupCollectionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBackupCollections(LocationName parent) 
  * listBackupCollections(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBackupCollectionsPagedCallable() 
  * listBackupCollectionsCallable() 

  
GetBackupCollection |  Get a backup collection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBackupCollection(GetBackupCollectionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBackupCollection(BackupCollectionName name) 
  * getBackupCollection(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBackupCollectionCallable() 

  
ListBackups |  Lists all backups owned by a backup collection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBackups(ListBackupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBackups(BackupCollectionName parent) 
  * listBackups(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBackupsPagedCallable() 
  * listBackupsCallable() 

  
GetBackup |  Gets the details of a specific backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBackup(GetBackupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBackup(BackupName name) 
  * getBackup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBackupCallable() 

  
DeleteBackup |  Deletes a specific backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBackupAsync(DeleteBackupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteBackupAsync(BackupName name) 
  * deleteBackupAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBackupOperationCallable() 
  * deleteBackupCallable() 

  
ExportBackup |  Exports a specific backup to a customer target Cloud Storage URI. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportBackupAsync(ExportBackupRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportBackupOperationCallable() 
  * exportBackupCallable() 

  
BackupInstance |  Backup Instance. If this is the first time a backup is being created, a backup collection will be created at the backend, and this backup belongs to this collection. Both collection and backup will have a resource name. Backup will be executed for each shard. A replica (primary if nonHA) will be selected to perform the execution. Backup call will be rejected if there is an ongoing backup or update operation. Be aware that during preview, if the instance's internal software version is too old, critical update will be performed before actual backup. Once the internal software version is updated to the minimum version required by the backup feature, subsequent backups will not require critical update. After preview, there will be no critical update needed for backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * backupInstanceAsync(BackupInstanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * backupInstanceAsync(InstanceName name) 
  * backupInstanceAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * backupInstanceOperationCallable() 
  * backupInstanceCallable() 

  
StartMigration |  Initiates the migration of a source instance to the target Memorystore instance.  After the successful completion of this operation, the target instance will: 1. Set up replication with the source instance and replicate any writes to the source instance. 2. Only allow reads. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * startMigrationAsync(StartMigrationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * startMigrationOperationCallable() 
  * startMigrationCallable() 

  
FinishMigration |  Finalizes the migration process.  After the successful completion of this operation, the target instance will: 1. Stop replicating from the source instance. 2. Allow both reads and writes. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * finishMigrationAsync(FinishMigrationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * finishMigrationAsync(InstanceName name, boolean force) 
  * finishMigrationAsync(String name, boolean force) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * finishMigrationOperationCallable() 
  * finishMigrationCallable() 

  
ListTokenAuthUsers |  Lists all the token auth users for a token based auth enabled instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTokenAuthUsers(ListTokenAuthUsersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTokenAuthUsers(InstanceName parent) 
  * listTokenAuthUsers(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTokenAuthUsersPagedCallable() 
  * listTokenAuthUsersCallable() 

  
GetTokenAuthUser |  Gets a specific token auth user for a token based auth enabled instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTokenAuthUser(GetTokenAuthUserRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTokenAuthUser(TokenAuthUserName name) 
  * getTokenAuthUser(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTokenAuthUserCallable() 

  
ListAuthTokens |  Lists all the auth tokens for a specific token auth user. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAuthTokens(ListAuthTokensRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAuthTokens(TokenAuthUserName parent) 
  * listAuthTokens(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAuthTokensPagedCallable() 
  * listAuthTokensCallable() 

  
GetAuthToken |  Gets a token based auth enabled instance's auth token for a given user. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAuthToken(GetAuthTokenRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAuthToken(AuthTokenName name) 
  * getAuthToken(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAuthTokenCallable() 

  
AddTokenAuthUser |  Adds a token auth user for a token based auth enabled instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addTokenAuthUserAsync(AddTokenAuthUserRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addTokenAuthUserAsync(InstanceName instance, String tokenAuthUser) 
  * addTokenAuthUserAsync(String instance, String tokenAuthUser) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addTokenAuthUserOperationCallable() 
  * addTokenAuthUserCallable() 

  
DeleteTokenAuthUser |  Deletes a token auth user for a token based auth enabled instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTokenAuthUserAsync(DeleteTokenAuthUserRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteTokenAuthUserAsync(TokenAuthUserName name) 
  * deleteTokenAuthUserAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTokenAuthUserOperationCallable() 
  * deleteTokenAuthUserCallable() 

  
AddAuthToken |  Adds a token for a user of a token based auth enabled instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addAuthTokenAsync(AddAuthTokenRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addAuthTokenAsync(TokenAuthUserName tokenAuthUser, AuthToken authToken) 
  * addAuthTokenAsync(String tokenAuthUser, AuthToken authToken) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addAuthTokenOperationCallable() 
  * addAuthTokenCallable() 

  
DeleteAuthToken |  Deletes a token for a user of a token based auth enabled instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAuthTokenAsync(DeleteAuthTokenRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAuthTokenAsync(AuthTokenName name) 
  * deleteAuthTokenAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAuthTokenOperationCallable() 
  * deleteAuthTokenCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of MemorystoreSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MemorystoreSettings memorystoreSettings =
         MemorystoreSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     MemorystoreClient memorystoreClient = MemorystoreClient.create(memorystoreSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MemorystoreSettings memorystoreSettings =
         MemorystoreSettings.newBuilder().setEndpoint(myEndpoint).build();
     MemorystoreClient memorystoreClient = MemorystoreClient.create(memorystoreSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     MemorystoreSettings memorystoreSettings = MemorystoreSettings.newHttpJsonBuilder().build();
     MemorystoreClient memorystoreClient = MemorystoreClient.create(memorystoreSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > MemorystoreClient

## Static Methods 

### create()
    
    
    public static final MemorystoreClient create()

Constructs an instance of MemorystoreClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MemorystoreSettings settings)
    
    
    public static final MemorystoreClient create(MemorystoreSettings settings)

Constructs an instance of MemorystoreClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MemorystoreSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(MemorystoreStub stub)
    
    
    public static final MemorystoreClient create(MemorystoreStub stub)

Constructs an instance of MemorystoreClient, using the given stub for making calls. This is for advanced usage - prefer using create(MemorystoreSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MemorystoreStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.stub.MemorystoreStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient)` |   
  
## Constructors 

### MemorystoreClient(MemorystoreSettings settings)
    
    
    protected MemorystoreClient(MemorystoreSettings settings)

Constructs an instance of MemorystoreClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[MemorystoreSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreSettings)`  
  
  
### MemorystoreClient(MemorystoreStub stub)
    
    
    protected MemorystoreClient(MemorystoreStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[MemorystoreStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.stub.MemorystoreStub)`  
  
  
## Methods 

### addAuthTokenAsync(@Nullable TokenAuthUserName tokenAuthUser, AuthToken authToken)
    
    
    public final OperationFuture<TokenAuthUser,OperationMetadata> addAuthTokenAsync(@Nullable TokenAuthUserName tokenAuthUser, AuthToken authToken)

Adds a token for a user of a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       TokenAuthUserName tokenAuthUser =
           TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]");
       AuthToken authToken = AuthToken.newBuilder().build();
       TokenAuthUser response = memorystoreClient.addAuthTokenAsync(tokenAuthUser, authToken).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tokenAuthUser` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.TokenAuthUserName`  
Required. The name of the token auth user resource that this token will be added for.  
`authToken` | `[AuthToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AuthToken)`  
Required. The auth token to add.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TokenAuthUser](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.TokenAuthUser),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### addAuthTokenAsync(AddAuthTokenRequest request)
    
    
    public final OperationFuture<TokenAuthUser,OperationMetadata> addAuthTokenAsync(AddAuthTokenRequest request)

Adds a token for a user of a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       AddAuthTokenRequest request =
           AddAuthTokenRequest.newBuilder()
               .setTokenAuthUser(
                   TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]")
                       .toString())
               .setAuthToken(AuthToken.newBuilder().build())
               .build();
       TokenAuthUser response = memorystoreClient.addAuthTokenAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddAuthTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AddAuthTokenRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TokenAuthUser](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.TokenAuthUser),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### addAuthTokenAsync(String tokenAuthUser, AuthToken authToken)
    
    
    public final OperationFuture<TokenAuthUser,OperationMetadata> addAuthTokenAsync(String tokenAuthUser, AuthToken authToken)

Adds a token for a user of a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String tokenAuthUser =
           TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]")
               .toString();
       AuthToken authToken = AuthToken.newBuilder().build();
       TokenAuthUser response = memorystoreClient.addAuthTokenAsync(tokenAuthUser, authToken).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`tokenAuthUser` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the token auth user resource that this token will be added for.  
`authToken` | `[AuthToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AuthToken)`  
Required. The auth token to add.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[TokenAuthUser](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.TokenAuthUser),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### addAuthTokenCallable()
    
    
    public final UnaryCallable<AddAuthTokenRequest,Operation> addAuthTokenCallable()

Adds a token for a user of a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       AddAuthTokenRequest request =
           AddAuthTokenRequest.newBuilder()
               .setTokenAuthUser(
                   TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]")
                       .toString())
               .setAuthToken(AuthToken.newBuilder().build())
               .build();
       ApiFuture<Operation> future = memorystoreClient.addAuthTokenCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddAuthTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AddAuthTokenRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### addAuthTokenOperationCallable()
    
    
    public final OperationCallable<AddAuthTokenRequest,TokenAuthUser,OperationMetadata> addAuthTokenOperationCallable()

Adds a token for a user of a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       AddAuthTokenRequest request =
           AddAuthTokenRequest.newBuilder()
               .setTokenAuthUser(
                   TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]")
                       .toString())
               .setAuthToken(AuthToken.newBuilder().build())
               .build();
       OperationFuture<TokenAuthUser, OperationMetadata> future =
           memorystoreClient.addAuthTokenOperationCallable().futureCall(request);
       // Do something.
       TokenAuthUser response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddAuthTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AddAuthTokenRequest),[TokenAuthUser](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.TokenAuthUser),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### addTokenAuthUserAsync(@Nullable InstanceName instance, String tokenAuthUser)
    
    
    public final OperationFuture<Instance,OperationMetadata> addTokenAuthUserAsync(@Nullable InstanceName instance, String tokenAuthUser)

Adds a token auth user for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       InstanceName instance = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       String tokenAuthUser = "tokenAuthUser345456300";
       Instance response = memorystoreClient.addTokenAuthUserAsync(instance, tokenAuthUser).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`instance` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.InstanceName`  
Required. The instance resource that this token auth user will be added for. Format: projects/{project}/locations/{location}/instances/{instance}  
`tokenAuthUser` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the token auth user to add.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### addTokenAuthUserAsync(AddTokenAuthUserRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> addTokenAuthUserAsync(AddTokenAuthUserRequest request)

Adds a token auth user for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       AddTokenAuthUserRequest request =
           AddTokenAuthUserRequest.newBuilder()
               .setInstance(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setTokenAuthUser("tokenAuthUser345456300")
               .build();
       Instance response = memorystoreClient.addTokenAuthUserAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddTokenAuthUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AddTokenAuthUserRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### addTokenAuthUserAsync(String instance, String tokenAuthUser)
    
    
    public final OperationFuture<Instance,OperationMetadata> addTokenAuthUserAsync(String instance, String tokenAuthUser)

Adds a token auth user for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String instance = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       String tokenAuthUser = "tokenAuthUser345456300";
       Instance response = memorystoreClient.addTokenAuthUserAsync(instance, tokenAuthUser).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The instance resource that this token auth user will be added for. Format: projects/{project}/locations/{location}/instances/{instance}  
`tokenAuthUser` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the token auth user to add.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### addTokenAuthUserCallable()
    
    
    public final UnaryCallable<AddTokenAuthUserRequest,Operation> addTokenAuthUserCallable()

Adds a token auth user for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       AddTokenAuthUserRequest request =
           AddTokenAuthUserRequest.newBuilder()
               .setInstance(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setTokenAuthUser("tokenAuthUser345456300")
               .build();
       ApiFuture<Operation> future =
           memorystoreClient.addTokenAuthUserCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddTokenAuthUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AddTokenAuthUserRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### addTokenAuthUserOperationCallable()
    
    
    public final OperationCallable<AddTokenAuthUserRequest,Instance,OperationMetadata> addTokenAuthUserOperationCallable()

Adds a token auth user for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       AddTokenAuthUserRequest request =
           AddTokenAuthUserRequest.newBuilder()
               .setInstance(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setTokenAuthUser("tokenAuthUser345456300")
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           memorystoreClient.addTokenAuthUserOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddTokenAuthUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AddTokenAuthUserRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
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
  
### backupInstanceAsync(@Nullable InstanceName name)
    
    
    public final OperationFuture<Instance,OperationMetadata> backupInstanceAsync(@Nullable InstanceName name)

Backup Instance. If this is the first time a backup is being created, a backup collection will be created at the backend, and this backup belongs to this collection. Both collection and backup will have a resource name. Backup will be executed for each shard. A replica (primary if nonHA) will be selected to perform the execution. Backup call will be rejected if there is an ongoing backup or update operation. Be aware that during preview, if the instance's internal software version is too old, critical update will be performed before actual backup. Once the internal software version is updated to the minimum version required by the backup feature, subsequent backups will not require critical update. After preview, there will be no critical update needed for backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       InstanceName name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       Instance response = memorystoreClient.backupInstanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.InstanceName`  
Required. Instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### backupInstanceAsync(BackupInstanceRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> backupInstanceAsync(BackupInstanceRequest request)

Backup Instance. If this is the first time a backup is being created, a backup collection will be created at the backend, and this backup belongs to this collection. Both collection and backup will have a resource name. Backup will be executed for each shard. A replica (primary if nonHA) will be selected to perform the execution. Backup call will be rejected if there is an ongoing backup or update operation. Be aware that during preview, if the instance's internal software version is too old, critical update will be performed before actual backup. Once the internal software version is updated to the minimum version required by the backup feature, subsequent backups will not require critical update. After preview, there will be no critical update needed for backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       BackupInstanceRequest request =
           BackupInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setTtl(Duration.newBuilder().build())
               .setBackupId("backupId2121930365")
               .build();
       Instance response = memorystoreClient.backupInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BackupInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.BackupInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### backupInstanceAsync(String name)
    
    
    public final OperationFuture<Instance,OperationMetadata> backupInstanceAsync(String name)

Backup Instance. If this is the first time a backup is being created, a backup collection will be created at the backend, and this backup belongs to this collection. Both collection and backup will have a resource name. Backup will be executed for each shard. A replica (primary if nonHA) will be selected to perform the execution. Backup call will be rejected if there is an ongoing backup or update operation. Be aware that during preview, if the instance's internal software version is too old, critical update will be performed before actual backup. Once the internal software version is updated to the minimum version required by the backup feature, subsequent backups will not require critical update. After preview, there will be no critical update needed for backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       Instance response = memorystoreClient.backupInstanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### backupInstanceCallable()
    
    
    public final UnaryCallable<BackupInstanceRequest,Operation> backupInstanceCallable()

Backup Instance. If this is the first time a backup is being created, a backup collection will be created at the backend, and this backup belongs to this collection. Both collection and backup will have a resource name. Backup will be executed for each shard. A replica (primary if nonHA) will be selected to perform the execution. Backup call will be rejected if there is an ongoing backup or update operation. Be aware that during preview, if the instance's internal software version is too old, critical update will be performed before actual backup. Once the internal software version is updated to the minimum version required by the backup feature, subsequent backups will not require critical update. After preview, there will be no critical update needed for backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       BackupInstanceRequest request =
           BackupInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setTtl(Duration.newBuilder().build())
               .setBackupId("backupId2121930365")
               .build();
       ApiFuture<Operation> future = memorystoreClient.backupInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BackupInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.BackupInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### backupInstanceOperationCallable()
    
    
    public final OperationCallable<BackupInstanceRequest,Instance,OperationMetadata> backupInstanceOperationCallable()

Backup Instance. If this is the first time a backup is being created, a backup collection will be created at the backend, and this backup belongs to this collection. Both collection and backup will have a resource name. Backup will be executed for each shard. A replica (primary if nonHA) will be selected to perform the execution. Backup call will be rejected if there is an ongoing backup or update operation. Be aware that during preview, if the instance's internal software version is too old, critical update will be performed before actual backup. Once the internal software version is updated to the minimum version required by the backup feature, subsequent backups will not require critical update. After preview, there will be no critical update needed for backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       BackupInstanceRequest request =
           BackupInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setTtl(Duration.newBuilder().build())
               .setBackupId("backupId2121930365")
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           memorystoreClient.backupInstanceOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BackupInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.BackupInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### close()
    
    
    public final void close()

### createInstanceAsync(@Nullable LocationName parent, Instance instance, String instanceId)
    
    
    public final OperationFuture<Instance,OperationMetadata> createInstanceAsync(@Nullable LocationName parent, Instance instance, String instanceId)

Creates a new Instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Instance instance = Instance.newBuilder().build();
       String instanceId = "instanceId902024336";
       Instance response = memorystoreClient.createInstanceAsync(parent, instance, instanceId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.LocationName`  
Required. The parent resource where this instance will be created. Format: projects/{project}/locations/{location}  
`instance` | `[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance)`  
Required. The instance to create.  
`instanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the instance, which will become the final component of the instance's resource name. This value is subject to the following restrictions: 

  * Must be 4-63 characters in length 
  * Must begin with a letter or digit 
  * Must contain only lowercase letters, digits, and hyphens 
  * Must not end with a hyphen 
  * Must be unique within a location 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### createInstanceAsync(CreateInstanceRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> createInstanceAsync(CreateInstanceRequest request)

Creates a new Instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       CreateInstanceRequest request =
           CreateInstanceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setInstanceId("instanceId902024336")
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Instance response = memorystoreClient.createInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CreateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### createInstanceAsync(String parent, Instance instance, String instanceId)
    
    
    public final OperationFuture<Instance,OperationMetadata> createInstanceAsync(String parent, Instance instance, String instanceId)

Creates a new Instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Instance instance = Instance.newBuilder().build();
       String instanceId = "instanceId902024336";
       Instance response = memorystoreClient.createInstanceAsync(parent, instance, instanceId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this instance will be created. Format: projects/{project}/locations/{location}  
`instance` | `[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance)`  
Required. The instance to create.  
`instanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the instance, which will become the final component of the instance's resource name. This value is subject to the following restrictions: 

  * Must be 4-63 characters in length 
  * Must begin with a letter or digit 
  * Must contain only lowercase letters, digits, and hyphens 
  * Must not end with a hyphen 
  * Must be unique within a location 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### createInstanceCallable()
    
    
    public final UnaryCallable<CreateInstanceRequest,Operation> createInstanceCallable()

Creates a new Instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       CreateInstanceRequest request =
           CreateInstanceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setInstanceId("instanceId902024336")
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = memorystoreClient.createInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CreateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createInstanceOperationCallable()
    
    
    public final OperationCallable<CreateInstanceRequest,Instance,OperationMetadata> createInstanceOperationCallable()

Creates a new Instance in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       CreateInstanceRequest request =
           CreateInstanceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setInstanceId("instanceId902024336")
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           memorystoreClient.createInstanceOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CreateInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### deleteAuthTokenAsync(@Nullable AuthTokenName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAuthTokenAsync(@Nullable AuthTokenName name)

Deletes a token for a user of a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       AuthTokenName name =
           AuthTokenName.of(
               "[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]", "[AUTH_TOKEN]");
       memorystoreClient.deleteAuthTokenAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.AuthTokenName`  
Required. The name of the token auth user resource that this token will be deleted from. Format: projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user}/authTokens/{name}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### deleteAuthTokenAsync(DeleteAuthTokenRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAuthTokenAsync(DeleteAuthTokenRequest request)

Deletes a token for a user of a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       DeleteAuthTokenRequest request =
           DeleteAuthTokenRequest.newBuilder()
               .setName(
                   AuthTokenName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[INSTANCE]",
                           "[TOKEN_AUTH_USER]",
                           "[AUTH_TOKEN]")
                       .toString())
               .build();
       memorystoreClient.deleteAuthTokenAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteAuthTokenRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### deleteAuthTokenAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAuthTokenAsync(String name)

Deletes a token for a user of a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String name =
           AuthTokenName.of(
                   "[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]", "[AUTH_TOKEN]")
               .toString();
       memorystoreClient.deleteAuthTokenAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the token auth user resource that this token will be deleted from. Format: projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user}/authTokens/{name}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### deleteAuthTokenCallable()
    
    
    public final UnaryCallable<DeleteAuthTokenRequest,Operation> deleteAuthTokenCallable()

Deletes a token for a user of a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       DeleteAuthTokenRequest request =
           DeleteAuthTokenRequest.newBuilder()
               .setName(
                   AuthTokenName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[INSTANCE]",
                           "[TOKEN_AUTH_USER]",
                           "[AUTH_TOKEN]")
                       .toString())
               .build();
       ApiFuture<Operation> future = memorystoreClient.deleteAuthTokenCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAuthTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteAuthTokenRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAuthTokenOperationCallable()
    
    
    public final OperationCallable<DeleteAuthTokenRequest,Empty,OperationMetadata> deleteAuthTokenOperationCallable()

Deletes a token for a user of a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       DeleteAuthTokenRequest request =
           DeleteAuthTokenRequest.newBuilder()
               .setName(
                   AuthTokenName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[INSTANCE]",
                           "[TOKEN_AUTH_USER]",
                           "[AUTH_TOKEN]")
                       .toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           memorystoreClient.deleteAuthTokenOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteAuthTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteAuthTokenRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### deleteBackupAsync(@Nullable BackupName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupAsync(@Nullable BackupName name)

Deletes a specific backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       BackupName name = BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]", "[BACKUP]");
       memorystoreClient.deleteBackupAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.BackupName`  
Required. Instance backup resource name using the form: `projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}/backups/{backup_id}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### deleteBackupAsync(DeleteBackupRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupAsync(DeleteBackupRequest request)

Deletes a specific backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       DeleteBackupRequest request =
           DeleteBackupRequest.newBuilder()
               .setName(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]", "[BACKUP]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       memorystoreClient.deleteBackupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### deleteBackupAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteBackupAsync(String name)

Deletes a specific backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String name =
           BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]", "[BACKUP]").toString();
       memorystoreClient.deleteBackupAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Instance backup resource name using the form: `projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}/backups/{backup_id}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### deleteBackupCallable()
    
    
    public final UnaryCallable<DeleteBackupRequest,Operation> deleteBackupCallable()

Deletes a specific backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       DeleteBackupRequest request =
           DeleteBackupRequest.newBuilder()
               .setName(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]", "[BACKUP]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = memorystoreClient.deleteBackupCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteBackupOperationCallable()
    
    
    public final OperationCallable<DeleteBackupRequest,Empty,OperationMetadata> deleteBackupOperationCallable()

Deletes a specific backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       DeleteBackupRequest request =
           DeleteBackupRequest.newBuilder()
               .setName(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]", "[BACKUP]")
                       .toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           memorystoreClient.deleteBackupOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteBackupRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### deleteInstanceAsync(@Nullable InstanceName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInstanceAsync(@Nullable InstanceName name)

Deletes a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       InstanceName name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       memorystoreClient.deleteInstanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.InstanceName`  
Required. The name of the instance to delete. Format: projects/{project}/locations/{location}/instances/{instance}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### deleteInstanceAsync(DeleteInstanceRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInstanceAsync(DeleteInstanceRequest request)

Deletes a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       DeleteInstanceRequest request =
           DeleteInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .build();
       memorystoreClient.deleteInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### deleteInstanceAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteInstanceAsync(String name)

Deletes a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       memorystoreClient.deleteInstanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the instance to delete. Format: projects/{project}/locations/{location}/instances/{instance}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### deleteInstanceCallable()
    
    
    public final UnaryCallable<DeleteInstanceRequest,Operation> deleteInstanceCallable()

Deletes a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       DeleteInstanceRequest request =
           DeleteInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = memorystoreClient.deleteInstanceCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteInstanceOperationCallable()
    
    
    public final OperationCallable<DeleteInstanceRequest,Empty,OperationMetadata> deleteInstanceOperationCallable()

Deletes a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       DeleteInstanceRequest request =
           DeleteInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           memorystoreClient.deleteInstanceOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteInstanceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### deleteTokenAuthUserAsync(@Nullable TokenAuthUserName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteTokenAuthUserAsync(@Nullable TokenAuthUserName name)

Deletes a token auth user for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       TokenAuthUserName name =
           TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]");
       memorystoreClient.deleteTokenAuthUserAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.TokenAuthUserName`  
Required. The name of the token auth user to delete. Format: projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### deleteTokenAuthUserAsync(DeleteTokenAuthUserRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteTokenAuthUserAsync(DeleteTokenAuthUserRequest request)

Deletes a token auth user for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       DeleteTokenAuthUserRequest request =
           DeleteTokenAuthUserRequest.newBuilder()
               .setName(
                   TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]")
                       .toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       memorystoreClient.deleteTokenAuthUserAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTokenAuthUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteTokenAuthUserRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### deleteTokenAuthUserAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteTokenAuthUserAsync(String name)

Deletes a token auth user for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String name =
           TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]")
               .toString();
       memorystoreClient.deleteTokenAuthUserAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the token auth user to delete. Format: projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user}  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### deleteTokenAuthUserCallable()
    
    
    public final UnaryCallable<DeleteTokenAuthUserRequest,Operation> deleteTokenAuthUserCallable()

Deletes a token auth user for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       DeleteTokenAuthUserRequest request =
           DeleteTokenAuthUserRequest.newBuilder()
               .setName(
                   TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]")
                       .toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           memorystoreClient.deleteTokenAuthUserCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTokenAuthUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteTokenAuthUserRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTokenAuthUserOperationCallable()
    
    
    public final OperationCallable<DeleteTokenAuthUserRequest,Empty,OperationMetadata> deleteTokenAuthUserOperationCallable()

Deletes a token auth user for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       DeleteTokenAuthUserRequest request =
           DeleteTokenAuthUserRequest.newBuilder()
               .setName(
                   TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]")
                       .toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           memorystoreClient.deleteTokenAuthUserOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTokenAuthUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.DeleteTokenAuthUserRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### exportBackupAsync(ExportBackupRequest request)
    
    
    public final OperationFuture<Backup,OperationMetadata> exportBackupAsync(ExportBackupRequest request)

Exports a specific backup to a customer target Cloud Storage URI.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ExportBackupRequest request =
           ExportBackupRequest.newBuilder()
               .setName(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]", "[BACKUP]")
                       .toString())
               .build();
       Backup response = memorystoreClient.exportBackupAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ExportBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### exportBackupCallable()
    
    
    public final UnaryCallable<ExportBackupRequest,Operation> exportBackupCallable()

Exports a specific backup to a customer target Cloud Storage URI.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ExportBackupRequest request =
           ExportBackupRequest.newBuilder()
               .setName(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]", "[BACKUP]")
                       .toString())
               .build();
       ApiFuture<Operation> future = memorystoreClient.exportBackupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ExportBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportBackupOperationCallable()
    
    
    public final OperationCallable<ExportBackupRequest,Backup,OperationMetadata> exportBackupOperationCallable()

Exports a specific backup to a customer target Cloud Storage URI.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ExportBackupRequest request =
           ExportBackupRequest.newBuilder()
               .setName(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]", "[BACKUP]")
                       .toString())
               .build();
       OperationFuture<Backup, OperationMetadata> future =
           memorystoreClient.exportBackupOperationCallable().futureCall(request);
       // Do something.
       Backup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ExportBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Backup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### finishMigrationAsync(@Nullable InstanceName name, boolean force)
    
    
    public final OperationFuture<Instance,OperationMetadata> finishMigrationAsync(@Nullable InstanceName name, boolean force)

Finalizes the migration process.

After the successful completion of this operation, the target instance will: 1. Stop replicating from the source instance. 2. Allow both reads and writes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       InstanceName name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       boolean force = true;
       Instance response = memorystoreClient.finishMigrationAsync(name, force).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.InstanceName`  
Required. The resource name of the instance to finalize migration on. Format: projects/{project}/locations/{location}/instances/{instance}  
`force` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Optional. By default, the `FinishMigration` operation ensures the target replication offset to catch up to the source offset as of the time of the call. Set this field to `true` to bypass this offset verification check.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### finishMigrationAsync(FinishMigrationRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> finishMigrationAsync(FinishMigrationRequest request)

Finalizes the migration process.

After the successful completion of this operation, the target instance will: 1. Stop replicating from the source instance. 2. Allow both reads and writes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       FinishMigrationRequest request =
           FinishMigrationRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setForce(true)
               .build();
       Instance response = memorystoreClient.finishMigrationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FinishMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.FinishMigrationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### finishMigrationAsync(String name, boolean force)
    
    
    public final OperationFuture<Instance,OperationMetadata> finishMigrationAsync(String name, boolean force)

Finalizes the migration process.

After the successful completion of this operation, the target instance will: 1. Stop replicating from the source instance. 2. Allow both reads and writes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       boolean force = true;
       Instance response = memorystoreClient.finishMigrationAsync(name, force).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the instance to finalize migration on. Format: projects/{project}/locations/{location}/instances/{instance}  
`force` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Optional. By default, the `FinishMigration` operation ensures the target replication offset to catch up to the source offset as of the time of the call. Set this field to `true` to bypass this offset verification check.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### finishMigrationCallable()
    
    
    public final UnaryCallable<FinishMigrationRequest,Operation> finishMigrationCallable()

Finalizes the migration process.

After the successful completion of this operation, the target instance will: 1. Stop replicating from the source instance. 2. Allow both reads and writes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       FinishMigrationRequest request =
           FinishMigrationRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setForce(true)
               .build();
       ApiFuture<Operation> future = memorystoreClient.finishMigrationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FinishMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.FinishMigrationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### finishMigrationOperationCallable()
    
    
    public final OperationCallable<FinishMigrationRequest,Instance,OperationMetadata> finishMigrationOperationCallable()

Finalizes the migration process.

After the successful completion of this operation, the target instance will: 1. Stop replicating from the source instance. 2. Allow both reads and writes.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       FinishMigrationRequest request =
           FinishMigrationRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setForce(true)
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           memorystoreClient.finishMigrationOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[FinishMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.FinishMigrationRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### getAuthToken(@Nullable AuthTokenName name)
    
    
    public final AuthToken getAuthToken(@Nullable AuthTokenName name)

Gets a token based auth enabled instance's auth token for a given user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       AuthTokenName name =
           AuthTokenName.of(
               "[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]", "[AUTH_TOKEN]");
       AuthToken response = memorystoreClient.getAuthToken(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.AuthTokenName`  
Required. The name of token auth user for a token auth enabled instance. Format: projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user}/authTokens/{auth_token}  
**Returns**  
---  
**Type** | **Description**  
`[AuthToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AuthToken)` |   
  
### getAuthToken(GetAuthTokenRequest request)
    
    
    public final AuthToken getAuthToken(GetAuthTokenRequest request)

Gets a token based auth enabled instance's auth token for a given user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       GetAuthTokenRequest request =
           GetAuthTokenRequest.newBuilder()
               .setName(
                   AuthTokenName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[INSTANCE]",
                           "[TOKEN_AUTH_USER]",
                           "[AUTH_TOKEN]")
                       .toString())
               .build();
       AuthToken response = memorystoreClient.getAuthToken(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAuthTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetAuthTokenRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AuthToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AuthToken)` |   
  
### getAuthToken(String name)
    
    
    public final AuthToken getAuthToken(String name)

Gets a token based auth enabled instance's auth token for a given user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String name =
           AuthTokenName.of(
                   "[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]", "[AUTH_TOKEN]")
               .toString();
       AuthToken response = memorystoreClient.getAuthToken(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of token auth user for a token auth enabled instance. Format: projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user}/authTokens/{auth_token}  
**Returns**  
---  
**Type** | **Description**  
`[AuthToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AuthToken)` |   
  
### getAuthTokenCallable()
    
    
    public final UnaryCallable<GetAuthTokenRequest,AuthToken> getAuthTokenCallable()

Gets a token based auth enabled instance's auth token for a given user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       GetAuthTokenRequest request =
           GetAuthTokenRequest.newBuilder()
               .setName(
                   AuthTokenName.of(
                           "[PROJECT]",
                           "[LOCATION]",
                           "[INSTANCE]",
                           "[TOKEN_AUTH_USER]",
                           "[AUTH_TOKEN]")
                       .toString())
               .build();
       ApiFuture<AuthToken> future = memorystoreClient.getAuthTokenCallable().futureCall(request);
       // Do something.
       AuthToken response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAuthTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetAuthTokenRequest),[AuthToken](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.AuthToken)>` |   
  
### getBackup(@Nullable BackupName name)
    
    
    public final Backup getBackup(@Nullable BackupName name)

Gets the details of a specific backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       BackupName name = BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]", "[BACKUP]");
       Backup response = memorystoreClient.getBackup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.BackupName`  
Required. Instance backup resource name using the form: `projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}/backups/{backup_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Backup)` |   
  
### getBackup(GetBackupRequest request)
    
    
    public final Backup getBackup(GetBackupRequest request)

Gets the details of a specific backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       GetBackupRequest request =
           GetBackupRequest.newBuilder()
               .setName(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]", "[BACKUP]")
                       .toString())
               .build();
       Backup response = memorystoreClient.getBackup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Backup)` |   
  
### getBackup(String name)
    
    
    public final Backup getBackup(String name)

Gets the details of a specific backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String name =
           BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]", "[BACKUP]").toString();
       Backup response = memorystoreClient.getBackup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Instance backup resource name using the form: `projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}/backups/{backup_id}`  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Backup)` |   
  
### getBackupCallable()
    
    
    public final UnaryCallable<GetBackupRequest,Backup> getBackupCallable()

Gets the details of a specific backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       GetBackupRequest request =
           GetBackupRequest.newBuilder()
               .setName(
                   BackupName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]", "[BACKUP]")
                       .toString())
               .build();
       ApiFuture<Backup> future = memorystoreClient.getBackupCallable().futureCall(request);
       // Do something.
       Backup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Backup)>` |   
  
### getBackupCollection(@Nullable BackupCollectionName name)
    
    
    public final BackupCollection getBackupCollection(@Nullable BackupCollectionName name)

Get a backup collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       BackupCollectionName name =
           BackupCollectionName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]");
       BackupCollection response = memorystoreClient.getBackupCollection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.BackupCollectionName`  
Required. Instance backupCollection resource name using the form: `projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}` where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[BackupCollection](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.BackupCollection)` |   
  
### getBackupCollection(GetBackupCollectionRequest request)
    
    
    public final BackupCollection getBackupCollection(GetBackupCollectionRequest request)

Get a backup collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       GetBackupCollectionRequest request =
           GetBackupCollectionRequest.newBuilder()
               .setName(
                   BackupCollectionName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]")
                       .toString())
               .build();
       BackupCollection response = memorystoreClient.getBackupCollection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupCollectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetBackupCollectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupCollection](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.BackupCollection)` |   
  
### getBackupCollection(String name)
    
    
    public final BackupCollection getBackupCollection(String name)

Get a backup collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String name =
           BackupCollectionName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]").toString();
       BackupCollection response = memorystoreClient.getBackupCollection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Instance backupCollection resource name using the form: `projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}` where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[BackupCollection](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.BackupCollection)` |   
  
### getBackupCollectionCallable()
    
    
    public final UnaryCallable<GetBackupCollectionRequest,BackupCollection> getBackupCollectionCallable()

Get a backup collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       GetBackupCollectionRequest request =
           GetBackupCollectionRequest.newBuilder()
               .setName(
                   BackupCollectionName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]")
                       .toString())
               .build();
       ApiFuture<BackupCollection> future =
           memorystoreClient.getBackupCollectionCallable().futureCall(request);
       // Do something.
       BackupCollection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBackupCollectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetBackupCollectionRequest),[BackupCollection](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.BackupCollection)>` |   
  
### getCertificateAuthority(@Nullable InstanceName name)
    
    
    public final CertificateAuthority getCertificateAuthority(@Nullable InstanceName name)

Gets details about the certificate authority for an Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       InstanceName name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       CertificateAuthority response = memorystoreClient.getCertificateAuthority(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.InstanceName`  
Required. The name of the certificate authority. Format: projects/{project}/locations/{location}/instances/{instance}/certificateAuthority  
**Returns**  
---  
**Type** | **Description**  
`[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CertificateAuthority)` |   
  
### getCertificateAuthority(GetCertificateAuthorityRequest request)
    
    
    public final CertificateAuthority getCertificateAuthority(GetCertificateAuthorityRequest request)

Gets details about the certificate authority for an Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       GetCertificateAuthorityRequest request =
           GetCertificateAuthorityRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       CertificateAuthority response = memorystoreClient.getCertificateAuthority(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetCertificateAuthorityRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CertificateAuthority)` |   
  
### getCertificateAuthority(String name)
    
    
    public final CertificateAuthority getCertificateAuthority(String name)

Gets details about the certificate authority for an Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       CertificateAuthority response = memorystoreClient.getCertificateAuthority(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the certificate authority. Format: projects/{project}/locations/{location}/instances/{instance}/certificateAuthority  
**Returns**  
---  
**Type** | **Description**  
`[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CertificateAuthority)` |   
  
### getCertificateAuthorityCallable()
    
    
    public final UnaryCallable<GetCertificateAuthorityRequest,CertificateAuthority> getCertificateAuthorityCallable()

Gets details about the certificate authority for an Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       GetCertificateAuthorityRequest request =
           GetCertificateAuthorityRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       ApiFuture<CertificateAuthority> future =
           memorystoreClient.getCertificateAuthorityCallable().futureCall(request);
       // Do something.
       CertificateAuthority response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetCertificateAuthorityRequest),[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.CertificateAuthority)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getInstance(@Nullable InstanceName name)
    
    
    public final Instance getInstance(@Nullable InstanceName name)

Gets details of a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       InstanceName name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       Instance response = memorystoreClient.getInstance(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.InstanceName`  
Required. The name of the instance to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance)` |   
  
### getInstance(GetInstanceRequest request)
    
    
    public final Instance getInstance(GetInstanceRequest request)

Gets details of a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       GetInstanceRequest request =
           GetInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       Instance response = memorystoreClient.getInstance(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance)` |   
  
### getInstance(String name)
    
    
    public final Instance getInstance(String name)

Gets details of a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       Instance response = memorystoreClient.getInstance(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the instance to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance)` |   
  
### getInstanceCallable()
    
    
    public final UnaryCallable<GetInstanceRequest,Instance> getInstanceCallable()

Gets details of a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       GetInstanceRequest request =
           GetInstanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       ApiFuture<Instance> future = memorystoreClient.getInstanceCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = memorystoreClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = memorystoreClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable MemorystoreSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.MemorystoreSettings` |   
  
### getSharedRegionalCertificateAuthority(@Nullable SharedRegionalCertificateAuthorityName name)
    
    
    public final SharedRegionalCertificateAuthority getSharedRegionalCertificateAuthority(@Nullable SharedRegionalCertificateAuthorityName name)

Gets the details of shared regional certificate authority information for Memorystore instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       SharedRegionalCertificateAuthorityName name =
           SharedRegionalCertificateAuthorityName.of("[PROJECT]", "[LOCATION]");
       SharedRegionalCertificateAuthority response =
           memorystoreClient.getSharedRegionalCertificateAuthority(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.SharedRegionalCertificateAuthorityName`  
Required. Regional certificate authority resource name using the form: `projects/{project}/locations/{location}/sharedRegionalCertificateAuthority` where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.SharedRegionalCertificateAuthority)` |   
  
### getSharedRegionalCertificateAuthority(GetSharedRegionalCertificateAuthorityRequest request)
    
    
    public final SharedRegionalCertificateAuthority getSharedRegionalCertificateAuthority(GetSharedRegionalCertificateAuthorityRequest request)

Gets the details of shared regional certificate authority information for Memorystore instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       GetSharedRegionalCertificateAuthorityRequest request =
           GetSharedRegionalCertificateAuthorityRequest.newBuilder()
               .setName(
                   SharedRegionalCertificateAuthorityName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       SharedRegionalCertificateAuthority response =
           memorystoreClient.getSharedRegionalCertificateAuthority(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetSharedRegionalCertificateAuthorityRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.SharedRegionalCertificateAuthority)` |   
  
### getSharedRegionalCertificateAuthority(String name)
    
    
    public final SharedRegionalCertificateAuthority getSharedRegionalCertificateAuthority(String name)

Gets the details of shared regional certificate authority information for Memorystore instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String name = SharedRegionalCertificateAuthorityName.of("[PROJECT]", "[LOCATION]").toString();
       SharedRegionalCertificateAuthority response =
           memorystoreClient.getSharedRegionalCertificateAuthority(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Regional certificate authority resource name using the form: `projects/{project}/locations/{location}/sharedRegionalCertificateAuthority` where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.SharedRegionalCertificateAuthority)` |   
  
### getSharedRegionalCertificateAuthorityCallable()
    
    
    public final UnaryCallable<GetSharedRegionalCertificateAuthorityRequest,SharedRegionalCertificateAuthority> getSharedRegionalCertificateAuthorityCallable()

Gets the details of shared regional certificate authority information for Memorystore instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       GetSharedRegionalCertificateAuthorityRequest request =
           GetSharedRegionalCertificateAuthorityRequest.newBuilder()
               .setName(
                   SharedRegionalCertificateAuthorityName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<SharedRegionalCertificateAuthority> future =
           memorystoreClient.getSharedRegionalCertificateAuthorityCallable().futureCall(request);
       // Do something.
       SharedRegionalCertificateAuthority response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetSharedRegionalCertificateAuthorityRequest),[SharedRegionalCertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.SharedRegionalCertificateAuthority)>` |   
  
### getStub()
    
    
    public MemorystoreStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[MemorystoreStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.stub.MemorystoreStub)` |   
  
### getTokenAuthUser(@Nullable TokenAuthUserName name)
    
    
    public final TokenAuthUser getTokenAuthUser(@Nullable TokenAuthUserName name)

Gets a specific token auth user for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       TokenAuthUserName name =
           TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]");
       TokenAuthUser response = memorystoreClient.getTokenAuthUser(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.TokenAuthUserName`  
Required. The name of token auth user for a basic auth enabled instance. Format: projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user}  
**Returns**  
---  
**Type** | **Description**  
`[TokenAuthUser](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.TokenAuthUser)` |   
  
### getTokenAuthUser(GetTokenAuthUserRequest request)
    
    
    public final TokenAuthUser getTokenAuthUser(GetTokenAuthUserRequest request)

Gets a specific token auth user for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       GetTokenAuthUserRequest request =
           GetTokenAuthUserRequest.newBuilder()
               .setName(
                   TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]")
                       .toString())
               .build();
       TokenAuthUser response = memorystoreClient.getTokenAuthUser(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTokenAuthUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetTokenAuthUserRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TokenAuthUser](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.TokenAuthUser)` |   
  
### getTokenAuthUser(String name)
    
    
    public final TokenAuthUser getTokenAuthUser(String name)

Gets a specific token auth user for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String name =
           TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]")
               .toString();
       TokenAuthUser response = memorystoreClient.getTokenAuthUser(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of token auth user for a basic auth enabled instance. Format: projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user}  
**Returns**  
---  
**Type** | **Description**  
`[TokenAuthUser](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.TokenAuthUser)` |   
  
### getTokenAuthUserCallable()
    
    
    public final UnaryCallable<GetTokenAuthUserRequest,TokenAuthUser> getTokenAuthUserCallable()

Gets a specific token auth user for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       GetTokenAuthUserRequest request =
           GetTokenAuthUserRequest.newBuilder()
               .setName(
                   TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]")
                       .toString())
               .build();
       ApiFuture<TokenAuthUser> future =
           memorystoreClient.getTokenAuthUserCallable().futureCall(request);
       // Do something.
       TokenAuthUser response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTokenAuthUserRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.GetTokenAuthUserRequest),[TokenAuthUser](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.TokenAuthUser)>` |   
  
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
  
### listAuthTokens(@Nullable TokenAuthUserName parent)
    
    
    public final MemorystoreClient.ListAuthTokensPagedResponse listAuthTokens(@Nullable TokenAuthUserName parent)

Lists all the auth tokens for a specific token auth user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       TokenAuthUserName parent =
           TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]");
       for (AuthToken element : memorystoreClient.listAuthTokens(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.TokenAuthUserName`  
Required. The parent to list auth tokens from. Format: projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user}  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient.ListAuthTokensPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListAuthTokensPagedResponse)` |   
  
### listAuthTokens(ListAuthTokensRequest request)
    
    
    public final MemorystoreClient.ListAuthTokensPagedResponse listAuthTokens(ListAuthTokensRequest request)

Lists all the auth tokens for a specific token auth user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListAuthTokensRequest request =
           ListAuthTokensRequest.newBuilder()
               .setParent(
                   TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (AuthToken element : memorystoreClient.listAuthTokens(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAuthTokensRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListAuthTokensRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient.ListAuthTokensPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListAuthTokensPagedResponse)` |   
  
### listAuthTokens(String parent)
    
    
    public final MemorystoreClient.ListAuthTokensPagedResponse listAuthTokens(String parent)

Lists all the auth tokens for a specific token auth user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String parent =
           TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]")
               .toString();
       for (AuthToken element : memorystoreClient.listAuthTokens(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent to list auth tokens from. Format: projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user}  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient.ListAuthTokensPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListAuthTokensPagedResponse)` |   
  
### listAuthTokensCallable()
    
    
    public final UnaryCallable<ListAuthTokensRequest,ListAuthTokensResponse> listAuthTokensCallable()

Lists all the auth tokens for a specific token auth user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListAuthTokensRequest request =
           ListAuthTokensRequest.newBuilder()
               .setParent(
                   TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListAuthTokensResponse response = memorystoreClient.listAuthTokensCallable().call(request);
         for (AuthToken element : response.getAuthTokensList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAuthTokensRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListAuthTokensRequest),[ListAuthTokensResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListAuthTokensResponse)>` |   
  
### listAuthTokensPagedCallable()
    
    
    public final UnaryCallable<ListAuthTokensRequest,MemorystoreClient.ListAuthTokensPagedResponse> listAuthTokensPagedCallable()

Lists all the auth tokens for a specific token auth user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListAuthTokensRequest request =
           ListAuthTokensRequest.newBuilder()
               .setParent(
                   TokenAuthUserName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]", "[TOKEN_AUTH_USER]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<AuthToken> future =
           memorystoreClient.listAuthTokensPagedCallable().futureCall(request);
       // Do something.
       for (AuthToken element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAuthTokensRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListAuthTokensRequest),[ListAuthTokensPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListAuthTokensPagedResponse)>` |   
  
### listBackupCollections(@Nullable LocationName parent)
    
    
    public final MemorystoreClient.ListBackupCollectionsPagedResponse listBackupCollections(@Nullable LocationName parent)

Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.

If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (BackupCollection element :
           memorystoreClient.listBackupCollections(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.LocationName`  
Required. The resource name of the backupCollection location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient.ListBackupCollectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListBackupCollectionsPagedResponse)` |   
  
### listBackupCollections(ListBackupCollectionsRequest request)
    
    
    public final MemorystoreClient.ListBackupCollectionsPagedResponse listBackupCollections(ListBackupCollectionsRequest request)

Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.

If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListBackupCollectionsRequest request =
           ListBackupCollectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (BackupCollection element :
           memorystoreClient.listBackupCollections(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupCollectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListBackupCollectionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient.ListBackupCollectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListBackupCollectionsPagedResponse)` |   
  
### listBackupCollections(String parent)
    
    
    public final MemorystoreClient.ListBackupCollectionsPagedResponse listBackupCollections(String parent)

Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.

If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (BackupCollection element :
           memorystoreClient.listBackupCollections(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the backupCollection location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient.ListBackupCollectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListBackupCollectionsPagedResponse)` |   
  
### listBackupCollectionsCallable()
    
    
    public final UnaryCallable<ListBackupCollectionsRequest,ListBackupCollectionsResponse> listBackupCollectionsCallable()

Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.

If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListBackupCollectionsRequest request =
           ListBackupCollectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListBackupCollectionsResponse response =
             memorystoreClient.listBackupCollectionsCallable().call(request);
         for (BackupCollection element : response.getBackupCollectionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupCollectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListBackupCollectionsRequest),[ListBackupCollectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListBackupCollectionsResponse)>` |   
  
### listBackupCollectionsPagedCallable()
    
    
    public final UnaryCallable<ListBackupCollectionsRequest,MemorystoreClient.ListBackupCollectionsPagedResponse> listBackupCollectionsPagedCallable()

Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.

If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListBackupCollectionsRequest request =
           ListBackupCollectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<BackupCollection> future =
           memorystoreClient.listBackupCollectionsPagedCallable().futureCall(request);
       // Do something.
       for (BackupCollection element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupCollectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListBackupCollectionsRequest),[ListBackupCollectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListBackupCollectionsPagedResponse)>` |   
  
### listBackups(@Nullable BackupCollectionName parent)
    
    
    public final MemorystoreClient.ListBackupsPagedResponse listBackups(@Nullable BackupCollectionName parent)

Lists all backups owned by a backup collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       BackupCollectionName parent =
           BackupCollectionName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]");
       for (Backup element : memorystoreClient.listBackups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.BackupCollectionName`  
Required. The resource name of the backupCollection using the form: `projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}`  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient.ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListBackupsPagedResponse)` |   
  
### listBackups(ListBackupsRequest request)
    
    
    public final MemorystoreClient.ListBackupsPagedResponse listBackups(ListBackupsRequest request)

Lists all backups owned by a backup collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(
                   BackupCollectionName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Backup element : memorystoreClient.listBackups(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListBackupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient.ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListBackupsPagedResponse)` |   
  
### listBackups(String parent)
    
    
    public final MemorystoreClient.ListBackupsPagedResponse listBackups(String parent)

Lists all backups owned by a backup collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String parent =
           BackupCollectionName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]").toString();
       for (Backup element : memorystoreClient.listBackups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the backupCollection using the form: `projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}`  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient.ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListBackupsPagedResponse)` |   
  
### listBackupsCallable()
    
    
    public final UnaryCallable<ListBackupsRequest,ListBackupsResponse> listBackupsCallable()

Lists all backups owned by a backup collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(
                   BackupCollectionName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListBackupsResponse response = memorystoreClient.listBackupsCallable().call(request);
         for (Backup element : response.getBackupsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListBackupsRequest),[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListBackupsResponse)>` |   
  
### listBackupsPagedCallable()
    
    
    public final UnaryCallable<ListBackupsRequest,MemorystoreClient.ListBackupsPagedResponse> listBackupsPagedCallable()

Lists all backups owned by a backup collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(
                   BackupCollectionName.of("[PROJECT]", "[LOCATION]", "[BACKUP_COLLECTION]")
                       .toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Backup> future = memorystoreClient.listBackupsPagedCallable().futureCall(request);
       // Do something.
       for (Backup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListBackupsRequest),[ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListBackupsPagedResponse)>` |   
  
### listInstances(@Nullable LocationName parent)
    
    
    public final MemorystoreClient.ListInstancesPagedResponse listInstances(@Nullable LocationName parent)

Lists Instances in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Instance element : memorystoreClient.listInstances(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.LocationName`  
Required. The parent to list instances from. Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient.ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListInstancesPagedResponse)` |   
  
### listInstances(ListInstancesRequest request)
    
    
    public final MemorystoreClient.ListInstancesPagedResponse listInstances(ListInstancesRequest request)

Lists Instances in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListInstancesRequest request =
           ListInstancesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Instance element : memorystoreClient.listInstances(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListInstancesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient.ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListInstancesPagedResponse)` |   
  
### listInstances(String parent)
    
    
    public final MemorystoreClient.ListInstancesPagedResponse listInstances(String parent)

Lists Instances in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Instance element : memorystoreClient.listInstances(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent to list instances from. Format: projects/{project}/locations/{location}  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient.ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListInstancesPagedResponse)` |   
  
### listInstancesCallable()
    
    
    public final UnaryCallable<ListInstancesRequest,ListInstancesResponse> listInstancesCallable()

Lists Instances in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListInstancesRequest request =
           ListInstancesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListInstancesResponse response = memorystoreClient.listInstancesCallable().call(request);
         for (Instance element : response.getInstancesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListInstancesRequest),[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListInstancesResponse)>` |   
  
### listInstancesPagedCallable()
    
    
    public final UnaryCallable<ListInstancesRequest,MemorystoreClient.ListInstancesPagedResponse> listInstancesPagedCallable()

Lists Instances in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListInstancesRequest request =
           ListInstancesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Instance> future =
           memorystoreClient.listInstancesPagedCallable().futureCall(request);
       // Do something.
       for (Instance element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListInstancesRequest),[ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListInstancesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final MemorystoreClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : memorystoreClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = memorystoreClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,MemorystoreClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           memorystoreClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListLocationsPagedResponse)>` |   
  
### listTokenAuthUsers(@Nullable InstanceName parent)
    
    
    public final MemorystoreClient.ListTokenAuthUsersPagedResponse listTokenAuthUsers(@Nullable InstanceName parent)

Lists all the token auth users for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       InstanceName parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       for (TokenAuthUser element : memorystoreClient.listTokenAuthUsers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.InstanceName`  
Required. The parent to list token auth users from. Format: projects/{project}/locations/{location}/instances/{instance}  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient.ListTokenAuthUsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListTokenAuthUsersPagedResponse)` |   
  
### listTokenAuthUsers(ListTokenAuthUsersRequest request)
    
    
    public final MemorystoreClient.ListTokenAuthUsersPagedResponse listTokenAuthUsers(ListTokenAuthUsersRequest request)

Lists all the token auth users for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListTokenAuthUsersRequest request =
           ListTokenAuthUsersRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (TokenAuthUser element : memorystoreClient.listTokenAuthUsers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTokenAuthUsersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListTokenAuthUsersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient.ListTokenAuthUsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListTokenAuthUsersPagedResponse)` |   
  
### listTokenAuthUsers(String parent)
    
    
    public final MemorystoreClient.ListTokenAuthUsersPagedResponse listTokenAuthUsers(String parent)

Lists all the token auth users for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String parent = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       for (TokenAuthUser element : memorystoreClient.listTokenAuthUsers(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent to list token auth users from. Format: projects/{project}/locations/{location}/instances/{instance}  
**Returns**  
---  
**Type** | **Description**  
`[MemorystoreClient.ListTokenAuthUsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListTokenAuthUsersPagedResponse)` |   
  
### listTokenAuthUsersCallable()
    
    
    public final UnaryCallable<ListTokenAuthUsersRequest,ListTokenAuthUsersResponse> listTokenAuthUsersCallable()

Lists all the token auth users for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListTokenAuthUsersRequest request =
           ListTokenAuthUsersRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListTokenAuthUsersResponse response =
             memorystoreClient.listTokenAuthUsersCallable().call(request);
         for (TokenAuthUser element : response.getTokenAuthUsersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTokenAuthUsersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListTokenAuthUsersRequest),[ListTokenAuthUsersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListTokenAuthUsersResponse)>` |   
  
### listTokenAuthUsersPagedCallable()
    
    
    public final UnaryCallable<ListTokenAuthUsersRequest,MemorystoreClient.ListTokenAuthUsersPagedResponse> listTokenAuthUsersPagedCallable()

Lists all the token auth users for a token based auth enabled instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       ListTokenAuthUsersRequest request =
           ListTokenAuthUsersRequest.newBuilder()
               .setParent(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<TokenAuthUser> future =
           memorystoreClient.listTokenAuthUsersPagedCallable().futureCall(request);
       // Do something.
       for (TokenAuthUser element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTokenAuthUsersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.ListTokenAuthUsersRequest),[ListTokenAuthUsersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.MemorystoreClient.ListTokenAuthUsersPagedResponse)>` |   
  
### rescheduleMaintenanceAsync(@Nullable InstanceName name, RescheduleMaintenanceRequest.RescheduleType rescheduleType, Timestamp scheduleTime)
    
    
    public final OperationFuture<Instance,OperationMetadata> rescheduleMaintenanceAsync(@Nullable InstanceName name, RescheduleMaintenanceRequest.RescheduleType rescheduleType, Timestamp scheduleTime)

Reschedules upcoming maintenance event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       InstanceName name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]");
       RescheduleMaintenanceRequest.RescheduleType rescheduleType =
           RescheduleMaintenanceRequest.RescheduleType.forNumber(0);
       Timestamp scheduleTime = Timestamp.newBuilder().build();
       Instance response =
           memorystoreClient.rescheduleMaintenanceAsync(name, rescheduleType, scheduleTime).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.memorystore.v1.InstanceName`  
Required. Name of the instance to reschedule maintenance for: `projects/{project}/locations/{location_id}/instances/{instance}`  
`rescheduleType` | `[RescheduleMaintenanceRequest.RescheduleType](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.RescheduleMaintenanceRequest.RescheduleType)`  
Required. If reschedule type is SPECIFIC_TIME, schedule_time must be set.  
`scheduleTime` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
Optional. Timestamp when the maintenance shall be rescheduled to if reschedule_type=SPECIFIC_TIME, in RFC 3339 format. Example: `2012-11-15T16:19:00.094Z`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### rescheduleMaintenanceAsync(RescheduleMaintenanceRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> rescheduleMaintenanceAsync(RescheduleMaintenanceRequest request)

Reschedules upcoming maintenance event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       RescheduleMaintenanceRequest request =
           RescheduleMaintenanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setScheduleTime(Timestamp.newBuilder().build())
               .build();
       Instance response = memorystoreClient.rescheduleMaintenanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RescheduleMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.RescheduleMaintenanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### rescheduleMaintenanceAsync(String name, RescheduleMaintenanceRequest.RescheduleType rescheduleType, Timestamp scheduleTime)
    
    
    public final OperationFuture<Instance,OperationMetadata> rescheduleMaintenanceAsync(String name, RescheduleMaintenanceRequest.RescheduleType rescheduleType, Timestamp scheduleTime)

Reschedules upcoming maintenance event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       String name = InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString();
       RescheduleMaintenanceRequest.RescheduleType rescheduleType =
           RescheduleMaintenanceRequest.RescheduleType.forNumber(0);
       Timestamp scheduleTime = Timestamp.newBuilder().build();
       Instance response =
           memorystoreClient.rescheduleMaintenanceAsync(name, rescheduleType, scheduleTime).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the instance to reschedule maintenance for: `projects/{project}/locations/{location_id}/instances/{instance}`  
`rescheduleType` | `[RescheduleMaintenanceRequest.RescheduleType](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.RescheduleMaintenanceRequest.RescheduleType)`  
Required. If reschedule type is SPECIFIC_TIME, schedule_time must be set.  
`scheduleTime` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
Optional. Timestamp when the maintenance shall be rescheduled to if reschedule_type=SPECIFIC_TIME, in RFC 3339 format. Example: `2012-11-15T16:19:00.094Z`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### rescheduleMaintenanceCallable()
    
    
    public final UnaryCallable<RescheduleMaintenanceRequest,Operation> rescheduleMaintenanceCallable()

Reschedules upcoming maintenance event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       RescheduleMaintenanceRequest request =
           RescheduleMaintenanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setScheduleTime(Timestamp.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           memorystoreClient.rescheduleMaintenanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RescheduleMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.RescheduleMaintenanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### rescheduleMaintenanceOperationCallable()
    
    
    public final OperationCallable<RescheduleMaintenanceRequest,Instance,OperationMetadata> rescheduleMaintenanceOperationCallable()

Reschedules upcoming maintenance event.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       RescheduleMaintenanceRequest request =
           RescheduleMaintenanceRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .setScheduleTime(Timestamp.newBuilder().build())
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           memorystoreClient.rescheduleMaintenanceOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RescheduleMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.RescheduleMaintenanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### startMigrationAsync(StartMigrationRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> startMigrationAsync(StartMigrationRequest request)

Initiates the migration of a source instance to the target Memorystore instance.

After the successful completion of this operation, the target instance will: 1. Set up replication with the source instance and replicate any writes to the source instance. 2. Only allow reads.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       StartMigrationRequest request =
           StartMigrationRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       Instance response = memorystoreClient.startMigrationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.StartMigrationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### startMigrationCallable()
    
    
    public final UnaryCallable<StartMigrationRequest,Operation> startMigrationCallable()

Initiates the migration of a source instance to the target Memorystore instance.

After the successful completion of this operation, the target instance will: 1. Set up replication with the source instance and replicate any writes to the source instance. 2. Only allow reads.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       StartMigrationRequest request =
           StartMigrationRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       ApiFuture<Operation> future = memorystoreClient.startMigrationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StartMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.StartMigrationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### startMigrationOperationCallable()
    
    
    public final OperationCallable<StartMigrationRequest,Instance,OperationMetadata> startMigrationOperationCallable()

Initiates the migration of a source instance to the target Memorystore instance.

After the successful completion of this operation, the target instance will: 1. Set up replication with the source instance and replicate any writes to the source instance. 2. Only allow reads.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       StartMigrationRequest request =
           StartMigrationRequest.newBuilder()
               .setName(InstanceName.of("[PROJECT]", "[LOCATION]", "[INSTANCE]").toString())
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           memorystoreClient.startMigrationOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StartMigrationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.StartMigrationRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### updateInstanceAsync(Instance instance, FieldMask updateMask)
    
    
    public final OperationFuture<Instance,OperationMetadata> updateInstanceAsync(Instance instance, FieldMask updateMask)

Updates the parameters of a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       Instance instance = Instance.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Instance response = memorystoreClient.updateInstanceAsync(instance, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`instance` | `[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance)`  
Required. The instance to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The list of fields to be updated on the instance. At least one field must be specified.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### updateInstanceAsync(UpdateInstanceRequest request)
    
    
    public final OperationFuture<Instance,OperationMetadata> updateInstanceAsync(UpdateInstanceRequest request)

Updates the parameters of a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       UpdateInstanceRequest request =
           UpdateInstanceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Instance response = memorystoreClient.updateInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.UpdateInstanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
### updateInstanceCallable()
    
    
    public final UnaryCallable<UpdateInstanceRequest,Operation> updateInstanceCallable()

Updates the parameters of a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       UpdateInstanceRequest request =
           UpdateInstanceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = memorystoreClient.updateInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.UpdateInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateInstanceOperationCallable()
    
    
    public final OperationCallable<UpdateInstanceRequest,Instance,OperationMetadata> updateInstanceOperationCallable()

Updates the parameters of a single Instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (MemorystoreClient memorystoreClient = MemorystoreClient.create()) {
       UpdateInstanceRequest request =
           UpdateInstanceRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setInstance(Instance.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Instance, OperationMetadata> future =
           memorystoreClient.updateInstanceOperationCallable().futureCall(request);
       // Do something.
       Instance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.UpdateInstanceRequest),[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.Instance),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-valkey/latest/com.google.cloud.memorystore.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
