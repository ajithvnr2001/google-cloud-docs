---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotsClient
title: Class InstantSnapshotsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:43.342566+00:00
---

# Class InstantSnapshotsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InstantSnapshotsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/InstantSnapshotsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The InstantSnapshots API.

This client uses InstantSnapshots version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instantSnapshot = "instantSnapshot800321221";
       InstantSnapshot response = instantSnapshotsClient.get(project, zone, instantSnapshot);
     }
     

Note: close() needs to be called on the InstantSnapshotsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves an aggregated list of instantSnapshots.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListInstantSnapshotsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified InstantSnapshot resource. Keep in mind that deleting a single instantSnapshot might not necessarily delete all the data on that instantSnapshot. If any data on the instantSnapshot that is marked for deletion is needed for subsequent instantSnapshots, the data will be moved to the next corresponding instantSnapshot.  For more information, seeDeleting instantSnapshots. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteInstantSnapshotRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String zone, String instantSnapshot) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified InstantSnapshot resource in the specified zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetInstantSnapshotRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String instantSnapshot) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyInstantSnapshotRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String zone, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
Insert |  Creates an instant snapshot in the specified zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertInstantSnapshotRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String zone, InstantSnapshot instantSnapshotResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of InstantSnapshot resources contained within the specified zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListInstantSnapshotsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyInstantSnapshotRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String zone, String resource, ZoneSetPolicyRequest zoneSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
SetLabels |  Sets the labels on a instantSnapshot in the given zone. To learn more about labels, read the Labeling Resources documentation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setLabelsAsync(SetLabelsInstantSnapshotRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setLabelsAsync(String project, String zone, String resource, ZoneSetLabelsRequest zoneSetLabelsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setLabelsOperationCallable() 
  * setLabelsCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsInstantSnapshotRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String zone, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of InstantSnapshotsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InstantSnapshotsSettings instantSnapshotsSettings =
         InstantSnapshotsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     InstantSnapshotsClient instantSnapshotsClient =
         InstantSnapshotsClient.create(instantSnapshotsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InstantSnapshotsSettings instantSnapshotsSettings =
         InstantSnapshotsSettings.newBuilder().setEndpoint(myEndpoint).build();
     InstantSnapshotsClient instantSnapshotsClient =
         InstantSnapshotsClient.create(instantSnapshotsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > InstantSnapshotsClient

## Static Methods 

### create()
    
    
    public static final InstantSnapshotsClient create()

Constructs an instance of InstantSnapshotsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[InstantSnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InstantSnapshotsSettings settings)
    
    
    public static final InstantSnapshotsClient create(InstantSnapshotsSettings settings)

Constructs an instance of InstantSnapshotsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InstantSnapshotsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantSnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InstantSnapshotsStub stub)
    
    
    public static final InstantSnapshotsClient create(InstantSnapshotsStub stub)

Constructs an instance of InstantSnapshotsClient, using the given stub for making calls. This is for advanced usage - prefer using create(InstantSnapshotsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InstantSnapshotsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InstantSnapshotsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantSnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotsClient)` |   
  
## Constructors 

### InstantSnapshotsClient(InstantSnapshotsSettings settings)
    
    
    protected InstantSnapshotsClient(InstantSnapshotsSettings settings)

Constructs an instance of InstantSnapshotsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InstantSnapshotsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotsSettings)`  
  
  
### InstantSnapshotsClient(InstantSnapshotsStub stub)
    
    
    protected InstantSnapshotsClient(InstantSnapshotsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InstantSnapshotsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InstantSnapshotsStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListInstantSnapshotsRequest request)
    
    
    public final InstantSnapshotsClient.AggregatedListPagedResponse aggregatedList(AggregatedListInstantSnapshotsRequest request)

Retrieves an aggregated list of instantSnapshots.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       AggregatedListInstantSnapshotsRequest request =
           AggregatedListInstantSnapshotsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, InstantSnapshotsScopedList> element :
           instantSnapshotsClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListInstantSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstantSnapshotsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstantSnapshotsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotsClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final InstantSnapshotsClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves an aggregated list of instantSnapshots.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, InstantSnapshotsScopedList> element :
           instantSnapshotsClient.aggregatedList(project).iterateAll()) {
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
`[InstantSnapshotsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotsClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListInstantSnapshotsRequest,InstantSnapshotAggregatedList> aggregatedListCallable()

Retrieves an aggregated list of instantSnapshots.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       AggregatedListInstantSnapshotsRequest request =
           AggregatedListInstantSnapshotsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         InstantSnapshotAggregatedList response =
             instantSnapshotsClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, InstantSnapshotsScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListInstantSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstantSnapshotsRequest),[InstantSnapshotAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListInstantSnapshotsRequest,InstantSnapshotsClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves an aggregated list of instantSnapshots.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       AggregatedListInstantSnapshotsRequest request =
           AggregatedListInstantSnapshotsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, InstantSnapshotsScopedList>> future =
           instantSnapshotsClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, InstantSnapshotsScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListInstantSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstantSnapshotsRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotsClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteInstantSnapshotRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteInstantSnapshotRequest request)

Deletes the specified InstantSnapshot resource. Keep in mind that deleting a single instantSnapshot might not necessarily delete all the data on that instantSnapshot. If any data on the instantSnapshot that is marked for deletion is needed for subsequent instantSnapshots, the data will be moved to the next corresponding instantSnapshot.

For more information, seeDeleting instantSnapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       DeleteInstantSnapshotRequest request =
           DeleteInstantSnapshotRequest.newBuilder()
               .setInstantSnapshot("instantSnapshot800321221")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instantSnapshotsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstantSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String zone, String instantSnapshot)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String zone, String instantSnapshot)

Deletes the specified InstantSnapshot resource. Keep in mind that deleting a single instantSnapshot might not necessarily delete all the data on that instantSnapshot. If any data on the instantSnapshot that is marked for deletion is needed for subsequent instantSnapshots, the data will be moved to the next corresponding instantSnapshot.

For more information, seeDeleting instantSnapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instantSnapshot = "instantSnapshot800321221";
       Operation response = instantSnapshotsClient.deleteAsync(project, zone, instantSnapshot).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instantSnapshot` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the InstantSnapshot resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteInstantSnapshotRequest,Operation> deleteCallable()

Deletes the specified InstantSnapshot resource. Keep in mind that deleting a single instantSnapshot might not necessarily delete all the data on that instantSnapshot. If any data on the instantSnapshot that is marked for deletion is needed for subsequent instantSnapshots, the data will be moved to the next corresponding instantSnapshot.

For more information, seeDeleting instantSnapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       DeleteInstantSnapshotRequest request =
           DeleteInstantSnapshotRequest.newBuilder()
               .setInstantSnapshot("instantSnapshot800321221")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instantSnapshotsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstantSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteInstantSnapshotRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified InstantSnapshot resource. Keep in mind that deleting a single instantSnapshot might not necessarily delete all the data on that instantSnapshot. If any data on the instantSnapshot that is marked for deletion is needed for subsequent instantSnapshots, the data will be moved to the next corresponding instantSnapshot.

For more information, seeDeleting instantSnapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       DeleteInstantSnapshotRequest request =
           DeleteInstantSnapshotRequest.newBuilder()
               .setInstantSnapshot("instantSnapshot800321221")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instantSnapshotsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstantSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetInstantSnapshotRequest request)
    
    
    public final InstantSnapshot get(GetInstantSnapshotRequest request)

Returns the specified InstantSnapshot resource in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       GetInstantSnapshotRequest request =
           GetInstantSnapshotRequest.newBuilder()
               .setInstantSnapshot("instantSnapshot800321221")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       InstantSnapshot response = instantSnapshotsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstantSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstantSnapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshot)` |   
  
### get(String project, String zone, String instantSnapshot)
    
    
    public final InstantSnapshot get(String project, String zone, String instantSnapshot)

Returns the specified InstantSnapshot resource in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instantSnapshot = "instantSnapshot800321221";
       InstantSnapshot response = instantSnapshotsClient.get(project, zone, instantSnapshot);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`instantSnapshot` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the InstantSnapshot resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[InstantSnapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshot)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetInstantSnapshotRequest,InstantSnapshot> getCallable()

Returns the specified InstantSnapshot resource in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       GetInstantSnapshotRequest request =
           GetInstantSnapshotRequest.newBuilder()
               .setInstantSnapshot("instantSnapshot800321221")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<InstantSnapshot> future = instantSnapshotsClient.getCallable().futureCall(request);
       // Do something.
       InstantSnapshot response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstantSnapshotRequest),[InstantSnapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshot)>` |   
  
### getIamPolicy(GetIamPolicyInstantSnapshotRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyInstantSnapshotRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       GetIamPolicyInstantSnapshotRequest request =
           GetIamPolicyInstantSnapshotRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       Policy response = instantSnapshotsClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyInstantSnapshotRequest)`  
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
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       Policy response = instantSnapshotsClient.getIamPolicy(project, zone, resource);
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
    
    
    public final UnaryCallable<GetIamPolicyInstantSnapshotRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       GetIamPolicyInstantSnapshotRequest request =
           GetIamPolicyInstantSnapshotRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       ApiFuture<Policy> future = instantSnapshotsClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyInstantSnapshotRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getSettings()
    
    
    public final @Nullable InstantSnapshotsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.InstantSnapshotsSettings` |   
  
### getStub()
    
    
    public InstantSnapshotsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[InstantSnapshotsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InstantSnapshotsStub)` |   
  
### insertAsync(InsertInstantSnapshotRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertInstantSnapshotRequest request)

Creates an instant snapshot in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       InsertInstantSnapshotRequest request =
           InsertInstantSnapshotRequest.newBuilder()
               .setInstantSnapshotResource(InstantSnapshot.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instantSnapshotsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstantSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String zone, InstantSnapshot instantSnapshotResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String zone, InstantSnapshot instantSnapshotResource)

Creates an instant snapshot in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       InstantSnapshot instantSnapshotResource = InstantSnapshot.newBuilder().build();
       Operation response =
           instantSnapshotsClient.insertAsync(project, zone, instantSnapshotResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`instantSnapshotResource` | `[InstantSnapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshot)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertInstantSnapshotRequest,Operation> insertCallable()

Creates an instant snapshot in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       InsertInstantSnapshotRequest request =
           InsertInstantSnapshotRequest.newBuilder()
               .setInstantSnapshotResource(InstantSnapshot.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instantSnapshotsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstantSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertInstantSnapshotRequest,Operation,Operation> insertOperationCallable()

Creates an instant snapshot in the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       InsertInstantSnapshotRequest request =
           InsertInstantSnapshotRequest.newBuilder()
               .setInstantSnapshotResource(InstantSnapshot.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instantSnapshotsClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstantSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListInstantSnapshotsRequest request)
    
    
    public final InstantSnapshotsClient.ListPagedResponse list(ListInstantSnapshotsRequest request)

Retrieves the list of InstantSnapshot resources contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       ListInstantSnapshotsRequest request =
           ListInstantSnapshotsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (InstantSnapshot element : instantSnapshotsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInstantSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstantSnapshotsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstantSnapshotsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotsClient.ListPagedResponse)` |   
  
### list(String project, String zone)
    
    
    public final InstantSnapshotsClient.ListPagedResponse list(String project, String zone)

Retrieves the list of InstantSnapshot resources contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       for (InstantSnapshot element : instantSnapshotsClient.list(project, zone).iterateAll()) {
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
`[InstantSnapshotsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListInstantSnapshotsRequest,InstantSnapshotList> listCallable()

Retrieves the list of InstantSnapshot resources contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       ListInstantSnapshotsRequest request =
           ListInstantSnapshotsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         InstantSnapshotList response = instantSnapshotsClient.listCallable().call(request);
         for (InstantSnapshot element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstantSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstantSnapshotsRequest),[InstantSnapshotList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListInstantSnapshotsRequest,InstantSnapshotsClient.ListPagedResponse> listPagedCallable()

Retrieves the list of InstantSnapshot resources contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       ListInstantSnapshotsRequest request =
           ListInstantSnapshotsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<InstantSnapshot> future =
           instantSnapshotsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (InstantSnapshot element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstantSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstantSnapshotsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstantSnapshotsClient.ListPagedResponse)>` |   
  
### setIamPolicy(SetIamPolicyInstantSnapshotRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyInstantSnapshotRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       SetIamPolicyInstantSnapshotRequest request =
           SetIamPolicyInstantSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetPolicyRequestResource(ZoneSetPolicyRequest.newBuilder().build())
               .build();
       Policy response = instantSnapshotsClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyInstantSnapshotRequest)`  
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
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       ZoneSetPolicyRequest zoneSetPolicyRequestResource = ZoneSetPolicyRequest.newBuilder().build();
       Policy response =
           instantSnapshotsClient.setIamPolicy(
               project, zone, resource, zoneSetPolicyRequestResource);
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
    
    
    public final UnaryCallable<SetIamPolicyInstantSnapshotRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       SetIamPolicyInstantSnapshotRequest request =
           SetIamPolicyInstantSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetPolicyRequestResource(ZoneSetPolicyRequest.newBuilder().build())
               .build();
       ApiFuture<Policy> future = instantSnapshotsClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyInstantSnapshotRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### setLabelsAsync(SetLabelsInstantSnapshotRequest request)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(SetLabelsInstantSnapshotRequest request)

Sets the labels on a instantSnapshot in the given zone. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       SetLabelsInstantSnapshotRequest request =
           SetLabelsInstantSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetLabelsRequestResource(ZoneSetLabelsRequest.newBuilder().build())
               .build();
       Operation response = instantSnapshotsClient.setLabelsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetLabelsInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsInstantSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsAsync(String project, String zone, String resource, ZoneSetLabelsRequest zoneSetLabelsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(String project, String zone, String resource, ZoneSetLabelsRequest zoneSetLabelsRequestResource)

Sets the labels on a instantSnapshot in the given zone. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       ZoneSetLabelsRequest zoneSetLabelsRequestResource = ZoneSetLabelsRequest.newBuilder().build();
       Operation response =
           instantSnapshotsClient
               .setLabelsAsync(project, zone, resource, zoneSetLabelsRequestResource)
               .get();
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
`zoneSetLabelsRequestResource` | `[ZoneSetLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneSetLabelsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsCallable()
    
    
    public final UnaryCallable<SetLabelsInstantSnapshotRequest,Operation> setLabelsCallable()

Sets the labels on a instantSnapshot in the given zone. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       SetLabelsInstantSnapshotRequest request =
           SetLabelsInstantSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetLabelsRequestResource(ZoneSetLabelsRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future = instantSnapshotsClient.setLabelsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLabelsInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsInstantSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsOperationCallable()
    
    
    public final OperationCallable<SetLabelsInstantSnapshotRequest,Operation,Operation> setLabelsOperationCallable()

Sets the labels on a instantSnapshot in the given zone. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       SetLabelsInstantSnapshotRequest request =
           SetLabelsInstantSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetLabelsRequestResource(ZoneSetLabelsRequest.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           instantSnapshotsClient.setLabelsOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetLabelsInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsInstantSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsInstantSnapshotRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsInstantSnapshotRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       TestIamPermissionsInstantSnapshotRequest request =
           TestIamPermissionsInstantSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       TestPermissionsResponse response = instantSnapshotsClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsInstantSnapshotRequest)`  
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
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           instantSnapshotsClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsInstantSnapshotRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstantSnapshotsClient instantSnapshotsClient = InstantSnapshotsClient.create()) {
       TestIamPermissionsInstantSnapshotRequest request =
           TestIamPermissionsInstantSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<TestPermissionsResponse> future =
           instantSnapshotsClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsInstantSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsInstantSnapshotRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
