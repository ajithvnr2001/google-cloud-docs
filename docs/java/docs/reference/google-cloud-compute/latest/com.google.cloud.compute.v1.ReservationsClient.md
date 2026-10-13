---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient
title: Class ReservationsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:13.531567+00:00
---

# Class ReservationsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ReservationsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/ReservationsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The Reservations API.

This client uses Reservations version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String reservation = "reservation-1563081780";
       Reservation response = reservationsClient.get(project, zone, reservation);
     }
     

Note: close() needs to be called on the ReservationsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves an aggregated list of reservations.  To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListReservationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified reservation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteReservationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String zone, String reservation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Retrieves information about the specified reservation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetReservationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String reservation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyReservationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String zone, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
Insert |  Creates a new reservation. For more information, readReserving zonal resources. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertReservationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String zone, Reservation reservationResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  A list of all the reservations that have been configured for the specified project in specified zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListReservationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
PerformMaintenance |  Perform maintenance on an extended reservation |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * performMaintenanceAsync(PerformMaintenanceReservationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * performMaintenanceAsync(String project, String zone, String reservation, ReservationsPerformMaintenanceRequest reservationsPerformMaintenanceRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * performMaintenanceOperationCallable() 
  * performMaintenanceCallable() 

  
Resize |  Resizes the reservation (applicable to standalone reservations only). For more information, readModifying reservations. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resizeAsync(ResizeReservationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * resizeAsync(String project, String zone, String reservation, ReservationsResizeRequest reservationsResizeRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resizeOperationCallable() 
  * resizeCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyReservationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String zone, String resource, ZoneSetPolicyRequest zoneSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsReservationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String zone, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
Update |  Update share settings of the reservation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAsync(UpdateReservationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAsync(String project, String zone, String reservation, Reservation reservationResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOperationCallable() 
  * updateCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ReservationsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ReservationsSettings reservationsSettings =
         ReservationsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ReservationsClient reservationsClient = ReservationsClient.create(reservationsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ReservationsSettings reservationsSettings =
         ReservationsSettings.newBuilder().setEndpoint(myEndpoint).build();
     ReservationsClient reservationsClient = ReservationsClient.create(reservationsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ReservationsClient

## Static Methods 

### create()
    
    
    public static final ReservationsClient create()

Constructs an instance of ReservationsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ReservationsSettings settings)
    
    
    public static final ReservationsClient create(ReservationsSettings settings)

Constructs an instance of ReservationsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ReservationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ReservationsStub stub)
    
    
    public static final ReservationsClient create(ReservationsStub stub)

Constructs an instance of ReservationsClient, using the given stub for making calls. This is for advanced usage - prefer using create(ReservationsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ReservationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ReservationsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient)` |   
  
## Constructors 

### ReservationsClient(ReservationsSettings settings)
    
    
    protected ReservationsClient(ReservationsSettings settings)

Constructs an instance of ReservationsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ReservationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsSettings)`  
  
  
### ReservationsClient(ReservationsStub stub)
    
    
    protected ReservationsClient(ReservationsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ReservationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ReservationsStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListReservationsRequest request)
    
    
    public final ReservationsClient.AggregatedListPagedResponse aggregatedList(AggregatedListReservationsRequest request)

Retrieves an aggregated list of reservations.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       AggregatedListReservationsRequest request =
           AggregatedListReservationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, ReservationsScopedList> element :
           reservationsClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListReservationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListReservationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReservationsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final ReservationsClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves an aggregated list of reservations.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, ReservationsScopedList> element :
           reservationsClient.aggregatedList(project).iterateAll()) {
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
`[ReservationsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListReservationsRequest,ReservationAggregatedList> aggregatedListCallable()

Retrieves an aggregated list of reservations.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       AggregatedListReservationsRequest request =
           AggregatedListReservationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         ReservationAggregatedList response =
             reservationsClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, ReservationsScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListReservationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListReservationsRequest),[ReservationAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListReservationsRequest,ReservationsClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves an aggregated list of reservations.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       AggregatedListReservationsRequest request =
           AggregatedListReservationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, ReservationsScopedList>> future =
           reservationsClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, ReservationsScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListReservationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListReservationsRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteReservationRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteReservationRequest request)

Deletes the specified reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       DeleteReservationRequest request =
           DeleteReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservation("reservation-1563081780")
               .setZone("zone3744684")
               .build();
       Operation response = reservationsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteReservationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String zone, String reservation)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String zone, String reservation)

Deletes the specified reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String reservation = "reservation-1563081780";
       Operation response = reservationsClient.deleteAsync(project, zone, reservation).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`reservation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the reservation to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteReservationRequest,Operation> deleteCallable()

Deletes the specified reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       DeleteReservationRequest request =
           DeleteReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservation("reservation-1563081780")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = reservationsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteReservationRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       DeleteReservationRequest request =
           DeleteReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservation("reservation-1563081780")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           reservationsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetReservationRequest request)
    
    
    public final Reservation get(GetReservationRequest request)

Retrieves information about the specified reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       GetReservationRequest request =
           GetReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setReservation("reservation-1563081780")
               .setZone("zone3744684")
               .build();
       Reservation response = reservationsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetReservationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation)` |   
  
### get(String project, String zone, String reservation)
    
    
    public final Reservation get(String project, String zone, String reservation)

Retrieves information about the specified reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String reservation = "reservation-1563081780";
       Reservation response = reservationsClient.get(project, zone, reservation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`reservation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the reservation to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetReservationRequest,Reservation> getCallable()

Retrieves information about the specified reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       GetReservationRequest request =
           GetReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setReservation("reservation-1563081780")
               .setZone("zone3744684")
               .build();
       ApiFuture<Reservation> future = reservationsClient.getCallable().futureCall(request);
       // Do something.
       Reservation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetReservationRequest),[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation)>` |   
  
### getIamPolicy(GetIamPolicyReservationRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyReservationRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       GetIamPolicyReservationRequest request =
           GetIamPolicyReservationRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       Policy response = reservationsClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyReservationRequest)`  
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
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       Policy response = reservationsClient.getIamPolicy(project, zone, resource);
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
    
    
    public final UnaryCallable<GetIamPolicyReservationRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       GetIamPolicyReservationRequest request =
           GetIamPolicyReservationRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       ApiFuture<Policy> future = reservationsClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyReservationRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getSettings()
    
    
    public final @Nullable ReservationsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.ReservationsSettings` |   
  
### getStub()
    
    
    public ReservationsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ReservationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ReservationsStub)` |   
  
### insertAsync(InsertReservationRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertReservationRequest request)

Creates a new reservation. For more information, readReserving zonal resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       InsertReservationRequest request =
           InsertReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationResource(Reservation.newBuilder().build())
               .setZone("zone3744684")
               .build();
       Operation response = reservationsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertReservationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String zone, Reservation reservationResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String zone, Reservation reservationResource)

Creates a new reservation. For more information, readReserving zonal resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       Reservation reservationResource = Reservation.newBuilder().build();
       Operation response = reservationsClient.insertAsync(project, zone, reservationResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`reservationResource` | `[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertReservationRequest,Operation> insertCallable()

Creates a new reservation. For more information, readReserving zonal resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       InsertReservationRequest request =
           InsertReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationResource(Reservation.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = reservationsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertReservationRequest,Operation,Operation> insertOperationCallable()

Creates a new reservation. For more information, readReserving zonal resources.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       InsertReservationRequest request =
           InsertReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationResource(Reservation.newBuilder().build())
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           reservationsClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListReservationsRequest request)
    
    
    public final ReservationsClient.ListPagedResponse list(ListReservationsRequest request)

A list of all the reservations that have been configured for the specified project in specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       ListReservationsRequest request =
           ListReservationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (Reservation element : reservationsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReservationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListReservationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReservationsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.ListPagedResponse)` |   
  
### list(String project, String zone)
    
    
    public final ReservationsClient.ListPagedResponse list(String project, String zone)

A list of all the reservations that have been configured for the specified project in specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       for (Reservation element : reservationsClient.list(project, zone).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
**Returns**  
---  
**Type** | **Description**  
`[ReservationsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListReservationsRequest,ReservationList> listCallable()

A list of all the reservations that have been configured for the specified project in specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       ListReservationsRequest request =
           ListReservationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         ReservationList response = reservationsClient.listCallable().call(request);
         for (Reservation element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReservationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListReservationsRequest),[ReservationList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListReservationsRequest,ReservationsClient.ListPagedResponse> listPagedCallable()

A list of all the reservations that have been configured for the specified project in specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       ListReservationsRequest request =
           ListReservationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<Reservation> future = reservationsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (Reservation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReservationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListReservationsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.ListPagedResponse)>` |   
  
### performMaintenanceAsync(PerformMaintenanceReservationRequest request)
    
    
    public final OperationFuture<Operation,Operation> performMaintenanceAsync(PerformMaintenanceReservationRequest request)

Perform maintenance on an extended reservation

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       PerformMaintenanceReservationRequest request =
           PerformMaintenanceReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservation("reservation-1563081780")
               .setReservationsPerformMaintenanceRequestResource(
                   ReservationsPerformMaintenanceRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       Operation response = reservationsClient.performMaintenanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PerformMaintenanceReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceReservationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceAsync(String project, String zone, String reservation, ReservationsPerformMaintenanceRequest reservationsPerformMaintenanceRequestResource)
    
    
    public final OperationFuture<Operation,Operation> performMaintenanceAsync(String project, String zone, String reservation, ReservationsPerformMaintenanceRequest reservationsPerformMaintenanceRequestResource)

Perform maintenance on an extended reservation

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String reservation = "reservation-1563081780";
       ReservationsPerformMaintenanceRequest reservationsPerformMaintenanceRequestResource =
           ReservationsPerformMaintenanceRequest.newBuilder().build();
       Operation response =
           reservationsClient
               .performMaintenanceAsync(
                   project, zone, reservation, reservationsPerformMaintenanceRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request. Zone name should conform to RFC1035.  
`reservation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the reservation. Name should conform to RFC1035 or be a resource ID.  
`reservationsPerformMaintenanceRequestResource` | `[ReservationsPerformMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsPerformMaintenanceRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceCallable()
    
    
    public final UnaryCallable<PerformMaintenanceReservationRequest,Operation> performMaintenanceCallable()

Perform maintenance on an extended reservation

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       PerformMaintenanceReservationRequest request =
           PerformMaintenanceReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservation("reservation-1563081780")
               .setReservationsPerformMaintenanceRequestResource(
                   ReservationsPerformMaintenanceRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           reservationsClient.performMaintenanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PerformMaintenanceReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceOperationCallable()
    
    
    public final OperationCallable<PerformMaintenanceReservationRequest,Operation,Operation> performMaintenanceOperationCallable()

Perform maintenance on an extended reservation

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       PerformMaintenanceReservationRequest request =
           PerformMaintenanceReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservation("reservation-1563081780")
               .setReservationsPerformMaintenanceRequestResource(
                   ReservationsPerformMaintenanceRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           reservationsClient.performMaintenanceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PerformMaintenanceReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resizeAsync(ResizeReservationRequest request)
    
    
    public final OperationFuture<Operation,Operation> resizeAsync(ResizeReservationRequest request)

Resizes the reservation (applicable to standalone reservations only). For more information, readModifying reservations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       ResizeReservationRequest request =
           ResizeReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservation("reservation-1563081780")
               .setReservationsResizeRequestResource(ReservationsResizeRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       Operation response = reservationsClient.resizeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResizeReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResizeReservationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resizeAsync(String project, String zone, String reservation, ReservationsResizeRequest reservationsResizeRequestResource)
    
    
    public final OperationFuture<Operation,Operation> resizeAsync(String project, String zone, String reservation, ReservationsResizeRequest reservationsResizeRequestResource)

Resizes the reservation (applicable to standalone reservations only). For more information, readModifying reservations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String reservation = "reservation-1563081780";
       ReservationsResizeRequest reservationsResizeRequestResource =
           ReservationsResizeRequest.newBuilder().build();
       Operation response =
           reservationsClient
               .resizeAsync(project, zone, reservation, reservationsResizeRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`reservation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the reservation to update.  
`reservationsResizeRequestResource` | `[ReservationsResizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsResizeRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resizeCallable()
    
    
    public final UnaryCallable<ResizeReservationRequest,Operation> resizeCallable()

Resizes the reservation (applicable to standalone reservations only). For more information, readModifying reservations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       ResizeReservationRequest request =
           ResizeReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservation("reservation-1563081780")
               .setReservationsResizeRequestResource(ReservationsResizeRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = reservationsClient.resizeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResizeReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResizeReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resizeOperationCallable()
    
    
    public final OperationCallable<ResizeReservationRequest,Operation,Operation> resizeOperationCallable()

Resizes the reservation (applicable to standalone reservations only). For more information, readModifying reservations.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       ResizeReservationRequest request =
           ResizeReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservation("reservation-1563081780")
               .setReservationsResizeRequestResource(ReservationsResizeRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           reservationsClient.resizeOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ResizeReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResizeReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setIamPolicy(SetIamPolicyReservationRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyReservationRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       SetIamPolicyReservationRequest request =
           SetIamPolicyReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetPolicyRequestResource(ZoneSetPolicyRequest.newBuilder().build())
               .build();
       Policy response = reservationsClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyReservationRequest)`  
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
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       ZoneSetPolicyRequest zoneSetPolicyRequestResource = ZoneSetPolicyRequest.newBuilder().build();
       Policy response =
           reservationsClient.setIamPolicy(project, zone, resource, zoneSetPolicyRequestResource);
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
    
    
    public final UnaryCallable<SetIamPolicyReservationRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       SetIamPolicyReservationRequest request =
           SetIamPolicyReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetPolicyRequestResource(ZoneSetPolicyRequest.newBuilder().build())
               .build();
       ApiFuture<Policy> future = reservationsClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyReservationRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsReservationRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsReservationRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       TestIamPermissionsReservationRequest request =
           TestIamPermissionsReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       TestPermissionsResponse response = reservationsClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsReservationRequest)`  
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
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           reservationsClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsReservationRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       TestIamPermissionsReservationRequest request =
           TestIamPermissionsReservationRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<TestPermissionsResponse> future =
           reservationsClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsReservationRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
### updateAsync(UpdateReservationRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(UpdateReservationRequest request)

Update share settings of the reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       UpdateReservationRequest request =
           UpdateReservationRequest.newBuilder()
               .setPaths("paths106438894")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservation("reservation-1563081780")
               .setReservationResource(Reservation.newBuilder().build())
               .setUpdateMask("updateMask-296147115")
               .setZone("zone3744684")
               .build();
       Operation response = reservationsClient.updateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateReservationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(String project, String zone, String reservation, Reservation reservationResource)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(String project, String zone, String reservation, Reservation reservationResource)

Update share settings of the reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String reservation = "reservation-1563081780";
       Reservation reservationResource = Reservation.newBuilder().build();
       Operation response =
           reservationsClient.updateAsync(project, zone, reservation, reservationResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`reservation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the reservation to update.  
`reservationResource` | `[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateCallable()
    
    
    public final UnaryCallable<UpdateReservationRequest,Operation> updateCallable()

Update share settings of the reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       UpdateReservationRequest request =
           UpdateReservationRequest.newBuilder()
               .setPaths("paths106438894")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservation("reservation-1563081780")
               .setReservationResource(Reservation.newBuilder().build())
               .setUpdateMask("updateMask-296147115")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = reservationsClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationCallable()
    
    
    public final OperationCallable<UpdateReservationRequest,Operation,Operation> updateOperationCallable()

Update share settings of the reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationsClient reservationsClient = ReservationsClient.create()) {
       UpdateReservationRequest request =
           UpdateReservationRequest.newBuilder()
               .setPaths("paths106438894")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservation("reservation-1563081780")
               .setReservationResource(Reservation.newBuilder().build())
               .setUpdateMask("updateMask-296147115")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           reservationsClient.updateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
