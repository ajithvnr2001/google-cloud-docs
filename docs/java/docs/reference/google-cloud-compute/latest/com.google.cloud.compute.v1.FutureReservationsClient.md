---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservationsClient
title: Class FutureReservationsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:16.512347+00:00
---

# Class FutureReservationsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservationsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class FutureReservationsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/FutureReservationsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The FutureReservations API.

This client uses FutureReservations version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String futureReservation = "futureReservation1926247945";
       FutureReservation response = futureReservationsClient.get(project, zone, futureReservation);
     }
     

Note: close() needs to be called on the FutureReservationsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves an aggregated list of future reservations.  To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListFutureReservationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Cancel |  Cancel the specified future reservation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelAsync(CancelFutureReservationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * cancelAsync(String project, String zone, String futureReservation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelOperationCallable() 
  * cancelCallable() 

  
Delete |  Deletes the specified future reservation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteFutureReservationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String zone, String futureReservation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Retrieves information about the specified future reservation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetFutureReservationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String futureReservation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a new Future Reservation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertFutureReservationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String zone, FutureReservation futureReservationResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  A list of all the future reservations that have been configured for the specified project in specified zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListFutureReservationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Update |  Updates the specified future reservation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAsync(UpdateFutureReservationRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAsync(String project, String zone, String futureReservation, FutureReservation futureReservationResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOperationCallable() 
  * updateCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of FutureReservationsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FutureReservationsSettings futureReservationsSettings =
         FutureReservationsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     FutureReservationsClient futureReservationsClient =
         FutureReservationsClient.create(futureReservationsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     FutureReservationsSettings futureReservationsSettings =
         FutureReservationsSettings.newBuilder().setEndpoint(myEndpoint).build();
     FutureReservationsClient futureReservationsClient =
         FutureReservationsClient.create(futureReservationsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FutureReservationsClient

## Static Methods 

### create()
    
    
    public static final FutureReservationsClient create()

Constructs an instance of FutureReservationsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[FutureReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FutureReservationsSettings settings)
    
    
    public static final FutureReservationsClient create(FutureReservationsSettings settings)

Constructs an instance of FutureReservationsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FutureReservationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservationsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FutureReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(FutureReservationsStub stub)
    
    
    public static final FutureReservationsClient create(FutureReservationsStub stub)

Constructs an instance of FutureReservationsClient, using the given stub for making calls. This is for advanced usage - prefer using create(FutureReservationsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FutureReservationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.FutureReservationsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FutureReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservationsClient)` |   
  
## Constructors 

### FutureReservationsClient(FutureReservationsSettings settings)
    
    
    protected FutureReservationsClient(FutureReservationsSettings settings)

Constructs an instance of FutureReservationsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[FutureReservationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservationsSettings)`  
  
  
### FutureReservationsClient(FutureReservationsStub stub)
    
    
    protected FutureReservationsClient(FutureReservationsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[FutureReservationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.FutureReservationsStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListFutureReservationsRequest request)
    
    
    public final FutureReservationsClient.AggregatedListPagedResponse aggregatedList(AggregatedListFutureReservationsRequest request)

Retrieves an aggregated list of future reservations.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       AggregatedListFutureReservationsRequest request =
           AggregatedListFutureReservationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, FutureReservationsScopedList> element :
           futureReservationsClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListFutureReservationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListFutureReservationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FutureReservationsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservationsClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final FutureReservationsClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves an aggregated list of future reservations.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, FutureReservationsScopedList> element :
           futureReservationsClient.aggregatedList(project).iterateAll()) {
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
`[FutureReservationsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservationsClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListFutureReservationsRequest,FutureReservationsAggregatedListResponse> aggregatedListCallable()

Retrieves an aggregated list of future reservations.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       AggregatedListFutureReservationsRequest request =
           AggregatedListFutureReservationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         FutureReservationsAggregatedListResponse response =
             futureReservationsClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, FutureReservationsScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListFutureReservationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListFutureReservationsRequest),[FutureReservationsAggregatedListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservationsAggregatedListResponse)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListFutureReservationsRequest,FutureReservationsClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves an aggregated list of future reservations.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       AggregatedListFutureReservationsRequest request =
           AggregatedListFutureReservationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, FutureReservationsScopedList>> future =
           futureReservationsClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, FutureReservationsScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListFutureReservationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListFutureReservationsRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservationsClient.AggregatedListPagedResponse)>` |   
  
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
  
### cancelAsync(CancelFutureReservationRequest request)
    
    
    public final OperationFuture<Operation,Operation> cancelAsync(CancelFutureReservationRequest request)

Cancel the specified future reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       CancelFutureReservationRequest request =
           CancelFutureReservationRequest.newBuilder()
               .setFutureReservation("futureReservation1926247945")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = futureReservationsClient.cancelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelFutureReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CancelFutureReservationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cancelAsync(String project, String zone, String futureReservation)
    
    
    public final OperationFuture<Operation,Operation> cancelAsync(String project, String zone, String futureReservation)

Cancel the specified future reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String futureReservation = "futureReservation1926247945";
       Operation response =
           futureReservationsClient.cancelAsync(project, zone, futureReservation).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request. Name should conform to RFC1035.  
`futureReservation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the future reservation to retrieve. Name should conform to RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cancelCallable()
    
    
    public final UnaryCallable<CancelFutureReservationRequest,Operation> cancelCallable()

Cancel the specified future reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       CancelFutureReservationRequest request =
           CancelFutureReservationRequest.newBuilder()
               .setFutureReservation("futureReservation1926247945")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = futureReservationsClient.cancelCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelFutureReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CancelFutureReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cancelOperationCallable()
    
    
    public final OperationCallable<CancelFutureReservationRequest,Operation,Operation> cancelOperationCallable()

Cancel the specified future reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       CancelFutureReservationRequest request =
           CancelFutureReservationRequest.newBuilder()
               .setFutureReservation("futureReservation1926247945")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           futureReservationsClient.cancelOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CancelFutureReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CancelFutureReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### close()
    
    
    public final void close()

### deleteAsync(DeleteFutureReservationRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteFutureReservationRequest request)

Deletes the specified future reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       DeleteFutureReservationRequest request =
           DeleteFutureReservationRequest.newBuilder()
               .setFutureReservation("futureReservation1926247945")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = futureReservationsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFutureReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteFutureReservationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String zone, String futureReservation)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String zone, String futureReservation)

Deletes the specified future reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String futureReservation = "futureReservation1926247945";
       Operation response =
           futureReservationsClient.deleteAsync(project, zone, futureReservation).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request. Name should conform to RFC1035.  
`futureReservation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the future reservation to retrieve. Name should conform to RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteFutureReservationRequest,Operation> deleteCallable()

Deletes the specified future reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       DeleteFutureReservationRequest request =
           DeleteFutureReservationRequest.newBuilder()
               .setFutureReservation("futureReservation1926247945")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = futureReservationsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteFutureReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteFutureReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteFutureReservationRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified future reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       DeleteFutureReservationRequest request =
           DeleteFutureReservationRequest.newBuilder()
               .setFutureReservation("futureReservation1926247945")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           futureReservationsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteFutureReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteFutureReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetFutureReservationRequest request)
    
    
    public final FutureReservation get(GetFutureReservationRequest request)

Retrieves information about the specified future reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       GetFutureReservationRequest request =
           GetFutureReservationRequest.newBuilder()
               .setFutureReservation("futureReservation1926247945")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       FutureReservation response = futureReservationsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFutureReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetFutureReservationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FutureReservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservation)` |   
  
### get(String project, String zone, String futureReservation)
    
    
    public final FutureReservation get(String project, String zone, String futureReservation)

Retrieves information about the specified future reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String futureReservation = "futureReservation1926247945";
       FutureReservation response = futureReservationsClient.get(project, zone, futureReservation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request. Name should conform to RFC1035.  
`futureReservation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the future reservation to retrieve. Name should conform to RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[FutureReservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservation)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetFutureReservationRequest,FutureReservation> getCallable()

Retrieves information about the specified future reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       GetFutureReservationRequest request =
           GetFutureReservationRequest.newBuilder()
               .setFutureReservation("futureReservation1926247945")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<FutureReservation> future =
           futureReservationsClient.getCallable().futureCall(request);
       // Do something.
       FutureReservation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetFutureReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetFutureReservationRequest),[FutureReservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservation)>` |   
  
### getSettings()
    
    
    public final @Nullable FutureReservationsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.FutureReservationsSettings` |   
  
### getStub()
    
    
    public FutureReservationsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[FutureReservationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.FutureReservationsStub)` |   
  
### insertAsync(InsertFutureReservationRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertFutureReservationRequest request)

Creates a new Future Reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       InsertFutureReservationRequest request =
           InsertFutureReservationRequest.newBuilder()
               .setFutureReservationResource(FutureReservation.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = futureReservationsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertFutureReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertFutureReservationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String zone, FutureReservation futureReservationResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String zone, FutureReservation futureReservationResource)

Creates a new Future Reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       FutureReservation futureReservationResource = FutureReservation.newBuilder().build();
       Operation response =
           futureReservationsClient.insertAsync(project, zone, futureReservationResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request. Name should conform to RFC1035.  
`futureReservationResource` | `[FutureReservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservation)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertFutureReservationRequest,Operation> insertCallable()

Creates a new Future Reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       InsertFutureReservationRequest request =
           InsertFutureReservationRequest.newBuilder()
               .setFutureReservationResource(FutureReservation.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = futureReservationsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertFutureReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertFutureReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertFutureReservationRequest,Operation,Operation> insertOperationCallable()

Creates a new Future Reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       InsertFutureReservationRequest request =
           InsertFutureReservationRequest.newBuilder()
               .setFutureReservationResource(FutureReservation.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           futureReservationsClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertFutureReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertFutureReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListFutureReservationsRequest request)
    
    
    public final FutureReservationsClient.ListPagedResponse list(ListFutureReservationsRequest request)

A list of all the future reservations that have been configured for the specified project in specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       ListFutureReservationsRequest request =
           ListFutureReservationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (FutureReservation element : futureReservationsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFutureReservationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListFutureReservationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[FutureReservationsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservationsClient.ListPagedResponse)` |   
  
### list(String project, String zone)
    
    
    public final FutureReservationsClient.ListPagedResponse list(String project, String zone)

A list of all the future reservations that have been configured for the specified project in specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       for (FutureReservation element : futureReservationsClient.list(project, zone).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request. Name should conform to RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[FutureReservationsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservationsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListFutureReservationsRequest,FutureReservationsListResponse> listCallable()

A list of all the future reservations that have been configured for the specified project in specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       ListFutureReservationsRequest request =
           ListFutureReservationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         FutureReservationsListResponse response =
             futureReservationsClient.listCallable().call(request);
         for (FutureReservation element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFutureReservationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListFutureReservationsRequest),[FutureReservationsListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservationsListResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListFutureReservationsRequest,FutureReservationsClient.ListPagedResponse> listPagedCallable()

A list of all the future reservations that have been configured for the specified project in specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       ListFutureReservationsRequest request =
           ListFutureReservationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<FutureReservation> future =
           futureReservationsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (FutureReservation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListFutureReservationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListFutureReservationsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservationsClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateAsync(UpdateFutureReservationRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(UpdateFutureReservationRequest request)

Updates the specified future reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       UpdateFutureReservationRequest request =
           UpdateFutureReservationRequest.newBuilder()
               .setFutureReservation("futureReservation1926247945")
               .setFutureReservationResource(FutureReservation.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .setZone("zone3744684")
               .build();
       Operation response = futureReservationsClient.updateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFutureReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateFutureReservationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(String project, String zone, String futureReservation, FutureReservation futureReservationResource)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(String project, String zone, String futureReservation, FutureReservation futureReservationResource)

Updates the specified future reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String futureReservation = "futureReservation1926247945";
       FutureReservation futureReservationResource = FutureReservation.newBuilder().build();
       Operation response =
           futureReservationsClient
               .updateAsync(project, zone, futureReservation, futureReservationResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request. Name should conform to RFC1035.  
`futureReservation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the reservation to update. Name should conform to RFC1035.  
`futureReservationResource` | `[FutureReservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.FutureReservation)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateCallable()
    
    
    public final UnaryCallable<UpdateFutureReservationRequest,Operation> updateCallable()

Updates the specified future reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       UpdateFutureReservationRequest request =
           UpdateFutureReservationRequest.newBuilder()
               .setFutureReservation("futureReservation1926247945")
               .setFutureReservationResource(FutureReservation.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = futureReservationsClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateFutureReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateFutureReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationCallable()
    
    
    public final OperationCallable<UpdateFutureReservationRequest,Operation,Operation> updateOperationCallable()

Updates the specified future reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (FutureReservationsClient futureReservationsClient = FutureReservationsClient.create()) {
       UpdateFutureReservationRequest request =
           UpdateFutureReservationRequest.newBuilder()
               .setFutureReservation("futureReservation1926247945")
               .setFutureReservationResource(FutureReservation.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           futureReservationsClient.updateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateFutureReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateFutureReservationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
