---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient
title: Class RoutersClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:19.866465+00:00
---

# Class RoutersClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RoutersClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RoutersClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The Routers API.

This client uses Routers version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       Router response = routersClient.get(project, region, router);
     }
     

Note: close() needs to be called on the RoutersClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves an aggregated list of routers.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListRoutersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified Router resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRouterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String router) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
DeleteNamedSet |  Deletes Named Set |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteNamedSetAsync(DeleteNamedSetRouterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteNamedSetAsync(String project, String region, String router) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteNamedSetOperationCallable() 
  * deleteNamedSetCallable() 

  
DeleteRoutePolicy |  Deletes Route Policy |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteRoutePolicyAsync(DeleteRoutePolicyRouterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteRoutePolicyAsync(String project, String region, String router) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteRoutePolicyOperationCallable() 
  * deleteRoutePolicyCallable() 

  
Get |  Returns the specified Router resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRouterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String router) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetNamedSet |  Returns specified Named Set |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNamedSet(GetNamedSetRouterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNamedSet(String project, String region, String router) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNamedSetCallable() 

  
GetNatIpInfo |  Retrieves runtime NAT IP information. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNatIpInfo(GetNatIpInfoRouterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNatIpInfo(String project, String region, String router) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNatIpInfoCallable() 

  
GetNatMappingInfo |  Retrieves runtime Nat mapping information of VM endpoints. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getNatMappingInfo(GetNatMappingInfoRoutersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getNatMappingInfo(String project, String region, String router) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getNatMappingInfoPagedCallable() 
  * getNatMappingInfoCallable() 

  
GetRoutePolicy |  Returns specified Route Policy |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRoutePolicy(GetRoutePolicyRouterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRoutePolicy(String project, String region, String router) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRoutePolicyCallable() 

  
GetRouterStatus |  Retrieves runtime information of the specified router. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getRouterStatus(GetRouterStatusRouterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getRouterStatus(String project, String region, String router) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getRouterStatusCallable() 

  
Insert |  Creates a Router resource in the specified project and region using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRouterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, Router routerResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves a list of Router resources available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRoutersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListBgpRoutes |  Retrieves a list of router bgp routes available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBgpRoutes(ListBgpRoutesRoutersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBgpRoutes(String project, String region, String router) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBgpRoutesPagedCallable() 
  * listBgpRoutesCallable() 

  
ListNamedSets |  Retrieves a list of router named set subresources available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNamedSets(ListNamedSetsRoutersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNamedSets(String project, String region, String router) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNamedSetsPagedCallable() 
  * listNamedSetsCallable() 

  
ListRoutePolicies |  Retrieves a list of router route policy subresources available to the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listRoutePolicies(ListRoutePoliciesRoutersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listRoutePolicies(String project, String region, String router) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listRoutePoliciesPagedCallable() 
  * listRoutePoliciesCallable() 

  
Patch |  Patches the specified Router resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchRouterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String region, String router, Router routerResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
PatchNamedSet |  Patches Named Set |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchNamedSetAsync(PatchNamedSetRouterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchNamedSetAsync(String project, String region, String router, NamedSet namedSetResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchNamedSetOperationCallable() 
  * patchNamedSetCallable() 

  
PatchRoutePolicy |  Patches Route Policy |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchRoutePolicyAsync(PatchRoutePolicyRouterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchRoutePolicyAsync(String project, String region, String router, RoutePolicy routePolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchRoutePolicyOperationCallable() 
  * patchRoutePolicyCallable() 

  
Preview |  Preview fields auto-generated during router create andupdate operations. Calling this method does NOT create or update the router. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * preview(PreviewRouterRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * preview(String project, String region, String router, Router routerResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * previewCallable() 

  
Update |  Updates the specified Router resource with the data included in the request. This method conforms toPUT semantics, which requests that the state of the target resource be created or replaced with the state defined by the representation enclosed in the request message payload. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAsync(UpdateRouterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAsync(String project, String region, String router, Router routerResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOperationCallable() 
  * updateCallable() 

  
UpdateNamedSet |  Updates or creates new Named Set |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateNamedSetAsync(UpdateNamedSetRouterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateNamedSetAsync(String project, String region, String router, NamedSet namedSetResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateNamedSetOperationCallable() 
  * updateNamedSetCallable() 

  
UpdateRoutePolicy |  Updates or creates new Route Policy |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateRoutePolicyAsync(UpdateRoutePolicyRouterRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateRoutePolicyAsync(String project, String region, String router, RoutePolicy routePolicyResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateRoutePolicyOperationCallable() 
  * updateRoutePolicyCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RoutersSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RoutersSettings routersSettings =
         RoutersSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RoutersClient routersClient = RoutersClient.create(routersSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RoutersSettings routersSettings = RoutersSettings.newBuilder().setEndpoint(myEndpoint).build();
     RoutersClient routersClient = RoutersClient.create(routersSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RoutersClient

## Static Methods 

### create()
    
    
    public static final RoutersClient create()

Constructs an instance of RoutersClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RoutersClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RoutersSettings settings)
    
    
    public static final RoutersClient create(RoutersSettings settings)

Constructs an instance of RoutersClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RoutersSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RoutersClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RoutersStub stub)
    
    
    public static final RoutersClient create(RoutersStub stub)

Constructs an instance of RoutersClient, using the given stub for making calls. This is for advanced usage - prefer using create(RoutersSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RoutersStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RoutersStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RoutersClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient)` |   
  
## Constructors 

### RoutersClient(RoutersSettings settings)
    
    
    protected RoutersClient(RoutersSettings settings)

Constructs an instance of RoutersClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RoutersSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersSettings)`  
  
  
### RoutersClient(RoutersStub stub)
    
    
    protected RoutersClient(RoutersStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RoutersStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RoutersStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListRoutersRequest request)
    
    
    public final RoutersClient.AggregatedListPagedResponse aggregatedList(AggregatedListRoutersRequest request)

Retrieves an aggregated list of routers.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       AggregatedListRoutersRequest request =
           AggregatedListRoutersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, RoutersScopedList> element :
           routersClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListRoutersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RoutersClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final RoutersClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves an aggregated list of routers.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, RoutersScopedList> element :
           routersClient.aggregatedList(project).iterateAll()) {
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
`[RoutersClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListRoutersRequest,RouterAggregatedList> aggregatedListCallable()

Retrieves an aggregated list of routers.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       AggregatedListRoutersRequest request =
           AggregatedListRoutersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         RouterAggregatedList response = routersClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, RoutersScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListRoutersRequest),[RouterAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RouterAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListRoutersRequest,RoutersClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves an aggregated list of routers.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       AggregatedListRoutersRequest request =
           AggregatedListRoutersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, RoutersScopedList>> future =
           routersClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, RoutersScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListRoutersRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteRouterRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRouterRequest request)

Deletes the specified Router resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       DeleteRouterRequest request =
           DeleteRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .build();
       Operation response = routersClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String router)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String router)

Deletes the specified Router resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       Operation response = routersClient.deleteAsync(project, region, router).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Router resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRouterRequest,Operation> deleteCallable()

Deletes the specified Router resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       DeleteRouterRequest request =
           DeleteRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .build();
       ApiFuture<Operation> future = routersClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteNamedSetAsync(DeleteNamedSetRouterRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteNamedSetAsync(DeleteNamedSetRouterRequest request)

Deletes Named Set

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       DeleteNamedSetRouterRequest request =
           DeleteNamedSetRouterRequest.newBuilder()
               .setNamedSet("namedSet1841034857")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .build();
       Operation response = routersClient.deleteNamedSetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNamedSetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNamedSetRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteNamedSetAsync(String project, String region, String router)
    
    
    public final OperationFuture<Operation,Operation> deleteNamedSetAsync(String project, String region, String router)

Deletes Named Set

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       Operation response = routersClient.deleteNamedSetAsync(project, region, router).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Router resource where Named Set is defined.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteNamedSetCallable()
    
    
    public final UnaryCallable<DeleteNamedSetRouterRequest,Operation> deleteNamedSetCallable()

Deletes Named Set

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       DeleteNamedSetRouterRequest request =
           DeleteNamedSetRouterRequest.newBuilder()
               .setNamedSet("namedSet1841034857")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .build();
       ApiFuture<Operation> future = routersClient.deleteNamedSetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNamedSetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNamedSetRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteNamedSetOperationCallable()
    
    
    public final OperationCallable<DeleteNamedSetRouterRequest,Operation,Operation> deleteNamedSetOperationCallable()

Deletes Named Set

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       DeleteNamedSetRouterRequest request =
           DeleteNamedSetRouterRequest.newBuilder()
               .setNamedSet("namedSet1841034857")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .build();
       OperationFuture<Operation, Operation> future =
           routersClient.deleteNamedSetOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteNamedSetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNamedSetRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRouterRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified Router resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       DeleteRouterRequest request =
           DeleteRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .build();
       OperationFuture<Operation, Operation> future =
           routersClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteRoutePolicyAsync(DeleteRoutePolicyRouterRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteRoutePolicyAsync(DeleteRoutePolicyRouterRequest request)

Deletes Route Policy

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       DeleteRoutePolicyRouterRequest request =
           DeleteRoutePolicyRouterRequest.newBuilder()
               .setPolicy("policy-982670030")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .build();
       Operation response = routersClient.deleteRoutePolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRoutePolicyRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRoutePolicyRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteRoutePolicyAsync(String project, String region, String router)
    
    
    public final OperationFuture<Operation,Operation> deleteRoutePolicyAsync(String project, String region, String router)

Deletes Route Policy

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       Operation response = routersClient.deleteRoutePolicyAsync(project, region, router).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Router resource where Route Policy is defined.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteRoutePolicyCallable()
    
    
    public final UnaryCallable<DeleteRoutePolicyRouterRequest,Operation> deleteRoutePolicyCallable()

Deletes Route Policy

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       DeleteRoutePolicyRouterRequest request =
           DeleteRoutePolicyRouterRequest.newBuilder()
               .setPolicy("policy-982670030")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .build();
       ApiFuture<Operation> future = routersClient.deleteRoutePolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRoutePolicyRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRoutePolicyRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteRoutePolicyOperationCallable()
    
    
    public final OperationCallable<DeleteRoutePolicyRouterRequest,Operation,Operation> deleteRoutePolicyOperationCallable()

Deletes Route Policy

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       DeleteRoutePolicyRouterRequest request =
           DeleteRoutePolicyRouterRequest.newBuilder()
               .setPolicy("policy-982670030")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .build();
       OperationFuture<Operation, Operation> future =
           routersClient.deleteRoutePolicyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRoutePolicyRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRoutePolicyRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRouterRequest request)
    
    
    public final Router get(GetRouterRequest request)

Returns the specified Router resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       GetRouterRequest request =
           GetRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       Router response = routersClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Router)` |   
  
### get(String project, String region, String router)
    
    
    public final Router get(String project, String region, String router)

Returns the specified Router resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       Router response = routersClient.get(project, region, router);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Router resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Router)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRouterRequest,Router> getCallable()

Returns the specified Router resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       GetRouterRequest request =
           GetRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       ApiFuture<Router> future = routersClient.getCallable().futureCall(request);
       // Do something.
       Router response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRouterRequest),[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Router)>` |   
  
### getNamedSet(GetNamedSetRouterRequest request)
    
    
    public final RoutersGetNamedSetResponse getNamedSet(GetNamedSetRouterRequest request)

Returns specified Named Set

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       GetNamedSetRouterRequest request =
           GetNamedSetRouterRequest.newBuilder()
               .setNamedSet("namedSet1841034857")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       RoutersGetNamedSetResponse response = routersClient.getNamedSet(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNamedSetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNamedSetRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RoutersGetNamedSetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersGetNamedSetResponse)` |   
  
### getNamedSet(String project, String region, String router)
    
    
    public final RoutersGetNamedSetResponse getNamedSet(String project, String region, String router)

Returns specified Named Set

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       RoutersGetNamedSetResponse response = routersClient.getNamedSet(project, region, router);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Router resource to query for the named set. The name should conform to RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[RoutersGetNamedSetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersGetNamedSetResponse)` |   
  
### getNamedSetCallable()
    
    
    public final UnaryCallable<GetNamedSetRouterRequest,RoutersGetNamedSetResponse> getNamedSetCallable()

Returns specified Named Set

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       GetNamedSetRouterRequest request =
           GetNamedSetRouterRequest.newBuilder()
               .setNamedSet("namedSet1841034857")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       ApiFuture<RoutersGetNamedSetResponse> future =
           routersClient.getNamedSetCallable().futureCall(request);
       // Do something.
       RoutersGetNamedSetResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNamedSetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNamedSetRouterRequest),[RoutersGetNamedSetResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersGetNamedSetResponse)>` |   
  
### getNatIpInfo(GetNatIpInfoRouterRequest request)
    
    
    public final NatIpInfoResponse getNatIpInfo(GetNatIpInfoRouterRequest request)

Retrieves runtime NAT IP information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       GetNatIpInfoRouterRequest request =
           GetNatIpInfoRouterRequest.newBuilder()
               .setNatName("natName1727733580")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       NatIpInfoResponse response = routersClient.getNatIpInfo(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNatIpInfoRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNatIpInfoRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NatIpInfoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NatIpInfoResponse)` |   
  
### getNatIpInfo(String project, String region, String router)
    
    
    public final NatIpInfoResponse getNatIpInfo(String project, String region, String router)

Retrieves runtime NAT IP information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       NatIpInfoResponse response = routersClient.getNatIpInfo(project, region, router);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Router resource to query for Nat IP information. The name should conform to RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[NatIpInfoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NatIpInfoResponse)` |   
  
### getNatIpInfoCallable()
    
    
    public final UnaryCallable<GetNatIpInfoRouterRequest,NatIpInfoResponse> getNatIpInfoCallable()

Retrieves runtime NAT IP information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       GetNatIpInfoRouterRequest request =
           GetNatIpInfoRouterRequest.newBuilder()
               .setNatName("natName1727733580")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       ApiFuture<NatIpInfoResponse> future =
           routersClient.getNatIpInfoCallable().futureCall(request);
       // Do something.
       NatIpInfoResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNatIpInfoRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNatIpInfoRouterRequest),[NatIpInfoResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NatIpInfoResponse)>` |   
  
### getNatMappingInfo(GetNatMappingInfoRoutersRequest request)
    
    
    public final RoutersClient.GetNatMappingInfoPagedResponse getNatMappingInfo(GetNatMappingInfoRoutersRequest request)

Retrieves runtime Nat mapping information of VM endpoints.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       GetNatMappingInfoRoutersRequest request =
           GetNatMappingInfoRoutersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNatName("natName1727733580")
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       for (VmEndpointNatMappings element : routersClient.getNatMappingInfo(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNatMappingInfoRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNatMappingInfoRoutersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RoutersClient.GetNatMappingInfoPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.GetNatMappingInfoPagedResponse)` |   
  
### getNatMappingInfo(String project, String region, String router)
    
    
    public final RoutersClient.GetNatMappingInfoPagedResponse getNatMappingInfo(String project, String region, String router)

Retrieves runtime Nat mapping information of VM endpoints.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       for (VmEndpointNatMappings element :
           routersClient.getNatMappingInfo(project, region, router).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Router resource to query for Nat Mapping information of VM endpoints.  
**Returns**  
---  
**Type** | **Description**  
`[RoutersClient.GetNatMappingInfoPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.GetNatMappingInfoPagedResponse)` |   
  
### getNatMappingInfoCallable()
    
    
    public final UnaryCallable<GetNatMappingInfoRoutersRequest,VmEndpointNatMappingsList> getNatMappingInfoCallable()

Retrieves runtime Nat mapping information of VM endpoints.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       GetNatMappingInfoRoutersRequest request =
           GetNatMappingInfoRoutersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNatName("natName1727733580")
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       while (true) {
         VmEndpointNatMappingsList response =
             routersClient.getNatMappingInfoCallable().call(request);
         for (VmEndpointNatMappings element : response.getResultList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNatMappingInfoRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNatMappingInfoRoutersRequest),[VmEndpointNatMappingsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.VmEndpointNatMappingsList)>` |   
  
### getNatMappingInfoPagedCallable()
    
    
    public final UnaryCallable<GetNatMappingInfoRoutersRequest,RoutersClient.GetNatMappingInfoPagedResponse> getNatMappingInfoPagedCallable()

Retrieves runtime Nat mapping information of VM endpoints.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       GetNatMappingInfoRoutersRequest request =
           GetNatMappingInfoRoutersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNatName("natName1727733580")
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       ApiFuture<VmEndpointNatMappings> future =
           routersClient.getNatMappingInfoPagedCallable().futureCall(request);
       // Do something.
       for (VmEndpointNatMappings element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNatMappingInfoRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNatMappingInfoRoutersRequest),[GetNatMappingInfoPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.GetNatMappingInfoPagedResponse)>` |   
  
### getRoutePolicy(GetRoutePolicyRouterRequest request)
    
    
    public final RoutersGetRoutePolicyResponse getRoutePolicy(GetRoutePolicyRouterRequest request)

Returns specified Route Policy

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       GetRoutePolicyRouterRequest request =
           GetRoutePolicyRouterRequest.newBuilder()
               .setPolicy("policy-982670030")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       RoutersGetRoutePolicyResponse response = routersClient.getRoutePolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRoutePolicyRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRoutePolicyRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RoutersGetRoutePolicyResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersGetRoutePolicyResponse)` |   
  
### getRoutePolicy(String project, String region, String router)
    
    
    public final RoutersGetRoutePolicyResponse getRoutePolicy(String project, String region, String router)

Returns specified Route Policy

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       RoutersGetRoutePolicyResponse response =
           routersClient.getRoutePolicy(project, region, router);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Router resource to query for the route policy. The name should conform to RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[RoutersGetRoutePolicyResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersGetRoutePolicyResponse)` |   
  
### getRoutePolicyCallable()
    
    
    public final UnaryCallable<GetRoutePolicyRouterRequest,RoutersGetRoutePolicyResponse> getRoutePolicyCallable()

Returns specified Route Policy

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       GetRoutePolicyRouterRequest request =
           GetRoutePolicyRouterRequest.newBuilder()
               .setPolicy("policy-982670030")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       ApiFuture<RoutersGetRoutePolicyResponse> future =
           routersClient.getRoutePolicyCallable().futureCall(request);
       // Do something.
       RoutersGetRoutePolicyResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRoutePolicyRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRoutePolicyRouterRequest),[RoutersGetRoutePolicyResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersGetRoutePolicyResponse)>` |   
  
### getRouterStatus(GetRouterStatusRouterRequest request)
    
    
    public final RouterStatusResponse getRouterStatus(GetRouterStatusRouterRequest request)

Retrieves runtime information of the specified router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       GetRouterStatusRouterRequest request =
           GetRouterStatusRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       RouterStatusResponse response = routersClient.getRouterStatus(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRouterStatusRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRouterStatusRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RouterStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RouterStatusResponse)` |   
  
### getRouterStatus(String project, String region, String router)
    
    
    public final RouterStatusResponse getRouterStatus(String project, String region, String router)

Retrieves runtime information of the specified router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       RouterStatusResponse response = routersClient.getRouterStatus(project, region, router);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Router resource to query.  
**Returns**  
---  
**Type** | **Description**  
`[RouterStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RouterStatusResponse)` |   
  
### getRouterStatusCallable()
    
    
    public final UnaryCallable<GetRouterStatusRouterRequest,RouterStatusResponse> getRouterStatusCallable()

Retrieves runtime information of the specified router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       GetRouterStatusRouterRequest request =
           GetRouterStatusRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       ApiFuture<RouterStatusResponse> future =
           routersClient.getRouterStatusCallable().futureCall(request);
       // Do something.
       RouterStatusResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRouterStatusRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRouterStatusRouterRequest),[RouterStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RouterStatusResponse)>` |   
  
### getSettings()
    
    
    public final @Nullable RoutersSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RoutersSettings` |   
  
### getStub()
    
    
    public RoutersStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RoutersStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RoutersStub)` |   
  
### insertAsync(InsertRouterRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRouterRequest request)

Creates a Router resource in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       InsertRouterRequest request =
           InsertRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouterResource(Router.newBuilder().build())
               .build();
       Operation response = routersClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, Router routerResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, Router routerResource)

Creates a Router resource in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       Router routerResource = Router.newBuilder().build();
       Operation response = routersClient.insertAsync(project, region, routerResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`routerResource` | `[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Router)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRouterRequest,Operation> insertCallable()

Creates a Router resource in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       InsertRouterRequest request =
           InsertRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouterResource(Router.newBuilder().build())
               .build();
       ApiFuture<Operation> future = routersClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRouterRequest,Operation,Operation> insertOperationCallable()

Creates a Router resource in the specified project and region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       InsertRouterRequest request =
           InsertRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouterResource(Router.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           routersClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRoutersRequest request)
    
    
    public final RoutersClient.ListPagedResponse list(ListRoutersRequest request)

Retrieves a list of Router resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       ListRoutersRequest request =
           ListRoutersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (Router element : routersClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRoutersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RoutersClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final RoutersClient.ListPagedResponse list(String project, String region)

Retrieves a list of Router resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (Router element : routersClient.list(project, region).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
**Returns**  
---  
**Type** | **Description**  
`[RoutersClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.ListPagedResponse)` |   
  
### listBgpRoutes(ListBgpRoutesRoutersRequest request)
    
    
    public final RoutersClient.ListBgpRoutesPagedResponse listBgpRoutes(ListBgpRoutesRoutersRequest request)

Retrieves a list of router bgp routes available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       ListBgpRoutesRoutersRequest request =
           ListBgpRoutesRoutersRequest.newBuilder()
               .setAddressFamily("addressFamily-1130029960")
               .setDestinationPrefix("destinationPrefix-1718345664")
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setPeer("peer3436898")
               .setPolicyApplied(true)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouteType("routeType167668003")
               .setRouter("router-925132983")
               .build();
       for (BgpRoute element : routersClient.listBgpRoutes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBgpRoutesRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListBgpRoutesRoutersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RoutersClient.ListBgpRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.ListBgpRoutesPagedResponse)` |   
  
### listBgpRoutes(String project, String region, String router)
    
    
    public final RoutersClient.ListBgpRoutesPagedResponse listBgpRoutes(String project, String region, String router)

Retrieves a list of router bgp routes available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       for (BgpRoute element : routersClient.listBgpRoutes(project, region, router).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request. Name should conform to RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[RoutersClient.ListBgpRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.ListBgpRoutesPagedResponse)` |   
  
### listBgpRoutesCallable()
    
    
    public final UnaryCallable<ListBgpRoutesRoutersRequest,RoutersListBgpRoutes> listBgpRoutesCallable()

Retrieves a list of router bgp routes available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       ListBgpRoutesRoutersRequest request =
           ListBgpRoutesRoutersRequest.newBuilder()
               .setAddressFamily("addressFamily-1130029960")
               .setDestinationPrefix("destinationPrefix-1718345664")
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setPeer("peer3436898")
               .setPolicyApplied(true)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouteType("routeType167668003")
               .setRouter("router-925132983")
               .build();
       while (true) {
         RoutersListBgpRoutes response = routersClient.listBgpRoutesCallable().call(request);
         for (BgpRoute element : response.getResultList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBgpRoutesRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListBgpRoutesRoutersRequest),[RoutersListBgpRoutes](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersListBgpRoutes)>` |   
  
### listBgpRoutesPagedCallable()
    
    
    public final UnaryCallable<ListBgpRoutesRoutersRequest,RoutersClient.ListBgpRoutesPagedResponse> listBgpRoutesPagedCallable()

Retrieves a list of router bgp routes available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       ListBgpRoutesRoutersRequest request =
           ListBgpRoutesRoutersRequest.newBuilder()
               .setAddressFamily("addressFamily-1130029960")
               .setDestinationPrefix("destinationPrefix-1718345664")
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setPeer("peer3436898")
               .setPolicyApplied(true)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouteType("routeType167668003")
               .setRouter("router-925132983")
               .build();
       ApiFuture<BgpRoute> future = routersClient.listBgpRoutesPagedCallable().futureCall(request);
       // Do something.
       for (BgpRoute element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBgpRoutesRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListBgpRoutesRoutersRequest),[ListBgpRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.ListBgpRoutesPagedResponse)>` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRoutersRequest,RouterList> listCallable()

Retrieves a list of Router resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       ListRoutersRequest request =
           ListRoutersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         RouterList response = routersClient.listCallable().call(request);
         for (Router element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRoutersRequest),[RouterList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RouterList)>` |   
  
### listNamedSets(ListNamedSetsRoutersRequest request)
    
    
    public final RoutersClient.ListNamedSetsPagedResponse listNamedSets(ListNamedSetsRoutersRequest request)

Retrieves a list of router named set subresources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       ListNamedSetsRoutersRequest request =
           ListNamedSetsRoutersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       for (NamedSet element : routersClient.listNamedSets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNamedSetsRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNamedSetsRoutersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RoutersClient.ListNamedSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.ListNamedSetsPagedResponse)` |   
  
### listNamedSets(String project, String region, String router)
    
    
    public final RoutersClient.ListNamedSetsPagedResponse listNamedSets(String project, String region, String router)

Retrieves a list of router named set subresources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       for (NamedSet element : routersClient.listNamedSets(project, region, router).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request. Name should conform to RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[RoutersClient.ListNamedSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.ListNamedSetsPagedResponse)` |   
  
### listNamedSetsCallable()
    
    
    public final UnaryCallable<ListNamedSetsRoutersRequest,RoutersListNamedSets> listNamedSetsCallable()

Retrieves a list of router named set subresources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       ListNamedSetsRoutersRequest request =
           ListNamedSetsRoutersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       while (true) {
         RoutersListNamedSets response = routersClient.listNamedSetsCallable().call(request);
         for (NamedSet element : response.getResultList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNamedSetsRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNamedSetsRoutersRequest),[RoutersListNamedSets](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersListNamedSets)>` |   
  
### listNamedSetsPagedCallable()
    
    
    public final UnaryCallable<ListNamedSetsRoutersRequest,RoutersClient.ListNamedSetsPagedResponse> listNamedSetsPagedCallable()

Retrieves a list of router named set subresources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       ListNamedSetsRoutersRequest request =
           ListNamedSetsRoutersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       ApiFuture<NamedSet> future = routersClient.listNamedSetsPagedCallable().futureCall(request);
       // Do something.
       for (NamedSet element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNamedSetsRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNamedSetsRoutersRequest),[ListNamedSetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.ListNamedSetsPagedResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRoutersRequest,RoutersClient.ListPagedResponse> listPagedCallable()

Retrieves a list of Router resources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       ListRoutersRequest request =
           ListRoutersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<Router> future = routersClient.listPagedCallable().futureCall(request);
       // Do something.
       for (Router element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRoutersRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.ListPagedResponse)>` |   
  
### listRoutePolicies(ListRoutePoliciesRoutersRequest request)
    
    
    public final RoutersClient.ListRoutePoliciesPagedResponse listRoutePolicies(ListRoutePoliciesRoutersRequest request)

Retrieves a list of router route policy subresources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       ListRoutePoliciesRoutersRequest request =
           ListRoutePoliciesRoutersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       for (RoutePolicy element : routersClient.listRoutePolicies(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRoutePoliciesRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRoutePoliciesRoutersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RoutersClient.ListRoutePoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.ListRoutePoliciesPagedResponse)` |   
  
### listRoutePolicies(String project, String region, String router)
    
    
    public final RoutersClient.ListRoutePoliciesPagedResponse listRoutePolicies(String project, String region, String router)

Retrieves a list of router route policy subresources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       for (RoutePolicy element :
           routersClient.listRoutePolicies(project, region, router).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request. Name should conform to RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[RoutersClient.ListRoutePoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.ListRoutePoliciesPagedResponse)` |   
  
### listRoutePoliciesCallable()
    
    
    public final UnaryCallable<ListRoutePoliciesRoutersRequest,RoutersListRoutePolicies> listRoutePoliciesCallable()

Retrieves a list of router route policy subresources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       ListRoutePoliciesRoutersRequest request =
           ListRoutePoliciesRoutersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       while (true) {
         RoutersListRoutePolicies response = routersClient.listRoutePoliciesCallable().call(request);
         for (RoutePolicy element : response.getResultList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRoutePoliciesRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRoutePoliciesRoutersRequest),[RoutersListRoutePolicies](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersListRoutePolicies)>` |   
  
### listRoutePoliciesPagedCallable()
    
    
    public final UnaryCallable<ListRoutePoliciesRoutersRequest,RoutersClient.ListRoutePoliciesPagedResponse> listRoutePoliciesPagedCallable()

Retrieves a list of router route policy subresources available to the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       ListRoutePoliciesRoutersRequest request =
           ListRoutePoliciesRoutersRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .build();
       ApiFuture<RoutePolicy> future =
           routersClient.listRoutePoliciesPagedCallable().futureCall(request);
       // Do something.
       for (RoutePolicy element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRoutePoliciesRoutersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRoutePoliciesRoutersRequest),[ListRoutePoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersClient.ListRoutePoliciesPagedResponse)>` |   
  
### patchAsync(PatchRouterRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchRouterRequest request)

Patches the specified Router resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       PatchRouterRequest request =
           PatchRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .setRouterResource(Router.newBuilder().build())
               .build();
       Operation response = routersClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String region, String router, Router routerResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String region, String router, Router routerResource)

Patches the specified Router resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       Router routerResource = Router.newBuilder().build();
       Operation response = routersClient.patchAsync(project, region, router, routerResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Router resource to patch.  
`routerResource` | `[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Router)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchRouterRequest,Operation> patchCallable()

Patches the specified Router resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       PatchRouterRequest request =
           PatchRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .setRouterResource(Router.newBuilder().build())
               .build();
       ApiFuture<Operation> future = routersClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchNamedSetAsync(PatchNamedSetRouterRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchNamedSetAsync(PatchNamedSetRouterRequest request)

Patches Named Set

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       PatchNamedSetRouterRequest request =
           PatchNamedSetRouterRequest.newBuilder()
               .setNamedSetResource(NamedSet.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .build();
       Operation response = routersClient.patchNamedSetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchNamedSetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchNamedSetRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchNamedSetAsync(String project, String region, String router, NamedSet namedSetResource)
    
    
    public final OperationFuture<Operation,Operation> patchNamedSetAsync(String project, String region, String router, NamedSet namedSetResource)

Patches Named Set

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       NamedSet namedSetResource = NamedSet.newBuilder().build();
       Operation response =
           routersClient.patchNamedSetAsync(project, region, router, namedSetResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Router resource where Named Set is defined.  
`namedSetResource` | `[NamedSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NamedSet)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchNamedSetCallable()
    
    
    public final UnaryCallable<PatchNamedSetRouterRequest,Operation> patchNamedSetCallable()

Patches Named Set

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       PatchNamedSetRouterRequest request =
           PatchNamedSetRouterRequest.newBuilder()
               .setNamedSetResource(NamedSet.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .build();
       ApiFuture<Operation> future = routersClient.patchNamedSetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchNamedSetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchNamedSetRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchNamedSetOperationCallable()
    
    
    public final OperationCallable<PatchNamedSetRouterRequest,Operation,Operation> patchNamedSetOperationCallable()

Patches Named Set

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       PatchNamedSetRouterRequest request =
           PatchNamedSetRouterRequest.newBuilder()
               .setNamedSetResource(NamedSet.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .build();
       OperationFuture<Operation, Operation> future =
           routersClient.patchNamedSetOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchNamedSetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchNamedSetRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchRouterRequest,Operation,Operation> patchOperationCallable()

Patches the specified Router resource with the data included in the request. This method supportsPATCH semantics and usesJSON merge patch format and processing rules.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       PatchRouterRequest request =
           PatchRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .setRouterResource(Router.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           routersClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRoutePolicyAsync(PatchRoutePolicyRouterRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchRoutePolicyAsync(PatchRoutePolicyRouterRequest request)

Patches Route Policy

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       PatchRoutePolicyRouterRequest request =
           PatchRoutePolicyRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRoutePolicyResource(RoutePolicy.newBuilder().build())
               .setRouter("router-925132983")
               .build();
       Operation response = routersClient.patchRoutePolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchRoutePolicyRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRoutePolicyRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRoutePolicyAsync(String project, String region, String router, RoutePolicy routePolicyResource)
    
    
    public final OperationFuture<Operation,Operation> patchRoutePolicyAsync(String project, String region, String router, RoutePolicy routePolicyResource)

Patches Route Policy

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       RoutePolicy routePolicyResource = RoutePolicy.newBuilder().build();
       Operation response =
           routersClient.patchRoutePolicyAsync(project, region, router, routePolicyResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Router resource where Route Policy is defined.  
`routePolicyResource` | `[RoutePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutePolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRoutePolicyCallable()
    
    
    public final UnaryCallable<PatchRoutePolicyRouterRequest,Operation> patchRoutePolicyCallable()

Patches Route Policy

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       PatchRoutePolicyRouterRequest request =
           PatchRoutePolicyRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRoutePolicyResource(RoutePolicy.newBuilder().build())
               .setRouter("router-925132983")
               .build();
       ApiFuture<Operation> future = routersClient.patchRoutePolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchRoutePolicyRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRoutePolicyRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRoutePolicyOperationCallable()
    
    
    public final OperationCallable<PatchRoutePolicyRouterRequest,Operation,Operation> patchRoutePolicyOperationCallable()

Patches Route Policy

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       PatchRoutePolicyRouterRequest request =
           PatchRoutePolicyRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRoutePolicyResource(RoutePolicy.newBuilder().build())
               .setRouter("router-925132983")
               .build();
       OperationFuture<Operation, Operation> future =
           routersClient.patchRoutePolicyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchRoutePolicyRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRoutePolicyRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### preview(PreviewRouterRequest request)
    
    
    public final RoutersPreviewResponse preview(PreviewRouterRequest request)

Preview fields auto-generated during router create andupdate operations. Calling this method does NOT create or update the router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       PreviewRouterRequest request =
           PreviewRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .setRouterResource(Router.newBuilder().build())
               .build();
       RoutersPreviewResponse response = routersClient.preview(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PreviewRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RoutersPreviewResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersPreviewResponse)` |   
  
### preview(String project, String region, String router, Router routerResource)
    
    
    public final RoutersPreviewResponse preview(String project, String region, String router, Router routerResource)

Preview fields auto-generated during router create andupdate operations. Calling this method does NOT create or update the router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       Router routerResource = Router.newBuilder().build();
       RoutersPreviewResponse response =
           routersClient.preview(project, region, router, routerResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Router resource to query.  
`routerResource` | `[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Router)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[RoutersPreviewResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersPreviewResponse)` |   
  
### previewCallable()
    
    
    public final UnaryCallable<PreviewRouterRequest,RoutersPreviewResponse> previewCallable()

Preview fields auto-generated during router create andupdate operations. Calling this method does NOT create or update the router.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       PreviewRouterRequest request =
           PreviewRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRouter("router-925132983")
               .setRouterResource(Router.newBuilder().build())
               .build();
       ApiFuture<RoutersPreviewResponse> future =
           routersClient.previewCallable().futureCall(request);
       // Do something.
       RoutersPreviewResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PreviewRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewRouterRequest),[RoutersPreviewResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutersPreviewResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateAsync(UpdateRouterRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(UpdateRouterRequest request)

Updates the specified Router resource with the data included in the request. This method conforms toPUT semantics, which requests that the state of the target resource be created or replaced with the state defined by the representation enclosed in the request message payload.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       UpdateRouterRequest request =
           UpdateRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .setRouterResource(Router.newBuilder().build())
               .build();
       Operation response = routersClient.updateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(String project, String region, String router, Router routerResource)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(String project, String region, String router, Router routerResource)

Updates the specified Router resource with the data included in the request. This method conforms toPUT semantics, which requests that the state of the target resource be created or replaced with the state defined by the representation enclosed in the request message payload.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       Router routerResource = Router.newBuilder().build();
       Operation response = routersClient.updateAsync(project, region, router, routerResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Router resource to update.  
`routerResource` | `[Router](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Router)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateCallable()
    
    
    public final UnaryCallable<UpdateRouterRequest,Operation> updateCallable()

Updates the specified Router resource with the data included in the request. This method conforms toPUT semantics, which requests that the state of the target resource be created or replaced with the state defined by the representation enclosed in the request message payload.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       UpdateRouterRequest request =
           UpdateRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .setRouterResource(Router.newBuilder().build())
               .build();
       ApiFuture<Operation> future = routersClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateNamedSetAsync(UpdateNamedSetRouterRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateNamedSetAsync(UpdateNamedSetRouterRequest request)

Updates or creates new Named Set

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       UpdateNamedSetRouterRequest request =
           UpdateNamedSetRouterRequest.newBuilder()
               .setNamedSetResource(NamedSet.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .build();
       Operation response = routersClient.updateNamedSetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateNamedSetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateNamedSetRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateNamedSetAsync(String project, String region, String router, NamedSet namedSetResource)
    
    
    public final OperationFuture<Operation,Operation> updateNamedSetAsync(String project, String region, String router, NamedSet namedSetResource)

Updates or creates new Named Set

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       NamedSet namedSetResource = NamedSet.newBuilder().build();
       Operation response =
           routersClient.updateNamedSetAsync(project, region, router, namedSetResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Router resource where Named Set is defined.  
`namedSetResource` | `[NamedSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NamedSet)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateNamedSetCallable()
    
    
    public final UnaryCallable<UpdateNamedSetRouterRequest,Operation> updateNamedSetCallable()

Updates or creates new Named Set

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       UpdateNamedSetRouterRequest request =
           UpdateNamedSetRouterRequest.newBuilder()
               .setNamedSetResource(NamedSet.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .build();
       ApiFuture<Operation> future = routersClient.updateNamedSetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateNamedSetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateNamedSetRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateNamedSetOperationCallable()
    
    
    public final OperationCallable<UpdateNamedSetRouterRequest,Operation,Operation> updateNamedSetOperationCallable()

Updates or creates new Named Set

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       UpdateNamedSetRouterRequest request =
           UpdateNamedSetRouterRequest.newBuilder()
               .setNamedSetResource(NamedSet.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .build();
       OperationFuture<Operation, Operation> future =
           routersClient.updateNamedSetOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateNamedSetRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateNamedSetRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationCallable()
    
    
    public final OperationCallable<UpdateRouterRequest,Operation,Operation> updateOperationCallable()

Updates the specified Router resource with the data included in the request. This method conforms toPUT semantics, which requests that the state of the target resource be created or replaced with the state defined by the representation enclosed in the request message payload.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       UpdateRouterRequest request =
           UpdateRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRouter("router-925132983")
               .setRouterResource(Router.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           routersClient.updateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateRoutePolicyAsync(UpdateRoutePolicyRouterRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateRoutePolicyAsync(UpdateRoutePolicyRouterRequest request)

Updates or creates new Route Policy

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       UpdateRoutePolicyRouterRequest request =
           UpdateRoutePolicyRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRoutePolicyResource(RoutePolicy.newBuilder().build())
               .setRouter("router-925132983")
               .build();
       Operation response = routersClient.updateRoutePolicyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRoutePolicyRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateRoutePolicyRouterRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateRoutePolicyAsync(String project, String region, String router, RoutePolicy routePolicyResource)
    
    
    public final OperationFuture<Operation,Operation> updateRoutePolicyAsync(String project, String region, String router, RoutePolicy routePolicyResource)

Updates or creates new Route Policy

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String router = "router-925132983";
       RoutePolicy routePolicyResource = RoutePolicy.newBuilder().build();
       Operation response =
           routersClient.updateRoutePolicyAsync(project, region, router, routePolicyResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`router` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Router resource where Route Policy is defined.  
`routePolicyResource` | `[RoutePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RoutePolicy)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateRoutePolicyCallable()
    
    
    public final UnaryCallable<UpdateRoutePolicyRouterRequest,Operation> updateRoutePolicyCallable()

Updates or creates new Route Policy

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       UpdateRoutePolicyRouterRequest request =
           UpdateRoutePolicyRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRoutePolicyResource(RoutePolicy.newBuilder().build())
               .setRouter("router-925132983")
               .build();
       ApiFuture<Operation> future = routersClient.updateRoutePolicyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRoutePolicyRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateRoutePolicyRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateRoutePolicyOperationCallable()
    
    
    public final OperationCallable<UpdateRoutePolicyRouterRequest,Operation,Operation> updateRoutePolicyOperationCallable()

Updates or creates new Route Policy

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RoutersClient routersClient = RoutersClient.create()) {
       UpdateRoutePolicyRouterRequest request =
           UpdateRoutePolicyRouterRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setRoutePolicyResource(RoutePolicy.newBuilder().build())
               .setRouter("router-925132983")
               .build();
       OperationFuture<Operation, Operation> future =
           routersClient.updateRoutePolicyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateRoutePolicyRouterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateRoutePolicyRouterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
