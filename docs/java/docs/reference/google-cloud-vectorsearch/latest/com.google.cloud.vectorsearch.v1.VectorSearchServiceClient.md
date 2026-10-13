---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient
title: Class VectorSearchServiceClient (0.21.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:26.380687+00:00
---

# Class VectorSearchServiceClient (0.21.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class VectorSearchServiceClient (0.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.21.0 (latest)  0.17.0  0.16.0  0.15.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-vectorsearch/google-cloud-vectorsearch/src/main/java/com/google/cloud/vectorsearch/v1/VectorSearchServiceClient.java)| [Product Reference](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview)  
---|---  
  
Service Description: VectorSearchService provides methods for managing Collection resources, and Collection Index resources. The primary resources offered by this service are Collections which are a container for a set of related JSON data objects, and Collection Indexes which enable efficient ANN search across data objects within a Collection.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       CollectionName name = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]");
       Collection response = vectorSearchServiceClient.getCollection(name);
     }
     

Note: close() needs to be called on the VectorSearchServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
ListCollections |  Lists Collections in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCollections(ListCollectionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCollections(LocationName parent) 
  * listCollections(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCollectionsPagedCallable() 
  * listCollectionsCallable() 

  
GetCollection |  Gets details of a single Collection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCollection(GetCollectionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCollection(CollectionName name) 
  * getCollection(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCollectionCallable() 

  
CreateCollection |  Creates a new Collection in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCollectionAsync(CreateCollectionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createCollectionAsync(LocationName parent, Collection collection, String collectionId) 
  * createCollectionAsync(String parent, Collection collection, String collectionId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCollectionOperationCallable() 
  * createCollectionCallable() 

  
UpdateCollection |  Updates the parameters of a single Collection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateCollectionAsync(UpdateCollectionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateCollectionAsync(Collection collection, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateCollectionOperationCallable() 
  * updateCollectionCallable() 

  
DeleteCollection |  Deletes a single Collection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteCollectionAsync(DeleteCollectionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteCollectionAsync(CollectionName name) 
  * deleteCollectionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCollectionOperationCallable() 
  * deleteCollectionCallable() 

  
ListIndexes |  Lists Indexes in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listIndexes(ListIndexesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listIndexes(CollectionName parent) 
  * listIndexes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listIndexesPagedCallable() 
  * listIndexesCallable() 

  
GetIndex |  Gets details of a single Index. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIndex(GetIndexRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIndex(IndexName name) 
  * getIndex(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIndexCallable() 

  
CreateIndex |  Creates a new Index in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createIndexAsync(CreateIndexRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createIndexAsync(CollectionName parent, Index index, String indexId) 
  * createIndexAsync(String parent, Index index, String indexId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createIndexOperationCallable() 
  * createIndexCallable() 

  
UpdateIndex |  Updates the parameters of a single Index. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateIndexAsync(UpdateIndexRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateIndexAsync(Index index, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateIndexOperationCallable() 
  * updateIndexCallable() 

  
DeleteIndex |  Deletes a single Index. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteIndexAsync(DeleteIndexRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteIndexAsync(IndexName name) 
  * deleteIndexAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteIndexOperationCallable() 
  * deleteIndexCallable() 

  
ImportDataObjects |  Initiates a Long-Running Operation to import DataObjects into a Collection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * importDataObjectsAsync(ImportDataObjectsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * importDataObjectsOperationCallable() 
  * importDataObjectsCallable() 

  
ExportDataObjects |  Initiates a Long-Running Operation to export DataObjects from a Collection. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * exportDataObjectsAsync(ExportDataObjectsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * exportDataObjectsOperationCallable() 
  * exportDataObjectsCallable() 

  
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

This class can be customized by passing in a custom instance of VectorSearchServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VectorSearchServiceSettings vectorSearchServiceSettings =
         VectorSearchServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     VectorSearchServiceClient vectorSearchServiceClient =
         VectorSearchServiceClient.create(vectorSearchServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VectorSearchServiceSettings vectorSearchServiceSettings =
         VectorSearchServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     VectorSearchServiceClient vectorSearchServiceClient =
         VectorSearchServiceClient.create(vectorSearchServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     VectorSearchServiceSettings vectorSearchServiceSettings =
         VectorSearchServiceSettings.newHttpJsonBuilder().build();
     VectorSearchServiceClient vectorSearchServiceClient =
         VectorSearchServiceClient.create(vectorSearchServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > VectorSearchServiceClient

## Static Methods 

### create()
    
    
    public static final VectorSearchServiceClient create()

Constructs an instance of VectorSearchServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[VectorSearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(VectorSearchServiceSettings settings)
    
    
    public static final VectorSearchServiceClient create(VectorSearchServiceSettings settings)

Constructs an instance of VectorSearchServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[VectorSearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VectorSearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(VectorSearchServiceStub stub)
    
    
    public static final VectorSearchServiceClient create(VectorSearchServiceStub stub)

Constructs an instance of VectorSearchServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(VectorSearchServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[VectorSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.stub.VectorSearchServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VectorSearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient)` |   
  
## Constructors 

### VectorSearchServiceClient(VectorSearchServiceSettings settings)
    
    
    protected VectorSearchServiceClient(VectorSearchServiceSettings settings)

Constructs an instance of VectorSearchServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[VectorSearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceSettings)`  
  
  
### VectorSearchServiceClient(VectorSearchServiceStub stub)
    
    
    protected VectorSearchServiceClient(VectorSearchServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[VectorSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.stub.VectorSearchServiceStub)`  
  
  
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

### createCollectionAsync(@Nullable LocationName parent, Collection collection, String collectionId)
    
    
    public final OperationFuture<Collection,OperationMetadata> createCollectionAsync(@Nullable LocationName parent, Collection collection, String collectionId)

Creates a new Collection in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Collection collection = Collection.newBuilder().build();
       String collectionId = "collectionId1636075609";
       Collection response =
           vectorSearchServiceClient.createCollectionAsync(parent, collection, collectionId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vectorsearch.v1.LocationName`  
Required. Value for parent.  
`collection` | `[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Collection)`  
Required. The resource being created  
`collectionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the Collection to create. The id must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, it must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient?:\[-a-z0-9\]{0,61}\[a-z0-9\])?`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Collection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### createCollectionAsync(CreateCollectionRequest request)
    
    
    public final OperationFuture<Collection,OperationMetadata> createCollectionAsync(CreateCollectionRequest request)

Creates a new Collection in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       CreateCollectionRequest request =
           CreateCollectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setCollectionId("collectionId1636075609")
               .setCollection(Collection.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Collection response = vectorSearchServiceClient.createCollectionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCollectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.CreateCollectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Collection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### createCollectionAsync(String parent, Collection collection, String collectionId)
    
    
    public final OperationFuture<Collection,OperationMetadata> createCollectionAsync(String parent, Collection collection, String collectionId)

Creates a new Collection in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Collection collection = Collection.newBuilder().build();
       String collectionId = "collectionId1636075609";
       Collection response =
           vectorSearchServiceClient.createCollectionAsync(parent, collection, collectionId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Value for parent.  
`collection` | `[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Collection)`  
Required. The resource being created  
`collectionId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the Collection to create. The id must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, it must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient?:\[-a-z0-9\]{0,61}\[a-z0-9\])?`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Collection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### createCollectionCallable()
    
    
    public final UnaryCallable<CreateCollectionRequest,Operation> createCollectionCallable()

Creates a new Collection in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       CreateCollectionRequest request =
           CreateCollectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setCollectionId("collectionId1636075609")
               .setCollection(Collection.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vectorSearchServiceClient.createCollectionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCollectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.CreateCollectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createCollectionOperationCallable()
    
    
    public final OperationCallable<CreateCollectionRequest,Collection,OperationMetadata> createCollectionOperationCallable()

Creates a new Collection in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       CreateCollectionRequest request =
           CreateCollectionRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setCollectionId("collectionId1636075609")
               .setCollection(Collection.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Collection, OperationMetadata> future =
           vectorSearchServiceClient.createCollectionOperationCallable().futureCall(request);
       // Do something.
       Collection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateCollectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.CreateCollectionRequest),[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Collection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### createIndexAsync(@Nullable CollectionName parent, Index index, String indexId)
    
    
    public final OperationFuture<Index,OperationMetadata> createIndexAsync(@Nullable CollectionName parent, Index index, String indexId)

Creates a new Index in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       CollectionName parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]");
       Index index = Index.newBuilder().build();
       String indexId = "indexId1943291277";
       Index response = vectorSearchServiceClient.createIndexAsync(parent, index, indexId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vectorsearch.v1.CollectionName`  
Required. The resource name of the Collection for which to create the Index. Format: `projects/{project}/locations/{location}/collections/{collection}`  
`index` | `[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Index)`  
Required. The resource being created  
`indexId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the Index to create. The id must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, it must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient?:\[-a-z0-9\]{0,61}\[a-z0-9\])?`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Index),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### createIndexAsync(CreateIndexRequest request)
    
    
    public final OperationFuture<Index,OperationMetadata> createIndexAsync(CreateIndexRequest request)

Creates a new Index in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       CreateIndexRequest request =
           CreateIndexRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setIndexId("indexId1943291277")
               .setIndex(Index.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Index response = vectorSearchServiceClient.createIndexAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.CreateIndexRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Index),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### createIndexAsync(String parent, Index index, String indexId)
    
    
    public final OperationFuture<Index,OperationMetadata> createIndexAsync(String parent, Index index, String indexId)

Creates a new Index in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       String parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString();
       Index index = Index.newBuilder().build();
       String indexId = "indexId1943291277";
       Index response = vectorSearchServiceClient.createIndexAsync(parent, index, indexId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Collection for which to create the Index. Format: `projects/{project}/locations/{location}/collections/{collection}`  
`index` | `[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Index)`  
Required. The resource being created  
`indexId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the Index to create. The id must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, it must be 1-63 characters long and match the regular expression `[a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient?:\[-a-z0-9\]{0,61}\[a-z0-9\])?`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Index),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### createIndexCallable()
    
    
    public final UnaryCallable<CreateIndexRequest,Operation> createIndexCallable()

Creates a new Index in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       CreateIndexRequest request =
           CreateIndexRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setIndexId("indexId1943291277")
               .setIndex(Index.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vectorSearchServiceClient.createIndexCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.CreateIndexRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createIndexOperationCallable()
    
    
    public final OperationCallable<CreateIndexRequest,Index,OperationMetadata> createIndexOperationCallable()

Creates a new Index in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       CreateIndexRequest request =
           CreateIndexRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setIndexId("indexId1943291277")
               .setIndex(Index.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Index, OperationMetadata> future =
           vectorSearchServiceClient.createIndexOperationCallable().futureCall(request);
       // Do something.
       Index response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.CreateIndexRequest),[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Index),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### deleteCollectionAsync(@Nullable CollectionName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteCollectionAsync(@Nullable CollectionName name)

Deletes a single Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       CollectionName name = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]");
       vectorSearchServiceClient.deleteCollectionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vectorsearch.v1.CollectionName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### deleteCollectionAsync(DeleteCollectionRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteCollectionAsync(DeleteCollectionRequest request)

Deletes a single Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       DeleteCollectionRequest request =
           DeleteCollectionRequest.newBuilder()
               .setName(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       vectorSearchServiceClient.deleteCollectionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCollectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DeleteCollectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### deleteCollectionAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteCollectionAsync(String name)

Deletes a single Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       String name = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString();
       vectorSearchServiceClient.deleteCollectionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### deleteCollectionCallable()
    
    
    public final UnaryCallable<DeleteCollectionRequest,Operation> deleteCollectionCallable()

Deletes a single Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       DeleteCollectionRequest request =
           DeleteCollectionRequest.newBuilder()
               .setName(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           vectorSearchServiceClient.deleteCollectionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteCollectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DeleteCollectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteCollectionOperationCallable()
    
    
    public final OperationCallable<DeleteCollectionRequest,Empty,OperationMetadata> deleteCollectionOperationCallable()

Deletes a single Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       DeleteCollectionRequest request =
           DeleteCollectionRequest.newBuilder()
               .setName(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setRequestId("requestId693933066")
               .setForce(true)
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           vectorSearchServiceClient.deleteCollectionOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteCollectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DeleteCollectionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### deleteIndexAsync(@Nullable IndexName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteIndexAsync(@Nullable IndexName name)

Deletes a single Index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       IndexName name = IndexName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[INDEX]");
       vectorSearchServiceClient.deleteIndexAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vectorsearch.v1.IndexName`  
Required. The resource name of the Index to delete. Format: `projects/{project}/locations/{location}/collections/{collection}/indexes/{index}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### deleteIndexAsync(DeleteIndexRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteIndexAsync(DeleteIndexRequest request)

Deletes a single Index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       DeleteIndexRequest request =
           DeleteIndexRequest.newBuilder()
               .setName(
                   IndexName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[INDEX]").toString())
               .setRequestId("requestId693933066")
               .build();
       vectorSearchServiceClient.deleteIndexAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DeleteIndexRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### deleteIndexAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteIndexAsync(String name)

Deletes a single Index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       String name = IndexName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[INDEX]").toString();
       vectorSearchServiceClient.deleteIndexAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Index to delete. Format: `projects/{project}/locations/{location}/collections/{collection}/indexes/{index}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### deleteIndexCallable()
    
    
    public final UnaryCallable<DeleteIndexRequest,Operation> deleteIndexCallable()

Deletes a single Index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       DeleteIndexRequest request =
           DeleteIndexRequest.newBuilder()
               .setName(
                   IndexName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[INDEX]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vectorSearchServiceClient.deleteIndexCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DeleteIndexRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteIndexOperationCallable()
    
    
    public final OperationCallable<DeleteIndexRequest,Empty,OperationMetadata> deleteIndexOperationCallable()

Deletes a single Index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       DeleteIndexRequest request =
           DeleteIndexRequest.newBuilder()
               .setName(
                   IndexName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[INDEX]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           vectorSearchServiceClient.deleteIndexOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DeleteIndexRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### exportDataObjectsAsync(ExportDataObjectsRequest request)
    
    
    public final OperationFuture<ExportDataObjectsResponse,ExportDataObjectsMetadata> exportDataObjectsAsync(ExportDataObjectsRequest request)

Initiates a Long-Running Operation to export DataObjects from a Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       ExportDataObjectsRequest request =
           ExportDataObjectsRequest.newBuilder()
               .setName(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setFieldFilter(ExportDataObjectsRequest.FieldFilter.newBuilder().build())
               .build();
       ExportDataObjectsResponse response =
           vectorSearchServiceClient.exportDataObjectsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ExportDataObjectsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ExportDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ExportDataObjectsResponse),[ExportDataObjectsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ExportDataObjectsMetadata)>` |   
  
### exportDataObjectsCallable()
    
    
    public final UnaryCallable<ExportDataObjectsRequest,Operation> exportDataObjectsCallable()

Initiates a Long-Running Operation to export DataObjects from a Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       ExportDataObjectsRequest request =
           ExportDataObjectsRequest.newBuilder()
               .setName(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setFieldFilter(ExportDataObjectsRequest.FieldFilter.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           vectorSearchServiceClient.exportDataObjectsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExportDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ExportDataObjectsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### exportDataObjectsOperationCallable()
    
    
    public final OperationCallable<ExportDataObjectsRequest,ExportDataObjectsResponse,ExportDataObjectsMetadata> exportDataObjectsOperationCallable()

Initiates a Long-Running Operation to export DataObjects from a Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       ExportDataObjectsRequest request =
           ExportDataObjectsRequest.newBuilder()
               .setName(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setFieldFilter(ExportDataObjectsRequest.FieldFilter.newBuilder().build())
               .build();
       OperationFuture<ExportDataObjectsResponse, ExportDataObjectsMetadata> future =
           vectorSearchServiceClient.exportDataObjectsOperationCallable().futureCall(request);
       // Do something.
       ExportDataObjectsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ExportDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ExportDataObjectsRequest),[ExportDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ExportDataObjectsResponse),[ExportDataObjectsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ExportDataObjectsMetadata)>` |   
  
### getCollection(@Nullable CollectionName name)
    
    
    public final Collection getCollection(@Nullable CollectionName name)

Gets details of a single Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       CollectionName name = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]");
       Collection response = vectorSearchServiceClient.getCollection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vectorsearch.v1.CollectionName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Collection)` |   
  
### getCollection(GetCollectionRequest request)
    
    
    public final Collection getCollection(GetCollectionRequest request)

Gets details of a single Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       GetCollectionRequest request =
           GetCollectionRequest.newBuilder()
               .setName(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .build();
       Collection response = vectorSearchServiceClient.getCollection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCollectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.GetCollectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Collection)` |   
  
### getCollection(String name)
    
    
    public final Collection getCollection(String name)

Gets details of a single Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       String name = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString();
       Collection response = vectorSearchServiceClient.getCollection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Collection)` |   
  
### getCollectionCallable()
    
    
    public final UnaryCallable<GetCollectionRequest,Collection> getCollectionCallable()

Gets details of a single Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       GetCollectionRequest request =
           GetCollectionRequest.newBuilder()
               .setName(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .build();
       ApiFuture<Collection> future =
           vectorSearchServiceClient.getCollectionCallable().futureCall(request);
       // Do something.
       Collection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCollectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.GetCollectionRequest),[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Collection)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getIndex(@Nullable IndexName name)
    
    
    public final Index getIndex(@Nullable IndexName name)

Gets details of a single Index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       IndexName name = IndexName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[INDEX]");
       Index response = vectorSearchServiceClient.getIndex(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.vectorsearch.v1.IndexName`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Index)` |   
  
### getIndex(GetIndexRequest request)
    
    
    public final Index getIndex(GetIndexRequest request)

Gets details of a single Index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       GetIndexRequest request =
           GetIndexRequest.newBuilder()
               .setName(
                   IndexName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[INDEX]").toString())
               .build();
       Index response = vectorSearchServiceClient.getIndex(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.GetIndexRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Index)` |   
  
### getIndex(String name)
    
    
    public final Index getIndex(String name)

Gets details of a single Index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       String name = IndexName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[INDEX]").toString();
       Index response = vectorSearchServiceClient.getIndex(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the resource  
**Returns**  
---  
**Type** | **Description**  
`[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Index)` |   
  
### getIndexCallable()
    
    
    public final UnaryCallable<GetIndexRequest,Index> getIndexCallable()

Gets details of a single Index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       GetIndexRequest request =
           GetIndexRequest.newBuilder()
               .setName(
                   IndexName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]", "[INDEX]").toString())
               .build();
       ApiFuture<Index> future = vectorSearchServiceClient.getIndexCallable().futureCall(request);
       // Do something.
       Index response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.GetIndexRequest),[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Index)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = vectorSearchServiceClient.getLocation(request);
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
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           vectorSearchServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable VectorSearchServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.vectorsearch.v1.VectorSearchServiceSettings` |   
  
### getStub()
    
    
    public VectorSearchServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[VectorSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.stub.VectorSearchServiceStub)` |   
  
### importDataObjectsAsync(ImportDataObjectsRequest request)
    
    
    public final OperationFuture<ImportDataObjectsResponse,ImportDataObjectsMetadata> importDataObjectsAsync(ImportDataObjectsRequest request)

Initiates a Long-Running Operation to import DataObjects into a Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       ImportDataObjectsRequest request =
           ImportDataObjectsRequest.newBuilder()
               .setName(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .build();
       ImportDataObjectsResponse response =
           vectorSearchServiceClient.importDataObjectsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ImportDataObjectsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ImportDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ImportDataObjectsResponse),[ImportDataObjectsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ImportDataObjectsMetadata)>` |   
  
### importDataObjectsCallable()
    
    
    public final UnaryCallable<ImportDataObjectsRequest,Operation> importDataObjectsCallable()

Initiates a Long-Running Operation to import DataObjects into a Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       ImportDataObjectsRequest request =
           ImportDataObjectsRequest.newBuilder()
               .setName(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .build();
       ApiFuture<Operation> future =
           vectorSearchServiceClient.importDataObjectsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ImportDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ImportDataObjectsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### importDataObjectsOperationCallable()
    
    
    public final OperationCallable<ImportDataObjectsRequest,ImportDataObjectsResponse,ImportDataObjectsMetadata> importDataObjectsOperationCallable()

Initiates a Long-Running Operation to import DataObjects into a Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       ImportDataObjectsRequest request =
           ImportDataObjectsRequest.newBuilder()
               .setName(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .build();
       OperationFuture<ImportDataObjectsResponse, ImportDataObjectsMetadata> future =
           vectorSearchServiceClient.importDataObjectsOperationCallable().futureCall(request);
       // Do something.
       ImportDataObjectsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ImportDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ImportDataObjectsRequest),[ImportDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ImportDataObjectsResponse),[ImportDataObjectsMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ImportDataObjectsMetadata)>` |   
  
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
  
### listCollections(@Nullable LocationName parent)
    
    
    public final VectorSearchServiceClient.ListCollectionsPagedResponse listCollections(@Nullable LocationName parent)

Lists Collections in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Collection element : vectorSearchServiceClient.listCollections(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vectorsearch.v1.LocationName`  
Required. Parent value for ListCollectionsRequest  
**Returns**  
---  
**Type** | **Description**  
`[VectorSearchServiceClient.ListCollectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient.ListCollectionsPagedResponse)` |   
  
### listCollections(ListCollectionsRequest request)
    
    
    public final VectorSearchServiceClient.ListCollectionsPagedResponse listCollections(ListCollectionsRequest request)

Lists Collections in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       ListCollectionsRequest request =
           ListCollectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Collection element : vectorSearchServiceClient.listCollections(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCollectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ListCollectionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VectorSearchServiceClient.ListCollectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient.ListCollectionsPagedResponse)` |   
  
### listCollections(String parent)
    
    
    public final VectorSearchServiceClient.ListCollectionsPagedResponse listCollections(String parent)

Lists Collections in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Collection element : vectorSearchServiceClient.listCollections(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListCollectionsRequest  
**Returns**  
---  
**Type** | **Description**  
`[VectorSearchServiceClient.ListCollectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient.ListCollectionsPagedResponse)` |   
  
### listCollectionsCallable()
    
    
    public final UnaryCallable<ListCollectionsRequest,ListCollectionsResponse> listCollectionsCallable()

Lists Collections in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       ListCollectionsRequest request =
           ListCollectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListCollectionsResponse response =
             vectorSearchServiceClient.listCollectionsCallable().call(request);
         for (Collection element : response.getCollectionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCollectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ListCollectionsRequest),[ListCollectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ListCollectionsResponse)>` |   
  
### listCollectionsPagedCallable()
    
    
    public final UnaryCallable<ListCollectionsRequest,VectorSearchServiceClient.ListCollectionsPagedResponse> listCollectionsPagedCallable()

Lists Collections in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       ListCollectionsRequest request =
           ListCollectionsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Collection> future =
           vectorSearchServiceClient.listCollectionsPagedCallable().futureCall(request);
       // Do something.
       for (Collection element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCollectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ListCollectionsRequest),[ListCollectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient.ListCollectionsPagedResponse)>` |   
  
### listIndexes(@Nullable CollectionName parent)
    
    
    public final VectorSearchServiceClient.ListIndexesPagedResponse listIndexes(@Nullable CollectionName parent)

Lists Indexes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       CollectionName parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]");
       for (Index element : vectorSearchServiceClient.listIndexes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.vectorsearch.v1.CollectionName`  
Required. Parent value for ListIndexesRequest  
**Returns**  
---  
**Type** | **Description**  
`[VectorSearchServiceClient.ListIndexesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient.ListIndexesPagedResponse)` |   
  
### listIndexes(ListIndexesRequest request)
    
    
    public final VectorSearchServiceClient.ListIndexesPagedResponse listIndexes(ListIndexesRequest request)

Lists Indexes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       ListIndexesRequest request =
           ListIndexesRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Index element : vectorSearchServiceClient.listIndexes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListIndexesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ListIndexesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[VectorSearchServiceClient.ListIndexesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient.ListIndexesPagedResponse)` |   
  
### listIndexes(String parent)
    
    
    public final VectorSearchServiceClient.ListIndexesPagedResponse listIndexes(String parent)

Lists Indexes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       String parent = CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString();
       for (Index element : vectorSearchServiceClient.listIndexes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent value for ListIndexesRequest  
**Returns**  
---  
**Type** | **Description**  
`[VectorSearchServiceClient.ListIndexesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient.ListIndexesPagedResponse)` |   
  
### listIndexesCallable()
    
    
    public final UnaryCallable<ListIndexesRequest,ListIndexesResponse> listIndexesCallable()

Lists Indexes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       ListIndexesRequest request =
           ListIndexesRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListIndexesResponse response =
             vectorSearchServiceClient.listIndexesCallable().call(request);
         for (Index element : response.getIndexesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListIndexesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ListIndexesRequest),[ListIndexesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ListIndexesResponse)>` |   
  
### listIndexesPagedCallable()
    
    
    public final UnaryCallable<ListIndexesRequest,VectorSearchServiceClient.ListIndexesPagedResponse> listIndexesPagedCallable()

Lists Indexes in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       ListIndexesRequest request =
           ListIndexesRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Index> future =
           vectorSearchServiceClient.listIndexesPagedCallable().futureCall(request);
       // Do something.
       for (Index element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListIndexesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.ListIndexesRequest),[ListIndexesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient.ListIndexesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final VectorSearchServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : vectorSearchServiceClient.listLocations(request).iterateAll()) {
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
`[VectorSearchServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient.ListLocationsPagedResponse)` |   
  
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
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             vectorSearchServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,VectorSearchServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           vectorSearchServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.VectorSearchServiceClient.ListLocationsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateCollectionAsync(Collection collection, FieldMask updateMask)
    
    
    public final OperationFuture<Collection,OperationMetadata> updateCollectionAsync(Collection collection, FieldMask updateMask)

Updates the parameters of a single Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       Collection collection = Collection.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Collection response =
           vectorSearchServiceClient.updateCollectionAsync(collection, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`collection` | `[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Collection)`  
Required. The resource being updated  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Collection resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields present in the request will be overwritten. The following fields support update: `display_name`, `description`, `labels`, `data_schema`, `vector_schema`. For `data_schema` and `vector_schema`, fields can only be added, not deleted, but `vertex_embedding_config` in `vector_schema` can be added or removed. Partial updates for `data_schema` and `vector_schema` are also supported by using sub-field paths in `update_mask`, e.g. `data_schema.properties.foo` or `vector_schema.my_vector_field`. If `*` is provided in the update_mask, full replacement will be performed.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Collection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### updateCollectionAsync(UpdateCollectionRequest request)
    
    
    public final OperationFuture<Collection,OperationMetadata> updateCollectionAsync(UpdateCollectionRequest request)

Updates the parameters of a single Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       UpdateCollectionRequest request =
           UpdateCollectionRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setCollection(Collection.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Collection response = vectorSearchServiceClient.updateCollectionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCollectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.UpdateCollectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Collection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### updateCollectionCallable()
    
    
    public final UnaryCallable<UpdateCollectionRequest,Operation> updateCollectionCallable()

Updates the parameters of a single Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       UpdateCollectionRequest request =
           UpdateCollectionRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setCollection(Collection.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vectorSearchServiceClient.updateCollectionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateCollectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.UpdateCollectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateCollectionOperationCallable()
    
    
    public final OperationCallable<UpdateCollectionRequest,Collection,OperationMetadata> updateCollectionOperationCallable()

Updates the parameters of a single Collection.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       UpdateCollectionRequest request =
           UpdateCollectionRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setCollection(Collection.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Collection, OperationMetadata> future =
           vectorSearchServiceClient.updateCollectionOperationCallable().futureCall(request);
       // Do something.
       Collection response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateCollectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.UpdateCollectionRequest),[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Collection),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### updateIndexAsync(Index index, FieldMask updateMask)
    
    
    public final OperationFuture<Index,OperationMetadata> updateIndexAsync(Index index, FieldMask updateMask)

Updates the parameters of a single Index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       Index index = Index.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Index response = vectorSearchServiceClient.updateIndexAsync(index, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`index` | `[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Index)`  
Required. The resource being updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Specifies the fields to be overwritten in the Index resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields present in the request with non-empty values will be overwritten. The following fields support update: * `display_name` * `description` * `labels` * `dedicated_infrastructure.autoscaling_spec.min_replica_count` * `dedicated_infrastructure.autoscaling_spec.max_replica_count` If `*` is provided in the `update_mask`, full replacement of mutable fields will be performed.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Index),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### updateIndexAsync(UpdateIndexRequest request)
    
    
    public final OperationFuture<Index,OperationMetadata> updateIndexAsync(UpdateIndexRequest request)

Updates the parameters of a single Index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       UpdateIndexRequest request =
           UpdateIndexRequest.newBuilder()
               .setIndex(Index.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Index response = vectorSearchServiceClient.updateIndexAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.UpdateIndexRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Index),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
### updateIndexCallable()
    
    
    public final UnaryCallable<UpdateIndexRequest,Operation> updateIndexCallable()

Updates the parameters of a single Index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       UpdateIndexRequest request =
           UpdateIndexRequest.newBuilder()
               .setIndex(Index.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           vectorSearchServiceClient.updateIndexCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.UpdateIndexRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateIndexOperationCallable()
    
    
    public final OperationCallable<UpdateIndexRequest,Index,OperationMetadata> updateIndexOperationCallable()

Updates the parameters of a single Index.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (VectorSearchServiceClient vectorSearchServiceClient = VectorSearchServiceClient.create()) {
       UpdateIndexRequest request =
           UpdateIndexRequest.newBuilder()
               .setIndex(Index.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Index, OperationMetadata> future =
           vectorSearchServiceClient.updateIndexOperationCallable().futureCall(request);
       // Do something.
       Index response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.UpdateIndexRequest),[Index](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.Index),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
