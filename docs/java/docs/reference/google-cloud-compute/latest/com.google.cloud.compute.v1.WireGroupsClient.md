---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupsClient
title: Class WireGroupsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:48.811024+00:00
---

# Class WireGroupsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class WireGroupsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/WireGroupsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The WireGroups API.

This client uses WireGroups version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       String project = "project-309310695";
       String crossSiteNetwork = "crossSiteNetwork1009388679";
       String wireGroup = "wireGroup-970399494";
       WireGroup response = wireGroupsClient.get(project, crossSiteNetwork, wireGroup);
     }
     

Note: close() needs to be called on the WireGroupsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified wire group in the given scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteWireGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String crossSiteNetwork, String wireGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Gets the specified wire group resource in the given scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetWireGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String crossSiteNetwork, String wireGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a wire group in the specified project in the given scope using the parameters that are included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertWireGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String crossSiteNetwork, WireGroup wireGroupResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists the wire groups for a project in the given scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListWireGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String crossSiteNetwork) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Updates the specified wire group resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchWireGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String crossSiteNetwork, String wireGroup, WireGroup wireGroupResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of WireGroupsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     WireGroupsSettings wireGroupsSettings =
         WireGroupsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     WireGroupsClient wireGroupsClient = WireGroupsClient.create(wireGroupsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     WireGroupsSettings wireGroupsSettings =
         WireGroupsSettings.newBuilder().setEndpoint(myEndpoint).build();
     WireGroupsClient wireGroupsClient = WireGroupsClient.create(wireGroupsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > WireGroupsClient

## Static Methods 

### create()
    
    
    public static final WireGroupsClient create()

Constructs an instance of WireGroupsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[WireGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(WireGroupsSettings settings)
    
    
    public static final WireGroupsClient create(WireGroupsSettings settings)

Constructs an instance of WireGroupsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[WireGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WireGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(WireGroupsStub stub)
    
    
    public static final WireGroupsClient create(WireGroupsStub stub)

Constructs an instance of WireGroupsClient, using the given stub for making calls. This is for advanced usage - prefer using create(WireGroupsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[WireGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.WireGroupsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WireGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupsClient)` |   
  
## Constructors 

### WireGroupsClient(WireGroupsSettings settings)
    
    
    protected WireGroupsClient(WireGroupsSettings settings)

Constructs an instance of WireGroupsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[WireGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupsSettings)`  
  
  
### WireGroupsClient(WireGroupsStub stub)
    
    
    protected WireGroupsClient(WireGroupsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[WireGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.WireGroupsStub)`  
  
  
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

### deleteAsync(DeleteWireGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteWireGroupRequest request)

Deletes the specified wire group in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       DeleteWireGroupRequest request =
           DeleteWireGroupRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setWireGroup("wireGroup-970399494")
               .build();
       Operation response = wireGroupsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteWireGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteWireGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String crossSiteNetwork, String wireGroup)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String crossSiteNetwork, String wireGroup)

Deletes the specified wire group in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       String project = "project-309310695";
       String crossSiteNetwork = "crossSiteNetwork1009388679";
       String wireGroup = "wireGroup-970399494";
       Operation response = wireGroupsClient.deleteAsync(project, crossSiteNetwork, wireGroup).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`crossSiteNetwork` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`wireGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the wire group resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteWireGroupRequest,Operation> deleteCallable()

Deletes the specified wire group in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       DeleteWireGroupRequest request =
           DeleteWireGroupRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setWireGroup("wireGroup-970399494")
               .build();
       ApiFuture<Operation> future = wireGroupsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteWireGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteWireGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteWireGroupRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified wire group in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       DeleteWireGroupRequest request =
           DeleteWireGroupRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setWireGroup("wireGroup-970399494")
               .build();
       OperationFuture<Operation, Operation> future =
           wireGroupsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteWireGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteWireGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetWireGroupRequest request)
    
    
    public final WireGroup get(GetWireGroupRequest request)

Gets the specified wire group resource in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       GetWireGroupRequest request =
           GetWireGroupRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setProject("project-309310695")
               .setWireGroup("wireGroup-970399494")
               .build();
       WireGroup response = wireGroupsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetWireGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetWireGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WireGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroup)` |   
  
### get(String project, String crossSiteNetwork, String wireGroup)
    
    
    public final WireGroup get(String project, String crossSiteNetwork, String wireGroup)

Gets the specified wire group resource in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       String project = "project-309310695";
       String crossSiteNetwork = "crossSiteNetwork1009388679";
       String wireGroup = "wireGroup-970399494";
       WireGroup response = wireGroupsClient.get(project, crossSiteNetwork, wireGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`crossSiteNetwork` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`wireGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the wire group resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[WireGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroup)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetWireGroupRequest,WireGroup> getCallable()

Gets the specified wire group resource in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       GetWireGroupRequest request =
           GetWireGroupRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setProject("project-309310695")
               .setWireGroup("wireGroup-970399494")
               .build();
       ApiFuture<WireGroup> future = wireGroupsClient.getCallable().futureCall(request);
       // Do something.
       WireGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetWireGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetWireGroupRequest),[WireGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroup)>` |   
  
### getSettings()
    
    
    public final @Nullable WireGroupsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.WireGroupsSettings` |   
  
### getStub()
    
    
    public WireGroupsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[WireGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.WireGroupsStub)` |   
  
### insertAsync(InsertWireGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertWireGroupRequest request)

Creates a wire group in the specified project in the given scope using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       InsertWireGroupRequest request =
           InsertWireGroupRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setWireGroupResource(WireGroup.newBuilder().build())
               .build();
       Operation response = wireGroupsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertWireGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertWireGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String crossSiteNetwork, WireGroup wireGroupResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String crossSiteNetwork, WireGroup wireGroupResource)

Creates a wire group in the specified project in the given scope using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       String project = "project-309310695";
       String crossSiteNetwork = "crossSiteNetwork1009388679";
       WireGroup wireGroupResource = WireGroup.newBuilder().build();
       Operation response =
           wireGroupsClient.insertAsync(project, crossSiteNetwork, wireGroupResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`crossSiteNetwork` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`wireGroupResource` | `[WireGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroup)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertWireGroupRequest,Operation> insertCallable()

Creates a wire group in the specified project in the given scope using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       InsertWireGroupRequest request =
           InsertWireGroupRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setWireGroupResource(WireGroup.newBuilder().build())
               .build();
       ApiFuture<Operation> future = wireGroupsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertWireGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertWireGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertWireGroupRequest,Operation,Operation> insertOperationCallable()

Creates a wire group in the specified project in the given scope using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       InsertWireGroupRequest request =
           InsertWireGroupRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .setWireGroupResource(WireGroup.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           wireGroupsClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertWireGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertWireGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListWireGroupsRequest request)
    
    
    public final WireGroupsClient.ListPagedResponse list(ListWireGroupsRequest request)

Lists the wire groups for a project in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       ListWireGroupsRequest request =
           ListWireGroupsRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (WireGroup element : wireGroupsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListWireGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListWireGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WireGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupsClient.ListPagedResponse)` |   
  
### list(String project, String crossSiteNetwork)
    
    
    public final WireGroupsClient.ListPagedResponse list(String project, String crossSiteNetwork)

Lists the wire groups for a project in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       String project = "project-309310695";
       String crossSiteNetwork = "crossSiteNetwork1009388679";
       for (WireGroup element : wireGroupsClient.list(project, crossSiteNetwork).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`crossSiteNetwork` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WireGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListWireGroupsRequest,WireGroupList> listCallable()

Lists the wire groups for a project in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       ListWireGroupsRequest request =
           ListWireGroupsRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         WireGroupList response = wireGroupsClient.listCallable().call(request);
         for (WireGroup element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWireGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListWireGroupsRequest),[WireGroupList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListWireGroupsRequest,WireGroupsClient.ListPagedResponse> listPagedCallable()

Lists the wire groups for a project in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       ListWireGroupsRequest request =
           ListWireGroupsRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<WireGroup> future = wireGroupsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (WireGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWireGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListWireGroupsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroupsClient.ListPagedResponse)>` |   
  
### patchAsync(PatchWireGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchWireGroupRequest request)

Updates the specified wire group resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       PatchWireGroupRequest request =
           PatchWireGroupRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .setValidateOnly(true)
               .setWireGroup("wireGroup-970399494")
               .setWireGroupResource(WireGroup.newBuilder().build())
               .build();
       Operation response = wireGroupsClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchWireGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchWireGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String crossSiteNetwork, String wireGroup, WireGroup wireGroupResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String crossSiteNetwork, String wireGroup, WireGroup wireGroupResource)

Updates the specified wire group resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       String project = "project-309310695";
       String crossSiteNetwork = "crossSiteNetwork1009388679";
       String wireGroup = "wireGroup-970399494";
       WireGroup wireGroupResource = WireGroup.newBuilder().build();
       Operation response =
           wireGroupsClient
               .patchAsync(project, crossSiteNetwork, wireGroup, wireGroupResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`crossSiteNetwork` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`wireGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the WireGroups resource to patch.  
`wireGroupResource` | `[WireGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WireGroup)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchWireGroupRequest,Operation> patchCallable()

Updates the specified wire group resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       PatchWireGroupRequest request =
           PatchWireGroupRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .setValidateOnly(true)
               .setWireGroup("wireGroup-970399494")
               .setWireGroupResource(WireGroup.newBuilder().build())
               .build();
       ApiFuture<Operation> future = wireGroupsClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchWireGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchWireGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchWireGroupRequest,Operation,Operation> patchOperationCallable()

Updates the specified wire group resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (WireGroupsClient wireGroupsClient = WireGroupsClient.create()) {
       PatchWireGroupRequest request =
           PatchWireGroupRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .setValidateOnly(true)
               .setWireGroup("wireGroup-970399494")
               .setWireGroupResource(WireGroup.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           wireGroupsClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchWireGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchWireGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
