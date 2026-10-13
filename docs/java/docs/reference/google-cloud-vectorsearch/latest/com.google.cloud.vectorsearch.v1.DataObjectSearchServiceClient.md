---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectSearchServiceClient
title: Class DataObjectSearchServiceClient (0.21.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:24.942905+00:00
---

# Class DataObjectSearchServiceClient (0.21.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectSearchServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataObjectSearchServiceClient (0.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.21.0 (latest)  0.17.0  0.16.0  0.15.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-vectorsearch/google-cloud-vectorsearch/src/main/java/com/google/cloud/vectorsearch/v1/DataObjectSearchServiceClient.java)| [Product Reference](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview)  
---|---  
  
Service Description: Service for searching data objects.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create()) {
       AggregateDataObjectsRequest request =
           AggregateDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setFilter(Struct.newBuilder().build())
               .setAggregate(AggregationMethod.forNumber(0))
               .build();
       AggregateDataObjectsResponse response =
           dataObjectSearchServiceClient.aggregateDataObjects(request);
     }
     

Note: close() needs to be called on the DataObjectSearchServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
SearchDataObjects |  Searches data objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchDataObjects(SearchDataObjectsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchDataObjectsPagedCallable() 
  * searchDataObjectsCallable() 

  
QueryDataObjects |  Queries data objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * queryDataObjects(QueryDataObjectsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * queryDataObjectsPagedCallable() 
  * queryDataObjectsCallable() 

  
AggregateDataObjects |  Aggregates data objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregateDataObjects(AggregateDataObjectsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregateDataObjectsCallable() 

  
BatchSearchDataObjects |  Batch searches data objects. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchSearchDataObjects(BatchSearchDataObjectsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchSearchDataObjectsCallable() 

  
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

This class can be customized by passing in a custom instance of DataObjectSearchServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataObjectSearchServiceSettings dataObjectSearchServiceSettings =
         DataObjectSearchServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create(dataObjectSearchServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataObjectSearchServiceSettings dataObjectSearchServiceSettings =
         DataObjectSearchServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create(dataObjectSearchServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataObjectSearchServiceSettings dataObjectSearchServiceSettings =
         DataObjectSearchServiceSettings.newHttpJsonBuilder().build();
     DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create(dataObjectSearchServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataObjectSearchServiceClient

## Static Methods 

### create()
    
    
    public static final DataObjectSearchServiceClient create()

Constructs an instance of DataObjectSearchServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DataObjectSearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectSearchServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataObjectSearchServiceSettings settings)
    
    
    public static final DataObjectSearchServiceClient create(DataObjectSearchServiceSettings settings)

Constructs an instance of DataObjectSearchServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataObjectSearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectSearchServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataObjectSearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectSearchServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataObjectSearchServiceStub stub)
    
    
    public static final DataObjectSearchServiceClient create(DataObjectSearchServiceStub stub)

Constructs an instance of DataObjectSearchServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DataObjectSearchServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataObjectSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.stub.DataObjectSearchServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataObjectSearchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectSearchServiceClient)` |   
  
## Constructors 

### DataObjectSearchServiceClient(DataObjectSearchServiceSettings settings)
    
    
    protected DataObjectSearchServiceClient(DataObjectSearchServiceSettings settings)

Constructs an instance of DataObjectSearchServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataObjectSearchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectSearchServiceSettings)`  
  
  
### DataObjectSearchServiceClient(DataObjectSearchServiceStub stub)
    
    
    protected DataObjectSearchServiceClient(DataObjectSearchServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataObjectSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.stub.DataObjectSearchServiceStub)`  
  
  
## Methods 

### aggregateDataObjects(AggregateDataObjectsRequest request)
    
    
    public final AggregateDataObjectsResponse aggregateDataObjects(AggregateDataObjectsRequest request)

Aggregates data objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create()) {
       AggregateDataObjectsRequest request =
           AggregateDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setFilter(Struct.newBuilder().build())
               .setAggregate(AggregationMethod.forNumber(0))
               .build();
       AggregateDataObjectsResponse response =
           dataObjectSearchServiceClient.aggregateDataObjects(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregateDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.AggregateDataObjectsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AggregateDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.AggregateDataObjectsResponse)` |   
  
### aggregateDataObjectsCallable()
    
    
    public final UnaryCallable<AggregateDataObjectsRequest,AggregateDataObjectsResponse> aggregateDataObjectsCallable()

Aggregates data objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create()) {
       AggregateDataObjectsRequest request =
           AggregateDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setFilter(Struct.newBuilder().build())
               .setAggregate(AggregationMethod.forNumber(0))
               .build();
       ApiFuture<AggregateDataObjectsResponse> future =
           dataObjectSearchServiceClient.aggregateDataObjectsCallable().futureCall(request);
       // Do something.
       AggregateDataObjectsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregateDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.AggregateDataObjectsRequest),[AggregateDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.AggregateDataObjectsResponse)>` |   
  
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
  
### batchSearchDataObjects(BatchSearchDataObjectsRequest request)
    
    
    public final BatchSearchDataObjectsResponse batchSearchDataObjects(BatchSearchDataObjectsRequest request)

Batch searches data objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create()) {
       BatchSearchDataObjectsRequest request =
           BatchSearchDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .addAllSearches(new ArrayList<Search>())
               .setCombine(BatchSearchDataObjectsRequest.CombineResultsOptions.newBuilder().build())
               .build();
       BatchSearchDataObjectsResponse response =
           dataObjectSearchServiceClient.batchSearchDataObjects(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchSearchDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.BatchSearchDataObjectsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchSearchDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.BatchSearchDataObjectsResponse)` |   
  
### batchSearchDataObjectsCallable()
    
    
    public final UnaryCallable<BatchSearchDataObjectsRequest,BatchSearchDataObjectsResponse> batchSearchDataObjectsCallable()

Batch searches data objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create()) {
       BatchSearchDataObjectsRequest request =
           BatchSearchDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .addAllSearches(new ArrayList<Search>())
               .setCombine(BatchSearchDataObjectsRequest.CombineResultsOptions.newBuilder().build())
               .build();
       ApiFuture<BatchSearchDataObjectsResponse> future =
           dataObjectSearchServiceClient.batchSearchDataObjectsCallable().futureCall(request);
       // Do something.
       BatchSearchDataObjectsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchSearchDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.BatchSearchDataObjectsRequest),[BatchSearchDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.BatchSearchDataObjectsResponse)>` |   
  
### close()
    
    
    public final void close()

### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = dataObjectSearchServiceClient.getLocation(request);
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
     try (DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           dataObjectSearchServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSettings()
    
    
    public final @Nullable DataObjectSearchServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.vectorsearch.v1.DataObjectSearchServiceSettings` |   
  
### getStub()
    
    
    public DataObjectSearchServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DataObjectSearchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.stub.DataObjectSearchServiceStub)` |   
  
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
    
    
    public final DataObjectSearchServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : dataObjectSearchServiceClient.listLocations(request).iterateAll()) {
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
`[DataObjectSearchServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectSearchServiceClient.ListLocationsPagedResponse)` |   
  
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
     try (DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             dataObjectSearchServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,DataObjectSearchServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           dataObjectSearchServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectSearchServiceClient.ListLocationsPagedResponse)>` |   
  
### queryDataObjects(QueryDataObjectsRequest request)
    
    
    public final DataObjectSearchServiceClient.QueryDataObjectsPagedResponse queryDataObjects(QueryDataObjectsRequest request)

Queries data objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create()) {
       QueryDataObjectsRequest request =
           QueryDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setFilter(Struct.newBuilder().build())
               .setOutputFields(OutputFields.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (DataObject element :
           dataObjectSearchServiceClient.queryDataObjects(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.QueryDataObjectsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataObjectSearchServiceClient.QueryDataObjectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectSearchServiceClient.QueryDataObjectsPagedResponse)` |   
  
### queryDataObjectsCallable()
    
    
    public final UnaryCallable<QueryDataObjectsRequest,QueryDataObjectsResponse> queryDataObjectsCallable()

Queries data objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create()) {
       QueryDataObjectsRequest request =
           QueryDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setFilter(Struct.newBuilder().build())
               .setOutputFields(OutputFields.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         QueryDataObjectsResponse response =
             dataObjectSearchServiceClient.queryDataObjectsCallable().call(request);
         for (DataObject element : response.getDataObjectsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.QueryDataObjectsRequest),[QueryDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.QueryDataObjectsResponse)>` |   
  
### queryDataObjectsPagedCallable()
    
    
    public final UnaryCallable<QueryDataObjectsRequest,DataObjectSearchServiceClient.QueryDataObjectsPagedResponse> queryDataObjectsPagedCallable()

Queries data objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create()) {
       QueryDataObjectsRequest request =
           QueryDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setFilter(Struct.newBuilder().build())
               .setOutputFields(OutputFields.newBuilder().build())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<DataObject> future =
           dataObjectSearchServiceClient.queryDataObjectsPagedCallable().futureCall(request);
       // Do something.
       for (DataObject element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[QueryDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.QueryDataObjectsRequest),[QueryDataObjectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectSearchServiceClient.QueryDataObjectsPagedResponse)>` |   
  
### searchDataObjects(SearchDataObjectsRequest request)
    
    
    public final DataObjectSearchServiceClient.SearchDataObjectsPagedResponse searchDataObjects(SearchDataObjectsRequest request)

Searches data objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create()) {
       SearchDataObjectsRequest request =
           SearchDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (SearchResult element :
           dataObjectSearchServiceClient.searchDataObjects(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.SearchDataObjectsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataObjectSearchServiceClient.SearchDataObjectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectSearchServiceClient.SearchDataObjectsPagedResponse)` |   
  
### searchDataObjectsCallable()
    
    
    public final UnaryCallable<SearchDataObjectsRequest,SearchDataObjectsResponse> searchDataObjectsCallable()

Searches data objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create()) {
       SearchDataObjectsRequest request =
           SearchDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         SearchDataObjectsResponse response =
             dataObjectSearchServiceClient.searchDataObjectsCallable().call(request);
         for (SearchResult element : response.getResultsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.SearchDataObjectsRequest),[SearchDataObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.SearchDataObjectsResponse)>` |   
  
### searchDataObjectsPagedCallable()
    
    
    public final UnaryCallable<SearchDataObjectsRequest,DataObjectSearchServiceClient.SearchDataObjectsPagedResponse> searchDataObjectsPagedCallable()

Searches data objects.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataObjectSearchServiceClient dataObjectSearchServiceClient =
         DataObjectSearchServiceClient.create()) {
       SearchDataObjectsRequest request =
           SearchDataObjectsRequest.newBuilder()
               .setParent(CollectionName.of("[PROJECT]", "[LOCATION]", "[COLLECTION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<SearchResult> future =
           dataObjectSearchServiceClient.searchDataObjectsPagedCallable().futureCall(request);
       // Do something.
       for (SearchResult element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchDataObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.SearchDataObjectsRequest),[SearchDataObjectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.DataObjectSearchServiceClient.SearchDataObjectsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
