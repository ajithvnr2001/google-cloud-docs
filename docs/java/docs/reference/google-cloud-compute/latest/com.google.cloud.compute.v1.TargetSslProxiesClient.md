---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxiesClient
title: Class TargetSslProxiesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:40.526746+00:00
---

# Class TargetSslProxiesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxiesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TargetSslProxiesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/TargetSslProxiesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The TargetSslProxies API.

This client uses TargetSslProxies version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       String project = "project-309310695";
       String targetSslProxy = "targetSslProxy-879314829";
       TargetSslProxy response = targetSslProxiesClient.get(project, targetSslProxy);
     }
     

Note: close() needs to be called on the TargetSslProxiesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified TargetSslProxy resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteTargetSslProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String targetSslProxy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified TargetSslProxy resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetTargetSslProxyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String targetSslProxy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a TargetSslProxy resource in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertTargetSslProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, TargetSslProxy targetSslProxyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of TargetSslProxy resources available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListTargetSslProxiesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
SetBackendService |  Changes the BackendService for TargetSslProxy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setBackendServiceAsync(SetBackendServiceTargetSslProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setBackendServiceAsync(String project, String targetSslProxy, TargetSslProxiesSetBackendServiceRequest targetSslProxiesSetBackendServiceRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setBackendServiceOperationCallable() 
  * setBackendServiceCallable() 

  
SetCertificateMap |  Changes the Certificate Map for TargetSslProxy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setCertificateMapAsync(SetCertificateMapTargetSslProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setCertificateMapAsync(String project, String targetSslProxy, TargetSslProxiesSetCertificateMapRequest targetSslProxiesSetCertificateMapRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setCertificateMapOperationCallable() 
  * setCertificateMapCallable() 

  
SetProxyHeader |  Changes the ProxyHeaderType for TargetSslProxy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setProxyHeaderAsync(SetProxyHeaderTargetSslProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setProxyHeaderAsync(String project, String targetSslProxy, TargetSslProxiesSetProxyHeaderRequest targetSslProxiesSetProxyHeaderRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setProxyHeaderOperationCallable() 
  * setProxyHeaderCallable() 

  
SetSslCertificates |  Changes SslCertificates for TargetSslProxy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setSslCertificatesAsync(SetSslCertificatesTargetSslProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setSslCertificatesAsync(String project, String targetSslProxy, TargetSslProxiesSetSslCertificatesRequest targetSslProxiesSetSslCertificatesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setSslCertificatesOperationCallable() 
  * setSslCertificatesCallable() 

  
SetSslPolicy |  Sets the SSL policy for TargetSslProxy. The SSL policy specifies the server-side support for SSL features. This affects connections between clients and the load balancer. They do not affect the connection between the load balancer and the backends. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setSslPolicyAsync(SetSslPolicyTargetSslProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setSslPolicyAsync(String project, String targetSslProxy, SslPolicyReference sslPolicyReferenceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setSslPolicyOperationCallable() 
  * setSslPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsTargetSslProxyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of TargetSslProxiesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TargetSslProxiesSettings targetSslProxiesSettings =
         TargetSslProxiesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     TargetSslProxiesClient targetSslProxiesClient =
         TargetSslProxiesClient.create(targetSslProxiesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TargetSslProxiesSettings targetSslProxiesSettings =
         TargetSslProxiesSettings.newBuilder().setEndpoint(myEndpoint).build();
     TargetSslProxiesClient targetSslProxiesClient =
         TargetSslProxiesClient.create(targetSslProxiesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TargetSslProxiesClient

## Static Methods 

### create()
    
    
    public static final TargetSslProxiesClient create()

Constructs an instance of TargetSslProxiesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[TargetSslProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxiesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TargetSslProxiesSettings settings)
    
    
    public static final TargetSslProxiesClient create(TargetSslProxiesSettings settings)

Constructs an instance of TargetSslProxiesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TargetSslProxiesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxiesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TargetSslProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxiesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TargetSslProxiesStub stub)
    
    
    public static final TargetSslProxiesClient create(TargetSslProxiesStub stub)

Constructs an instance of TargetSslProxiesClient, using the given stub for making calls. This is for advanced usage - prefer using create(TargetSslProxiesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TargetSslProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.TargetSslProxiesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TargetSslProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxiesClient)` |   
  
## Constructors 

### TargetSslProxiesClient(TargetSslProxiesSettings settings)
    
    
    protected TargetSslProxiesClient(TargetSslProxiesSettings settings)

Constructs an instance of TargetSslProxiesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TargetSslProxiesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxiesSettings)`  
  
  
### TargetSslProxiesClient(TargetSslProxiesStub stub)
    
    
    protected TargetSslProxiesClient(TargetSslProxiesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TargetSslProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.TargetSslProxiesStub)`  
  
  
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

### deleteAsync(DeleteTargetSslProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteTargetSslProxyRequest request)

Deletes the specified TargetSslProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       DeleteTargetSslProxyRequest request =
           DeleteTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       Operation response = targetSslProxiesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteTargetSslProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String targetSslProxy)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String targetSslProxy)

Deletes the specified TargetSslProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       String project = "project-309310695";
       String targetSslProxy = "targetSslProxy-879314829";
       Operation response = targetSslProxiesClient.deleteAsync(project, targetSslProxy).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetSslProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetSslProxy resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteTargetSslProxyRequest,Operation> deleteCallable()

Deletes the specified TargetSslProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       DeleteTargetSslProxyRequest request =
           DeleteTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       ApiFuture<Operation> future = targetSslProxiesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteTargetSslProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteTargetSslProxyRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified TargetSslProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       DeleteTargetSslProxyRequest request =
           DeleteTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       OperationFuture<Operation, Operation> future =
           targetSslProxiesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteTargetSslProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetTargetSslProxyRequest request)
    
    
    public final TargetSslProxy get(GetTargetSslProxyRequest request)

Returns the specified TargetSslProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       GetTargetSslProxyRequest request =
           GetTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       TargetSslProxy response = targetSslProxiesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetTargetSslProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetSslProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxy)` |   
  
### get(String project, String targetSslProxy)
    
    
    public final TargetSslProxy get(String project, String targetSslProxy)

Returns the specified TargetSslProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       String project = "project-309310695";
       String targetSslProxy = "targetSslProxy-879314829";
       TargetSslProxy response = targetSslProxiesClient.get(project, targetSslProxy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetSslProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetSslProxy resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[TargetSslProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxy)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetTargetSslProxyRequest,TargetSslProxy> getCallable()

Returns the specified TargetSslProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       GetTargetSslProxyRequest request =
           GetTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       ApiFuture<TargetSslProxy> future = targetSslProxiesClient.getCallable().futureCall(request);
       // Do something.
       TargetSslProxy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetTargetSslProxyRequest),[TargetSslProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxy)>` |   
  
### getSettings()
    
    
    public final @Nullable TargetSslProxiesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.TargetSslProxiesSettings` |   
  
### getStub()
    
    
    public TargetSslProxiesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[TargetSslProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.TargetSslProxiesStub)` |   
  
### insertAsync(InsertTargetSslProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertTargetSslProxyRequest request)

Creates a TargetSslProxy resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       InsertTargetSslProxyRequest request =
           InsertTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxyResource(TargetSslProxy.newBuilder().build())
               .build();
       Operation response = targetSslProxiesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertTargetSslProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, TargetSslProxy targetSslProxyResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, TargetSslProxy targetSslProxyResource)

Creates a TargetSslProxy resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       String project = "project-309310695";
       TargetSslProxy targetSslProxyResource = TargetSslProxy.newBuilder().build();
       Operation response =
           targetSslProxiesClient.insertAsync(project, targetSslProxyResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetSslProxyResource` | `[TargetSslProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertTargetSslProxyRequest,Operation> insertCallable()

Creates a TargetSslProxy resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       InsertTargetSslProxyRequest request =
           InsertTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxyResource(TargetSslProxy.newBuilder().build())
               .build();
       ApiFuture<Operation> future = targetSslProxiesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertTargetSslProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertTargetSslProxyRequest,Operation,Operation> insertOperationCallable()

Creates a TargetSslProxy resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       InsertTargetSslProxyRequest request =
           InsertTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxyResource(TargetSslProxy.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           targetSslProxiesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertTargetSslProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListTargetSslProxiesRequest request)
    
    
    public final TargetSslProxiesClient.ListPagedResponse list(ListTargetSslProxiesRequest request)

Retrieves the list of TargetSslProxy resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       ListTargetSslProxiesRequest request =
           ListTargetSslProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (TargetSslProxy element : targetSslProxiesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTargetSslProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListTargetSslProxiesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetSslProxiesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxiesClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final TargetSslProxiesClient.ListPagedResponse list(String project)

Retrieves the list of TargetSslProxy resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       String project = "project-309310695";
       for (TargetSslProxy element : targetSslProxiesClient.list(project).iterateAll()) {
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
`[TargetSslProxiesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxiesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListTargetSslProxiesRequest,TargetSslProxyList> listCallable()

Retrieves the list of TargetSslProxy resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       ListTargetSslProxiesRequest request =
           ListTargetSslProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         TargetSslProxyList response = targetSslProxiesClient.listCallable().call(request);
         for (TargetSslProxy element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTargetSslProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListTargetSslProxiesRequest),[TargetSslProxyList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxyList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListTargetSslProxiesRequest,TargetSslProxiesClient.ListPagedResponse> listPagedCallable()

Retrieves the list of TargetSslProxy resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       ListTargetSslProxiesRequest request =
           ListTargetSslProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<TargetSslProxy> future =
           targetSslProxiesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (TargetSslProxy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTargetSslProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListTargetSslProxiesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxiesClient.ListPagedResponse)>` |   
  
### setBackendServiceAsync(SetBackendServiceTargetSslProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> setBackendServiceAsync(SetBackendServiceTargetSslProxyRequest request)

Changes the BackendService for TargetSslProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       SetBackendServiceTargetSslProxyRequest request =
           SetBackendServiceTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxiesSetBackendServiceRequestResource(
                   TargetSslProxiesSetBackendServiceRequest.newBuilder().build())
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       Operation response = targetSslProxiesClient.setBackendServiceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetBackendServiceTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetBackendServiceTargetSslProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setBackendServiceAsync(String project, String targetSslProxy, TargetSslProxiesSetBackendServiceRequest targetSslProxiesSetBackendServiceRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setBackendServiceAsync(String project, String targetSslProxy, TargetSslProxiesSetBackendServiceRequest targetSslProxiesSetBackendServiceRequestResource)

Changes the BackendService for TargetSslProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       String project = "project-309310695";
       String targetSslProxy = "targetSslProxy-879314829";
       TargetSslProxiesSetBackendServiceRequest targetSslProxiesSetBackendServiceRequestResource =
           TargetSslProxiesSetBackendServiceRequest.newBuilder().build();
       Operation response =
           targetSslProxiesClient
               .setBackendServiceAsync(
                   project, targetSslProxy, targetSslProxiesSetBackendServiceRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetSslProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetSslProxy resource whose BackendService resource is to be set.  
`targetSslProxiesSetBackendServiceRequestResource` | `[TargetSslProxiesSetBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxiesSetBackendServiceRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setBackendServiceCallable()
    
    
    public final UnaryCallable<SetBackendServiceTargetSslProxyRequest,Operation> setBackendServiceCallable()

Changes the BackendService for TargetSslProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       SetBackendServiceTargetSslProxyRequest request =
           SetBackendServiceTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxiesSetBackendServiceRequestResource(
                   TargetSslProxiesSetBackendServiceRequest.newBuilder().build())
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       ApiFuture<Operation> future =
           targetSslProxiesClient.setBackendServiceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetBackendServiceTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetBackendServiceTargetSslProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setBackendServiceOperationCallable()
    
    
    public final OperationCallable<SetBackendServiceTargetSslProxyRequest,Operation,Operation> setBackendServiceOperationCallable()

Changes the BackendService for TargetSslProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       SetBackendServiceTargetSslProxyRequest request =
           SetBackendServiceTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxiesSetBackendServiceRequestResource(
                   TargetSslProxiesSetBackendServiceRequest.newBuilder().build())
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       OperationFuture<Operation, Operation> future =
           targetSslProxiesClient.setBackendServiceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetBackendServiceTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetBackendServiceTargetSslProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setCertificateMapAsync(SetCertificateMapTargetSslProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> setCertificateMapAsync(SetCertificateMapTargetSslProxyRequest request)

Changes the Certificate Map for TargetSslProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       SetCertificateMapTargetSslProxyRequest request =
           SetCertificateMapTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxiesSetCertificateMapRequestResource(
                   TargetSslProxiesSetCertificateMapRequest.newBuilder().build())
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       Operation response = targetSslProxiesClient.setCertificateMapAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetCertificateMapTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetCertificateMapTargetSslProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setCertificateMapAsync(String project, String targetSslProxy, TargetSslProxiesSetCertificateMapRequest targetSslProxiesSetCertificateMapRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setCertificateMapAsync(String project, String targetSslProxy, TargetSslProxiesSetCertificateMapRequest targetSslProxiesSetCertificateMapRequestResource)

Changes the Certificate Map for TargetSslProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       String project = "project-309310695";
       String targetSslProxy = "targetSslProxy-879314829";
       TargetSslProxiesSetCertificateMapRequest targetSslProxiesSetCertificateMapRequestResource =
           TargetSslProxiesSetCertificateMapRequest.newBuilder().build();
       Operation response =
           targetSslProxiesClient
               .setCertificateMapAsync(
                   project, targetSslProxy, targetSslProxiesSetCertificateMapRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetSslProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetSslProxy resource whose CertificateMap is to be set. The name must be 1-63 characters long, and comply with RFC1035.  
`targetSslProxiesSetCertificateMapRequestResource` | `[TargetSslProxiesSetCertificateMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxiesSetCertificateMapRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setCertificateMapCallable()
    
    
    public final UnaryCallable<SetCertificateMapTargetSslProxyRequest,Operation> setCertificateMapCallable()

Changes the Certificate Map for TargetSslProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       SetCertificateMapTargetSslProxyRequest request =
           SetCertificateMapTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxiesSetCertificateMapRequestResource(
                   TargetSslProxiesSetCertificateMapRequest.newBuilder().build())
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       ApiFuture<Operation> future =
           targetSslProxiesClient.setCertificateMapCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetCertificateMapTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetCertificateMapTargetSslProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setCertificateMapOperationCallable()
    
    
    public final OperationCallable<SetCertificateMapTargetSslProxyRequest,Operation,Operation> setCertificateMapOperationCallable()

Changes the Certificate Map for TargetSslProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       SetCertificateMapTargetSslProxyRequest request =
           SetCertificateMapTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxiesSetCertificateMapRequestResource(
                   TargetSslProxiesSetCertificateMapRequest.newBuilder().build())
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       OperationFuture<Operation, Operation> future =
           targetSslProxiesClient.setCertificateMapOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetCertificateMapTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetCertificateMapTargetSslProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setProxyHeaderAsync(SetProxyHeaderTargetSslProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> setProxyHeaderAsync(SetProxyHeaderTargetSslProxyRequest request)

Changes the ProxyHeaderType for TargetSslProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       SetProxyHeaderTargetSslProxyRequest request =
           SetProxyHeaderTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxiesSetProxyHeaderRequestResource(
                   TargetSslProxiesSetProxyHeaderRequest.newBuilder().build())
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       Operation response = targetSslProxiesClient.setProxyHeaderAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetProxyHeaderTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetProxyHeaderTargetSslProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setProxyHeaderAsync(String project, String targetSslProxy, TargetSslProxiesSetProxyHeaderRequest targetSslProxiesSetProxyHeaderRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setProxyHeaderAsync(String project, String targetSslProxy, TargetSslProxiesSetProxyHeaderRequest targetSslProxiesSetProxyHeaderRequestResource)

Changes the ProxyHeaderType for TargetSslProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       String project = "project-309310695";
       String targetSslProxy = "targetSslProxy-879314829";
       TargetSslProxiesSetProxyHeaderRequest targetSslProxiesSetProxyHeaderRequestResource =
           TargetSslProxiesSetProxyHeaderRequest.newBuilder().build();
       Operation response =
           targetSslProxiesClient
               .setProxyHeaderAsync(
                   project, targetSslProxy, targetSslProxiesSetProxyHeaderRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetSslProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetSslProxy resource whose ProxyHeader is to be set.  
`targetSslProxiesSetProxyHeaderRequestResource` | `[TargetSslProxiesSetProxyHeaderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxiesSetProxyHeaderRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setProxyHeaderCallable()
    
    
    public final UnaryCallable<SetProxyHeaderTargetSslProxyRequest,Operation> setProxyHeaderCallable()

Changes the ProxyHeaderType for TargetSslProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       SetProxyHeaderTargetSslProxyRequest request =
           SetProxyHeaderTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxiesSetProxyHeaderRequestResource(
                   TargetSslProxiesSetProxyHeaderRequest.newBuilder().build())
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       ApiFuture<Operation> future =
           targetSslProxiesClient.setProxyHeaderCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetProxyHeaderTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetProxyHeaderTargetSslProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setProxyHeaderOperationCallable()
    
    
    public final OperationCallable<SetProxyHeaderTargetSslProxyRequest,Operation,Operation> setProxyHeaderOperationCallable()

Changes the ProxyHeaderType for TargetSslProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       SetProxyHeaderTargetSslProxyRequest request =
           SetProxyHeaderTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxiesSetProxyHeaderRequestResource(
                   TargetSslProxiesSetProxyHeaderRequest.newBuilder().build())
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       OperationFuture<Operation, Operation> future =
           targetSslProxiesClient.setProxyHeaderOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetProxyHeaderTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetProxyHeaderTargetSslProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslCertificatesAsync(SetSslCertificatesTargetSslProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> setSslCertificatesAsync(SetSslCertificatesTargetSslProxyRequest request)

Changes SslCertificates for TargetSslProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       SetSslCertificatesTargetSslProxyRequest request =
           SetSslCertificatesTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxiesSetSslCertificatesRequestResource(
                   TargetSslProxiesSetSslCertificatesRequest.newBuilder().build())
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       Operation response = targetSslProxiesClient.setSslCertificatesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetSslCertificatesTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSslCertificatesTargetSslProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslCertificatesAsync(String project, String targetSslProxy, TargetSslProxiesSetSslCertificatesRequest targetSslProxiesSetSslCertificatesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setSslCertificatesAsync(String project, String targetSslProxy, TargetSslProxiesSetSslCertificatesRequest targetSslProxiesSetSslCertificatesRequestResource)

Changes SslCertificates for TargetSslProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       String project = "project-309310695";
       String targetSslProxy = "targetSslProxy-879314829";
       TargetSslProxiesSetSslCertificatesRequest targetSslProxiesSetSslCertificatesRequestResource =
           TargetSslProxiesSetSslCertificatesRequest.newBuilder().build();
       Operation response =
           targetSslProxiesClient
               .setSslCertificatesAsync(
                   project, targetSslProxy, targetSslProxiesSetSslCertificatesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetSslProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetSslProxy resource whose SslCertificate resource is to be set.  
`targetSslProxiesSetSslCertificatesRequestResource` | `[TargetSslProxiesSetSslCertificatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetSslProxiesSetSslCertificatesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslCertificatesCallable()
    
    
    public final UnaryCallable<SetSslCertificatesTargetSslProxyRequest,Operation> setSslCertificatesCallable()

Changes SslCertificates for TargetSslProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       SetSslCertificatesTargetSslProxyRequest request =
           SetSslCertificatesTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxiesSetSslCertificatesRequestResource(
                   TargetSslProxiesSetSslCertificatesRequest.newBuilder().build())
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       ApiFuture<Operation> future =
           targetSslProxiesClient.setSslCertificatesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetSslCertificatesTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSslCertificatesTargetSslProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslCertificatesOperationCallable()
    
    
    public final OperationCallable<SetSslCertificatesTargetSslProxyRequest,Operation,Operation> setSslCertificatesOperationCallable()

Changes SslCertificates for TargetSslProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       SetSslCertificatesTargetSslProxyRequest request =
           SetSslCertificatesTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetSslProxiesSetSslCertificatesRequestResource(
                   TargetSslProxiesSetSslCertificatesRequest.newBuilder().build())
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       OperationFuture<Operation, Operation> future =
           targetSslProxiesClient.setSslCertificatesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetSslCertificatesTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSslCertificatesTargetSslProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslPolicyAsync(SetSslPolicyTargetSslProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> setSslPolicyAsync(SetSslPolicyTargetSslProxyRequest request)

Sets the SSL policy for TargetSslProxy. The SSL policy specifies the server-side support for SSL features. This affects connections between clients and the load balancer. They do not affect the connection between the load balancer and the backends.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       SetSslPolicyTargetSslProxyRequest request =
           SetSslPolicyTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSslPolicyReferenceResource(SslPolicyReference.newBuilder().build())
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       Operation response = targetSslProxiesClient.setSslPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetSslPolicyTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSslPolicyTargetSslProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslPolicyAsync(String project, String targetSslProxy, SslPolicyReference sslPolicyReferenceResource)
    
    
    public final OperationFuture<Operation,Operation> setSslPolicyAsync(String project, String targetSslProxy, SslPolicyReference sslPolicyReferenceResource)

Sets the SSL policy for TargetSslProxy. The SSL policy specifies the server-side support for SSL features. This affects connections between clients and the load balancer. They do not affect the connection between the load balancer and the backends.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       String project = "project-309310695";
       String targetSslProxy = "targetSslProxy-879314829";
       SslPolicyReference sslPolicyReferenceResource = SslPolicyReference.newBuilder().build();
       Operation response =
           targetSslProxiesClient
               .setSslPolicyAsync(project, targetSslProxy, sslPolicyReferenceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetSslProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetSslProxy resource whose SSL policy is to be set. The name must be 1-63 characters long, and comply with RFC1035.  
`sslPolicyReferenceResource` | `[SslPolicyReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslPolicyReference)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslPolicyCallable()
    
    
    public final UnaryCallable<SetSslPolicyTargetSslProxyRequest,Operation> setSslPolicyCallable()

Sets the SSL policy for TargetSslProxy. The SSL policy specifies the server-side support for SSL features. This affects connections between clients and the load balancer. They do not affect the connection between the load balancer and the backends.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       SetSslPolicyTargetSslProxyRequest request =
           SetSslPolicyTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSslPolicyReferenceResource(SslPolicyReference.newBuilder().build())
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       ApiFuture<Operation> future =
           targetSslProxiesClient.setSslPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetSslPolicyTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSslPolicyTargetSslProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslPolicyOperationCallable()
    
    
    public final OperationCallable<SetSslPolicyTargetSslProxyRequest,Operation,Operation> setSslPolicyOperationCallable()

Sets the SSL policy for TargetSslProxy. The SSL policy specifies the server-side support for SSL features. This affects connections between clients and the load balancer. They do not affect the connection between the load balancer and the backends.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       SetSslPolicyTargetSslProxyRequest request =
           SetSslPolicyTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSslPolicyReferenceResource(SslPolicyReference.newBuilder().build())
               .setTargetSslProxy("targetSslProxy-879314829")
               .build();
       OperationFuture<Operation, Operation> future =
           targetSslProxiesClient.setSslPolicyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetSslPolicyTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSslPolicyTargetSslProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsTargetSslProxyRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsTargetSslProxyRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       TestIamPermissionsTargetSslProxyRequest request =
           TestIamPermissionsTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = targetSslProxiesClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsTargetSslProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource)
    
    
    public final TestPermissionsResponse testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           targetSslProxiesClient.testIamPermissions(
               project, resource, testPermissionsRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsTargetSslProxyRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetSslProxiesClient targetSslProxiesClient = TargetSslProxiesClient.create()) {
       TestIamPermissionsTargetSslProxyRequest request =
           TestIamPermissionsTargetSslProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           targetSslProxiesClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsTargetSslProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsTargetSslProxyRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
