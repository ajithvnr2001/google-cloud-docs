---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxiesClient
title: Class TargetHttpProxiesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:34.428066+00:00
---

# Class TargetHttpProxiesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxiesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TargetHttpProxiesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/TargetHttpProxiesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The TargetHttpProxies API.

This client uses TargetHttpProxies version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       String project = "project-309310695";
       String targetHttpProxy = "targetHttpProxy-1944074187";
       TargetHttpProxy response = targetHttpProxiesClient.get(project, targetHttpProxy);
     }
     

Note: close() needs to be called on the TargetHttpProxiesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves the list of all TargetHttpProxy resources, regional and global, available to the specified project.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListTargetHttpProxiesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified TargetHttpProxy resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteTargetHttpProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String targetHttpProxy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified TargetHttpProxy resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetTargetHttpProxyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String targetHttpProxy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a TargetHttpProxy resource in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertTargetHttpProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, TargetHttpProxy targetHttpProxyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of TargetHttpProxy resources available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListTargetHttpProxiesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Patches the specified TargetHttpProxy resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchTargetHttpProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String targetHttpProxy, TargetHttpProxy targetHttpProxyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
SetUrlMap |  Changes the URL map for TargetHttpProxy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setUrlMapAsync(SetUrlMapTargetHttpProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setUrlMapAsync(String project, String targetHttpProxy, UrlMapReference urlMapReferenceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setUrlMapOperationCallable() 
  * setUrlMapCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of TargetHttpProxiesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TargetHttpProxiesSettings targetHttpProxiesSettings =
         TargetHttpProxiesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     TargetHttpProxiesClient targetHttpProxiesClient =
         TargetHttpProxiesClient.create(targetHttpProxiesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TargetHttpProxiesSettings targetHttpProxiesSettings =
         TargetHttpProxiesSettings.newBuilder().setEndpoint(myEndpoint).build();
     TargetHttpProxiesClient targetHttpProxiesClient =
         TargetHttpProxiesClient.create(targetHttpProxiesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TargetHttpProxiesClient

## Static Methods 

### create()
    
    
    public static final TargetHttpProxiesClient create()

Constructs an instance of TargetHttpProxiesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[TargetHttpProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxiesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TargetHttpProxiesSettings settings)
    
    
    public static final TargetHttpProxiesClient create(TargetHttpProxiesSettings settings)

Constructs an instance of TargetHttpProxiesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TargetHttpProxiesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxiesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxiesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TargetHttpProxiesStub stub)
    
    
    public static final TargetHttpProxiesClient create(TargetHttpProxiesStub stub)

Constructs an instance of TargetHttpProxiesClient, using the given stub for making calls. This is for advanced usage - prefer using create(TargetHttpProxiesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TargetHttpProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.TargetHttpProxiesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxiesClient)` |   
  
## Constructors 

### TargetHttpProxiesClient(TargetHttpProxiesSettings settings)
    
    
    protected TargetHttpProxiesClient(TargetHttpProxiesSettings settings)

Constructs an instance of TargetHttpProxiesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TargetHttpProxiesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxiesSettings)`  
  
  
### TargetHttpProxiesClient(TargetHttpProxiesStub stub)
    
    
    protected TargetHttpProxiesClient(TargetHttpProxiesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TargetHttpProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.TargetHttpProxiesStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListTargetHttpProxiesRequest request)
    
    
    public final TargetHttpProxiesClient.AggregatedListPagedResponse aggregatedList(AggregatedListTargetHttpProxiesRequest request)

Retrieves the list of all TargetHttpProxy resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       AggregatedListTargetHttpProxiesRequest request =
           AggregatedListTargetHttpProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, TargetHttpProxiesScopedList> element :
           targetHttpProxiesClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListTargetHttpProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListTargetHttpProxiesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpProxiesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxiesClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final TargetHttpProxiesClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves the list of all TargetHttpProxy resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, TargetHttpProxiesScopedList> element :
           targetHttpProxiesClient.aggregatedList(project).iterateAll()) {
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
`[TargetHttpProxiesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxiesClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListTargetHttpProxiesRequest,TargetHttpProxyAggregatedList> aggregatedListCallable()

Retrieves the list of all TargetHttpProxy resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       AggregatedListTargetHttpProxiesRequest request =
           AggregatedListTargetHttpProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         TargetHttpProxyAggregatedList response =
             targetHttpProxiesClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, TargetHttpProxiesScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListTargetHttpProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListTargetHttpProxiesRequest),[TargetHttpProxyAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxyAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListTargetHttpProxiesRequest,TargetHttpProxiesClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves the list of all TargetHttpProxy resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       AggregatedListTargetHttpProxiesRequest request =
           AggregatedListTargetHttpProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, TargetHttpProxiesScopedList>> future =
           targetHttpProxiesClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, TargetHttpProxiesScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListTargetHttpProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListTargetHttpProxiesRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxiesClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteTargetHttpProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteTargetHttpProxyRequest request)

Deletes the specified TargetHttpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       DeleteTargetHttpProxyRequest request =
           DeleteTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .build();
       Operation response = targetHttpProxiesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteTargetHttpProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String targetHttpProxy)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String targetHttpProxy)

Deletes the specified TargetHttpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       String project = "project-309310695";
       String targetHttpProxy = "targetHttpProxy-1944074187";
       Operation response = targetHttpProxiesClient.deleteAsync(project, targetHttpProxy).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetHttpProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpProxy resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteTargetHttpProxyRequest,Operation> deleteCallable()

Deletes the specified TargetHttpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       DeleteTargetHttpProxyRequest request =
           DeleteTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .build();
       ApiFuture<Operation> future = targetHttpProxiesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteTargetHttpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteTargetHttpProxyRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified TargetHttpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       DeleteTargetHttpProxyRequest request =
           DeleteTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .build();
       OperationFuture<Operation, Operation> future =
           targetHttpProxiesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteTargetHttpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetTargetHttpProxyRequest request)
    
    
    public final TargetHttpProxy get(GetTargetHttpProxyRequest request)

Returns the specified TargetHttpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       GetTargetHttpProxyRequest request =
           GetTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .build();
       TargetHttpProxy response = targetHttpProxiesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetTargetHttpProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxy)` |   
  
### get(String project, String targetHttpProxy)
    
    
    public final TargetHttpProxy get(String project, String targetHttpProxy)

Returns the specified TargetHttpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       String project = "project-309310695";
       String targetHttpProxy = "targetHttpProxy-1944074187";
       TargetHttpProxy response = targetHttpProxiesClient.get(project, targetHttpProxy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetHttpProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpProxy resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxy)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetTargetHttpProxyRequest,TargetHttpProxy> getCallable()

Returns the specified TargetHttpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       GetTargetHttpProxyRequest request =
           GetTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .build();
       ApiFuture<TargetHttpProxy> future = targetHttpProxiesClient.getCallable().futureCall(request);
       // Do something.
       TargetHttpProxy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetTargetHttpProxyRequest),[TargetHttpProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxy)>` |   
  
### getSettings()
    
    
    public final @Nullable TargetHttpProxiesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.TargetHttpProxiesSettings` |   
  
### getStub()
    
    
    public TargetHttpProxiesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[TargetHttpProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.TargetHttpProxiesStub)` |   
  
### insertAsync(InsertTargetHttpProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertTargetHttpProxyRequest request)

Creates a TargetHttpProxy resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       InsertTargetHttpProxyRequest request =
           InsertTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpProxyResource(TargetHttpProxy.newBuilder().build())
               .build();
       Operation response = targetHttpProxiesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertTargetHttpProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, TargetHttpProxy targetHttpProxyResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, TargetHttpProxy targetHttpProxyResource)

Creates a TargetHttpProxy resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       String project = "project-309310695";
       TargetHttpProxy targetHttpProxyResource = TargetHttpProxy.newBuilder().build();
       Operation response =
           targetHttpProxiesClient.insertAsync(project, targetHttpProxyResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetHttpProxyResource` | `[TargetHttpProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertTargetHttpProxyRequest,Operation> insertCallable()

Creates a TargetHttpProxy resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       InsertTargetHttpProxyRequest request =
           InsertTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpProxyResource(TargetHttpProxy.newBuilder().build())
               .build();
       ApiFuture<Operation> future = targetHttpProxiesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertTargetHttpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertTargetHttpProxyRequest,Operation,Operation> insertOperationCallable()

Creates a TargetHttpProxy resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       InsertTargetHttpProxyRequest request =
           InsertTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpProxyResource(TargetHttpProxy.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           targetHttpProxiesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertTargetHttpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListTargetHttpProxiesRequest request)
    
    
    public final TargetHttpProxiesClient.ListPagedResponse list(ListTargetHttpProxiesRequest request)

Retrieves the list of TargetHttpProxy resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       ListTargetHttpProxiesRequest request =
           ListTargetHttpProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (TargetHttpProxy element : targetHttpProxiesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTargetHttpProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListTargetHttpProxiesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetHttpProxiesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxiesClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final TargetHttpProxiesClient.ListPagedResponse list(String project)

Retrieves the list of TargetHttpProxy resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       String project = "project-309310695";
       for (TargetHttpProxy element : targetHttpProxiesClient.list(project).iterateAll()) {
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
`[TargetHttpProxiesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxiesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListTargetHttpProxiesRequest,TargetHttpProxyList> listCallable()

Retrieves the list of TargetHttpProxy resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       ListTargetHttpProxiesRequest request =
           ListTargetHttpProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         TargetHttpProxyList response = targetHttpProxiesClient.listCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTargetHttpProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListTargetHttpProxiesRequest),[TargetHttpProxyList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxyList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListTargetHttpProxiesRequest,TargetHttpProxiesClient.ListPagedResponse> listPagedCallable()

Retrieves the list of TargetHttpProxy resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       ListTargetHttpProxiesRequest request =
           ListTargetHttpProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<TargetHttpProxy> future =
           targetHttpProxiesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (TargetHttpProxy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTargetHttpProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListTargetHttpProxiesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxiesClient.ListPagedResponse)>` |   
  
### patchAsync(PatchTargetHttpProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchTargetHttpProxyRequest request)

Patches the specified TargetHttpProxy resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       PatchTargetHttpProxyRequest request =
           PatchTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .setTargetHttpProxyResource(TargetHttpProxy.newBuilder().build())
               .build();
       Operation response = targetHttpProxiesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchTargetHttpProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String targetHttpProxy, TargetHttpProxy targetHttpProxyResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String targetHttpProxy, TargetHttpProxy targetHttpProxyResource)

Patches the specified TargetHttpProxy resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       String project = "project-309310695";
       String targetHttpProxy = "targetHttpProxy-1944074187";
       TargetHttpProxy targetHttpProxyResource = TargetHttpProxy.newBuilder().build();
       Operation response =
           targetHttpProxiesClient
               .patchAsync(project, targetHttpProxy, targetHttpProxyResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetHttpProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpProxy resource to patch.  
`targetHttpProxyResource` | `[TargetHttpProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetHttpProxy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchTargetHttpProxyRequest,Operation> patchCallable()

Patches the specified TargetHttpProxy resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       PatchTargetHttpProxyRequest request =
           PatchTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .setTargetHttpProxyResource(TargetHttpProxy.newBuilder().build())
               .build();
       ApiFuture<Operation> future = targetHttpProxiesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchTargetHttpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchTargetHttpProxyRequest,Operation,Operation> patchOperationCallable()

Patches the specified TargetHttpProxy resource with the data included in the request. This method supports PATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       PatchTargetHttpProxyRequest request =
           PatchTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .setTargetHttpProxyResource(TargetHttpProxy.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           targetHttpProxiesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchTargetHttpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUrlMapAsync(SetUrlMapTargetHttpProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> setUrlMapAsync(SetUrlMapTargetHttpProxyRequest request)

Changes the URL map for TargetHttpProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       SetUrlMapTargetHttpProxyRequest request =
           SetUrlMapTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .setUrlMapReferenceResource(UrlMapReference.newBuilder().build())
               .build();
       Operation response = targetHttpProxiesClient.setUrlMapAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetUrlMapTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUrlMapTargetHttpProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUrlMapAsync(String project, String targetHttpProxy, UrlMapReference urlMapReferenceResource)
    
    
    public final OperationFuture<Operation,Operation> setUrlMapAsync(String project, String targetHttpProxy, UrlMapReference urlMapReferenceResource)

Changes the URL map for TargetHttpProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       String project = "project-309310695";
       String targetHttpProxy = "targetHttpProxy-1944074187";
       UrlMapReference urlMapReferenceResource = UrlMapReference.newBuilder().build();
       Operation response =
           targetHttpProxiesClient
               .setUrlMapAsync(project, targetHttpProxy, urlMapReferenceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetHttpProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetHttpProxy to set a URL map for.  
`urlMapReferenceResource` | `[UrlMapReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapReference)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUrlMapCallable()
    
    
    public final UnaryCallable<SetUrlMapTargetHttpProxyRequest,Operation> setUrlMapCallable()

Changes the URL map for TargetHttpProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       SetUrlMapTargetHttpProxyRequest request =
           SetUrlMapTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .setUrlMapReferenceResource(UrlMapReference.newBuilder().build())
               .build();
       ApiFuture<Operation> future = targetHttpProxiesClient.setUrlMapCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetUrlMapTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUrlMapTargetHttpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUrlMapOperationCallable()
    
    
    public final OperationCallable<SetUrlMapTargetHttpProxyRequest,Operation,Operation> setUrlMapOperationCallable()

Changes the URL map for TargetHttpProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetHttpProxiesClient targetHttpProxiesClient = TargetHttpProxiesClient.create()) {
       SetUrlMapTargetHttpProxyRequest request =
           SetUrlMapTargetHttpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetHttpProxy("targetHttpProxy-1944074187")
               .setUrlMapReferenceResource(UrlMapReference.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           targetHttpProxiesClient.setUrlMapOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetUrlMapTargetHttpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUrlMapTargetHttpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
