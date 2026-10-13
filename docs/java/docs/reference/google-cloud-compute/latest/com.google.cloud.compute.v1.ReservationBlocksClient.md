---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlocksClient
title: Class ReservationBlocksClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:09.626713+00:00
---

# Class ReservationBlocksClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlocksClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ReservationBlocksClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/ReservationBlocksClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The ReservationBlocks API.

This client uses ReservationBlocks version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String reservation = "reservation-1563081780";
       String reservationBlock = "reservationBlock-1897000927";
       ReservationBlocksGetResponse response =
           reservationBlocksClient.get(project, zone, reservation, reservationBlock);
     }
     

Note: close() needs to be called on the ReservationBlocksClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Get |  Retrieves information about the specified reservation block. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetReservationBlockRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String reservation, String reservationBlock) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyReservationBlockRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String zone, String parentResource, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
List |  Retrieves a list of reservation blocks under a single reservation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListReservationBlocksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone, String reservation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
PerformMaintenance |  Allows customers to perform maintenance on a reservation block |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * performMaintenanceAsync(PerformMaintenanceReservationBlockRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * performMaintenanceAsync(String project, String zone, String reservation, String reservationBlock, ReservationsBlocksPerformMaintenanceRequest reservationsBlocksPerformMaintenanceRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * performMaintenanceOperationCallable() 
  * performMaintenanceCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyReservationBlockRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String zone, String parentResource, String resource, ZoneSetNestedPolicyRequest zoneSetNestedPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsReservationBlockRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String zone, String parentResource, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ReservationBlocksSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ReservationBlocksSettings reservationBlocksSettings =
         ReservationBlocksSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ReservationBlocksClient reservationBlocksClient =
         ReservationBlocksClient.create(reservationBlocksSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ReservationBlocksSettings reservationBlocksSettings =
         ReservationBlocksSettings.newBuilder().setEndpoint(myEndpoint).build();
     ReservationBlocksClient reservationBlocksClient =
         ReservationBlocksClient.create(reservationBlocksSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ReservationBlocksClient

## Static Methods 

### create()
    
    
    public static final ReservationBlocksClient create()

Constructs an instance of ReservationBlocksClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ReservationBlocksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlocksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ReservationBlocksSettings settings)
    
    
    public static final ReservationBlocksClient create(ReservationBlocksSettings settings)

Constructs an instance of ReservationBlocksClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ReservationBlocksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlocksSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReservationBlocksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlocksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ReservationBlocksStub stub)
    
    
    public static final ReservationBlocksClient create(ReservationBlocksStub stub)

Constructs an instance of ReservationBlocksClient, using the given stub for making calls. This is for advanced usage - prefer using create(ReservationBlocksSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ReservationBlocksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ReservationBlocksStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReservationBlocksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlocksClient)` |   
  
## Constructors 

### ReservationBlocksClient(ReservationBlocksSettings settings)
    
    
    protected ReservationBlocksClient(ReservationBlocksSettings settings)

Constructs an instance of ReservationBlocksClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ReservationBlocksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlocksSettings)`  
  
  
### ReservationBlocksClient(ReservationBlocksStub stub)
    
    
    protected ReservationBlocksClient(ReservationBlocksStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ReservationBlocksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ReservationBlocksStub)`  
  
  
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

### get(GetReservationBlockRequest request)
    
    
    public final ReservationBlocksGetResponse get(GetReservationBlockRequest request)

Retrieves information about the specified reservation block.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       GetReservationBlockRequest request =
           GetReservationBlockRequest.newBuilder()
               .setProject("project-309310695")
               .setReservation("reservation-1563081780")
               .setReservationBlock("reservationBlock-1897000927")
               .setView("view3619493")
               .setZone("zone3744684")
               .build();
       ReservationBlocksGetResponse response = reservationBlocksClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetReservationBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetReservationBlockRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReservationBlocksGetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlocksGetResponse)` |   
  
### get(String project, String zone, String reservation, String reservationBlock)
    
    
    public final ReservationBlocksGetResponse get(String project, String zone, String reservation, String reservationBlock)

Retrieves information about the specified reservation block.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String reservation = "reservation-1563081780";
       String reservationBlock = "reservationBlock-1897000927";
       ReservationBlocksGetResponse response =
           reservationBlocksClient.get(project, zone, reservation, reservationBlock);
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
`reservationBlock` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the reservation block. Name should conform to RFC1035 or be a resource ID.  
**Returns**  
---  
**Type** | **Description**  
`[ReservationBlocksGetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlocksGetResponse)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetReservationBlockRequest,ReservationBlocksGetResponse> getCallable()

Retrieves information about the specified reservation block.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       GetReservationBlockRequest request =
           GetReservationBlockRequest.newBuilder()
               .setProject("project-309310695")
               .setReservation("reservation-1563081780")
               .setReservationBlock("reservationBlock-1897000927")
               .setView("view3619493")
               .setZone("zone3744684")
               .build();
       ApiFuture<ReservationBlocksGetResponse> future =
           reservationBlocksClient.getCallable().futureCall(request);
       // Do something.
       ReservationBlocksGetResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetReservationBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetReservationBlockRequest),[ReservationBlocksGetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlocksGetResponse)>` |   
  
### getIamPolicy(GetIamPolicyReservationBlockRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyReservationBlockRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       GetIamPolicyReservationBlockRequest request =
           GetIamPolicyReservationBlockRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setParentResource("parentResource1914365656")
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       Policy response = reservationBlocksClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyReservationBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyReservationBlockRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicy(String project, String zone, String parentResource, String resource)
    
    
    public final Policy getIamPolicy(String project, String zone, String parentResource, String resource)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentResource = "parentResource1914365656";
       String resource = "resource-341064690";
       Policy response =
           reservationBlocksClient.getIamPolicy(project, zone, parentResource, resource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`parentResource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of parent resource of the resource for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyReservationBlockRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       GetIamPolicyReservationBlockRequest request =
           GetIamPolicyReservationBlockRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setParentResource("parentResource1914365656")
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       ApiFuture<Policy> future = reservationBlocksClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyReservationBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyReservationBlockRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getSettings()
    
    
    public final @Nullable ReservationBlocksSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.ReservationBlocksSettings` |   
  
### getStub()
    
    
    public ReservationBlocksStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ReservationBlocksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ReservationBlocksStub)` |   
  
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
  
### list(ListReservationBlocksRequest request)
    
    
    public final ReservationBlocksClient.ListPagedResponse list(ListReservationBlocksRequest request)

Retrieves a list of reservation blocks under a single reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       ListReservationBlocksRequest request =
           ListReservationBlocksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setReservation("reservation-1563081780")
               .setZone("zone3744684")
               .build();
       for (ReservationBlock element : reservationBlocksClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReservationBlocksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListReservationBlocksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReservationBlocksClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlocksClient.ListPagedResponse)` |   
  
### list(String project, String zone, String reservation)
    
    
    public final ReservationBlocksClient.ListPagedResponse list(String project, String zone, String reservation)

Retrieves a list of reservation blocks under a single reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String reservation = "reservation-1563081780";
       for (ReservationBlock element :
           reservationBlocksClient.list(project, zone, reservation).iterateAll()) {
         // doThingsWith(element);
       }
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
**Returns**  
---  
**Type** | **Description**  
`[ReservationBlocksClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlocksClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListReservationBlocksRequest,ReservationBlocksListResponse> listCallable()

Retrieves a list of reservation blocks under a single reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       ListReservationBlocksRequest request =
           ListReservationBlocksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setReservation("reservation-1563081780")
               .setZone("zone3744684")
               .build();
       while (true) {
         ReservationBlocksListResponse response =
             reservationBlocksClient.listCallable().call(request);
         for (ReservationBlock element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReservationBlocksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListReservationBlocksRequest),[ReservationBlocksListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlocksListResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListReservationBlocksRequest,ReservationBlocksClient.ListPagedResponse> listPagedCallable()

Retrieves a list of reservation blocks under a single reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       ListReservationBlocksRequest request =
           ListReservationBlocksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setReservation("reservation-1563081780")
               .setZone("zone3744684")
               .build();
       ApiFuture<ReservationBlock> future =
           reservationBlocksClient.listPagedCallable().futureCall(request);
       // Do something.
       for (ReservationBlock element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReservationBlocksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListReservationBlocksRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlocksClient.ListPagedResponse)>` |   
  
### performMaintenanceAsync(PerformMaintenanceReservationBlockRequest request)
    
    
    public final OperationFuture<Operation,Operation> performMaintenanceAsync(PerformMaintenanceReservationBlockRequest request)

Allows customers to perform maintenance on a reservation block

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       PerformMaintenanceReservationBlockRequest request =
           PerformMaintenanceReservationBlockRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservation("reservation-1563081780")
               .setReservationBlock("reservationBlock-1897000927")
               .setReservationsBlocksPerformMaintenanceRequestResource(
                   ReservationsBlocksPerformMaintenanceRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       Operation response = reservationBlocksClient.performMaintenanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PerformMaintenanceReservationBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceReservationBlockRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceAsync(String project, String zone, String reservation, String reservationBlock, ReservationsBlocksPerformMaintenanceRequest reservationsBlocksPerformMaintenanceRequestResource)
    
    
    public final OperationFuture<Operation,Operation> performMaintenanceAsync(String project, String zone, String reservation, String reservationBlock, ReservationsBlocksPerformMaintenanceRequest reservationsBlocksPerformMaintenanceRequestResource)

Allows customers to perform maintenance on a reservation block

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String reservation = "reservation-1563081780";
       String reservationBlock = "reservationBlock-1897000927";
       ReservationsBlocksPerformMaintenanceRequest
           reservationsBlocksPerformMaintenanceRequestResource =
               ReservationsBlocksPerformMaintenanceRequest.newBuilder().build();
       Operation response =
           reservationBlocksClient
               .performMaintenanceAsync(
                   project,
                   zone,
                   reservation,
                   reservationBlock,
                   reservationsBlocksPerformMaintenanceRequestResource)
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
`reservationBlock` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the reservation block. Name should conform to RFC1035 or be a resource ID.  
`reservationsBlocksPerformMaintenanceRequestResource` | `[ReservationsBlocksPerformMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsBlocksPerformMaintenanceRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceCallable()
    
    
    public final UnaryCallable<PerformMaintenanceReservationBlockRequest,Operation> performMaintenanceCallable()

Allows customers to perform maintenance on a reservation block

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       PerformMaintenanceReservationBlockRequest request =
           PerformMaintenanceReservationBlockRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservation("reservation-1563081780")
               .setReservationBlock("reservationBlock-1897000927")
               .setReservationsBlocksPerformMaintenanceRequestResource(
                   ReservationsBlocksPerformMaintenanceRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           reservationBlocksClient.performMaintenanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PerformMaintenanceReservationBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceReservationBlockRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceOperationCallable()
    
    
    public final OperationCallable<PerformMaintenanceReservationBlockRequest,Operation,Operation> performMaintenanceOperationCallable()

Allows customers to perform maintenance on a reservation block

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       PerformMaintenanceReservationBlockRequest request =
           PerformMaintenanceReservationBlockRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservation("reservation-1563081780")
               .setReservationBlock("reservationBlock-1897000927")
               .setReservationsBlocksPerformMaintenanceRequestResource(
                   ReservationsBlocksPerformMaintenanceRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           reservationBlocksClient.performMaintenanceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PerformMaintenanceReservationBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceReservationBlockRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setIamPolicy(SetIamPolicyReservationBlockRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyReservationBlockRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       SetIamPolicyReservationBlockRequest request =
           SetIamPolicyReservationBlockRequest.newBuilder()
               .setParentResource("parentResource1914365656")
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetNestedPolicyRequestResource(
                   ZoneSetNestedPolicyRequest.newBuilder().build())
               .build();
       Policy response = reservationBlocksClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyReservationBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyReservationBlockRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicy(String project, String zone, String parentResource, String resource, ZoneSetNestedPolicyRequest zoneSetNestedPolicyRequestResource)
    
    
    public final Policy setIamPolicy(String project, String zone, String parentResource, String resource, ZoneSetNestedPolicyRequest zoneSetNestedPolicyRequestResource)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentResource = "parentResource1914365656";
       String resource = "resource-341064690";
       ZoneSetNestedPolicyRequest zoneSetNestedPolicyRequestResource =
           ZoneSetNestedPolicyRequest.newBuilder().build();
       Policy response =
           reservationBlocksClient.setIamPolicy(
               project, zone, parentResource, resource, zoneSetNestedPolicyRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`parentResource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of parent resource of the resource for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`zoneSetNestedPolicyRequestResource` | `[ZoneSetNestedPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneSetNestedPolicyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyReservationBlockRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       SetIamPolicyReservationBlockRequest request =
           SetIamPolicyReservationBlockRequest.newBuilder()
               .setParentResource("parentResource1914365656")
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetNestedPolicyRequestResource(
                   ZoneSetNestedPolicyRequest.newBuilder().build())
               .build();
       ApiFuture<Policy> future = reservationBlocksClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyReservationBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyReservationBlockRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsReservationBlockRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsReservationBlockRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       TestIamPermissionsReservationBlockRequest request =
           TestIamPermissionsReservationBlockRequest.newBuilder()
               .setParentResource("parentResource1914365656")
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       TestPermissionsResponse response = reservationBlocksClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsReservationBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsReservationBlockRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissions(String project, String zone, String parentResource, String resource, TestPermissionsRequest testPermissionsRequestResource)
    
    
    public final TestPermissionsResponse testIamPermissions(String project, String zone, String parentResource, String resource, TestPermissionsRequest testPermissionsRequestResource)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentResource = "parentResource1914365656";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           reservationBlocksClient.testIamPermissions(
               project, zone, parentResource, resource, testPermissionsRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`parentResource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of parent resource of the resource for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsReservationBlockRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationBlocksClient reservationBlocksClient = ReservationBlocksClient.create()) {
       TestIamPermissionsReservationBlockRequest request =
           TestIamPermissionsReservationBlockRequest.newBuilder()
               .setParentResource("parentResource1914365656")
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<TestPermissionsResponse> future =
           reservationBlocksClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsReservationBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsReservationBlockRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
