---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectServiceClient
title: Class DataObjectServiceClient (0.21.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:25.351164+00:00
---

# Class DataObjectServiceClient (0.21.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataObjectServiceClient (0.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.21.0 (latest)  0.17.0  0.16.0  0.15.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-vectorsearch/google-cloud-vectorsearch/src/main/java/com/google/cloud/vectorsearch/v1/DataObjectServiceClient.java)| [Product Reference](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview)  
---|---  
  
Service Description: Service for creating and managing data objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       CollectionName parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]");
       DataObject dataObject = DataObject.newBuilder().build();
       String dataObjectId = "dataObjectId1417732740";
       DataObject response =
           dataObjectServiceClient.createDataObject(parent, dataObject, dataObjectId);
     }
     

Note: close() needs to be called on the DataObjectServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateDataObject |  Creates a dataObject. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createDataObject(CreateDataObjectRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createDataObject(CollectionName parent, DataObject dataObject, String dataObjectId) 
  * createDataObject(String parent, DataObject dataObject, String dataObjectId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createDataObjectCallable() 

  
BatchCreateDataObjects |  Creates a batch of dataObjects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCreateDataObjects(BatchCreateDataObjectsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCreateDataObjectsCallable() 

  
GetDataObject |  Gets a data object. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDataObject(GetDataObjectRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDataObject(DataObjectName name) 
  * getDataObject(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDataObjectCallable() 

  
UpdateDataObject |  Updates a dataObject. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateDataObject(UpdateDataObjectRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateDataObject(DataObject dataObject, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateDataObjectCallable() 

  
BatchUpdateDataObjects |  Updates dataObjects in a batch. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchUpdateDataObjects(CollectionName parent, List<UpdateDataObjectRequest> requests) 
  * batchUpdateDataObjects(String parent, List<UpdateDataObjectRequest> requests) 
  * batchUpdateDataObjects(BatchUpdateDataObjectsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchUpdateDataObjectsCallable() 

  
DeleteDataObject |  Deletes a dataObject. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteDataObject(DeleteDataObjectRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteDataObject(DataObjectName name) 
  * deleteDataObject(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteDataObjectCallable() 

  
BatchDeleteDataObjects |  Deletes dataObjects in a batch. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeleteDataObjects(CollectionName parent, List<DeleteDataObjectRequest> requests) 
  * batchDeleteDataObjects(String parent, List<DeleteDataObjectRequest> requests) 
  * batchDeleteDataObjects(BatchDeleteDataObjectsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeleteDataObjectsCallable() 

  
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

This class can be customized by passing in a custom instance of DataObjectServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataObjectServiceSettings dataObjectServiceSettings =
         DataObjectServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DataObjectServiceClient dataObjectServiceClient =
         DataObjectServiceClient.create(dataObjectServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataObjectServiceSettings dataObjectServiceSettings =
         DataObjectServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DataObjectServiceClient dataObjectServiceClient =
         DataObjectServiceClient.create(dataObjectServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataObjectServiceSettings dataObjectServiceSettings =
         DataObjectServiceSettings.newHttpJsonBuilder().build();
     DataObjectServiceClient dataObjectServiceClient =
         DataObjectServiceClient.create(dataObjectServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataObjectServiceClient

## Static Methods 

### create()
    
    
    public static final DataObjectServiceClient create()

Constructs an instance of DataObjectServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DataObjectServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataObjectServiceSettings settings)
    
    
    public static final DataObjectServiceClient create(DataObjectServiceSettings settings)

Constructs an instance of DataObjectServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataObjectServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataObjectServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataObjectServiceStub stub)
    
    
    public static final DataObjectServiceClient create(DataObjectServiceStub stub)

Constructs an instance of DataObjectServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DataObjectServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataObjectServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.stub.DataObjectServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataObjectServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectServiceClient)` |   
  
## Constructors 

### DataObjectServiceClient(DataObjectServiceSettings settings)
    
    
    protected DataObjectServiceClient(DataObjectServiceSettings settings)

Constructs an instance of DataObjectServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataObjectServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectServiceSettings)`  
  
  
### DataObjectServiceClient(DataObjectServiceStub stub)
    
    
    protected DataObjectServiceClient(DataObjectServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataObjectServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.stub.DataObjectServiceStub)`  
  
  
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
  
### batchCreateDataObjects(BatchCreateDataObjectsRequest request)
    
    
    public final BatchCreateDataObjectsResponse batchCreateDataObjects(BatchCreateDataObjectsRequest request)

Creates a batch of dataObjects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       BatchCreateDataObjectsRequest request =
           BatchCreateDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .addAllRequests(new ArrayList<CreateDataObjectRequest>())
               .build();
       BatchCreateDataObjectsResponse response =
           dataObjectServiceClient.batchCreateDataObjects(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.BatchCreateDataObjectsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.BatchCreateDataObjectsResponse)` |   
  
### batchCreateDataObjectsCallable()
    
    
    public final UnaryCallable<BatchCreateDataObjectsRequest,BatchCreateDataObjectsResponse> batchCreateDataObjectsCallable()

Creates a batch of dataObjects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       BatchCreateDataObjectsRequest request =
           BatchCreateDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .addAllRequests(new ArrayList<CreateDataObjectRequest>())
               .build();
       ApiFuture<BatchCreateDataObjectsResponse> future =
           dataObjectServiceClient.batchCreateDataObjectsCallable().futureCall(request);
       // Do something.
       BatchCreateDataObjectsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCreateDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.BatchCreateDataObjectsRequest),[BatchCreateDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.BatchCreateDataObjectsResponse)>` |   
  
### batchDeleteDataObjects(@Nullable CollectionName parent, List<DeleteDataObjectRequest> requests)
    
    
    public final void batchDeleteDataObjects(@Nullable CollectionName parent, List<DeleteDataObjectRequest> requests)

Deletes dataObjects in a batch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       CollectionName parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]");
       List<DeleteDataObjectRequest> requests = new ArrayList<>();
       dataObjectServiceClient.batchDeleteDataObjects(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vectorsearch.v1.CollectionName`  
Required. The resource name of the Collection to delete the DataObjects in. Format: `projects/{project}/locations/{location}/collections/{collection}`.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DeleteDataObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DeleteDataObjectRequest)>`  
Required. The request message specifying the resources to delete. A maximum of 1000 DataObjects can be deleted in a batch.  
  
### batchDeleteDataObjects(BatchDeleteDataObjectsRequest request)
    
    
    public final void batchDeleteDataObjects(BatchDeleteDataObjectsRequest request)

Deletes dataObjects in a batch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       BatchDeleteDataObjectsRequest request =
           BatchDeleteDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .addAllRequests(new ArrayList<DeleteDataObjectRequest>())
               .build();
       dataObjectServiceClient.batchDeleteDataObjects(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeleteDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.BatchDeleteDataObjectsRequest)`  
The request object containing all of the parameters for the API call.  
  
### batchDeleteDataObjects(String parent, List<DeleteDataObjectRequest> requests)
    
    
    public final void batchDeleteDataObjects(String parent, List<DeleteDataObjectRequest> requests)

Deletes dataObjects in a batch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       String parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString();
       List<DeleteDataObjectRequest> requests = new ArrayList<>();
       dataObjectServiceClient.batchDeleteDataObjects(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Collection to delete the DataObjects in. Format: `projects/{project}/locations/{location}/collections/{collection}`.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DeleteDataObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DeleteDataObjectRequest)>`  
Required. The request message specifying the resources to delete. A maximum of 1000 DataObjects can be deleted in a batch.  
  
### batchDeleteDataObjectsCallable()
    
    
    public final UnaryCallable<BatchDeleteDataObjectsRequest,Empty> batchDeleteDataObjectsCallable()

Deletes dataObjects in a batch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       BatchDeleteDataObjectsRequest request =
           BatchDeleteDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .addAllRequests(new ArrayList<DeleteDataObjectRequest>())
               .build();
       ApiFuture<Empty> future =
           dataObjectServiceClient.batchDeleteDataObjectsCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeleteDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.BatchDeleteDataObjectsRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### batchUpdateDataObjects(@Nullable CollectionName parent, List<UpdateDataObjectRequest> requests)
    
    
    public final BatchUpdateDataObjectsResponse batchUpdateDataObjects(@Nullable CollectionName parent, List<UpdateDataObjectRequest> requests)

Updates dataObjects in a batch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       CollectionName parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]");
       List<UpdateDataObjectRequest> requests = new ArrayList<>();
       BatchUpdateDataObjectsResponse response =
           dataObjectServiceClient.batchUpdateDataObjects(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vectorsearch.v1.CollectionName`  
Required. The resource name of the Collection to update the DataObjects in. Format: `projects/{project}/locations/{location}/collections/{collection}`. The parent field in the UpdateDataObjectRequest messages must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateDataObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.UpdateDataObjectRequest)>`  
Required. The request message specifying the resources to update. A maximum of 1000 DataObjects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.BatchUpdateDataObjectsResponse)` |   
  
### batchUpdateDataObjects(BatchUpdateDataObjectsRequest request)
    
    
    public final BatchUpdateDataObjectsResponse batchUpdateDataObjects(BatchUpdateDataObjectsRequest request)

Updates dataObjects in a batch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       BatchUpdateDataObjectsRequest request =
           BatchUpdateDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .addAllRequests(new ArrayList<UpdateDataObjectRequest>())
               .build();
       BatchUpdateDataObjectsResponse response =
           dataObjectServiceClient.batchUpdateDataObjects(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchUpdateDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.BatchUpdateDataObjectsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.BatchUpdateDataObjectsResponse)` |   
  
### batchUpdateDataObjects(String parent, List<UpdateDataObjectRequest> requests)
    
    
    public final BatchUpdateDataObjectsResponse batchUpdateDataObjects(String parent, List<UpdateDataObjectRequest> requests)

Updates dataObjects in a batch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       String parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString();
       List<UpdateDataObjectRequest> requests = new ArrayList<>();
       BatchUpdateDataObjectsResponse response =
           dataObjectServiceClient.batchUpdateDataObjects(parent, requests);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Collection to update the DataObjects in. Format: `projects/{project}/locations/{location}/collections/{collection}`. The parent field in the UpdateDataObjectRequest messages must match this field.  
`requests` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UpdateDataObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.UpdateDataObjectRequest)>`  
Required. The request message specifying the resources to update. A maximum of 1000 DataObjects can be updated in a batch.  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.BatchUpdateDataObjectsResponse)` |   
  
### batchUpdateDataObjectsCallable()
    
    
    public final UnaryCallable<BatchUpdateDataObjectsRequest,BatchUpdateDataObjectsResponse> batchUpdateDataObjectsCallable()

Updates dataObjects in a batch.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       BatchUpdateDataObjectsRequest request =
           BatchUpdateDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .addAllRequests(new ArrayList<UpdateDataObjectRequest>())
               .build();
       ApiFuture<BatchUpdateDataObjectsResponse> future =
           dataObjectServiceClient.batchUpdateDataObjectsCallable().futureCall(request);
       // Do something.
       BatchUpdateDataObjectsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchUpdateDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.BatchUpdateDataObjectsRequest),[BatchUpdateDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.BatchUpdateDataObjectsResponse)>` |   
  
### close()
    
    
    public final void close()

### createDataObject(@Nullable CollectionName parent, DataObject dataObject, String dataObjectId)
    
    
    public final DataObject createDataObject(@Nullable CollectionName parent, DataObject dataObject, String dataObjectId)

Creates a dataObject.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       CollectionName parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]");
       DataObject dataObject = DataObject.newBuilder().build();
       String dataObjectId = "dataObjectId1417732740";
       DataObject response =
           dataObjectServiceClient.createDataObject(parent, dataObject, dataObjectId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vectorsearch.v1.CollectionName`  
Required. The resource name of the Collection to create the DataObject in. Format: `projects/{project}/locations/{location}/collections/{collection}`  
`dataObject` | `[DataObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObject)`  
Required. The DataObject to create.  
`dataObjectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The id of the dataObject to create. The id must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, it must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectServiceClient?:\[-a-z0-9\]{0,61}\[a-z0-9\])?`.  
**Returns**  
---  
**Type** | **Description**  
`[DataObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObject)` |   
  
### createDataObject(CreateDataObjectRequest request)
    
    
    public final DataObject createDataObject(CreateDataObjectRequest request)

Creates a dataObject.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       CreateDataObjectRequest request =
           CreateDataObjectRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setDataObjectId("dataObjectId1417732740")
               .setDataObject(DataObject.newBuilder().build())
               .build();
       DataObject response = dataObjectServiceClient.createDataObject(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDataObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.CreateDataObjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObject)` |   
  
### createDataObject(String parent, DataObject dataObject, String dataObjectId)
    
    
    public final DataObject createDataObject(String parent, DataObject dataObject, String dataObjectId)

Creates a dataObject.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       String parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString();
       DataObject dataObject = DataObject.newBuilder().build();
       String dataObjectId = "dataObjectId1417732740";
       DataObject response =
           dataObjectServiceClient.createDataObject(parent, dataObject, dataObjectId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Collection to create the DataObject in. Format: `projects/{project}/locations/{location}/collections/{collection}`  
`dataObject` | `[DataObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObject)`  
Required. The DataObject to create.  
`dataObjectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The id of the dataObject to create. The id must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, it must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectServiceClient?:\[-a-z0-9\]{0,61}\[a-z0-9\])?`.  
**Returns**  
---  
**Type** | **Description**  
`[DataObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObject)` |   
  
### createDataObjectCallable()
    
    
    public final UnaryCallable<CreateDataObjectRequest,DataObject> createDataObjectCallable()

Creates a dataObject.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       CreateDataObjectRequest request =
           CreateDataObjectRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setDataObjectId("dataObjectId1417732740")
               .setDataObject(DataObject.newBuilder().build())
               .build();
       ApiFuture<DataObject> future =
           dataObjectServiceClient.createDataObjectCallable().futureCall(request);
       // Do something.
       DataObject response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateDataObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.CreateDataObjectRequest),[DataObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObject)>` |   
  
### deleteDataObject(@Nullable DataObjectName name)
    
    
    public final void deleteDataObject(@Nullable DataObjectName name)

Deletes a dataObject.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       DataObjectName name =
           DataObjectName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATAOBJECT]");
       dataObjectServiceClient.deleteDataObject(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vectorsearch.v1.DataObjectName`  
Required. The name of the DataObject resource to be deleted. Format: `projects/{project}/locations/{location}/collections/{collection}/dataObjects/{dataObject}`  
  
### deleteDataObject(DeleteDataObjectRequest request)
    
    
    public final void deleteDataObject(DeleteDataObjectRequest request)

Deletes a dataObject.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       DeleteDataObjectRequest request =
           DeleteDataObjectRequest.newBuilder()
               .setName(
                   DataObjectName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATAOBJECT]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       dataObjectServiceClient.deleteDataObject(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDataObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DeleteDataObjectRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteDataObject(String name)
    
    
    public final void deleteDataObject(String name)

Deletes a dataObject.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       String name =
           DataObjectName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATAOBJECT]").toString();
       dataObjectServiceClient.deleteDataObject(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the DataObject resource to be deleted. Format: `projects/{project}/locations/{location}/collections/{collection}/dataObjects/{dataObject}`  
  
### deleteDataObjectCallable()
    
    
    public final UnaryCallable<DeleteDataObjectRequest,Empty> deleteDataObjectCallable()

Deletes a dataObject.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       DeleteDataObjectRequest request =
           DeleteDataObjectRequest.newBuilder()
               .setName(
                   DataObjectName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATAOBJECT]")
                       .toString())
               .setEtag("etag3123477")
               .build();
       ApiFuture<Empty> future =
           dataObjectServiceClient.deleteDataObjectCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteDataObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DeleteDataObjectRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDataObject(@Nullable DataObjectName name)
    
    
    public final DataObject getDataObject(@Nullable DataObjectName name)

Gets a data object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       DataObjectName name =
           DataObjectName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATAOBJECT]");
       DataObject response = dataObjectServiceClient.getDataObject(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vectorsearch.v1.DataObjectName`  
Required. The name of the DataObject resource. Format: `projects/{project}/locations/{location}/collections/{collection}/dataObjects/{dataObject}`  
**Returns**  
---  
**Type** | **Description**  
`[DataObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObject)` |   
  
### getDataObject(GetDataObjectRequest request)
    
    
    public final DataObject getDataObject(GetDataObjectRequest request)

Gets a data object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       GetDataObjectRequest request =
           GetDataObjectRequest.newBuilder()
               .setName(
                   DataObjectName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATAOBJECT]")
                       .toString())
               .build();
       DataObject response = dataObjectServiceClient.getDataObject(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.GetDataObjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObject)` |   
  
### getDataObject(String name)
    
    
    public final DataObject getDataObject(String name)

Gets a data object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       String name =
           DataObjectName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATAOBJECT]").toString();
       DataObject response = dataObjectServiceClient.getDataObject(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the DataObject resource. Format: `projects/{project}/locations/{location}/collections/{collection}/dataObjects/{dataObject}`  
**Returns**  
---  
**Type** | **Description**  
`[DataObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObject)` |   
  
### getDataObjectCallable()
    
    
    public final UnaryCallable<GetDataObjectRequest,DataObject> getDataObjectCallable()

Gets a data object.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       GetDataObjectRequest request =
           GetDataObjectRequest.newBuilder()
               .setName(
                   DataObjectName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[DATAOBJECT]")
                       .toString())
               .build();
       ApiFuture<DataObject> future =
           dataObjectServiceClient.getDataObjectCallable().futureCall(request);
       // Do something.
       DataObject response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDataObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.GetDataObjectRequest),[DataObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObject)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = dataObjectServiceClient.getLocation(request);
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
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           dataObjectServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable DataObjectServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.vectorsearch.v1.DataObjectServiceSettings` |   
  
### getStub()
    
    
    public DataObjectServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DataObjectServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.stub.DataObjectServiceStub)` |   
  
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
  
### listLocations(ListLocationsRequest request)
    
    
    public final DataObjectServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : dataObjectServiceClient.listLocations(request).iterateAll()) {
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
`[DataObjectServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectServiceClient.ListLocationsPagedResponse)` |   
  
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
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             dataObjectServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,DataObjectServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           dataObjectServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectServiceClient.ListLocationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateDataObject(DataObject dataObject, FieldMask updateMask)
    
    
    public final DataObject updateDataObject(DataObject dataObject, FieldMask updateMask)

Updates a dataObject.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       DataObject dataObject = DataObject.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       DataObject response = dataObjectServiceClient.updateDataObject(dataObject, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`dataObject` | `[DataObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObject)`  
Required. The DataObject which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. The update mask applies to the resource. See google.protobuf.FieldMask.  
**Returns**  
---  
**Type** | **Description**  
`[DataObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObject)` |   
  
### updateDataObject(UpdateDataObjectRequest request)
    
    
    public final DataObject updateDataObject(UpdateDataObjectRequest request)

Updates a dataObject.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       UpdateDataObjectRequest request =
           UpdateDataObjectRequest.newBuilder()
               .setDataObject(DataObject.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       DataObject response = dataObjectServiceClient.updateDataObject(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDataObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.UpdateDataObjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObject)` |   
  
### updateDataObjectCallable()
    
    
    public final UnaryCallable<UpdateDataObjectRequest,DataObject> updateDataObjectCallable()

Updates a dataObject.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectServiceClient dataObjectServiceClient = DataObjectServiceClient.create()) {
       UpdateDataObjectRequest request =
           UpdateDataObjectRequest.newBuilder()
               .setDataObject(DataObject.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<DataObject> future =
           dataObjectServiceClient.updateDataObjectCallable().futureCall(request);
       // Do something.
       DataObject response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateDataObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.UpdateDataObjectRequest),[DataObject](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObject)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
