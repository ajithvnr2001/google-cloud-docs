---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AutoscalersClient
title: Class AutoscalersClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:01:52.491155+00:00
---

# Class AutoscalersClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AutoscalersClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AutoscalersClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/AutoscalersClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The Autoscalers API.

This client uses Autoscalers version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String autoscaler = "autoscaler517258967";
       Autoscaler response = autoscalersClient.get(project, zone, autoscaler);
     }
     

Note: close() needs to be called on the AutoscalersClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves an aggregated list of autoscalers.  To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListAutoscalersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified autoscaler. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteAutoscalerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String zone, String autoscaler) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified autoscaler resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetAutoscalerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String autoscaler) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates an autoscaler in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertAutoscalerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String zone, Autoscaler autoscalerResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves a list of autoscalers contained within the specified zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListAutoscalersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Patch |  Updates an autoscaler in the specified project using the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchAutoscalerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String zone, Autoscaler autoscalerResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsAutoscalerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String zone, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
Update |  Updates an autoscaler in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAsync(UpdateAutoscalerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAsync(String project, String zone, Autoscaler autoscalerResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOperationCallable() 
  * updateCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of AutoscalersSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AutoscalersSettings autoscalersSettings =
         AutoscalersSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     AutoscalersClient autoscalersClient = AutoscalersClient.create(autoscalersSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AutoscalersSettings autoscalersSettings =
         AutoscalersSettings.newBuilder().setEndpoint(myEndpoint).build();
     AutoscalersClient autoscalersClient = AutoscalersClient.create(autoscalersSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AutoscalersClient

## Static Methods 

### create()
    
    
    public static final AutoscalersClient create()

Constructs an instance of AutoscalersClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[AutoscalersClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AutoscalersClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AutoscalersSettings settings)
    
    
    public static final AutoscalersClient create(AutoscalersSettings settings)

Constructs an instance of AutoscalersClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AutoscalersSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AutoscalersSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutoscalersClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AutoscalersClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(AutoscalersStub stub)
    
    
    public static final AutoscalersClient create(AutoscalersStub stub)

Constructs an instance of AutoscalersClient, using the given stub for making calls. This is for advanced usage - prefer using create(AutoscalersSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AutoscalersStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.AutoscalersStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutoscalersClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AutoscalersClient)` |   
  
## Constructors 

### AutoscalersClient(AutoscalersSettings settings)
    
    
    protected AutoscalersClient(AutoscalersSettings settings)

Constructs an instance of AutoscalersClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[AutoscalersSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AutoscalersSettings)`  
  
  
### AutoscalersClient(AutoscalersStub stub)
    
    
    protected AutoscalersClient(AutoscalersStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AutoscalersStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.AutoscalersStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListAutoscalersRequest request)
    
    
    public final AutoscalersClient.AggregatedListPagedResponse aggregatedList(AggregatedListAutoscalersRequest request)

Retrieves an aggregated list of autoscalers.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       AggregatedListAutoscalersRequest request =
           AggregatedListAutoscalersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, AutoscalersScopedList> element :
           autoscalersClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListAutoscalersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListAutoscalersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AutoscalersClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AutoscalersClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final AutoscalersClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves an aggregated list of autoscalers.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, AutoscalersScopedList> element :
           autoscalersClient.aggregatedList(project).iterateAll()) {
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
`[AutoscalersClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AutoscalersClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListAutoscalersRequest,AutoscalerAggregatedList> aggregatedListCallable()

Retrieves an aggregated list of autoscalers.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       AggregatedListAutoscalersRequest request =
           AggregatedListAutoscalersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         AutoscalerAggregatedList response =
             autoscalersClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, AutoscalersScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListAutoscalersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListAutoscalersRequest),[AutoscalerAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AutoscalerAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListAutoscalersRequest,AutoscalersClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves an aggregated list of autoscalers.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       AggregatedListAutoscalersRequest request =
           AggregatedListAutoscalersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, AutoscalersScopedList>> future =
           autoscalersClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, AutoscalersScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListAutoscalersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListAutoscalersRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AutoscalersClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteAutoscalerRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteAutoscalerRequest request)

Deletes the specified autoscaler.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       DeleteAutoscalerRequest request =
           DeleteAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = autoscalersClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteAutoscalerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String zone, String autoscaler)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String zone, String autoscaler)

Deletes the specified autoscaler.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String autoscaler = "autoscaler517258967";
       Operation response = autoscalersClient.deleteAsync(project, zone, autoscaler).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`autoscaler` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the autoscaler to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteAutoscalerRequest,Operation> deleteCallable()

Deletes the specified autoscaler.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       DeleteAutoscalerRequest request =
           DeleteAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = autoscalersClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteAutoscalerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteAutoscalerRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified autoscaler.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       DeleteAutoscalerRequest request =
           DeleteAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           autoscalersClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteAutoscalerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetAutoscalerRequest request)
    
    
    public final Autoscaler get(GetAutoscalerRequest request)

Returns the specified autoscaler resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       GetAutoscalerRequest request =
           GetAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       Autoscaler response = autoscalersClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetAutoscalerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Autoscaler](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Autoscaler)` |   
  
### get(String project, String zone, String autoscaler)
    
    
    public final Autoscaler get(String project, String zone, String autoscaler)

Returns the specified autoscaler resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String autoscaler = "autoscaler517258967";
       Autoscaler response = autoscalersClient.get(project, zone, autoscaler);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`autoscaler` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the autoscaler to return.  
**Returns**  
---  
**Type** | **Description**  
`[Autoscaler](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Autoscaler)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetAutoscalerRequest,Autoscaler> getCallable()

Returns the specified autoscaler resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       GetAutoscalerRequest request =
           GetAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<Autoscaler> future = autoscalersClient.getCallable().futureCall(request);
       // Do something.
       Autoscaler response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetAutoscalerRequest),[Autoscaler](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Autoscaler)>` |   
  
### getSettings()
    
    
    public final @Nullable AutoscalersSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.AutoscalersSettings` |   
  
### getStub()
    
    
    public AutoscalersStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[AutoscalersStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.AutoscalersStub)` |   
  
### insertAsync(InsertAutoscalerRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertAutoscalerRequest request)

Creates an autoscaler in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       InsertAutoscalerRequest request =
           InsertAutoscalerRequest.newBuilder()
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = autoscalersClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertAutoscalerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String zone, Autoscaler autoscalerResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String zone, Autoscaler autoscalerResource)

Creates an autoscaler in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       Autoscaler autoscalerResource = Autoscaler.newBuilder().build();
       Operation response = autoscalersClient.insertAsync(project, zone, autoscalerResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`autoscalerResource` | `[Autoscaler](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Autoscaler)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertAutoscalerRequest,Operation> insertCallable()

Creates an autoscaler in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       InsertAutoscalerRequest request =
           InsertAutoscalerRequest.newBuilder()
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = autoscalersClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertAutoscalerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertAutoscalerRequest,Operation,Operation> insertOperationCallable()

Creates an autoscaler in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       InsertAutoscalerRequest request =
           InsertAutoscalerRequest.newBuilder()
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           autoscalersClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertAutoscalerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListAutoscalersRequest request)
    
    
    public final AutoscalersClient.ListPagedResponse list(ListAutoscalersRequest request)

Retrieves a list of autoscalers contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       ListAutoscalersRequest request =
           ListAutoscalersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (Autoscaler element : autoscalersClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAutoscalersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListAutoscalersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[AutoscalersClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AutoscalersClient.ListPagedResponse)` |   
  
### list(String project, String zone)
    
    
    public final AutoscalersClient.ListPagedResponse list(String project, String zone)

Retrieves a list of autoscalers contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       for (Autoscaler element : autoscalersClient.list(project, zone).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
**Returns**  
---  
**Type** | **Description**  
`[AutoscalersClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AutoscalersClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListAutoscalersRequest,AutoscalerList> listCallable()

Retrieves a list of autoscalers contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       ListAutoscalersRequest request =
           ListAutoscalersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         AutoscalerList response = autoscalersClient.listCallable().call(request);
         for (Autoscaler element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAutoscalersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListAutoscalersRequest),[AutoscalerList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AutoscalerList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListAutoscalersRequest,AutoscalersClient.ListPagedResponse> listPagedCallable()

Retrieves a list of autoscalers contained within the specified zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       ListAutoscalersRequest request =
           ListAutoscalersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<Autoscaler> future = autoscalersClient.listPagedCallable().futureCall(request);
       // Do something.
       for (Autoscaler element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAutoscalersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListAutoscalersRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AutoscalersClient.ListPagedResponse)>` |   
  
### patchAsync(PatchAutoscalerRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchAutoscalerRequest request)

Updates an autoscaler in the specified project using the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       PatchAutoscalerRequest request =
           PatchAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = autoscalersClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchAutoscalerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String zone, Autoscaler autoscalerResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String zone, Autoscaler autoscalerResource)

Updates an autoscaler in the specified project using the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       Autoscaler autoscalerResource = Autoscaler.newBuilder().build();
       Operation response = autoscalersClient.patchAsync(project, zone, autoscalerResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`autoscalerResource` | `[Autoscaler](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Autoscaler)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchAutoscalerRequest,Operation> patchCallable()

Updates an autoscaler in the specified project using the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       PatchAutoscalerRequest request =
           PatchAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = autoscalersClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchAutoscalerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchAutoscalerRequest,Operation,Operation> patchOperationCallable()

Updates an autoscaler in the specified project using the data included in the request. This method supportsPATCH semantics and uses theJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       PatchAutoscalerRequest request =
           PatchAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           autoscalersClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchAutoscalerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsAutoscalerRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsAutoscalerRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       TestIamPermissionsAutoscalerRequest request =
           TestIamPermissionsAutoscalerRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       TestPermissionsResponse response = autoscalersClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsAutoscalerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissions(String project, String zone, String resource, TestPermissionsRequest testPermissionsRequestResource)
    
    
    public final TestPermissionsResponse testIamPermissions(String project, String zone, String resource, TestPermissionsRequest testPermissionsRequestResource)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           autoscalersClient.testIamPermissions(
               project, zone, resource, testPermissionsRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsAutoscalerRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       TestIamPermissionsAutoscalerRequest request =
           TestIamPermissionsAutoscalerRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<TestPermissionsResponse> future =
           autoscalersClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsAutoscalerRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
### updateAsync(UpdateAutoscalerRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(UpdateAutoscalerRequest request)

Updates an autoscaler in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       UpdateAutoscalerRequest request =
           UpdateAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = autoscalersClient.updateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateAutoscalerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(String project, String zone, Autoscaler autoscalerResource)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(String project, String zone, Autoscaler autoscalerResource)

Updates an autoscaler in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       Autoscaler autoscalerResource = Autoscaler.newBuilder().build();
       Operation response = autoscalersClient.updateAsync(project, zone, autoscalerResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the zone for this request.  
`autoscalerResource` | `[Autoscaler](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Autoscaler)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateCallable()
    
    
    public final UnaryCallable<UpdateAutoscalerRequest,Operation> updateCallable()

Updates an autoscaler in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       UpdateAutoscalerRequest request =
           UpdateAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = autoscalersClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateAutoscalerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationCallable()
    
    
    public final OperationCallable<UpdateAutoscalerRequest,Operation,Operation> updateOperationCallable()

Updates an autoscaler in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (AutoscalersClient autoscalersClient = AutoscalersClient.create()) {
       UpdateAutoscalerRequest request =
           UpdateAutoscalerRequest.newBuilder()
               .setAutoscaler("autoscaler517258967")
               .setAutoscalerResource(Autoscaler.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           autoscalersClient.updateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateAutoscalerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateAutoscalerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
