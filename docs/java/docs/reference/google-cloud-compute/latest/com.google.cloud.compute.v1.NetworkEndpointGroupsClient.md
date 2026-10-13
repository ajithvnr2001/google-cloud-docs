---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsClient
title: Class NetworkEndpointGroupsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:05.074725+00:00
---

# Class NetworkEndpointGroupsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NetworkEndpointGroupsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/NetworkEndpointGroupsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The NetworkEndpointGroups API.

This client uses NetworkEndpointGroups version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       NetworkEndpointGroup response =
           networkEndpointGroupsClient.get(project, zone, networkEndpointGroup);
     }
     

Note: close() needs to be called on the NetworkEndpointGroupsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AggregatedList |  Retrieves the list of network endpoint groups and sorts them by zone.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListNetworkEndpointGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
AttachNetworkEndpoints |  Attach a list of network endpoints to the specified network endpoint group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * attachNetworkEndpointsAsync(AttachNetworkEndpointsNetworkEndpointGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * attachNetworkEndpointsAsync(String project, String zone, String networkEndpointGroup, NetworkEndpointGroupsAttachEndpointsRequest networkEndpointGroupsAttachEndpointsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * attachNetworkEndpointsOperationCallable() 
  * attachNetworkEndpointsCallable() 

  
Delete |  Deletes the specified network endpoint group. The network endpoints in the NEG and the VM instances they belong to are not terminated when the NEG is deleted. Note that the NEG cannot be deleted if there are backend services referencing it. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteNetworkEndpointGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String zone, String networkEndpointGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
DetachNetworkEndpoints |  Detach a list of network endpoints from the specified network endpoint group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * detachNetworkEndpointsAsync(DetachNetworkEndpointsNetworkEndpointGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * detachNetworkEndpointsAsync(String project, String zone, String networkEndpointGroup, NetworkEndpointGroupsDetachEndpointsRequest networkEndpointGroupsDetachEndpointsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * detachNetworkEndpointsOperationCallable() 
  * detachNetworkEndpointsCallable() 

  
Get |  Returns the specified network endpoint group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetNetworkEndpointGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String networkEndpointGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a network endpoint group in the specified project using the parameters that are included in the request.  Note: Use the following APIs to manage network endpoint groups:  \- To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API - To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API - To manage NEGs with global scope (such as global internet NEGs):global API |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertNetworkEndpointGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String zone, NetworkEndpointGroup networkEndpointGroupResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of network endpoint groups that are located in the specified project and zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListNetworkEndpointGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListNetworkEndpoints |  Lists the network endpoints in the specified network endpoint group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNetworkEndpoints(ListNetworkEndpointsNetworkEndpointGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNetworkEndpoints(String project, String zone, String networkEndpointGroup, NetworkEndpointGroupsListEndpointsRequest networkEndpointGroupsListEndpointsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNetworkEndpointsPagedCallable() 
  * listNetworkEndpointsCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsNetworkEndpointGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String zone, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of NetworkEndpointGroupsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworkEndpointGroupsSettings networkEndpointGroupsSettings =
         NetworkEndpointGroupsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create(networkEndpointGroupsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworkEndpointGroupsSettings networkEndpointGroupsSettings =
         NetworkEndpointGroupsSettings.newBuilder().setEndpoint(myEndpoint).build();
     NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create(networkEndpointGroupsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > NetworkEndpointGroupsClient

## Static Methods 

### create()
    
    
    public static final NetworkEndpointGroupsClient create()

Constructs an instance of NetworkEndpointGroupsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NetworkEndpointGroupsSettings settings)
    
    
    public static final NetworkEndpointGroupsClient create(NetworkEndpointGroupsSettings settings)

Constructs an instance of NetworkEndpointGroupsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NetworkEndpointGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NetworkEndpointGroupsStub stub)
    
    
    public static final NetworkEndpointGroupsClient create(NetworkEndpointGroupsStub stub)

Constructs an instance of NetworkEndpointGroupsClient, using the given stub for making calls. This is for advanced usage - prefer using create(NetworkEndpointGroupsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NetworkEndpointGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.NetworkEndpointGroupsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsClient)` |   
  
## Constructors 

### NetworkEndpointGroupsClient(NetworkEndpointGroupsSettings settings)
    
    
    protected NetworkEndpointGroupsClient(NetworkEndpointGroupsSettings settings)

Constructs an instance of NetworkEndpointGroupsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NetworkEndpointGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsSettings)`  
  
  
### NetworkEndpointGroupsClient(NetworkEndpointGroupsStub stub)
    
    
    protected NetworkEndpointGroupsClient(NetworkEndpointGroupsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NetworkEndpointGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.NetworkEndpointGroupsStub)`  
  
  
## Methods 

### aggregatedList(AggregatedListNetworkEndpointGroupsRequest request)
    
    
    public final NetworkEndpointGroupsClient.AggregatedListPagedResponse aggregatedList(AggregatedListNetworkEndpointGroupsRequest request)

Retrieves the list of network endpoint groups and sorts them by zone.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       AggregatedListNetworkEndpointGroupsRequest request =
           AggregatedListNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, NetworkEndpointGroupsScopedList> element :
           networkEndpointGroupsClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListNetworkEndpointGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final NetworkEndpointGroupsClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves the list of network endpoint groups and sorts them by zone.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, NetworkEndpointGroupsScopedList> element :
           networkEndpointGroupsClient.aggregatedList(project).iterateAll()) {
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
`[NetworkEndpointGroupsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListNetworkEndpointGroupsRequest,NetworkEndpointGroupAggregatedList> aggregatedListCallable()

Retrieves the list of network endpoint groups and sorts them by zone.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       AggregatedListNetworkEndpointGroupsRequest request =
           AggregatedListNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         NetworkEndpointGroupAggregatedList response =
             networkEndpointGroupsClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, NetworkEndpointGroupsScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListNetworkEndpointGroupsRequest),[NetworkEndpointGroupAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListNetworkEndpointGroupsRequest,NetworkEndpointGroupsClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves the list of network endpoint groups and sorts them by zone.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       AggregatedListNetworkEndpointGroupsRequest request =
           AggregatedListNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, NetworkEndpointGroupsScopedList>> future =
           networkEndpointGroupsClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, NetworkEndpointGroupsScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListNetworkEndpointGroupsRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsClient.AggregatedListPagedResponse)>` |   
  
### attachNetworkEndpointsAsync(AttachNetworkEndpointsNetworkEndpointGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> attachNetworkEndpointsAsync(AttachNetworkEndpointsNetworkEndpointGroupRequest request)

Attach a list of network endpoints to the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       AttachNetworkEndpointsNetworkEndpointGroupRequest request =
           AttachNetworkEndpointsNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setNetworkEndpointGroupsAttachEndpointsRequestResource(
                   NetworkEndpointGroupsAttachEndpointsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = networkEndpointGroupsClient.attachNetworkEndpointsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AttachNetworkEndpointsNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachNetworkEndpointsNetworkEndpointGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### attachNetworkEndpointsAsync(String project, String zone, String networkEndpointGroup, NetworkEndpointGroupsAttachEndpointsRequest networkEndpointGroupsAttachEndpointsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> attachNetworkEndpointsAsync(String project, String zone, String networkEndpointGroup, NetworkEndpointGroupsAttachEndpointsRequest networkEndpointGroupsAttachEndpointsRequestResource)

Attach a list of network endpoints to the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       NetworkEndpointGroupsAttachEndpointsRequest
           networkEndpointGroupsAttachEndpointsRequestResource =
               NetworkEndpointGroupsAttachEndpointsRequest.newBuilder().build();
       Operation response =
           networkEndpointGroupsClient
               .attachNetworkEndpointsAsync(
                   project,
                   zone,
                   networkEndpointGroup,
                   networkEndpointGroupsAttachEndpointsRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone where the network endpoint group is located. It should comply with RFC1035.  
`networkEndpointGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network endpoint group where you are attaching network endpoints to. It should comply with RFC1035.  
`networkEndpointGroupsAttachEndpointsRequestResource` | `[NetworkEndpointGroupsAttachEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsAttachEndpointsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### attachNetworkEndpointsCallable()
    
    
    public final UnaryCallable<AttachNetworkEndpointsNetworkEndpointGroupRequest,Operation> attachNetworkEndpointsCallable()

Attach a list of network endpoints to the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       AttachNetworkEndpointsNetworkEndpointGroupRequest request =
           AttachNetworkEndpointsNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setNetworkEndpointGroupsAttachEndpointsRequestResource(
                   NetworkEndpointGroupsAttachEndpointsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           networkEndpointGroupsClient.attachNetworkEndpointsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AttachNetworkEndpointsNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachNetworkEndpointsNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### attachNetworkEndpointsOperationCallable()
    
    
    public final OperationCallable<AttachNetworkEndpointsNetworkEndpointGroupRequest,Operation,Operation> attachNetworkEndpointsOperationCallable()

Attach a list of network endpoints to the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       AttachNetworkEndpointsNetworkEndpointGroupRequest request =
           AttachNetworkEndpointsNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setNetworkEndpointGroupsAttachEndpointsRequestResource(
                   NetworkEndpointGroupsAttachEndpointsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           networkEndpointGroupsClient.attachNetworkEndpointsOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AttachNetworkEndpointsNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachNetworkEndpointsNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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

### deleteAsync(DeleteNetworkEndpointGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteNetworkEndpointGroupRequest request)

Deletes the specified network endpoint group. The network endpoints in the NEG and the VM instances they belong to are not terminated when the NEG is deleted. Note that the NEG cannot be deleted if there are backend services referencing it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       DeleteNetworkEndpointGroupRequest request =
           DeleteNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = networkEndpointGroupsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkEndpointGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String zone, String networkEndpointGroup)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String zone, String networkEndpointGroup)

Deletes the specified network endpoint group. The network endpoints in the NEG and the VM instances they belong to are not terminated when the NEG is deleted. Note that the NEG cannot be deleted if there are backend services referencing it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       Operation response =
           networkEndpointGroupsClient.deleteAsync(project, zone, networkEndpointGroup).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone where the network endpoint group is located. It should comply with RFC1035.  
`networkEndpointGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network endpoint group to delete. It should comply with RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteNetworkEndpointGroupRequest,Operation> deleteCallable()

Deletes the specified network endpoint group. The network endpoints in the NEG and the VM instances they belong to are not terminated when the NEG is deleted. Note that the NEG cannot be deleted if there are backend services referencing it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       DeleteNetworkEndpointGroupRequest request =
           DeleteNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           networkEndpointGroupsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteNetworkEndpointGroupRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified network endpoint group. The network endpoints in the NEG and the VM instances they belong to are not terminated when the NEG is deleted. Note that the NEG cannot be deleted if there are backend services referencing it.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       DeleteNetworkEndpointGroupRequest request =
           DeleteNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           networkEndpointGroupsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachNetworkEndpointsAsync(DetachNetworkEndpointsNetworkEndpointGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> detachNetworkEndpointsAsync(DetachNetworkEndpointsNetworkEndpointGroupRequest request)

Detach a list of network endpoints from the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       DetachNetworkEndpointsNetworkEndpointGroupRequest request =
           DetachNetworkEndpointsNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setNetworkEndpointGroupsDetachEndpointsRequestResource(
                   NetworkEndpointGroupsDetachEndpointsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = networkEndpointGroupsClient.detachNetworkEndpointsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DetachNetworkEndpointsNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DetachNetworkEndpointsNetworkEndpointGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachNetworkEndpointsAsync(String project, String zone, String networkEndpointGroup, NetworkEndpointGroupsDetachEndpointsRequest networkEndpointGroupsDetachEndpointsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> detachNetworkEndpointsAsync(String project, String zone, String networkEndpointGroup, NetworkEndpointGroupsDetachEndpointsRequest networkEndpointGroupsDetachEndpointsRequestResource)

Detach a list of network endpoints from the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       NetworkEndpointGroupsDetachEndpointsRequest
           networkEndpointGroupsDetachEndpointsRequestResource =
               NetworkEndpointGroupsDetachEndpointsRequest.newBuilder().build();
       Operation response =
           networkEndpointGroupsClient
               .detachNetworkEndpointsAsync(
                   project,
                   zone,
                   networkEndpointGroup,
                   networkEndpointGroupsDetachEndpointsRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone where the network endpoint group is located. It should comply with RFC1035.  
`networkEndpointGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network endpoint group where you are removing network endpoints. It should comply with RFC1035.  
`networkEndpointGroupsDetachEndpointsRequestResource` | `[NetworkEndpointGroupsDetachEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsDetachEndpointsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachNetworkEndpointsCallable()
    
    
    public final UnaryCallable<DetachNetworkEndpointsNetworkEndpointGroupRequest,Operation> detachNetworkEndpointsCallable()

Detach a list of network endpoints from the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       DetachNetworkEndpointsNetworkEndpointGroupRequest request =
           DetachNetworkEndpointsNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setNetworkEndpointGroupsDetachEndpointsRequestResource(
                   NetworkEndpointGroupsDetachEndpointsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           networkEndpointGroupsClient.detachNetworkEndpointsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DetachNetworkEndpointsNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DetachNetworkEndpointsNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### detachNetworkEndpointsOperationCallable()
    
    
    public final OperationCallable<DetachNetworkEndpointsNetworkEndpointGroupRequest,Operation,Operation> detachNetworkEndpointsOperationCallable()

Detach a list of network endpoints from the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       DetachNetworkEndpointsNetworkEndpointGroupRequest request =
           DetachNetworkEndpointsNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setNetworkEndpointGroupsDetachEndpointsRequestResource(
                   NetworkEndpointGroupsDetachEndpointsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           networkEndpointGroupsClient.detachNetworkEndpointsOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DetachNetworkEndpointsNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DetachNetworkEndpointsNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetNetworkEndpointGroupRequest request)
    
    
    public final NetworkEndpointGroup get(GetNetworkEndpointGroupRequest request)

Returns the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       GetNetworkEndpointGroupRequest request =
           GetNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       NetworkEndpointGroup response = networkEndpointGroupsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNetworkEndpointGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroup)` |   
  
### get(String project, String zone, String networkEndpointGroup)
    
    
    public final NetworkEndpointGroup get(String project, String zone, String networkEndpointGroup)

Returns the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       NetworkEndpointGroup response =
           networkEndpointGroupsClient.get(project, zone, networkEndpointGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone where the network endpoint group is located. It should comply with RFC1035.  
`networkEndpointGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network endpoint group. It should comply with RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroup)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetNetworkEndpointGroupRequest,NetworkEndpointGroup> getCallable()

Returns the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       GetNetworkEndpointGroupRequest request =
           GetNetworkEndpointGroupRequest.newBuilder()
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<NetworkEndpointGroup> future =
           networkEndpointGroupsClient.getCallable().futureCall(request);
       // Do something.
       NetworkEndpointGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNetworkEndpointGroupRequest),[NetworkEndpointGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroup)>` |   
  
### getSettings()
    
    
    public final @Nullable NetworkEndpointGroupsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.NetworkEndpointGroupsSettings` |   
  
### getStub()
    
    
    public NetworkEndpointGroupsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.NetworkEndpointGroupsStub)` |   
  
### insertAsync(InsertNetworkEndpointGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertNetworkEndpointGroupRequest request)

Creates a network endpoint group in the specified project using the parameters that are included in the request.

Note: Use the following APIs to manage network endpoint groups:

\- To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API

  * To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API - To manage NEGs with global scope (such as global internet NEGs):global API

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
          NetworkEndpointGroupsClient.create()) {
        InsertNetworkEndpointGroupRequest request =
            InsertNetworkEndpointGroupRequest.newBuilder()
                .setNetworkEndpointGroupResource(NetworkEndpointGroup.newBuilder().build())
                .setProject("project-309310695")
                .setRequestId("requestId693933066")
                .setZone("zone3744684")
                .build();
        Operation response = networkEndpointGroupsClient.insertAsync(request).get();
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertNetworkEndpointGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String zone, NetworkEndpointGroup networkEndpointGroupResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String zone, NetworkEndpointGroup networkEndpointGroupResource)

Creates a network endpoint group in the specified project using the parameters that are included in the request.

Note: Use the following APIs to manage network endpoint groups:

\- To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API

  * To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API - To manage NEGs with global scope (such as global internet NEGs):global API

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
          NetworkEndpointGroupsClient.create()) {
        String project = "project-309310695";
        String zone = "zone3744684";
        NetworkEndpointGroup networkEndpointGroupResource = NetworkEndpointGroup.newBuilder().build();
        Operation response =
            networkEndpointGroupsClient
                .insertAsync(project, zone, networkEndpointGroupResource)
                .get();
        }
        




**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone where you want to create the network endpoint group. It should comply with RFC1035.  
`networkEndpointGroupResource` | `[NetworkEndpointGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroup)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertNetworkEndpointGroupRequest,Operation> insertCallable()

Creates a network endpoint group in the specified project using the parameters that are included in the request.

Note: Use the following APIs to manage network endpoint groups:

\- To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API

  * To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API - To manage NEGs with global scope (such as global internet NEGs):global API

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
          NetworkEndpointGroupsClient.create()) {
        InsertNetworkEndpointGroupRequest request =
            InsertNetworkEndpointGroupRequest.newBuilder()
                .setNetworkEndpointGroupResource(NetworkEndpointGroup.newBuilder().build())
                .setProject("project-309310695")
                .setRequestId("requestId693933066")
                .setZone("zone3744684")
                .build();
        ApiFuture<Operation> future =
            networkEndpointGroupsClient.insertCallable().futureCall(request);
        // Do something.
        Operation response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertNetworkEndpointGroupRequest,Operation,Operation> insertOperationCallable()

Creates a network endpoint group in the specified project using the parameters that are included in the request.

Note: Use the following APIs to manage network endpoint groups:

\- To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API

  * To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API - To manage NEGs with global scope (such as global internet NEGs):global API

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
          NetworkEndpointGroupsClient.create()) {
        InsertNetworkEndpointGroupRequest request =
            InsertNetworkEndpointGroupRequest.newBuilder()
                .setNetworkEndpointGroupResource(NetworkEndpointGroup.newBuilder().build())
                .setProject("project-309310695")
                .setRequestId("requestId693933066")
                .setZone("zone3744684")
                .build();
        OperationFuture<Operation, Operation> future =
            networkEndpointGroupsClient.insertOperationCallable().futureCall(request);
        // Do something.
        Operation response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertNetworkEndpointGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListNetworkEndpointGroupsRequest request)
    
    
    public final NetworkEndpointGroupsClient.ListPagedResponse list(ListNetworkEndpointGroupsRequest request)

Retrieves the list of network endpoint groups that are located in the specified project and zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       ListNetworkEndpointGroupsRequest request =
           ListNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (NetworkEndpointGroup element : networkEndpointGroupsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworkEndpointGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsClient.ListPagedResponse)` |   
  
### list(String project, String zone)
    
    
    public final NetworkEndpointGroupsClient.ListPagedResponse list(String project, String zone)

Retrieves the list of network endpoint groups that are located in the specified project and zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       for (NetworkEndpointGroup element :
           networkEndpointGroupsClient.list(project, zone).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the network endpoint group is located. It should comply with RFC1035.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListNetworkEndpointGroupsRequest,NetworkEndpointGroupList> listCallable()

Retrieves the list of network endpoint groups that are located in the specified project and zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       ListNetworkEndpointGroupsRequest request =
           ListNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         NetworkEndpointGroupList response =
             networkEndpointGroupsClient.listCallable().call(request);
         for (NetworkEndpointGroup element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworkEndpointGroupsRequest),[NetworkEndpointGroupList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupList)>` |   
  
### listNetworkEndpoints(ListNetworkEndpointsNetworkEndpointGroupsRequest request)
    
    
    public final NetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse listNetworkEndpoints(ListNetworkEndpointsNetworkEndpointGroupsRequest request)

Lists the network endpoints in the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       ListNetworkEndpointsNetworkEndpointGroupsRequest request =
           ListNetworkEndpointsNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setNetworkEndpointGroupsListEndpointsRequestResource(
                   NetworkEndpointGroupsListEndpointsRequest.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (NetworkEndpointWithHealthStatus element :
           networkEndpointGroupsClient.listNetworkEndpoints(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNetworkEndpointsNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworkEndpointsNetworkEndpointGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse)` |   
  
### listNetworkEndpoints(String project, String zone, String networkEndpointGroup, NetworkEndpointGroupsListEndpointsRequest networkEndpointGroupsListEndpointsRequestResource)
    
    
    public final NetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse listNetworkEndpoints(String project, String zone, String networkEndpointGroup, NetworkEndpointGroupsListEndpointsRequest networkEndpointGroupsListEndpointsRequestResource)

Lists the network endpoints in the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String networkEndpointGroup = "networkEndpointGroup-2120389028";
       NetworkEndpointGroupsListEndpointsRequest networkEndpointGroupsListEndpointsRequestResource =
           NetworkEndpointGroupsListEndpointsRequest.newBuilder().build();
       for (NetworkEndpointWithHealthStatus element :
           networkEndpointGroupsClient
               .listNetworkEndpoints(
                   project,
                   zone,
                   networkEndpointGroup,
                   networkEndpointGroupsListEndpointsRequestResource)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone where the network endpoint group is located. It should comply with RFC1035.  
`networkEndpointGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the network endpoint group from which you want to generate a list of included network endpoints. It should comply with RFC1035.  
`networkEndpointGroupsListEndpointsRequestResource` | `[NetworkEndpointGroupsListEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsListEndpointsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse)` |   
  
### listNetworkEndpointsCallable()
    
    
    public final UnaryCallable<ListNetworkEndpointsNetworkEndpointGroupsRequest,NetworkEndpointGroupsListNetworkEndpoints> listNetworkEndpointsCallable()

Lists the network endpoints in the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       ListNetworkEndpointsNetworkEndpointGroupsRequest request =
           ListNetworkEndpointsNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setNetworkEndpointGroupsListEndpointsRequestResource(
                   NetworkEndpointGroupsListEndpointsRequest.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         NetworkEndpointGroupsListNetworkEndpoints response =
             networkEndpointGroupsClient.listNetworkEndpointsCallable().call(request);
         for (NetworkEndpointWithHealthStatus element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworkEndpointsNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworkEndpointsNetworkEndpointGroupsRequest),[NetworkEndpointGroupsListNetworkEndpoints](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsListNetworkEndpoints)>` |   
  
### listNetworkEndpointsPagedCallable()
    
    
    public final UnaryCallable<ListNetworkEndpointsNetworkEndpointGroupsRequest,NetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse> listNetworkEndpointsPagedCallable()

Lists the network endpoints in the specified network endpoint group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       ListNetworkEndpointsNetworkEndpointGroupsRequest request =
           ListNetworkEndpointsNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNetworkEndpointGroup("networkEndpointGroup-2120389028")
               .setNetworkEndpointGroupsListEndpointsRequestResource(
                   NetworkEndpointGroupsListEndpointsRequest.newBuilder().build())
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<NetworkEndpointWithHealthStatus> future =
           networkEndpointGroupsClient.listNetworkEndpointsPagedCallable().futureCall(request);
       // Do something.
       for (NetworkEndpointWithHealthStatus element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworkEndpointsNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworkEndpointsNetworkEndpointGroupsRequest),[ListNetworkEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsClient.ListNetworkEndpointsPagedResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListNetworkEndpointGroupsRequest,NetworkEndpointGroupsClient.ListPagedResponse> listPagedCallable()

Retrieves the list of network endpoint groups that are located in the specified project and zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       ListNetworkEndpointGroupsRequest request =
           ListNetworkEndpointGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<NetworkEndpointGroup> future =
           networkEndpointGroupsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (NetworkEndpointGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNetworkEndpointGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNetworkEndpointGroupsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkEndpointGroupsClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsNetworkEndpointGroupRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsNetworkEndpointGroupRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       TestIamPermissionsNetworkEndpointGroupRequest request =
           TestIamPermissionsNetworkEndpointGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       TestPermissionsResponse response = networkEndpointGroupsClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsNetworkEndpointGroupRequest)`  
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
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           networkEndpointGroupsClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsNetworkEndpointGroupRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NetworkEndpointGroupsClient networkEndpointGroupsClient =
         NetworkEndpointGroupsClient.create()) {
       TestIamPermissionsNetworkEndpointGroupRequest request =
           TestIamPermissionsNetworkEndpointGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<TestPermissionsResponse> future =
           networkEndpointGroupsClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsNetworkEndpointGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsNetworkEndpointGroupRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
