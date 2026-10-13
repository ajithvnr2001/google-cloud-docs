---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CrossSiteNetworksClient
title: Class CrossSiteNetworksClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:07.467736+00:00
---

# Class CrossSiteNetworksClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CrossSiteNetworksClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CrossSiteNetworksClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/CrossSiteNetworksClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The CrossSiteNetworks API.

This client uses CrossSiteNetworks version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       String project = "project-309310695";
       String crossSiteNetwork = "crossSiteNetwork1009388679";
       CrossSiteNetwork response = crossSiteNetworksClient.get(project, crossSiteNetwork);
     }
     

Note: close() needs to be called on the CrossSiteNetworksClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified cross-site network in the given scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteCrossSiteNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String crossSiteNetwork) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified cross-site network in the given scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetCrossSiteNetworkRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String crossSiteNetwork) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a cross-site network in the specified project in the given scope using the parameters that are included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertCrossSiteNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, CrossSiteNetwork crossSiteNetworkResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists the cross-site networks for a project in the given scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListCrossSiteNetworksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Updates the specified cross-site network with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchCrossSiteNetworkRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String crossSiteNetwork, CrossSiteNetwork crossSiteNetworkResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CrossSiteNetworksSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CrossSiteNetworksSettings crossSiteNetworksSettings =
         CrossSiteNetworksSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CrossSiteNetworksClient crossSiteNetworksClient =
         CrossSiteNetworksClient.create(crossSiteNetworksSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CrossSiteNetworksSettings crossSiteNetworksSettings =
         CrossSiteNetworksSettings.newBuilder().setEndpoint(myEndpoint).build();
     CrossSiteNetworksClient crossSiteNetworksClient =
         CrossSiteNetworksClient.create(crossSiteNetworksSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CrossSiteNetworksClient

## Static Methods 

### create()
    
    
    public static final CrossSiteNetworksClient create()

Constructs an instance of CrossSiteNetworksClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CrossSiteNetworksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CrossSiteNetworksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CrossSiteNetworksSettings settings)
    
    
    public static final CrossSiteNetworksClient create(CrossSiteNetworksSettings settings)

Constructs an instance of CrossSiteNetworksClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CrossSiteNetworksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CrossSiteNetworksSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CrossSiteNetworksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CrossSiteNetworksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CrossSiteNetworksStub stub)
    
    
    public static final CrossSiteNetworksClient create(CrossSiteNetworksStub stub)

Constructs an instance of CrossSiteNetworksClient, using the given stub for making calls. This is for advanced usage - prefer using create(CrossSiteNetworksSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CrossSiteNetworksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.CrossSiteNetworksStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CrossSiteNetworksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CrossSiteNetworksClient)` |   
  
## Constructors 

### CrossSiteNetworksClient(CrossSiteNetworksSettings settings)
    
    
    protected CrossSiteNetworksClient(CrossSiteNetworksSettings settings)

Constructs an instance of CrossSiteNetworksClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CrossSiteNetworksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CrossSiteNetworksSettings)`  
  
  
### CrossSiteNetworksClient(CrossSiteNetworksStub stub)
    
    
    protected CrossSiteNetworksClient(CrossSiteNetworksStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CrossSiteNetworksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.CrossSiteNetworksStub)`  
  
  
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

### deleteAsync(DeleteCrossSiteNetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteCrossSiteNetworkRequest request)

Deletes the specified cross-site network in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       DeleteCrossSiteNetworkRequest request =
           DeleteCrossSiteNetworkRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = crossSiteNetworksClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCrossSiteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteCrossSiteNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String crossSiteNetwork)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String crossSiteNetwork)

Deletes the specified cross-site network in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       String project = "project-309310695";
       String crossSiteNetwork = "crossSiteNetwork1009388679";
       Operation response = crossSiteNetworksClient.deleteAsync(project, crossSiteNetwork).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`crossSiteNetwork` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the cross-site network to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteCrossSiteNetworkRequest,Operation> deleteCallable()

Deletes the specified cross-site network in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       DeleteCrossSiteNetworkRequest request =
           DeleteCrossSiteNetworkRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = crossSiteNetworksClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteCrossSiteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteCrossSiteNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteCrossSiteNetworkRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified cross-site network in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       DeleteCrossSiteNetworkRequest request =
           DeleteCrossSiteNetworkRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           crossSiteNetworksClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteCrossSiteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteCrossSiteNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetCrossSiteNetworkRequest request)
    
    
    public final CrossSiteNetwork get(GetCrossSiteNetworkRequest request)

Returns the specified cross-site network in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       GetCrossSiteNetworkRequest request =
           GetCrossSiteNetworkRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setProject("project-309310695")
               .build();
       CrossSiteNetwork response = crossSiteNetworksClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCrossSiteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetCrossSiteNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CrossSiteNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CrossSiteNetwork)` |   
  
### get(String project, String crossSiteNetwork)
    
    
    public final CrossSiteNetwork get(String project, String crossSiteNetwork)

Returns the specified cross-site network in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       String project = "project-309310695";
       String crossSiteNetwork = "crossSiteNetwork1009388679";
       CrossSiteNetwork response = crossSiteNetworksClient.get(project, crossSiteNetwork);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`crossSiteNetwork` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the cross-site network to return.  
**Returns**  
---  
**Type** | **Description**  
`[CrossSiteNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CrossSiteNetwork)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetCrossSiteNetworkRequest,CrossSiteNetwork> getCallable()

Returns the specified cross-site network in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       GetCrossSiteNetworkRequest request =
           GetCrossSiteNetworkRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setProject("project-309310695")
               .build();
       ApiFuture<CrossSiteNetwork> future =
           crossSiteNetworksClient.getCallable().futureCall(request);
       // Do something.
       CrossSiteNetwork response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCrossSiteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetCrossSiteNetworkRequest),[CrossSiteNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CrossSiteNetwork)>` |   
  
### getSettings()
    
    
    public final @Nullable CrossSiteNetworksSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.CrossSiteNetworksSettings` |   
  
### getStub()
    
    
    public CrossSiteNetworksStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CrossSiteNetworksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.CrossSiteNetworksStub)` |   
  
### insertAsync(InsertCrossSiteNetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertCrossSiteNetworkRequest request)

Creates a cross-site network in the specified project in the given scope using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       InsertCrossSiteNetworkRequest request =
           InsertCrossSiteNetworkRequest.newBuilder()
               .setCrossSiteNetworkResource(CrossSiteNetwork.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       Operation response = crossSiteNetworksClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertCrossSiteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertCrossSiteNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, CrossSiteNetwork crossSiteNetworkResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, CrossSiteNetwork crossSiteNetworkResource)

Creates a cross-site network in the specified project in the given scope using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       String project = "project-309310695";
       CrossSiteNetwork crossSiteNetworkResource = CrossSiteNetwork.newBuilder().build();
       Operation response =
           crossSiteNetworksClient.insertAsync(project, crossSiteNetworkResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`crossSiteNetworkResource` | `[CrossSiteNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CrossSiteNetwork)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertCrossSiteNetworkRequest,Operation> insertCallable()

Creates a cross-site network in the specified project in the given scope using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       InsertCrossSiteNetworkRequest request =
           InsertCrossSiteNetworkRequest.newBuilder()
               .setCrossSiteNetworkResource(CrossSiteNetwork.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = crossSiteNetworksClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertCrossSiteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertCrossSiteNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertCrossSiteNetworkRequest,Operation,Operation> insertOperationCallable()

Creates a cross-site network in the specified project in the given scope using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       InsertCrossSiteNetworkRequest request =
           InsertCrossSiteNetworkRequest.newBuilder()
               .setCrossSiteNetworkResource(CrossSiteNetwork.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<Operation, Operation> future =
           crossSiteNetworksClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertCrossSiteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertCrossSiteNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListCrossSiteNetworksRequest request)
    
    
    public final CrossSiteNetworksClient.ListPagedResponse list(ListCrossSiteNetworksRequest request)

Lists the cross-site networks for a project in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       ListCrossSiteNetworksRequest request =
           ListCrossSiteNetworksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (CrossSiteNetwork element : crossSiteNetworksClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCrossSiteNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListCrossSiteNetworksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CrossSiteNetworksClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CrossSiteNetworksClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final CrossSiteNetworksClient.ListPagedResponse list(String project)

Lists the cross-site networks for a project in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       String project = "project-309310695";
       for (CrossSiteNetwork element : crossSiteNetworksClient.list(project).iterateAll()) {
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
`[CrossSiteNetworksClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CrossSiteNetworksClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListCrossSiteNetworksRequest,CrossSiteNetworkList> listCallable()

Lists the cross-site networks for a project in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       ListCrossSiteNetworksRequest request =
           ListCrossSiteNetworksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         CrossSiteNetworkList response = crossSiteNetworksClient.listCallable().call(request);
         for (CrossSiteNetwork element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCrossSiteNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListCrossSiteNetworksRequest),[CrossSiteNetworkList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CrossSiteNetworkList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListCrossSiteNetworksRequest,CrossSiteNetworksClient.ListPagedResponse> listPagedCallable()

Lists the cross-site networks for a project in the given scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       ListCrossSiteNetworksRequest request =
           ListCrossSiteNetworksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<CrossSiteNetwork> future =
           crossSiteNetworksClient.listPagedCallable().futureCall(request);
       // Do something.
       for (CrossSiteNetwork element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCrossSiteNetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListCrossSiteNetworksRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CrossSiteNetworksClient.ListPagedResponse)>` |   
  
### patchAsync(PatchCrossSiteNetworkRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchCrossSiteNetworkRequest request)

Updates the specified cross-site network with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       PatchCrossSiteNetworkRequest request =
           PatchCrossSiteNetworkRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setCrossSiteNetworkResource(CrossSiteNetwork.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .setValidateOnly(true)
               .build();
       Operation response = crossSiteNetworksClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchCrossSiteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchCrossSiteNetworkRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String crossSiteNetwork, CrossSiteNetwork crossSiteNetworkResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String crossSiteNetwork, CrossSiteNetwork crossSiteNetworkResource)

Updates the specified cross-site network with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       String project = "project-309310695";
       String crossSiteNetwork = "crossSiteNetwork1009388679";
       CrossSiteNetwork crossSiteNetworkResource = CrossSiteNetwork.newBuilder().build();
       Operation response =
           crossSiteNetworksClient
               .patchAsync(project, crossSiteNetwork, crossSiteNetworkResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`crossSiteNetwork` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the cross-site network to update.  
`crossSiteNetworkResource` | `[CrossSiteNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CrossSiteNetwork)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchCrossSiteNetworkRequest,Operation> patchCallable()

Updates the specified cross-site network with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       PatchCrossSiteNetworkRequest request =
           PatchCrossSiteNetworkRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setCrossSiteNetworkResource(CrossSiteNetwork.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = crossSiteNetworksClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchCrossSiteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchCrossSiteNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchCrossSiteNetworkRequest,Operation,Operation> patchOperationCallable()

Updates the specified cross-site network with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CrossSiteNetworksClient crossSiteNetworksClient = CrossSiteNetworksClient.create()) {
       PatchCrossSiteNetworkRequest request =
           PatchCrossSiteNetworkRequest.newBuilder()
               .setCrossSiteNetwork("crossSiteNetwork1009388679")
               .setCrossSiteNetworkResource(CrossSiteNetwork.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .setValidateOnly(true)
               .build();
       OperationFuture<Operation, Operation> future =
           crossSiteNetworksClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchCrossSiteNetworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchCrossSiteNetworkRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
