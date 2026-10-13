---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSubBlocksClient
title: Class ReservationSubBlocksClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:12.114231+00:00
---

# Class ReservationSubBlocksClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSubBlocksClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ReservationSubBlocksClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/ReservationSubBlocksClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The ReservationSubBlocks API.

This client uses ReservationSubBlocks version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentName = "parentName-244870571";
       String reservationSubBlock = "reservationSubBlock-1816847847";
       ReservationSubBlocksGetResponse response =
           reservationSubBlocksClient.get(project, zone, parentName, reservationSubBlock);
     }
     

Note: close() needs to be called on the ReservationSubBlocksClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Get |  Retrieves information about the specified reservation subBlock. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetReservationSubBlockRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String parentName, String reservationSubBlock) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyReservationSubBlockRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String zone, String parentResource, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
GetVersion |  Allows customers to get SBOM versions of a reservation subBlock. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getVersionAsync(GetVersionReservationSubBlockRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * getVersionAsync(String project, String zone, String parentName, String reservationSubBlock, ReservationSubBlocksGetVersionRequest reservationSubBlocksGetVersionRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getVersionOperationCallable() 
  * getVersionCallable() 

  
List |  Retrieves a list of reservation subBlocks under a single reservation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListReservationSubBlocksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone, String parentName) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
PerformMaintenance |  Allows customers to perform maintenance on a reservation subBlock |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * performMaintenanceAsync(PerformMaintenanceReservationSubBlockRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * performMaintenanceAsync(String project, String zone, String parentName, String reservationSubBlock) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * performMaintenanceOperationCallable() 
  * performMaintenanceCallable() 

  
ReportFaulty |  Allows customers to report a faulty subBlock. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * reportFaultyAsync(ReportFaultyReservationSubBlockRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * reportFaultyAsync(String project, String zone, String parentName, String reservationSubBlock, ReservationSubBlocksReportFaultyRequest reservationSubBlocksReportFaultyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * reportFaultyOperationCallable() 
  * reportFaultyCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyReservationSubBlockRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String zone, String parentResource, String resource, ZoneSetNestedPolicyRequest zoneSetNestedPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsReservationSubBlockRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String zone, String parentResource, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ReservationSubBlocksSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ReservationSubBlocksSettings reservationSubBlocksSettings =
         ReservationSubBlocksSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create(reservationSubBlocksSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ReservationSubBlocksSettings reservationSubBlocksSettings =
         ReservationSubBlocksSettings.newBuilder().setEndpoint(myEndpoint).build();
     ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create(reservationSubBlocksSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ReservationSubBlocksClient

## Static Methods 

### create()
    
    
    public static final ReservationSubBlocksClient create()

Constructs an instance of ReservationSubBlocksClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ReservationSubBlocksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSubBlocksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ReservationSubBlocksSettings settings)
    
    
    public static final ReservationSubBlocksClient create(ReservationSubBlocksSettings settings)

Constructs an instance of ReservationSubBlocksClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ReservationSubBlocksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSubBlocksSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReservationSubBlocksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSubBlocksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ReservationSubBlocksStub stub)
    
    
    public static final ReservationSubBlocksClient create(ReservationSubBlocksStub stub)

Constructs an instance of ReservationSubBlocksClient, using the given stub for making calls. This is for advanced usage - prefer using create(ReservationSubBlocksSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ReservationSubBlocksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ReservationSubBlocksStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReservationSubBlocksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSubBlocksClient)` |   
  
## Constructors 

### ReservationSubBlocksClient(ReservationSubBlocksSettings settings)
    
    
    protected ReservationSubBlocksClient(ReservationSubBlocksSettings settings)

Constructs an instance of ReservationSubBlocksClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ReservationSubBlocksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSubBlocksSettings)`  
  
  
### ReservationSubBlocksClient(ReservationSubBlocksStub stub)
    
    
    protected ReservationSubBlocksClient(ReservationSubBlocksStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ReservationSubBlocksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ReservationSubBlocksStub)`  
  
  
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

### get(GetReservationSubBlockRequest request)
    
    
    public final ReservationSubBlocksGetResponse get(GetReservationSubBlockRequest request)

Retrieves information about the specified reservation subBlock.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       GetReservationSubBlockRequest request =
           GetReservationSubBlockRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setReservationSubBlock("reservationSubBlock-1816847847")
               .setView("view3619493")
               .setZone("zone3744684")
               .build();
       ReservationSubBlocksGetResponse response = reservationSubBlocksClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetReservationSubBlockRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReservationSubBlocksGetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSubBlocksGetResponse)` |   
  
### get(String project, String zone, String parentName, String reservationSubBlock)
    
    
    public final ReservationSubBlocksGetResponse get(String project, String zone, String parentName, String reservationSubBlock)

Retrieves information about the specified reservation subBlock.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentName = "parentName-244870571";
       String reservationSubBlock = "reservationSubBlock-1816847847";
       ReservationSubBlocksGetResponse response =
           reservationSubBlocksClient.get(project, zone, parentName, reservationSubBlock);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request. Zone name should conform to RFC1035.  
`parentName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the parent reservation and parent block. In the format of reservations/{reservation_name}/reservationBlocks/{reservation_block_name}  
`reservationSubBlock` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the reservation subBlock. Name should conform to RFC1035 or be a resource ID.  
**Returns**  
---  
**Type** | **Description**  
`[ReservationSubBlocksGetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSubBlocksGetResponse)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetReservationSubBlockRequest,ReservationSubBlocksGetResponse> getCallable()

Retrieves information about the specified reservation subBlock.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       GetReservationSubBlockRequest request =
           GetReservationSubBlockRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setReservationSubBlock("reservationSubBlock-1816847847")
               .setView("view3619493")
               .setZone("zone3744684")
               .build();
       ApiFuture<ReservationSubBlocksGetResponse> future =
           reservationSubBlocksClient.getCallable().futureCall(request);
       // Do something.
       ReservationSubBlocksGetResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetReservationSubBlockRequest),[ReservationSubBlocksGetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSubBlocksGetResponse)>` |   
  
### getIamPolicy(GetIamPolicyReservationSubBlockRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyReservationSubBlockRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       GetIamPolicyReservationSubBlockRequest request =
           GetIamPolicyReservationSubBlockRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setParentResource("parentResource1914365656")
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       Policy response = reservationSubBlocksClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyReservationSubBlockRequest)`  
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
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentResource = "parentResource1914365656";
       String resource = "resource-341064690";
       Policy response =
           reservationSubBlocksClient.getIamPolicy(project, zone, parentResource, resource);
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
    
    
    public final UnaryCallable<GetIamPolicyReservationSubBlockRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       GetIamPolicyReservationSubBlockRequest request =
           GetIamPolicyReservationSubBlockRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setParentResource("parentResource1914365656")
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       ApiFuture<Policy> future =
           reservationSubBlocksClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyReservationSubBlockRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getSettings()
    
    
    public final @Nullable ReservationSubBlocksSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.ReservationSubBlocksSettings` |   
  
### getStub()
    
    
    public ReservationSubBlocksStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ReservationSubBlocksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ReservationSubBlocksStub)` |   
  
### getVersionAsync(GetVersionReservationSubBlockRequest request)
    
    
    public final OperationFuture<Operation,Operation> getVersionAsync(GetVersionReservationSubBlockRequest request)

Allows customers to get SBOM versions of a reservation subBlock.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       GetVersionReservationSubBlockRequest request =
           GetVersionReservationSubBlockRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationSubBlock("reservationSubBlock-1816847847")
               .setReservationSubBlocksGetVersionRequestResource(
                   ReservationSubBlocksGetVersionRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       Operation response = reservationSubBlocksClient.getVersionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetVersionReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetVersionReservationSubBlockRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getVersionAsync(String project, String zone, String parentName, String reservationSubBlock, ReservationSubBlocksGetVersionRequest reservationSubBlocksGetVersionRequestResource)
    
    
    public final OperationFuture<Operation,Operation> getVersionAsync(String project, String zone, String parentName, String reservationSubBlock, ReservationSubBlocksGetVersionRequest reservationSubBlocksGetVersionRequestResource)

Allows customers to get SBOM versions of a reservation subBlock.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentName = "parentName-244870571";
       String reservationSubBlock = "reservationSubBlock-1816847847";
       ReservationSubBlocksGetVersionRequest reservationSubBlocksGetVersionRequestResource =
           ReservationSubBlocksGetVersionRequest.newBuilder().build();
       Operation response =
           reservationSubBlocksClient
               .getVersionAsync(
                   project,
                   zone,
                   parentName,
                   reservationSubBlock,
                   reservationSubBlocksGetVersionRequestResource)
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
The name of the parent reservation and parent block. In the format of reservations/{reservation_name}/reservationBlocks/{reservation_block_name}  
`reservationSubBlock` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the reservation subBlock. Name should conform to RFC1035 or be a resource ID.  
`reservationSubBlocksGetVersionRequestResource` | `[ReservationSubBlocksGetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSubBlocksGetVersionRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getVersionCallable()
    
    
    public final UnaryCallable<GetVersionReservationSubBlockRequest,Operation> getVersionCallable()

Allows customers to get SBOM versions of a reservation subBlock.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       GetVersionReservationSubBlockRequest request =
           GetVersionReservationSubBlockRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationSubBlock("reservationSubBlock-1816847847")
               .setReservationSubBlocksGetVersionRequestResource(
                   ReservationSubBlocksGetVersionRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           reservationSubBlocksClient.getVersionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetVersionReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetVersionReservationSubBlockRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getVersionOperationCallable()
    
    
    public final OperationCallable<GetVersionReservationSubBlockRequest,Operation,Operation> getVersionOperationCallable()

Allows customers to get SBOM versions of a reservation subBlock.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       GetVersionReservationSubBlockRequest request =
           GetVersionReservationSubBlockRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationSubBlock("reservationSubBlock-1816847847")
               .setReservationSubBlocksGetVersionRequestResource(
                   ReservationSubBlocksGetVersionRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           reservationSubBlocksClient.getVersionOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[GetVersionReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetVersionReservationSubBlockRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListReservationSubBlocksRequest request)
    
    
    public final ReservationSubBlocksClient.ListPagedResponse list(ListReservationSubBlocksRequest request)

Retrieves a list of reservation subBlocks under a single reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       ListReservationSubBlocksRequest request =
           ListReservationSubBlocksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (ReservationSubBlock element : reservationSubBlocksClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReservationSubBlocksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListReservationSubBlocksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReservationSubBlocksClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSubBlocksClient.ListPagedResponse)` |   
  
### list(String project, String zone, String parentName)
    
    
    public final ReservationSubBlocksClient.ListPagedResponse list(String project, String zone, String parentName)

Retrieves a list of reservation subBlocks under a single reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentName = "parentName-244870571";
       for (ReservationSubBlock element :
           reservationSubBlocksClient.list(project, zone, parentName).iterateAll()) {
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
`parentName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the parent reservation and parent block. In the format of reservations/{reservation_name}/reservationBlocks/{reservation_block_name}  
**Returns**  
---  
**Type** | **Description**  
`[ReservationSubBlocksClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSubBlocksClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListReservationSubBlocksRequest,ReservationSubBlocksListResponse> listCallable()

Retrieves a list of reservation subBlocks under a single reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       ListReservationSubBlocksRequest request =
           ListReservationSubBlocksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         ReservationSubBlocksListResponse response =
             reservationSubBlocksClient.listCallable().call(request);
         for (ReservationSubBlock element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReservationSubBlocksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListReservationSubBlocksRequest),[ReservationSubBlocksListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSubBlocksListResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListReservationSubBlocksRequest,ReservationSubBlocksClient.ListPagedResponse> listPagedCallable()

Retrieves a list of reservation subBlocks under a single reservation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       ListReservationSubBlocksRequest request =
           ListReservationSubBlocksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<ReservationSubBlock> future =
           reservationSubBlocksClient.listPagedCallable().futureCall(request);
       // Do something.
       for (ReservationSubBlock element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReservationSubBlocksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListReservationSubBlocksRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSubBlocksClient.ListPagedResponse)>` |   
  
### performMaintenanceAsync(PerformMaintenanceReservationSubBlockRequest request)
    
    
    public final OperationFuture<Operation,Operation> performMaintenanceAsync(PerformMaintenanceReservationSubBlockRequest request)

Allows customers to perform maintenance on a reservation subBlock

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       PerformMaintenanceReservationSubBlockRequest request =
           PerformMaintenanceReservationSubBlockRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationSubBlock("reservationSubBlock-1816847847")
               .setZone("zone3744684")
               .build();
       Operation response = reservationSubBlocksClient.performMaintenanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PerformMaintenanceReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceReservationSubBlockRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceAsync(String project, String zone, String parentName, String reservationSubBlock)
    
    
    public final OperationFuture<Operation,Operation> performMaintenanceAsync(String project, String zone, String parentName, String reservationSubBlock)

Allows customers to perform maintenance on a reservation subBlock

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentName = "parentName-244870571";
       String reservationSubBlock = "reservationSubBlock-1816847847";
       Operation response =
           reservationSubBlocksClient
               .performMaintenanceAsync(project, zone, parentName, reservationSubBlock)
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
The name of the parent reservation and parent block. In the format of reservations/{reservation_name}/reservationBlocks/{reservation_block_name}  
`reservationSubBlock` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the reservation subBlock. Name should conform to RFC1035 or be a resource ID.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceCallable()
    
    
    public final UnaryCallable<PerformMaintenanceReservationSubBlockRequest,Operation> performMaintenanceCallable()

Allows customers to perform maintenance on a reservation subBlock

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       PerformMaintenanceReservationSubBlockRequest request =
           PerformMaintenanceReservationSubBlockRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationSubBlock("reservationSubBlock-1816847847")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           reservationSubBlocksClient.performMaintenanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PerformMaintenanceReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceReservationSubBlockRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceOperationCallable()
    
    
    public final OperationCallable<PerformMaintenanceReservationSubBlockRequest,Operation,Operation> performMaintenanceOperationCallable()

Allows customers to perform maintenance on a reservation subBlock

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       PerformMaintenanceReservationSubBlockRequest request =
           PerformMaintenanceReservationSubBlockRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationSubBlock("reservationSubBlock-1816847847")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           reservationSubBlocksClient.performMaintenanceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PerformMaintenanceReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceReservationSubBlockRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### reportFaultyAsync(ReportFaultyReservationSubBlockRequest request)
    
    
    public final OperationFuture<Operation,Operation> reportFaultyAsync(ReportFaultyReservationSubBlockRequest request)

Allows customers to report a faulty subBlock.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       ReportFaultyReservationSubBlockRequest request =
           ReportFaultyReservationSubBlockRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationSubBlock("reservationSubBlock-1816847847")
               .setReservationSubBlocksReportFaultyRequestResource(
                   ReservationSubBlocksReportFaultyRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       Operation response = reservationSubBlocksClient.reportFaultyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReportFaultyReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReportFaultyReservationSubBlockRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### reportFaultyAsync(String project, String zone, String parentName, String reservationSubBlock, ReservationSubBlocksReportFaultyRequest reservationSubBlocksReportFaultyRequestResource)
    
    
    public final OperationFuture<Operation,Operation> reportFaultyAsync(String project, String zone, String parentName, String reservationSubBlock, ReservationSubBlocksReportFaultyRequest reservationSubBlocksReportFaultyRequestResource)

Allows customers to report a faulty subBlock.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentName = "parentName-244870571";
       String reservationSubBlock = "reservationSubBlock-1816847847";
       ReservationSubBlocksReportFaultyRequest reservationSubBlocksReportFaultyRequestResource =
           ReservationSubBlocksReportFaultyRequest.newBuilder().build();
       Operation response =
           reservationSubBlocksClient
               .reportFaultyAsync(
                   project,
                   zone,
                   parentName,
                   reservationSubBlock,
                   reservationSubBlocksReportFaultyRequestResource)
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
The name of the parent reservation and parent block. In the format of reservations/{reservation_name}/reservationBlocks/{reservation_block_name}  
`reservationSubBlock` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the reservation subBlock. Name should conform to RFC1035 or be a resource ID.  
`reservationSubBlocksReportFaultyRequestResource` | `[ReservationSubBlocksReportFaultyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationSubBlocksReportFaultyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### reportFaultyCallable()
    
    
    public final UnaryCallable<ReportFaultyReservationSubBlockRequest,Operation> reportFaultyCallable()

Allows customers to report a faulty subBlock.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       ReportFaultyReservationSubBlockRequest request =
           ReportFaultyReservationSubBlockRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationSubBlock("reservationSubBlock-1816847847")
               .setReservationSubBlocksReportFaultyRequestResource(
                   ReservationSubBlocksReportFaultyRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           reservationSubBlocksClient.reportFaultyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReportFaultyReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReportFaultyReservationSubBlockRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### reportFaultyOperationCallable()
    
    
    public final OperationCallable<ReportFaultyReservationSubBlockRequest,Operation,Operation> reportFaultyOperationCallable()

Allows customers to report a faulty subBlock.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       ReportFaultyReservationSubBlockRequest request =
           ReportFaultyReservationSubBlockRequest.newBuilder()
               .setParentName("parentName-244870571")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setReservationSubBlock("reservationSubBlock-1816847847")
               .setReservationSubBlocksReportFaultyRequestResource(
                   ReservationSubBlocksReportFaultyRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           reservationSubBlocksClient.reportFaultyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ReportFaultyReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReportFaultyReservationSubBlockRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setIamPolicy(SetIamPolicyReservationSubBlockRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyReservationSubBlockRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       SetIamPolicyReservationSubBlockRequest request =
           SetIamPolicyReservationSubBlockRequest.newBuilder()
               .setParentResource("parentResource1914365656")
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetNestedPolicyRequestResource(
                   ZoneSetNestedPolicyRequest.newBuilder().build())
               .build();
       Policy response = reservationSubBlocksClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyReservationSubBlockRequest)`  
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
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentResource = "parentResource1914365656";
       String resource = "resource-341064690";
       ZoneSetNestedPolicyRequest zoneSetNestedPolicyRequestResource =
           ZoneSetNestedPolicyRequest.newBuilder().build();
       Policy response =
           reservationSubBlocksClient.setIamPolicy(
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
    
    
    public final UnaryCallable<SetIamPolicyReservationSubBlockRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       SetIamPolicyReservationSubBlockRequest request =
           SetIamPolicyReservationSubBlockRequest.newBuilder()
               .setParentResource("parentResource1914365656")
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetNestedPolicyRequestResource(
                   ZoneSetNestedPolicyRequest.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           reservationSubBlocksClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyReservationSubBlockRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsReservationSubBlockRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsReservationSubBlockRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       TestIamPermissionsReservationSubBlockRequest request =
           TestIamPermissionsReservationSubBlockRequest.newBuilder()
               .setParentResource("parentResource1914365656")
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       TestPermissionsResponse response = reservationSubBlocksClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsReservationSubBlockRequest)`  
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
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String parentResource = "parentResource1914365656";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           reservationSubBlocksClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsReservationSubBlockRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReservationSubBlocksClient reservationSubBlocksClient =
         ReservationSubBlocksClient.create()) {
       TestIamPermissionsReservationSubBlockRequest request =
           TestIamPermissionsReservationSubBlockRequest.newBuilder()
               .setParentResource("parentResource1914365656")
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<TestPermissionsResponse> future =
           reservationSubBlocksClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsReservationSubBlockRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsReservationSubBlockRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
