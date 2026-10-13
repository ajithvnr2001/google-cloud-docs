---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsClient
title: Class InstanceGroupsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:02:33.139822+00:00
---

# Class InstanceGroupsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InstanceGroupsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/InstanceGroupsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The InstanceGroups API.

This client uses InstanceGroups version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroup = "instanceGroup-1404696854";
       InstanceGroup response = instanceGroupsClient.get(project, zone, instanceGroup);
     }
     

Note: close() needs to be called on the InstanceGroupsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AddInstances |  Adds a list of instances to the specified instance group. All of the instances in the instance group must be in the same network/subnetwork. Read Adding instances for more information. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addInstancesAsync(AddInstancesInstanceGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addInstancesAsync(String project, String zone, String instanceGroup, InstanceGroupsAddInstancesRequest instanceGroupsAddInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addInstancesOperationCallable() 
  * addInstancesCallable() 

  
AggregatedList |  Retrieves the list of instance groups and sorts them by zone.  To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * aggregatedList(AggregatedListInstanceGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * aggregatedList(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * aggregatedListPagedCallable() 
  * aggregatedListCallable() 

  
Delete |  Deletes the specified instance group. The instances in the group are not deleted. Note that instance group must not belong to a backend service. Read Deleting an instance group for more information. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteInstanceGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String zone, String instanceGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified zonal instance group. Get a list of available zonal instance groups by making a list() request.  For managed instance groups, use theinstanceGroupManagers or regionInstanceGroupManagers methods instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetInstanceGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String zone, String instanceGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates an instance group in the specified project using the parameters that are included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertInstanceGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String zone, InstanceGroup instanceGroupResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of zonal instance group resources contained within the specified zone.  For managed instance groups, use theinstanceGroupManagers or regionInstanceGroupManagers methods instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListInstanceGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String zone) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListInstances |  Lists the instances in the specified instance group. The orderBy query parameter is not supported. The filter query parameter is supported, but only for expressions that use `eq` (equal) or `ne` (not equal) operators. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listInstances(ListInstancesInstanceGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listInstances(String project, String zone, String instanceGroup, InstanceGroupsListInstancesRequest instanceGroupsListInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listInstancesPagedCallable() 
  * listInstancesCallable() 

  
RemoveInstances |  Removes one or more instances from the specified instance group, but does not delete those instances.  If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration before the VM instance is removed or deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeInstancesAsync(RemoveInstancesInstanceGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removeInstancesAsync(String project, String zone, String instanceGroup, InstanceGroupsRemoveInstancesRequest instanceGroupsRemoveInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeInstancesOperationCallable() 
  * removeInstancesCallable() 

  
SetNamedPorts |  Sets the named ports for the specified instance group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setNamedPortsAsync(SetNamedPortsInstanceGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setNamedPortsAsync(String project, String zone, String instanceGroup, InstanceGroupsSetNamedPortsRequest instanceGroupsSetNamedPortsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setNamedPortsOperationCallable() 
  * setNamedPortsCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsInstanceGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String zone, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of InstanceGroupsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InstanceGroupsSettings instanceGroupsSettings =
         InstanceGroupsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create(instanceGroupsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     InstanceGroupsSettings instanceGroupsSettings =
         InstanceGroupsSettings.newBuilder().setEndpoint(myEndpoint).build();
     InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create(instanceGroupsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > InstanceGroupsClient

## Static Methods 

### create()
    
    
    public static final InstanceGroupsClient create()

Constructs an instance of InstanceGroupsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InstanceGroupsSettings settings)
    
    
    public static final InstanceGroupsClient create(InstanceGroupsSettings settings)

Constructs an instance of InstanceGroupsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InstanceGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(InstanceGroupsStub stub)
    
    
    public static final InstanceGroupsClient create(InstanceGroupsStub stub)

Constructs an instance of InstanceGroupsClient, using the given stub for making calls. This is for advanced usage - prefer using create(InstanceGroupsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InstanceGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InstanceGroupsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsClient)` |   
  
## Constructors 

### InstanceGroupsClient(InstanceGroupsSettings settings)
    
    
    protected InstanceGroupsClient(InstanceGroupsSettings settings)

Constructs an instance of InstanceGroupsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[InstanceGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsSettings)`  
  
  
### InstanceGroupsClient(InstanceGroupsStub stub)
    
    
    protected InstanceGroupsClient(InstanceGroupsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[InstanceGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InstanceGroupsStub)`  
  
  
## Methods 

### addInstancesAsync(AddInstancesInstanceGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> addInstancesAsync(AddInstancesInstanceGroupRequest request)

Adds a list of instances to the specified instance group. All of the instances in the instance group must be in the same network/subnetwork. Read Adding instances for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       AddInstancesInstanceGroupRequest request =
           AddInstancesInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setInstanceGroupsAddInstancesRequestResource(
                   InstanceGroupsAddInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupsClient.addInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddInstancesInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddInstancesInstanceGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addInstancesAsync(String project, String zone, String instanceGroup, InstanceGroupsAddInstancesRequest instanceGroupsAddInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> addInstancesAsync(String project, String zone, String instanceGroup, InstanceGroupsAddInstancesRequest instanceGroupsAddInstancesRequestResource)

Adds a list of instances to the specified instance group. All of the instances in the instance group must be in the same network/subnetwork. Read Adding instances for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroup = "instanceGroup-1404696854";
       InstanceGroupsAddInstancesRequest instanceGroupsAddInstancesRequestResource =
           InstanceGroupsAddInstancesRequest.newBuilder().build();
       Operation response =
           instanceGroupsClient
               .addInstancesAsync(
                   project, zone, instanceGroup, instanceGroupsAddInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone where the instance group is located.  
`instanceGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the instance group where you are adding instances.  
`instanceGroupsAddInstancesRequestResource` | `[InstanceGroupsAddInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsAddInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addInstancesCallable()
    
    
    public final UnaryCallable<AddInstancesInstanceGroupRequest,Operation> addInstancesCallable()

Adds a list of instances to the specified instance group. All of the instances in the instance group must be in the same network/subnetwork. Read Adding instances for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       AddInstancesInstanceGroupRequest request =
           AddInstancesInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setInstanceGroupsAddInstancesRequestResource(
                   InstanceGroupsAddInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instanceGroupsClient.addInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddInstancesInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddInstancesInstanceGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addInstancesOperationCallable()
    
    
    public final OperationCallable<AddInstancesInstanceGroupRequest,Operation,Operation> addInstancesOperationCallable()

Adds a list of instances to the specified instance group. All of the instances in the instance group must be in the same network/subnetwork. Read Adding instances for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       AddInstancesInstanceGroupRequest request =
           AddInstancesInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setInstanceGroupsAddInstancesRequestResource(
                   InstanceGroupsAddInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupsClient.addInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddInstancesInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddInstancesInstanceGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### aggregatedList(AggregatedListInstanceGroupsRequest request)
    
    
    public final InstanceGroupsClient.AggregatedListPagedResponse aggregatedList(AggregatedListInstanceGroupsRequest request)

Retrieves the list of instance groups and sorts them by zone.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       AggregatedListInstanceGroupsRequest request =
           AggregatedListInstanceGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       for (Map.Entry<String, InstanceGroupsScopedList> element :
           instanceGroupsClient.aggregatedList(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AggregatedListInstanceGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstanceGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsClient.AggregatedListPagedResponse)` |   
  
### aggregatedList(String project)
    
    
    public final InstanceGroupsClient.AggregatedListPagedResponse aggregatedList(String project)

Retrieves the list of instance groups and sorts them by zone.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       String project = "project-309310695";
       for (Map.Entry<String, InstanceGroupsScopedList> element :
           instanceGroupsClient.aggregatedList(project).iterateAll()) {
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
`[InstanceGroupsClient.AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsClient.AggregatedListPagedResponse)` |   
  
### aggregatedListCallable()
    
    
    public final UnaryCallable<AggregatedListInstanceGroupsRequest,InstanceGroupAggregatedList> aggregatedListCallable()

Retrieves the list of instance groups and sorts them by zone.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       AggregatedListInstanceGroupsRequest request =
           AggregatedListInstanceGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       while (true) {
         InstanceGroupAggregatedList response =
             instanceGroupsClient.aggregatedListCallable().call(request);
         for (Map.Entry<String, InstanceGroupsScopedList> element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListInstanceGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstanceGroupsRequest),[InstanceGroupAggregatedList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupAggregatedList)>` |   
  
### aggregatedListPagedCallable()
    
    
    public final UnaryCallable<AggregatedListInstanceGroupsRequest,InstanceGroupsClient.AggregatedListPagedResponse> aggregatedListPagedCallable()

Retrieves the list of instance groups and sorts them by zone.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       AggregatedListInstanceGroupsRequest request =
           AggregatedListInstanceGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setIncludeAllScopes(true)
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setServiceProjectNumber(-1293855239)
               .build();
       ApiFuture<Map.Entry<String, InstanceGroupsScopedList>> future =
           instanceGroupsClient.aggregatedListPagedCallable().futureCall(request);
       // Do something.
       for (Map.Entry<String, InstanceGroupsScopedList> element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AggregatedListInstanceGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AggregatedListInstanceGroupsRequest),[AggregatedListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsClient.AggregatedListPagedResponse)>` |   
  
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

### deleteAsync(DeleteInstanceGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteInstanceGroupRequest request)

Deletes the specified instance group. The instances in the group are not deleted. Note that instance group must not belong to a backend service. Read Deleting an instance group for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       DeleteInstanceGroupRequest request =
           DeleteInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String zone, String instanceGroup)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String zone, String instanceGroup)

Deletes the specified instance group. The instances in the group are not deleted. Note that instance group must not belong to a backend service. Read Deleting an instance group for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroup = "instanceGroup-1404696854";
       Operation response = instanceGroupsClient.deleteAsync(project, zone, instanceGroup).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone where the instance group is located.  
`instanceGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the instance group to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteInstanceGroupRequest,Operation> deleteCallable()

Deletes the specified instance group. The instances in the group are not deleted. Note that instance group must not belong to a backend service. Read Deleting an instance group for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       DeleteInstanceGroupRequest request =
           DeleteInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instanceGroupsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteInstanceGroupRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified instance group. The instances in the group are not deleted. Note that instance group must not belong to a backend service. Read Deleting an instance group for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       DeleteInstanceGroupRequest request =
           DeleteInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetInstanceGroupRequest request)
    
    
    public final InstanceGroup get(GetInstanceGroupRequest request)

Returns the specified zonal instance group. Get a list of available zonal instance groups by making a list() request.

For managed instance groups, use theinstanceGroupManagers or regionInstanceGroupManagers methods instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       GetInstanceGroupRequest request =
           GetInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       InstanceGroup response = instanceGroupsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup)` |   
  
### get(String project, String zone, String instanceGroup)
    
    
    public final InstanceGroup get(String project, String zone, String instanceGroup)

Returns the specified zonal instance group. Get a list of available zonal instance groups by making a list() request.

For managed instance groups, use theinstanceGroupManagers or regionInstanceGroupManagers methods instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroup = "instanceGroup-1404696854";
       InstanceGroup response = instanceGroupsClient.get(project, zone, instanceGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone where the instance group is located.  
`instanceGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the instance group.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetInstanceGroupRequest,InstanceGroup> getCallable()

Returns the specified zonal instance group. Get a list of available zonal instance groups by making a list() request.

For managed instance groups, use theinstanceGroupManagers or regionInstanceGroupManagers methods instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       GetInstanceGroupRequest request =
           GetInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<InstanceGroup> future = instanceGroupsClient.getCallable().futureCall(request);
       // Do something.
       InstanceGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceGroupRequest),[InstanceGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup)>` |   
  
### getSettings()
    
    
    public final @Nullable InstanceGroupsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.InstanceGroupsSettings` |   
  
### getStub()
    
    
    public InstanceGroupsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.InstanceGroupsStub)` |   
  
### insertAsync(InsertInstanceGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertInstanceGroupRequest request)

Creates an instance group in the specified project using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       InsertInstanceGroupRequest request =
           InsertInstanceGroupRequest.newBuilder()
               .setInstanceGroupResource(InstanceGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String zone, InstanceGroup instanceGroupResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String zone, InstanceGroup instanceGroupResource)

Creates an instance group in the specified project using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       InstanceGroup instanceGroupResource = InstanceGroup.newBuilder().build();
       Operation response =
           instanceGroupsClient.insertAsync(project, zone, instanceGroupResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone where you want to create the instance group.  
`instanceGroupResource` | `[InstanceGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertInstanceGroupRequest,Operation> insertCallable()

Creates an instance group in the specified project using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       InsertInstanceGroupRequest request =
           InsertInstanceGroupRequest.newBuilder()
               .setInstanceGroupResource(InstanceGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future = instanceGroupsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertInstanceGroupRequest,Operation,Operation> insertOperationCallable()

Creates an instance group in the specified project using the parameters that are included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       InsertInstanceGroupRequest request =
           InsertInstanceGroupRequest.newBuilder()
               .setInstanceGroupResource(InstanceGroup.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupsClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListInstanceGroupsRequest request)
    
    
    public final InstanceGroupsClient.ListPagedResponse list(ListInstanceGroupsRequest request)

Retrieves the list of zonal instance group resources contained within the specified zone.

For managed instance groups, use theinstanceGroupManagers or regionInstanceGroupManagers methods instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       ListInstanceGroupsRequest request =
           ListInstanceGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (InstanceGroup element : instanceGroupsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInstanceGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstanceGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsClient.ListPagedResponse)` |   
  
### list(String project, String zone)
    
    
    public final InstanceGroupsClient.ListPagedResponse list(String project, String zone)

Retrieves the list of zonal instance group resources contained within the specified zone.

For managed instance groups, use theinstanceGroupManagers or regionInstanceGroupManagers methods instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       for (InstanceGroup element : instanceGroupsClient.list(project, zone).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of thezone where the instance group is located.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListInstanceGroupsRequest,InstanceGroupList> listCallable()

Retrieves the list of zonal instance group resources contained within the specified zone.

For managed instance groups, use theinstanceGroupManagers or regionInstanceGroupManagers methods instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       ListInstanceGroupsRequest request =
           ListInstanceGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         InstanceGroupList response = instanceGroupsClient.listCallable().call(request);
         for (InstanceGroup element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstanceGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstanceGroupsRequest),[InstanceGroupList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupList)>` |   
  
### listInstances(ListInstancesInstanceGroupsRequest request)
    
    
    public final InstanceGroupsClient.ListInstancesPagedResponse listInstances(ListInstancesInstanceGroupsRequest request)

Lists the instances in the specified instance group. The orderBy query parameter is not supported. The filter query parameter is supported, but only for expressions that use `eq` (equal) or `ne` (not equal) operators.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       ListInstancesInstanceGroupsRequest request =
           ListInstancesInstanceGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroup("instanceGroup-1404696854")
               .setInstanceGroupsListInstancesRequestResource(
                   InstanceGroupsListInstancesRequest.newBuilder().build())
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       for (InstanceWithNamedPorts element :
           instanceGroupsClient.listInstances(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInstancesInstanceGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstancesInstanceGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupsClient.ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsClient.ListInstancesPagedResponse)` |   
  
### listInstances(String project, String zone, String instanceGroup, InstanceGroupsListInstancesRequest instanceGroupsListInstancesRequestResource)
    
    
    public final InstanceGroupsClient.ListInstancesPagedResponse listInstances(String project, String zone, String instanceGroup, InstanceGroupsListInstancesRequest instanceGroupsListInstancesRequestResource)

Lists the instances in the specified instance group. The orderBy query parameter is not supported. The filter query parameter is supported, but only for expressions that use `eq` (equal) or `ne` (not equal) operators.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroup = "instanceGroup-1404696854";
       InstanceGroupsListInstancesRequest instanceGroupsListInstancesRequestResource =
           InstanceGroupsListInstancesRequest.newBuilder().build();
       for (InstanceWithNamedPorts element :
           instanceGroupsClient
               .listInstances(
                   project, zone, instanceGroup, instanceGroupsListInstancesRequestResource)
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
The name of the zone where the instance group is located.  
`instanceGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the instance group from which you want to generate a list of included instances.  
`instanceGroupsListInstancesRequestResource` | `[InstanceGroupsListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsListInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroupsClient.ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsClient.ListInstancesPagedResponse)` |   
  
### listInstancesCallable()
    
    
    public final UnaryCallable<ListInstancesInstanceGroupsRequest,InstanceGroupsListInstances> listInstancesCallable()

Lists the instances in the specified instance group. The orderBy query parameter is not supported. The filter query parameter is supported, but only for expressions that use `eq` (equal) or `ne` (not equal) operators.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       ListInstancesInstanceGroupsRequest request =
           ListInstancesInstanceGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroup("instanceGroup-1404696854")
               .setInstanceGroupsListInstancesRequestResource(
                   InstanceGroupsListInstancesRequest.newBuilder().build())
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       while (true) {
         InstanceGroupsListInstances response =
             instanceGroupsClient.listInstancesCallable().call(request);
         for (InstanceWithNamedPorts element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesInstanceGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstancesInstanceGroupsRequest),[InstanceGroupsListInstances](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsListInstances)>` |   
  
### listInstancesPagedCallable()
    
    
    public final UnaryCallable<ListInstancesInstanceGroupsRequest,InstanceGroupsClient.ListInstancesPagedResponse> listInstancesPagedCallable()

Lists the instances in the specified instance group. The orderBy query parameter is not supported. The filter query parameter is supported, but only for expressions that use `eq` (equal) or `ne` (not equal) operators.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       ListInstancesInstanceGroupsRequest request =
           ListInstancesInstanceGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroup("instanceGroup-1404696854")
               .setInstanceGroupsListInstancesRequestResource(
                   InstanceGroupsListInstancesRequest.newBuilder().build())
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<InstanceWithNamedPorts> future =
           instanceGroupsClient.listInstancesPagedCallable().futureCall(request);
       // Do something.
       for (InstanceWithNamedPorts element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesInstanceGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstancesInstanceGroupsRequest),[ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsClient.ListInstancesPagedResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListInstanceGroupsRequest,InstanceGroupsClient.ListPagedResponse> listPagedCallable()

Retrieves the list of zonal instance group resources contained within the specified zone.

For managed instance groups, use theinstanceGroupManagers or regionInstanceGroupManagers methods instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       ListInstanceGroupsRequest request =
           ListInstanceGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setZone("zone3744684")
               .build();
       ApiFuture<InstanceGroup> future =
           instanceGroupsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (InstanceGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstanceGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstanceGroupsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsClient.ListPagedResponse)>` |   
  
### removeInstancesAsync(RemoveInstancesInstanceGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> removeInstancesAsync(RemoveInstancesInstanceGroupRequest request)

Removes one or more instances from the specified instance group, but does not delete those instances.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration before the VM instance is removed or deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       RemoveInstancesInstanceGroupRequest request =
           RemoveInstancesInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setInstanceGroupsRemoveInstancesRequestResource(
                   InstanceGroupsRemoveInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupsClient.removeInstancesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveInstancesInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveInstancesInstanceGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeInstancesAsync(String project, String zone, String instanceGroup, InstanceGroupsRemoveInstancesRequest instanceGroupsRemoveInstancesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> removeInstancesAsync(String project, String zone, String instanceGroup, InstanceGroupsRemoveInstancesRequest instanceGroupsRemoveInstancesRequestResource)

Removes one or more instances from the specified instance group, but does not delete those instances.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration before the VM instance is removed or deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroup = "instanceGroup-1404696854";
       InstanceGroupsRemoveInstancesRequest instanceGroupsRemoveInstancesRequestResource =
           InstanceGroupsRemoveInstancesRequest.newBuilder().build();
       Operation response =
           instanceGroupsClient
               .removeInstancesAsync(
                   project, zone, instanceGroup, instanceGroupsRemoveInstancesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone where the instance group is located.  
`instanceGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the instance group where the specified instances will be removed.  
`instanceGroupsRemoveInstancesRequestResource` | `[InstanceGroupsRemoveInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsRemoveInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeInstancesCallable()
    
    
    public final UnaryCallable<RemoveInstancesInstanceGroupRequest,Operation> removeInstancesCallable()

Removes one or more instances from the specified instance group, but does not delete those instances.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration before the VM instance is removed or deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       RemoveInstancesInstanceGroupRequest request =
           RemoveInstancesInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setInstanceGroupsRemoveInstancesRequestResource(
                   InstanceGroupsRemoveInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupsClient.removeInstancesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveInstancesInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveInstancesInstanceGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeInstancesOperationCallable()
    
    
    public final OperationCallable<RemoveInstancesInstanceGroupRequest,Operation,Operation> removeInstancesOperationCallable()

Removes one or more instances from the specified instance group, but does not delete those instances.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration before the VM instance is removed or deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       RemoveInstancesInstanceGroupRequest request =
           RemoveInstancesInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setInstanceGroupsRemoveInstancesRequestResource(
                   InstanceGroupsRemoveInstancesRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupsClient.removeInstancesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveInstancesInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveInstancesInstanceGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setNamedPortsAsync(SetNamedPortsInstanceGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> setNamedPortsAsync(SetNamedPortsInstanceGroupRequest request)

Sets the named ports for the specified instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       SetNamedPortsInstanceGroupRequest request =
           SetNamedPortsInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setInstanceGroupsSetNamedPortsRequestResource(
                   InstanceGroupsSetNamedPortsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       Operation response = instanceGroupsClient.setNamedPortsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetNamedPortsInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetNamedPortsInstanceGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setNamedPortsAsync(String project, String zone, String instanceGroup, InstanceGroupsSetNamedPortsRequest instanceGroupsSetNamedPortsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setNamedPortsAsync(String project, String zone, String instanceGroup, InstanceGroupsSetNamedPortsRequest instanceGroupsSetNamedPortsRequestResource)

Sets the named ports for the specified instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String instanceGroup = "instanceGroup-1404696854";
       InstanceGroupsSetNamedPortsRequest instanceGroupsSetNamedPortsRequestResource =
           InstanceGroupsSetNamedPortsRequest.newBuilder().build();
       Operation response =
           instanceGroupsClient
               .setNamedPortsAsync(
                   project, zone, instanceGroup, instanceGroupsSetNamedPortsRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`zone` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the zone where the instance group is located.  
`instanceGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the instance group where the named ports are updated.  
`instanceGroupsSetNamedPortsRequestResource` | `[InstanceGroupsSetNamedPortsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupsSetNamedPortsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setNamedPortsCallable()
    
    
    public final UnaryCallable<SetNamedPortsInstanceGroupRequest,Operation> setNamedPortsCallable()

Sets the named ports for the specified instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       SetNamedPortsInstanceGroupRequest request =
           SetNamedPortsInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setInstanceGroupsSetNamedPortsRequestResource(
                   InstanceGroupsSetNamedPortsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       ApiFuture<Operation> future =
           instanceGroupsClient.setNamedPortsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetNamedPortsInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetNamedPortsInstanceGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setNamedPortsOperationCallable()
    
    
    public final OperationCallable<SetNamedPortsInstanceGroupRequest,Operation,Operation> setNamedPortsOperationCallable()

Sets the named ports for the specified instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       SetNamedPortsInstanceGroupRequest request =
           SetNamedPortsInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setInstanceGroupsSetNamedPortsRequestResource(
                   InstanceGroupsSetNamedPortsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setZone("zone3744684")
               .build();
       OperationFuture<Operation, Operation> future =
           instanceGroupsClient.setNamedPortsOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetNamedPortsInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetNamedPortsInstanceGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsInstanceGroupRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsInstanceGroupRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       TestIamPermissionsInstanceGroupRequest request =
           TestIamPermissionsInstanceGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       TestPermissionsResponse response = instanceGroupsClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsInstanceGroupRequest)`  
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
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       String project = "project-309310695";
       String zone = "zone3744684";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           instanceGroupsClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsInstanceGroupRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (InstanceGroupsClient instanceGroupsClient = InstanceGroupsClient.create()) {
       TestIamPermissionsInstanceGroupRequest request =
           TestIamPermissionsInstanceGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .setZone("zone3744684")
               .build();
       ApiFuture<TestPermissionsResponse> future =
           instanceGroupsClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsInstanceGroupRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
