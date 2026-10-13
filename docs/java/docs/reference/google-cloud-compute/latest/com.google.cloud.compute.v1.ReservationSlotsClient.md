---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSlotsClient
title: Class ReservationSlotsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:10.915455+00:00
---

# Class ReservationSlotsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSlotsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ReservationSlotsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/ReservationSlotsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The ReservationSlots API.

This client uses ReservationSlots version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentName = "parentName-244870571";
       String reservationSlot = "reservationSlot-337781782";
       ReservationSlotsGetResponse response =
           reservationSlotsClient.get(project, zone, parentName, reservationSlot);
     }
     

Note: close() needs to be called on the ReservationSlotsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Get |  Retrieves information about the specified reservation slot. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetReservationSlotRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String parentName, String reservationSlot) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetHealth |  Get health info on a reservation slot. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getHealthAsync(GetHealthReservationSlotRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * getHealthAsync(String project, String zone, String parentName, String reservationSlot) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getHealthOperationCallable() 
  * getHealthCallable() 

  
GetVersion |  Allows customers to get SBOM versions of a reservation slot. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getVersionAsync(GetVersionReservationSlotRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * getVersionAsync(String project, String zone, String parentName, String reservationSlot, ReservationSlotsGetVersionRequest reservationSlotsGetVersionRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getVersionOperationCallable() 
  * getVersionCallable() 

  
List |  Retrieves a list of reservation slots under a single reservation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListReservationSlotsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone, String parentName) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Update |  Update a reservation slot in the specified sub-block. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAsync(UpdateReservationSlotRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAsync(String project, String zone, String parentName, String reservationSlot, ReservationSlot reservationSlotResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOperationCallable() 
  * updateCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ReservationSlotsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ReservationSlotsSettings reservationSlotsSettings =
         ReservationSlotsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ReservationSlotsClient reservationSlotsClient =
         ReservationSlotsClient.create(reservationSlotsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ReservationSlotsSettings reservationSlotsSettings =
         ReservationSlotsSettings.newBuilder().setEndpoint(myEndpoint).build();
     ReservationSlotsClient reservationSlotsClient =
         ReservationSlotsClient.create(reservationSlotsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ReservationSlotsClient

## Static Methods 

### create()
    
    
    public static final ReservationSlotsClient create()

Constructs an instance of ReservationSlotsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ReservationSlotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSlotsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ReservationSlotsSettings settings)
    
    
    public static final ReservationSlotsClient create(ReservationSlotsSettings settings)

Constructs an instance of ReservationSlotsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ReservationSlotsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSlotsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReservationSlotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSlotsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ReservationSlotsStub stub)
    
    
    public static final ReservationSlotsClient create(ReservationSlotsStub stub)

Constructs an instance of ReservationSlotsClient, using the given stub for making calls. This is for advanced usage - prefer using create(ReservationSlotsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ReservationSlotsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ReservationSlotsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReservationSlotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSlotsClient)` |   
  
## Constructors 

### ReservationSlotsClient(ReservationSlotsSettings settings)
    
    
    protected ReservationSlotsClient(ReservationSlotsSettings settings)

Constructs an instance of ReservationSlotsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ReservationSlotsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSlotsSettings)`  
  
  
### ReservationSlotsClient(ReservationSlotsStub stub)
    
    
    protected ReservationSlotsClient(ReservationSlotsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ReservationSlotsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ReservationSlotsStub)`  
  
  
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

### get(GetReservationSlotRequest request)
    
    
    public final ReservationSlotsGetResponse get(GetReservationSlotRequest request)

Retrieves information about the specified reservation slot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       GetReservationSlotRequest request =
           GetReservationSlotRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setReservationSlot("reservationSlot-337781782")
               .setZone("zone3744684")
               .build();
       ReservationSlotsGetResponse response = reservationSlotsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetReservationSlotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetReservationSlotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReservationSlotsGetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSlotsGetResponse)` |   
  
### get(String project, String zone, String parentName, String reservationSlot)
    
    
    public final ReservationSlotsGetResponse get(String project, String zone, String parentName, String reservationSlot)

Retrieves information about the specified reservation slot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentName = "parentName-244870571";
       String reservationSlot = "reservationSlot-337781782";
       ReservationSlotsGetResponse response =
           reservationSlotsClient.get(project, zone, parentName, reservationSlot);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request, formatted as RFC1035.  
`parentName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the parent reservation and parent block, formatted as reservations/{reservation_name}/reservationBlocks/{reservation_block_name}/reservationSubBlocks/{reservation_sub_block_name}  
`reservationSlot` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the reservation slot, formatted as RFC1035 or a resource ID number.  
**Returns**  
---  
**Type** | **Description**  
`[ReservationSlotsGetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSlotsGetResponse)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetReservationSlotRequest,ReservationSlotsGetResponse> getCallable()

Retrieves information about the specified reservation slot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       GetReservationSlotRequest request =
           GetReservationSlotRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setReservationSlot("reservationSlot-337781782")
               .setZone("zone3744684")
               .build();
       ApiFuture<ReservationSlotsGetResponse> future =
           reservationSlotsClient.getCallable().futureCall(request);
       // Do something.
       ReservationSlotsGetResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetReservationSlotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetReservationSlotRequest),[ReservationSlotsGetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSlotsGetResponse)>` |   
  
### getHealthAsync(GetHealthReservationSlotRequest request)
    
    
    public final OperationFuture<Operation,Operation> getHealthAsync(GetHealthReservationSlotRequest request)

Get health info on a reservation slot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       GetHealthReservationSlotRequest request =
           GetHealthReservationSlotRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationSlot("reservationSlot-337781782")
               .setZone("zone3744684")
               .build();
       Operation response = reservationSlotsClient.getHealthAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHealthReservationSlotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetHealthReservationSlotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getHealthAsync(String project, String zone, String parentName, String reservationSlot)
    
    
    public final OperationFuture<Operation,Operation> getHealthAsync(String project, String zone, String parentName, String reservationSlot)

Get health info on a reservation slot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentName = "parentName-244870571";
       String reservationSlot = "reservationSlot-337781782";
       Operation response =
           reservationSlotsClient.getHealthAsync(project, zone, parentName, reservationSlot).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request. Zone name should conform to RFC1035.  
`parentName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the parent reservation, parent block and parent sub-block. In the format of reservations/{reservation_name}/reservationBlocks/{reservation_block_name}/reservationSubBlocks/{reservation_sub_block_name}  
`reservationSlot` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the reservation slot. Name should conform to RFC1035 or be a resource ID.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getHealthCallable()
    
    
    public final UnaryCallable<GetHealthReservationSlotRequest,Operation> getHealthCallable()

Get health info on a reservation slot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       GetHealthReservationSlotRequest request =
           GetHealthReservationSlotRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationSlot("reservationSlot-337781782")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = reservationSlotsClient.getHealthCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetHealthReservationSlotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetHealthReservationSlotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getHealthOperationCallable()
    
    
    public final OperationCallable<GetHealthReservationSlotRequest,Operation,Operation> getHealthOperationCallable()

Get health info on a reservation slot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       GetHealthReservationSlotRequest request =
           GetHealthReservationSlotRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationSlot("reservationSlot-337781782")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           reservationSlotsClient.getHealthOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[GetHealthReservationSlotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetHealthReservationSlotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getSettings()
    
    
    public final @Nullable ReservationSlotsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.ReservationSlotsSettings` |   
  
### getStub()
    
    
    public ReservationSlotsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ReservationSlotsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ReservationSlotsStub)` |   
  
### getVersionAsync(GetVersionReservationSlotRequest request)
    
    
    public final OperationFuture<Operation,Operation> getVersionAsync(GetVersionReservationSlotRequest request)

Allows customers to get SBOM versions of a reservation slot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       GetVersionReservationSlotRequest request =
           GetVersionReservationSlotRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationSlot("reservationSlot-337781782")
               .setReservationSlotsGetVersionRequestResource(
                   ReservationSlotsGetVersionRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       Operation response = reservationSlotsClient.getVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetVersionReservationSlotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetVersionReservationSlotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getVersionAsync(String project, String zone, String parentName, String reservationSlot, ReservationSlotsGetVersionRequest reservationSlotsGetVersionRequestResource)
    
    
    public final OperationFuture<Operation,Operation> getVersionAsync(String project, String zone, String parentName, String reservationSlot, ReservationSlotsGetVersionRequest reservationSlotsGetVersionRequestResource)

Allows customers to get SBOM versions of a reservation slot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentName = "parentName-244870571";
       String reservationSlot = "reservationSlot-337781782";
       ReservationSlotsGetVersionRequest reservationSlotsGetVersionRequestResource =
           ReservationSlotsGetVersionRequest.newBuilder().build();
       Operation response =
           reservationSlotsClient
               .getVersionAsync(
                   project,
                   zone,
                   parentName,
                   reservationSlot,
                   reservationSlotsGetVersionRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request. Zone name should conform to RFC1035.  
`parentName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the parent reservation and parent block. In the format of reservations/{reservation_name}/reservationBlocks/{reservation_block_name}/reservationSubBlocks/{reservation_sub_block_name}  
`reservationSlot` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the reservation slot. Name should conform to RFC1035 or be a resource ID.  
`reservationSlotsGetVersionRequestResource` | `[ReservationSlotsGetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSlotsGetVersionRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getVersionCallable()
    
    
    public final UnaryCallable<GetVersionReservationSlotRequest,Operation> getVersionCallable()

Allows customers to get SBOM versions of a reservation slot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       GetVersionReservationSlotRequest request =
           GetVersionReservationSlotRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationSlot("reservationSlot-337781782")
               .setReservationSlotsGetVersionRequestResource(
                   ReservationSlotsGetVersionRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = reservationSlotsClient.getVersionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetVersionReservationSlotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetVersionReservationSlotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getVersionOperationCallable()
    
    
    public final OperationCallable<GetVersionReservationSlotRequest,Operation,Operation> getVersionOperationCallable()

Allows customers to get SBOM versions of a reservation slot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       GetVersionReservationSlotRequest request =
           GetVersionReservationSlotRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationSlot("reservationSlot-337781782")
               .setReservationSlotsGetVersionRequestResource(
                   ReservationSlotsGetVersionRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           reservationSlotsClient.getVersionOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[GetVersionReservationSlotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetVersionReservationSlotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListReservationSlotsRequest request)
    
    
    public final ReservationSlotsClient.ListPagedResponse list(ListReservationSlotsRequest request)

Retrieves a list of reservation slots under a single reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       ListReservationSlotsRequest request =
           ListReservationSlotsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (ReservationSlot element : reservationSlotsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReservationSlotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListReservationSlotsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReservationSlotsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSlotsClient.ListPagedResponse)` |   
  
### list(String project, String zone, String parentName)
    
    
    public final ReservationSlotsClient.ListPagedResponse list(String project, String zone, String parentName)

Retrieves a list of reservation slots under a single reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentName = "parentName-244870571";
       for (ReservationSlot element :
           reservationSlotsClient.list(project, zone, parentName).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request, formatted as RFC1035.  
`parentName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the parent reservation and parent block, formatted as reservations/{reservation_name}/reservationBlocks/{reservation_block_name}/reservationSubBlocks/{reservation_sub_block_name}  
**Returns**  
---  
**Type** | **Description**  
`[ReservationSlotsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSlotsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListReservationSlotsRequest,ReservationSlotsListResponse> listCallable()

Retrieves a list of reservation slots under a single reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       ListReservationSlotsRequest request =
           ListReservationSlotsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         ReservationSlotsListResponse response = reservationSlotsClient.listCallable().call(request);
         for (ReservationSlot element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReservationSlotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListReservationSlotsRequest),[ReservationSlotsListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSlotsListResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListReservationSlotsRequest,ReservationSlotsClient.ListPagedResponse> listPagedCallable()

Retrieves a list of reservation slots under a single reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       ListReservationSlotsRequest request =
           ListReservationSlotsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<ReservationSlot> future =
           reservationSlotsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (ReservationSlot element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReservationSlotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListReservationSlotsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSlotsClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateAsync(UpdateReservationSlotRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(UpdateReservationSlotRequest request)

Update a reservation slot in the specified sub-block.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       UpdateReservationSlotRequest request =
           UpdateReservationSlotRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setReservationSlot("reservationSlot-337781782")
               .setReservationSlotResource(ReservationSlot.newBuilder().build())
               .setUpdateMask("updateMask-296147115")
               .setZone("zone3744684")
               .build();
       Operation response = reservationSlotsClient.updateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateReservationSlotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateReservationSlotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(String project, String zone, String parentName, String reservationSlot, ReservationSlot reservationSlotResource)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(String project, String zone, String parentName, String reservationSlot, ReservationSlot reservationSlotResource)

Update a reservation slot in the specified sub-block.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentName = "parentName-244870571";
       String reservationSlot = "reservationSlot-337781782";
       ReservationSlot reservationSlotResource = ReservationSlot.newBuilder().build();
       Operation response =
           reservationSlotsClient
               .updateAsync(project, zone, parentName, reservationSlot, reservationSlotResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request, formatted as RFC1035.  
`parentName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the sub-block resource.  
`reservationSlot` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the slot resource.  
`reservationSlotResource` | `[ReservationSlot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSlot)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateCallable()
    
    
    public final UnaryCallable<UpdateReservationSlotRequest,Operation> updateCallable()

Update a reservation slot in the specified sub-block.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       UpdateReservationSlotRequest request =
           UpdateReservationSlotRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setReservationSlot("reservationSlot-337781782")
               .setReservationSlotResource(ReservationSlot.newBuilder().build())
               .setUpdateMask("updateMask-296147115")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = reservationSlotsClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateReservationSlotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateReservationSlotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationCallable()
    
    
    public final OperationCallable<UpdateReservationSlotRequest,Operation,Operation> updateOperationCallable()

Update a reservation slot in the specified sub-block.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSlotsClient reservationSlotsClient = ReservationSlotsClient.create()) {
       UpdateReservationSlotRequest request =
           UpdateReservationSlotRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setReservationSlot("reservationSlot-337781782")
               .setReservationSlotResource(ReservationSlot.newBuilder().build())
               .setUpdateMask("updateMask-296147115")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           reservationSlotsClient.updateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateReservationSlotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateReservationSlotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
