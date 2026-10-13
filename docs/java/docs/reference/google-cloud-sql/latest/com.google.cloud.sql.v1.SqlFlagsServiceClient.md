---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlFlagsServiceClient
title: Class SqlFlagsServiceClient (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:56:18.936534+00:00
---

# Class SqlFlagsServiceClient (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlFlagsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SqlFlagsServiceClient (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-sql/google-cloud-sql/src/main/java/com/google/cloud/sql/v1/SqlFlagsServiceClient.java)| [Product Reference](https://cloud.google.com/sql/)  
---|---  
  
Service Description: Service to manage database flags for Cloud SQL instances.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlFlagsServiceClient sqlFlagsServiceClient = SqlFlagsServiceClient.create()) {
       SqlFlagsListRequest request =
           SqlFlagsListRequest.newBuilder()
               .setDatabaseVersion("databaseVersion1250955997")
               .setFlagScope(SqlFlagScope.forNumber(0))
               .build();
       FlagsListResponse response = sqlFlagsServiceClient.list(request);
     }
     

Note: close() needs to be called on the SqlFlagsServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
List |  Lists all available database flags for Cloud SQL instances. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(SqlFlagsListRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SqlFlagsServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlFlagsServiceSettings sqlFlagsServiceSettings =
         SqlFlagsServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SqlFlagsServiceClient sqlFlagsServiceClient =
         SqlFlagsServiceClient.create(sqlFlagsServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlFlagsServiceSettings sqlFlagsServiceSettings =
         SqlFlagsServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SqlFlagsServiceClient sqlFlagsServiceClient =
         SqlFlagsServiceClient.create(sqlFlagsServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SqlFlagsServiceSettings sqlFlagsServiceSettings =
         SqlFlagsServiceSettings.newHttpJsonBuilder().build();
     SqlFlagsServiceClient sqlFlagsServiceClient =
         SqlFlagsServiceClient.create(sqlFlagsServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SqlFlagsServiceClient

## Static Methods 

### create()
    
    
    public static final SqlFlagsServiceClient create()

Constructs an instance of SqlFlagsServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SqlFlagsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlFlagsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlFlagsServiceSettings settings)
    
    
    public static final SqlFlagsServiceClient create(SqlFlagsServiceSettings settings)

Constructs an instance of SqlFlagsServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlFlagsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlFlagsServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlFlagsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlFlagsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SqlFlagsServiceStub stub)
    
    
    public static final SqlFlagsServiceClient create(SqlFlagsServiceStub stub)

Constructs an instance of SqlFlagsServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SqlFlagsServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SqlFlagsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlFlagsServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlFlagsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlFlagsServiceClient)` |   
  
## Constructors 

### SqlFlagsServiceClient(SqlFlagsServiceSettings settings)
    
    
    protected SqlFlagsServiceClient(SqlFlagsServiceSettings settings)

Constructs an instance of SqlFlagsServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SqlFlagsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlFlagsServiceSettings)`  
  
  
### SqlFlagsServiceClient(SqlFlagsServiceStub stub)
    
    
    protected SqlFlagsServiceClient(SqlFlagsServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SqlFlagsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlFlagsServiceStub)`  
  
  
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

### getSettings()
    
    
    public final @Nullable SqlFlagsServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.sql.v1.SqlFlagsServiceSettings` |   
  
### getStub()
    
    
    public SqlFlagsServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SqlFlagsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.stub.SqlFlagsServiceStub)` |   
  
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
  
### list(SqlFlagsListRequest request)
    
    
    public final FlagsListResponse list(SqlFlagsListRequest request)

Lists all available database flags for Cloud SQL instances.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlFlagsServiceClient sqlFlagsServiceClient = SqlFlagsServiceClient.create()) {
       SqlFlagsListRequest request =
           SqlFlagsListRequest.newBuilder()
               .setDatabaseVersion("databaseVersion1250955997")
               .setFlagScope(SqlFlagScope.forNumber(0))
               .build();
       FlagsListResponse response = sqlFlagsServiceClient.list(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SqlFlagsListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlFlagsListRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FlagsListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.FlagsListResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<SqlFlagsListRequest,FlagsListResponse> listCallable()

Lists all available database flags for Cloud SQL instances.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SqlFlagsServiceClient sqlFlagsServiceClient = SqlFlagsServiceClient.create()) {
       SqlFlagsListRequest request =
           SqlFlagsListRequest.newBuilder()
               .setDatabaseVersion("databaseVersion1250955997")
               .setFlagScope(SqlFlagScope.forNumber(0))
               .build();
       ApiFuture<FlagsListResponse> future =
           sqlFlagsServiceClient.listCallable().futureCall(request);
       // Do something.
       FlagsListResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SqlFlagsListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlFlagsListRequest),[FlagsListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.FlagsListResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
