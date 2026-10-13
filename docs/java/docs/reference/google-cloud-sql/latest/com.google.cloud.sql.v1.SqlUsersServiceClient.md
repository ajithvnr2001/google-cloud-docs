---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersServiceClient
title: Class SqlUsersServiceClient (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:56:21.708200+00:00
---

# Class SqlUsersServiceClient (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SqlUsersServiceClient (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-sql/google-cloud-sql/src/main/java/com/google/cloud/sql/v1/SqlUsersServiceClient.java)| [Product Reference](https://cloud.google.com/sql/)  
---|---  
  
Service Description: Cloud SQL users service.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlUsersServiceClient sqlUsersServiceClient = SqlUsersServiceClient.create()) {
       SqlUsersDeleteRequest request =
           SqlUsersDeleteRequest.newBuilder()
               .setHost("host3208616")
               .setInstance("instance555127957")
               .setName("name3373707")
               .setProject("project-309310695")
               .build();
       Operation response = sqlUsersServiceClient.delete(request);
     }
     

Note: close() needs to be called on the SqlUsersServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes a user from a Cloud SQL instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * delete(SqlUsersDeleteRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCallable() 

  
Get |  Retrieves a resource containing information about a user. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(SqlUsersGetRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a new user in a Cloud SQL instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insert(SqlUsersInsertRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertCallable() 

  
List |  Lists users in the specified Cloud SQL instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(SqlUsersListRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCallable() 

  
Update |  Updates an existing user in a Cloud SQL instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * update(SqlUsersUpdateRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SqlUsersServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlUsersServiceSettings sqlUsersServiceSettings =
         SqlUsersServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SqlUsersServiceClient sqlUsersServiceClient =
         SqlUsersServiceClient.create(sqlUsersServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlUsersServiceSettings sqlUsersServiceSettings =
         SqlUsersServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SqlUsersServiceClient sqlUsersServiceClient =
         SqlUsersServiceClient.create(sqlUsersServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlUsersServiceSettings sqlUsersServiceSettings =
         SqlUsersServiceSettings.newHttpJsonBuilder().build();
     SqlUsersServiceClient sqlUsersServiceClient =
         SqlUsersServiceClient.create(sqlUsersServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SqlUsersServiceClient

## Static Methods 

### create()
    
    
    public static final SqlUsersServiceClient create()

Constructs an instance of SqlUsersServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SqlUsersServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlUsersServiceSettings settings)
    
    
    public static final SqlUsersServiceClient create(SqlUsersServiceSettings settings)

Constructs an instance of SqlUsersServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlUsersServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlUsersServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlUsersServiceStub stub)
    
    
    public static final SqlUsersServiceClient create(SqlUsersServiceStub stub)

Constructs an instance of SqlUsersServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SqlUsersServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SqlUsersServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlUsersServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlUsersServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersServiceClient)` |   
  
## Constructors 

### SqlUsersServiceClient(SqlUsersServiceSettings settings)
    
    
    protected SqlUsersServiceClient(SqlUsersServiceSettings settings)

Constructs an instance of SqlUsersServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlUsersServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersServiceSettings)`  
  
  
### SqlUsersServiceClient(SqlUsersServiceStub stub)
    
    
    protected SqlUsersServiceClient(SqlUsersServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SqlUsersServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlUsersServiceStub)`  
  
  
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

### delete(SqlUsersDeleteRequest request)
    
    
    public final Operation delete(SqlUsersDeleteRequest request)

Deletes a user from a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlUsersServiceClient sqlUsersServiceClient = SqlUsersServiceClient.create()) {
       SqlUsersDeleteRequest request =
           SqlUsersDeleteRequest.newBuilder()
               .setHost("host3208616")
               .setInstance("instance555127957")
               .setName("name3373707")
               .setProject("project-309310695")
               .build();
       Operation response = sqlUsersServiceClient.delete(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlUsersDeleteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersDeleteRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<SqlUsersDeleteRequest,Operation> deleteCallable()

Deletes a user from a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlUsersServiceClient sqlUsersServiceClient = SqlUsersServiceClient.create()) {
       SqlUsersDeleteRequest request =
           SqlUsersDeleteRequest.newBuilder()
               .setHost("host3208616")
               .setInstance("instance555127957")
               .setName("name3373707")
               .setProject("project-309310695")
               .build();
       ApiFuture<Operation> future = sqlUsersServiceClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlUsersDeleteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersDeleteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### get(SqlUsersGetRequest request)
    
    
    public final User get(SqlUsersGetRequest request)

Retrieves a resource containing information about a user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlUsersServiceClient sqlUsersServiceClient = SqlUsersServiceClient.create()) {
       SqlUsersGetRequest request =
           SqlUsersGetRequest.newBuilder()
               .setInstance("instance555127957")
               .setName("name3373707")
               .setProject("project-309310695")
               .setHost("host3208616")
               .build();
       User response = sqlUsersServiceClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlUsersGetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersGetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.User)` |   
  
### getCallable()
    
    
    public final UnaryCallable<SqlUsersGetRequest,User> getCallable()

Retrieves a resource containing information about a user.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlUsersServiceClient sqlUsersServiceClient = SqlUsersServiceClient.create()) {
       SqlUsersGetRequest request =
           SqlUsersGetRequest.newBuilder()
               .setInstance("instance555127957")
               .setName("name3373707")
               .setProject("project-309310695")
               .setHost("host3208616")
               .build();
       ApiFuture<User> future = sqlUsersServiceClient.getCallable().futureCall(request);
       // Do something.
       User response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlUsersGetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersGetRequest),[User](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.User)>` |   
  
### getSettings()
    
    
    public final @Nullable SqlUsersServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.sql.v1.SqlUsersServiceSettings` |   
  
### getStub()
    
    
    public SqlUsersServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SqlUsersServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlUsersServiceStub)` |   
  
### insert(SqlUsersInsertRequest request)
    
    
    public final Operation insert(SqlUsersInsertRequest request)

Creates a new user in a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlUsersServiceClient sqlUsersServiceClient = SqlUsersServiceClient.create()) {
       SqlUsersInsertRequest request =
           SqlUsersInsertRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(User.newBuilder().build())
               .build();
       Operation response = sqlUsersServiceClient.insert(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlUsersInsertRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersInsertRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### insertCallable()
    
    
    public final UnaryCallable<SqlUsersInsertRequest,Operation> insertCallable()

Creates a new user in a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlUsersServiceClient sqlUsersServiceClient = SqlUsersServiceClient.create()) {
       SqlUsersInsertRequest request =
           SqlUsersInsertRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .setBody(User.newBuilder().build())
               .build();
       ApiFuture<Operation> future = sqlUsersServiceClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlUsersInsertRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersInsertRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
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
  
### list(SqlUsersListRequest request)
    
    
    public final UsersListResponse list(SqlUsersListRequest request)

Lists users in the specified Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlUsersServiceClient sqlUsersServiceClient = SqlUsersServiceClient.create()) {
       SqlUsersListRequest request =
           SqlUsersListRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       UsersListResponse response = sqlUsersServiceClient.list(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlUsersListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersListRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UsersListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.UsersListResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<SqlUsersListRequest,UsersListResponse> listCallable()

Lists users in the specified Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlUsersServiceClient sqlUsersServiceClient = SqlUsersServiceClient.create()) {
       SqlUsersListRequest request =
           SqlUsersListRequest.newBuilder()
               .setInstance("instance555127957")
               .setProject("project-309310695")
               .build();
       ApiFuture<UsersListResponse> future =
           sqlUsersServiceClient.listCallable().futureCall(request);
       // Do something.
       UsersListResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlUsersListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersListRequest),[UsersListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.UsersListResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### update(SqlUsersUpdateRequest request)
    
    
    public final Operation update(SqlUsersUpdateRequest request)

Updates an existing user in a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlUsersServiceClient sqlUsersServiceClient = SqlUsersServiceClient.create()) {
       SqlUsersUpdateRequest request =
           SqlUsersUpdateRequest.newBuilder()
               .setHost("host3208616")
               .setInstance("instance555127957")
               .setName("name3373707")
               .setProject("project-309310695")
               .addAllDatabaseRoles(new ArrayList<String>())
               .setRevokeExistingRoles(true)
               .addAllServerRoles(new ArrayList<String>())
               .setRevokeExistingServerRoles(true)
               .setBody(User.newBuilder().build())
               .build();
       Operation response = sqlUsersServiceClient.update(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlUsersUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersUpdateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### updateCallable()
    
    
    public final UnaryCallable<SqlUsersUpdateRequest,Operation> updateCallable()

Updates an existing user in a Cloud SQL instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlUsersServiceClient sqlUsersServiceClient = SqlUsersServiceClient.create()) {
       SqlUsersUpdateRequest request =
           SqlUsersUpdateRequest.newBuilder()
               .setHost("host3208616")
               .setInstance("instance555127957")
               .setName("name3373707")
               .setProject("project-309310695")
               .addAllDatabaseRoles(new ArrayList<String>())
               .setRevokeExistingRoles(true)
               .addAllServerRoles(new ArrayList<String>())
               .setRevokeExistingServerRoles(true)
               .setBody(User.newBuilder().build())
               .build();
       ApiFuture<Operation> future = sqlUsersServiceClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlUsersUpdateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlUsersUpdateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
