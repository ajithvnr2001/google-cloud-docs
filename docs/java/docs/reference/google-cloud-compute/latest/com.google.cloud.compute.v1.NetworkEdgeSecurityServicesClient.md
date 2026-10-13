---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEdgeSecurityServicesClient
title: Class NetworkEdgeSecurityServicesClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:03.351776+00:00
---

# Class NetworkEdgeSecurityServicesClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEdgeSecurityServicesClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NetworkEdgeSecurityServicesClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/NetworkEdgeSecurityServicesClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The NetworkEdgeSecurityServices API.

This client uses NetworkEdgeSecurityServices version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String networkEdgeSecurityService = "networkEdgeSecurityService-1390253366";
       NetworkEdgeSecurityService response =
           networkEdgeSecurityServicesClient.get(project, region, networkEdgeSecurityService);
     }
     

Note: close() needs to be called on the NetworkEdgeSecurityServicesClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves the list of all NetworkEdgeSecurityService resources available to the specified project.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListNetworkEdgeSecurityServicesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteNetworkEdgeSecurityServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String networkEdgeSecurityService) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Gets a specified NetworkEdgeSecurityService. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetNetworkEdgeSecurityServiceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String networkEdgeSecurityService) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a new service in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertNetworkEdgeSecurityServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, NetworkEdgeSecurityService networkEdgeSecurityServiceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
Patch |  Patches the specified policy with the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchNetworkEdgeSecurityServiceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String region, String networkEdgeSecurityService, NetworkEdgeSecurityService networkEdgeSecurityServiceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of NetworkEdgeSecurityServicesSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworkEdgeSecurityServicesSettings networkEdgeSecurityServicesSettings =
         NetworkEdgeSecurityServicesSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create(networkEdgeSecurityServicesSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworkEdgeSecurityServicesSettings networkEdgeSecurityServicesSettings =
         NetworkEdgeSecurityServicesSettings.newBuilder().setEndpoint(myEndpoint).build();
     NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create(networkEdgeSecurityServicesSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > NetworkEdgeSecurityServicesClient

## Static Methods 

### create()
    
    
    public static final NetworkEdgeSecurityServicesClient create()

Constructs an instance of NetworkEdgeSecurityServicesClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[NetworkEdgeSecurityServicesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEdgeSecurityServicesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NetworkEdgeSecurityServicesSettings settings)
    
    
    public static final NetworkEdgeSecurityServicesClient create(NetworkEdgeSecurityServicesSettings settings)

Constructs an instance of NetworkEdgeSecurityServicesClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NetworkEdgeSecurityServicesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEdgeSecurityServicesSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEdgeSecurityServicesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEdgeSecurityServicesClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NetworkEdgeSecurityServicesStub stub)
    
    
    public static final NetworkEdgeSecurityServicesClient create(NetworkEdgeSecurityServicesStub stub)

Constructs an instance of NetworkEdgeSecurityServicesClient, using the given stub for making calls. This is for advanced usage - prefer using create(NetworkEdgeSecurityServicesSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NetworkEdgeSecurityServicesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.NetworkEdgeSecurityServicesStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEdgeSecurityServicesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEdgeSecurityServicesClient)` |   
  
## Constructors 

### NetworkEdgeSecurityServicesClient(NetworkEdgeSecurityServicesSettings settings)
    
    
    protected NetworkEdgeSecurityServicesClient(NetworkEdgeSecurityServicesSettings settings)

Constructs an instance of NetworkEdgeSecurityServicesClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NetworkEdgeSecurityServicesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEdgeSecurityServicesSettings)`  
  
  
### NetworkEdgeSecurityServicesClient(NetworkEdgeSecurityServicesStub stub)
    
    
    protected NetworkEdgeSecurityServicesClient(NetworkEdgeSecurityServicesStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NetworkEdgeSecurityServicesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.NetworkEdgeSecurityServicesStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListNetworkEdgeSecurityServicesRequest request)
    
    
    public final NetworkEdgeSecurityServicesClient.AggregatedListPagedResponse aggregatedList(AggregatedListNetworkEdgeSecurityServicesRequest request)

Retrieves the list of all NetworkEdgeSecurityService resources available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       AggregatedListNetworkEdgeSecurityServicesRequest request =
           AggregatedListNetworkEdgeSecurityServicesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, NetworkEdgeSecurityServicesScopedList> element :
           networkEdgeSecurityServicesClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListNetworkEdgeSecurityServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListNetworkEdgeSecurityServicesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEdgeSecurityServicesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEdgeSecurityServicesClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final NetworkEdgeSecurityServicesClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves the list of all NetworkEdgeSecurityService resources available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, NetworkEdgeSecurityServicesScopedList> element :
           networkEdgeSecurityServicesClient.aggregatedList(project).iterateAll()) {
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
`[NetworkEdgeSecurityServicesClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEdgeSecurityServicesClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListNetworkEdgeSecurityServicesRequest,NetworkEdgeSecurityServiceAggregatedList> aggregatedListCallable()

Retrieves the list of all NetworkEdgeSecurityService resources available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       AggregatedListNetworkEdgeSecurityServicesRequest request =
           AggregatedListNetworkEdgeSecurityServicesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         NetworkEdgeSecurityServiceAggregatedList response =
             networkEdgeSecurityServicesClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, NetworkEdgeSecurityServicesScopedList> element :
             response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListNetworkEdgeSecurityServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListNetworkEdgeSecurityServicesRequest),[NetworkEdgeSecurityServiceAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEdgeSecurityServiceAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListNetworkEdgeSecurityServicesRequest,NetworkEdgeSecurityServicesClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves the list of all NetworkEdgeSecurityService resources available to the specified project.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       AggregatedListNetworkEdgeSecurityServicesRequest request =
           AggregatedListNetworkEdgeSecurityServicesRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, NetworkEdgeSecurityServicesScopedList>> future =
           networkEdgeSecurityServicesClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, NetworkEdgeSecurityServicesScopedList> element :
           future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListNetworkEdgeSecurityServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListNetworkEdgeSecurityServicesRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEdgeSecurityServicesClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteNetworkEdgeSecurityServiceRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteNetworkEdgeSecurityServiceRequest request)

Deletes the specified service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       DeleteNetworkEdgeSecurityServiceRequest request =
           DeleteNetworkEdgeSecurityServiceRequest.newBuilder()
               .setNetworkEdgeSecurityService("networkEdgeSecurityService-1390253366")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = networkEdgeSecurityServicesClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNetworkEdgeSecurityServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkEdgeSecurityServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String networkEdgeSecurityService)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String networkEdgeSecurityService)

Deletes the specified service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String networkEdgeSecurityService = "networkEdgeSecurityService-1390253366";
       Operation response =
           networkEdgeSecurityServicesClient
               .deleteAsync(project, region, networkEdgeSecurityService)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`networkEdgeSecurityService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the network edge security service to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteNetworkEdgeSecurityServiceRequest,Operation> deleteCallable()

Deletes the specified service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       DeleteNetworkEdgeSecurityServiceRequest request =
           DeleteNetworkEdgeSecurityServiceRequest.newBuilder()
               .setNetworkEdgeSecurityService("networkEdgeSecurityService-1390253366")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           networkEdgeSecurityServicesClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNetworkEdgeSecurityServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkEdgeSecurityServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteNetworkEdgeSecurityServiceRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       DeleteNetworkEdgeSecurityServiceRequest request =
           DeleteNetworkEdgeSecurityServiceRequest.newBuilder()
               .setNetworkEdgeSecurityService("networkEdgeSecurityService-1390253366")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           networkEdgeSecurityServicesClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteNetworkEdgeSecurityServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkEdgeSecurityServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetNetworkEdgeSecurityServiceRequest request)
    
    
    public final NetworkEdgeSecurityService get(GetNetworkEdgeSecurityServiceRequest request)

Gets a specified NetworkEdgeSecurityService.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       GetNetworkEdgeSecurityServiceRequest request =
           GetNetworkEdgeSecurityServiceRequest.newBuilder()
               .setNetworkEdgeSecurityService("networkEdgeSecurityService-1390253366")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       NetworkEdgeSecurityService response = networkEdgeSecurityServicesClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNetworkEdgeSecurityServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNetworkEdgeSecurityServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEdgeSecurityService](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEdgeSecurityService)` |   
  
### get(String project, String region, String networkEdgeSecurityService)
    
    
    public final NetworkEdgeSecurityService get(String project, String region, String networkEdgeSecurityService)

Gets a specified NetworkEdgeSecurityService.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String networkEdgeSecurityService = "networkEdgeSecurityService-1390253366";
       NetworkEdgeSecurityService response =
           networkEdgeSecurityServicesClient.get(project, region, networkEdgeSecurityService);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`networkEdgeSecurityService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the network edge security service to get.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEdgeSecurityService](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEdgeSecurityService)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetNetworkEdgeSecurityServiceRequest,NetworkEdgeSecurityService> getCallable()

Gets a specified NetworkEdgeSecurityService.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       GetNetworkEdgeSecurityServiceRequest request =
           GetNetworkEdgeSecurityServiceRequest.newBuilder()
               .setNetworkEdgeSecurityService("networkEdgeSecurityService-1390253366")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<NetworkEdgeSecurityService> future =
           networkEdgeSecurityServicesClient.getCallable().futureCall(request);
       // Do something.
       NetworkEdgeSecurityService response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNetworkEdgeSecurityServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNetworkEdgeSecurityServiceRequest),[NetworkEdgeSecurityService](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEdgeSecurityService)>` |   
  
### getSettings()
    
    
    public final @Nullable NetworkEdgeSecurityServicesSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.NetworkEdgeSecurityServicesSettings` |   
  
### getStub()
    
    
    public NetworkEdgeSecurityServicesStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[NetworkEdgeSecurityServicesStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.NetworkEdgeSecurityServicesStub)` |   
  
### insertAsync(InsertNetworkEdgeSecurityServiceRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertNetworkEdgeSecurityServiceRequest request)

Creates a new service in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       InsertNetworkEdgeSecurityServiceRequest request =
           InsertNetworkEdgeSecurityServiceRequest.newBuilder()
               .setNetworkEdgeSecurityServiceResource(
                   NetworkEdgeSecurityService.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       Operation response = networkEdgeSecurityServicesClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertNetworkEdgeSecurityServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertNetworkEdgeSecurityServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, NetworkEdgeSecurityService networkEdgeSecurityServiceResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, NetworkEdgeSecurityService networkEdgeSecurityServiceResource)

Creates a new service in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       NetworkEdgeSecurityService networkEdgeSecurityServiceResource =
           NetworkEdgeSecurityService.newBuilder().build();
       Operation response =
           networkEdgeSecurityServicesClient
               .insertAsync(project, region, networkEdgeSecurityServiceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`networkEdgeSecurityServiceResource` | `[NetworkEdgeSecurityService](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEdgeSecurityService)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertNetworkEdgeSecurityServiceRequest,Operation> insertCallable()

Creates a new service in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       InsertNetworkEdgeSecurityServiceRequest request =
           InsertNetworkEdgeSecurityServiceRequest.newBuilder()
               .setNetworkEdgeSecurityServiceResource(
                   NetworkEdgeSecurityService.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future =
           networkEdgeSecurityServicesClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertNetworkEdgeSecurityServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertNetworkEdgeSecurityServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertNetworkEdgeSecurityServiceRequest,Operation,Operation> insertOperationCallable()

Creates a new service in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       InsertNetworkEdgeSecurityServiceRequest request =
           InsertNetworkEdgeSecurityServiceRequest.newBuilder()
               .setNetworkEdgeSecurityServiceResource(
                   NetworkEdgeSecurityService.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setValidateOnly(true)
               .build();
       OperationFuture<Operation, Operation> future =
           networkEdgeSecurityServicesClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertNetworkEdgeSecurityServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertNetworkEdgeSecurityServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### patchAsync(PatchNetworkEdgeSecurityServiceRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchNetworkEdgeSecurityServiceRequest request)

Patches the specified policy with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       PatchNetworkEdgeSecurityServiceRequest request =
           PatchNetworkEdgeSecurityServiceRequest.newBuilder()
               .setNetworkEdgeSecurityService("networkEdgeSecurityService-1390253366")
               .setNetworkEdgeSecurityServiceResource(
                   NetworkEdgeSecurityService.newBuilder().build())
               .setPaths("paths106438894")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .build();
       Operation response = networkEdgeSecurityServicesClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchNetworkEdgeSecurityServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchNetworkEdgeSecurityServiceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String region, String networkEdgeSecurityService, NetworkEdgeSecurityService networkEdgeSecurityServiceResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String region, String networkEdgeSecurityService, NetworkEdgeSecurityService networkEdgeSecurityServiceResource)

Patches the specified policy with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String networkEdgeSecurityService = "networkEdgeSecurityService-1390253366";
       NetworkEdgeSecurityService networkEdgeSecurityServiceResource =
           NetworkEdgeSecurityService.newBuilder().build();
       Operation response =
           networkEdgeSecurityServicesClient
               .patchAsync(
                   project, region, networkEdgeSecurityService, networkEdgeSecurityServiceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`networkEdgeSecurityService` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the network edge security service to update.  
`networkEdgeSecurityServiceResource` | `[NetworkEdgeSecurityService](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEdgeSecurityService)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchNetworkEdgeSecurityServiceRequest,Operation> patchCallable()

Patches the specified policy with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       PatchNetworkEdgeSecurityServiceRequest request =
           PatchNetworkEdgeSecurityServiceRequest.newBuilder()
               .setNetworkEdgeSecurityService("networkEdgeSecurityService-1390253366")
               .setNetworkEdgeSecurityServiceResource(
                   NetworkEdgeSecurityService.newBuilder().build())
               .setPaths("paths106438894")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .build();
       ApiFuture<Operation> future =
           networkEdgeSecurityServicesClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchNetworkEdgeSecurityServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchNetworkEdgeSecurityServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchNetworkEdgeSecurityServiceRequest,Operation,Operation> patchOperationCallable()

Patches the specified policy with the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEdgeSecurityServicesClient networkEdgeSecurityServicesClient =
         NetworkEdgeSecurityServicesClient.create()) {
       PatchNetworkEdgeSecurityServiceRequest request =
           PatchNetworkEdgeSecurityServiceRequest.newBuilder()
               .setNetworkEdgeSecurityService("networkEdgeSecurityService-1390253366")
               .setNetworkEdgeSecurityServiceResource(
                   NetworkEdgeSecurityService.newBuilder().build())
               .setPaths("paths106438894")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .build();
       OperationFuture<Operation, Operation> future =
           networkEdgeSecurityServicesClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchNetworkEdgeSecurityServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchNetworkEdgeSecurityServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
