---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpsProxiesClient
title: Class RegionTargetHttpsProxiesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:02.936115+00:00
---

# Class RegionTargetHttpsProxiesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpsProxiesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionTargetHttpsProxiesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RegionTargetHttpsProxiesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RegionTargetHttpsProxies API.

This client uses RegionTargetHttpsProxies version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetHttpsProxy = "targetHttpsProxy833943732";
       TargetHttpsProxy response =
           regionTargetHttpsProxiesClient.get(project, region, targetHttpsProxy);
     }
     

Note: close() needs to be called on the RegionTargetHttpsProxiesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified TargetHttpsProxy resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRegionTargetHttpsProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String targetHttpsProxy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified TargetHttpsProxy resource in the specified region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRegionTargetHttpsProxyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String targetHttpsProxy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a TargetHttpsProxy resource in the specified project and region using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRegionTargetHttpsProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, TargetHttpsProxy targetHttpsProxyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of TargetHttpsProxy resources available to the specified project in the specified region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRegionTargetHttpsProxiesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Patches the specified regional TargetHttpsProxy resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchRegionTargetHttpsProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String region, String targetHttpsProxy, TargetHttpsProxy targetHttpsProxyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
SetSslCertificates |  Replaces SslCertificates for TargetHttpsProxy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setSslCertificatesAsync(SetSslCertificatesRegionTargetHttpsProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setSslCertificatesAsync(String project, String region, String targetHttpsProxy, RegionTargetHttpsProxiesSetSslCertificatesRequest regionTargetHttpsProxiesSetSslCertificatesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setSslCertificatesOperationCallable() 
  * setSslCertificatesCallable() 

  
SetUrlMap |  Changes the URL map for TargetHttpsProxy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setUrlMapAsync(SetUrlMapRegionTargetHttpsProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setUrlMapAsync(String project, String region, String targetHttpsProxy, UrlMapReference urlMapReferenceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setUrlMapOperationCallable() 
  * setUrlMapCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionTargetHttpsProxiesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionTargetHttpsProxiesSettings regionTargetHttpsProxiesSettings =
         RegionTargetHttpsProxiesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create(regionTargetHttpsProxiesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionTargetHttpsProxiesSettings regionTargetHttpsProxiesSettings =
         RegionTargetHttpsProxiesSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create(regionTargetHttpsProxiesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionTargetHttpsProxiesClient

## Static Methods 

### create()
    
    
    public static final RegionTargetHttpsProxiesClient create()

Constructs an instance of RegionTargetHttpsProxiesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionTargetHttpsProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpsProxiesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionTargetHttpsProxiesSettings settings)
    
    
    public static final RegionTargetHttpsProxiesClient create(RegionTargetHttpsProxiesSettings settings)

Constructs an instance of RegionTargetHttpsProxiesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionTargetHttpsProxiesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpsProxiesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionTargetHttpsProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpsProxiesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionTargetHttpsProxiesStub stub)
    
    
    public static final RegionTargetHttpsProxiesClient create(RegionTargetHttpsProxiesStub stub)

Constructs an instance of RegionTargetHttpsProxiesClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionTargetHttpsProxiesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionTargetHttpsProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionTargetHttpsProxiesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionTargetHttpsProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpsProxiesClient)` |   
  
## Constructors 

### RegionTargetHttpsProxiesClient(RegionTargetHttpsProxiesSettings settings)
    
    
    protected RegionTargetHttpsProxiesClient(RegionTargetHttpsProxiesSettings settings)

Constructs an instance of RegionTargetHttpsProxiesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionTargetHttpsProxiesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpsProxiesSettings)`  
  
  
### RegionTargetHttpsProxiesClient(RegionTargetHttpsProxiesStub stub)
    
    
    protected RegionTargetHttpsProxiesClient(RegionTargetHttpsProxiesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionTargetHttpsProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionTargetHttpsProxiesStub)`  
  
  
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

### deleteAsync(DeleteRegionTargetHttpsProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRegionTargetHttpsProxyRequest request)

Deletes the specified TargetHttpsProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       DeleteRegionTargetHttpsProxyRequest request =
           DeleteRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       Operation response = regionTargetHttpsProxiesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionTargetHttpsProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String targetHttpsProxy)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String targetHttpsProxy)

Deletes the specified TargetHttpsProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetHttpsProxy = "targetHttpsProxy833943732";
       Operation response =
           regionTargetHttpsProxiesClient.deleteAsync(project, region, targetHttpsProxy).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetHttpsProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpsProxy resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRegionTargetHttpsProxyRequest,Operation> deleteCallable()

Deletes the specified TargetHttpsProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       DeleteRegionTargetHttpsProxyRequest request =
           DeleteRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       ApiFuture<Operation> future =
           regionTargetHttpsProxiesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRegionTargetHttpsProxyRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified TargetHttpsProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       DeleteRegionTargetHttpsProxyRequest request =
           DeleteRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       OperationFuture<Operation, Operation> future =
           regionTargetHttpsProxiesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRegionTargetHttpsProxyRequest request)
    
    
    public final TargetHttpsProxy get(GetRegionTargetHttpsProxyRequest request)

Returns the specified TargetHttpsProxy resource in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       GetRegionTargetHttpsProxyRequest request =
           GetRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       TargetHttpsProxy response = regionTargetHttpsProxiesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionTargetHttpsProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpsProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxy)` |   
  
### get(String project, String region, String targetHttpsProxy)
    
    
    public final TargetHttpsProxy get(String project, String region, String targetHttpsProxy)

Returns the specified TargetHttpsProxy resource in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetHttpsProxy = "targetHttpsProxy833943732";
       TargetHttpsProxy response =
           regionTargetHttpsProxiesClient.get(project, region, targetHttpsProxy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetHttpsProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpsProxy resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpsProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxy)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRegionTargetHttpsProxyRequest,TargetHttpsProxy> getCallable()

Returns the specified TargetHttpsProxy resource in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       GetRegionTargetHttpsProxyRequest request =
           GetRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       ApiFuture<TargetHttpsProxy> future =
           regionTargetHttpsProxiesClient.getCallable().futureCall(request);
       // Do something.
       TargetHttpsProxy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionTargetHttpsProxyRequest),[TargetHttpsProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxy)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionTargetHttpsProxiesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RegionTargetHttpsProxiesSettings` |   
  
### getStub()
    
    
    public RegionTargetHttpsProxiesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionTargetHttpsProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionTargetHttpsProxiesStub)` |   
  
### insertAsync(InsertRegionTargetHttpsProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRegionTargetHttpsProxyRequest request)

Creates a TargetHttpsProxy resource in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       InsertRegionTargetHttpsProxyRequest request =
           InsertRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxyResource(TargetHttpsProxy.newBuilder().build())
               .build();
       Operation response = regionTargetHttpsProxiesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionTargetHttpsProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, TargetHttpsProxy targetHttpsProxyResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, TargetHttpsProxy targetHttpsProxyResource)

Creates a TargetHttpsProxy resource in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       TargetHttpsProxy targetHttpsProxyResource = TargetHttpsProxy.newBuilder().build();
       Operation response =
           regionTargetHttpsProxiesClient
               .insertAsync(project, region, targetHttpsProxyResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetHttpsProxyResource` | `[TargetHttpsProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRegionTargetHttpsProxyRequest,Operation> insertCallable()

Creates a TargetHttpsProxy resource in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       InsertRegionTargetHttpsProxyRequest request =
           InsertRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxyResource(TargetHttpsProxy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           regionTargetHttpsProxiesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRegionTargetHttpsProxyRequest,Operation,Operation> insertOperationCallable()

Creates a TargetHttpsProxy resource in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       InsertRegionTargetHttpsProxyRequest request =
           InsertRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxyResource(TargetHttpsProxy.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           regionTargetHttpsProxiesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRegionTargetHttpsProxiesRequest request)
    
    
    public final RegionTargetHttpsProxiesClient.ListPagedResponse list(ListRegionTargetHttpsProxiesRequest request)

Retrieves the list of TargetHttpsProxy resources available to the specified project in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       ListRegionTargetHttpsProxiesRequest request =
           ListRegionTargetHttpsProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (TargetHttpsProxy element : regionTargetHttpsProxiesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionTargetHttpsProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionTargetHttpsProxiesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionTargetHttpsProxiesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpsProxiesClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final RegionTargetHttpsProxiesClient.ListPagedResponse list(String project, String region)

Retrieves the list of TargetHttpsProxy resources available to the specified project in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (TargetHttpsProxy element :
           regionTargetHttpsProxiesClient.list(project, region).iterateAll()) {
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
`[RegionTargetHttpsProxiesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpsProxiesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRegionTargetHttpsProxiesRequest,TargetHttpsProxyList> listCallable()

Retrieves the list of TargetHttpsProxy resources available to the specified project in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       ListRegionTargetHttpsProxiesRequest request =
           ListRegionTargetHttpsProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         TargetHttpsProxyList response = regionTargetHttpsProxiesClient.listCallable().call(request);
         for (TargetHttpsProxy element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionTargetHttpsProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionTargetHttpsProxiesRequest),[TargetHttpsProxyList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxyList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRegionTargetHttpsProxiesRequest,RegionTargetHttpsProxiesClient.ListPagedResponse> listPagedCallable()

Retrieves the list of TargetHttpsProxy resources available to the specified project in the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       ListRegionTargetHttpsProxiesRequest request =
           ListRegionTargetHttpsProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<TargetHttpsProxy> future =
           regionTargetHttpsProxiesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (TargetHttpsProxy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionTargetHttpsProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionTargetHttpsProxiesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpsProxiesClient.ListPagedResponse)>` |   
  
### patchAsync(PatchRegionTargetHttpsProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchRegionTargetHttpsProxyRequest request)

Patches the specified regional TargetHttpsProxy resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       PatchRegionTargetHttpsProxyRequest request =
           PatchRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .setTargetHttpsProxyResource(TargetHttpsProxy.newBuilder().build())
               .build();
       Operation response = regionTargetHttpsProxiesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionTargetHttpsProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String region, String targetHttpsProxy, TargetHttpsProxy targetHttpsProxyResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String region, String targetHttpsProxy, TargetHttpsProxy targetHttpsProxyResource)

Patches the specified regional TargetHttpsProxy resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetHttpsProxy = "targetHttpsProxy833943732";
       TargetHttpsProxy targetHttpsProxyResource = TargetHttpsProxy.newBuilder().build();
       Operation response =
           regionTargetHttpsProxiesClient
               .patchAsync(project, region, targetHttpsProxy, targetHttpsProxyResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`targetHttpsProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpsProxy resource to patch.  
`targetHttpsProxyResource` | `[TargetHttpsProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchRegionTargetHttpsProxyRequest,Operation> patchCallable()

Patches the specified regional TargetHttpsProxy resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       PatchRegionTargetHttpsProxyRequest request =
           PatchRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .setTargetHttpsProxyResource(TargetHttpsProxy.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           regionTargetHttpsProxiesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchRegionTargetHttpsProxyRequest,Operation,Operation> patchOperationCallable()

Patches the specified regional TargetHttpsProxy resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       PatchRegionTargetHttpsProxyRequest request =
           PatchRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .setTargetHttpsProxyResource(TargetHttpsProxy.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           regionTargetHttpsProxiesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslCertificatesAsync(SetSslCertificatesRegionTargetHttpsProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> setSslCertificatesAsync(SetSslCertificatesRegionTargetHttpsProxyRequest request)

Replaces SslCertificates for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       SetSslCertificatesRegionTargetHttpsProxyRequest request =
           SetSslCertificatesRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionTargetHttpsProxiesSetSslCertificatesRequestResource(
                   RegionTargetHttpsProxiesSetSslCertificatesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       Operation response = regionTargetHttpsProxiesClient.setSslCertificatesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetSslCertificatesRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSslCertificatesRegionTargetHttpsProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslCertificatesAsync(String project, String region, String targetHttpsProxy, RegionTargetHttpsProxiesSetSslCertificatesRequest regionTargetHttpsProxiesSetSslCertificatesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setSslCertificatesAsync(String project, String region, String targetHttpsProxy, RegionTargetHttpsProxiesSetSslCertificatesRequest regionTargetHttpsProxiesSetSslCertificatesRequestResource)

Replaces SslCertificates for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetHttpsProxy = "targetHttpsProxy833943732";
       RegionTargetHttpsProxiesSetSslCertificatesRequest
           regionTargetHttpsProxiesSetSslCertificatesRequestResource =
               RegionTargetHttpsProxiesSetSslCertificatesRequest.newBuilder().build();
       Operation response =
           regionTargetHttpsProxiesClient
               .setSslCertificatesAsync(
                   project,
                   region,
                   targetHttpsProxy,
                   regionTargetHttpsProxiesSetSslCertificatesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetHttpsProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpsProxy resource to set an SslCertificates resource for.  
`regionTargetHttpsProxiesSetSslCertificatesRequestResource` | `[RegionTargetHttpsProxiesSetSslCertificatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionTargetHttpsProxiesSetSslCertificatesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslCertificatesCallable()
    
    
    public final UnaryCallable<SetSslCertificatesRegionTargetHttpsProxyRequest,Operation> setSslCertificatesCallable()

Replaces SslCertificates for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       SetSslCertificatesRegionTargetHttpsProxyRequest request =
           SetSslCertificatesRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionTargetHttpsProxiesSetSslCertificatesRequestResource(
                   RegionTargetHttpsProxiesSetSslCertificatesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       ApiFuture<Operation> future =
           regionTargetHttpsProxiesClient.setSslCertificatesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetSslCertificatesRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSslCertificatesRegionTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslCertificatesOperationCallable()
    
    
    public final OperationCallable<SetSslCertificatesRegionTargetHttpsProxyRequest,Operation,Operation> setSslCertificatesOperationCallable()

Replaces SslCertificates for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       SetSslCertificatesRegionTargetHttpsProxyRequest request =
           SetSslCertificatesRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionTargetHttpsProxiesSetSslCertificatesRequestResource(
                   RegionTargetHttpsProxiesSetSslCertificatesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       OperationFuture<Operation, Operation> future =
           regionTargetHttpsProxiesClient.setSslCertificatesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetSslCertificatesRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSslCertificatesRegionTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUrlMapAsync(SetUrlMapRegionTargetHttpsProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> setUrlMapAsync(SetUrlMapRegionTargetHttpsProxyRequest request)

Changes the URL map for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       SetUrlMapRegionTargetHttpsProxyRequest request =
           SetUrlMapRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .setUrlMapReferenceResource(UrlMapReference.newBuilder().build())
               .build();
       Operation response = regionTargetHttpsProxiesClient.setUrlMapAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetUrlMapRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUrlMapRegionTargetHttpsProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUrlMapAsync(String project, String region, String targetHttpsProxy, UrlMapReference urlMapReferenceResource)
    
    
    public final OperationFuture<Operation,Operation> setUrlMapAsync(String project, String region, String targetHttpsProxy, UrlMapReference urlMapReferenceResource)

Changes the URL map for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String targetHttpsProxy = "targetHttpsProxy833943732";
       UrlMapReference urlMapReferenceResource = UrlMapReference.newBuilder().build();
       Operation response =
           regionTargetHttpsProxiesClient
               .setUrlMapAsync(project, region, targetHttpsProxy, urlMapReferenceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`targetHttpsProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpsProxy to set a URL map for.  
`urlMapReferenceResource` | `[UrlMapReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapReference)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUrlMapCallable()
    
    
    public final UnaryCallable<SetUrlMapRegionTargetHttpsProxyRequest,Operation> setUrlMapCallable()

Changes the URL map for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       SetUrlMapRegionTargetHttpsProxyRequest request =
           SetUrlMapRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .setUrlMapReferenceResource(UrlMapReference.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           regionTargetHttpsProxiesClient.setUrlMapCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetUrlMapRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUrlMapRegionTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUrlMapOperationCallable()
    
    
    public final OperationCallable<SetUrlMapRegionTargetHttpsProxyRequest,Operation,Operation> setUrlMapOperationCallable()

Changes the URL map for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionTargetHttpsProxiesClient regionTargetHttpsProxiesClient =
         RegionTargetHttpsProxiesClient.create()) {
       SetUrlMapRegionTargetHttpsProxyRequest request =
           SetUrlMapRegionTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .setUrlMapReferenceResource(UrlMapReference.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           regionTargetHttpsProxiesClient.setUrlMapOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetUrlMapRegionTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUrlMapRegionTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
