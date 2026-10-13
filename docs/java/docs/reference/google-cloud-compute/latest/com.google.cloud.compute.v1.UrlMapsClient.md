---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsClient
title: Class UrlMapsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:43.418086+00:00
---

# Class UrlMapsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class UrlMapsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/UrlMapsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The UrlMaps API.

This client uses UrlMaps version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       String project = "project-309310695";
       String urlMap = "urlMap-836780691";
       UrlMap response = urlMapsClient.get(project, urlMap);
     }
     

Note: close() needs to be called on the UrlMapsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves the list of all UrlMap resources, regional and global, available to the specified project.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListUrlMapsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified UrlMap resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteUrlMapRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String urlMap) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified UrlMap resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetUrlMapRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String urlMap) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a UrlMap resource in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertUrlMapRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, UrlMap urlMapResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
InvalidateCache |  Initiates a cache invalidation operation, invalidating the specified path, scoped to the specified UrlMap.  For more information, see [Invalidating cached content](https://docs.cloud.google.com/cdn/docs/invalidating-cached-content). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * invalidateCacheAsync(InvalidateCacheUrlMapRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * invalidateCacheAsync(String project, String urlMap, CacheInvalidationRule cacheInvalidationRuleResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * invalidateCacheOperationCallable() 
  * invalidateCacheCallable() 

  
List |  Retrieves the list of UrlMap resources available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListUrlMapsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Patches the specified UrlMap resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchUrlMapRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String urlMap, UrlMap urlMapResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsUrlMapRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
Update |  Updates the specified UrlMap resource with the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAsync(UpdateUrlMapRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAsync(String project, String urlMap, UrlMap urlMapResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOperationCallable() 
  * updateCallable() 

  
Validate |  Runs static validation for the UrlMap. In particular, the tests of the provided UrlMap will be run. Calling this method does NOT create the UrlMap. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * validate(ValidateUrlMapRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * validate(String project, String urlMap, UrlMapsValidateRequest urlMapsValidateRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * validateCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of UrlMapsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     UrlMapsSettings urlMapsSettings =
         UrlMapsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     UrlMapsClient urlMapsClient = UrlMapsClient.create(urlMapsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     UrlMapsSettings urlMapsSettings = UrlMapsSettings.newBuilder().setEndpoint(myEndpoint).build();
     UrlMapsClient urlMapsClient = UrlMapsClient.create(urlMapsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > UrlMapsClient

## Static Methods 

### create()
    
    
    public static final UrlMapsClient create()

Constructs an instance of UrlMapsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[UrlMapsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(UrlMapsSettings settings)
    
    
    public static final UrlMapsClient create(UrlMapsSettings settings)

Constructs an instance of UrlMapsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[UrlMapsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UrlMapsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(UrlMapsStub stub)
    
    
    public static final UrlMapsClient create(UrlMapsStub stub)

Constructs an instance of UrlMapsClient, using the given stub for making calls. This is for advanced usage - prefer using create(UrlMapsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[UrlMapsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.UrlMapsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UrlMapsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsClient)` |   
  
## Constructors 

### UrlMapsClient(UrlMapsSettings settings)
    
    
    protected UrlMapsClient(UrlMapsSettings settings)

Constructs an instance of UrlMapsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[UrlMapsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsSettings)`  
  
  
### UrlMapsClient(UrlMapsStub stub)
    
    
    protected UrlMapsClient(UrlMapsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[UrlMapsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.UrlMapsStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListUrlMapsRequest request)
    
    
    public final UrlMapsClient.AggregatedListPagedResponse aggregatedList(AggregatedListUrlMapsRequest request)

Retrieves the list of all UrlMap resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       AggregatedListUrlMapsRequest request =
           AggregatedListUrlMapsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, UrlMapsScopedList> element :
           urlMapsClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListUrlMapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListUrlMapsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UrlMapsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final UrlMapsClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves the list of all UrlMap resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, UrlMapsScopedList> element :
           urlMapsClient.aggregatedList(project).iterateAll()) {
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
`[UrlMapsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListUrlMapsRequest,UrlMapsAggregatedList> aggregatedListCallable()

Retrieves the list of all UrlMap resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       AggregatedListUrlMapsRequest request =
           AggregatedListUrlMapsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         UrlMapsAggregatedList response = urlMapsClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, UrlMapsScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListUrlMapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListUrlMapsRequest),[UrlMapsAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListUrlMapsRequest,UrlMapsClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves the list of all UrlMap resources, regional and global, available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       AggregatedListUrlMapsRequest request =
           AggregatedListUrlMapsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, UrlMapsScopedList>> future =
           urlMapsClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, UrlMapsScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListUrlMapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListUrlMapsRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteUrlMapRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteUrlMapRequest request)

Deletes the specified UrlMap resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       DeleteUrlMapRequest request =
           DeleteUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUrlMap("urlMap-836780691")
               .build();
       Operation response = urlMapsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteUrlMapRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String urlMap)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String urlMap)

Deletes the specified UrlMap resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       String project = "project-309310695";
       String urlMap = "urlMap-836780691";
       Operation response = urlMapsClient.deleteAsync(project, urlMap).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`urlMap` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the UrlMap resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteUrlMapRequest,Operation> deleteCallable()

Deletes the specified UrlMap resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       DeleteUrlMapRequest request =
           DeleteUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUrlMap("urlMap-836780691")
               .build();
       ApiFuture<Operation> future = urlMapsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteUrlMapRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteUrlMapRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified UrlMap resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       DeleteUrlMapRequest request =
           DeleteUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUrlMap("urlMap-836780691")
               .build();
       OperationFuture<Operation, Operation> future =
           urlMapsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteUrlMapRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetUrlMapRequest request)
    
    
    public final UrlMap get(GetUrlMapRequest request)

Returns the specified UrlMap resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       GetUrlMapRequest request =
           GetUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setUrlMap("urlMap-836780691")
               .build();
       UrlMap response = urlMapsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetUrlMapRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UrlMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMap)` |   
  
### get(String project, String urlMap)
    
    
    public final UrlMap get(String project, String urlMap)

Returns the specified UrlMap resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       String project = "project-309310695";
       String urlMap = "urlMap-836780691";
       UrlMap response = urlMapsClient.get(project, urlMap);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`urlMap` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the UrlMap resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[UrlMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMap)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetUrlMapRequest,UrlMap> getCallable()

Returns the specified UrlMap resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       GetUrlMapRequest request =
           GetUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setUrlMap("urlMap-836780691")
               .build();
       ApiFuture<UrlMap> future = urlMapsClient.getCallable().futureCall(request);
       // Do something.
       UrlMap response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetUrlMapRequest),[UrlMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMap)>` |   
  
### getSettings()
    
    
    public final @Nullable UrlMapsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.UrlMapsSettings` |   
  
### getStub()
    
    
    public UrlMapsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[UrlMapsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.UrlMapsStub)` |   
  
### insertAsync(InsertUrlMapRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertUrlMapRequest request)

Creates a UrlMap resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       InsertUrlMapRequest request =
           InsertUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUrlMapResource(UrlMap.newBuilder().build())
               .build();
       Operation response = urlMapsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertUrlMapRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, UrlMap urlMapResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, UrlMap urlMapResource)

Creates a UrlMap resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       String project = "project-309310695";
       UrlMap urlMapResource = UrlMap.newBuilder().build();
       Operation response = urlMapsClient.insertAsync(project, urlMapResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`urlMapResource` | `[UrlMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMap)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertUrlMapRequest,Operation> insertCallable()

Creates a UrlMap resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       InsertUrlMapRequest request =
           InsertUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUrlMapResource(UrlMap.newBuilder().build())
               .build();
       ApiFuture<Operation> future = urlMapsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertUrlMapRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertUrlMapRequest,Operation,Operation> insertOperationCallable()

Creates a UrlMap resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       InsertUrlMapRequest request =
           InsertUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUrlMapResource(UrlMap.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           urlMapsClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertUrlMapRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### invalidateCacheAsync(InvalidateCacheUrlMapRequest request)
    
    
    public final OperationFuture<Operation,Operation> invalidateCacheAsync(InvalidateCacheUrlMapRequest request)

Initiates a cache invalidation operation, invalidating the specified path, scoped to the specified UrlMap.

For more information, see [Invalidating cached content](https://docs.cloud.google.com/cdn/docs/invalidating-cached-content).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       InvalidateCacheUrlMapRequest request =
           InvalidateCacheUrlMapRequest.newBuilder()
               .setCacheInvalidationRuleResource(CacheInvalidationRule.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUrlMap("urlMap-836780691")
               .build();
       Operation response = urlMapsClient.invalidateCacheAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InvalidateCacheUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InvalidateCacheUrlMapRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### invalidateCacheAsync(String project, String urlMap, CacheInvalidationRule cacheInvalidationRuleResource)
    
    
    public final OperationFuture<Operation,Operation> invalidateCacheAsync(String project, String urlMap, CacheInvalidationRule cacheInvalidationRuleResource)

Initiates a cache invalidation operation, invalidating the specified path, scoped to the specified UrlMap.

For more information, see [Invalidating cached content](https://docs.cloud.google.com/cdn/docs/invalidating-cached-content).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       String project = "project-309310695";
       String urlMap = "urlMap-836780691";
       CacheInvalidationRule cacheInvalidationRuleResource =
           CacheInvalidationRule.newBuilder().build();
       Operation response =
           urlMapsClient.invalidateCacheAsync(project, urlMap, cacheInvalidationRuleResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`urlMap` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the UrlMap scoping this request.  
`cacheInvalidationRuleResource` | `[CacheInvalidationRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CacheInvalidationRule)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### invalidateCacheCallable()
    
    
    public final UnaryCallable<InvalidateCacheUrlMapRequest,Operation> invalidateCacheCallable()

Initiates a cache invalidation operation, invalidating the specified path, scoped to the specified UrlMap.

For more information, see [Invalidating cached content](https://docs.cloud.google.com/cdn/docs/invalidating-cached-content).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       InvalidateCacheUrlMapRequest request =
           InvalidateCacheUrlMapRequest.newBuilder()
               .setCacheInvalidationRuleResource(CacheInvalidationRule.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUrlMap("urlMap-836780691")
               .build();
       ApiFuture<Operation> future = urlMapsClient.invalidateCacheCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InvalidateCacheUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InvalidateCacheUrlMapRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### invalidateCacheOperationCallable()
    
    
    public final OperationCallable<InvalidateCacheUrlMapRequest,Operation,Operation> invalidateCacheOperationCallable()

Initiates a cache invalidation operation, invalidating the specified path, scoped to the specified UrlMap.

For more information, see [Invalidating cached content](https://docs.cloud.google.com/cdn/docs/invalidating-cached-content).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       InvalidateCacheUrlMapRequest request =
           InvalidateCacheUrlMapRequest.newBuilder()
               .setCacheInvalidationRuleResource(CacheInvalidationRule.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUrlMap("urlMap-836780691")
               .build();
       OperationFuture<Operation, Operation> future =
           urlMapsClient.invalidateCacheOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InvalidateCacheUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InvalidateCacheUrlMapRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListUrlMapsRequest request)
    
    
    public final UrlMapsClient.ListPagedResponse list(ListUrlMapsRequest request)

Retrieves the list of UrlMap resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       ListUrlMapsRequest request =
           ListUrlMapsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (UrlMap element : urlMapsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUrlMapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListUrlMapsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UrlMapsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final UrlMapsClient.ListPagedResponse list(String project)

Retrieves the list of UrlMap resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       String project = "project-309310695";
       for (UrlMap element : urlMapsClient.list(project).iterateAll()) {
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
`[UrlMapsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListUrlMapsRequest,UrlMapList> listCallable()

Retrieves the list of UrlMap resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       ListUrlMapsRequest request =
           ListUrlMapsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         UrlMapList response = urlMapsClient.listCallable().call(request);
         for (UrlMap element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUrlMapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListUrlMapsRequest),[UrlMapList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListUrlMapsRequest,UrlMapsClient.ListPagedResponse> listPagedCallable()

Retrieves the list of UrlMap resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       ListUrlMapsRequest request =
           ListUrlMapsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<UrlMap> future = urlMapsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (UrlMap element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListUrlMapsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListUrlMapsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsClient.ListPagedResponse)>` |   
  
### patchAsync(PatchUrlMapRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchUrlMapRequest request)

Patches the specified UrlMap resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       PatchUrlMapRequest request =
           PatchUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUrlMap("urlMap-836780691")
               .setUrlMapResource(UrlMap.newBuilder().build())
               .build();
       Operation response = urlMapsClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchUrlMapRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String urlMap, UrlMap urlMapResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String urlMap, UrlMap urlMapResource)

Patches the specified UrlMap resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       String project = "project-309310695";
       String urlMap = "urlMap-836780691";
       UrlMap urlMapResource = UrlMap.newBuilder().build();
       Operation response = urlMapsClient.patchAsync(project, urlMap, urlMapResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`urlMap` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the UrlMap resource to patch.  
`urlMapResource` | `[UrlMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMap)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchUrlMapRequest,Operation> patchCallable()

Patches the specified UrlMap resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       PatchUrlMapRequest request =
           PatchUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUrlMap("urlMap-836780691")
               .setUrlMapResource(UrlMap.newBuilder().build())
               .build();
       ApiFuture<Operation> future = urlMapsClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchUrlMapRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchUrlMapRequest,Operation,Operation> patchOperationCallable()

Patches the specified UrlMap resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       PatchUrlMapRequest request =
           PatchUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUrlMap("urlMap-836780691")
               .setUrlMapResource(UrlMap.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           urlMapsClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchUrlMapRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsUrlMapRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsUrlMapRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       TestIamPermissionsUrlMapRequest request =
           TestIamPermissionsUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = urlMapsClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsUrlMapRequest)`  
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
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           urlMapsClient.testIamPermissions(project, resource, testPermissionsRequestResource);
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
    
    
    public final UnaryCallable<TestIamPermissionsUrlMapRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       TestIamPermissionsUrlMapRequest request =
           TestIamPermissionsUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           urlMapsClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsUrlMapRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
### updateAsync(UpdateUrlMapRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(UpdateUrlMapRequest request)

Updates the specified UrlMap resource with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       UpdateUrlMapRequest request =
           UpdateUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUrlMap("urlMap-836780691")
               .setUrlMapResource(UrlMap.newBuilder().build())
               .build();
       Operation response = urlMapsClient.updateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateUrlMapRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(String project, String urlMap, UrlMap urlMapResource)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(String project, String urlMap, UrlMap urlMapResource)

Updates the specified UrlMap resource with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       String project = "project-309310695";
       String urlMap = "urlMap-836780691";
       UrlMap urlMapResource = UrlMap.newBuilder().build();
       Operation response = urlMapsClient.updateAsync(project, urlMap, urlMapResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`urlMap` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the UrlMap resource to update.  
`urlMapResource` | `[UrlMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMap)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateCallable()
    
    
    public final UnaryCallable<UpdateUrlMapRequest,Operation> updateCallable()

Updates the specified UrlMap resource with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       UpdateUrlMapRequest request =
           UpdateUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUrlMap("urlMap-836780691")
               .setUrlMapResource(UrlMap.newBuilder().build())
               .build();
       ApiFuture<Operation> future = urlMapsClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateUrlMapRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationCallable()
    
    
    public final OperationCallable<UpdateUrlMapRequest,Operation,Operation> updateOperationCallable()

Updates the specified UrlMap resource with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       UpdateUrlMapRequest request =
           UpdateUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUrlMap("urlMap-836780691")
               .setUrlMapResource(UrlMap.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           urlMapsClient.updateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateUrlMapRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### validate(ValidateUrlMapRequest request)
    
    
    public final UrlMapsValidateResponse validate(ValidateUrlMapRequest request)

Runs static validation for the UrlMap. In particular, the tests of the provided UrlMap will be run. Calling this method does NOT create the UrlMap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       ValidateUrlMapRequest request =
           ValidateUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setUrlMap("urlMap-836780691")
               .setUrlMapsValidateRequestResource(UrlMapsValidateRequest.newBuilder().build())
               .build();
       UrlMapsValidateResponse response = urlMapsClient.validate(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ValidateUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ValidateUrlMapRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UrlMapsValidateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsValidateResponse)` |   
  
### validate(String project, String urlMap, UrlMapsValidateRequest urlMapsValidateRequestResource)
    
    
    public final UrlMapsValidateResponse validate(String project, String urlMap, UrlMapsValidateRequest urlMapsValidateRequestResource)

Runs static validation for the UrlMap. In particular, the tests of the provided UrlMap will be run. Calling this method does NOT create the UrlMap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       String project = "project-309310695";
       String urlMap = "urlMap-836780691";
       UrlMapsValidateRequest urlMapsValidateRequestResource =
           UrlMapsValidateRequest.newBuilder().build();
       UrlMapsValidateResponse response =
           urlMapsClient.validate(project, urlMap, urlMapsValidateRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`urlMap` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the UrlMap resource to be validated as.  
`urlMapsValidateRequestResource` | `[UrlMapsValidateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsValidateRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[UrlMapsValidateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsValidateResponse)` |   
  
### validateCallable()
    
    
    public final UnaryCallable<ValidateUrlMapRequest,UrlMapsValidateResponse> validateCallable()

Runs static validation for the UrlMap. In particular, the tests of the provided UrlMap will be run. Calling this method does NOT create the UrlMap.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (UrlMapsClient urlMapsClient = UrlMapsClient.create()) {
       ValidateUrlMapRequest request =
           ValidateUrlMapRequest.newBuilder()
               .setProject("project-309310695")
               .setUrlMap("urlMap-836780691")
               .setUrlMapsValidateRequestResource(UrlMapsValidateRequest.newBuilder().build())
               .build();
       ApiFuture<UrlMapsValidateResponse> future =
           urlMapsClient.validateCallable().futureCall(request);
       // Do something.
       UrlMapsValidateResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ValidateUrlMapRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ValidateUrlMapRequest),[UrlMapsValidateResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UrlMapsValidateResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
