---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupsServiceClient
title: Class SqlBackupsServiceClient (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:56:18.361473+00:00
---

# Class SqlBackupsServiceClient (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SqlBackupsServiceClient (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-sql/google-cloud-sql/src/main/java/com/google/cloud/sql/v1/SqlBackupsServiceClient.java)| [Product Reference](https://cloud.google.com/sql/)  
---|---  
  
This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       Backup backup = Backup.newBuilder().build();
       Operation response = sqlBackupsServiceClient.createBackup(parent, backup);
     }
     

Note: close() needs to be called on the SqlBackupsServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateBackup |  Creates a backup for a Cloud SQL instance. This API can be used only to create on-demand backups. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createBackup(CreateBackupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createBackup(ProjectName parent, Backup backup) 
  * createBackup(String parent, Backup backup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createBackupCallable() 

  
GetBackup |  Retrieves a resource containing information about a backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBackup(GetBackupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBackup(BackupName name) 
  * getBackup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBackupCallable() 

  
ListBackups |  Lists all backups associated with the project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBackups(ListBackupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBackups(ProjectName parent) 
  * listBackups(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBackupsPagedCallable() 
  * listBackupsCallable() 

  
UpdateBackup |  Updates the retention period and description of the backup. You can use this API to update final backups only. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateBackup(UpdateBackupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateBackup(Backup backup, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateBackupCallable() 

  
DeleteBackup |  Deletes the backup. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBackup(DeleteBackupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteBackup(BackupName name) 
  * deleteBackup(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBackupCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SqlBackupsServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlBackupsServiceSettings sqlBackupsServiceSettings =
         SqlBackupsServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SqlBackupsServiceClient sqlBackupsServiceClient =
         SqlBackupsServiceClient.create(sqlBackupsServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlBackupsServiceSettings sqlBackupsServiceSettings =
         SqlBackupsServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SqlBackupsServiceClient sqlBackupsServiceClient =
         SqlBackupsServiceClient.create(sqlBackupsServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlBackupsServiceSettings sqlBackupsServiceSettings =
         SqlBackupsServiceSettings.newHttpJsonBuilder().build();
     SqlBackupsServiceClient sqlBackupsServiceClient =
         SqlBackupsServiceClient.create(sqlBackupsServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SqlBackupsServiceClient

## Static Methods 

### create()
    
    
    public static final SqlBackupsServiceClient create()

Constructs an instance of SqlBackupsServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SqlBackupsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlBackupsServiceSettings settings)
    
    
    public static final SqlBackupsServiceClient create(SqlBackupsServiceSettings settings)

Constructs an instance of SqlBackupsServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlBackupsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupsServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlBackupsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlBackupsServiceStub stub)
    
    
    public static final SqlBackupsServiceClient create(SqlBackupsServiceStub stub)

Constructs an instance of SqlBackupsServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SqlBackupsServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SqlBackupsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlBackupsServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlBackupsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupsServiceClient)` |   
  
## Constructors 

### SqlBackupsServiceClient(SqlBackupsServiceSettings settings)
    
    
    protected SqlBackupsServiceClient(SqlBackupsServiceSettings settings)

Constructs an instance of SqlBackupsServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlBackupsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupsServiceSettings)`  
  
  
### SqlBackupsServiceClient(SqlBackupsServiceStub stub)
    
    
    protected SqlBackupsServiceClient(SqlBackupsServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SqlBackupsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlBackupsServiceStub)`  
  
  
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
  
### close()
    
    
    public final void close()

### createBackup(@Nullable ProjectName parent, Backup backup)
    
    
    public final Operation createBackup(@Nullable ProjectName parent, Backup backup)

Creates a backup for a Cloud SQL instance. This API can be used only to create on-demand backups.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       Backup backup = Backup.newBuilder().build();
       Operation response = sqlBackupsServiceClient.createBackup(parent, backup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.sql.v1.ProjectName`  
Required. The parent resource where this backup is created. Format: projects/{project}  
`backup` | `[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Backup)`  
Required. The Backup to create.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### createBackup(CreateBackupRequest request)
    
    
    public final Operation createBackup(CreateBackupRequest request)

Creates a backup for a Cloud SQL instance. This API can be used only to create on-demand backups.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       CreateBackupRequest request =
           CreateBackupRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setBackup(Backup.newBuilder().build())
               .build();
       Operation response = sqlBackupsServiceClient.createBackup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.CreateBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### createBackup(String parent, Backup backup)
    
    
    public final Operation createBackup(String parent, Backup backup)

Creates a backup for a Cloud SQL instance. This API can be used only to create on-demand backups.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       Backup backup = Backup.newBuilder().build();
       Operation response = sqlBackupsServiceClient.createBackup(parent, backup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this backup is created. Format: projects/{project}  
`backup` | `[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Backup)`  
Required. The Backup to create.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### createBackupCallable()
    
    
    public final UnaryCallable<CreateBackupRequest,Operation> createBackupCallable()

Creates a backup for a Cloud SQL instance. This API can be used only to create on-demand backups.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       CreateBackupRequest request =
           CreateBackupRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setBackup(Backup.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           sqlBackupsServiceClient.createBackupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.CreateBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### deleteBackup(@Nullable BackupName name)
    
    
    public final Operation deleteBackup(@Nullable BackupName name)

Deletes the backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       BackupName name = BackupName.of("[PROJECT]", "[BACKUP]");
       Operation response = sqlBackupsServiceClient.deleteBackup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.sql.v1.BackupName`  
Required. The name of the backup to delete. Format: projects/{project}/backups/{backup}  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### deleteBackup(DeleteBackupRequest request)
    
    
    public final Operation deleteBackup(DeleteBackupRequest request)

Deletes the backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       DeleteBackupRequest request =
           DeleteBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[BACKUP]").toString())
               .build();
       Operation response = sqlBackupsServiceClient.deleteBackup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.DeleteBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### deleteBackup(String name)
    
    
    public final Operation deleteBackup(String name)

Deletes the backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       String name = BackupName.of("[PROJECT]", "[BACKUP]").toString();
       Operation response = sqlBackupsServiceClient.deleteBackup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the backup to delete. Format: projects/{project}/backups/{backup}  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### deleteBackupCallable()
    
    
    public final UnaryCallable<DeleteBackupRequest,Operation> deleteBackupCallable()

Deletes the backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       DeleteBackupRequest request =
           DeleteBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[BACKUP]").toString())
               .build();
       ApiFuture<Operation> future =
           sqlBackupsServiceClient.deleteBackupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.DeleteBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### getBackup(@Nullable BackupName name)
    
    
    public final Backup getBackup(@Nullable BackupName name)

Retrieves a resource containing information about a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       BackupName name = BackupName.of("[PROJECT]", "[BACKUP]");
       Backup response = sqlBackupsServiceClient.getBackup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.sql.v1.BackupName`  
Required. The name of the backup to retrieve. Format: projects/{project}/backups/{backup}  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Backup)` |   
  
### getBackup(GetBackupRequest request)
    
    
    public final Backup getBackup(GetBackupRequest request)

Retrieves a resource containing information about a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       GetBackupRequest request =
           GetBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[BACKUP]").toString())
               .build();
       Backup response = sqlBackupsServiceClient.getBackup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.GetBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Backup)` |   
  
### getBackup(String name)
    
    
    public final Backup getBackup(String name)

Retrieves a resource containing information about a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       String name = BackupName.of("[PROJECT]", "[BACKUP]").toString();
       Backup response = sqlBackupsServiceClient.getBackup(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the backup to retrieve. Format: projects/{project}/backups/{backup}  
**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Backup)` |   
  
### getBackupCallable()
    
    
    public final UnaryCallable<GetBackupRequest,Backup> getBackupCallable()

Retrieves a resource containing information about a backup.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       GetBackupRequest request =
           GetBackupRequest.newBuilder()
               .setName(BackupName.of("[PROJECT]", "[BACKUP]").toString())
               .build();
       ApiFuture<Backup> future = sqlBackupsServiceClient.getBackupCallable().futureCall(request);
       // Do something.
       Backup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.GetBackupRequest),[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Backup)>` |   
  
### getSettings()
    
    
    public final @Nullable SqlBackupsServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.sql.v1.SqlBackupsServiceSettings` |   
  
### getStub()
    
    
    public SqlBackupsServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SqlBackupsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlBackupsServiceStub)` |   
  
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
  
### listBackups(@Nullable ProjectName parent)
    
    
    public final SqlBackupsServiceClient.ListBackupsPagedResponse listBackups(@Nullable ProjectName parent)

Lists all backups associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       for (Backup element : sqlBackupsServiceClient.listBackups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.sql.v1.ProjectName`  
Required. The parent that owns this collection of backups. Format: projects/{project}  
**Returns**  
---  
**Type** | **Description**  
`[SqlBackupsServiceClient.ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupsServiceClient.ListBackupsPagedResponse)` |   
  
### listBackups(ListBackupsRequest request)
    
    
    public final SqlBackupsServiceClient.ListBackupsPagedResponse listBackups(ListBackupsRequest request)

Lists all backups associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Backup element : sqlBackupsServiceClient.listBackups(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ListBackupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SqlBackupsServiceClient.ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupsServiceClient.ListBackupsPagedResponse)` |   
  
### listBackups(String parent)
    
    
    public final SqlBackupsServiceClient.ListBackupsPagedResponse listBackups(String parent)

Lists all backups associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       for (Backup element : sqlBackupsServiceClient.listBackups(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent that owns this collection of backups. Format: projects/{project}  
**Returns**  
---  
**Type** | **Description**  
`[SqlBackupsServiceClient.ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupsServiceClient.ListBackupsPagedResponse)` |   
  
### listBackupsCallable()
    
    
    public final UnaryCallable<ListBackupsRequest,ListBackupsResponse> listBackupsCallable()

Lists all backups associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListBackupsResponse response = sqlBackupsServiceClient.listBackupsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ListBackupsRequest),[ListBackupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ListBackupsResponse)>` |   
  
### listBackupsPagedCallable()
    
    
    public final UnaryCallable<ListBackupsRequest,SqlBackupsServiceClient.ListBackupsPagedResponse> listBackupsPagedCallable()

Lists all backups associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       ListBackupsRequest request =
           ListBackupsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Backup> future =
           sqlBackupsServiceClient.listBackupsPagedCallable().futureCall(request);
       // Do something.
       for (Backup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBackupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ListBackupsRequest),[ListBackupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupsServiceClient.ListBackupsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateBackup(Backup backup, FieldMask updateMask)
    
    
    public final Operation updateBackup(Backup backup, FieldMask updateMask)

Updates the retention period and description of the backup. You can use this API to update final backups only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       Backup backup = Backup.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Operation response = sqlBackupsServiceClient.updateBackup(backup, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`backup` | `[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Backup)`  
Required. The backup to update. The backup’s `name` field is used to identify the backup to update. Format: projects/{project}/backups/{backup}  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
The list of fields that you can update. You can update only the description and retention period of the final backup.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### updateBackup(UpdateBackupRequest request)
    
    
    public final Operation updateBackup(UpdateBackupRequest request)

Updates the retention period and description of the backup. You can use this API to update final backups only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       UpdateBackupRequest request =
           UpdateBackupRequest.newBuilder()
               .setBackup(Backup.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Operation response = sqlBackupsServiceClient.updateBackup(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.UpdateBackupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### updateBackupCallable()
    
    
    public final UnaryCallable<UpdateBackupRequest,Operation> updateBackupCallable()

Updates the retention period and description of the backup. You can use this API to update final backups only.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupsServiceClient sqlBackupsServiceClient = SqlBackupsServiceClient.create()) {
       UpdateBackupRequest request =
           UpdateBackupRequest.newBuilder()
               .setBackup(Backup.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           sqlBackupsServiceClient.updateBackupCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.UpdateBackupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
