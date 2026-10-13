---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionCompositeHealthChecksClient
title: Class RegionCompositeHealthChecksClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:30.642876+00:00
---

# Class RegionCompositeHealthChecksClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionCompositeHealthChecksClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionCompositeHealthChecksClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RegionCompositeHealthChecksClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RegionCompositeHealthChecks API.

This client uses RegionCompositeHealthChecks version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String compositeHealthCheck = "compositeHealthCheck-1727645947";
       CompositeHealthCheck response =
           regionCompositeHealthChecksClient.get(project, region, compositeHealthCheck);
     }
     

Note: close() needs to be called on the RegionCompositeHealthChecksClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves the list of all CompositeHealthCheck resources (all regional) available to the specified project.  To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListRegionCompositeHealthChecksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified CompositeHealthCheck in the given region |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRegionCompositeHealthCheckRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String compositeHealthCheck) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified CompositeHealthCheck resource in the given region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRegionCompositeHealthCheckRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String compositeHealthCheck) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetHealth |  Gets the most recent health check results for this regional CompositeHealthCheck. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getHealth(GetHealthRegionCompositeHealthCheckRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getHealth(String project, String region, String compositeHealthCheck) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getHealthCallable() 

  
Insert |  Create a CompositeHealthCheck in the specified project in the given region using the parameters that are included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRegionCompositeHealthCheckRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, CompositeHealthCheck compositeHealthCheckResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists the CompositeHealthChecks for a project in the given region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRegionCompositeHealthChecksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Updates the specified regional CompositeHealthCheck resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchRegionCompositeHealthCheckRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String region, String compositeHealthCheck, CompositeHealthCheck compositeHealthCheckResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRegionCompositeHealthCheckRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionCompositeHealthChecksSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionCompositeHealthChecksSettings regionCompositeHealthChecksSettings =
         RegionCompositeHealthChecksSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create(regionCompositeHealthChecksSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionCompositeHealthChecksSettings regionCompositeHealthChecksSettings =
         RegionCompositeHealthChecksSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create(regionCompositeHealthChecksSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionCompositeHealthChecksClient

## Static Methods 

### create()
    
    
    public static final RegionCompositeHealthChecksClient create()

Constructs an instance of RegionCompositeHealthChecksClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionCompositeHealthChecksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionCompositeHealthChecksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionCompositeHealthChecksSettings settings)
    
    
    public static final RegionCompositeHealthChecksClient create(RegionCompositeHealthChecksSettings settings)

Constructs an instance of RegionCompositeHealthChecksClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionCompositeHealthChecksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionCompositeHealthChecksSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionCompositeHealthChecksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionCompositeHealthChecksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionCompositeHealthChecksStub stub)
    
    
    public static final RegionCompositeHealthChecksClient create(RegionCompositeHealthChecksStub stub)

Constructs an instance of RegionCompositeHealthChecksClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionCompositeHealthChecksSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionCompositeHealthChecksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionCompositeHealthChecksStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionCompositeHealthChecksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionCompositeHealthChecksClient)` |   
  
## Constructors 

### RegionCompositeHealthChecksClient(RegionCompositeHealthChecksSettings settings)
    
    
    protected RegionCompositeHealthChecksClient(RegionCompositeHealthChecksSettings settings)

Constructs an instance of RegionCompositeHealthChecksClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionCompositeHealthChecksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionCompositeHealthChecksSettings)`  
  
  
### RegionCompositeHealthChecksClient(RegionCompositeHealthChecksStub stub)
    
    
    protected RegionCompositeHealthChecksClient(RegionCompositeHealthChecksStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionCompositeHealthChecksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionCompositeHealthChecksStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListRegionCompositeHealthChecksRequest request)
    
    
    public final RegionCompositeHealthChecksClient.AggregatedListPagedResponse aggregatedList(AggregatedListRegionCompositeHealthChecksRequest request)

Retrieves the list of all CompositeHealthCheck resources (all regional) available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       AggregatedListRegionCompositeHealthChecksRequest request =
           AggregatedListRegionCompositeHealthChecksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, CompositeHealthChecksScopedList> element :
           regionCompositeHealthChecksClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListRegionCompositeHealthChecksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListRegionCompositeHealthChecksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionCompositeHealthChecksClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionCompositeHealthChecksClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final RegionCompositeHealthChecksClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves the list of all CompositeHealthCheck resources (all regional) available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, CompositeHealthChecksScopedList> element :
           regionCompositeHealthChecksClient.aggregatedList(project).iterateAll()) {
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
`[RegionCompositeHealthChecksClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionCompositeHealthChecksClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListRegionCompositeHealthChecksRequest,CompositeHealthCheckAggregatedList> aggregatedListCallable()

Retrieves the list of all CompositeHealthCheck resources (all regional) available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       AggregatedListRegionCompositeHealthChecksRequest request =
           AggregatedListRegionCompositeHealthChecksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         CompositeHealthCheckAggregatedList response =
             regionCompositeHealthChecksClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, CompositeHealthChecksScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListRegionCompositeHealthChecksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListRegionCompositeHealthChecksRequest),[CompositeHealthCheckAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CompositeHealthCheckAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListRegionCompositeHealthChecksRequest,RegionCompositeHealthChecksClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves the list of all CompositeHealthCheck resources (all regional) available to the specified project.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       AggregatedListRegionCompositeHealthChecksRequest request =
           AggregatedListRegionCompositeHealthChecksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, CompositeHealthChecksScopedList>> future =
           regionCompositeHealthChecksClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, CompositeHealthChecksScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListRegionCompositeHealthChecksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListRegionCompositeHealthChecksRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionCompositeHealthChecksClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteRegionCompositeHealthCheckRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRegionCompositeHealthCheckRequest request)

Deletes the specified CompositeHealthCheck in the given region

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       DeleteRegionCompositeHealthCheckRequest request =
           DeleteRegionCompositeHealthCheckRequest.newBuilder()
               .setCompositeHealthCheck("compositeHealthCheck-1727645947")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionCompositeHealthChecksClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionCompositeHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionCompositeHealthCheckRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String compositeHealthCheck)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String compositeHealthCheck)

Deletes the specified CompositeHealthCheck in the given region

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String compositeHealthCheck = "compositeHealthCheck-1727645947";
       Operation response =
           regionCompositeHealthChecksClient
               .deleteAsync(project, region, compositeHealthCheck)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`compositeHealthCheck` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the CompositeHealthCheck resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRegionCompositeHealthCheckRequest,Operation> deleteCallable()

Deletes the specified CompositeHealthCheck in the given region

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       DeleteRegionCompositeHealthCheckRequest request =
           DeleteRegionCompositeHealthCheckRequest.newBuilder()
               .setCompositeHealthCheck("compositeHealthCheck-1727645947")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionCompositeHealthChecksClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionCompositeHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionCompositeHealthCheckRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRegionCompositeHealthCheckRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified CompositeHealthCheck in the given region

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       DeleteRegionCompositeHealthCheckRequest request =
           DeleteRegionCompositeHealthCheckRequest.newBuilder()
               .setCompositeHealthCheck("compositeHealthCheck-1727645947")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionCompositeHealthChecksClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRegionCompositeHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionCompositeHealthCheckRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRegionCompositeHealthCheckRequest request)
    
    
    public final CompositeHealthCheck get(GetRegionCompositeHealthCheckRequest request)

Returns the specified CompositeHealthCheck resource in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       GetRegionCompositeHealthCheckRequest request =
           GetRegionCompositeHealthCheckRequest.newBuilder()
               .setCompositeHealthCheck("compositeHealthCheck-1727645947")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       CompositeHealthCheck response = regionCompositeHealthChecksClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegionCompositeHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionCompositeHealthCheckRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CompositeHealthCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CompositeHealthCheck)` |   
  
### get(String project, String region, String compositeHealthCheck)
    
    
    public final CompositeHealthCheck get(String project, String region, String compositeHealthCheck)

Returns the specified CompositeHealthCheck resource in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String compositeHealthCheck = "compositeHealthCheck-1727645947";
       CompositeHealthCheck response =
           regionCompositeHealthChecksClient.get(project, region, compositeHealthCheck);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`compositeHealthCheck` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the CompositeHealthCheck resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[CompositeHealthCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CompositeHealthCheck)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRegionCompositeHealthCheckRequest,CompositeHealthCheck> getCallable()

Returns the specified CompositeHealthCheck resource in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       GetRegionCompositeHealthCheckRequest request =
           GetRegionCompositeHealthCheckRequest.newBuilder()
               .setCompositeHealthCheck("compositeHealthCheck-1727645947")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<CompositeHealthCheck> future =
           regionCompositeHealthChecksClient.getCallable().futureCall(request);
       // Do something.
       CompositeHealthCheck response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegionCompositeHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionCompositeHealthCheckRequest),[CompositeHealthCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CompositeHealthCheck)>` |   
  
### getHealth(GetHealthRegionCompositeHealthCheckRequest request)
    
    
    public final CompositeHealthCheckHealth getHealth(GetHealthRegionCompositeHealthCheckRequest request)

Gets the most recent health check results for this regional CompositeHealthCheck.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       GetHealthRegionCompositeHealthCheckRequest request =
           GetHealthRegionCompositeHealthCheckRequest.newBuilder()
               .setCompositeHealthCheck("compositeHealthCheck-1727645947")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       CompositeHealthCheckHealth response = regionCompositeHealthChecksClient.getHealth(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHealthRegionCompositeHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetHealthRegionCompositeHealthCheckRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CompositeHealthCheckHealth](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CompositeHealthCheckHealth)` |   
  
### getHealth(String project, String region, String compositeHealthCheck)
    
    
    public final CompositeHealthCheckHealth getHealth(String project, String region, String compositeHealthCheck)

Gets the most recent health check results for this regional CompositeHealthCheck.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String compositeHealthCheck = "compositeHealthCheck-1727645947";
       CompositeHealthCheckHealth response =
           regionCompositeHealthChecksClient.getHealth(project, region, compositeHealthCheck);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the project scoping this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`compositeHealthCheck` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the CompositeHealthCheck resource to get health for.  
**Returns**  
---  
**Type** | **Description**  
`[CompositeHealthCheckHealth](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CompositeHealthCheckHealth)` |   
  
### getHealthCallable()
    
    
    public final UnaryCallable<GetHealthRegionCompositeHealthCheckRequest,CompositeHealthCheckHealth> getHealthCallable()

Gets the most recent health check results for this regional CompositeHealthCheck.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       GetHealthRegionCompositeHealthCheckRequest request =
           GetHealthRegionCompositeHealthCheckRequest.newBuilder()
               .setCompositeHealthCheck("compositeHealthCheck-1727645947")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<CompositeHealthCheckHealth> future =
           regionCompositeHealthChecksClient.getHealthCallable().futureCall(request);
       // Do something.
       CompositeHealthCheckHealth response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetHealthRegionCompositeHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetHealthRegionCompositeHealthCheckRequest),[CompositeHealthCheckHealth](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CompositeHealthCheckHealth)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionCompositeHealthChecksSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RegionCompositeHealthChecksSettings` |   
  
### getStub()
    
    
    public RegionCompositeHealthChecksStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionCompositeHealthChecksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionCompositeHealthChecksStub)` |   
  
### insertAsync(InsertRegionCompositeHealthCheckRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRegionCompositeHealthCheckRequest request)

Create a CompositeHealthCheck in the specified project in the given region using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       InsertRegionCompositeHealthCheckRequest request =
           InsertRegionCompositeHealthCheckRequest.newBuilder()
               .setCompositeHealthCheckResource(CompositeHealthCheck.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionCompositeHealthChecksClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRegionCompositeHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionCompositeHealthCheckRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, CompositeHealthCheck compositeHealthCheckResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, CompositeHealthCheck compositeHealthCheckResource)

Create a CompositeHealthCheck in the specified project in the given region using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       CompositeHealthCheck compositeHealthCheckResource = CompositeHealthCheck.newBuilder().build();
       Operation response =
           regionCompositeHealthChecksClient
               .insertAsync(project, region, compositeHealthCheckResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`compositeHealthCheckResource` | `[CompositeHealthCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CompositeHealthCheck)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRegionCompositeHealthCheckRequest,Operation> insertCallable()

Create a CompositeHealthCheck in the specified project in the given region using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       InsertRegionCompositeHealthCheckRequest request =
           InsertRegionCompositeHealthCheckRequest.newBuilder()
               .setCompositeHealthCheckResource(CompositeHealthCheck.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionCompositeHealthChecksClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionCompositeHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionCompositeHealthCheckRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRegionCompositeHealthCheckRequest,Operation,Operation> insertOperationCallable()

Create a CompositeHealthCheck in the specified project in the given region using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       InsertRegionCompositeHealthCheckRequest request =
           InsertRegionCompositeHealthCheckRequest.newBuilder()
               .setCompositeHealthCheckResource(CompositeHealthCheck.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionCompositeHealthChecksClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRegionCompositeHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionCompositeHealthCheckRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRegionCompositeHealthChecksRequest request)
    
    
    public final RegionCompositeHealthChecksClient.ListPagedResponse list(ListRegionCompositeHealthChecksRequest request)

Lists the CompositeHealthChecks for a project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       ListRegionCompositeHealthChecksRequest request =
           ListRegionCompositeHealthChecksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (CompositeHealthCheck element :
           regionCompositeHealthChecksClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionCompositeHealthChecksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionCompositeHealthChecksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionCompositeHealthChecksClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionCompositeHealthChecksClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final RegionCompositeHealthChecksClient.ListPagedResponse list(String project, String region)

Lists the CompositeHealthChecks for a project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (CompositeHealthCheck element :
           regionCompositeHealthChecksClient.list(project, region).iterateAll()) {
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
`[RegionCompositeHealthChecksClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionCompositeHealthChecksClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRegionCompositeHealthChecksRequest,CompositeHealthCheckList> listCallable()

Lists the CompositeHealthChecks for a project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       ListRegionCompositeHealthChecksRequest request =
           ListRegionCompositeHealthChecksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         CompositeHealthCheckList response =
             regionCompositeHealthChecksClient.listCallable().call(request);
         for (CompositeHealthCheck element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionCompositeHealthChecksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionCompositeHealthChecksRequest),[CompositeHealthCheckList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CompositeHealthCheckList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRegionCompositeHealthChecksRequest,RegionCompositeHealthChecksClient.ListPagedResponse> listPagedCallable()

Lists the CompositeHealthChecks for a project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       ListRegionCompositeHealthChecksRequest request =
           ListRegionCompositeHealthChecksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<CompositeHealthCheck> future =
           regionCompositeHealthChecksClient.listPagedCallable().futureCall(request);
       // Do something.
       for (CompositeHealthCheck element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionCompositeHealthChecksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionCompositeHealthChecksRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionCompositeHealthChecksClient.ListPagedResponse)>` |   
  
### patchAsync(PatchRegionCompositeHealthCheckRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchRegionCompositeHealthCheckRequest request)

Updates the specified regional CompositeHealthCheck resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       PatchRegionCompositeHealthCheckRequest request =
           PatchRegionCompositeHealthCheckRequest.newBuilder()
               .setCompositeHealthCheck("compositeHealthCheck-1727645947")
               .setCompositeHealthCheckResource(CompositeHealthCheck.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionCompositeHealthChecksClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchRegionCompositeHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionCompositeHealthCheckRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String region, String compositeHealthCheck, CompositeHealthCheck compositeHealthCheckResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String region, String compositeHealthCheck, CompositeHealthCheck compositeHealthCheckResource)

Updates the specified regional CompositeHealthCheck resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String compositeHealthCheck = "compositeHealthCheck-1727645947";
       CompositeHealthCheck compositeHealthCheckResource = CompositeHealthCheck.newBuilder().build();
       Operation response =
           regionCompositeHealthChecksClient
               .patchAsync(project, region, compositeHealthCheck, compositeHealthCheckResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`compositeHealthCheck` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the CompositeHealthCheck to update. The name must be 1-63 characters long, and comply with RFC1035.  
`compositeHealthCheckResource` | `[CompositeHealthCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CompositeHealthCheck)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchRegionCompositeHealthCheckRequest,Operation> patchCallable()

Updates the specified regional CompositeHealthCheck resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       PatchRegionCompositeHealthCheckRequest request =
           PatchRegionCompositeHealthCheckRequest.newBuilder()
               .setCompositeHealthCheck("compositeHealthCheck-1727645947")
               .setCompositeHealthCheckResource(CompositeHealthCheck.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionCompositeHealthChecksClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchRegionCompositeHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionCompositeHealthCheckRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchRegionCompositeHealthCheckRequest,Operation,Operation> patchOperationCallable()

Updates the specified regional CompositeHealthCheck resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       PatchRegionCompositeHealthCheckRequest request =
           PatchRegionCompositeHealthCheckRequest.newBuilder()
               .setCompositeHealthCheck("compositeHealthCheck-1727645947")
               .setCompositeHealthCheckResource(CompositeHealthCheck.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionCompositeHealthChecksClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchRegionCompositeHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionCompositeHealthCheckRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRegionCompositeHealthCheckRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsRegionCompositeHealthCheckRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       TestIamPermissionsRegionCompositeHealthCheckRequest request =
           TestIamPermissionsRegionCompositeHealthCheckRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response =
           regionCompositeHealthChecksClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRegionCompositeHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionCompositeHealthCheckRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource)
    
    
    public final TestPermissionsResponse testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           regionCompositeHealthChecksClient.testIamPermissions(
               project, region, resource, testPermissionsRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRegionCompositeHealthCheckRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionCompositeHealthChecksClient regionCompositeHealthChecksClient =
         RegionCompositeHealthChecksClient.create()) {
       TestIamPermissionsRegionCompositeHealthCheckRequest request =
           TestIamPermissionsRegionCompositeHealthCheckRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           regionCompositeHealthChecksClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsRegionCompositeHealthCheckRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionCompositeHealthCheckRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
