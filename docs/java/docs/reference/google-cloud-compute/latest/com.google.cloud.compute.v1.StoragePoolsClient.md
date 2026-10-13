---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient
title: Class StoragePoolsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:30.300419+00:00
---

# Class StoragePoolsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class StoragePoolsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/StoragePoolsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The StoragePools API.

This client uses StoragePools version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String storagePool = "storagePool-525690569";
       StoragePool response = storagePoolsClient.get(project, zone, storagePool);
     }
     

Note: close() needs to be called on the StoragePoolsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves an aggregated list of storage pools.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListStoragePoolsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified storage pool. Deleting a storagePool removes its data permanently and is irreversible. However, deleting a storagePool does not delete any snapshots previously made from the storagePool. You must separately delete snapshots. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteStoragePoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String zone, String storagePool) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns a specified storage pool. Gets a list of available storage pools by making a list() request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetStoragePoolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String storagePool) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyStoragePoolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String zone, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
Insert |  Creates a storage pool in the specified project using the data in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertStoragePoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String zone, StoragePool storagePoolResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves a list of storage pools contained within the specified zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListStoragePoolsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListDisks |  Lists the disks in a specified storage pool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listDisks(ListDisksStoragePoolsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listDisks(String project, String zone, String storagePool) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listDisksPagedCallable() 
  * listDisksCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyStoragePoolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String zone, String resource, ZoneSetPolicyRequest zoneSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsStoragePoolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String zone, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
Update |  Updates the specified storagePool with the data included in the request. The update is performed only on selected fields included as part of update-mask. Only the following fields can be modified: pool_provisioned_capacity_gb, pool_provisioned_iops and pool_provisioned_throughput. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAsync(UpdateStoragePoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAsync(String project, String zone, String storagePool, StoragePool storagePoolResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOperationCallable() 
  * updateCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of StoragePoolsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     StoragePoolsSettings storagePoolsSettings =
         StoragePoolsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     StoragePoolsClient storagePoolsClient = StoragePoolsClient.create(storagePoolsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     StoragePoolsSettings storagePoolsSettings =
         StoragePoolsSettings.newBuilder().setEndpoint(myEndpoint).build();
     StoragePoolsClient storagePoolsClient = StoragePoolsClient.create(storagePoolsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > StoragePoolsClient

## Static Methods 

### create()
    
    
    public static final StoragePoolsClient create()

Constructs an instance of StoragePoolsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[StoragePoolsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(StoragePoolsSettings settings)
    
    
    public static final StoragePoolsClient create(StoragePoolsSettings settings)

Constructs an instance of StoragePoolsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[StoragePoolsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StoragePoolsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(StoragePoolsStub stub)
    
    
    public static final StoragePoolsClient create(StoragePoolsStub stub)

Constructs an instance of StoragePoolsClient, using the given stub for making calls. This is for advanced usage - prefer using create(StoragePoolsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[StoragePoolsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.StoragePoolsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StoragePoolsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient)` |   
  
## Constructors 

### StoragePoolsClient(StoragePoolsSettings settings)
    
    
    protected StoragePoolsClient(StoragePoolsSettings settings)

Constructs an instance of StoragePoolsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[StoragePoolsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsSettings)`  
  
  
### StoragePoolsClient(StoragePoolsStub stub)
    
    
    protected StoragePoolsClient(StoragePoolsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[StoragePoolsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.StoragePoolsStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListStoragePoolsRequest request)
    
    
    public final StoragePoolsClient.AggregatedListPagedResponse aggregatedList(AggregatedListStoragePoolsRequest request)

Retrieves an aggregated list of storage pools.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       AggregatedListStoragePoolsRequest request =
           AggregatedListStoragePoolsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, StoragePoolsScopedList> element :
           storagePoolsClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListStoragePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListStoragePoolsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StoragePoolsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final StoragePoolsClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves an aggregated list of storage pools.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, StoragePoolsScopedList> element :
           storagePoolsClient.aggregatedList(project).iterateAll()) {
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
`[StoragePoolsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListStoragePoolsRequest,StoragePoolAggregatedList> aggregatedListCallable()

Retrieves an aggregated list of storage pools.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       AggregatedListStoragePoolsRequest request =
           AggregatedListStoragePoolsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         StoragePoolAggregatedList response =
             storagePoolsClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, StoragePoolsScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListStoragePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListStoragePoolsRequest),[StoragePoolAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListStoragePoolsRequest,StoragePoolsClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves an aggregated list of storage pools.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       AggregatedListStoragePoolsRequest request =
           AggregatedListStoragePoolsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, StoragePoolsScopedList>> future =
           storagePoolsClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, StoragePoolsScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListStoragePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListStoragePoolsRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteStoragePoolRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteStoragePoolRequest request)

Deletes the specified storage pool. Deleting a storagePool removes its data permanently and is irreversible. However, deleting a storagePool does not delete any snapshots previously made from the storagePool. You must separately delete snapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       DeleteStoragePoolRequest request =
           DeleteStoragePoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setStoragePool("storagePool-525690569")
               .setZone("zone3744684")
               .build();
       Operation response = storagePoolsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteStoragePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String zone, String storagePool)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String zone, String storagePool)

Deletes the specified storage pool. Deleting a storagePool removes its data permanently and is irreversible. However, deleting a storagePool does not delete any snapshots previously made from the storagePool. You must separately delete snapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String storagePool = "storagePool-525690569";
       Operation response = storagePoolsClient.deleteAsync(project, zone, storagePool).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`storagePool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the storage pool to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteStoragePoolRequest,Operation> deleteCallable()

Deletes the specified storage pool. Deleting a storagePool removes its data permanently and is irreversible. However, deleting a storagePool does not delete any snapshots previously made from the storagePool. You must separately delete snapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       DeleteStoragePoolRequest request =
           DeleteStoragePoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setStoragePool("storagePool-525690569")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = storagePoolsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteStoragePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteStoragePoolRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified storage pool. Deleting a storagePool removes its data permanently and is irreversible. However, deleting a storagePool does not delete any snapshots previously made from the storagePool. You must separately delete snapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       DeleteStoragePoolRequest request =
           DeleteStoragePoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setStoragePool("storagePool-525690569")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           storagePoolsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteStoragePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetStoragePoolRequest request)
    
    
    public final StoragePool get(GetStoragePoolRequest request)

Returns a specified storage pool. Gets a list of available storage pools by making a list() request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       GetStoragePoolRequest request =
           GetStoragePoolRequest.newBuilder()
               .setProject("project-309310695")
               .setStoragePool("storagePool-525690569")
               .setZone("zone3744684")
               .build();
       StoragePool response = storagePoolsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetStoragePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StoragePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePool)` |   
  
### get(String project, String zone, String storagePool)
    
    
    public final StoragePool get(String project, String zone, String storagePool)

Returns a specified storage pool. Gets a list of available storage pools by making a list() request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String storagePool = "storagePool-525690569";
       StoragePool response = storagePoolsClient.get(project, zone, storagePool);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`storagePool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the storage pool to return.  
**Returns**  
---  
**Type** | **Description**  
`[StoragePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePool)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetStoragePoolRequest,StoragePool> getCallable()

Returns a specified storage pool. Gets a list of available storage pools by making a list() request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       GetStoragePoolRequest request =
           GetStoragePoolRequest.newBuilder()
               .setProject("project-309310695")
               .setStoragePool("storagePool-525690569")
               .setZone("zone3744684")
               .build();
       ApiFuture<StoragePool> future = storagePoolsClient.getCallable().futureCall(request);
       // Do something.
       StoragePool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetStoragePoolRequest),[StoragePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePool)>` |   
  
### getIamPolicy(GetIamPolicyStoragePoolRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyStoragePoolRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       GetIamPolicyStoragePoolRequest request =
           GetIamPolicyStoragePoolRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       Policy response = storagePoolsClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyStoragePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicy(String project, String zone, String resource)
    
    
    public final Policy getIamPolicy(String project, String zone, String resource)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       Policy response = storagePoolsClient.getIamPolicy(project, zone, resource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyStoragePoolRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       GetIamPolicyStoragePoolRequest request =
           GetIamPolicyStoragePoolRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       ApiFuture<Policy> future = storagePoolsClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyStoragePoolRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getSettings()
    
    
    public final @Nullable StoragePoolsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.StoragePoolsSettings` |   
  
### getStub()
    
    
    public StoragePoolsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[StoragePoolsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.StoragePoolsStub)` |   
  
### insertAsync(InsertStoragePoolRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertStoragePoolRequest request)

Creates a storage pool in the specified project using the data in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       InsertStoragePoolRequest request =
           InsertStoragePoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setStoragePoolResource(StoragePool.newBuilder().build())
               .setZone("zone3744684")
               .build();
       Operation response = storagePoolsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertStoragePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String zone, StoragePool storagePoolResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String zone, StoragePool storagePoolResource)

Creates a storage pool in the specified project using the data in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       StoragePool storagePoolResource = StoragePool.newBuilder().build();
       Operation response = storagePoolsClient.insertAsync(project, zone, storagePoolResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`storagePoolResource` | `[StoragePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePool)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertStoragePoolRequest,Operation> insertCallable()

Creates a storage pool in the specified project using the data in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       InsertStoragePoolRequest request =
           InsertStoragePoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setStoragePoolResource(StoragePool.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = storagePoolsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertStoragePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertStoragePoolRequest,Operation,Operation> insertOperationCallable()

Creates a storage pool in the specified project using the data in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       InsertStoragePoolRequest request =
           InsertStoragePoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setStoragePoolResource(StoragePool.newBuilder().build())
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           storagePoolsClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertStoragePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListStoragePoolsRequest request)
    
    
    public final StoragePoolsClient.ListPagedResponse list(ListStoragePoolsRequest request)

Retrieves a list of storage pools contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       ListStoragePoolsRequest request =
           ListStoragePoolsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (StoragePool element : storagePoolsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListStoragePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListStoragePoolsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StoragePoolsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient.ListPagedResponse)` |   
  
### list(String project, String zone)
    
    
    public final StoragePoolsClient.ListPagedResponse list(String project, String zone)

Retrieves a list of storage pools contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       for (StoragePool element : storagePoolsClient.list(project, zone).iterateAll()) {
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
`[StoragePoolsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListStoragePoolsRequest,StoragePoolList> listCallable()

Retrieves a list of storage pools contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       ListStoragePoolsRequest request =
           ListStoragePoolsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         StoragePoolList response = storagePoolsClient.listCallable().call(request);
         for (StoragePool element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListStoragePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListStoragePoolsRequest),[StoragePoolList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolList)>` |   
  
### listDisks(ListDisksStoragePoolsRequest request)
    
    
    public final StoragePoolsClient.ListDisksPagedResponse listDisks(ListDisksStoragePoolsRequest request)

Lists the disks in a specified storage pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       ListDisksStoragePoolsRequest request =
           ListDisksStoragePoolsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setStoragePool("storagePool-525690569")
               .setZone("zone3744684")
               .build();
       for (StoragePoolDisk element : storagePoolsClient.listDisks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDisksStoragePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListDisksStoragePoolsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[StoragePoolsClient.ListDisksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient.ListDisksPagedResponse)` |   
  
### listDisks(String project, String zone, String storagePool)
    
    
    public final StoragePoolsClient.ListDisksPagedResponse listDisks(String project, String zone, String storagePool)

Lists the disks in a specified storage pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String storagePool = "storagePool-525690569";
       for (StoragePoolDisk element :
           storagePoolsClient.listDisks(project, zone, storagePool).iterateAll()) {
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
`storagePool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the storage pool to list disks of.  
**Returns**  
---  
**Type** | **Description**  
`[StoragePoolsClient.ListDisksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient.ListDisksPagedResponse)` |   
  
### listDisksCallable()
    
    
    public final UnaryCallable<ListDisksStoragePoolsRequest,StoragePoolListDisks> listDisksCallable()

Lists the disks in a specified storage pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       ListDisksStoragePoolsRequest request =
           ListDisksStoragePoolsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setStoragePool("storagePool-525690569")
               .setZone("zone3744684")
               .build();
       while (true) {
         StoragePoolListDisks response = storagePoolsClient.listDisksCallable().call(request);
         for (StoragePoolDisk element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDisksStoragePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListDisksStoragePoolsRequest),[StoragePoolListDisks](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolListDisks)>` |   
  
### listDisksPagedCallable()
    
    
    public final UnaryCallable<ListDisksStoragePoolsRequest,StoragePoolsClient.ListDisksPagedResponse> listDisksPagedCallable()

Lists the disks in a specified storage pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       ListDisksStoragePoolsRequest request =
           ListDisksStoragePoolsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setStoragePool("storagePool-525690569")
               .setZone("zone3744684")
               .build();
       ApiFuture<StoragePoolDisk> future =
           storagePoolsClient.listDisksPagedCallable().futureCall(request);
       // Do something.
       for (StoragePoolDisk element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListDisksStoragePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListDisksStoragePoolsRequest),[ListDisksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient.ListDisksPagedResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListStoragePoolsRequest,StoragePoolsClient.ListPagedResponse> listPagedCallable()

Retrieves a list of storage pools contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       ListStoragePoolsRequest request =
           ListStoragePoolsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<StoragePool> future = storagePoolsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (StoragePool element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListStoragePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListStoragePoolsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePoolsClient.ListPagedResponse)>` |   
  
### setIamPolicy(SetIamPolicyStoragePoolRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyStoragePoolRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       SetIamPolicyStoragePoolRequest request =
           SetIamPolicyStoragePoolRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetPolicyRequestResource(ZoneSetPolicyRequest.newBuilder().build())
               .build();
       Policy response = storagePoolsClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyStoragePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicy(String project, String zone, String resource, ZoneSetPolicyRequest zoneSetPolicyRequestResource)
    
    
    public final Policy setIamPolicy(String project, String zone, String resource, ZoneSetPolicyRequest zoneSetPolicyRequestResource)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       ZoneSetPolicyRequest zoneSetPolicyRequestResource = ZoneSetPolicyRequest.newBuilder().build();
       Policy response =
           storagePoolsClient.setIamPolicy(project, zone, resource, zoneSetPolicyRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`zoneSetPolicyRequestResource` | `[ZoneSetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneSetPolicyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyStoragePoolRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       SetIamPolicyStoragePoolRequest request =
           SetIamPolicyStoragePoolRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetPolicyRequestResource(ZoneSetPolicyRequest.newBuilder().build())
               .build();
       ApiFuture<Policy> future = storagePoolsClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyStoragePoolRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsStoragePoolRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsStoragePoolRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       TestIamPermissionsStoragePoolRequest request =
           TestIamPermissionsStoragePoolRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       TestPermissionsResponse response = storagePoolsClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsStoragePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissions(String project, String zone, String resource, TestPermissionsRequest testPermissionsRequestResource)
    
    
    public final TestPermissionsResponse testIamPermissions(String project, String zone, String resource, TestPermissionsRequest testPermissionsRequestResource)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           storagePoolsClient.testIamPermissions(
               project, zone, resource, testPermissionsRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsStoragePoolRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       TestIamPermissionsStoragePoolRequest request =
           TestIamPermissionsStoragePoolRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<TestPermissionsResponse> future =
           storagePoolsClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsStoragePoolRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
### updateAsync(UpdateStoragePoolRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(UpdateStoragePoolRequest request)

Updates the specified storagePool with the data included in the request. The update is performed only on selected fields included as part of update-mask. Only the following fields can be modified: pool_provisioned_capacity_gb, pool_provisioned_iops and pool_provisioned_throughput.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       UpdateStoragePoolRequest request =
           UpdateStoragePoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setStoragePool("storagePool-525690569")
               .setStoragePoolResource(StoragePool.newBuilder().build())
               .setUpdateMask("updateMask-296147115")
               .setZone("zone3744684")
               .build();
       Operation response = storagePoolsClient.updateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateStoragePoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(String project, String zone, String storagePool, StoragePool storagePoolResource)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(String project, String zone, String storagePool, StoragePool storagePoolResource)

Updates the specified storagePool with the data included in the request. The update is performed only on selected fields included as part of update-mask. Only the following fields can be modified: pool_provisioned_capacity_gb, pool_provisioned_iops and pool_provisioned_throughput.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String storagePool = "storagePool-525690569";
       StoragePool storagePoolResource = StoragePool.newBuilder().build();
       Operation response =
           storagePoolsClient.updateAsync(project, zone, storagePool, storagePoolResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`storagePool` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The storagePool name for this request.  
`storagePoolResource` | `[StoragePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StoragePool)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateCallable()
    
    
    public final UnaryCallable<UpdateStoragePoolRequest,Operation> updateCallable()

Updates the specified storagePool with the data included in the request. The update is performed only on selected fields included as part of update-mask. Only the following fields can be modified: pool_provisioned_capacity_gb, pool_provisioned_iops and pool_provisioned_throughput.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       UpdateStoragePoolRequest request =
           UpdateStoragePoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setStoragePool("storagePool-525690569")
               .setStoragePoolResource(StoragePool.newBuilder().build())
               .setUpdateMask("updateMask-296147115")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = storagePoolsClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateStoragePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationCallable()
    
    
    public final OperationCallable<UpdateStoragePoolRequest,Operation,Operation> updateOperationCallable()

Updates the specified storagePool with the data included in the request. The update is performed only on selected fields included as part of update-mask. Only the following fields can be modified: pool_provisioned_capacity_gb, pool_provisioned_iops and pool_provisioned_throughput.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (StoragePoolsClient storagePoolsClient = StoragePoolsClient.create()) {
       UpdateStoragePoolRequest request =
           UpdateStoragePoolRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setStoragePool("storagePool-525690569")
               .setStoragePoolResource(StoragePool.newBuilder().build())
               .setUpdateMask("updateMask-296147115")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           storagePoolsClient.updateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateStoragePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateStoragePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
