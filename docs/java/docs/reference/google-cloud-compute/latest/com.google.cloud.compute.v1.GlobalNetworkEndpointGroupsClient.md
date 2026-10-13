---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalNetworkEndpointGroupsClient
title: Class GlobalNetworkEndpointGroupsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:21.872428+00:00
---

# Class GlobalNetworkEndpointGroupsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalNetworkEndpointGroupsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GlobalNetworkEndpointGroupsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/GlobalNetworkEndpointGroupsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The GlobalNetworkEndpointGroups API.

This client uses GlobalNetworkEndpointGroups version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       NetworkEndpointGroup response =
           globalNetworkEndpointGroupsClient.get(project, networkEndpointGroup);
     }
     

Note: close() needs to be called on the GlobalNetworkEndpointGroupsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AttachNetworkEndpoints |  Attach a network endpoint to the specified network endpoint group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * attachNetworkEndpointsAsync(AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * attachNetworkEndpointsAsync(String project, String networkEndpointGroup, GlobalNetworkEndpointGroupsAttachEndpointsRequest globalNetworkEndpointGroupsAttachEndpointsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * attachNetworkEndpointsOperationCallable() 
  * attachNetworkEndpointsCallable() 

  
Delete |  Deletes the specified network endpoint group.Note that the NEG cannot be deleted if there are backend services referencing it. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteGlobalNetworkEndpointGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String networkEndpointGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
DetachNetworkEndpoints |  Detach the network endpoint from the specified network endpoint group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * detachNetworkEndpointsAsync(DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * detachNetworkEndpointsAsync(String project, String networkEndpointGroup, GlobalNetworkEndpointGroupsDetachEndpointsRequest globalNetworkEndpointGroupsDetachEndpointsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * detachNetworkEndpointsOperationCallable() 
  * detachNetworkEndpointsCallable() 

  
Get |  Returns the specified network endpoint group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetGlobalNetworkEndpointGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String networkEndpointGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a network endpoint group in the specified project using the parameters that are included in the request.  Note: Use the following APIs to manage network endpoint groups:  \- To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API - To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API - To manage NEGs with global scope (such as global internet NEGs):global API |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertGlobalNetworkEndpointGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, NetworkEndpointGroup networkEndpointGroupResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of network endpoint groups that are located in the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListGlobalNetworkEndpointGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListNetworkEndpoints |  Lists the network endpoints in the specified network endpoint group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNetworkEndpoints(ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNetworkEndpoints(String project, String networkEndpointGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNetworkEndpointsPagedCallable() 
  * listNetworkEndpointsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of GlobalNetworkEndpointGroupsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GlobalNetworkEndpointGroupsSettings globalNetworkEndpointGroupsSettings =
         GlobalNetworkEndpointGroupsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create(globalNetworkEndpointGroupsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GlobalNetworkEndpointGroupsSettings globalNetworkEndpointGroupsSettings =
         GlobalNetworkEndpointGroupsSettings.newBuilder().setEndpoint(myEndpoint).build();
     GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create(globalNetworkEndpointGroupsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GlobalNetworkEndpointGroupsClient

## Static Methods 

### create()
    
    
    public static final GlobalNetworkEndpointGroupsClient create()

Constructs an instance of GlobalNetworkEndpointGroupsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalNetworkEndpointGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GlobalNetworkEndpointGroupsSettings settings)
    
    
    public static final GlobalNetworkEndpointGroupsClient create(GlobalNetworkEndpointGroupsSettings settings)

Constructs an instance of GlobalNetworkEndpointGroupsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GlobalNetworkEndpointGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalNetworkEndpointGroupsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalNetworkEndpointGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GlobalNetworkEndpointGroupsStub stub)
    
    
    public static final GlobalNetworkEndpointGroupsClient create(GlobalNetworkEndpointGroupsStub stub)

Constructs an instance of GlobalNetworkEndpointGroupsClient, using the given stub for making calls. This is for advanced usage - prefer using create(GlobalNetworkEndpointGroupsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GlobalNetworkEndpointGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalNetworkEndpointGroupsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalNetworkEndpointGroupsClient)` |   
  
## Constructors 

### GlobalNetworkEndpointGroupsClient(GlobalNetworkEndpointGroupsSettings settings)
    
    
    protected GlobalNetworkEndpointGroupsClient(GlobalNetworkEndpointGroupsSettings settings)

Constructs an instance of GlobalNetworkEndpointGroupsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GlobalNetworkEndpointGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalNetworkEndpointGroupsSettings)`  
  
  
### GlobalNetworkEndpointGroupsClient(GlobalNetworkEndpointGroupsStub stub)
    
    
    protected GlobalNetworkEndpointGroupsClient(GlobalNetworkEndpointGroupsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GlobalNetworkEndpointGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalNetworkEndpointGroupsStub)`  
  
  
## Methods 

### attachNetworkEndpointsAsync(AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> attachNetworkEndpointsAsync(AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest request)

Attach a network endpoint to the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest request =
           AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest.newBuilder()
               .setGlobalNetworkEndpointGroupsAttachEndpointsRequestResource(
                   GlobalNetworkEndpointGroupsAttachEndpointsRequest.newBuilder().build())
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response =
           globalNetworkEndpointGroupsClient.attachNetworkEndpointsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### attachNetworkEndpointsAsync(String project, String networkEndpointGroup, GlobalNetworkEndpointGroupsAttachEndpointsRequest globalNetworkEndpointGroupsAttachEndpointsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> attachNetworkEndpointsAsync(String project, String networkEndpointGroup, GlobalNetworkEndpointGroupsAttachEndpointsRequest globalNetworkEndpointGroupsAttachEndpointsRequestResource)

Attach a network endpoint to the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       GlobalNetworkEndpointGroupsAttachEndpointsRequest
           globalNetworkEndpointGroupsAttachEndpointsRequestResource =
               GlobalNetworkEndpointGroupsAttachEndpointsRequest.newBuilder().build();
       Operation response =
           globalNetworkEndpointGroupsClient
               .attachNetworkEndpointsAsync(
                   project,
                   networkEndpointGroup,
                   globalNetworkEndpointGroupsAttachEndpointsRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`networkEndpointGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network endpoint group where you are attaching network endpoints to. It should comply with RFC1035.  
`globalNetworkEndpointGroupsAttachEndpointsRequestResource` | `[GlobalNetworkEndpointGroupsAttachEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalNetworkEndpointGroupsAttachEndpointsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### attachNetworkEndpointsCallable()
    
    
    public final UnaryCallable<AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest,Operation> attachNetworkEndpointsCallable()

Attach a network endpoint to the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest request =
           AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest.newBuilder()
               .setGlobalNetworkEndpointGroupsAttachEndpointsRequestResource(
                   GlobalNetworkEndpointGroupsAttachEndpointsRequest.newBuilder().build())
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           globalNetworkEndpointGroupsClient.attachNetworkEndpointsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### attachNetworkEndpointsOperationCallable()
    
    
    public final OperationCallable<AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest,Operation,Operation> attachNetworkEndpointsOperationCallable()

Attach a network endpoint to the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest request =
           AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest.newBuilder()
               .setGlobalNetworkEndpointGroupsAttachEndpointsRequestResource(
                   GlobalNetworkEndpointGroupsAttachEndpointsRequest.newBuilder().build())
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           globalNetworkEndpointGroupsClient
               .attachNetworkEndpointsOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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

### deleteAsync(DeleteGlobalNetworkEndpointGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteGlobalNetworkEndpointGroupRequest request)

Deletes the specified network endpoint group.Note that the NEG cannot be deleted if there are backend services referencing it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       DeleteGlobalNetworkEndpointGroupRequest request =
           DeleteGlobalNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = globalNetworkEndpointGroupsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalNetworkEndpointGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String networkEndpointGroup)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String networkEndpointGroup)

Deletes the specified network endpoint group.Note that the NEG cannot be deleted if there are backend services referencing it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       Operation response =
           globalNetworkEndpointGroupsClient.deleteAsync(project, networkEndpointGroup).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`networkEndpointGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network endpoint group to delete. It should comply with RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteGlobalNetworkEndpointGroupRequest,Operation> deleteCallable()

Deletes the specified network endpoint group.Note that the NEG cannot be deleted if there are backend services referencing it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       DeleteGlobalNetworkEndpointGroupRequest request =
           DeleteGlobalNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           globalNetworkEndpointGroupsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteGlobalNetworkEndpointGroupRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified network endpoint group.Note that the NEG cannot be deleted if there are backend services referencing it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       DeleteGlobalNetworkEndpointGroupRequest request =
           DeleteGlobalNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           globalNetworkEndpointGroupsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachNetworkEndpointsAsync(DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> detachNetworkEndpointsAsync(DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest request)

Detach the network endpoint from the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest request =
           DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest.newBuilder()
               .setGlobalNetworkEndpointGroupsDetachEndpointsRequestResource(
                   GlobalNetworkEndpointGroupsDetachEndpointsRequest.newBuilder().build())
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response =
           globalNetworkEndpointGroupsClient.detachNetworkEndpointsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachNetworkEndpointsAsync(String project, String networkEndpointGroup, GlobalNetworkEndpointGroupsDetachEndpointsRequest globalNetworkEndpointGroupsDetachEndpointsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> detachNetworkEndpointsAsync(String project, String networkEndpointGroup, GlobalNetworkEndpointGroupsDetachEndpointsRequest globalNetworkEndpointGroupsDetachEndpointsRequestResource)

Detach the network endpoint from the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       GlobalNetworkEndpointGroupsDetachEndpointsRequest
           globalNetworkEndpointGroupsDetachEndpointsRequestResource =
               GlobalNetworkEndpointGroupsDetachEndpointsRequest.newBuilder().build();
       Operation response =
           globalNetworkEndpointGroupsClient
               .detachNetworkEndpointsAsync(
                   project,
                   networkEndpointGroup,
                   globalNetworkEndpointGroupsDetachEndpointsRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`networkEndpointGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network endpoint group where you are removing network endpoints. It should comply with RFC1035.  
`globalNetworkEndpointGroupsDetachEndpointsRequestResource` | `[GlobalNetworkEndpointGroupsDetachEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalNetworkEndpointGroupsDetachEndpointsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachNetworkEndpointsCallable()
    
    
    public final UnaryCallable<DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest,Operation> detachNetworkEndpointsCallable()

Detach the network endpoint from the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest request =
           DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest.newBuilder()
               .setGlobalNetworkEndpointGroupsDetachEndpointsRequestResource(
                   GlobalNetworkEndpointGroupsDetachEndpointsRequest.newBuilder().build())
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           globalNetworkEndpointGroupsClient.detachNetworkEndpointsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachNetworkEndpointsOperationCallable()
    
    
    public final OperationCallable<DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest,Operation,Operation> detachNetworkEndpointsOperationCallable()

Detach the network endpoint from the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest request =
           DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest.newBuilder()
               .setGlobalNetworkEndpointGroupsDetachEndpointsRequestResource(
                   GlobalNetworkEndpointGroupsDetachEndpointsRequest.newBuilder().build())
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           globalNetworkEndpointGroupsClient
               .detachNetworkEndpointsOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetGlobalNetworkEndpointGroupRequest request)
    
    
    public final NetworkEndpointGroup get(GetGlobalNetworkEndpointGroupRequest request)

Returns the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       GetGlobalNetworkEndpointGroupRequest request =
           GetGlobalNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .build();
       NetworkEndpointGroup response = globalNetworkEndpointGroupsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGlobalNetworkEndpointGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroup)` |   
  
### get(String project, String networkEndpointGroup)
    
    
    public final NetworkEndpointGroup get(String project, String networkEndpointGroup)

Returns the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       NetworkEndpointGroup response =
           globalNetworkEndpointGroupsClient.get(project, networkEndpointGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`networkEndpointGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network endpoint group. It should comply with RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroup)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetGlobalNetworkEndpointGroupRequest,NetworkEndpointGroup> getCallable()

Returns the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       GetGlobalNetworkEndpointGroupRequest request =
           GetGlobalNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .build();
       ApiFuture<NetworkEndpointGroup> future =
           globalNetworkEndpointGroupsClient.getCallable().futureCall(request);
       // Do something.
       NetworkEndpointGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGlobalNetworkEndpointGroupRequest),[NetworkEndpointGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroup)>` |   
  
### getSettings()
    
    
    public final @Nullable GlobalNetworkEndpointGroupsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.GlobalNetworkEndpointGroupsSettings` |   
  
### getStub()
    
    
    public GlobalNetworkEndpointGroupsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[GlobalNetworkEndpointGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalNetworkEndpointGroupsStub)` |   
  
### insertAsync(InsertGlobalNetworkEndpointGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertGlobalNetworkEndpointGroupRequest request)

Creates a network endpoint group in the specified project using the parameters that are included in the request.

Note: Use the following APIs to manage network endpoint groups:

\- To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API

  * To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API - To manage NEGs with global scope (such as global internet NEGs):global API

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
          GlobalNetworkEndpointGroupsClient.create()) {
        InsertGlobalNetworkEndpointGroupRequest request =
            InsertGlobalNetworkEndpointGroupRequest.newBuilder()
                .setNetworkEndpointGroupResource(NetworkEndpointGroup.newBuilder().build())
                .setProject("project-309310695")
                .setRequestId("requestId693933066")
                .build();
        Operation response = globalNetworkEndpointGroupsClient.insertAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertGlobalNetworkEndpointGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, NetworkEndpointGroup networkEndpointGroupResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, NetworkEndpointGroup networkEndpointGroupResource)

Creates a network endpoint group in the specified project using the parameters that are included in the request.

Note: Use the following APIs to manage network endpoint groups:

\- To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API

  * To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API - To manage NEGs with global scope (such as global internet NEGs):global API

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
          GlobalNetworkEndpointGroupsClient.create()) {
        String project = "project-309310695";
        NetworkEndpointGroup networkEndpointGroupResource = NetworkEndpointGroup.newBuilder().build();
        Operation response =
            globalNetworkEndpointGroupsClient
                .insertAsync(project, networkEndpointGroupResource)
                .get();
        }
        




**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`networkEndpointGroupResource` | `[NetworkEndpointGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroup)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertGlobalNetworkEndpointGroupRequest,Operation> insertCallable()

Creates a network endpoint group in the specified project using the parameters that are included in the request.

Note: Use the following APIs to manage network endpoint groups:

\- To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API

  * To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API - To manage NEGs with global scope (such as global internet NEGs):global API

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
          GlobalNetworkEndpointGroupsClient.create()) {
        InsertGlobalNetworkEndpointGroupRequest request =
            InsertGlobalNetworkEndpointGroupRequest.newBuilder()
                .setNetworkEndpointGroupResource(NetworkEndpointGroup.newBuilder().build())
                .setProject("project-309310695")
                .setRequestId("requestId693933066")
                .build();
        ApiFuture<Operation> future =
            globalNetworkEndpointGroupsClient.insertCallable().futureCall(request);
        // Do something.
        Operation response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertGlobalNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertGlobalNetworkEndpointGroupRequest,Operation,Operation> insertOperationCallable()

Creates a network endpoint group in the specified project using the parameters that are included in the request.

Note: Use the following APIs to manage network endpoint groups:

\- To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API

  * To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API - To manage NEGs with global scope (such as global internet NEGs):global API

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
          GlobalNetworkEndpointGroupsClient.create()) {
        InsertGlobalNetworkEndpointGroupRequest request =
            InsertGlobalNetworkEndpointGroupRequest.newBuilder()
                .setNetworkEndpointGroupResource(NetworkEndpointGroup.newBuilder().build())
                .setProject("project-309310695")
                .setRequestId("requestId693933066")
                .build();
        OperationFuture<Operation, Operation> future =
            globalNetworkEndpointGroupsClient.insertOperationCallable().futureCall(request);
        // Do something.
        Operation response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertGlobalNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListGlobalNetworkEndpointGroupsRequest request)
    
    
    public final GlobalNetworkEndpointGroupsClient.ListPagedResponse list(ListGlobalNetworkEndpointGroupsRequest request)

Retrieves the list of network endpoint groups that are located in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       ListGlobalNetworkEndpointGroupsRequest request =
           ListGlobalNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (NetworkEndpointGroup element :
           globalNetworkEndpointGroupsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGlobalNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalNetworkEndpointGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GlobalNetworkEndpointGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalNetworkEndpointGroupsClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final GlobalNetworkEndpointGroupsClient.ListPagedResponse list(String project)

Retrieves the list of network endpoint groups that are located in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       for (NetworkEndpointGroup element :
           globalNetworkEndpointGroupsClient.list(project).iterateAll()) {
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
`[GlobalNetworkEndpointGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalNetworkEndpointGroupsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListGlobalNetworkEndpointGroupsRequest,NetworkEndpointGroupList> listCallable()

Retrieves the list of network endpoint groups that are located in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       ListGlobalNetworkEndpointGroupsRequest request =
           ListGlobalNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         NetworkEndpointGroupList response =
             globalNetworkEndpointGroupsClient.listCallable().call(request);
         for (NetworkEndpointGroup element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlobalNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalNetworkEndpointGroupsRequest),[NetworkEndpointGroupList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupList)>` |   
  
### listNetworkEndpoints(ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest request)
    
    
    public final GlobalNetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse listNetworkEndpoints(ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest request)

Lists the network endpoints in the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest request =
           ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (NetworkEndpointWithHealthStatus element :
           globalNetworkEndpointGroupsClient.listNetworkEndpoints(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GlobalNetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalNetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse)` |   
  
### listNetworkEndpoints(String project, String networkEndpointGroup)
    
    
    public final GlobalNetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse listNetworkEndpoints(String project, String networkEndpointGroup)

Lists the network endpoints in the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       for (NetworkEndpointWithHealthStatus element :
           globalNetworkEndpointGroupsClient
               .listNetworkEndpoints(project, networkEndpointGroup)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`networkEndpointGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network endpoint group from which you want to generate a list of included network endpoints. It should comply with RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[GlobalNetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalNetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse)` |   
  
### listNetworkEndpointsCallable()
    
    
    public final UnaryCallable<ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest,NetworkEndpointGroupsListNetworkEndpoints> listNetworkEndpointsCallable()

Lists the network endpoints in the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest request =
           ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         NetworkEndpointGroupsListNetworkEndpoints response =
             globalNetworkEndpointGroupsClient.listNetworkEndpointsCallable().call(request);
         for (NetworkEndpointWithHealthStatus element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest),[NetworkEndpointGroupsListNetworkEndpoints](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsListNetworkEndpoints)>` |   
  
### listNetworkEndpointsPagedCallable()
    
    
    public final UnaryCallable<ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest,GlobalNetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse> listNetworkEndpointsPagedCallable()

Lists the network endpoints in the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest request =
           ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<NetworkEndpointWithHealthStatus> future =
           globalNetworkEndpointGroupsClient.listNetworkEndpointsPagedCallable().futureCall(request);
       // Do something.
       for (NetworkEndpointWithHealthStatus element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest),[ListNetworkEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalNetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListGlobalNetworkEndpointGroupsRequest,GlobalNetworkEndpointGroupsClient.ListPagedResponse> listPagedCallable()

Retrieves the list of network endpoint groups that are located in the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalNetworkEndpointGroupsClient globalNetworkEndpointGroupsClient =
         GlobalNetworkEndpointGroupsClient.create()) {
       ListGlobalNetworkEndpointGroupsRequest request =
           ListGlobalNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<NetworkEndpointGroup> future =
           globalNetworkEndpointGroupsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (NetworkEndpointGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlobalNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalNetworkEndpointGroupsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalNetworkEndpointGroupsClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
