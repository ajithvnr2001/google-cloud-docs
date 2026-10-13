---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolTypesClient
title: Class StoragePoolTypesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:28.768989+00:00
---

# Class StoragePoolTypesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolTypesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class StoragePoolTypesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/StoragePoolTypesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The StoragePoolTypes API.

This client uses StoragePoolTypes version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolTypesClient storagePoolTypesClient = StoragePoolTypesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String storagePoolType = "storagePoolType-354080495";
       StoragePoolType response = storagePoolTypesClient.get(project, zone, storagePoolType);
     }
     

Note: close() needs to be called on the StoragePoolTypesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves an aggregated list of storage pool types.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListStoragePoolTypesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Get |  Returns the specified storage pool type. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetStoragePoolTypeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String storagePoolType) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
List |  Retrieves a list of storage pool types available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListStoragePoolTypesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of StoragePoolTypesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     StoragePoolTypesSettings storagePoolTypesSettings =
         StoragePoolTypesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     StoragePoolTypesClient storagePoolTypesClient =
         StoragePoolTypesClient.create(storagePoolTypesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     StoragePoolTypesSettings storagePoolTypesSettings =
         StoragePoolTypesSettings.newBuilder().setEndpoint(myEndpoint).build();
     StoragePoolTypesClient storagePoolTypesClient =
         StoragePoolTypesClient.create(storagePoolTypesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > StoragePoolTypesClient

## Static Methods 

### create()
    
    
    public static final StoragePoolTypesClient create()

Constructs an instance of StoragePoolTypesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[StoragePoolTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolTypesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(StoragePoolTypesSettings settings)
    
    
    public static final StoragePoolTypesClient create(StoragePoolTypesSettings settings)

Constructs an instance of StoragePoolTypesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[StoragePoolTypesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolTypesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StoragePoolTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolTypesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(StoragePoolTypesStub stub)
    
    
    public static final StoragePoolTypesClient create(StoragePoolTypesStub stub)

Constructs an instance of StoragePoolTypesClient, using the given stub for making calls. This is for advanced usage - prefer using create(StoragePoolTypesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[StoragePoolTypesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.StoragePoolTypesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StoragePoolTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolTypesClient)` |   
  
## Constructors 

### StoragePoolTypesClient(StoragePoolTypesSettings settings)
    
    
    protected StoragePoolTypesClient(StoragePoolTypesSettings settings)

Constructs an instance of StoragePoolTypesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[StoragePoolTypesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolTypesSettings)`  
  
  
### StoragePoolTypesClient(StoragePoolTypesStub stub)
    
    
    protected StoragePoolTypesClient(StoragePoolTypesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[StoragePoolTypesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.StoragePoolTypesStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListStoragePoolTypesRequest request)
    
    
    public final StoragePoolTypesClient.AggregatedListPagedResponse aggregatedList(AggregatedListStoragePoolTypesRequest request)

Retrieves an aggregated list of storage pool types.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolTypesClient storagePoolTypesClient = StoragePoolTypesClient.create()) {
       AggregatedListStoragePoolTypesRequest request =
           AggregatedListStoragePoolTypesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, StoragePoolTypesScopedList> element :
           storagePoolTypesClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListStoragePoolTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListStoragePoolTypesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StoragePoolTypesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolTypesClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final StoragePoolTypesClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves an aggregated list of storage pool types.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolTypesClient storagePoolTypesClient = StoragePoolTypesClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, StoragePoolTypesScopedList> element :
           storagePoolTypesClient.aggregatedList(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
**Returns**  
---  
**Type** | **Description**  
`[StoragePoolTypesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolTypesClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListStoragePoolTypesRequest,StoragePoolTypeAggregatedList> aggregatedListCallable()

Retrieves an aggregated list of storage pool types.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolTypesClient storagePoolTypesClient = StoragePoolTypesClient.create()) {
       AggregatedListStoragePoolTypesRequest request =
           AggregatedListStoragePoolTypesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         StoragePoolTypeAggregatedList response =
             storagePoolTypesClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, StoragePoolTypesScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListStoragePoolTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListStoragePoolTypesRequest),[StoragePoolTypeAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolTypeAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListStoragePoolTypesRequest,StoragePoolTypesClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves an aggregated list of storage pool types.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolTypesClient storagePoolTypesClient = StoragePoolTypesClient.create()) {
       AggregatedListStoragePoolTypesRequest request =
           AggregatedListStoragePoolTypesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, StoragePoolTypesScopedList>> future =
           storagePoolTypesClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, StoragePoolTypesScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListStoragePoolTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListStoragePoolTypesRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolTypesClient.AggregatedListPagedResponse)>` |   
  
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

### get(GetStoragePoolTypeRequest request)
    
    
    public final StoragePoolType get(GetStoragePoolTypeRequest request)

Returns the specified storage pool type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolTypesClient storagePoolTypesClient = StoragePoolTypesClient.create()) {
       GetStoragePoolTypeRequest request =
           GetStoragePoolTypeRequest.newBuilder()
               .setProject("project-309310695")
               .setStoragePoolType("storagePoolType-354080495")
               .setZone("zone3744684")
               .build();
       StoragePoolType response = storagePoolTypesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetStoragePoolTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetStoragePoolTypeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StoragePoolType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolType)` |   
  
### get(String project, String zone, String storagePoolType)
    
    
    public final StoragePoolType get(String project, String zone, String storagePoolType)

Returns the specified storage pool type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolTypesClient storagePoolTypesClient = StoragePoolTypesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String storagePoolType = "storagePoolType-354080495";
       StoragePoolType response = storagePoolTypesClient.get(project, zone, storagePoolType);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`storagePoolType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the storage pool type to return.  
**Returns**  
---  
**Type** | **Description**  
`[StoragePoolType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolType)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetStoragePoolTypeRequest,StoragePoolType> getCallable()

Returns the specified storage pool type.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolTypesClient storagePoolTypesClient = StoragePoolTypesClient.create()) {
       GetStoragePoolTypeRequest request =
           GetStoragePoolTypeRequest.newBuilder()
               .setProject("project-309310695")
               .setStoragePoolType("storagePoolType-354080495")
               .setZone("zone3744684")
               .build();
       ApiFuture<StoragePoolType> future = storagePoolTypesClient.getCallable().futureCall(request);
       // Do something.
       StoragePoolType response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetStoragePoolTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetStoragePoolTypeRequest),[StoragePoolType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolType)>` |   
  
### getSettings()
    
    
    public final @Nullable StoragePoolTypesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.StoragePoolTypesSettings` |   
  
### getStub()
    
    
    public StoragePoolTypesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[StoragePoolTypesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.StoragePoolTypesStub)` |   
  
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
  
### list(ListStoragePoolTypesRequest request)
    
    
    public final StoragePoolTypesClient.ListPagedResponse list(ListStoragePoolTypesRequest request)

Retrieves a list of storage pool types available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolTypesClient storagePoolTypesClient = StoragePoolTypesClient.create()) {
       ListStoragePoolTypesRequest request =
           ListStoragePoolTypesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (StoragePoolType element : storagePoolTypesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListStoragePoolTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListStoragePoolTypesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StoragePoolTypesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolTypesClient.ListPagedResponse)` |   
  
### list(String project, String zone)
    
    
    public final StoragePoolTypesClient.ListPagedResponse list(String project, String zone)

Retrieves a list of storage pool types available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolTypesClient storagePoolTypesClient = StoragePoolTypesClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       for (StoragePoolType element : storagePoolTypesClient.list(project, zone).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
**Returns**  
---  
**Type** | **Description**  
`[StoragePoolTypesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolTypesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListStoragePoolTypesRequest,StoragePoolTypeList> listCallable()

Retrieves a list of storage pool types available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolTypesClient storagePoolTypesClient = StoragePoolTypesClient.create()) {
       ListStoragePoolTypesRequest request =
           ListStoragePoolTypesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         StoragePoolTypeList response = storagePoolTypesClient.listCallable().call(request);
         for (StoragePoolType element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListStoragePoolTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListStoragePoolTypesRequest),[StoragePoolTypeList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolTypeList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListStoragePoolTypesRequest,StoragePoolTypesClient.ListPagedResponse> listPagedCallable()

Retrieves a list of storage pool types available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolTypesClient storagePoolTypesClient = StoragePoolTypesClient.create()) {
       ListStoragePoolTypesRequest request =
           ListStoragePoolTypesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<StoragePoolType> future =
           storagePoolTypesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (StoragePoolType element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListStoragePoolTypesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListStoragePoolTypesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolTypesClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
