---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequestsClient
title: Class RegionInstanceGroupManagerResizeRequestsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:38.954875+00:00
---

# Class RegionInstanceGroupManagerResizeRequestsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequestsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionInstanceGroupManagerResizeRequestsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RegionInstanceGroupManagerResizeRequestsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RegionInstanceGroupManagerResizeRequests API.

This client uses RegionInstanceGroupManagerResizeRequests version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       String resizeRequest = "resizeRequest-1656358085";
       InstanceGroupManagerResizeRequest response =
           regionInstanceGroupManagerResizeRequestsClient.get(
               project, region, instanceGroupManager, resizeRequest);
     }
     

Note: close() needs to be called on the RegionInstanceGroupManagerResizeRequestsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Cancel |  Cancels the specified resize request. Cancelled resize request no longer waits for the resources to be provisioned. Cancel is only possible for requests that are in accepted state. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelAsync(CancelRegionInstanceGroupManagerResizeRequestRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * cancelAsync(String project, String region, String instanceGroupManager, String resizeRequest) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelOperationCallable() 
  * cancelCallable() 

  
Delete |  Deletes the specified, inactive resize request. Requests that are still active cannot be deleted. Deleting request does not delete instances that were provisioned previously. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRegionInstanceGroupManagerResizeRequestRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String instanceGroupManager, String resizeRequest) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns all of the details about the specified resize request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRegionInstanceGroupManagerResizeRequestRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String instanceGroupManager, String resizeRequest) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a new Resize Request that starts provisioning VMs immediately or queues VM creation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRegionInstanceGroupManagerResizeRequestRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, String instanceGroupManager, InstanceGroupManagerResizeRequest instanceGroupManagerResizeRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves a list of Resize Requests that are contained in the managed instance group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRegionInstanceGroupManagerResizeRequestsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region, String instanceGroupManager) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionInstanceGroupManagerResizeRequestsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionInstanceGroupManagerResizeRequestsSettings
         regionInstanceGroupManagerResizeRequestsSettings =
             RegionInstanceGroupManagerResizeRequestsSettings.newBuilder()
                 .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
                 .build();
     RegionInstanceGroupManagerResizeRequestsClient regionInstanceGroupManagerResizeRequestsClient =
         RegionInstanceGroupManagerResizeRequestsClient.create(
             regionInstanceGroupManagerResizeRequestsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionInstanceGroupManagerResizeRequestsSettings
         regionInstanceGroupManagerResizeRequestsSettings =
             RegionInstanceGroupManagerResizeRequestsSettings.newBuilder()
                 .setEndpoint(myEndpoint)
                 .build();
     RegionInstanceGroupManagerResizeRequestsClient regionInstanceGroupManagerResizeRequestsClient =
         RegionInstanceGroupManagerResizeRequestsClient.create(
             regionInstanceGroupManagerResizeRequestsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionInstanceGroupManagerResizeRequestsClient

## Static Methods 

### create()
    
    
    public static final RegionInstanceGroupManagerResizeRequestsClient create()

Constructs an instance of RegionInstanceGroupManagerResizeRequestsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagerResizeRequestsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequestsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionInstanceGroupManagerResizeRequestsSettings settings)
    
    
    public static final RegionInstanceGroupManagerResizeRequestsClient create(RegionInstanceGroupManagerResizeRequestsSettings settings)

Constructs an instance of RegionInstanceGroupManagerResizeRequestsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionInstanceGroupManagerResizeRequestsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequestsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagerResizeRequestsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequestsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionInstanceGroupManagerResizeRequestsStub stub)
    
    
    public static final RegionInstanceGroupManagerResizeRequestsClient create(RegionInstanceGroupManagerResizeRequestsStub stub)

Constructs an instance of RegionInstanceGroupManagerResizeRequestsClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionInstanceGroupManagerResizeRequestsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionInstanceGroupManagerResizeRequestsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionInstanceGroupManagerResizeRequestsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagerResizeRequestsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequestsClient)` |   
  
## Constructors 

### RegionInstanceGroupManagerResizeRequestsClient(RegionInstanceGroupManagerResizeRequestsSettings settings)
    
    
    protected RegionInstanceGroupManagerResizeRequestsClient(RegionInstanceGroupManagerResizeRequestsSettings settings)

Constructs an instance of RegionInstanceGroupManagerResizeRequestsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionInstanceGroupManagerResizeRequestsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequestsSettings)`  
  
  
### RegionInstanceGroupManagerResizeRequestsClient(RegionInstanceGroupManagerResizeRequestsStub stub)
    
    
    protected RegionInstanceGroupManagerResizeRequestsClient(RegionInstanceGroupManagerResizeRequestsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionInstanceGroupManagerResizeRequestsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionInstanceGroupManagerResizeRequestsStub)`  
  
  
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
  
### cancelAsync(CancelRegionInstanceGroupManagerResizeRequestRequest request)
    
    
    public final OperationFuture<Operation,Operation> cancelAsync(CancelRegionInstanceGroupManagerResizeRequestRequest request)

Cancels the specified resize request. Cancelled resize request no longer waits for the resources to be provisioned. Cancel is only possible for requests that are in accepted state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       CancelRegionInstanceGroupManagerResizeRequestRequest request =
           CancelRegionInstanceGroupManagerResizeRequestRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setResizeRequest("resizeRequest-1656358085")
               .build();
       Operation response =
           regionInstanceGroupManagerResizeRequestsClient.cancelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CancelRegionInstanceGroupManagerResizeRequestRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cancelAsync(String project, String region, String instanceGroupManager, String resizeRequest)
    
    
    public final OperationFuture<Operation,Operation> cancelAsync(String project, String region, String instanceGroupManager, String resizeRequest)

Cancels the specified resize request. Cancelled resize request no longer waits for the resources to be provisioned. Cancel is only possible for requests that are in accepted state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       String resizeRequest = "resizeRequest-1656358085";
       Operation response =
           regionInstanceGroupManagerResizeRequestsClient
               .cancelAsync(project, region, instanceGroupManager, resizeRequest)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region scoping this request. Name should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group. Name should conform to RFC1035 or be a resource ID.  
`resizeRequest` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the resize request to cancel. Name should conform to RFC1035 or be a resource ID.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cancelCallable()
    
    
    public final UnaryCallable<CancelRegionInstanceGroupManagerResizeRequestRequest,Operation> cancelCallable()

Cancels the specified resize request. Cancelled resize request no longer waits for the resources to be provisioned. Cancel is only possible for requests that are in accepted state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       CancelRegionInstanceGroupManagerResizeRequestRequest request =
           CancelRegionInstanceGroupManagerResizeRequestRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setResizeRequest("resizeRequest-1656358085")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagerResizeRequestsClient.cancelCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CancelRegionInstanceGroupManagerResizeRequestRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cancelOperationCallable()
    
    
    public final OperationCallable<CancelRegionInstanceGroupManagerResizeRequestRequest,Operation,Operation> cancelOperationCallable()

Cancels the specified resize request. Cancelled resize request no longer waits for the resources to be provisioned. Cancel is only possible for requests that are in accepted state.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       CancelRegionInstanceGroupManagerResizeRequestRequest request =
           CancelRegionInstanceGroupManagerResizeRequestRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setResizeRequest("resizeRequest-1656358085")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagerResizeRequestsClient
               .cancelOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CancelRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CancelRegionInstanceGroupManagerResizeRequestRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### close()
    
    
    public final void close()

### deleteAsync(DeleteRegionInstanceGroupManagerResizeRequestRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRegionInstanceGroupManagerResizeRequestRequest request)

Deletes the specified, inactive resize request. Requests that are still active cannot be deleted. Deleting request does not delete instances that were provisioned previously.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       DeleteRegionInstanceGroupManagerResizeRequestRequest request =
           DeleteRegionInstanceGroupManagerResizeRequestRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setResizeRequest("resizeRequest-1656358085")
               .build();
       Operation response =
           regionInstanceGroupManagerResizeRequestsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionInstanceGroupManagerResizeRequestRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String instanceGroupManager, String resizeRequest)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String instanceGroupManager, String resizeRequest)

Deletes the specified, inactive resize request. Requests that are still active cannot be deleted. Deleting request does not delete instances that were provisioned previously.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       String resizeRequest = "resizeRequest-1656358085";
       Operation response =
           regionInstanceGroupManagerResizeRequestsClient
               .deleteAsync(project, region, instanceGroupManager, resizeRequest)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region scoping this request. Name should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group. Name should conform to RFC1035 or be a resource ID.  
`resizeRequest` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the resize request to delete. Name should conform to RFC1035 or be a resource ID.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRegionInstanceGroupManagerResizeRequestRequest,Operation> deleteCallable()

Deletes the specified, inactive resize request. Requests that are still active cannot be deleted. Deleting request does not delete instances that were provisioned previously.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       DeleteRegionInstanceGroupManagerResizeRequestRequest request =
           DeleteRegionInstanceGroupManagerResizeRequestRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setResizeRequest("resizeRequest-1656358085")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagerResizeRequestsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionInstanceGroupManagerResizeRequestRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRegionInstanceGroupManagerResizeRequestRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified, inactive resize request. Requests that are still active cannot be deleted. Deleting request does not delete instances that were provisioned previously.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       DeleteRegionInstanceGroupManagerResizeRequestRequest request =
           DeleteRegionInstanceGroupManagerResizeRequestRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setResizeRequest("resizeRequest-1656358085")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagerResizeRequestsClient
               .deleteOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionInstanceGroupManagerResizeRequestRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRegionInstanceGroupManagerResizeRequestRequest request)
    
    
    public final InstanceGroupManagerResizeRequest get(GetRegionInstanceGroupManagerResizeRequestRequest request)

Returns all of the details about the specified resize request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       GetRegionInstanceGroupManagerResizeRequestRequest request =
           GetRegionInstanceGroupManagerResizeRequestRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResizeRequest("resizeRequest-1656358085")
               .build();
       InstanceGroupManagerResizeRequest response =
           regionInstanceGroupManagerResizeRequestsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionInstanceGroupManagerResizeRequestRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManagerResizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagerResizeRequest)` |   
  
### get(String project, String region, String instanceGroupManager, String resizeRequest)
    
    
    public final InstanceGroupManagerResizeRequest get(String project, String region, String instanceGroupManager, String resizeRequest)

Returns all of the details about the specified resize request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       String resizeRequest = "resizeRequest-1656358085";
       InstanceGroupManagerResizeRequest response =
           regionInstanceGroupManagerResizeRequestsClient.get(
               project, region, instanceGroupManager, resizeRequest);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region scoping this request. Name should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group. Name should conform to RFC1035 or be a resource ID.  
`resizeRequest` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the resize request. Name should conform to RFC1035 or be a resource ID.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupManagerResizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagerResizeRequest)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRegionInstanceGroupManagerResizeRequestRequest,InstanceGroupManagerResizeRequest> getCallable()

Returns all of the details about the specified resize request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       GetRegionInstanceGroupManagerResizeRequestRequest request =
           GetRegionInstanceGroupManagerResizeRequestRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResizeRequest("resizeRequest-1656358085")
               .build();
       ApiFuture<InstanceGroupManagerResizeRequest> future =
           regionInstanceGroupManagerResizeRequestsClient.getCallable().futureCall(request);
       // Do something.
       InstanceGroupManagerResizeRequest response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionInstanceGroupManagerResizeRequestRequest),[InstanceGroupManagerResizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagerResizeRequest)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionInstanceGroupManagerResizeRequestsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequestsSettings` |   
  
### getStub()
    
    
    public RegionInstanceGroupManagerResizeRequestsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagerResizeRequestsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionInstanceGroupManagerResizeRequestsStub)` |   
  
### insertAsync(InsertRegionInstanceGroupManagerResizeRequestRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRegionInstanceGroupManagerResizeRequestRequest request)

Creates a new Resize Request that starts provisioning VMs immediately or queues VM creation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       InsertRegionInstanceGroupManagerResizeRequestRequest request =
           InsertRegionInstanceGroupManagerResizeRequestRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagerResizeRequestResource(
                   InstanceGroupManagerResizeRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response =
           regionInstanceGroupManagerResizeRequestsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionInstanceGroupManagerResizeRequestRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, String instanceGroupManager, InstanceGroupManagerResizeRequest instanceGroupManagerResizeRequestResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, String instanceGroupManager, InstanceGroupManagerResizeRequest instanceGroupManagerResizeRequestResource)

Creates a new Resize Request that starts provisioning VMs immediately or queues VM creation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       InstanceGroupManagerResizeRequest instanceGroupManagerResizeRequestResource =
           InstanceGroupManagerResizeRequest.newBuilder().build();
       Operation response =
           regionInstanceGroupManagerResizeRequestsClient
               .insertAsync(
                   project, region, instanceGroupManager, instanceGroupManagerResizeRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request. Name should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the managed instance group to which the resize request is scoped. Name should conform to RFC1035 or be a resource ID.  
`instanceGroupManagerResizeRequestResource` | `[InstanceGroupManagerResizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagerResizeRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRegionInstanceGroupManagerResizeRequestRequest,Operation> insertCallable()

Creates a new Resize Request that starts provisioning VMs immediately or queues VM creation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       InsertRegionInstanceGroupManagerResizeRequestRequest request =
           InsertRegionInstanceGroupManagerResizeRequestRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagerResizeRequestResource(
                   InstanceGroupManagerResizeRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupManagerResizeRequestsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionInstanceGroupManagerResizeRequestRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRegionInstanceGroupManagerResizeRequestRequest,Operation,Operation> insertOperationCallable()

Creates a new Resize Request that starts provisioning VMs immediately or queues VM creation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       InsertRegionInstanceGroupManagerResizeRequestRequest request =
           InsertRegionInstanceGroupManagerResizeRequestRequest.newBuilder()
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setInstanceGroupManagerResizeRequestResource(
                   InstanceGroupManagerResizeRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupManagerResizeRequestsClient
               .insertOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionInstanceGroupManagerResizeRequestRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRegionInstanceGroupManagerResizeRequestsRequest request)
    
    
    public final RegionInstanceGroupManagerResizeRequestsClient.ListPagedResponse list(ListRegionInstanceGroupManagerResizeRequestsRequest request)

Retrieves a list of Resize Requests that are contained in the managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       ListRegionInstanceGroupManagerResizeRequestsRequest request =
           ListRegionInstanceGroupManagerResizeRequestsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (InstanceGroupManagerResizeRequest element :
           regionInstanceGroupManagerResizeRequestsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionInstanceGroupManagerResizeRequestsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionInstanceGroupManagerResizeRequestsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagerResizeRequestsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequestsClient.ListPagedResponse)` |   
  
### list(String project, String region, String instanceGroupManager)
    
    
    public final RegionInstanceGroupManagerResizeRequestsClient.ListPagedResponse list(String project, String region, String instanceGroupManager)

Retrieves a list of Resize Requests that are contained in the managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroupManager = "instanceGroupManager-388242077";
       for (InstanceGroupManagerResizeRequest element :
           regionInstanceGroupManagerResizeRequestsClient
               .list(project, region, instanceGroupManager)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request. Name should conform to RFC1035.  
`instanceGroupManager` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the managed instance group. The name should conform to RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupManagerResizeRequestsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequestsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRegionInstanceGroupManagerResizeRequestsRequest,RegionInstanceGroupManagerResizeRequestsListResponse> listCallable()

Retrieves a list of Resize Requests that are contained in the managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       ListRegionInstanceGroupManagerResizeRequestsRequest request =
           ListRegionInstanceGroupManagerResizeRequestsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         RegionInstanceGroupManagerResizeRequestsListResponse response =
             regionInstanceGroupManagerResizeRequestsClient.listCallable().call(request);
         for (InstanceGroupManagerResizeRequest element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionInstanceGroupManagerResizeRequestsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionInstanceGroupManagerResizeRequestsRequest),[RegionInstanceGroupManagerResizeRequestsListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequestsListResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRegionInstanceGroupManagerResizeRequestsRequest,RegionInstanceGroupManagerResizeRequestsClient.ListPagedResponse> listPagedCallable()

Retrieves a list of Resize Requests that are contained in the managed instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupManagerResizeRequestsClient
         regionInstanceGroupManagerResizeRequestsClient =
             RegionInstanceGroupManagerResizeRequestsClient.create()) {
       ListRegionInstanceGroupManagerResizeRequestsRequest request =
           ListRegionInstanceGroupManagerResizeRequestsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroupManager("instanceGroupManager-388242077")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<InstanceGroupManagerResizeRequest> future =
           regionInstanceGroupManagerResizeRequestsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (InstanceGroupManagerResizeRequest element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionInstanceGroupManagerResizeRequestsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionInstanceGroupManagerResizeRequestsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequestsClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
