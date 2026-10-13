---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxiesClient
title: Class TargetHttpsProxiesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:36.126931+00:00
---

# Class TargetHttpsProxiesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxiesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TargetHttpsProxiesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/TargetHttpsProxiesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The TargetHttpsProxies API.

This client uses TargetHttpsProxies version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String targetHttpsProxy = "targetHttpsProxy833943732";
       TargetHttpsProxy response = targetHttpsProxiesClient.get(project, targetHttpsProxy);
     }
     

Note: close() needs to be called on the TargetHttpsProxiesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves the list of all TargetHttpsProxy resources, regional and global, available to the specified project.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListTargetHttpsProxiesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified TargetHttpsProxy resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteTargetHttpsProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String targetHttpsProxy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified TargetHttpsProxy resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetTargetHttpsProxyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String targetHttpsProxy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a TargetHttpsProxy resource in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertTargetHttpsProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, TargetHttpsProxy targetHttpsProxyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of TargetHttpsProxy resources available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListTargetHttpsProxiesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Patches the specified TargetHttpsProxy resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchTargetHttpsProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String targetHttpsProxy, TargetHttpsProxy targetHttpsProxyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
SetCertificateMap |  Changes the Certificate Map for TargetHttpsProxy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setCertificateMapAsync(SetCertificateMapTargetHttpsProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setCertificateMapAsync(String project, String targetHttpsProxy, TargetHttpsProxiesSetCertificateMapRequest targetHttpsProxiesSetCertificateMapRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setCertificateMapOperationCallable() 
  * setCertificateMapCallable() 

  
SetQuicOverride |  Sets the QUIC override policy for TargetHttpsProxy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setQuicOverrideAsync(SetQuicOverrideTargetHttpsProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setQuicOverrideAsync(String project, String targetHttpsProxy, TargetHttpsProxiesSetQuicOverrideRequest targetHttpsProxiesSetQuicOverrideRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setQuicOverrideOperationCallable() 
  * setQuicOverrideCallable() 

  
SetSslCertificates |  Replaces SslCertificates for TargetHttpsProxy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setSslCertificatesAsync(SetSslCertificatesTargetHttpsProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setSslCertificatesAsync(String project, String targetHttpsProxy, TargetHttpsProxiesSetSslCertificatesRequest targetHttpsProxiesSetSslCertificatesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setSslCertificatesOperationCallable() 
  * setSslCertificatesCallable() 

  
SetSslPolicy |  Sets the SSL policy for TargetHttpsProxy. The SSL policy specifies the server-side support for SSL features. This affects connections between clients and the HTTPS proxy load balancer. They do not affect the connection between the load balancer and the backends. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setSslPolicyAsync(SetSslPolicyTargetHttpsProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setSslPolicyAsync(String project, String targetHttpsProxy, SslPolicyReference sslPolicyReferenceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setSslPolicyOperationCallable() 
  * setSslPolicyCallable() 

  
SetUrlMap |  Changes the URL map for TargetHttpsProxy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setUrlMapAsync(SetUrlMapTargetHttpsProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setUrlMapAsync(String project, String targetHttpsProxy, UrlMapReference urlMapReferenceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setUrlMapOperationCallable() 
  * setUrlMapCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of TargetHttpsProxiesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TargetHttpsProxiesSettings targetHttpsProxiesSettings =
         TargetHttpsProxiesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     TargetHttpsProxiesClient targetHttpsProxiesClient =
         TargetHttpsProxiesClient.create(targetHttpsProxiesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TargetHttpsProxiesSettings targetHttpsProxiesSettings =
         TargetHttpsProxiesSettings.newBuilder().setEndpoint(myEndpoint).build();
     TargetHttpsProxiesClient targetHttpsProxiesClient =
         TargetHttpsProxiesClient.create(targetHttpsProxiesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TargetHttpsProxiesClient

## Static Methods 

### create()
    
    
    public static final TargetHttpsProxiesClient create()

Constructs an instance of TargetHttpsProxiesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[TargetHttpsProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxiesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TargetHttpsProxiesSettings settings)
    
    
    public static final TargetHttpsProxiesClient create(TargetHttpsProxiesSettings settings)

Constructs an instance of TargetHttpsProxiesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TargetHttpsProxiesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxiesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpsProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxiesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TargetHttpsProxiesStub stub)
    
    
    public static final TargetHttpsProxiesClient create(TargetHttpsProxiesStub stub)

Constructs an instance of TargetHttpsProxiesClient, using the given stub for making calls. This is for advanced usage - prefer using create(TargetHttpsProxiesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TargetHttpsProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.TargetHttpsProxiesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpsProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxiesClient)` |   
  
## Constructors 

### TargetHttpsProxiesClient(TargetHttpsProxiesSettings settings)
    
    
    protected TargetHttpsProxiesClient(TargetHttpsProxiesSettings settings)

Constructs an instance of TargetHttpsProxiesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TargetHttpsProxiesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxiesSettings)`  
  
  
### TargetHttpsProxiesClient(TargetHttpsProxiesStub stub)
    
    
    protected TargetHttpsProxiesClient(TargetHttpsProxiesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TargetHttpsProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.TargetHttpsProxiesStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListTargetHttpsProxiesRequest request)
    
    
    public final TargetHttpsProxiesClient.AggregatedListPagedResponse aggregatedList(AggregatedListTargetHttpsProxiesRequest request)

Retrieves the list of all TargetHttpsProxy resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       AggregatedListTargetHttpsProxiesRequest request =
           AggregatedListTargetHttpsProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, TargetHttpsProxiesScopedList> element :
           targetHttpsProxiesClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListTargetHttpsProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListTargetHttpsProxiesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpsProxiesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxiesClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final TargetHttpsProxiesClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves the list of all TargetHttpsProxy resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, TargetHttpsProxiesScopedList> element :
           targetHttpsProxiesClient.aggregatedList(project).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the project scoping this request.  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpsProxiesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxiesClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListTargetHttpsProxiesRequest,TargetHttpsProxyAggregatedList> aggregatedListCallable()

Retrieves the list of all TargetHttpsProxy resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       AggregatedListTargetHttpsProxiesRequest request =
           AggregatedListTargetHttpsProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         TargetHttpsProxyAggregatedList response =
             targetHttpsProxiesClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, TargetHttpsProxiesScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListTargetHttpsProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListTargetHttpsProxiesRequest),[TargetHttpsProxyAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxyAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListTargetHttpsProxiesRequest,TargetHttpsProxiesClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves the list of all TargetHttpsProxy resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       AggregatedListTargetHttpsProxiesRequest request =
           AggregatedListTargetHttpsProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, TargetHttpsProxiesScopedList>> future =
           targetHttpsProxiesClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, TargetHttpsProxiesScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListTargetHttpsProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListTargetHttpsProxiesRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxiesClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteTargetHttpsProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteTargetHttpsProxyRequest request)

Deletes the specified TargetHttpsProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       DeleteTargetHttpsProxyRequest request =
           DeleteTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       Operation response = targetHttpsProxiesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteTargetHttpsProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String targetHttpsProxy)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String targetHttpsProxy)

Deletes the specified TargetHttpsProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String targetHttpsProxy = "targetHttpsProxy833943732";
       Operation response = targetHttpsProxiesClient.deleteAsync(project, targetHttpsProxy).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetHttpsProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpsProxy resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteTargetHttpsProxyRequest,Operation> deleteCallable()

Deletes the specified TargetHttpsProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       DeleteTargetHttpsProxyRequest request =
           DeleteTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       ApiFuture<Operation> future = targetHttpsProxiesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteTargetHttpsProxyRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified TargetHttpsProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       DeleteTargetHttpsProxyRequest request =
           DeleteTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       OperationFuture<Operation, Operation> future =
           targetHttpsProxiesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetTargetHttpsProxyRequest request)
    
    
    public final TargetHttpsProxy get(GetTargetHttpsProxyRequest request)

Returns the specified TargetHttpsProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       GetTargetHttpsProxyRequest request =
           GetTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       TargetHttpsProxy response = targetHttpsProxiesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetTargetHttpsProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpsProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxy)` |   
  
### get(String project, String targetHttpsProxy)
    
    
    public final TargetHttpsProxy get(String project, String targetHttpsProxy)

Returns the specified TargetHttpsProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String targetHttpsProxy = "targetHttpsProxy833943732";
       TargetHttpsProxy response = targetHttpsProxiesClient.get(project, targetHttpsProxy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetHttpsProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpsProxy resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpsProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxy)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetTargetHttpsProxyRequest,TargetHttpsProxy> getCallable()

Returns the specified TargetHttpsProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       GetTargetHttpsProxyRequest request =
           GetTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       ApiFuture<TargetHttpsProxy> future =
           targetHttpsProxiesClient.getCallable().futureCall(request);
       // Do something.
       TargetHttpsProxy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetTargetHttpsProxyRequest),[TargetHttpsProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxy)>` |   
  
### getSettings()
    
    
    public final @Nullable TargetHttpsProxiesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.TargetHttpsProxiesSettings` |   
  
### getStub()
    
    
    public TargetHttpsProxiesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[TargetHttpsProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.TargetHttpsProxiesStub)` |   
  
### insertAsync(InsertTargetHttpsProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertTargetHttpsProxyRequest request)

Creates a TargetHttpsProxy resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       InsertTargetHttpsProxyRequest request =
           InsertTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxyResource(TargetHttpsProxy.newBuilder().build())
               .build();
       Operation response = targetHttpsProxiesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertTargetHttpsProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, TargetHttpsProxy targetHttpsProxyResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, TargetHttpsProxy targetHttpsProxyResource)

Creates a TargetHttpsProxy resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       TargetHttpsProxy targetHttpsProxyResource = TargetHttpsProxy.newBuilder().build();
       Operation response =
           targetHttpsProxiesClient.insertAsync(project, targetHttpsProxyResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetHttpsProxyResource` | `[TargetHttpsProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertTargetHttpsProxyRequest,Operation> insertCallable()

Creates a TargetHttpsProxy resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       InsertTargetHttpsProxyRequest request =
           InsertTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxyResource(TargetHttpsProxy.newBuilder().build())
               .build();
       ApiFuture<Operation> future = targetHttpsProxiesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertTargetHttpsProxyRequest,Operation,Operation> insertOperationCallable()

Creates a TargetHttpsProxy resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       InsertTargetHttpsProxyRequest request =
           InsertTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxyResource(TargetHttpsProxy.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           targetHttpsProxiesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListTargetHttpsProxiesRequest request)
    
    
    public final TargetHttpsProxiesClient.ListPagedResponse list(ListTargetHttpsProxiesRequest request)

Retrieves the list of TargetHttpsProxy resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       ListTargetHttpsProxiesRequest request =
           ListTargetHttpsProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (TargetHttpsProxy element : targetHttpsProxiesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTargetHttpsProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListTargetHttpsProxiesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpsProxiesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxiesClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final TargetHttpsProxiesClient.ListPagedResponse list(String project)

Retrieves the list of TargetHttpsProxy resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       for (TargetHttpsProxy element : targetHttpsProxiesClient.list(project).iterateAll()) {
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
`[TargetHttpsProxiesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxiesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListTargetHttpsProxiesRequest,TargetHttpsProxyList> listCallable()

Retrieves the list of TargetHttpsProxy resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       ListTargetHttpsProxiesRequest request =
           ListTargetHttpsProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         TargetHttpsProxyList response = targetHttpsProxiesClient.listCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTargetHttpsProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListTargetHttpsProxiesRequest),[TargetHttpsProxyList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxyList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListTargetHttpsProxiesRequest,TargetHttpsProxiesClient.ListPagedResponse> listPagedCallable()

Retrieves the list of TargetHttpsProxy resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       ListTargetHttpsProxiesRequest request =
           ListTargetHttpsProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<TargetHttpsProxy> future =
           targetHttpsProxiesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (TargetHttpsProxy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTargetHttpsProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListTargetHttpsProxiesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxiesClient.ListPagedResponse)>` |   
  
### patchAsync(PatchTargetHttpsProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchTargetHttpsProxyRequest request)

Patches the specified TargetHttpsProxy resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       PatchTargetHttpsProxyRequest request =
           PatchTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .setTargetHttpsProxyResource(TargetHttpsProxy.newBuilder().build())
               .build();
       Operation response = targetHttpsProxiesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchTargetHttpsProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String targetHttpsProxy, TargetHttpsProxy targetHttpsProxyResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String targetHttpsProxy, TargetHttpsProxy targetHttpsProxyResource)

Patches the specified TargetHttpsProxy resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String targetHttpsProxy = "targetHttpsProxy833943732";
       TargetHttpsProxy targetHttpsProxyResource = TargetHttpsProxy.newBuilder().build();
       Operation response =
           targetHttpsProxiesClient
               .patchAsync(project, targetHttpsProxy, targetHttpsProxyResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetHttpsProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpsProxy resource to patch.  
`targetHttpsProxyResource` | `[TargetHttpsProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchTargetHttpsProxyRequest,Operation> patchCallable()

Patches the specified TargetHttpsProxy resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       PatchTargetHttpsProxyRequest request =
           PatchTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .setTargetHttpsProxyResource(TargetHttpsProxy.newBuilder().build())
               .build();
       ApiFuture<Operation> future = targetHttpsProxiesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchTargetHttpsProxyRequest,Operation,Operation> patchOperationCallable()

Patches the specified TargetHttpsProxy resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       PatchTargetHttpsProxyRequest request =
           PatchTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .setTargetHttpsProxyResource(TargetHttpsProxy.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           targetHttpsProxiesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setCertificateMapAsync(SetCertificateMapTargetHttpsProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> setCertificateMapAsync(SetCertificateMapTargetHttpsProxyRequest request)

Changes the Certificate Map for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       SetCertificateMapTargetHttpsProxyRequest request =
           SetCertificateMapTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxiesSetCertificateMapRequestResource(
                   TargetHttpsProxiesSetCertificateMapRequest.newBuilder().build())
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       Operation response = targetHttpsProxiesClient.setCertificateMapAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetCertificateMapTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetCertificateMapTargetHttpsProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setCertificateMapAsync(String project, String targetHttpsProxy, TargetHttpsProxiesSetCertificateMapRequest targetHttpsProxiesSetCertificateMapRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setCertificateMapAsync(String project, String targetHttpsProxy, TargetHttpsProxiesSetCertificateMapRequest targetHttpsProxiesSetCertificateMapRequestResource)

Changes the Certificate Map for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String targetHttpsProxy = "targetHttpsProxy833943732";
       TargetHttpsProxiesSetCertificateMapRequest
           targetHttpsProxiesSetCertificateMapRequestResource =
               TargetHttpsProxiesSetCertificateMapRequest.newBuilder().build();
       Operation response =
           targetHttpsProxiesClient
               .setCertificateMapAsync(
                   project, targetHttpsProxy, targetHttpsProxiesSetCertificateMapRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetHttpsProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpsProxy resource whose CertificateMap is to be set. The name must be 1-63 characters long, and comply with RFC1035.  
`targetHttpsProxiesSetCertificateMapRequestResource` | `[TargetHttpsProxiesSetCertificateMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxiesSetCertificateMapRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setCertificateMapCallable()
    
    
    public final UnaryCallable<SetCertificateMapTargetHttpsProxyRequest,Operation> setCertificateMapCallable()

Changes the Certificate Map for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       SetCertificateMapTargetHttpsProxyRequest request =
           SetCertificateMapTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxiesSetCertificateMapRequestResource(
                   TargetHttpsProxiesSetCertificateMapRequest.newBuilder().build())
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       ApiFuture<Operation> future =
           targetHttpsProxiesClient.setCertificateMapCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetCertificateMapTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetCertificateMapTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setCertificateMapOperationCallable()
    
    
    public final OperationCallable<SetCertificateMapTargetHttpsProxyRequest,Operation,Operation> setCertificateMapOperationCallable()

Changes the Certificate Map for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       SetCertificateMapTargetHttpsProxyRequest request =
           SetCertificateMapTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxiesSetCertificateMapRequestResource(
                   TargetHttpsProxiesSetCertificateMapRequest.newBuilder().build())
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       OperationFuture<Operation, Operation> future =
           targetHttpsProxiesClient.setCertificateMapOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetCertificateMapTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetCertificateMapTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setQuicOverrideAsync(SetQuicOverrideTargetHttpsProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> setQuicOverrideAsync(SetQuicOverrideTargetHttpsProxyRequest request)

Sets the QUIC override policy for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       SetQuicOverrideTargetHttpsProxyRequest request =
           SetQuicOverrideTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxiesSetQuicOverrideRequestResource(
                   TargetHttpsProxiesSetQuicOverrideRequest.newBuilder().build())
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       Operation response = targetHttpsProxiesClient.setQuicOverrideAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetQuicOverrideTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetQuicOverrideTargetHttpsProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setQuicOverrideAsync(String project, String targetHttpsProxy, TargetHttpsProxiesSetQuicOverrideRequest targetHttpsProxiesSetQuicOverrideRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setQuicOverrideAsync(String project, String targetHttpsProxy, TargetHttpsProxiesSetQuicOverrideRequest targetHttpsProxiesSetQuicOverrideRequestResource)

Sets the QUIC override policy for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String targetHttpsProxy = "targetHttpsProxy833943732";
       TargetHttpsProxiesSetQuicOverrideRequest targetHttpsProxiesSetQuicOverrideRequestResource =
           TargetHttpsProxiesSetQuicOverrideRequest.newBuilder().build();
       Operation response =
           targetHttpsProxiesClient
               .setQuicOverrideAsync(
                   project, targetHttpsProxy, targetHttpsProxiesSetQuicOverrideRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetHttpsProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpsProxy resource to set the QUIC override policy for. The name should conform to RFC1035.  
`targetHttpsProxiesSetQuicOverrideRequestResource` | `[TargetHttpsProxiesSetQuicOverrideRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxiesSetQuicOverrideRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setQuicOverrideCallable()
    
    
    public final UnaryCallable<SetQuicOverrideTargetHttpsProxyRequest,Operation> setQuicOverrideCallable()

Sets the QUIC override policy for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       SetQuicOverrideTargetHttpsProxyRequest request =
           SetQuicOverrideTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxiesSetQuicOverrideRequestResource(
                   TargetHttpsProxiesSetQuicOverrideRequest.newBuilder().build())
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       ApiFuture<Operation> future =
           targetHttpsProxiesClient.setQuicOverrideCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetQuicOverrideTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetQuicOverrideTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setQuicOverrideOperationCallable()
    
    
    public final OperationCallable<SetQuicOverrideTargetHttpsProxyRequest,Operation,Operation> setQuicOverrideOperationCallable()

Sets the QUIC override policy for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       SetQuicOverrideTargetHttpsProxyRequest request =
           SetQuicOverrideTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxiesSetQuicOverrideRequestResource(
                   TargetHttpsProxiesSetQuicOverrideRequest.newBuilder().build())
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       OperationFuture<Operation, Operation> future =
           targetHttpsProxiesClient.setQuicOverrideOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetQuicOverrideTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetQuicOverrideTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslCertificatesAsync(SetSslCertificatesTargetHttpsProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> setSslCertificatesAsync(SetSslCertificatesTargetHttpsProxyRequest request)

Replaces SslCertificates for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       SetSslCertificatesTargetHttpsProxyRequest request =
           SetSslCertificatesTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxiesSetSslCertificatesRequestResource(
                   TargetHttpsProxiesSetSslCertificatesRequest.newBuilder().build())
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       Operation response = targetHttpsProxiesClient.setSslCertificatesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetSslCertificatesTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSslCertificatesTargetHttpsProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslCertificatesAsync(String project, String targetHttpsProxy, TargetHttpsProxiesSetSslCertificatesRequest targetHttpsProxiesSetSslCertificatesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setSslCertificatesAsync(String project, String targetHttpsProxy, TargetHttpsProxiesSetSslCertificatesRequest targetHttpsProxiesSetSslCertificatesRequestResource)

Replaces SslCertificates for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String targetHttpsProxy = "targetHttpsProxy833943732";
       TargetHttpsProxiesSetSslCertificatesRequest
           targetHttpsProxiesSetSslCertificatesRequestResource =
               TargetHttpsProxiesSetSslCertificatesRequest.newBuilder().build();
       Operation response =
           targetHttpsProxiesClient
               .setSslCertificatesAsync(
                   project, targetHttpsProxy, targetHttpsProxiesSetSslCertificatesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetHttpsProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpsProxy resource to set an SslCertificates resource for.  
`targetHttpsProxiesSetSslCertificatesRequestResource` | `[TargetHttpsProxiesSetSslCertificatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpsProxiesSetSslCertificatesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslCertificatesCallable()
    
    
    public final UnaryCallable<SetSslCertificatesTargetHttpsProxyRequest,Operation> setSslCertificatesCallable()

Replaces SslCertificates for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       SetSslCertificatesTargetHttpsProxyRequest request =
           SetSslCertificatesTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxiesSetSslCertificatesRequestResource(
                   TargetHttpsProxiesSetSslCertificatesRequest.newBuilder().build())
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       ApiFuture<Operation> future =
           targetHttpsProxiesClient.setSslCertificatesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetSslCertificatesTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSslCertificatesTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslCertificatesOperationCallable()
    
    
    public final OperationCallable<SetSslCertificatesTargetHttpsProxyRequest,Operation,Operation> setSslCertificatesOperationCallable()

Replaces SslCertificates for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       SetSslCertificatesTargetHttpsProxyRequest request =
           SetSslCertificatesTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxiesSetSslCertificatesRequestResource(
                   TargetHttpsProxiesSetSslCertificatesRequest.newBuilder().build())
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       OperationFuture<Operation, Operation> future =
           targetHttpsProxiesClient.setSslCertificatesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetSslCertificatesTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSslCertificatesTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslPolicyAsync(SetSslPolicyTargetHttpsProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> setSslPolicyAsync(SetSslPolicyTargetHttpsProxyRequest request)

Sets the SSL policy for TargetHttpsProxy. The SSL policy specifies the server-side support for SSL features. This affects connections between clients and the HTTPS proxy load balancer. They do not affect the connection between the load balancer and the backends.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       SetSslPolicyTargetHttpsProxyRequest request =
           SetSslPolicyTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSslPolicyReferenceResource(SslPolicyReference.newBuilder().build())
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       Operation response = targetHttpsProxiesClient.setSslPolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetSslPolicyTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSslPolicyTargetHttpsProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslPolicyAsync(String project, String targetHttpsProxy, SslPolicyReference sslPolicyReferenceResource)
    
    
    public final OperationFuture<Operation,Operation> setSslPolicyAsync(String project, String targetHttpsProxy, SslPolicyReference sslPolicyReferenceResource)

Sets the SSL policy for TargetHttpsProxy. The SSL policy specifies the server-side support for SSL features. This affects connections between clients and the HTTPS proxy load balancer. They do not affect the connection between the load balancer and the backends.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String targetHttpsProxy = "targetHttpsProxy833943732";
       SslPolicyReference sslPolicyReferenceResource = SslPolicyReference.newBuilder().build();
       Operation response =
           targetHttpsProxiesClient
               .setSslPolicyAsync(project, targetHttpsProxy, sslPolicyReferenceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetHttpsProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpsProxy resource whose SSL policy is to be set. The name must be 1-63 characters long, and comply with RFC1035.  
`sslPolicyReferenceResource` | `[SslPolicyReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SslPolicyReference)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslPolicyCallable()
    
    
    public final UnaryCallable<SetSslPolicyTargetHttpsProxyRequest,Operation> setSslPolicyCallable()

Sets the SSL policy for TargetHttpsProxy. The SSL policy specifies the server-side support for SSL features. This affects connections between clients and the HTTPS proxy load balancer. They do not affect the connection between the load balancer and the backends.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       SetSslPolicyTargetHttpsProxyRequest request =
           SetSslPolicyTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSslPolicyReferenceResource(SslPolicyReference.newBuilder().build())
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       ApiFuture<Operation> future =
           targetHttpsProxiesClient.setSslPolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetSslPolicyTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSslPolicyTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setSslPolicyOperationCallable()
    
    
    public final OperationCallable<SetSslPolicyTargetHttpsProxyRequest,Operation,Operation> setSslPolicyOperationCallable()

Sets the SSL policy for TargetHttpsProxy. The SSL policy specifies the server-side support for SSL features. This affects connections between clients and the HTTPS proxy load balancer. They do not affect the connection between the load balancer and the backends.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       SetSslPolicyTargetHttpsProxyRequest request =
           SetSslPolicyTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSslPolicyReferenceResource(SslPolicyReference.newBuilder().build())
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .build();
       OperationFuture<Operation, Operation> future =
           targetHttpsProxiesClient.setSslPolicyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetSslPolicyTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetSslPolicyTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUrlMapAsync(SetUrlMapTargetHttpsProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> setUrlMapAsync(SetUrlMapTargetHttpsProxyRequest request)

Changes the URL map for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       SetUrlMapTargetHttpsProxyRequest request =
           SetUrlMapTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .setUrlMapReferenceResource(UrlMapReference.newBuilder().build())
               .build();
       Operation response = targetHttpsProxiesClient.setUrlMapAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetUrlMapTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUrlMapTargetHttpsProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUrlMapAsync(String project, String targetHttpsProxy, UrlMapReference urlMapReferenceResource)
    
    
    public final OperationFuture<Operation,Operation> setUrlMapAsync(String project, String targetHttpsProxy, UrlMapReference urlMapReferenceResource)

Changes the URL map for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       String project = "project-309310695";
       String targetHttpsProxy = "targetHttpsProxy833943732";
       UrlMapReference urlMapReferenceResource = UrlMapReference.newBuilder().build();
       Operation response =
           targetHttpsProxiesClient
               .setUrlMapAsync(project, targetHttpsProxy, urlMapReferenceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetHttpsProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpsProxy resource whose URL map is to be set.  
`urlMapReferenceResource` | `[UrlMapReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapReference)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUrlMapCallable()
    
    
    public final UnaryCallable<SetUrlMapTargetHttpsProxyRequest,Operation> setUrlMapCallable()

Changes the URL map for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       SetUrlMapTargetHttpsProxyRequest request =
           SetUrlMapTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .setUrlMapReferenceResource(UrlMapReference.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           targetHttpsProxiesClient.setUrlMapCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetUrlMapTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUrlMapTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUrlMapOperationCallable()
    
    
    public final OperationCallable<SetUrlMapTargetHttpsProxyRequest,Operation,Operation> setUrlMapOperationCallable()

Changes the URL map for TargetHttpsProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpsProxiesClient targetHttpsProxiesClient = TargetHttpsProxiesClient.create()) {
       SetUrlMapTargetHttpsProxyRequest request =
           SetUrlMapTargetHttpsProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpsProxy("targetHttpsProxy833943732")
               .setUrlMapReferenceResource(UrlMapReference.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           targetHttpsProxiesClient.setUrlMapOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetUrlMapTargetHttpsProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUrlMapTargetHttpsProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
