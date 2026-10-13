---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsClient
title: Class NodeGroupsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:11.105520+00:00
---

# Class NodeGroupsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NodeGroupsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/NodeGroupsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The NodeGroups API.

This client uses NodeGroups version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String nodeGroup = "nodeGroup443599261";
       NodeGroup response = nodeGroupsClient.get(project, zone, nodeGroup);
     }
     

Note: close() needs to be called on the NodeGroupsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AddNodes |  Adds specified number of nodes to the node group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addNodesAsync(AddNodesNodeGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addNodesAsync(String project, String zone, String nodeGroup, NodeGroupsAddNodesRequest nodeGroupsAddNodesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addNodesOperationCallable() 
  * addNodesCallable() 

  
AggregatedList |  Retrieves an aggregated list of node groups. Note: use nodeGroups.listNodes for more details about each group.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListNodeGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified NodeGroup resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteNodeGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String zone, String nodeGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
DeleteNodes |  Deletes specified nodes from the node group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteNodesAsync(DeleteNodesNodeGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteNodesAsync(String project, String zone, String nodeGroup, NodeGroupsDeleteNodesRequest nodeGroupsDeleteNodesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteNodesOperationCallable() 
  * deleteNodesCallable() 

  
Get |  Returns the specified NodeGroup. Get a list of available NodeGroups by making a list() request. Note: the "nodes" field should not be used. Use nodeGroups.listNodes instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetNodeGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String nodeGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyNodeGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String zone, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
Insert |  Creates a NodeGroup resource in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertNodeGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String zone, int initialNodeCount, NodeGroup nodeGroupResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves a list of node groups available to the specified project. Note: use nodeGroups.listNodes for more details about each group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListNodeGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListNodes |  Lists nodes in the node group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listNodes(ListNodesNodeGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listNodes(String project, String zone, String nodeGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listNodesPagedCallable() 
  * listNodesCallable() 

  
Patch |  Updates the specified node group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * patchAsync(PatchNodeGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * patchAsync(String project, String zone, String nodeGroup, NodeGroup nodeGroupResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * patchOperationCallable() 
  * patchCallable() 

  
PerformMaintenance |  Perform maintenance on a subset of nodes in the node group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * performMaintenanceAsync(PerformMaintenanceNodeGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * performMaintenanceAsync(String project, String zone, String nodeGroup, NodeGroupsPerformMaintenanceRequest nodeGroupsPerformMaintenanceRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * performMaintenanceOperationCallable() 
  * performMaintenanceCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyNodeGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String zone, String resource, ZoneSetPolicyRequest zoneSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
SetNodeTemplate |  Updates the node template of the node group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setNodeTemplateAsync(SetNodeTemplateNodeGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setNodeTemplateAsync(String project, String zone, String nodeGroup, NodeGroupsSetNodeTemplateRequest nodeGroupsSetNodeTemplateRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setNodeTemplateOperationCallable() 
  * setNodeTemplateCallable() 

  
SimulateMaintenanceEvent |  Simulates maintenance event on specified nodes from the node group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * simulateMaintenanceEventAsync(SimulateMaintenanceEventNodeGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * simulateMaintenanceEventAsync(String project, String zone, String nodeGroup, NodeGroupsSimulateMaintenanceEventRequest nodeGroupsSimulateMaintenanceEventRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * simulateMaintenanceEventOperationCallable() 
  * simulateMaintenanceEventCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsNodeGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String zone, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of NodeGroupsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NodeGroupsSettings nodeGroupsSettings =
         NodeGroupsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create(nodeGroupsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NodeGroupsSettings nodeGroupsSettings =
         NodeGroupsSettings.newBuilder().setEndpoint(myEndpoint).build();
     NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create(nodeGroupsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > NodeGroupsClient

## Static Methods 

### create()
    
    
    public static final NodeGroupsClient create()

Constructs an instance of NodeGroupsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[NodeGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NodeGroupsSettings settings)
    
    
    public static final NodeGroupsClient create(NodeGroupsSettings settings)

Constructs an instance of NodeGroupsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NodeGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NodeGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(NodeGroupsStub stub)
    
    
    public static final NodeGroupsClient create(NodeGroupsStub stub)

Constructs an instance of NodeGroupsClient, using the given stub for making calls. This is for advanced usage - prefer using create(NodeGroupsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NodeGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.NodeGroupsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NodeGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsClient)` |   
  
## Constructors 

### NodeGroupsClient(NodeGroupsSettings settings)
    
    
    protected NodeGroupsClient(NodeGroupsSettings settings)

Constructs an instance of NodeGroupsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[NodeGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsSettings)`  
  
  
### NodeGroupsClient(NodeGroupsStub stub)
    
    
    protected NodeGroupsClient(NodeGroupsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NodeGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.NodeGroupsStub)`  
  
  
## Methods 

### addNodesAsync(AddNodesNodeGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> addNodesAsync(AddNodesNodeGroupRequest request)

Adds specified number of nodes to the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       AddNodesNodeGroupRequest request =
           AddNodesNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupsAddNodesRequestResource(NodeGroupsAddNodesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = nodeGroupsClient.addNodesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddNodesNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddNodesNodeGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addNodesAsync(String project, String zone, String nodeGroup, NodeGroupsAddNodesRequest nodeGroupsAddNodesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> addNodesAsync(String project, String zone, String nodeGroup, NodeGroupsAddNodesRequest nodeGroupsAddNodesRequestResource)

Adds specified number of nodes to the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String nodeGroup = "nodeGroup443599261";
       NodeGroupsAddNodesRequest nodeGroupsAddNodesRequestResource =
           NodeGroupsAddNodesRequest.newBuilder().build();
       Operation response =
           nodeGroupsClient
               .addNodesAsync(project, zone, nodeGroup, nodeGroupsAddNodesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`nodeGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the NodeGroup resource.  
`nodeGroupsAddNodesRequestResource` | `[NodeGroupsAddNodesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsAddNodesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addNodesCallable()
    
    
    public final UnaryCallable<AddNodesNodeGroupRequest,Operation> addNodesCallable()

Adds specified number of nodes to the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       AddNodesNodeGroupRequest request =
           AddNodesNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupsAddNodesRequestResource(NodeGroupsAddNodesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = nodeGroupsClient.addNodesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddNodesNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddNodesNodeGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addNodesOperationCallable()
    
    
    public final OperationCallable<AddNodesNodeGroupRequest,Operation,Operation> addNodesOperationCallable()

Adds specified number of nodes to the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       AddNodesNodeGroupRequest request =
           AddNodesNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupsAddNodesRequestResource(NodeGroupsAddNodesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           nodeGroupsClient.addNodesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddNodesNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddNodesNodeGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### aggregatedList(AggregatedListNodeGroupsRequest request)
    
    
    public final NodeGroupsClient.AggregatedListPagedResponse aggregatedList(AggregatedListNodeGroupsRequest request)

Retrieves an aggregated list of node groups. Note: use nodeGroups.listNodes for more details about each group.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       AggregatedListNodeGroupsRequest request =
           AggregatedListNodeGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, NodeGroupsScopedList> element :
           nodeGroupsClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListNodeGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListNodeGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NodeGroupsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final NodeGroupsClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves an aggregated list of node groups. Note: use nodeGroups.listNodes for more details about each group.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, NodeGroupsScopedList> element :
           nodeGroupsClient.aggregatedList(project).iterateAll()) {
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
`[NodeGroupsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListNodeGroupsRequest,NodeGroupAggregatedList> aggregatedListCallable()

Retrieves an aggregated list of node groups. Note: use nodeGroups.listNodes for more details about each group.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       AggregatedListNodeGroupsRequest request =
           AggregatedListNodeGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         NodeGroupAggregatedList response = nodeGroupsClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, NodeGroupsScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListNodeGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListNodeGroupsRequest),[NodeGroupAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListNodeGroupsRequest,NodeGroupsClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves an aggregated list of node groups. Note: use nodeGroups.listNodes for more details about each group.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       AggregatedListNodeGroupsRequest request =
           AggregatedListNodeGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, NodeGroupsScopedList>> future =
           nodeGroupsClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, NodeGroupsScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListNodeGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListNodeGroupsRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteNodeGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteNodeGroupRequest request)

Deletes the specified NodeGroup resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       DeleteNodeGroupRequest request =
           DeleteNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = nodeGroupsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNodeGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String zone, String nodeGroup)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String zone, String nodeGroup)

Deletes the specified NodeGroup resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String nodeGroup = "nodeGroup443599261";
       Operation response = nodeGroupsClient.deleteAsync(project, zone, nodeGroup).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`nodeGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the NodeGroup resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteNodeGroupRequest,Operation> deleteCallable()

Deletes the specified NodeGroup resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       DeleteNodeGroupRequest request =
           DeleteNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = nodeGroupsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNodeGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteNodesAsync(DeleteNodesNodeGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteNodesAsync(DeleteNodesNodeGroupRequest request)

Deletes specified nodes from the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       DeleteNodesNodeGroupRequest request =
           DeleteNodesNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupsDeleteNodesRequestResource(
                   NodeGroupsDeleteNodesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = nodeGroupsClient.deleteNodesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNodesNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNodesNodeGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteNodesAsync(String project, String zone, String nodeGroup, NodeGroupsDeleteNodesRequest nodeGroupsDeleteNodesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> deleteNodesAsync(String project, String zone, String nodeGroup, NodeGroupsDeleteNodesRequest nodeGroupsDeleteNodesRequestResource)

Deletes specified nodes from the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String nodeGroup = "nodeGroup443599261";
       NodeGroupsDeleteNodesRequest nodeGroupsDeleteNodesRequestResource =
           NodeGroupsDeleteNodesRequest.newBuilder().build();
       Operation response =
           nodeGroupsClient
               .deleteNodesAsync(project, zone, nodeGroup, nodeGroupsDeleteNodesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`nodeGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the NodeGroup resource whose nodes will be deleted.  
`nodeGroupsDeleteNodesRequestResource` | `[NodeGroupsDeleteNodesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsDeleteNodesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteNodesCallable()
    
    
    public final UnaryCallable<DeleteNodesNodeGroupRequest,Operation> deleteNodesCallable()

Deletes specified nodes from the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       DeleteNodesNodeGroupRequest request =
           DeleteNodesNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupsDeleteNodesRequestResource(
                   NodeGroupsDeleteNodesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = nodeGroupsClient.deleteNodesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteNodesNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNodesNodeGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteNodesOperationCallable()
    
    
    public final OperationCallable<DeleteNodesNodeGroupRequest,Operation,Operation> deleteNodesOperationCallable()

Deletes specified nodes from the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       DeleteNodesNodeGroupRequest request =
           DeleteNodesNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupsDeleteNodesRequestResource(
                   NodeGroupsDeleteNodesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           nodeGroupsClient.deleteNodesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteNodesNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNodesNodeGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteNodeGroupRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified NodeGroup resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       DeleteNodeGroupRequest request =
           DeleteNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           nodeGroupsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteNodeGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetNodeGroupRequest request)
    
    
    public final NodeGroup get(GetNodeGroupRequest request)

Returns the specified NodeGroup. Get a list of available NodeGroups by making a list() request. Note: the "nodes" field should not be used. Use nodeGroups.listNodes instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       GetNodeGroupRequest request =
           GetNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       NodeGroup response = nodeGroupsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNodeGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NodeGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroup)` |   
  
### get(String project, String zone, String nodeGroup)
    
    
    public final NodeGroup get(String project, String zone, String nodeGroup)

Returns the specified NodeGroup. Get a list of available NodeGroups by making a list() request. Note: the "nodes" field should not be used. Use nodeGroups.listNodes instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String nodeGroup = "nodeGroup443599261";
       NodeGroup response = nodeGroupsClient.get(project, zone, nodeGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`nodeGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the node group to return.  
**Returns**  
---  
**Type** | **Description**  
`[NodeGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroup)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetNodeGroupRequest,NodeGroup> getCallable()

Returns the specified NodeGroup. Get a list of available NodeGroups by making a list() request. Note: the "nodes" field should not be used. Use nodeGroups.listNodes instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       GetNodeGroupRequest request =
           GetNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<NodeGroup> future = nodeGroupsClient.getCallable().futureCall(request);
       // Do something.
       NodeGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetNodeGroupRequest),[NodeGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroup)>` |   
  
### getIamPolicy(GetIamPolicyNodeGroupRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyNodeGroupRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       GetIamPolicyNodeGroupRequest request =
           GetIamPolicyNodeGroupRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       Policy response = nodeGroupsClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyNodeGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicy(String project, String zone, String resource)
    
    
    public final Policy getIamPolicy(String project, String zone, String resource)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       Policy response = nodeGroupsClient.getIamPolicy(project, zone, resource);
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
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyNodeGroupRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       GetIamPolicyNodeGroupRequest request =
           GetIamPolicyNodeGroupRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .build();
       ApiFuture<Policy> future = nodeGroupsClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyNodeGroupRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getSettings()
    
    
    public final @Nullable NodeGroupsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.NodeGroupsSettings` |   
  
### getStub()
    
    
    public NodeGroupsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[NodeGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.NodeGroupsStub)` |   
  
### insertAsync(InsertNodeGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertNodeGroupRequest request)

Creates a NodeGroup resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       InsertNodeGroupRequest request =
           InsertNodeGroupRequest.newBuilder()
               .setInitialNodeCount(1682564205)
               .setNodeGroupResource(NodeGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = nodeGroupsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertNodeGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String zone, int initialNodeCount, NodeGroup nodeGroupResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String zone, int initialNodeCount, NodeGroup nodeGroupResource)

Creates a NodeGroup resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       int initialNodeCount = 1682564205;
       NodeGroup nodeGroupResource = NodeGroup.newBuilder().build();
       Operation response =
           nodeGroupsClient.insertAsync(project, zone, initialNodeCount, nodeGroupResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`initialNodeCount` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Initial count of nodes in the node group.  
`nodeGroupResource` | `[NodeGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroup)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertNodeGroupRequest,Operation> insertCallable()

Creates a NodeGroup resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       InsertNodeGroupRequest request =
           InsertNodeGroupRequest.newBuilder()
               .setInitialNodeCount(1682564205)
               .setNodeGroupResource(NodeGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = nodeGroupsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertNodeGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertNodeGroupRequest,Operation,Operation> insertOperationCallable()

Creates a NodeGroup resource in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       InsertNodeGroupRequest request =
           InsertNodeGroupRequest.newBuilder()
               .setInitialNodeCount(1682564205)
               .setNodeGroupResource(NodeGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           nodeGroupsClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertNodeGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListNodeGroupsRequest request)
    
    
    public final NodeGroupsClient.ListPagedResponse list(ListNodeGroupsRequest request)

Retrieves a list of node groups available to the specified project. Note: use nodeGroups.listNodes for more details about each group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       ListNodeGroupsRequest request =
           ListNodeGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (NodeGroup element : nodeGroupsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNodeGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNodeGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NodeGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsClient.ListPagedResponse)` |   
  
### list(String project, String zone)
    
    
    public final NodeGroupsClient.ListPagedResponse list(String project, String zone)

Retrieves a list of node groups available to the specified project. Note: use nodeGroups.listNodes for more details about each group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       for (NodeGroup element : nodeGroupsClient.list(project, zone).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
**Returns**  
---  
**Type** | **Description**  
`[NodeGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListNodeGroupsRequest,NodeGroupList> listCallable()

Retrieves a list of node groups available to the specified project. Note: use nodeGroups.listNodes for more details about each group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       ListNodeGroupsRequest request =
           ListNodeGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         NodeGroupList response = nodeGroupsClient.listCallable().call(request);
         for (NodeGroup element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNodeGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNodeGroupsRequest),[NodeGroupList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupList)>` |   
  
### listNodes(ListNodesNodeGroupsRequest request)
    
    
    public final NodeGroupsClient.ListNodesPagedResponse listNodes(ListNodesNodeGroupsRequest request)

Lists nodes in the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       ListNodesNodeGroupsRequest request =
           ListNodesNodeGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNodeGroup("nodeGroup443599261")
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (NodeGroupNode element : nodeGroupsClient.listNodes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNodesNodeGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNodesNodeGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[NodeGroupsClient.ListNodesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsClient.ListNodesPagedResponse)` |   
  
### listNodes(String project, String zone, String nodeGroup)
    
    
    public final NodeGroupsClient.ListNodesPagedResponse listNodes(String project, String zone, String nodeGroup)

Lists nodes in the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String nodeGroup = "nodeGroup443599261";
       for (NodeGroupNode element :
           nodeGroupsClient.listNodes(project, zone, nodeGroup).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`nodeGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the NodeGroup resource whose nodes you want to list.  
**Returns**  
---  
**Type** | **Description**  
`[NodeGroupsClient.ListNodesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsClient.ListNodesPagedResponse)` |   
  
### listNodesCallable()
    
    
    public final UnaryCallable<ListNodesNodeGroupsRequest,NodeGroupsListNodes> listNodesCallable()

Lists nodes in the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       ListNodesNodeGroupsRequest request =
           ListNodesNodeGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNodeGroup("nodeGroup443599261")
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         NodeGroupsListNodes response = nodeGroupsClient.listNodesCallable().call(request);
         for (NodeGroupNode element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNodesNodeGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNodesNodeGroupsRequest),[NodeGroupsListNodes](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsListNodes)>` |   
  
### listNodesPagedCallable()
    
    
    public final UnaryCallable<ListNodesNodeGroupsRequest,NodeGroupsClient.ListNodesPagedResponse> listNodesPagedCallable()

Lists nodes in the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       ListNodesNodeGroupsRequest request =
           ListNodesNodeGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setNodeGroup("nodeGroup443599261")
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<NodeGroupNode> future =
           nodeGroupsClient.listNodesPagedCallable().futureCall(request);
       // Do something.
       for (NodeGroupNode element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNodesNodeGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNodesNodeGroupsRequest),[ListNodesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsClient.ListNodesPagedResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListNodeGroupsRequest,NodeGroupsClient.ListPagedResponse> listPagedCallable()

Retrieves a list of node groups available to the specified project. Note: use nodeGroups.listNodes for more details about each group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       ListNodeGroupsRequest request =
           ListNodeGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<NodeGroup> future = nodeGroupsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (NodeGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListNodeGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListNodeGroupsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsClient.ListPagedResponse)>` |   
  
### patchAsync(PatchNodeGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(PatchNodeGroupRequest request)

Updates the specified node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       PatchNodeGroupRequest request =
           PatchNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupResource(NodeGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = nodeGroupsClient.patchAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchNodeGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchAsync(String project, String zone, String nodeGroup, NodeGroup nodeGroupResource)
    
    
    public final OperationFuture<Operation,Operation> patchAsync(String project, String zone, String nodeGroup, NodeGroup nodeGroupResource)

Updates the specified node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String nodeGroup = "nodeGroup443599261";
       NodeGroup nodeGroupResource = NodeGroup.newBuilder().build();
       Operation response =
           nodeGroupsClient.patchAsync(project, zone, nodeGroup, nodeGroupResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`nodeGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the NodeGroup resource to update.  
`nodeGroupResource` | `[NodeGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroup)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchCallable()
    
    
    public final UnaryCallable<PatchNodeGroupRequest,Operation> patchCallable()

Updates the specified node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       PatchNodeGroupRequest request =
           PatchNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupResource(NodeGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = nodeGroupsClient.patchCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PatchNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchNodeGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationCallable()
    
    
    public final OperationCallable<PatchNodeGroupRequest,Operation,Operation> patchOperationCallable()

Updates the specified node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       PatchNodeGroupRequest request =
           PatchNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupResource(NodeGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           nodeGroupsClient.patchOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PatchNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchNodeGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceAsync(PerformMaintenanceNodeGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> performMaintenanceAsync(PerformMaintenanceNodeGroupRequest request)

Perform maintenance on a subset of nodes in the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       PerformMaintenanceNodeGroupRequest request =
           PerformMaintenanceNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupsPerformMaintenanceRequestResource(
                   NodeGroupsPerformMaintenanceRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = nodeGroupsClient.performMaintenanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PerformMaintenanceNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceNodeGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceAsync(String project, String zone, String nodeGroup, NodeGroupsPerformMaintenanceRequest nodeGroupsPerformMaintenanceRequestResource)
    
    
    public final OperationFuture<Operation,Operation> performMaintenanceAsync(String project, String zone, String nodeGroup, NodeGroupsPerformMaintenanceRequest nodeGroupsPerformMaintenanceRequestResource)

Perform maintenance on a subset of nodes in the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String nodeGroup = "nodeGroup443599261";
       NodeGroupsPerformMaintenanceRequest nodeGroupsPerformMaintenanceRequestResource =
           NodeGroupsPerformMaintenanceRequest.newBuilder().build();
       Operation response =
           nodeGroupsClient
               .performMaintenanceAsync(
                   project, zone, nodeGroup, nodeGroupsPerformMaintenanceRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`nodeGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the node group scoping this request.  
`nodeGroupsPerformMaintenanceRequestResource` | `[NodeGroupsPerformMaintenanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsPerformMaintenanceRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceCallable()
    
    
    public final UnaryCallable<PerformMaintenanceNodeGroupRequest,Operation> performMaintenanceCallable()

Perform maintenance on a subset of nodes in the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       PerformMaintenanceNodeGroupRequest request =
           PerformMaintenanceNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupsPerformMaintenanceRequestResource(
                   NodeGroupsPerformMaintenanceRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           nodeGroupsClient.performMaintenanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PerformMaintenanceNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceNodeGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### performMaintenanceOperationCallable()
    
    
    public final OperationCallable<PerformMaintenanceNodeGroupRequest,Operation,Operation> performMaintenanceOperationCallable()

Perform maintenance on a subset of nodes in the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       PerformMaintenanceNodeGroupRequest request =
           PerformMaintenanceNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupsPerformMaintenanceRequestResource(
                   NodeGroupsPerformMaintenanceRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           nodeGroupsClient.performMaintenanceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PerformMaintenanceNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PerformMaintenanceNodeGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setIamPolicy(SetIamPolicyNodeGroupRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyNodeGroupRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       SetIamPolicyNodeGroupRequest request =
           SetIamPolicyNodeGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetPolicyRequestResource(ZoneSetPolicyRequest.newBuilder().build())
               .build();
       Policy response = nodeGroupsClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyNodeGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicy(String project, String zone, String resource, ZoneSetPolicyRequest zoneSetPolicyRequestResource)
    
    
    public final Policy setIamPolicy(String project, String zone, String resource, ZoneSetPolicyRequest zoneSetPolicyRequestResource)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       ZoneSetPolicyRequest zoneSetPolicyRequestResource = ZoneSetPolicyRequest.newBuilder().build();
       Policy response =
           nodeGroupsClient.setIamPolicy(project, zone, resource, zoneSetPolicyRequestResource);
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
`zoneSetPolicyRequestResource` | `[ZoneSetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneSetPolicyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyNodeGroupRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       SetIamPolicyNodeGroupRequest request =
           SetIamPolicyNodeGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setZone("zone3744684")
               .setZoneSetPolicyRequestResource(ZoneSetPolicyRequest.newBuilder().build())
               .build();
       ApiFuture<Policy> future = nodeGroupsClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyNodeGroupRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### setNodeTemplateAsync(SetNodeTemplateNodeGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> setNodeTemplateAsync(SetNodeTemplateNodeGroupRequest request)

Updates the node template of the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       SetNodeTemplateNodeGroupRequest request =
           SetNodeTemplateNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupsSetNodeTemplateRequestResource(
                   NodeGroupsSetNodeTemplateRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = nodeGroupsClient.setNodeTemplateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetNodeTemplateNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetNodeTemplateNodeGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setNodeTemplateAsync(String project, String zone, String nodeGroup, NodeGroupsSetNodeTemplateRequest nodeGroupsSetNodeTemplateRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setNodeTemplateAsync(String project, String zone, String nodeGroup, NodeGroupsSetNodeTemplateRequest nodeGroupsSetNodeTemplateRequestResource)

Updates the node template of the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String nodeGroup = "nodeGroup443599261";
       NodeGroupsSetNodeTemplateRequest nodeGroupsSetNodeTemplateRequestResource =
           NodeGroupsSetNodeTemplateRequest.newBuilder().build();
       Operation response =
           nodeGroupsClient
               .setNodeTemplateAsync(
                   project, zone, nodeGroup, nodeGroupsSetNodeTemplateRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`nodeGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the NodeGroup resource to update.  
`nodeGroupsSetNodeTemplateRequestResource` | `[NodeGroupsSetNodeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsSetNodeTemplateRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setNodeTemplateCallable()
    
    
    public final UnaryCallable<SetNodeTemplateNodeGroupRequest,Operation> setNodeTemplateCallable()

Updates the node template of the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       SetNodeTemplateNodeGroupRequest request =
           SetNodeTemplateNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupsSetNodeTemplateRequestResource(
                   NodeGroupsSetNodeTemplateRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = nodeGroupsClient.setNodeTemplateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetNodeTemplateNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetNodeTemplateNodeGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setNodeTemplateOperationCallable()
    
    
    public final OperationCallable<SetNodeTemplateNodeGroupRequest,Operation,Operation> setNodeTemplateOperationCallable()

Updates the node template of the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       SetNodeTemplateNodeGroupRequest request =
           SetNodeTemplateNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupsSetNodeTemplateRequestResource(
                   NodeGroupsSetNodeTemplateRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           nodeGroupsClient.setNodeTemplateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetNodeTemplateNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetNodeTemplateNodeGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### simulateMaintenanceEventAsync(SimulateMaintenanceEventNodeGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> simulateMaintenanceEventAsync(SimulateMaintenanceEventNodeGroupRequest request)

Simulates maintenance event on specified nodes from the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       SimulateMaintenanceEventNodeGroupRequest request =
           SimulateMaintenanceEventNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupsSimulateMaintenanceEventRequestResource(
                   NodeGroupsSimulateMaintenanceEventRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = nodeGroupsClient.simulateMaintenanceEventAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SimulateMaintenanceEventNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SimulateMaintenanceEventNodeGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### simulateMaintenanceEventAsync(String project, String zone, String nodeGroup, NodeGroupsSimulateMaintenanceEventRequest nodeGroupsSimulateMaintenanceEventRequestResource)
    
    
    public final OperationFuture<Operation,Operation> simulateMaintenanceEventAsync(String project, String zone, String nodeGroup, NodeGroupsSimulateMaintenanceEventRequest nodeGroupsSimulateMaintenanceEventRequestResource)

Simulates maintenance event on specified nodes from the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String nodeGroup = "nodeGroup443599261";
       NodeGroupsSimulateMaintenanceEventRequest nodeGroupsSimulateMaintenanceEventRequestResource =
           NodeGroupsSimulateMaintenanceEventRequest.newBuilder().build();
       Operation response =
           nodeGroupsClient
               .simulateMaintenanceEventAsync(
                   project, zone, nodeGroup, nodeGroupsSimulateMaintenanceEventRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone for this request.  
`nodeGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the NodeGroup resource whose nodes will go under maintenance simulation.  
`nodeGroupsSimulateMaintenanceEventRequestResource` | `[NodeGroupsSimulateMaintenanceEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NodeGroupsSimulateMaintenanceEventRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### simulateMaintenanceEventCallable()
    
    
    public final UnaryCallable<SimulateMaintenanceEventNodeGroupRequest,Operation> simulateMaintenanceEventCallable()

Simulates maintenance event on specified nodes from the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       SimulateMaintenanceEventNodeGroupRequest request =
           SimulateMaintenanceEventNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupsSimulateMaintenanceEventRequestResource(
                   NodeGroupsSimulateMaintenanceEventRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           nodeGroupsClient.simulateMaintenanceEventCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SimulateMaintenanceEventNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SimulateMaintenanceEventNodeGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### simulateMaintenanceEventOperationCallable()
    
    
    public final OperationCallable<SimulateMaintenanceEventNodeGroupRequest,Operation,Operation> simulateMaintenanceEventOperationCallable()

Simulates maintenance event on specified nodes from the node group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       SimulateMaintenanceEventNodeGroupRequest request =
           SimulateMaintenanceEventNodeGroupRequest.newBuilder()
               .setNodeGroup("nodeGroup443599261")
               .setNodeGroupsSimulateMaintenanceEventRequestResource(
                   NodeGroupsSimulateMaintenanceEventRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           nodeGroupsClient.simulateMaintenanceEventOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SimulateMaintenanceEventNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SimulateMaintenanceEventNodeGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### testIamPermissions(TestIamPermissionsNodeGroupRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsNodeGroupRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       TestIamPermissionsNodeGroupRequest request =
           TestIamPermissionsNodeGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       TestPermissionsResponse response = nodeGroupsClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsNodeGroupRequest)`  
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
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           nodeGroupsClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsNodeGroupRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (NodeGroupsClient nodeGroupsClient = NodeGroupsClient.create()) {
       TestIamPermissionsNodeGroupRequest request =
           TestIamPermissionsNodeGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<TestPermissionsResponse> future =
           nodeGroupsClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsNodeGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsNodeGroupRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
