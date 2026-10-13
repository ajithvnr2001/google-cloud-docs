---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpProxiesClient
title: Class RegionTargetHttpProxiesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:01.795705+00:00
---

# Class RegionTargetHttpProxiesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpProxiesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionTargetHttpProxiesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RegionTargetHttpProxiesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RegionTargetHttpProxies API.

This client uses RegionTargetHttpProxies version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetHttpProxy = "targetHttpProxy-1944074187";
       TargetHttpProxy response =
           regionTargetHttpProxiesClient.get(project, region, targetHttpProxy);
     }
     

Note: close() needs to be called on the RegionTargetHttpProxiesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified TargetHttpProxy resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRegionTargetHttpProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String targetHttpProxy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified TargetHttpProxy resource in the specified region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRegionTargetHttpProxyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String targetHttpProxy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a TargetHttpProxy resource in the specified project and region using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRegionTargetHttpProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, TargetHttpProxy targetHttpProxyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of TargetHttpProxy resources available to the specified project in the specified region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRegionTargetHttpProxiesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
SetUrlMap |  Changes the URL map for TargetHttpProxy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setUrlMapAsync(SetUrlMapRegionTargetHttpProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setUrlMapAsync(String project, String region, String targetHttpProxy, UrlMapReference urlMapReferenceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setUrlMapOperationCallable() 
  * setUrlMapCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionTargetHttpProxiesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionTargetHttpProxiesSettings regionTargetHttpProxiesSettings =
         RegionTargetHttpProxiesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create(regionTargetHttpProxiesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionTargetHttpProxiesSettings regionTargetHttpProxiesSettings =
         RegionTargetHttpProxiesSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create(regionTargetHttpProxiesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionTargetHttpProxiesClient

## Static Methods 

### create()
    
    
    public static final RegionTargetHttpProxiesClient create()

Constructs an instance of RegionTargetHttpProxiesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionTargetHttpProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpProxiesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionTargetHttpProxiesSettings settings)
    
    
    public static final RegionTargetHttpProxiesClient create(RegionTargetHttpProxiesSettings settings)

Constructs an instance of RegionTargetHttpProxiesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionTargetHttpProxiesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpProxiesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionTargetHttpProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpProxiesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionTargetHttpProxiesStub stub)
    
    
    public static final RegionTargetHttpProxiesClient create(RegionTargetHttpProxiesStub stub)

Constructs an instance of RegionTargetHttpProxiesClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionTargetHttpProxiesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionTargetHttpProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionTargetHttpProxiesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionTargetHttpProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpProxiesClient)` |   
  
## Constructors 

### RegionTargetHttpProxiesClient(RegionTargetHttpProxiesSettings settings)
    
    
    protected RegionTargetHttpProxiesClient(RegionTargetHttpProxiesSettings settings)

Constructs an instance of RegionTargetHttpProxiesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionTargetHttpProxiesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpProxiesSettings)`  
  
  
### RegionTargetHttpProxiesClient(RegionTargetHttpProxiesStub stub)
    
    
    protected RegionTargetHttpProxiesClient(RegionTargetHttpProxiesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionTargetHttpProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionTargetHttpProxiesStub)`  
  
  
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

### deleteAsync(DeleteRegionTargetHttpProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRegionTargetHttpProxyRequest request)

Deletes the specified TargetHttpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       DeleteRegionTargetHttpProxyRequest request =
           DeleteRegionTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .build();
       Operation response = regionTargetHttpProxiesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionTargetHttpProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String targetHttpProxy)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String targetHttpProxy)

Deletes the specified TargetHttpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetHttpProxy = "targetHttpProxy-1944074187";
       Operation response =
           regionTargetHttpProxiesClient.deleteAsync(project, region, targetHttpProxy).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetHttpProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpProxy resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRegionTargetHttpProxyRequest,Operation> deleteCallable()

Deletes the specified TargetHttpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       DeleteRegionTargetHttpProxyRequest request =
           DeleteRegionTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .build();
       ApiFuture<Operation> future =
           regionTargetHttpProxiesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionTargetHttpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRegionTargetHttpProxyRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified TargetHttpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       DeleteRegionTargetHttpProxyRequest request =
           DeleteRegionTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .build();
       OperationFuture<Operation, Operation> future =
           regionTargetHttpProxiesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRegionTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionTargetHttpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRegionTargetHttpProxyRequest request)
    
    
    public final TargetHttpProxy get(GetRegionTargetHttpProxyRequest request)

Returns the specified TargetHttpProxy resource in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       GetRegionTargetHttpProxyRequest request =
           GetRegionTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .build();
       TargetHttpProxy response = regionTargetHttpProxiesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegionTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionTargetHttpProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxy)` |   
  
### get(String project, String region, String targetHttpProxy)
    
    
    public final TargetHttpProxy get(String project, String region, String targetHttpProxy)

Returns the specified TargetHttpProxy resource in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetHttpProxy = "targetHttpProxy-1944074187";
       TargetHttpProxy response =
           regionTargetHttpProxiesClient.get(project, region, targetHttpProxy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetHttpProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpProxy resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxy)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRegionTargetHttpProxyRequest,TargetHttpProxy> getCallable()

Returns the specified TargetHttpProxy resource in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       GetRegionTargetHttpProxyRequest request =
           GetRegionTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .build();
       ApiFuture<TargetHttpProxy> future =
           regionTargetHttpProxiesClient.getCallable().futureCall(request);
       // Do something.
       TargetHttpProxy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegionTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionTargetHttpProxyRequest),[TargetHttpProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxy)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionTargetHttpProxiesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RegionTargetHttpProxiesSettings` |   
  
### getStub()
    
    
    public RegionTargetHttpProxiesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionTargetHttpProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionTargetHttpProxiesStub)` |   
  
### insertAsync(InsertRegionTargetHttpProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRegionTargetHttpProxyRequest request)

Creates a TargetHttpProxy resource in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       InsertRegionTargetHttpProxyRequest request =
           InsertRegionTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpProxyResource(TargetHttpProxy.newBuilder().build())
               .build();
       Operation response = regionTargetHttpProxiesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRegionTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionTargetHttpProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, TargetHttpProxy targetHttpProxyResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, TargetHttpProxy targetHttpProxyResource)

Creates a TargetHttpProxy resource in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       TargetHttpProxy targetHttpProxyResource = TargetHttpProxy.newBuilder().build();
       Operation response =
           regionTargetHttpProxiesClient.insertAsync(project, region, targetHttpProxyResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetHttpProxyResource` | `[TargetHttpProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRegionTargetHttpProxyRequest,Operation> insertCallable()

Creates a TargetHttpProxy resource in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       InsertRegionTargetHttpProxyRequest request =
           InsertRegionTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpProxyResource(TargetHttpProxy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           regionTargetHttpProxiesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionTargetHttpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRegionTargetHttpProxyRequest,Operation,Operation> insertOperationCallable()

Creates a TargetHttpProxy resource in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       InsertRegionTargetHttpProxyRequest request =
           InsertRegionTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpProxyResource(TargetHttpProxy.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           regionTargetHttpProxiesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRegionTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionTargetHttpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRegionTargetHttpProxiesRequest request)
    
    
    public final RegionTargetHttpProxiesClient.ListPagedResponse list(ListRegionTargetHttpProxiesRequest request)

Retrieves the list of TargetHttpProxy resources available to the specified project in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       ListRegionTargetHttpProxiesRequest request =
           ListRegionTargetHttpProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (TargetHttpProxy element : regionTargetHttpProxiesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionTargetHttpProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionTargetHttpProxiesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionTargetHttpProxiesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpProxiesClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final RegionTargetHttpProxiesClient.ListPagedResponse list(String project, String region)

Retrieves the list of TargetHttpProxy resources available to the specified project in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (TargetHttpProxy element :
           regionTargetHttpProxiesClient.list(project, region).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
**Returns**  
---  
**Type** | **Description**  
`[RegionTargetHttpProxiesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpProxiesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRegionTargetHttpProxiesRequest,TargetHttpProxyList> listCallable()

Retrieves the list of TargetHttpProxy resources available to the specified project in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       ListRegionTargetHttpProxiesRequest request =
           ListRegionTargetHttpProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         TargetHttpProxyList response = regionTargetHttpProxiesClient.listCallable().call(request);
         for (TargetHttpProxy element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionTargetHttpProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionTargetHttpProxiesRequest),[TargetHttpProxyList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxyList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRegionTargetHttpProxiesRequest,RegionTargetHttpProxiesClient.ListPagedResponse> listPagedCallable()

Retrieves the list of TargetHttpProxy resources available to the specified project in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       ListRegionTargetHttpProxiesRequest request =
           ListRegionTargetHttpProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<TargetHttpProxy> future =
           regionTargetHttpProxiesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (TargetHttpProxy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionTargetHttpProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionTargetHttpProxiesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpProxiesClient.ListPagedResponse)>` |   
  
### setUrlMapAsync(SetUrlMapRegionTargetHttpProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> setUrlMapAsync(SetUrlMapRegionTargetHttpProxyRequest request)

Changes the URL map for TargetHttpProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       SetUrlMapRegionTargetHttpProxyRequest request =
           SetUrlMapRegionTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .setUrlMapReferenceResource(UrlMapReference.newBuilder().build())
               .build();
       Operation response = regionTargetHttpProxiesClient.setUrlMapAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetUrlMapRegionTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUrlMapRegionTargetHttpProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUrlMapAsync(String project, String region, String targetHttpProxy, UrlMapReference urlMapReferenceResource)
    
    
    public final OperationFuture<Operation,Operation> setUrlMapAsync(String project, String region, String targetHttpProxy, UrlMapReference urlMapReferenceResource)

Changes the URL map for TargetHttpProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetHttpProxy = "targetHttpProxy-1944074187";
       UrlMapReference urlMapReferenceResource = UrlMapReference.newBuilder().build();
       Operation response =
           regionTargetHttpProxiesClient
               .setUrlMapAsync(project, region, targetHttpProxy, urlMapReferenceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetHttpProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpProxy to set a URL map for.  
`urlMapReferenceResource` | `[UrlMapReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapReference)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUrlMapCallable()
    
    
    public final UnaryCallable<SetUrlMapRegionTargetHttpProxyRequest,Operation> setUrlMapCallable()

Changes the URL map for TargetHttpProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       SetUrlMapRegionTargetHttpProxyRequest request =
           SetUrlMapRegionTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .setUrlMapReferenceResource(UrlMapReference.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           regionTargetHttpProxiesClient.setUrlMapCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetUrlMapRegionTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUrlMapRegionTargetHttpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUrlMapOperationCallable()
    
    
    public final OperationCallable<SetUrlMapRegionTargetHttpProxyRequest,Operation,Operation> setUrlMapOperationCallable()

Changes the URL map for TargetHttpProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpProxiesClient regionTargetHttpProxiesClient =
         RegionTargetHttpProxiesClient.create()) {
       SetUrlMapRegionTargetHttpProxyRequest request =
           SetUrlMapRegionTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .setUrlMapReferenceResource(UrlMapReference.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           regionTargetHttpProxiesClient.setUrlMapOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetUrlMapRegionTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUrlMapRegionTargetHttpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
