---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceClient
title: Class DataPointsServiceClient (0.8.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:57.727180+00:00
---

# Class DataPointsServiceClient (0.8.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataPointsServiceClient (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.0 (latest)  0.4.0  0.3.0  0.2.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-health/google-cloud-health/src/main/java/com/google/devicesandservices/health/v4/DataPointsServiceClient.java)| [Product Reference](https://developers.google.com/health/api)| [RPC Documentation](https://developers.google.com/health/api/reference/rpc)  
---|---|---  
  
Service Description: Data Points Service exposing the user's health and fitness measured and derived data.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       DataPointName name = DataPointName.of("[USER]", "[DATA_TYPE]", "[DATA_POINT]");
       DataPoint response = dataPointsServiceClient.getDataPoint(name);
     }
     

Note: close() needs to be called on the DataPointsServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetDataPoint |  Get a single identifyable data point. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataPoint(GetDataPointRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataPoint(DataPointName name) 
  * getDataPoint(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDataPointCallable() 

  
ListDataPoints |  Query user health and fitness data points. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDataPoints(ListDataPointsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDataPoints(DataTypeName parent) 
  * listDataPoints(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDataPointsPagedCallable() 
  * listDataPointsCallable() 

  
CreateDataPoint |  Creates a single identifiable data point. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDataPointAsync(CreateDataPointRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createDataPointAsync(DataTypeName parent, DataPoint dataPoint) 
  * createDataPointAsync(String parent, DataPoint dataPoint) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDataPointOperationCallable() 
  * createDataPointCallable() 

  
UpdateDataPoint |  Updates a single identifiable data point. If a data point with the specified `name` is not found, the request will fail. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDataPointAsync(UpdateDataPointRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateDataPointAsync(DataPoint dataPoint) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDataPointOperationCallable() 
  * updateDataPointCallable() 

  
BatchDeleteDataPoints |  Delete a batch of identifyable data points. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeleteDataPointsAsync(BatchDeleteDataPointsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeleteDataPointsOperationCallable() 
  * batchDeleteDataPointsCallable() 

  
ReconcileDataPoints |  Reconcile data points from multiple data sources into a single data stream. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * reconcileDataPoints(ReconcileDataPointsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * reconcileDataPointsPagedCallable() 
  * reconcileDataPointsCallable() 

  
RollUpDataPoints |  Roll up data points over physical time intervals for supported data types. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * rollUpDataPoints(RollUpDataPointsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * rollUpDataPointsPagedCallable() 
  * rollUpDataPointsCallable() 

  
DailyRollUpDataPoints |  Roll up data points over civil time intervals for supported data types. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * dailyRollUpDataPoints(DailyRollUpDataPointsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * dailyRollUpDataPointsCallable() 

  
ExportExerciseTcx |  Exports exercise data in TCX format.  **IMPORTANT:** HTTP clients must append `?alt=media` to the request URL to download the raw TCX file.  Example: `<https://health.googleapis.com/v4/users/me/dataTypes/exercise/dataPoints/EXERCISE_ID:exportExerciseTcx?alt=media>` Without `alt=media`, the server returns a JSON response (`ExportExerciseTcxResponse`) which is intended primarily for gRPC clients.  **Note:** While the Authorization section below states that any one of the listed scopes is accepted, this specific method requires the user to provide both one of the `activity_and_fitness` scopes (`normal` or `readonly`) AND one of the `location` scopes (`normal` or `readonly`) in their access token to succeed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportExerciseTcx(ExportExerciseTcxRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * exportExerciseTcx(DataPointName name) 
  * exportExerciseTcx(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportExerciseTcxCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DataPointsServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataPointsServiceSettings dataPointsServiceSettings =
         DataPointsServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DataPointsServiceClient dataPointsServiceClient =
         DataPointsServiceClient.create(dataPointsServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataPointsServiceSettings dataPointsServiceSettings =
         DataPointsServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DataPointsServiceClient dataPointsServiceClient =
         DataPointsServiceClient.create(dataPointsServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataPointsServiceSettings dataPointsServiceSettings =
         DataPointsServiceSettings.newHttpJsonBuilder().build();
     DataPointsServiceClient dataPointsServiceClient =
         DataPointsServiceClient.create(dataPointsServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataPointsServiceClient

## Static Methods 

### create()
    
    
    public static final DataPointsServiceClient create()

Constructs an instance of DataPointsServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DataPointsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataPointsServiceSettings settings)
    
    
    public static final DataPointsServiceClient create(DataPointsServiceSettings settings)

Constructs an instance of DataPointsServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataPointsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataPointsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataPointsServiceStub stub)
    
    
    public static final DataPointsServiceClient create(DataPointsServiceStub stub)

Constructs an instance of DataPointsServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DataPointsServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataPointsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.stub.DataPointsServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataPointsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceClient)` |   
  
## Constructors 

### DataPointsServiceClient(DataPointsServiceSettings settings)
    
    
    protected DataPointsServiceClient(DataPointsServiceSettings settings)

Constructs an instance of DataPointsServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataPointsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceSettings)`  
  
  
### DataPointsServiceClient(DataPointsServiceStub stub)
    
    
    protected DataPointsServiceClient(DataPointsServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataPointsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.stub.DataPointsServiceStub)`  
  
  
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
  
### batchDeleteDataPointsAsync(BatchDeleteDataPointsRequest request)
    
    
    public final OperationFuture<BatchDeleteDataPointsResponse,BatchDeleteDataPointsOperationMetadata> batchDeleteDataPointsAsync(BatchDeleteDataPointsRequest request)

Delete a batch of identifyable data points.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       BatchDeleteDataPointsRequest request =
           BatchDeleteDataPointsRequest.newBuilder()
               .setParent(DataTypeName.of("[USER]", "[DATA_TYPE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeleteDataPointsResponse response =
           dataPointsServiceClient.batchDeleteDataPointsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BatchDeleteDataPointsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchDeleteDataPointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BatchDeleteDataPointsResponse),[BatchDeleteDataPointsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BatchDeleteDataPointsOperationMetadata)>` |   
  
### batchDeleteDataPointsCallable()
    
    
    public final UnaryCallable<BatchDeleteDataPointsRequest,Operation> batchDeleteDataPointsCallable()

Delete a batch of identifyable data points.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       BatchDeleteDataPointsRequest request =
           BatchDeleteDataPointsRequest.newBuilder()
               .setParent(DataTypeName.of("[USER]", "[DATA_TYPE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<Operation> future =
           dataPointsServiceClient.batchDeleteDataPointsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeleteDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BatchDeleteDataPointsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchDeleteDataPointsOperationCallable()
    
    
    public final OperationCallable<BatchDeleteDataPointsRequest,BatchDeleteDataPointsResponse,BatchDeleteDataPointsOperationMetadata> batchDeleteDataPointsOperationCallable()

Delete a batch of identifyable data points.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       BatchDeleteDataPointsRequest request =
           BatchDeleteDataPointsRequest.newBuilder()
               .setParent(DataTypeName.of("[USER]", "[DATA_TYPE]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       OperationFuture<BatchDeleteDataPointsResponse, BatchDeleteDataPointsOperationMetadata>
           future =
               dataPointsServiceClient.batchDeleteDataPointsOperationCallable().futureCall(request);
       // Do something.
       BatchDeleteDataPointsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchDeleteDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BatchDeleteDataPointsRequest),[BatchDeleteDataPointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BatchDeleteDataPointsResponse),[BatchDeleteDataPointsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.BatchDeleteDataPointsOperationMetadata)>` |   
  
### close()
    
    
    public final void close()

### createDataPointAsync(@Nullable DataTypeName parent, DataPoint dataPoint)
    
    
    public final OperationFuture<DataPoint,CreateDataPointOperationMetadata> createDataPointAsync(@Nullable DataTypeName parent, DataPoint dataPoint)

Creates a single identifiable data point.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       DataTypeName parent = DataTypeName.of("[USER]", "[DATA_TYPE]");
       DataPoint dataPoint = DataPoint.newBuilder().build();
       DataPoint response = dataPointsServiceClient.createDataPointAsync(parent, dataPoint).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.DataTypeName`  
Required. The parent resource name where the data point will be created. Format: `users/{user}/dataTypes/{data_type}`  
`dataPoint` | `[DataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPoint)`  
Required. The data point to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPoint),[CreateDataPointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateDataPointOperationMetadata)>` |   
  
### createDataPointAsync(CreateDataPointRequest request)
    
    
    public final OperationFuture<DataPoint,CreateDataPointOperationMetadata> createDataPointAsync(CreateDataPointRequest request)

Creates a single identifiable data point.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       CreateDataPointRequest request =
           CreateDataPointRequest.newBuilder()
               .setParent(DataTypeName.of("[USER]", "[DATA_TYPE]").toString())
               .setDataPoint(DataPoint.newBuilder().build())
               .build();
       DataPoint response = dataPointsServiceClient.createDataPointAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDataPointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateDataPointRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPoint),[CreateDataPointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateDataPointOperationMetadata)>` |   
  
### createDataPointAsync(String parent, DataPoint dataPoint)
    
    
    public final OperationFuture<DataPoint,CreateDataPointOperationMetadata> createDataPointAsync(String parent, DataPoint dataPoint)

Creates a single identifiable data point.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       String parent = DataTypeName.of("[USER]", "[DATA_TYPE]").toString();
       DataPoint dataPoint = DataPoint.newBuilder().build();
       DataPoint response = dataPointsServiceClient.createDataPointAsync(parent, dataPoint).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name where the data point will be created. Format: `users/{user}/dataTypes/{data_type}`  
`dataPoint` | `[DataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPoint)`  
Required. The data point to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPoint),[CreateDataPointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateDataPointOperationMetadata)>` |   
  
### createDataPointCallable()
    
    
    public final UnaryCallable<CreateDataPointRequest,Operation> createDataPointCallable()

Creates a single identifiable data point.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       CreateDataPointRequest request =
           CreateDataPointRequest.newBuilder()
               .setParent(DataTypeName.of("[USER]", "[DATA_TYPE]").toString())
               .setDataPoint(DataPoint.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           dataPointsServiceClient.createDataPointCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDataPointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateDataPointRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDataPointOperationCallable()
    
    
    public final OperationCallable<CreateDataPointRequest,DataPoint,CreateDataPointOperationMetadata> createDataPointOperationCallable()

Creates a single identifiable data point.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       CreateDataPointRequest request =
           CreateDataPointRequest.newBuilder()
               .setParent(DataTypeName.of("[USER]", "[DATA_TYPE]").toString())
               .setDataPoint(DataPoint.newBuilder().build())
               .build();
       OperationFuture<DataPoint, CreateDataPointOperationMetadata> future =
           dataPointsServiceClient.createDataPointOperationCallable().futureCall(request);
       // Do something.
       DataPoint response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateDataPointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateDataPointRequest),[DataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPoint),[CreateDataPointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateDataPointOperationMetadata)>` |   
  
### dailyRollUpDataPoints(DailyRollUpDataPointsRequest request)
    
    
    public final DailyRollUpDataPointsResponse dailyRollUpDataPoints(DailyRollUpDataPointsRequest request)

Roll up data points over civil time intervals for supported data types.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       DailyRollUpDataPointsRequest request =
           DailyRollUpDataPointsRequest.newBuilder()
               .setParent(DataTypeName.of("[USER]", "[DATA_TYPE]").toString())
               .setRange(CivilTimeInterval.newBuilder().build())
               .setWindowSizeDays(1064520774)
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setDataSourceFamily("dataSourceFamily586548265")
               .build();
       DailyRollUpDataPointsResponse response =
           dataPointsServiceClient.dailyRollUpDataPoints(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DailyRollUpDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollUpDataPointsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DailyRollUpDataPointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollUpDataPointsResponse)` |   
  
### dailyRollUpDataPointsCallable()
    
    
    public final UnaryCallable<DailyRollUpDataPointsRequest,DailyRollUpDataPointsResponse> dailyRollUpDataPointsCallable()

Roll up data points over civil time intervals for supported data types.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       DailyRollUpDataPointsRequest request =
           DailyRollUpDataPointsRequest.newBuilder()
               .setParent(DataTypeName.of("[USER]", "[DATA_TYPE]").toString())
               .setRange(CivilTimeInterval.newBuilder().build())
               .setWindowSizeDays(1064520774)
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setDataSourceFamily("dataSourceFamily586548265")
               .build();
       ApiFuture<DailyRollUpDataPointsResponse> future =
           dataPointsServiceClient.dailyRollUpDataPointsCallable().futureCall(request);
       // Do something.
       DailyRollUpDataPointsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DailyRollUpDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollUpDataPointsRequest),[DailyRollUpDataPointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DailyRollUpDataPointsResponse)>` |   
  
### exportExerciseTcx(@Nullable DataPointName name)
    
    
    public final ExportExerciseTcxResponse exportExerciseTcx(@Nullable DataPointName name)

Exports exercise data in TCX format.

**IMPORTANT:** HTTP clients must append `?alt=media` to the request URL to download the raw TCX file.

Example: `<https://health.googleapis.com/v4/users/me/dataTypes/exercise/dataPoints/EXERCISE_ID:exportExerciseTcx?alt=media>`

Without `alt=media`, the server returns a JSON response (`ExportExerciseTcxResponse`) which is intended primarily for gRPC clients.

**Note:** While the Authorization section below states that any one of the listed scopes is accepted, this specific method requires the user to provide both one of the `activity_and_fitness` scopes (`normal` or `readonly`) AND one of the `location` scopes (`normal` or `readonly`) in their access token to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       DataPointName name = DataPointName.of("[USER]", "[DATA_TYPE]", "[DATA_POINT]");
       ExportExerciseTcxResponse response = dataPointsServiceClient.exportExerciseTcx(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.DataPointName`  
Required. The resource name of the exercise data point to export. Format: `users/{user}/dataTypes/exercise/dataPoints/{data_point}` Example: `users/me/dataTypes/exercise/dataPoints/2026443605080188808` The `{user}` is the alias `"me"` currently. Future versions may support user IDs. The `{data_point}` ID maps to the exercise ID, which is a long integer.  
**Returns**  
---  
**Type** | **Description**  
`[ExportExerciseTcxResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ExportExerciseTcxResponse)` |   
  
### exportExerciseTcx(ExportExerciseTcxRequest request)
    
    
    public final ExportExerciseTcxResponse exportExerciseTcx(ExportExerciseTcxRequest request)

Exports exercise data in TCX format.

**IMPORTANT:** HTTP clients must append `?alt=media` to the request URL to download the raw TCX file.

Example: `<https://health.googleapis.com/v4/users/me/dataTypes/exercise/dataPoints/EXERCISE_ID:exportExerciseTcx?alt=media>`

Without `alt=media`, the server returns a JSON response (`ExportExerciseTcxResponse`) which is intended primarily for gRPC clients.

**Note:** While the Authorization section below states that any one of the listed scopes is accepted, this specific method requires the user to provide both one of the `activity_and_fitness` scopes (`normal` or `readonly`) AND one of the `location` scopes (`normal` or `readonly`) in their access token to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       ExportExerciseTcxRequest request =
           ExportExerciseTcxRequest.newBuilder()
               .setName(DataPointName.of("[USER]", "[DATA_TYPE]", "[DATA_POINT]").toString())
               .setPartialData(true)
               .build();
       ExportExerciseTcxResponse response = dataPointsServiceClient.exportExerciseTcx(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportExerciseTcxRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ExportExerciseTcxRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ExportExerciseTcxResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ExportExerciseTcxResponse)` |   
  
### exportExerciseTcx(String name)
    
    
    public final ExportExerciseTcxResponse exportExerciseTcx(String name)

Exports exercise data in TCX format.

**IMPORTANT:** HTTP clients must append `?alt=media` to the request URL to download the raw TCX file.

Example: `<https://health.googleapis.com/v4/users/me/dataTypes/exercise/dataPoints/EXERCISE_ID:exportExerciseTcx?alt=media>`

Without `alt=media`, the server returns a JSON response (`ExportExerciseTcxResponse`) which is intended primarily for gRPC clients.

**Note:** While the Authorization section below states that any one of the listed scopes is accepted, this specific method requires the user to provide both one of the `activity_and_fitness` scopes (`normal` or `readonly`) AND one of the `location` scopes (`normal` or `readonly`) in their access token to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       String name = DataPointName.of("[USER]", "[DATA_TYPE]", "[DATA_POINT]").toString();
       ExportExerciseTcxResponse response = dataPointsServiceClient.exportExerciseTcx(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the exercise data point to export. Format: `users/{user}/dataTypes/exercise/dataPoints/{data_point}` Example: `users/me/dataTypes/exercise/dataPoints/2026443605080188808` The `{user}` is the alias `"me"` currently. Future versions may support user IDs. The `{data_point}` ID maps to the exercise ID, which is a long integer.  
**Returns**  
---  
**Type** | **Description**  
`[ExportExerciseTcxResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ExportExerciseTcxResponse)` |   
  
### exportExerciseTcxCallable()
    
    
    public final UnaryCallable<ExportExerciseTcxRequest,ExportExerciseTcxResponse> exportExerciseTcxCallable()

Exports exercise data in TCX format.

**IMPORTANT:** HTTP clients must append `?alt=media` to the request URL to download the raw TCX file.

Example: `<https://health.googleapis.com/v4/users/me/dataTypes/exercise/dataPoints/EXERCISE_ID:exportExerciseTcx?alt=media>`

Without `alt=media`, the server returns a JSON response (`ExportExerciseTcxResponse`) which is intended primarily for gRPC clients.

**Note:** While the Authorization section below states that any one of the listed scopes is accepted, this specific method requires the user to provide both one of the `activity_and_fitness` scopes (`normal` or `readonly`) AND one of the `location` scopes (`normal` or `readonly`) in their access token to succeed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       ExportExerciseTcxRequest request =
           ExportExerciseTcxRequest.newBuilder()
               .setName(DataPointName.of("[USER]", "[DATA_TYPE]", "[DATA_POINT]").toString())
               .setPartialData(true)
               .build();
       ApiFuture<ExportExerciseTcxResponse> future =
           dataPointsServiceClient.exportExerciseTcxCallable().futureCall(request);
       // Do something.
       ExportExerciseTcxResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportExerciseTcxRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ExportExerciseTcxRequest),[ExportExerciseTcxResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ExportExerciseTcxResponse)>` |   
  
### getDataPoint(@Nullable DataPointName name)
    
    
    public final DataPoint getDataPoint(@Nullable DataPointName name)

Get a single identifyable data point.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       DataPointName name = DataPointName.of("[USER]", "[DATA_TYPE]", "[DATA_POINT]");
       DataPoint response = dataPointsServiceClient.getDataPoint(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.DataPointName`  
Required. The name of the data point to retrieve. Format: `users/{user}/dataTypes/{data_type}/dataPoints/{data_point}` See DataPoint.name for examples and possible values.  
**Returns**  
---  
**Type** | **Description**  
`[DataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPoint)` |   
  
### getDataPoint(GetDataPointRequest request)
    
    
    public final DataPoint getDataPoint(GetDataPointRequest request)

Get a single identifyable data point.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       GetDataPointRequest request =
           GetDataPointRequest.newBuilder()
               .setName(DataPointName.of("[USER]", "[DATA_TYPE]", "[DATA_POINT]").toString())
               .build();
       DataPoint response = dataPointsServiceClient.getDataPoint(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataPointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.GetDataPointRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPoint)` |   
  
### getDataPoint(String name)
    
    
    public final DataPoint getDataPoint(String name)

Get a single identifyable data point.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       String name = DataPointName.of("[USER]", "[DATA_TYPE]", "[DATA_POINT]").toString();
       DataPoint response = dataPointsServiceClient.getDataPoint(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the data point to retrieve. Format: `users/{user}/dataTypes/{data_type}/dataPoints/{data_point}` See DataPoint.name for examples and possible values.  
**Returns**  
---  
**Type** | **Description**  
`[DataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPoint)` |   
  
### getDataPointCallable()
    
    
    public final UnaryCallable<GetDataPointRequest,DataPoint> getDataPointCallable()

Get a single identifyable data point.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       GetDataPointRequest request =
           GetDataPointRequest.newBuilder()
               .setName(DataPointName.of("[USER]", "[DATA_TYPE]", "[DATA_POINT]").toString())
               .build();
       ApiFuture<DataPoint> future =
           dataPointsServiceClient.getDataPointCallable().futureCall(request);
       // Do something.
       DataPoint response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDataPointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.GetDataPointRequest),[DataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPoint)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable DataPointsServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.DataPointsServiceSettings` |   
  
### getStub()
    
    
    public DataPointsServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DataPointsServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.stub.DataPointsServiceStub)` |   
  
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
  
### listDataPoints(@Nullable DataTypeName parent)
    
    
    public final DataPointsServiceClient.ListDataPointsPagedResponse listDataPoints(@Nullable DataTypeName parent)

Query user health and fitness data points.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       DataTypeName parent = DataTypeName.of("[USER]", "[DATA_TYPE]");
       for (DataPoint element : dataPointsServiceClient.listDataPoints(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.devicesandservices.health.v4.DataTypeName`  
Required. Parent data type of the Data Point collection. Format: `users/me/dataTypes/{data_type}`, e.g.: \- `users/me/dataTypes/steps` \- `users/me/dataTypes/weight` For a list of the supported data types see the DataPoint data union field.  
**Returns**  
---  
**Type** | **Description**  
`[DataPointsServiceClient.ListDataPointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceClient.ListDataPointsPagedResponse)` |   
  
### listDataPoints(ListDataPointsRequest request)
    
    
    public final DataPointsServiceClient.ListDataPointsPagedResponse listDataPoints(ListDataPointsRequest request)

Query user health and fitness data points.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       ListDataPointsRequest request =
           ListDataPointsRequest.newBuilder()
               .setParent(DataTypeName.of("[USER]", "[DATA_TYPE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (DataPoint element : dataPointsServiceClient.listDataPoints(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListDataPointsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataPointsServiceClient.ListDataPointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceClient.ListDataPointsPagedResponse)` |   
  
### listDataPoints(String parent)
    
    
    public final DataPointsServiceClient.ListDataPointsPagedResponse listDataPoints(String parent)

Query user health and fitness data points.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       String parent = DataTypeName.of("[USER]", "[DATA_TYPE]").toString();
       for (DataPoint element : dataPointsServiceClient.listDataPoints(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent data type of the Data Point collection. Format: `users/me/dataTypes/{data_type}`, e.g.: \- `users/me/dataTypes/steps` \- `users/me/dataTypes/weight` For a list of the supported data types see the DataPoint data union field.  
**Returns**  
---  
**Type** | **Description**  
`[DataPointsServiceClient.ListDataPointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceClient.ListDataPointsPagedResponse)` |   
  
### listDataPointsCallable()
    
    
    public final UnaryCallable<ListDataPointsRequest,ListDataPointsResponse> listDataPointsCallable()

Query user health and fitness data points.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       ListDataPointsRequest request =
           ListDataPointsRequest.newBuilder()
               .setParent(DataTypeName.of("[USER]", "[DATA_TYPE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListDataPointsResponse response =
             dataPointsServiceClient.listDataPointsCallable().call(request);
         for (DataPoint element : response.getDataPointsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListDataPointsRequest),[ListDataPointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListDataPointsResponse)>` |   
  
### listDataPointsPagedCallable()
    
    
    public final UnaryCallable<ListDataPointsRequest,DataPointsServiceClient.ListDataPointsPagedResponse> listDataPointsPagedCallable()

Query user health and fitness data points.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       ListDataPointsRequest request =
           ListDataPointsRequest.newBuilder()
               .setParent(DataTypeName.of("[USER]", "[DATA_TYPE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<DataPoint> future =
           dataPointsServiceClient.listDataPointsPagedCallable().futureCall(request);
       // Do something.
       for (DataPoint element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListDataPointsRequest),[ListDataPointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceClient.ListDataPointsPagedResponse)>` |   
  
### reconcileDataPoints(ReconcileDataPointsRequest request)
    
    
    public final DataPointsServiceClient.ReconcileDataPointsPagedResponse reconcileDataPoints(ReconcileDataPointsRequest request)

Reconcile data points from multiple data sources into a single data stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       ReconcileDataPointsRequest request =
           ReconcileDataPointsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setDataSourceFamily("dataSourceFamily586548265")
               .build();
       for (ReconciledDataPoint element :
           dataPointsServiceClient.reconcileDataPoints(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReconcileDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ReconcileDataPointsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataPointsServiceClient.ReconcileDataPointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceClient.ReconcileDataPointsPagedResponse)` |   
  
### reconcileDataPointsCallable()
    
    
    public final UnaryCallable<ReconcileDataPointsRequest,ReconcileDataPointsResponse> reconcileDataPointsCallable()

Reconcile data points from multiple data sources into a single data stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       ReconcileDataPointsRequest request =
           ReconcileDataPointsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setDataSourceFamily("dataSourceFamily586548265")
               .build();
       while (true) {
         ReconcileDataPointsResponse response =
             dataPointsServiceClient.reconcileDataPointsCallable().call(request);
         for (ReconciledDataPoint element : response.getDataPointsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReconcileDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ReconcileDataPointsRequest),[ReconcileDataPointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ReconcileDataPointsResponse)>` |   
  
### reconcileDataPointsPagedCallable()
    
    
    public final UnaryCallable<ReconcileDataPointsRequest,DataPointsServiceClient.ReconcileDataPointsPagedResponse> reconcileDataPointsPagedCallable()

Reconcile data points from multiple data sources into a single data stream.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       ReconcileDataPointsRequest request =
           ReconcileDataPointsRequest.newBuilder()
               .setParent("parent-995424086")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setDataSourceFamily("dataSourceFamily586548265")
               .build();
       ApiFuture<ReconciledDataPoint> future =
           dataPointsServiceClient.reconcileDataPointsPagedCallable().futureCall(request);
       // Do something.
       for (ReconciledDataPoint element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReconcileDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ReconcileDataPointsRequest),[ReconcileDataPointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceClient.ReconcileDataPointsPagedResponse)>` |   
  
### rollUpDataPoints(RollUpDataPointsRequest request)
    
    
    public final DataPointsServiceClient.RollUpDataPointsPagedResponse rollUpDataPoints(RollUpDataPointsRequest request)

Roll up data points over physical time intervals for supported data types.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       RollUpDataPointsRequest request =
           RollUpDataPointsRequest.newBuilder()
               .setParent(DataTypeName.of("[USER]", "[DATA_TYPE]").toString())
               .setRange(Interval.newBuilder().build())
               .setWindowSize(Duration.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setDataSourceFamily("dataSourceFamily586548265")
               .build();
       for (RollupDataPoint element :
           dataPointsServiceClient.rollUpDataPoints(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RollUpDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RollUpDataPointsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataPointsServiceClient.RollUpDataPointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceClient.RollUpDataPointsPagedResponse)` |   
  
### rollUpDataPointsCallable()
    
    
    public final UnaryCallable<RollUpDataPointsRequest,RollUpDataPointsResponse> rollUpDataPointsCallable()

Roll up data points over physical time intervals for supported data types.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       RollUpDataPointsRequest request =
           RollUpDataPointsRequest.newBuilder()
               .setParent(DataTypeName.of("[USER]", "[DATA_TYPE]").toString())
               .setRange(Interval.newBuilder().build())
               .setWindowSize(Duration.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setDataSourceFamily("dataSourceFamily586548265")
               .build();
       while (true) {
         RollUpDataPointsResponse response =
             dataPointsServiceClient.rollUpDataPointsCallable().call(request);
         for (RollupDataPoint element : response.getRollupDataPointsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RollUpDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RollUpDataPointsRequest),[RollUpDataPointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RollUpDataPointsResponse)>` |   
  
### rollUpDataPointsPagedCallable()
    
    
    public final UnaryCallable<RollUpDataPointsRequest,DataPointsServiceClient.RollUpDataPointsPagedResponse> rollUpDataPointsPagedCallable()

Roll up data points over physical time intervals for supported data types.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       RollUpDataPointsRequest request =
           RollUpDataPointsRequest.newBuilder()
               .setParent(DataTypeName.of("[USER]", "[DATA_TYPE]").toString())
               .setRange(Interval.newBuilder().build())
               .setWindowSize(Duration.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setDataSourceFamily("dataSourceFamily586548265")
               .build();
       ApiFuture<RollupDataPoint> future =
           dataPointsServiceClient.rollUpDataPointsPagedCallable().futureCall(request);
       // Do something.
       for (RollupDataPoint element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RollUpDataPointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.RollUpDataPointsRequest),[RollUpDataPointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPointsServiceClient.RollUpDataPointsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateDataPointAsync(DataPoint dataPoint)
    
    
    public final OperationFuture<DataPoint,UpdateDataPointOperationMetadata> updateDataPointAsync(DataPoint dataPoint)

Updates a single identifiable data point. If a data point with the specified `name` is not found, the request will fail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       DataPoint dataPoint = DataPoint.newBuilder().build();
       DataPoint response = dataPointsServiceClient.updateDataPointAsync(dataPoint).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`dataPoint` | `[DataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPoint)`  
Required. The data point to update The data point's `name` field is used to identify the data point to update. Format: `users/{user}/dataTypes/{data_type}/dataPoints/{data_point}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPoint),[UpdateDataPointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateDataPointOperationMetadata)>` |   
  
### updateDataPointAsync(UpdateDataPointRequest request)
    
    
    public final OperationFuture<DataPoint,UpdateDataPointOperationMetadata> updateDataPointAsync(UpdateDataPointRequest request)

Updates a single identifiable data point. If a data point with the specified `name` is not found, the request will fail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       UpdateDataPointRequest request =
           UpdateDataPointRequest.newBuilder().setDataPoint(DataPoint.newBuilder().build()).build();
       DataPoint response = dataPointsServiceClient.updateDataPointAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDataPointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateDataPointRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPoint),[UpdateDataPointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateDataPointOperationMetadata)>` |   
  
### updateDataPointCallable()
    
    
    public final UnaryCallable<UpdateDataPointRequest,Operation> updateDataPointCallable()

Updates a single identifiable data point. If a data point with the specified `name` is not found, the request will fail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       UpdateDataPointRequest request =
           UpdateDataPointRequest.newBuilder().setDataPoint(DataPoint.newBuilder().build()).build();
       ApiFuture<Operation> future =
           dataPointsServiceClient.updateDataPointCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDataPointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateDataPointRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateDataPointOperationCallable()
    
    
    public final OperationCallable<UpdateDataPointRequest,DataPoint,UpdateDataPointOperationMetadata> updateDataPointOperationCallable()

Updates a single identifiable data point. If a data point with the specified `name` is not found, the request will fail.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataPointsServiceClient dataPointsServiceClient = DataPointsServiceClient.create()) {
       UpdateDataPointRequest request =
           UpdateDataPointRequest.newBuilder().setDataPoint(DataPoint.newBuilder().build()).build();
       OperationFuture<DataPoint, UpdateDataPointOperationMetadata> future =
           dataPointsServiceClient.updateDataPointOperationCallable().futureCall(request);
       // Do something.
       DataPoint response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateDataPointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateDataPointRequest),[DataPoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataPoint),[UpdateDataPointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateDataPointOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
