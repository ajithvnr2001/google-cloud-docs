---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient
title: Class GlobalOperationsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:23.195560+00:00
---

# Class GlobalOperationsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GlobalOperationsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/GlobalOperationsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The GlobalOperations API.

This client uses GlobalOperations version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       String project = "project-309310695";
       String operation = "operation1662702951";
       DeleteGlobalOperationResponse response = globalOperationsClient.delete(project, operation);
     }
     

Note: close() needs to be called on the GlobalOperationsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves an aggregated list of all operations.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListGlobalOperationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified Operations resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * delete(DeleteGlobalOperationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * delete(String project, String operation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCallable() 

  
Get |  Retrieves the specified Operations resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetGlobalOperationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String operation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
List |  Retrieves a list of Operation resources contained within the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListGlobalOperationsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Wait |  Waits for the specified Operation resource to return as `DONE` or for the request to approach the 2 minute deadline, and retrieves the specified Operation resource. This method differs from the `GET` method in that it waits for no more than the default deadline (2 minutes) and then returns the current state of the operation, which might be `DONE` or still in progress.  This method is called on a best-effort basis. Specifically:  \- In uncommon cases, when the server is overloaded, the request might return before the default deadline is reached, or might return after zero seconds. - If the default deadline is reached, there is no guarantee that the operation is actually done when the method returns. Be prepared to retry if the operation is not `DONE`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * wait(WaitGlobalOperationRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * wait(String project, String operation) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * waitCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of GlobalOperationsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GlobalOperationsSettings globalOperationsSettings =
         GlobalOperationsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     GlobalOperationsClient globalOperationsClient =
         GlobalOperationsClient.create(globalOperationsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GlobalOperationsSettings globalOperationsSettings =
         GlobalOperationsSettings.newBuilder().setEndpoint(myEndpoint).build();
     GlobalOperationsClient globalOperationsClient =
         GlobalOperationsClient.create(globalOperationsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > GlobalOperationsClient

## Static Methods 

### create()
    
    
    public static final GlobalOperationsClient create()

Constructs an instance of GlobalOperationsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GlobalOperationsSettings settings)
    
    
    public static final GlobalOperationsClient create(GlobalOperationsSettings settings)

Constructs an instance of GlobalOperationsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GlobalOperationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(GlobalOperationsStub stub)
    
    
    public static final GlobalOperationsClient create(GlobalOperationsStub stub)

Constructs an instance of GlobalOperationsClient, using the given stub for making calls. This is for advanced usage - prefer using create(GlobalOperationsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GlobalOperationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalOperationsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GlobalOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient)` |   
  
## Constructors 

### GlobalOperationsClient(GlobalOperationsSettings settings)
    
    
    protected GlobalOperationsClient(GlobalOperationsSettings settings)

Constructs an instance of GlobalOperationsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[GlobalOperationsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsSettings)`  
  
  
### GlobalOperationsClient(GlobalOperationsStub stub)
    
    
    protected GlobalOperationsClient(GlobalOperationsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GlobalOperationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalOperationsStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListGlobalOperationsRequest request)
    
    
    public final GlobalOperationsClient.AggregatedListPagedResponse aggregatedList(AggregatedListGlobalOperationsRequest request)

Retrieves an aggregated list of all operations.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       AggregatedListGlobalOperationsRequest request =
           AggregatedListGlobalOperationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, OperationsScopedList> element :
           globalOperationsClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListGlobalOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListGlobalOperationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GlobalOperationsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final GlobalOperationsClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves an aggregated list of all operations.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, OperationsScopedList> element :
           globalOperationsClient.aggregatedList(project).iterateAll()) {
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
`[GlobalOperationsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListGlobalOperationsRequest,OperationAggregatedList> aggregatedListCallable()

Retrieves an aggregated list of all operations.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       AggregatedListGlobalOperationsRequest request =
           AggregatedListGlobalOperationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         OperationAggregatedList response =
             globalOperationsClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, OperationsScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListGlobalOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListGlobalOperationsRequest),[OperationAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OperationAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListGlobalOperationsRequest,GlobalOperationsClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves an aggregated list of all operations.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       AggregatedListGlobalOperationsRequest request =
           AggregatedListGlobalOperationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, OperationsScopedList>> future =
           globalOperationsClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, OperationsScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListGlobalOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListGlobalOperationsRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.AggregatedListPagedResponse)>` |   
  
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

### delete(DeleteGlobalOperationRequest request)
    
    
    public final DeleteGlobalOperationResponse delete(DeleteGlobalOperationRequest request)

Deletes the specified Operations resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       DeleteGlobalOperationRequest request =
           DeleteGlobalOperationRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .build();
       DeleteGlobalOperationResponse response = globalOperationsClient.delete(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteGlobalOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalOperationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DeleteGlobalOperationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalOperationResponse)` |   
  
### delete(String project, String operation)
    
    
    public final DeleteGlobalOperationResponse delete(String project, String operation)

Deletes the specified Operations resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       String project = "project-309310695";
       String operation = "operation1662702951";
       DeleteGlobalOperationResponse response = globalOperationsClient.delete(project, operation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`operation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Operations resource to delete, or its unique numeric identifier.  
**Returns**  
---  
**Type** | **Description**  
`[DeleteGlobalOperationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalOperationResponse)` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteGlobalOperationRequest,DeleteGlobalOperationResponse> deleteCallable()

Deletes the specified Operations resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       DeleteGlobalOperationRequest request =
           DeleteGlobalOperationRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .build();
       ApiFuture<DeleteGlobalOperationResponse> future =
           globalOperationsClient.deleteCallable().futureCall(request);
       // Do something.
       DeleteGlobalOperationResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteGlobalOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalOperationRequest),[DeleteGlobalOperationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteGlobalOperationResponse)>` |   
  
### get(GetGlobalOperationRequest request)
    
    
    public final Operation get(GetGlobalOperationRequest request)

Retrieves the specified Operations resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       GetGlobalOperationRequest request =
           GetGlobalOperationRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .build();
       Operation response = globalOperationsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetGlobalOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGlobalOperationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)` |   
  
### get(String project, String operation)
    
    
    public final Operation get(String project, String operation)

Retrieves the specified Operations resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       String project = "project-309310695";
       String operation = "operation1662702951";
       Operation response = globalOperationsClient.get(project, operation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`operation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Operations resource to return, or its unique numeric identifier.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetGlobalOperationRequest,Operation> getCallable()

Retrieves the specified Operations resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       GetGlobalOperationRequest request =
           GetGlobalOperationRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .build();
       ApiFuture<Operation> future = globalOperationsClient.getCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetGlobalOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetGlobalOperationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getSettings()
    
    
    public final @Nullable GlobalOperationsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.GlobalOperationsSettings` |   
  
### getStub()
    
    
    public GlobalOperationsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[GlobalOperationsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.GlobalOperationsStub)` |   
  
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
  
### list(ListGlobalOperationsRequest request)
    
    
    public final GlobalOperationsClient.ListPagedResponse list(ListGlobalOperationsRequest request)

Retrieves a list of Operation resources contained within the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       ListGlobalOperationsRequest request =
           ListGlobalOperationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (Operation element : globalOperationsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListGlobalOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalOperationsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[GlobalOperationsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final GlobalOperationsClient.ListPagedResponse list(String project)

Retrieves a list of Operation resources contained within the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       String project = "project-309310695";
       for (Operation element : globalOperationsClient.list(project).iterateAll()) {
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
`[GlobalOperationsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListGlobalOperationsRequest,OperationList> listCallable()

Retrieves a list of Operation resources contained within the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       ListGlobalOperationsRequest request =
           ListGlobalOperationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         OperationList response = globalOperationsClient.listCallable().call(request);
         for (Operation element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlobalOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalOperationsRequest),[OperationList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OperationList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListGlobalOperationsRequest,GlobalOperationsClient.ListPagedResponse> listPagedCallable()

Retrieves a list of Operation resources contained within the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       ListGlobalOperationsRequest request =
           ListGlobalOperationsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<Operation> future = globalOperationsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (Operation element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListGlobalOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListGlobalOperationsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalOperationsClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### wait(WaitGlobalOperationRequest request)
    
    
    public final Operation wait(WaitGlobalOperationRequest request)

Waits for the specified Operation resource to return as `DONE` or for the request to approach the 2 minute deadline, and retrieves the specified Operation resource. This method differs from the `GET` method in that it waits for no more than the default deadline (2 minutes) and then returns the current state of the operation, which might be `DONE` or still in progress.

This method is called on a best-effort basis. Specifically:

\- In uncommon cases, when the server is overloaded, the request might return before the default deadline is reached, or might return after zero seconds. - If the default deadline is reached, there is no guarantee that the operation is actually done when the method returns. Be prepared to retry if the operation is not `DONE`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       WaitGlobalOperationRequest request =
           WaitGlobalOperationRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .build();
       Operation response = globalOperationsClient.wait(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[WaitGlobalOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WaitGlobalOperationRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)` |   
  
### wait(String project, String operation)
    
    
    public final Operation wait(String project, String operation)

Waits for the specified Operation resource to return as `DONE` or for the request to approach the 2 minute deadline, and retrieves the specified Operation resource. This method differs from the `GET` method in that it waits for no more than the default deadline (2 minutes) and then returns the current state of the operation, which might be `DONE` or still in progress.

This method is called on a best-effort basis. Specifically:

\- In uncommon cases, when the server is overloaded, the request might return before the default deadline is reached, or might return after zero seconds. - If the default deadline is reached, there is no guarantee that the operation is actually done when the method returns. Be prepared to retry if the operation is not `DONE`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       String project = "project-309310695";
       String operation = "operation1662702951";
       Operation response = globalOperationsClient.wait(project, operation);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`operation` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Operations resource to return, or its unique numeric identifier.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)` |   
  
### waitCallable()
    
    
    public final UnaryCallable<WaitGlobalOperationRequest,Operation> waitCallable()

Waits for the specified Operation resource to return as `DONE` or for the request to approach the 2 minute deadline, and retrieves the specified Operation resource. This method differs from the `GET` method in that it waits for no more than the default deadline (2 minutes) and then returns the current state of the operation, which might be `DONE` or still in progress.

This method is called on a best-effort basis. Specifically:

\- In uncommon cases, when the server is overloaded, the request might return before the default deadline is reached, or might return after zero seconds. - If the default deadline is reached, there is no guarantee that the operation is actually done when the method returns. Be prepared to retry if the operation is not `DONE`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (GlobalOperationsClient globalOperationsClient = GlobalOperationsClient.create()) {
       WaitGlobalOperationRequest request =
           WaitGlobalOperationRequest.newBuilder()
               .setOperation("operation1662702951")
               .setProject("project-309310695")
               .build();
       ApiFuture<Operation> future = globalOperationsClient.waitCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[WaitGlobalOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WaitGlobalOperationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
