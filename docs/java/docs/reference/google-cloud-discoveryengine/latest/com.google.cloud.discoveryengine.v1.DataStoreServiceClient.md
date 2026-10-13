---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient
title: Class DataStoreServiceClient (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:36.445989+00:00
---

# Class DataStoreServiceClient (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataStoreServiceClient (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-discoveryengine/google-cloud-discoveryengine/src/main/java/com/google/cloud/discoveryengine/v1/DataStoreServiceClient.java)| [Product Reference](https://cloud.google.com/discovery-engine/media/docs)  
---|---  
  
Service Description: Service for managing DataStore configuration.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       DataStoreName name =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       DataStore response = dataStoreServiceClient.getDataStore(name);
     }
     

Note: close() needs to be called on the DataStoreServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateDataStore |  Creates a DataStore.  DataStore is for storing Documents. To serve these documents for Search, or Recommendation use case, an Engine needs to be created separately. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDataStoreAsync(CreateDataStoreRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createDataStoreAsync(CollectionName parent, DataStore dataStore, String dataStoreId) 
  * createDataStoreAsync(String parent, DataStore dataStore, String dataStoreId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDataStoreOperationCallable() 
  * createDataStoreCallable() 

  
GetDataStore |  Gets a DataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataStore(GetDataStoreRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataStore(DataStoreName name) 
  * getDataStore(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDataStoreCallable() 

  
ListDataStores |  Lists all the DataStores associated with the project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDataStores(ListDataStoresRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDataStores(CollectionName parent) 
  * listDataStores(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDataStoresPagedCallable() 
  * listDataStoresCallable() 

  
DeleteDataStore |  Deletes a DataStore. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDataStoreAsync(DeleteDataStoreRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteDataStoreAsync(DataStoreName name) 
  * deleteDataStoreAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDataStoreOperationCallable() 
  * deleteDataStoreCallable() 

  
UpdateDataStore |  Updates a DataStore |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDataStore(UpdateDataStoreRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateDataStore(DataStore dataStore, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDataStoreCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DataStoreServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataStoreServiceSettings dataStoreServiceSettings =
         DataStoreServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DataStoreServiceClient dataStoreServiceClient =
         DataStoreServiceClient.create(dataStoreServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataStoreServiceSettings dataStoreServiceSettings =
         DataStoreServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DataStoreServiceClient dataStoreServiceClient =
         DataStoreServiceClient.create(dataStoreServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataStoreServiceSettings dataStoreServiceSettings =
         DataStoreServiceSettings.newHttpJsonBuilder().build();
     DataStoreServiceClient dataStoreServiceClient =
         DataStoreServiceClient.create(dataStoreServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataStoreServiceClient

## Static Methods 

### create()
    
    
    public static final DataStoreServiceClient create()

Constructs an instance of DataStoreServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DataStoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataStoreServiceSettings settings)
    
    
    public static final DataStoreServiceClient create(DataStoreServiceSettings settings)

Constructs an instance of DataStoreServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataStoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataStoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataStoreServiceStub stub)
    
    
    public static final DataStoreServiceClient create(DataStoreServiceStub stub)

Constructs an instance of DataStoreServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DataStoreServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataStoreServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.DataStoreServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataStoreServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient)` |   
  
## Constructors 

### DataStoreServiceClient(DataStoreServiceSettings settings)
    
    
    protected DataStoreServiceClient(DataStoreServiceSettings settings)

Constructs an instance of DataStoreServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataStoreServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceSettings)`  
  
  
### DataStoreServiceClient(DataStoreServiceStub stub)
    
    
    protected DataStoreServiceClient(DataStoreServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataStoreServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.DataStoreServiceStub)`  
  
  
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

### createDataStoreAsync(@Nullable CollectionName parent, DataStore dataStore, String dataStoreId)
    
    
    public final OperationFuture<DataStore,CreateDataStoreMetadata> createDataStoreAsync(@Nullable CollectionName parent, DataStore dataStore, String dataStoreId)

Creates a DataStore.

DataStore is for storing Documents. To serve these documents for Search, or Recommendation use case, an Engine needs to be created separately.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       CollectionName parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]");
       DataStore dataStore = DataStore.newBuilder().build();
       String dataStoreId = "dataStoreId929489618";
       DataStore response =
           dataStoreServiceClient.createDataStoreAsync(parent, dataStore, dataStoreId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.CollectionName`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}`.  
`dataStore` | `[DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore)`  
Required. The DataStore to create.  
`dataStoreId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the DataStore, which will become the final component of the DataStore's resource name. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore),[CreateDataStoreMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreMetadata)>` |   
  
### createDataStoreAsync(CreateDataStoreRequest request)
    
    
    public final OperationFuture<DataStore,CreateDataStoreMetadata> createDataStoreAsync(CreateDataStoreRequest request)

Creates a DataStore.

DataStore is for storing Documents. To serve these documents for Search, or Recommendation use case, an Engine needs to be created separately.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       CreateDataStoreRequest request =
           CreateDataStoreRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setDataStore(DataStore.newBuilder().build())
               .setDataStoreId("dataStoreId929489618")
               .setCreateAdvancedSiteSearch(true)
               .setSkipDefaultSchemaCreation(true)
               .build();
       DataStore response = dataStoreServiceClient.createDataStoreAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore),[CreateDataStoreMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreMetadata)>` |   
  
### createDataStoreAsync(String parent, DataStore dataStore, String dataStoreId)
    
    
    public final OperationFuture<DataStore,CreateDataStoreMetadata> createDataStoreAsync(String parent, DataStore dataStore, String dataStoreId)

Creates a DataStore.

DataStore is for storing Documents. To serve these documents for Search, or Recommendation use case, an Engine needs to be created separately.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       String parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString();
       DataStore dataStore = DataStore.newBuilder().build();
       String dataStoreId = "dataStoreId929489618";
       DataStore response =
           dataStoreServiceClient.createDataStoreAsync(parent, dataStore, dataStoreId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}`.  
`dataStore` | `[DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore)`  
Required. The DataStore to create.  
`dataStoreId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID to use for the DataStore, which will become the final component of the DataStore's resource name. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore),[CreateDataStoreMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreMetadata)>` |   
  
### createDataStoreCallable()
    
    
    public final UnaryCallable<CreateDataStoreRequest,Operation> createDataStoreCallable()

Creates a DataStore.

DataStore is for storing Documents. To serve these documents for Search, or Recommendation use case, an Engine needs to be created separately.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       CreateDataStoreRequest request =
           CreateDataStoreRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setDataStore(DataStore.newBuilder().build())
               .setDataStoreId("dataStoreId929489618")
               .setCreateAdvancedSiteSearch(true)
               .setSkipDefaultSchemaCreation(true)
               .build();
       ApiFuture<Operation> future =
           dataStoreServiceClient.createDataStoreCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDataStoreOperationCallable()
    
    
    public final OperationCallable<CreateDataStoreRequest,DataStore,CreateDataStoreMetadata> createDataStoreOperationCallable()

Creates a DataStore.

DataStore is for storing Documents. To serve these documents for Search, or Recommendation use case, an Engine needs to be created separately.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       CreateDataStoreRequest request =
           CreateDataStoreRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setDataStore(DataStore.newBuilder().build())
               .setDataStoreId("dataStoreId929489618")
               .setCreateAdvancedSiteSearch(true)
               .setSkipDefaultSchemaCreation(true)
               .build();
       OperationFuture<DataStore, CreateDataStoreMetadata> future =
           dataStoreServiceClient.createDataStoreOperationCallable().futureCall(request);
       // Do something.
       DataStore response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateDataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreRequest),[DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore),[CreateDataStoreMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.CreateDataStoreMetadata)>` |   
  
### deleteDataStoreAsync(@Nullable DataStoreName name)
    
    
    public final OperationFuture<Empty,DeleteDataStoreMetadata> deleteDataStoreAsync(@Nullable DataStoreName name)

Deletes a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       DataStoreName name =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       dataStoreServiceClient.deleteDataStoreAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.DataStoreName`  
Required. Full resource name of DataStore, such as `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}`. If the caller does not have permission to delete the DataStore, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the DataStore to delete does not exist, a NOT_FOUND error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteDataStoreMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteDataStoreMetadata)>` |   
  
### deleteDataStoreAsync(DeleteDataStoreRequest request)
    
    
    public final OperationFuture<Empty,DeleteDataStoreMetadata> deleteDataStoreAsync(DeleteDataStoreRequest request)

Deletes a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       DeleteDataStoreRequest request =
           DeleteDataStoreRequest.newBuilder()
               .setName(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .build();
       dataStoreServiceClient.deleteDataStoreAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteDataStoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteDataStoreMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteDataStoreMetadata)>` |   
  
### deleteDataStoreAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteDataStoreMetadata> deleteDataStoreAsync(String name)

Deletes a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       String name =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]")
               .toString();
       dataStoreServiceClient.deleteDataStoreAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of DataStore, such as `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}`. If the caller does not have permission to delete the DataStore, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the DataStore to delete does not exist, a NOT_FOUND error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteDataStoreMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteDataStoreMetadata)>` |   
  
### deleteDataStoreCallable()
    
    
    public final UnaryCallable<DeleteDataStoreRequest,Operation> deleteDataStoreCallable()

Deletes a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       DeleteDataStoreRequest request =
           DeleteDataStoreRequest.newBuilder()
               .setName(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           dataStoreServiceClient.deleteDataStoreCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteDataStoreRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDataStoreOperationCallable()
    
    
    public final OperationCallable<DeleteDataStoreRequest,Empty,DeleteDataStoreMetadata> deleteDataStoreOperationCallable()

Deletes a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       DeleteDataStoreRequest request =
           DeleteDataStoreRequest.newBuilder()
               .setName(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteDataStoreMetadata> future =
           dataStoreServiceClient.deleteDataStoreOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteDataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteDataStoreRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteDataStoreMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DeleteDataStoreMetadata)>` |   
  
### getDataStore(@Nullable DataStoreName name)
    
    
    public final DataStore getDataStore(@Nullable DataStoreName name)

Gets a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       DataStoreName name =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]");
       DataStore response = dataStoreServiceClient.getDataStore(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.DataStoreName`  
Required. Full resource name of DataStore, such as `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}`. If the caller does not have permission to access the DataStore, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the requested DataStore does not exist, a NOT_FOUND error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore)` |   
  
### getDataStore(GetDataStoreRequest request)
    
    
    public final DataStore getDataStore(GetDataStoreRequest request)

Gets a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       GetDataStoreRequest request =
           GetDataStoreRequest.newBuilder()
               .setName(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .build();
       DataStore response = dataStoreServiceClient.getDataStore(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetDataStoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore)` |   
  
### getDataStore(String name)
    
    
    public final DataStore getDataStore(String name)

Gets a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       String name =
           DataStoreName.ofProjectLocationDataStoreName("[PROJECT]", "[LOCATION]", "[DATA_STORE]")
               .toString();
       DataStore response = dataStoreServiceClient.getDataStore(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Full resource name of DataStore, such as `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}`. If the caller does not have permission to access the DataStore, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the requested DataStore does not exist, a NOT_FOUND error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore)` |   
  
### getDataStoreCallable()
    
    
    public final UnaryCallable<GetDataStoreRequest,DataStore> getDataStoreCallable()

Gets a DataStore.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       GetDataStoreRequest request =
           GetDataStoreRequest.newBuilder()
               .setName(
                   DataStoreName.ofProjectLocationDataStoreName(
                           "[PROJECT]", "[LOCATION]", "[DATA_STORE]")
                       .toString())
               .build();
       ApiFuture<DataStore> future =
           dataStoreServiceClient.getDataStoreCallable().futureCall(request);
       // Do something.
       DataStore response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.GetDataStoreRequest),[DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore)>` |   
  
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
    
    
    public final @Nullable DataStoreServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.DataStoreServiceSettings` |   
  
### getStub()
    
    
    public DataStoreServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DataStoreServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.stub.DataStoreServiceStub)` |   
  
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
  
### listDataStores(@Nullable CollectionName parent)
    
    
    public final DataStoreServiceClient.ListDataStoresPagedResponse listDataStores(@Nullable CollectionName parent)

Lists all the DataStores associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       CollectionName parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]");
       for (DataStore element : dataStoreServiceClient.listDataStores(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.discoveryengine.v1.CollectionName`  
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection_id}`. If the caller does not have permission to list DataStores under this location, regardless of whether or not this data store exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[DataStoreServiceClient.ListDataStoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient.ListDataStoresPagedResponse)` |   
  
### listDataStores(ListDataStoresRequest request)
    
    
    public final DataStoreServiceClient.ListDataStoresPagedResponse listDataStores(ListDataStoresRequest request)

Lists all the DataStores associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       ListDataStoresRequest request =
           ListDataStoresRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (DataStore element : dataStoreServiceClient.listDataStores(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataStoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListDataStoresRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataStoreServiceClient.ListDataStoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient.ListDataStoresPagedResponse)` |   
  
### listDataStores(String parent)
    
    
    public final DataStoreServiceClient.ListDataStoresPagedResponse listDataStores(String parent)

Lists all the DataStores associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       String parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString();
       for (DataStore element : dataStoreServiceClient.listDataStores(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection_id}`. If the caller does not have permission to list DataStores under this location, regardless of whether or not this data store exists, a PERMISSION_DENIED error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[DataStoreServiceClient.ListDataStoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient.ListDataStoresPagedResponse)` |   
  
### listDataStoresCallable()
    
    
    public final UnaryCallable<ListDataStoresRequest,ListDataStoresResponse> listDataStoresCallable()

Lists all the DataStores associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       ListDataStoresRequest request =
           ListDataStoresRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListDataStoresResponse response =
             dataStoreServiceClient.listDataStoresCallable().call(request);
         for (DataStore element : response.getDataStoresList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataStoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListDataStoresRequest),[ListDataStoresResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListDataStoresResponse)>` |   
  
### listDataStoresPagedCallable()
    
    
    public final UnaryCallable<ListDataStoresRequest,DataStoreServiceClient.ListDataStoresPagedResponse> listDataStoresPagedCallable()

Lists all the DataStores associated with the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       ListDataStoresRequest request =
           ListDataStoresRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<DataStore> future =
           dataStoreServiceClient.listDataStoresPagedCallable().futureCall(request);
       // Do something.
       for (DataStore element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDataStoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.ListDataStoresRequest),[ListDataStoresPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStoreServiceClient.ListDataStoresPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateDataStore(DataStore dataStore, FieldMask updateMask)
    
    
    public final DataStore updateDataStore(DataStore dataStore, FieldMask updateMask)

Updates a DataStore

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       DataStore dataStore = DataStore.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DataStore response = dataStoreServiceClient.updateDataStore(dataStore, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`dataStore` | `[DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore)`  
Required. The DataStore to update. If the caller does not have permission to update the DataStore, regardless of whether or not it exists, a PERMISSION_DENIED error is returned. If the DataStore to update does not exist, a NOT_FOUND error is returned.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Indicates which fields in the provided DataStore to update. If an unsupported or unknown field is provided, an INVALID_ARGUMENT error is returned.  
**Returns**  
---  
**Type** | **Description**  
`[DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore)` |   
  
### updateDataStore(UpdateDataStoreRequest request)
    
    
    public final DataStore updateDataStore(UpdateDataStoreRequest request)

Updates a DataStore

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       UpdateDataStoreRequest request =
           UpdateDataStoreRequest.newBuilder()
               .setDataStore(DataStore.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       DataStore response = dataStoreServiceClient.updateDataStore(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateDataStoreRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore)` |   
  
### updateDataStoreCallable()
    
    
    public final UnaryCallable<UpdateDataStoreRequest,DataStore> updateDataStoreCallable()

Updates a DataStore

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataStoreServiceClient dataStoreServiceClient = DataStoreServiceClient.create()) {
       UpdateDataStoreRequest request =
           UpdateDataStoreRequest.newBuilder()
               .setDataStore(DataStore.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<DataStore> future =
           dataStoreServiceClient.updateDataStoreCallable().futureCall(request);
       // Do something.
       DataStore response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDataStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.UpdateDataStoreRequest),[DataStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.DataStore)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
