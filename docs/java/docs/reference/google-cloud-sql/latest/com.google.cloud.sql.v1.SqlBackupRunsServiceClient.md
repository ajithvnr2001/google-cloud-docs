---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupRunsServiceClient
title: Class SqlBackupRunsServiceClient (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:56:17.045112+00:00
---

# Class SqlBackupRunsServiceClient (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupRunsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SqlBackupRunsServiceClient (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-sql/google-cloud-sql/src/main/java/com/google/cloud/sql/v1/SqlBackupRunsServiceClient.java)| [Product Reference](https://cloud.google.com/sql/)  
---|---  
  
Service Description: Service for managing database backups.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupRunsServiceClient sqlBackupRunsServiceClient =
         SqlBackupRunsServiceClient.create()) {
       SqlBackupRunsDeleteRequest request =
           SqlBackupRunsDeleteRequest.newBuilder()
               .setId(3355)
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       Operation response = sqlBackupRunsServiceClient.delete(request);
     }
     

Note: close() needs to be called on the SqlBackupRunsServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the backup taken by a backup run. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * delete(SqlBackupRunsDeleteRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCallable() 

  
Get |  Retrieves a resource containing information about a backup run. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(SqlBackupRunsGetRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a new backup run on demand. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insert(SqlBackupRunsInsertRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertCallable() 

  
List |  Lists all backup runs associated with the project or a given instance and configuration in the reverse chronological order of the backup initiation time. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(SqlBackupRunsListRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SqlBackupRunsServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlBackupRunsServiceSettings sqlBackupRunsServiceSettings =
         SqlBackupRunsServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SqlBackupRunsServiceClient sqlBackupRunsServiceClient =
         SqlBackupRunsServiceClient.create(sqlBackupRunsServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlBackupRunsServiceSettings sqlBackupRunsServiceSettings =
         SqlBackupRunsServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SqlBackupRunsServiceClient sqlBackupRunsServiceClient =
         SqlBackupRunsServiceClient.create(sqlBackupRunsServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlBackupRunsServiceSettings sqlBackupRunsServiceSettings =
         SqlBackupRunsServiceSettings.newHttpJsonBuilder().build();
     SqlBackupRunsServiceClient sqlBackupRunsServiceClient =
         SqlBackupRunsServiceClient.create(sqlBackupRunsServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SqlBackupRunsServiceClient

## Static Methods 

### create()
    
    
    public static final SqlBackupRunsServiceClient create()

Constructs an instance of SqlBackupRunsServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SqlBackupRunsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupRunsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlBackupRunsServiceSettings settings)
    
    
    public static final SqlBackupRunsServiceClient create(SqlBackupRunsServiceSettings settings)

Constructs an instance of SqlBackupRunsServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlBackupRunsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupRunsServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlBackupRunsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupRunsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlBackupRunsServiceStub stub)
    
    
    public static final SqlBackupRunsServiceClient create(SqlBackupRunsServiceStub stub)

Constructs an instance of SqlBackupRunsServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SqlBackupRunsServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SqlBackupRunsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlBackupRunsServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlBackupRunsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupRunsServiceClient)` |   
  
## Constructors 

### SqlBackupRunsServiceClient(SqlBackupRunsServiceSettings settings)
    
    
    protected SqlBackupRunsServiceClient(SqlBackupRunsServiceSettings settings)

Constructs an instance of SqlBackupRunsServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlBackupRunsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupRunsServiceSettings)`  
  
  
### SqlBackupRunsServiceClient(SqlBackupRunsServiceStub stub)
    
    
    protected SqlBackupRunsServiceClient(SqlBackupRunsServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SqlBackupRunsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlBackupRunsServiceStub)`  
  
  
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

### delete(SqlBackupRunsDeleteRequest request)
    
    
    public final Operation delete(SqlBackupRunsDeleteRequest request)

Deletes the backup taken by a backup run.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupRunsServiceClient sqlBackupRunsServiceClient =
         SqlBackupRunsServiceClient.create()) {
       SqlBackupRunsDeleteRequest request =
           SqlBackupRunsDeleteRequest.newBuilder()
               .setId(3355)
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       Operation response = sqlBackupRunsServiceClient.delete(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlBackupRunsDeleteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupRunsDeleteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<SqlBackupRunsDeleteRequest,Operation> deleteCallable()

Deletes the backup taken by a backup run.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupRunsServiceClient sqlBackupRunsServiceClient =
         SqlBackupRunsServiceClient.create()) {
       SqlBackupRunsDeleteRequest request =
           SqlBackupRunsDeleteRequest.newBuilder()
               .setId(3355)
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<Operation> future = sqlBackupRunsServiceClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlBackupRunsDeleteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupRunsDeleteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### get(SqlBackupRunsGetRequest request)
    
    
    public final BackupRun get(SqlBackupRunsGetRequest request)

Retrieves a resource containing information about a backup run.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupRunsServiceClient sqlBackupRunsServiceClient =
         SqlBackupRunsServiceClient.create()) {
       SqlBackupRunsGetRequest request =
           SqlBackupRunsGetRequest.newBuilder()
               .setId(3355)
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       BackupRun response = sqlBackupRunsServiceClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlBackupRunsGetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupRunsGetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.BackupRun)` |   
  
### getCallable()
    
    
    public final UnaryCallable<SqlBackupRunsGetRequest,BackupRun> getCallable()

Retrieves a resource containing information about a backup run.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupRunsServiceClient sqlBackupRunsServiceClient =
         SqlBackupRunsServiceClient.create()) {
       SqlBackupRunsGetRequest request =
           SqlBackupRunsGetRequest.newBuilder()
               .setId(3355)
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<BackupRun> future = sqlBackupRunsServiceClient.getCallable().futureCall(request);
       // Do something.
       BackupRun response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlBackupRunsGetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupRunsGetRequest),[BackupRun](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.BackupRun)>` |   
  
### getSettings()
    
    
    public final @Nullable SqlBackupRunsServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.sql.v1.SqlBackupRunsServiceSettings` |   
  
### getStub()
    
    
    public SqlBackupRunsServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SqlBackupRunsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlBackupRunsServiceStub)` |   
  
### insert(SqlBackupRunsInsertRequest request)
    
    
    public final Operation insert(SqlBackupRunsInsertRequest request)

Creates a new backup run on demand.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupRunsServiceClient sqlBackupRunsServiceClient =
         SqlBackupRunsServiceClient.create()) {
       SqlBackupRunsInsertRequest request =
           SqlBackupRunsInsertRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(BackupRun.newBuilder().build())
               .build();
       Operation response = sqlBackupRunsServiceClient.insert(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlBackupRunsInsertRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupRunsInsertRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### insertCallable()
    
    
    public final UnaryCallable<SqlBackupRunsInsertRequest,Operation> insertCallable()

Creates a new backup run on demand.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupRunsServiceClient sqlBackupRunsServiceClient =
         SqlBackupRunsServiceClient.create()) {
       SqlBackupRunsInsertRequest request =
           SqlBackupRunsInsertRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(BackupRun.newBuilder().build())
               .build();
       ApiFuture<Operation> future = sqlBackupRunsServiceClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlBackupRunsInsertRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupRunsInsertRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
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
  
### list(SqlBackupRunsListRequest request)
    
    
    public final BackupRunsListResponse list(SqlBackupRunsListRequest request)

Lists all backup runs associated with the project or a given instance and configuration in the reverse chronological order of the backup initiation time.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupRunsServiceClient sqlBackupRunsServiceClient =
         SqlBackupRunsServiceClient.create()) {
       SqlBackupRunsListRequest request =
           SqlBackupRunsListRequest.newBuilder()
               .setInstance("instance555127957")
               .setMaxResults(1128457243)
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       BackupRunsListResponse response = sqlBackupRunsServiceClient.list(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlBackupRunsListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupRunsListRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BackupRunsListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.BackupRunsListResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<SqlBackupRunsListRequest,BackupRunsListResponse> listCallable()

Lists all backup runs associated with the project or a given instance and configuration in the reverse chronological order of the backup initiation time.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlBackupRunsServiceClient sqlBackupRunsServiceClient =
         SqlBackupRunsServiceClient.create()) {
       SqlBackupRunsListRequest request =
           SqlBackupRunsListRequest.newBuilder()
               .setInstance("instance555127957")
               .setMaxResults(1128457243)
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<BackupRunsListResponse> future =
           sqlBackupRunsServiceClient.listCallable().futureCall(request);
       // Do something.
       BackupRunsListResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlBackupRunsListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlBackupRunsListRequest),[BackupRunsListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.BackupRunsListResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
