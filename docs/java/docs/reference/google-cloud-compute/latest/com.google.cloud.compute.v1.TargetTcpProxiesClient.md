---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxiesClient
title: Class TargetTcpProxiesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:42.086453+00:00
---

# Class TargetTcpProxiesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxiesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TargetTcpProxiesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/TargetTcpProxiesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The TargetTcpProxies API.

This client uses TargetTcpProxies version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       String project = "project-309310695";
       String targetTcpProxy = "targetTcpProxy-337144898";
       TargetTcpProxy response = targetTcpProxiesClient.get(project, targetTcpProxy);
     }
     

Note: close() needs to be called on the TargetTcpProxiesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves the list of all TargetTcpProxy resources, regional and global, available to the specified project.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListTargetTcpProxiesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified TargetTcpProxy resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteTargetTcpProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String targetTcpProxy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified TargetTcpProxy resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetTargetTcpProxyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String targetTcpProxy) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a TargetTcpProxy resource in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertTargetTcpProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, TargetTcpProxy targetTcpProxyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of TargetTcpProxy resources available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListTargetTcpProxiesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
SetBackendService |  Changes the BackendService for TargetTcpProxy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setBackendServiceAsync(SetBackendServiceTargetTcpProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setBackendServiceAsync(String project, String targetTcpProxy, TargetTcpProxiesSetBackendServiceRequest targetTcpProxiesSetBackendServiceRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setBackendServiceOperationCallable() 
  * setBackendServiceCallable() 

  
SetProxyHeader |  Changes the ProxyHeaderType for TargetTcpProxy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setProxyHeaderAsync(SetProxyHeaderTargetTcpProxyRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setProxyHeaderAsync(String project, String targetTcpProxy, TargetTcpProxiesSetProxyHeaderRequest targetTcpProxiesSetProxyHeaderRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setProxyHeaderOperationCallable() 
  * setProxyHeaderCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsTargetTcpProxyRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of TargetTcpProxiesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TargetTcpProxiesSettings targetTcpProxiesSettings =
         TargetTcpProxiesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     TargetTcpProxiesClient targetTcpProxiesClient =
         TargetTcpProxiesClient.create(targetTcpProxiesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     TargetTcpProxiesSettings targetTcpProxiesSettings =
         TargetTcpProxiesSettings.newBuilder().setEndpoint(myEndpoint).build();
     TargetTcpProxiesClient targetTcpProxiesClient =
         TargetTcpProxiesClient.create(targetTcpProxiesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TargetTcpProxiesClient

## Static Methods 

### create()
    
    
    public static final TargetTcpProxiesClient create()

Constructs an instance of TargetTcpProxiesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[TargetTcpProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxiesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TargetTcpProxiesSettings settings)
    
    
    public static final TargetTcpProxiesClient create(TargetTcpProxiesSettings settings)

Constructs an instance of TargetTcpProxiesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TargetTcpProxiesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxiesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TargetTcpProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxiesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(TargetTcpProxiesStub stub)
    
    
    public static final TargetTcpProxiesClient create(TargetTcpProxiesStub stub)

Constructs an instance of TargetTcpProxiesClient, using the given stub for making calls. This is for advanced usage - prefer using create(TargetTcpProxiesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TargetTcpProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.TargetTcpProxiesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TargetTcpProxiesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxiesClient)` |   
  
## Constructors 

### TargetTcpProxiesClient(TargetTcpProxiesSettings settings)
    
    
    protected TargetTcpProxiesClient(TargetTcpProxiesSettings settings)

Constructs an instance of TargetTcpProxiesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[TargetTcpProxiesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxiesSettings)`  
  
  
### TargetTcpProxiesClient(TargetTcpProxiesStub stub)
    
    
    protected TargetTcpProxiesClient(TargetTcpProxiesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[TargetTcpProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.TargetTcpProxiesStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListTargetTcpProxiesRequest request)
    
    
    public final TargetTcpProxiesClient.AggregatedListPagedResponse aggregatedList(AggregatedListTargetTcpProxiesRequest request)

Retrieves the list of all TargetTcpProxy resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       AggregatedListTargetTcpProxiesRequest request =
           AggregatedListTargetTcpProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, TargetTcpProxiesScopedList> element :
           targetTcpProxiesClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListTargetTcpProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListTargetTcpProxiesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetTcpProxiesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxiesClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final TargetTcpProxiesClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves the list of all TargetTcpProxy resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, TargetTcpProxiesScopedList> element :
           targetTcpProxiesClient.aggregatedList(project).iterateAll()) {
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
`[TargetTcpProxiesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxiesClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListTargetTcpProxiesRequest,TargetTcpProxyAggregatedList> aggregatedListCallable()

Retrieves the list of all TargetTcpProxy resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       AggregatedListTargetTcpProxiesRequest request =
           AggregatedListTargetTcpProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         TargetTcpProxyAggregatedList response =
             targetTcpProxiesClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, TargetTcpProxiesScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListTargetTcpProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListTargetTcpProxiesRequest),[TargetTcpProxyAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxyAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListTargetTcpProxiesRequest,TargetTcpProxiesClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves the list of all TargetTcpProxy resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       AggregatedListTargetTcpProxiesRequest request =
           AggregatedListTargetTcpProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, TargetTcpProxiesScopedList>> future =
           targetTcpProxiesClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, TargetTcpProxiesScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListTargetTcpProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListTargetTcpProxiesRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxiesClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteTargetTcpProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteTargetTcpProxyRequest request)

Deletes the specified TargetTcpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       DeleteTargetTcpProxyRequest request =
           DeleteTargetTcpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetTcpProxy("targetTcpProxy-337144898")
               .build();
       Operation response = targetTcpProxiesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTargetTcpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteTargetTcpProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String targetTcpProxy)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String targetTcpProxy)

Deletes the specified TargetTcpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       String project = "project-309310695";
       String targetTcpProxy = "targetTcpProxy-337144898";
       Operation response = targetTcpProxiesClient.deleteAsync(project, targetTcpProxy).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetTcpProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetTcpProxy resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteTargetTcpProxyRequest,Operation> deleteCallable()

Deletes the specified TargetTcpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       DeleteTargetTcpProxyRequest request =
           DeleteTargetTcpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetTcpProxy("targetTcpProxy-337144898")
               .build();
       ApiFuture<Operation> future = targetTcpProxiesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTargetTcpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteTargetTcpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteTargetTcpProxyRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified TargetTcpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       DeleteTargetTcpProxyRequest request =
           DeleteTargetTcpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetTcpProxy("targetTcpProxy-337144898")
               .build();
       OperationFuture<Operation, Operation> future =
           targetTcpProxiesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTargetTcpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteTargetTcpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetTargetTcpProxyRequest request)
    
    
    public final TargetTcpProxy get(GetTargetTcpProxyRequest request)

Returns the specified TargetTcpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       GetTargetTcpProxyRequest request =
           GetTargetTcpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setTargetTcpProxy("targetTcpProxy-337144898")
               .build();
       TargetTcpProxy response = targetTcpProxiesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTargetTcpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetTargetTcpProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetTcpProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxy)` |   
  
### get(String project, String targetTcpProxy)
    
    
    public final TargetTcpProxy get(String project, String targetTcpProxy)

Returns the specified TargetTcpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       String project = "project-309310695";
       String targetTcpProxy = "targetTcpProxy-337144898";
       TargetTcpProxy response = targetTcpProxiesClient.get(project, targetTcpProxy);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetTcpProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetTcpProxy resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[TargetTcpProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxy)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetTargetTcpProxyRequest,TargetTcpProxy> getCallable()

Returns the specified TargetTcpProxy resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       GetTargetTcpProxyRequest request =
           GetTargetTcpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setTargetTcpProxy("targetTcpProxy-337144898")
               .build();
       ApiFuture<TargetTcpProxy> future = targetTcpProxiesClient.getCallable().futureCall(request);
       // Do something.
       TargetTcpProxy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTargetTcpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetTargetTcpProxyRequest),[TargetTcpProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxy)>` |   
  
### getSettings()
    
    
    public final @Nullable TargetTcpProxiesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.TargetTcpProxiesSettings` |   
  
### getStub()
    
    
    public TargetTcpProxiesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[TargetTcpProxiesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.TargetTcpProxiesStub)` |   
  
### insertAsync(InsertTargetTcpProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertTargetTcpProxyRequest request)

Creates a TargetTcpProxy resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       InsertTargetTcpProxyRequest request =
           InsertTargetTcpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetTcpProxyResource(TargetTcpProxy.newBuilder().build())
               .build();
       Operation response = targetTcpProxiesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertTargetTcpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertTargetTcpProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, TargetTcpProxy targetTcpProxyResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, TargetTcpProxy targetTcpProxyResource)

Creates a TargetTcpProxy resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       String project = "project-309310695";
       TargetTcpProxy targetTcpProxyResource = TargetTcpProxy.newBuilder().build();
       Operation response =
           targetTcpProxiesClient.insertAsync(project, targetTcpProxyResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetTcpProxyResource` | `[TargetTcpProxy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertTargetTcpProxyRequest,Operation> insertCallable()

Creates a TargetTcpProxy resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       InsertTargetTcpProxyRequest request =
           InsertTargetTcpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetTcpProxyResource(TargetTcpProxy.newBuilder().build())
               .build();
       ApiFuture<Operation> future = targetTcpProxiesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertTargetTcpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertTargetTcpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertTargetTcpProxyRequest,Operation,Operation> insertOperationCallable()

Creates a TargetTcpProxy resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       InsertTargetTcpProxyRequest request =
           InsertTargetTcpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetTcpProxyResource(TargetTcpProxy.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           targetTcpProxiesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertTargetTcpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertTargetTcpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListTargetTcpProxiesRequest request)
    
    
    public final TargetTcpProxiesClient.ListPagedResponse list(ListTargetTcpProxiesRequest request)

Retrieves the list of TargetTcpProxy resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       ListTargetTcpProxiesRequest request =
           ListTargetTcpProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (TargetTcpProxy element : targetTcpProxiesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTargetTcpProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListTargetTcpProxiesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TargetTcpProxiesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxiesClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final TargetTcpProxiesClient.ListPagedResponse list(String project)

Retrieves the list of TargetTcpProxy resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       String project = "project-309310695";
       for (TargetTcpProxy element : targetTcpProxiesClient.list(project).iterateAll()) {
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
`[TargetTcpProxiesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxiesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListTargetTcpProxiesRequest,TargetTcpProxyList> listCallable()

Retrieves the list of TargetTcpProxy resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       ListTargetTcpProxiesRequest request =
           ListTargetTcpProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         TargetTcpProxyList response = targetTcpProxiesClient.listCallable().call(request);
         for (TargetTcpProxy element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTargetTcpProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListTargetTcpProxiesRequest),[TargetTcpProxyList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxyList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListTargetTcpProxiesRequest,TargetTcpProxiesClient.ListPagedResponse> listPagedCallable()

Retrieves the list of TargetTcpProxy resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       ListTargetTcpProxiesRequest request =
           ListTargetTcpProxiesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<TargetTcpProxy> future =
           targetTcpProxiesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (TargetTcpProxy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTargetTcpProxiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListTargetTcpProxiesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxiesClient.ListPagedResponse)>` |   
  
### setBackendServiceAsync(SetBackendServiceTargetTcpProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> setBackendServiceAsync(SetBackendServiceTargetTcpProxyRequest request)

Changes the BackendService for TargetTcpProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       SetBackendServiceTargetTcpProxyRequest request =
           SetBackendServiceTargetTcpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetTcpProxiesSetBackendServiceRequestResource(
                   TargetTcpProxiesSetBackendServiceRequest.newBuilder().build())
               .setTargetTcpProxy("targetTcpProxy-337144898")
               .build();
       Operation response = targetTcpProxiesClient.setBackendServiceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetBackendServiceTargetTcpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetBackendServiceTargetTcpProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setBackendServiceAsync(String project, String targetTcpProxy, TargetTcpProxiesSetBackendServiceRequest targetTcpProxiesSetBackendServiceRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setBackendServiceAsync(String project, String targetTcpProxy, TargetTcpProxiesSetBackendServiceRequest targetTcpProxiesSetBackendServiceRequestResource)

Changes the BackendService for TargetTcpProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       String project = "project-309310695";
       String targetTcpProxy = "targetTcpProxy-337144898";
       TargetTcpProxiesSetBackendServiceRequest targetTcpProxiesSetBackendServiceRequestResource =
           TargetTcpProxiesSetBackendServiceRequest.newBuilder().build();
       Operation response =
           targetTcpProxiesClient
               .setBackendServiceAsync(
                   project, targetTcpProxy, targetTcpProxiesSetBackendServiceRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetTcpProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetTcpProxy resource whose BackendService resource is to be set.  
`targetTcpProxiesSetBackendServiceRequestResource` | `[TargetTcpProxiesSetBackendServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxiesSetBackendServiceRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setBackendServiceCallable()
    
    
    public final UnaryCallable<SetBackendServiceTargetTcpProxyRequest,Operation> setBackendServiceCallable()

Changes the BackendService for TargetTcpProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       SetBackendServiceTargetTcpProxyRequest request =
           SetBackendServiceTargetTcpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetTcpProxiesSetBackendServiceRequestResource(
                   TargetTcpProxiesSetBackendServiceRequest.newBuilder().build())
               .setTargetTcpProxy("targetTcpProxy-337144898")
               .build();
       ApiFuture<Operation> future =
           targetTcpProxiesClient.setBackendServiceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetBackendServiceTargetTcpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetBackendServiceTargetTcpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setBackendServiceOperationCallable()
    
    
    public final OperationCallable<SetBackendServiceTargetTcpProxyRequest,Operation,Operation> setBackendServiceOperationCallable()

Changes the BackendService for TargetTcpProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       SetBackendServiceTargetTcpProxyRequest request =
           SetBackendServiceTargetTcpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetTcpProxiesSetBackendServiceRequestResource(
                   TargetTcpProxiesSetBackendServiceRequest.newBuilder().build())
               .setTargetTcpProxy("targetTcpProxy-337144898")
               .build();
       OperationFuture<Operation, Operation> future =
           targetTcpProxiesClient.setBackendServiceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetBackendServiceTargetTcpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetBackendServiceTargetTcpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setProxyHeaderAsync(SetProxyHeaderTargetTcpProxyRequest request)
    
    
    public final OperationFuture<Operation,Operation> setProxyHeaderAsync(SetProxyHeaderTargetTcpProxyRequest request)

Changes the ProxyHeaderType for TargetTcpProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       SetProxyHeaderTargetTcpProxyRequest request =
           SetProxyHeaderTargetTcpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetTcpProxiesSetProxyHeaderRequestResource(
                   TargetTcpProxiesSetProxyHeaderRequest.newBuilder().build())
               .setTargetTcpProxy("targetTcpProxy-337144898")
               .build();
       Operation response = targetTcpProxiesClient.setProxyHeaderAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetProxyHeaderTargetTcpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetProxyHeaderTargetTcpProxyRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setProxyHeaderAsync(String project, String targetTcpProxy, TargetTcpProxiesSetProxyHeaderRequest targetTcpProxiesSetProxyHeaderRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setProxyHeaderAsync(String project, String targetTcpProxy, TargetTcpProxiesSetProxyHeaderRequest targetTcpProxiesSetProxyHeaderRequestResource)

Changes the ProxyHeaderType for TargetTcpProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       String project = "project-309310695";
       String targetTcpProxy = "targetTcpProxy-337144898";
       TargetTcpProxiesSetProxyHeaderRequest targetTcpProxiesSetProxyHeaderRequestResource =
           TargetTcpProxiesSetProxyHeaderRequest.newBuilder().build();
       Operation response =
           targetTcpProxiesClient
               .setProxyHeaderAsync(
                   project, targetTcpProxy, targetTcpProxiesSetProxyHeaderRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`targetTcpProxy` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the TargetTcpProxy resource whose ProxyHeader is to be set.  
`targetTcpProxiesSetProxyHeaderRequestResource` | `[TargetTcpProxiesSetProxyHeaderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TargetTcpProxiesSetProxyHeaderRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setProxyHeaderCallable()
    
    
    public final UnaryCallable<SetProxyHeaderTargetTcpProxyRequest,Operation> setProxyHeaderCallable()

Changes the ProxyHeaderType for TargetTcpProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       SetProxyHeaderTargetTcpProxyRequest request =
           SetProxyHeaderTargetTcpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetTcpProxiesSetProxyHeaderRequestResource(
                   TargetTcpProxiesSetProxyHeaderRequest.newBuilder().build())
               .setTargetTcpProxy("targetTcpProxy-337144898")
               .build();
       ApiFuture<Operation> future =
           targetTcpProxiesClient.setProxyHeaderCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetProxyHeaderTargetTcpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetProxyHeaderTargetTcpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setProxyHeaderOperationCallable()
    
    
    public final OperationCallable<SetProxyHeaderTargetTcpProxyRequest,Operation,Operation> setProxyHeaderOperationCallable()

Changes the ProxyHeaderType for TargetTcpProxy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       SetProxyHeaderTargetTcpProxyRequest request =
           SetProxyHeaderTargetTcpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setTargetTcpProxiesSetProxyHeaderRequestResource(
                   TargetTcpProxiesSetProxyHeaderRequest.newBuilder().build())
               .setTargetTcpProxy("targetTcpProxy-337144898")
               .build();
       OperationFuture<Operation, Operation> future =
           targetTcpProxiesClient.setProxyHeaderOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetProxyHeaderTargetTcpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetProxyHeaderTargetTcpProxyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsTargetTcpProxyRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsTargetTcpProxyRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       TestIamPermissionsTargetTcpProxyRequest request =
           TestIamPermissionsTargetTcpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = targetTcpProxiesClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsTargetTcpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsTargetTcpProxyRequest)`  
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
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           targetTcpProxiesClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsTargetTcpProxyRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (TargetTcpProxiesClient targetTcpProxiesClient = TargetTcpProxiesClient.create()) {
       TestIamPermissionsTargetTcpProxyRequest request =
           TestIamPermissionsTargetTcpProxyRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           targetTcpProxiesClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsTargetTcpProxyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsTargetTcpProxyRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
