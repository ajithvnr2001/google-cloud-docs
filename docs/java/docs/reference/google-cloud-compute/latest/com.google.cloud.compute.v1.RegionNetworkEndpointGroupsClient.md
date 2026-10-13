---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkEndpointGroupsClient
title: Class RegionNetworkEndpointGroupsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:51.136407+00:00
---

# Class RegionNetworkEndpointGroupsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkEndpointGroupsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionNetworkEndpointGroupsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RegionNetworkEndpointGroupsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RegionNetworkEndpointGroups API.

This client uses RegionNetworkEndpointGroups version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       NetworkEndpointGroup response =
           regionNetworkEndpointGroupsClient.get(project, region, networkEndpointGroup);
     }
     

Note: close() needs to be called on the RegionNetworkEndpointGroupsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AttachNetworkEndpoints |  Attach a list of network endpoints to the specified network endpoint group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * attachNetworkEndpointsAsync(AttachNetworkEndpointsRegionNetworkEndpointGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * attachNetworkEndpointsAsync(String project, String region, String networkEndpointGroup, RegionNetworkEndpointGroupsAttachEndpointsRequest regionNetworkEndpointGroupsAttachEndpointsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * attachNetworkEndpointsOperationCallable() 
  * attachNetworkEndpointsCallable() 

  
Delete |  Deletes the specified network endpoint group. Note that the NEG cannot be deleted if it is configured as a backend of a backend service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRegionNetworkEndpointGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String networkEndpointGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
DetachNetworkEndpoints |  Detach the network endpoint from the specified network endpoint group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * detachNetworkEndpointsAsync(DetachNetworkEndpointsRegionNetworkEndpointGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * detachNetworkEndpointsAsync(String project, String region, String networkEndpointGroup, RegionNetworkEndpointGroupsDetachEndpointsRequest regionNetworkEndpointGroupsDetachEndpointsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * detachNetworkEndpointsOperationCallable() 
  * detachNetworkEndpointsCallable() 

  
Get |  Returns the specified network endpoint group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRegionNetworkEndpointGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String networkEndpointGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a network endpoint group in the specified project using the parameters that are included in the request.  Note: Use the following APIs to manage network endpoint groups:  \- To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API - To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API - To manage NEGs with global scope (such as global internet NEGs):global API |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRegionNetworkEndpointGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, NetworkEndpointGroup networkEndpointGroupResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of regional network endpoint groups available to the specified project in the given region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRegionNetworkEndpointGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListNetworkEndpoints |  Lists the network endpoints in the specified network endpoint group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNetworkEndpoints(ListNetworkEndpointsRegionNetworkEndpointGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNetworkEndpoints(String project, String region, String networkEndpointGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNetworkEndpointsPagedCallable() 
  * listNetworkEndpointsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionNetworkEndpointGroupsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionNetworkEndpointGroupsSettings regionNetworkEndpointGroupsSettings =
         RegionNetworkEndpointGroupsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create(regionNetworkEndpointGroupsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionNetworkEndpointGroupsSettings regionNetworkEndpointGroupsSettings =
         RegionNetworkEndpointGroupsSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create(regionNetworkEndpointGroupsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionNetworkEndpointGroupsClient

## Static Methods 

### create()
    
    
    public static final RegionNetworkEndpointGroupsClient create()

Constructs an instance of RegionNetworkEndpointGroupsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionNetworkEndpointGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkEndpointGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionNetworkEndpointGroupsSettings settings)
    
    
    public static final RegionNetworkEndpointGroupsClient create(RegionNetworkEndpointGroupsSettings settings)

Constructs an instance of RegionNetworkEndpointGroupsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionNetworkEndpointGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkEndpointGroupsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionNetworkEndpointGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkEndpointGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionNetworkEndpointGroupsStub stub)
    
    
    public static final RegionNetworkEndpointGroupsClient create(RegionNetworkEndpointGroupsStub stub)

Constructs an instance of RegionNetworkEndpointGroupsClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionNetworkEndpointGroupsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionNetworkEndpointGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionNetworkEndpointGroupsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionNetworkEndpointGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkEndpointGroupsClient)` |   
  
## Constructors 

### RegionNetworkEndpointGroupsClient(RegionNetworkEndpointGroupsSettings settings)
    
    
    protected RegionNetworkEndpointGroupsClient(RegionNetworkEndpointGroupsSettings settings)

Constructs an instance of RegionNetworkEndpointGroupsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionNetworkEndpointGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkEndpointGroupsSettings)`  
  
  
### RegionNetworkEndpointGroupsClient(RegionNetworkEndpointGroupsStub stub)
    
    
    protected RegionNetworkEndpointGroupsClient(RegionNetworkEndpointGroupsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionNetworkEndpointGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionNetworkEndpointGroupsStub)`  
  
  
## Methods 

### attachNetworkEndpointsAsync(AttachNetworkEndpointsRegionNetworkEndpointGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> attachNetworkEndpointsAsync(AttachNetworkEndpointsRegionNetworkEndpointGroupRequest request)

Attach a list of network endpoints to the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       AttachNetworkEndpointsRegionNetworkEndpointGroupRequest request =
           AttachNetworkEndpointsRegionNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionNetworkEndpointGroupsAttachEndpointsRequestResource(
                   RegionNetworkEndpointGroupsAttachEndpointsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response =
           regionNetworkEndpointGroupsClient.attachNetworkEndpointsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AttachNetworkEndpointsRegionNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachNetworkEndpointsRegionNetworkEndpointGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### attachNetworkEndpointsAsync(String project, String region, String networkEndpointGroup, RegionNetworkEndpointGroupsAttachEndpointsRequest regionNetworkEndpointGroupsAttachEndpointsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> attachNetworkEndpointsAsync(String project, String region, String networkEndpointGroup, RegionNetworkEndpointGroupsAttachEndpointsRequest regionNetworkEndpointGroupsAttachEndpointsRequestResource)

Attach a list of network endpoints to the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       RegionNetworkEndpointGroupsAttachEndpointsRequest
           regionNetworkEndpointGroupsAttachEndpointsRequestResource =
               RegionNetworkEndpointGroupsAttachEndpointsRequest.newBuilder().build();
       Operation response =
           regionNetworkEndpointGroupsClient
               .attachNetworkEndpointsAsync(
                   project,
                   region,
                   networkEndpointGroup,
                   regionNetworkEndpointGroupsAttachEndpointsRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region where you want to create the network endpoint group. It should comply with RFC1035.  
`networkEndpointGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network endpoint group where you are attaching network endpoints to. It should comply with RFC1035.  
`regionNetworkEndpointGroupsAttachEndpointsRequestResource` | `[RegionNetworkEndpointGroupsAttachEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkEndpointGroupsAttachEndpointsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### attachNetworkEndpointsCallable()
    
    
    public final UnaryCallable<AttachNetworkEndpointsRegionNetworkEndpointGroupRequest,Operation> attachNetworkEndpointsCallable()

Attach a list of network endpoints to the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       AttachNetworkEndpointsRegionNetworkEndpointGroupRequest request =
           AttachNetworkEndpointsRegionNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionNetworkEndpointGroupsAttachEndpointsRequestResource(
                   RegionNetworkEndpointGroupsAttachEndpointsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionNetworkEndpointGroupsClient.attachNetworkEndpointsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AttachNetworkEndpointsRegionNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachNetworkEndpointsRegionNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### attachNetworkEndpointsOperationCallable()
    
    
    public final OperationCallable<AttachNetworkEndpointsRegionNetworkEndpointGroupRequest,Operation,Operation> attachNetworkEndpointsOperationCallable()

Attach a list of network endpoints to the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       AttachNetworkEndpointsRegionNetworkEndpointGroupRequest request =
           AttachNetworkEndpointsRegionNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionNetworkEndpointGroupsAttachEndpointsRequestResource(
                   RegionNetworkEndpointGroupsAttachEndpointsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionNetworkEndpointGroupsClient
               .attachNetworkEndpointsOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AttachNetworkEndpointsRegionNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachNetworkEndpointsRegionNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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

### deleteAsync(DeleteRegionNetworkEndpointGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRegionNetworkEndpointGroupRequest request)

Deletes the specified network endpoint group. Note that the NEG cannot be deleted if it is configured as a backend of a backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       DeleteRegionNetworkEndpointGroupRequest request =
           DeleteRegionNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionNetworkEndpointGroupsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionNetworkEndpointGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String networkEndpointGroup)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String networkEndpointGroup)

Deletes the specified network endpoint group. Note that the NEG cannot be deleted if it is configured as a backend of a backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       Operation response =
           regionNetworkEndpointGroupsClient
               .deleteAsync(project, region, networkEndpointGroup)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region where the network endpoint group is located. It should comply with RFC1035.  
`networkEndpointGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network endpoint group to delete. It should comply with RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRegionNetworkEndpointGroupRequest,Operation> deleteCallable()

Deletes the specified network endpoint group. Note that the NEG cannot be deleted if it is configured as a backend of a backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       DeleteRegionNetworkEndpointGroupRequest request =
           DeleteRegionNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionNetworkEndpointGroupsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRegionNetworkEndpointGroupRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified network endpoint group. Note that the NEG cannot be deleted if it is configured as a backend of a backend service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       DeleteRegionNetworkEndpointGroupRequest request =
           DeleteRegionNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionNetworkEndpointGroupsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRegionNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachNetworkEndpointsAsync(DetachNetworkEndpointsRegionNetworkEndpointGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> detachNetworkEndpointsAsync(DetachNetworkEndpointsRegionNetworkEndpointGroupRequest request)

Detach the network endpoint from the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       DetachNetworkEndpointsRegionNetworkEndpointGroupRequest request =
           DetachNetworkEndpointsRegionNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionNetworkEndpointGroupsDetachEndpointsRequestResource(
                   RegionNetworkEndpointGroupsDetachEndpointsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response =
           regionNetworkEndpointGroupsClient.detachNetworkEndpointsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DetachNetworkEndpointsRegionNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DetachNetworkEndpointsRegionNetworkEndpointGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachNetworkEndpointsAsync(String project, String region, String networkEndpointGroup, RegionNetworkEndpointGroupsDetachEndpointsRequest regionNetworkEndpointGroupsDetachEndpointsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> detachNetworkEndpointsAsync(String project, String region, String networkEndpointGroup, RegionNetworkEndpointGroupsDetachEndpointsRequest regionNetworkEndpointGroupsDetachEndpointsRequestResource)

Detach the network endpoint from the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       RegionNetworkEndpointGroupsDetachEndpointsRequest
           regionNetworkEndpointGroupsDetachEndpointsRequestResource =
               RegionNetworkEndpointGroupsDetachEndpointsRequest.newBuilder().build();
       Operation response =
           regionNetworkEndpointGroupsClient
               .detachNetworkEndpointsAsync(
                   project,
                   region,
                   networkEndpointGroup,
                   regionNetworkEndpointGroupsDetachEndpointsRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region where the network endpoint group is located. It should comply with RFC1035.  
`networkEndpointGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network endpoint group you are detaching network endpoints from. It should comply with RFC1035.  
`regionNetworkEndpointGroupsDetachEndpointsRequestResource` | `[RegionNetworkEndpointGroupsDetachEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkEndpointGroupsDetachEndpointsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachNetworkEndpointsCallable()
    
    
    public final UnaryCallable<DetachNetworkEndpointsRegionNetworkEndpointGroupRequest,Operation> detachNetworkEndpointsCallable()

Detach the network endpoint from the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       DetachNetworkEndpointsRegionNetworkEndpointGroupRequest request =
           DetachNetworkEndpointsRegionNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionNetworkEndpointGroupsDetachEndpointsRequestResource(
                   RegionNetworkEndpointGroupsDetachEndpointsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionNetworkEndpointGroupsClient.detachNetworkEndpointsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DetachNetworkEndpointsRegionNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DetachNetworkEndpointsRegionNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachNetworkEndpointsOperationCallable()
    
    
    public final OperationCallable<DetachNetworkEndpointsRegionNetworkEndpointGroupRequest,Operation,Operation> detachNetworkEndpointsOperationCallable()

Detach the network endpoint from the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       DetachNetworkEndpointsRegionNetworkEndpointGroupRequest request =
           DetachNetworkEndpointsRegionNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionNetworkEndpointGroupsDetachEndpointsRequestResource(
                   RegionNetworkEndpointGroupsDetachEndpointsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionNetworkEndpointGroupsClient
               .detachNetworkEndpointsOperationCallable()
               .futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DetachNetworkEndpointsRegionNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DetachNetworkEndpointsRegionNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRegionNetworkEndpointGroupRequest request)
    
    
    public final NetworkEndpointGroup get(GetRegionNetworkEndpointGroupRequest request)

Returns the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       GetRegionNetworkEndpointGroupRequest request =
           GetRegionNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       NetworkEndpointGroup response = regionNetworkEndpointGroupsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegionNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionNetworkEndpointGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroup)` |   
  
### get(String project, String region, String networkEndpointGroup)
    
    
    public final NetworkEndpointGroup get(String project, String region, String networkEndpointGroup)

Returns the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       NetworkEndpointGroup response =
           regionNetworkEndpointGroupsClient.get(project, region, networkEndpointGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region where the network endpoint group is located. It should comply with RFC1035.  
`networkEndpointGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network endpoint group. It should comply with RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroup)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRegionNetworkEndpointGroupRequest,NetworkEndpointGroup> getCallable()

Returns the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       GetRegionNetworkEndpointGroupRequest request =
           GetRegionNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<NetworkEndpointGroup> future =
           regionNetworkEndpointGroupsClient.getCallable().futureCall(request);
       // Do something.
       NetworkEndpointGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegionNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionNetworkEndpointGroupRequest),[NetworkEndpointGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroup)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionNetworkEndpointGroupsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RegionNetworkEndpointGroupsSettings` |   
  
### getStub()
    
    
    public RegionNetworkEndpointGroupsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionNetworkEndpointGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionNetworkEndpointGroupsStub)` |   
  
### insertAsync(InsertRegionNetworkEndpointGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRegionNetworkEndpointGroupRequest request)

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
        try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
          RegionNetworkEndpointGroupsClient.create()) {
        InsertRegionNetworkEndpointGroupRequest request =
            InsertRegionNetworkEndpointGroupRequest.newBuilder()
                .setNetworkEndpointGroupResource(NetworkEndpointGroup.newBuilder().build())
                .setProject("project-309310695")
                .setRegion("region-934795532")
                .setRequestId("requestId693933066")
                .build();
        Operation response = regionNetworkEndpointGroupsClient.insertAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRegionNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionNetworkEndpointGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, NetworkEndpointGroup networkEndpointGroupResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, NetworkEndpointGroup networkEndpointGroupResource)

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
        try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
          RegionNetworkEndpointGroupsClient.create()) {
        String project = "project-309310695";
        String region = "region-934795532";
        NetworkEndpointGroup networkEndpointGroupResource = NetworkEndpointGroup.newBuilder().build();
        Operation response =
            regionNetworkEndpointGroupsClient
                .insertAsync(project, region, networkEndpointGroupResource)
                .get();
        }
        




**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region where you want to create the network endpoint group. It should comply with RFC1035.  
`networkEndpointGroupResource` | `[NetworkEndpointGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroup)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRegionNetworkEndpointGroupRequest,Operation> insertCallable()

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
        try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
          RegionNetworkEndpointGroupsClient.create()) {
        InsertRegionNetworkEndpointGroupRequest request =
            InsertRegionNetworkEndpointGroupRequest.newBuilder()
                .setNetworkEndpointGroupResource(NetworkEndpointGroup.newBuilder().build())
                .setProject("project-309310695")
                .setRegion("region-934795532")
                .setRequestId("requestId693933066")
                .build();
        ApiFuture<Operation> future =
            regionNetworkEndpointGroupsClient.insertCallable().futureCall(request);
        // Do something.
        Operation response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRegionNetworkEndpointGroupRequest,Operation,Operation> insertOperationCallable()

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
        try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
          RegionNetworkEndpointGroupsClient.create()) {
        InsertRegionNetworkEndpointGroupRequest request =
            InsertRegionNetworkEndpointGroupRequest.newBuilder()
                .setNetworkEndpointGroupResource(NetworkEndpointGroup.newBuilder().build())
                .setProject("project-309310695")
                .setRegion("region-934795532")
                .setRequestId("requestId693933066")
                .build();
        OperationFuture<Operation, Operation> future =
            regionNetworkEndpointGroupsClient.insertOperationCallable().futureCall(request);
        // Do something.
        Operation response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRegionNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRegionNetworkEndpointGroupsRequest request)
    
    
    public final RegionNetworkEndpointGroupsClient.ListPagedResponse list(ListRegionNetworkEndpointGroupsRequest request)

Retrieves the list of regional network endpoint groups available to the specified project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       ListRegionNetworkEndpointGroupsRequest request =
           ListRegionNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (NetworkEndpointGroup element :
           regionNetworkEndpointGroupsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionNetworkEndpointGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionNetworkEndpointGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkEndpointGroupsClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final RegionNetworkEndpointGroupsClient.ListPagedResponse list(String project, String region)

Retrieves the list of regional network endpoint groups available to the specified project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (NetworkEndpointGroup element :
           regionNetworkEndpointGroupsClient.list(project, region).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of theregion where the network endpoint group is located. It should comply with RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[RegionNetworkEndpointGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkEndpointGroupsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRegionNetworkEndpointGroupsRequest,NetworkEndpointGroupList> listCallable()

Retrieves the list of regional network endpoint groups available to the specified project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       ListRegionNetworkEndpointGroupsRequest request =
           ListRegionNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         NetworkEndpointGroupList response =
             regionNetworkEndpointGroupsClient.listCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionNetworkEndpointGroupsRequest),[NetworkEndpointGroupList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupList)>` |   
  
### listNetworkEndpoints(ListNetworkEndpointsRegionNetworkEndpointGroupsRequest request)
    
    
    public final RegionNetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse listNetworkEndpoints(ListNetworkEndpointsRegionNetworkEndpointGroupsRequest request)

Lists the network endpoints in the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       ListNetworkEndpointsRegionNetworkEndpointGroupsRequest request =
           ListNetworkEndpointsRegionNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (NetworkEndpointWithHealthStatus element :
           regionNetworkEndpointGroupsClient.listNetworkEndpoints(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNetworkEndpointsRegionNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworkEndpointsRegionNetworkEndpointGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionNetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse)` |   
  
### listNetworkEndpoints(String project, String region, String networkEndpointGroup)
    
    
    public final RegionNetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse listNetworkEndpoints(String project, String region, String networkEndpointGroup)

Lists the network endpoints in the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       for (NetworkEndpointWithHealthStatus element :
           regionNetworkEndpointGroupsClient
               .listNetworkEndpoints(project, region, networkEndpointGroup)
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
The name of theregion where the network endpoint group is located. It should comply with RFC1035.  
`networkEndpointGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network endpoint group from which you want to generate a list of included network endpoints. It should comply with RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[RegionNetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse)` |   
  
### listNetworkEndpointsCallable()
    
    
    public final UnaryCallable<ListNetworkEndpointsRegionNetworkEndpointGroupsRequest,NetworkEndpointGroupsListNetworkEndpoints> listNetworkEndpointsCallable()

Lists the network endpoints in the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       ListNetworkEndpointsRegionNetworkEndpointGroupsRequest request =
           ListNetworkEndpointsRegionNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         NetworkEndpointGroupsListNetworkEndpoints response =
             regionNetworkEndpointGroupsClient.listNetworkEndpointsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworkEndpointsRegionNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworkEndpointsRegionNetworkEndpointGroupsRequest),[NetworkEndpointGroupsListNetworkEndpoints](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsListNetworkEndpoints)>` |   
  
### listNetworkEndpointsPagedCallable()
    
    
    public final UnaryCallable<ListNetworkEndpointsRegionNetworkEndpointGroupsRequest,RegionNetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse> listNetworkEndpointsPagedCallable()

Lists the network endpoints in the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       ListNetworkEndpointsRegionNetworkEndpointGroupsRequest request =
           ListNetworkEndpointsRegionNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<NetworkEndpointWithHealthStatus> future =
           regionNetworkEndpointGroupsClient.listNetworkEndpointsPagedCallable().futureCall(request);
       // Do something.
       for (NetworkEndpointWithHealthStatus element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworkEndpointsRegionNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworkEndpointsRegionNetworkEndpointGroupsRequest),[ListNetworkEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRegionNetworkEndpointGroupsRequest,RegionNetworkEndpointGroupsClient.ListPagedResponse> listPagedCallable()

Retrieves the list of regional network endpoint groups available to the specified project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionNetworkEndpointGroupsClient regionNetworkEndpointGroupsClient =
         RegionNetworkEndpointGroupsClient.create()) {
       ListRegionNetworkEndpointGroupsRequest request =
           ListRegionNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<NetworkEndpointGroup> future =
           regionNetworkEndpointGroupsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (NetworkEndpointGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionNetworkEndpointGroupsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionNetworkEndpointGroupsClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
