---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesServiceClient
title: Class SqlDatabasesServiceClient (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:56:17.694386+00:00
---

# Class SqlDatabasesServiceClient (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SqlDatabasesServiceClient (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-sql/google-cloud-sql/src/main/java/com/google/cloud/sql/v1/SqlDatabasesServiceClient.java)| [Product Reference](https://cloud.google.com/sql/)  
---|---  
  
Service Description: Service to manage databases.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlDatabasesServiceClient sqlDatabasesServiceClient = SqlDatabasesServiceClient.create()) {
       SqlDatabasesDeleteRequest request =
           SqlDatabasesDeleteRequest.newBuilder()
               .setDatabase("database1789464955")
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       Operation response = sqlDatabasesServiceClient.delete(request);
     }
     

Note: close() needs to be called on the SqlDatabasesServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes a database from a Cloud SQL instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * delete(SqlDatabasesDeleteRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCallable() 

  
Get |  Retrieves a resource containing information about a database inside a Cloud SQL instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(SqlDatabasesGetRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Inserts a resource containing information about a database inside a Cloud SQL instance.  **Note:** You can't modify the default character set and collation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insert(SqlDatabasesInsertRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertCallable() 

  
List |  Lists databases in the specified Cloud SQL instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(SqlDatabasesListRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCallable() 

  
Patch |  Partially updates a resource containing information about a database inside a Cloud SQL instance. This method supports patch semantics. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patch(SqlDatabasesUpdateRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchCallable() 

  
Update |  Updates a resource containing information about a database inside a Cloud SQL instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * update(SqlDatabasesUpdateRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SqlDatabasesServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlDatabasesServiceSettings sqlDatabasesServiceSettings =
         SqlDatabasesServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SqlDatabasesServiceClient sqlDatabasesServiceClient =
         SqlDatabasesServiceClient.create(sqlDatabasesServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlDatabasesServiceSettings sqlDatabasesServiceSettings =
         SqlDatabasesServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SqlDatabasesServiceClient sqlDatabasesServiceClient =
         SqlDatabasesServiceClient.create(sqlDatabasesServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlDatabasesServiceSettings sqlDatabasesServiceSettings =
         SqlDatabasesServiceSettings.newHttpJsonBuilder().build();
     SqlDatabasesServiceClient sqlDatabasesServiceClient =
         SqlDatabasesServiceClient.create(sqlDatabasesServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SqlDatabasesServiceClient

## Static Methods 

### create()
    
    
    public static final SqlDatabasesServiceClient create()

Constructs an instance of SqlDatabasesServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SqlDatabasesServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlDatabasesServiceSettings settings)
    
    
    public static final SqlDatabasesServiceClient create(SqlDatabasesServiceSettings settings)

Constructs an instance of SqlDatabasesServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlDatabasesServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlDatabasesServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlDatabasesServiceStub stub)
    
    
    public static final SqlDatabasesServiceClient create(SqlDatabasesServiceStub stub)

Constructs an instance of SqlDatabasesServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SqlDatabasesServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SqlDatabasesServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlDatabasesServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlDatabasesServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesServiceClient)` |   
  
## Constructors 

### SqlDatabasesServiceClient(SqlDatabasesServiceSettings settings)
    
    
    protected SqlDatabasesServiceClient(SqlDatabasesServiceSettings settings)

Constructs an instance of SqlDatabasesServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlDatabasesServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesServiceSettings)`  
  
  
### SqlDatabasesServiceClient(SqlDatabasesServiceStub stub)
    
    
    protected SqlDatabasesServiceClient(SqlDatabasesServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SqlDatabasesServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlDatabasesServiceStub)`  
  
  
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

### delete(SqlDatabasesDeleteRequest request)
    
    
    public final Operation delete(SqlDatabasesDeleteRequest request)

Deletes a database from a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlDatabasesServiceClient sqlDatabasesServiceClient = SqlDatabasesServiceClient.create()) {
       SqlDatabasesDeleteRequest request =
           SqlDatabasesDeleteRequest.newBuilder()
               .setDatabase("database1789464955")
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       Operation response = sqlDatabasesServiceClient.delete(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlDatabasesDeleteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesDeleteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<SqlDatabasesDeleteRequest,Operation> deleteCallable()

Deletes a database from a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlDatabasesServiceClient sqlDatabasesServiceClient = SqlDatabasesServiceClient.create()) {
       SqlDatabasesDeleteRequest request =
           SqlDatabasesDeleteRequest.newBuilder()
               .setDatabase("database1789464955")
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<Operation> future = sqlDatabasesServiceClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlDatabasesDeleteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesDeleteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### get(SqlDatabasesGetRequest request)
    
    
    public final Database get(SqlDatabasesGetRequest request)

Retrieves a resource containing information about a database inside a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlDatabasesServiceClient sqlDatabasesServiceClient = SqlDatabasesServiceClient.create()) {
       SqlDatabasesGetRequest request =
           SqlDatabasesGetRequest.newBuilder()
               .setDatabase("database1789464955")
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       Database response = sqlDatabasesServiceClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlDatabasesGetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesGetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Database)` |   
  
### getCallable()
    
    
    public final UnaryCallable<SqlDatabasesGetRequest,Database> getCallable()

Retrieves a resource containing information about a database inside a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlDatabasesServiceClient sqlDatabasesServiceClient = SqlDatabasesServiceClient.create()) {
       SqlDatabasesGetRequest request =
           SqlDatabasesGetRequest.newBuilder()
               .setDatabase("database1789464955")
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<Database> future = sqlDatabasesServiceClient.getCallable().futureCall(request);
       // Do something.
       Database response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlDatabasesGetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesGetRequest),[Database](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Database)>` |   
  
### getSettings()
    
    
    public final @Nullable SqlDatabasesServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.sql.v1.SqlDatabasesServiceSettings` |   
  
### getStub()
    
    
    public SqlDatabasesServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SqlDatabasesServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlDatabasesServiceStub)` |   
  
### insert(SqlDatabasesInsertRequest request)
    
    
    public final Operation insert(SqlDatabasesInsertRequest request)

Inserts a resource containing information about a database inside a Cloud SQL instance.

**Note:** You can't modify the default character set and collation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlDatabasesServiceClient sqlDatabasesServiceClient = SqlDatabasesServiceClient.create()) {
       SqlDatabasesInsertRequest request =
           SqlDatabasesInsertRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(Database.newBuilder().build())
               .build();
       Operation response = sqlDatabasesServiceClient.insert(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlDatabasesInsertRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesInsertRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### insertCallable()
    
    
    public final UnaryCallable<SqlDatabasesInsertRequest,Operation> insertCallable()

Inserts a resource containing information about a database inside a Cloud SQL instance.

**Note:** You can't modify the default character set and collation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlDatabasesServiceClient sqlDatabasesServiceClient = SqlDatabasesServiceClient.create()) {
       SqlDatabasesInsertRequest request =
           SqlDatabasesInsertRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(Database.newBuilder().build())
               .build();
       ApiFuture<Operation> future = sqlDatabasesServiceClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlDatabasesInsertRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesInsertRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
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
  
### list(SqlDatabasesListRequest request)
    
    
    public final DatabasesListResponse list(SqlDatabasesListRequest request)

Lists databases in the specified Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlDatabasesServiceClient sqlDatabasesServiceClient = SqlDatabasesServiceClient.create()) {
       SqlDatabasesListRequest request =
           SqlDatabasesListRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       DatabasesListResponse response = sqlDatabasesServiceClient.list(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlDatabasesListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesListRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DatabasesListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.DatabasesListResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<SqlDatabasesListRequest,DatabasesListResponse> listCallable()

Lists databases in the specified Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlDatabasesServiceClient sqlDatabasesServiceClient = SqlDatabasesServiceClient.create()) {
       SqlDatabasesListRequest request =
           SqlDatabasesListRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<DatabasesListResponse> future =
           sqlDatabasesServiceClient.listCallable().futureCall(request);
       // Do something.
       DatabasesListResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlDatabasesListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesListRequest),[DatabasesListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.DatabasesListResponse)>` |   
  
### patch(SqlDatabasesUpdateRequest request)
    
    
    public final Operation patch(SqlDatabasesUpdateRequest request)

Partially updates a resource containing information about a database inside a Cloud SQL instance. This method supports patch semantics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlDatabasesServiceClient sqlDatabasesServiceClient = SqlDatabasesServiceClient.create()) {
       SqlDatabasesUpdateRequest request =
           SqlDatabasesUpdateRequest.newBuilder()
               .setDatabase("database1789464955")
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(Database.newBuilder().build())
               .build();
       Operation response = sqlDatabasesServiceClient.patch(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlDatabasesUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesUpdateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### patchCallable()
    
    
    public final UnaryCallable<SqlDatabasesUpdateRequest,Operation> patchCallable()

Partially updates a resource containing information about a database inside a Cloud SQL instance. This method supports patch semantics.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlDatabasesServiceClient sqlDatabasesServiceClient = SqlDatabasesServiceClient.create()) {
       SqlDatabasesUpdateRequest request =
           SqlDatabasesUpdateRequest.newBuilder()
               .setDatabase("database1789464955")
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(Database.newBuilder().build())
               .build();
       ApiFuture<Operation> future = sqlDatabasesServiceClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlDatabasesUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesUpdateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### update(SqlDatabasesUpdateRequest request)
    
    
    public final Operation update(SqlDatabasesUpdateRequest request)

Updates a resource containing information about a database inside a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlDatabasesServiceClient sqlDatabasesServiceClient = SqlDatabasesServiceClient.create()) {
       SqlDatabasesUpdateRequest request =
           SqlDatabasesUpdateRequest.newBuilder()
               .setDatabase("database1789464955")
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(Database.newBuilder().build())
               .build();
       Operation response = sqlDatabasesServiceClient.update(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlDatabasesUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesUpdateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### updateCallable()
    
    
    public final UnaryCallable<SqlDatabasesUpdateRequest,Operation> updateCallable()

Updates a resource containing information about a database inside a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlDatabasesServiceClient sqlDatabasesServiceClient = SqlDatabasesServiceClient.create()) {
       SqlDatabasesUpdateRequest request =
           SqlDatabasesUpdateRequest.newBuilder()
               .setDatabase("database1789464955")
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(Database.newBuilder().build())
               .build();
       ApiFuture<Operation> future = sqlDatabasesServiceClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlDatabasesUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlDatabasesUpdateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
