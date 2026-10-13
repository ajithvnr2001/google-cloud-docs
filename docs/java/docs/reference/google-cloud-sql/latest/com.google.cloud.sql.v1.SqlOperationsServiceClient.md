---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlOperationsServiceClient
title: Class SqlOperationsServiceClient (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:56:22.013334+00:00
---

# Class SqlOperationsServiceClient (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlOperationsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SqlOperationsServiceClient (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-sql/google-cloud-sql/src/main/java/com/google/cloud/sql/v1/SqlOperationsServiceClient.java)| [Product Reference](https://cloud.google.com/sql/)  
---|---  
  
Service Description: Service to fetch operations for database instances.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlOperationsServiceClient sqlOperationsServiceClient =
         SqlOperationsServiceClient.create()) {
       SqlOperationsGetRequest request =
           SqlOperationsGetRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .setLocation("location1901043637")
               .build();
       Operation response = sqlOperationsServiceClient.get(request);
     }
     

Note: close() needs to be called on the SqlOperationsServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Get |  Retrieves an instance operation that has been performed on an instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(SqlOperationsGetRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
List |  Lists all instance operations that have been performed on the given Cloud SQL instance in the reverse chronological order of the start time. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(SqlOperationsListRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCallable() 

  
Cancel |  Cancels an instance operation that has been performed on an instance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancel(SqlOperationsCancelRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SqlOperationsServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlOperationsServiceSettings sqlOperationsServiceSettings =
         SqlOperationsServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SqlOperationsServiceClient sqlOperationsServiceClient =
         SqlOperationsServiceClient.create(sqlOperationsServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlOperationsServiceSettings sqlOperationsServiceSettings =
         SqlOperationsServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SqlOperationsServiceClient sqlOperationsServiceClient =
         SqlOperationsServiceClient.create(sqlOperationsServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlOperationsServiceSettings sqlOperationsServiceSettings =
         SqlOperationsServiceSettings.newHttpJsonBuilder().build();
     SqlOperationsServiceClient sqlOperationsServiceClient =
         SqlOperationsServiceClient.create(sqlOperationsServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SqlOperationsServiceClient

## Static Methods 

### create()
    
    
    public static final SqlOperationsServiceClient create()

Constructs an instance of SqlOperationsServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SqlOperationsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlOperationsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlOperationsServiceSettings settings)
    
    
    public static final SqlOperationsServiceClient create(SqlOperationsServiceSettings settings)

Constructs an instance of SqlOperationsServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlOperationsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlOperationsServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlOperationsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlOperationsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlOperationsServiceStub stub)
    
    
    public static final SqlOperationsServiceClient create(SqlOperationsServiceStub stub)

Constructs an instance of SqlOperationsServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SqlOperationsServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SqlOperationsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlOperationsServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlOperationsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlOperationsServiceClient)` |   
  
## Constructors 

### SqlOperationsServiceClient(SqlOperationsServiceSettings settings)
    
    
    protected SqlOperationsServiceClient(SqlOperationsServiceSettings settings)

Constructs an instance of SqlOperationsServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlOperationsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlOperationsServiceSettings)`  
  
  
### SqlOperationsServiceClient(SqlOperationsServiceStub stub)
    
    
    protected SqlOperationsServiceClient(SqlOperationsServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SqlOperationsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlOperationsServiceStub)`  
  
  
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
  
### cancel(SqlOperationsCancelRequest request)
    
    
    public final void cancel(SqlOperationsCancelRequest request)

Cancels an instance operation that has been performed on an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlOperationsServiceClient sqlOperationsServiceClient =
         SqlOperationsServiceClient.create()) {
       SqlOperationsCancelRequest request =
           SqlOperationsCancelRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .setLocation("location1901043637")
               .build();
       sqlOperationsServiceClient.cancel(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlOperationsCancelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlOperationsCancelRequest)`  
The request object containing all of the parameters for the API call.  
  
### cancelCallable()
    
    
    public final UnaryCallable<SqlOperationsCancelRequest,Empty> cancelCallable()

Cancels an instance operation that has been performed on an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlOperationsServiceClient sqlOperationsServiceClient =
         SqlOperationsServiceClient.create()) {
       SqlOperationsCancelRequest request =
           SqlOperationsCancelRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .setLocation("location1901043637")
               .build();
       ApiFuture<Empty> future = sqlOperationsServiceClient.cancelCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlOperationsCancelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlOperationsCancelRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### close()
    
    
    public final void close()

### get(SqlOperationsGetRequest request)
    
    
    public final Operation get(SqlOperationsGetRequest request)

Retrieves an instance operation that has been performed on an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlOperationsServiceClient sqlOperationsServiceClient =
         SqlOperationsServiceClient.create()) {
       SqlOperationsGetRequest request =
           SqlOperationsGetRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .setLocation("location1901043637")
               .build();
       Operation response = sqlOperationsServiceClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlOperationsGetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlOperationsGetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)` |   
  
### getCallable()
    
    
    public final UnaryCallable<SqlOperationsGetRequest,Operation> getCallable()

Retrieves an instance operation that has been performed on an instance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlOperationsServiceClient sqlOperationsServiceClient =
         SqlOperationsServiceClient.create()) {
       SqlOperationsGetRequest request =
           SqlOperationsGetRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .setLocation("location1901043637")
               .build();
       ApiFuture<Operation> future = sqlOperationsServiceClient.getCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlOperationsGetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlOperationsGetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.Operation)>` |   
  
### getSettings()
    
    
    public final @Nullable SqlOperationsServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.sql.v1.SqlOperationsServiceSettings` |   
  
### getStub()
    
    
    public SqlOperationsServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SqlOperationsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlOperationsServiceStub)` |   
  
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
  
### list(SqlOperationsListRequest request)
    
    
    public final OperationsListResponse list(SqlOperationsListRequest request)

Lists all instance operations that have been performed on the given Cloud SQL instance in the reverse chronological order of the start time.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlOperationsServiceClient sqlOperationsServiceClient =
         SqlOperationsServiceClient.create()) {
       SqlOperationsListRequest request =
           SqlOperationsListRequest.newBuilder()
               .setInstance("instance555127957")
               .setMaxResults(1128457243)
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setLocation("location1901043637")
               .build();
       OperationsListResponse response = sqlOperationsServiceClient.list(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlOperationsListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlOperationsListRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationsListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.OperationsListResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<SqlOperationsListRequest,OperationsListResponse> listCallable()

Lists all instance operations that have been performed on the given Cloud SQL instance in the reverse chronological order of the start time.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlOperationsServiceClient sqlOperationsServiceClient =
         SqlOperationsServiceClient.create()) {
       SqlOperationsListRequest request =
           SqlOperationsListRequest.newBuilder()
               .setInstance("instance555127957")
               .setMaxResults(1128457243)
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setLocation("location1901043637")
               .build();
       ApiFuture<OperationsListResponse> future =
           sqlOperationsServiceClient.listCallable().futureCall(request);
       // Do something.
       OperationsListResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlOperationsListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlOperationsListRequest),[OperationsListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.OperationsListResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
