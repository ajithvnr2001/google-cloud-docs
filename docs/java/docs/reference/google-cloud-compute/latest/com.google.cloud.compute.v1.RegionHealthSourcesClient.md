---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthSourcesClient
title: Class RegionHealthSourcesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:37.642749+00:00
---

# Class RegionHealthSourcesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthSourcesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionHealthSourcesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RegionHealthSourcesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RegionHealthSources API.

This client uses RegionHealthSources version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String healthSource = "healthSource513679767";
       HealthSource response = regionHealthSourcesClient.get(project, region, healthSource);
     }
     

Note: close() needs to be called on the RegionHealthSourcesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves the list of all HealthSource resources (all regional) available to the specified project.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListRegionHealthSourcesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified HealthSource in the given region |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRegionHealthSourceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String healthSource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified HealthSource resource in the given region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRegionHealthSourceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String healthSource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetHealth |  Gets the most recent health check results for this regional HealthSource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getHealth(GetHealthRegionHealthSourceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getHealth(String project, String region, String healthSource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getHealthCallable() 

  
Insert |  Create a HealthSource in the specified project in the given region using the parameters that are included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRegionHealthSourceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, HealthSource healthSourceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists the HealthSources for a project in the given region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRegionHealthSourcesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Updates the specified regional HealthSource resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchRegionHealthSourceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String region, String healthSource, HealthSource healthSourceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRegionHealthSourceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionHealthSourcesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionHealthSourcesSettings regionHealthSourcesSettings =
         RegionHealthSourcesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegionHealthSourcesClient regionHealthSourcesClient =
         RegionHealthSourcesClient.create(regionHealthSourcesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionHealthSourcesSettings regionHealthSourcesSettings =
         RegionHealthSourcesSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegionHealthSourcesClient regionHealthSourcesClient =
         RegionHealthSourcesClient.create(regionHealthSourcesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionHealthSourcesClient

## Static Methods 

### create()
    
    
    public static final RegionHealthSourcesClient create()

Constructs an instance of RegionHealthSourcesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionHealthSourcesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthSourcesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionHealthSourcesSettings settings)
    
    
    public static final RegionHealthSourcesClient create(RegionHealthSourcesSettings settings)

Constructs an instance of RegionHealthSourcesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionHealthSourcesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthSourcesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionHealthSourcesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthSourcesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionHealthSourcesStub stub)
    
    
    public static final RegionHealthSourcesClient create(RegionHealthSourcesStub stub)

Constructs an instance of RegionHealthSourcesClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionHealthSourcesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionHealthSourcesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionHealthSourcesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionHealthSourcesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthSourcesClient)` |   
  
## Constructors 

### RegionHealthSourcesClient(RegionHealthSourcesSettings settings)
    
    
    protected RegionHealthSourcesClient(RegionHealthSourcesSettings settings)

Constructs an instance of RegionHealthSourcesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionHealthSourcesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthSourcesSettings)`  
  
  
### RegionHealthSourcesClient(RegionHealthSourcesStub stub)
    
    
    protected RegionHealthSourcesClient(RegionHealthSourcesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionHealthSourcesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionHealthSourcesStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListRegionHealthSourcesRequest request)
    
    
    public final RegionHealthSourcesClient.AggregatedListPagedResponse aggregatedList(AggregatedListRegionHealthSourcesRequest request)

Retrieves the list of all HealthSource resources (all regional) available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       AggregatedListRegionHealthSourcesRequest request =
           AggregatedListRegionHealthSourcesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, HealthSourcesScopedList> element :
           regionHealthSourcesClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListRegionHealthSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListRegionHealthSourcesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionHealthSourcesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthSourcesClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final RegionHealthSourcesClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves the list of all HealthSource resources (all regional) available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, HealthSourcesScopedList> element :
           regionHealthSourcesClient.aggregatedList(project).iterateAll()) {
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
`[RegionHealthSourcesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthSourcesClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListRegionHealthSourcesRequest,HealthSourceAggregatedList> aggregatedListCallable()

Retrieves the list of all HealthSource resources (all regional) available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       AggregatedListRegionHealthSourcesRequest request =
           AggregatedListRegionHealthSourcesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         HealthSourceAggregatedList response =
             regionHealthSourcesClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, HealthSourcesScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListRegionHealthSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListRegionHealthSourcesRequest),[HealthSourceAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthSourceAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListRegionHealthSourcesRequest,RegionHealthSourcesClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves the list of all HealthSource resources (all regional) available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       AggregatedListRegionHealthSourcesRequest request =
           AggregatedListRegionHealthSourcesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, HealthSourcesScopedList>> future =
           regionHealthSourcesClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, HealthSourcesScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListRegionHealthSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListRegionHealthSourcesRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthSourcesClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteRegionHealthSourceRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRegionHealthSourceRequest request)

Deletes the specified HealthSource in the given region

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       DeleteRegionHealthSourceRequest request =
           DeleteRegionHealthSourceRequest.newBuilder()
               .setHealthSource("healthSource513679767")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionHealthSourcesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionHealthSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionHealthSourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String healthSource)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String healthSource)

Deletes the specified HealthSource in the given region

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String healthSource = "healthSource513679767";
       Operation response =
           regionHealthSourcesClient.deleteAsync(project, region, healthSource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`healthSource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the HealthSource resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRegionHealthSourceRequest,Operation> deleteCallable()

Deletes the specified HealthSource in the given region

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       DeleteRegionHealthSourceRequest request =
           DeleteRegionHealthSourceRequest.newBuilder()
               .setHealthSource("healthSource513679767")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = regionHealthSourcesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionHealthSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionHealthSourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRegionHealthSourceRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified HealthSource in the given region

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       DeleteRegionHealthSourceRequest request =
           DeleteRegionHealthSourceRequest.newBuilder()
               .setHealthSource("healthSource513679767")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionHealthSourcesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRegionHealthSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionHealthSourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRegionHealthSourceRequest request)
    
    
    public final HealthSource get(GetRegionHealthSourceRequest request)

Returns the specified HealthSource resource in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       GetRegionHealthSourceRequest request =
           GetRegionHealthSourceRequest.newBuilder()
               .setHealthSource("healthSource513679767")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       HealthSource response = regionHealthSourcesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegionHealthSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionHealthSourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HealthSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthSource)` |   
  
### get(String project, String region, String healthSource)
    
    
    public final HealthSource get(String project, String region, String healthSource)

Returns the specified HealthSource resource in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String healthSource = "healthSource513679767";
       HealthSource response = regionHealthSourcesClient.get(project, region, healthSource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`healthSource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the HealthSource resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[HealthSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthSource)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRegionHealthSourceRequest,HealthSource> getCallable()

Returns the specified HealthSource resource in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       GetRegionHealthSourceRequest request =
           GetRegionHealthSourceRequest.newBuilder()
               .setHealthSource("healthSource513679767")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<HealthSource> future = regionHealthSourcesClient.getCallable().futureCall(request);
       // Do something.
       HealthSource response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegionHealthSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionHealthSourceRequest),[HealthSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthSource)>` |   
  
### getHealth(GetHealthRegionHealthSourceRequest request)
    
    
    public final HealthSourceHealth getHealth(GetHealthRegionHealthSourceRequest request)

Gets the most recent health check results for this regional HealthSource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       GetHealthRegionHealthSourceRequest request =
           GetHealthRegionHealthSourceRequest.newBuilder()
               .setHealthSource("healthSource513679767")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       HealthSourceHealth response = regionHealthSourcesClient.getHealth(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetHealthRegionHealthSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetHealthRegionHealthSourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[HealthSourceHealth](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthSourceHealth)` |   
  
### getHealth(String project, String region, String healthSource)
    
    
    public final HealthSourceHealth getHealth(String project, String region, String healthSource)

Gets the most recent health check results for this regional HealthSource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String healthSource = "healthSource513679767";
       HealthSourceHealth response =
           regionHealthSourcesClient.getHealth(project, region, healthSource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the project scoping this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`healthSource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the HealthSource resource to get health for.  
**Returns**  
---  
**Type** | **Description**  
`[HealthSourceHealth](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthSourceHealth)` |   
  
### getHealthCallable()
    
    
    public final UnaryCallable<GetHealthRegionHealthSourceRequest,HealthSourceHealth> getHealthCallable()

Gets the most recent health check results for this regional HealthSource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       GetHealthRegionHealthSourceRequest request =
           GetHealthRegionHealthSourceRequest.newBuilder()
               .setHealthSource("healthSource513679767")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<HealthSourceHealth> future =
           regionHealthSourcesClient.getHealthCallable().futureCall(request);
       // Do something.
       HealthSourceHealth response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetHealthRegionHealthSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetHealthRegionHealthSourceRequest),[HealthSourceHealth](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthSourceHealth)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionHealthSourcesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RegionHealthSourcesSettings` |   
  
### getStub()
    
    
    public RegionHealthSourcesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionHealthSourcesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionHealthSourcesStub)` |   
  
### insertAsync(InsertRegionHealthSourceRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRegionHealthSourceRequest request)

Create a HealthSource in the specified project in the given region using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       InsertRegionHealthSourceRequest request =
           InsertRegionHealthSourceRequest.newBuilder()
               .setHealthSourceResource(HealthSource.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionHealthSourcesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRegionHealthSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionHealthSourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, HealthSource healthSourceResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, HealthSource healthSourceResource)

Create a HealthSource in the specified project in the given region using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       HealthSource healthSourceResource = HealthSource.newBuilder().build();
       Operation response =
           regionHealthSourcesClient.insertAsync(project, region, healthSourceResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`healthSourceResource` | `[HealthSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthSource)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRegionHealthSourceRequest,Operation> insertCallable()

Create a HealthSource in the specified project in the given region using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       InsertRegionHealthSourceRequest request =
           InsertRegionHealthSourceRequest.newBuilder()
               .setHealthSourceResource(HealthSource.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = regionHealthSourcesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionHealthSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionHealthSourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRegionHealthSourceRequest,Operation,Operation> insertOperationCallable()

Create a HealthSource in the specified project in the given region using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       InsertRegionHealthSourceRequest request =
           InsertRegionHealthSourceRequest.newBuilder()
               .setHealthSourceResource(HealthSource.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionHealthSourcesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRegionHealthSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionHealthSourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRegionHealthSourcesRequest request)
    
    
    public final RegionHealthSourcesClient.ListPagedResponse list(ListRegionHealthSourcesRequest request)

Lists the HealthSources for a project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       ListRegionHealthSourcesRequest request =
           ListRegionHealthSourcesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (HealthSource element : regionHealthSourcesClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionHealthSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionHealthSourcesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionHealthSourcesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthSourcesClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final RegionHealthSourcesClient.ListPagedResponse list(String project, String region)

Lists the HealthSources for a project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (HealthSource element : regionHealthSourcesClient.list(project, region).iterateAll()) {
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
`[RegionHealthSourcesClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthSourcesClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRegionHealthSourcesRequest,HealthSourceList> listCallable()

Lists the HealthSources for a project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       ListRegionHealthSourcesRequest request =
           ListRegionHealthSourcesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         HealthSourceList response = regionHealthSourcesClient.listCallable().call(request);
         for (HealthSource element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionHealthSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionHealthSourcesRequest),[HealthSourceList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthSourceList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRegionHealthSourcesRequest,RegionHealthSourcesClient.ListPagedResponse> listPagedCallable()

Lists the HealthSources for a project in the given region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       ListRegionHealthSourcesRequest request =
           ListRegionHealthSourcesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<HealthSource> future =
           regionHealthSourcesClient.listPagedCallable().futureCall(request);
       // Do something.
       for (HealthSource element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionHealthSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionHealthSourcesRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionHealthSourcesClient.ListPagedResponse)>` |   
  
### patchAsync(PatchRegionHealthSourceRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchRegionHealthSourceRequest request)

Updates the specified regional HealthSource resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       PatchRegionHealthSourceRequest request =
           PatchRegionHealthSourceRequest.newBuilder()
               .setHealthSource("healthSource513679767")
               .setHealthSourceResource(HealthSource.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionHealthSourcesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchRegionHealthSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionHealthSourceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String region, String healthSource, HealthSource healthSourceResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String region, String healthSource, HealthSource healthSourceResource)

Updates the specified regional HealthSource resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String healthSource = "healthSource513679767";
       HealthSource healthSourceResource = HealthSource.newBuilder().build();
       Operation response =
           regionHealthSourcesClient
               .patchAsync(project, region, healthSource, healthSourceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`healthSource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the HealthSource to update. The name must be 1-63 characters long, and comply with RFC1035.  
`healthSourceResource` | `[HealthSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.HealthSource)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchRegionHealthSourceRequest,Operation> patchCallable()

Updates the specified regional HealthSource resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       PatchRegionHealthSourceRequest request =
           PatchRegionHealthSourceRequest.newBuilder()
               .setHealthSource("healthSource513679767")
               .setHealthSourceResource(HealthSource.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = regionHealthSourcesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchRegionHealthSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionHealthSourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchRegionHealthSourceRequest,Operation,Operation> patchOperationCallable()

Updates the specified regional HealthSource resource with the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       PatchRegionHealthSourceRequest request =
           PatchRegionHealthSourceRequest.newBuilder()
               .setHealthSource("healthSource513679767")
               .setHealthSourceResource(HealthSource.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionHealthSourcesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchRegionHealthSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRegionHealthSourceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRegionHealthSourceRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsRegionHealthSourceRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       TestIamPermissionsRegionHealthSourceRequest request =
           TestIamPermissionsRegionHealthSourceRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = regionHealthSourcesClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRegionHealthSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionHealthSourceRequest)`  
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
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           regionHealthSourcesClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsRegionHealthSourceRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionHealthSourcesClient regionHealthSourcesClient = RegionHealthSourcesClient.create()) {
       TestIamPermissionsRegionHealthSourceRequest request =
           TestIamPermissionsRegionHealthSourceRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           regionHealthSourcesClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsRegionHealthSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionHealthSourceRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
