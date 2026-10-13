---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupsClient
title: Class RegionInstanceGroupsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:42.790863+00:00
---

# Class RegionInstanceGroupsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionInstanceGroupsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RegionInstanceGroupsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RegionInstanceGroups API.

This client uses RegionInstanceGroups version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroup = "instanceGroup-1404696854";
       InstanceGroup response = regionInstanceGroupsClient.get(project, region, instanceGroup);
     }
     

Note: close() needs to be called on the RegionInstanceGroupsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Get |  Returns the specified instance group resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRegionInstanceGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String instanceGroup) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
List |  Retrieves the list of instance group resources contained within the specified region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRegionInstanceGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
ListInstances |  Lists the instances in the specified instance group and displays information about the named ports. Depending on the specified options, this method can list all instances or only the instances that are running. The orderBy query parameter is not supported. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listInstances(ListInstancesRegionInstanceGroupsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listInstances(String project, String region, String instanceGroup, RegionInstanceGroupsListInstancesRequest regionInstanceGroupsListInstancesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listInstancesPagedCallable() 
  * listInstancesCallable() 

  
SetNamedPorts |  Sets the named ports for the specified regional instance group. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setNamedPortsAsync(SetNamedPortsRegionInstanceGroupRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setNamedPortsAsync(String project, String region, String instanceGroup, RegionInstanceGroupsSetNamedPortsRequest regionInstanceGroupsSetNamedPortsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setNamedPortsOperationCallable() 
  * setNamedPortsCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRegionInstanceGroupRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionInstanceGroupsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionInstanceGroupsSettings regionInstanceGroupsSettings =
         RegionInstanceGroupsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create(regionInstanceGroupsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionInstanceGroupsSettings regionInstanceGroupsSettings =
         RegionInstanceGroupsSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create(regionInstanceGroupsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionInstanceGroupsClient

## Static Methods 

### create()
    
    
    public static final RegionInstanceGroupsClient create()

Constructs an instance of RegionInstanceGroupsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionInstanceGroupsSettings settings)
    
    
    public static final RegionInstanceGroupsClient create(RegionInstanceGroupsSettings settings)

Constructs an instance of RegionInstanceGroupsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionInstanceGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionInstanceGroupsStub stub)
    
    
    public static final RegionInstanceGroupsClient create(RegionInstanceGroupsStub stub)

Constructs an instance of RegionInstanceGroupsClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionInstanceGroupsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionInstanceGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionInstanceGroupsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupsClient)` |   
  
## Constructors 

### RegionInstanceGroupsClient(RegionInstanceGroupsSettings settings)
    
    
    protected RegionInstanceGroupsClient(RegionInstanceGroupsSettings settings)

Constructs an instance of RegionInstanceGroupsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionInstanceGroupsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupsSettings)`  
  
  
### RegionInstanceGroupsClient(RegionInstanceGroupsStub stub)
    
    
    protected RegionInstanceGroupsClient(RegionInstanceGroupsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionInstanceGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionInstanceGroupsStub)`  
  
  
## Methods 

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

### get(GetRegionInstanceGroupRequest request)
    
    
    public final InstanceGroup get(GetRegionInstanceGroupRequest request)

Returns the specified instance group resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       GetRegionInstanceGroupRequest request =
           GetRegionInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       InstanceGroup response = regionInstanceGroupsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegionInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionInstanceGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup)` |   
  
### get(String project, String region, String instanceGroup)
    
    
    public final InstanceGroup get(String project, String region, String instanceGroup)

Returns the specified instance group resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroup = "instanceGroup-1404696854";
       InstanceGroup response = regionInstanceGroupsClient.get(project, region, instanceGroup);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the instance group resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[InstanceGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRegionInstanceGroupRequest,InstanceGroup> getCallable()

Returns the specified instance group resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       GetRegionInstanceGroupRequest request =
           GetRegionInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<InstanceGroup> future =
           regionInstanceGroupsClient.getCallable().futureCall(request);
       // Do something.
       InstanceGroup response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegionInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionInstanceGroupRequest),[InstanceGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroup)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionInstanceGroupsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RegionInstanceGroupsSettings` |   
  
### getStub()
    
    
    public RegionInstanceGroupsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionInstanceGroupsStub)` |   
  
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
  
### list(ListRegionInstanceGroupsRequest request)
    
    
    public final RegionInstanceGroupsClient.ListPagedResponse list(ListRegionInstanceGroupsRequest request)

Retrieves the list of instance group resources contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       ListRegionInstanceGroupsRequest request =
           ListRegionInstanceGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (InstanceGroup element : regionInstanceGroupsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionInstanceGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionInstanceGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupsClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final RegionInstanceGroupsClient.ListPagedResponse list(String project, String region)

Retrieves the list of instance group resources contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (InstanceGroup element : regionInstanceGroupsClient.list(project, region).iterateAll()) {
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
`[RegionInstanceGroupsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRegionInstanceGroupsRequest,RegionInstanceGroupList> listCallable()

Retrieves the list of instance group resources contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       ListRegionInstanceGroupsRequest request =
           ListRegionInstanceGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         RegionInstanceGroupList response = regionInstanceGroupsClient.listCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionInstanceGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionInstanceGroupsRequest),[RegionInstanceGroupList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupList)>` |   
  
### listInstances(ListInstancesRegionInstanceGroupsRequest request)
    
    
    public final RegionInstanceGroupsClient.ListInstancesPagedResponse listInstances(ListInstancesRegionInstanceGroupsRequest request)

Lists the instances in the specified instance group and displays information about the named ports. Depending on the specified options, this method can list all instances or only the instances that are running. The orderBy query parameter is not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       ListInstancesRegionInstanceGroupsRequest request =
           ListInstancesRegionInstanceGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroup("instanceGroup-1404696854")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupsListInstancesRequestResource(
                   RegionInstanceGroupsListInstancesRequest.newBuilder().build())
               .build();
       for (InstanceWithNamedPorts element :
           regionInstanceGroupsClient.listInstances(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRegionInstanceGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstancesRegionInstanceGroupsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupsClient.ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupsClient.ListInstancesPagedResponse)` |   
  
### listInstances(String project, String region, String instanceGroup, RegionInstanceGroupsListInstancesRequest regionInstanceGroupsListInstancesRequestResource)
    
    
    public final RegionInstanceGroupsClient.ListInstancesPagedResponse listInstances(String project, String region, String instanceGroup, RegionInstanceGroupsListInstancesRequest regionInstanceGroupsListInstancesRequestResource)

Lists the instances in the specified instance group and displays information about the named ports. Depending on the specified options, this method can list all instances or only the instances that are running. The orderBy query parameter is not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroup = "instanceGroup-1404696854";
       RegionInstanceGroupsListInstancesRequest regionInstanceGroupsListInstancesRequestResource =
           RegionInstanceGroupsListInstancesRequest.newBuilder().build();
       for (InstanceWithNamedPorts element :
           regionInstanceGroupsClient
               .listInstances(
                   project, region, instanceGroup, regionInstanceGroupsListInstancesRequestResource)
               .iterateAll()) {
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
`instanceGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the regional instance group for which we want to list the instances.  
`regionInstanceGroupsListInstancesRequestResource` | `[RegionInstanceGroupsListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupsListInstancesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[RegionInstanceGroupsClient.ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupsClient.ListInstancesPagedResponse)` |   
  
### listInstancesCallable()
    
    
    public final UnaryCallable<ListInstancesRegionInstanceGroupsRequest,RegionInstanceGroupsListInstances> listInstancesCallable()

Lists the instances in the specified instance group and displays information about the named ports. Depending on the specified options, this method can list all instances or only the instances that are running. The orderBy query parameter is not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       ListInstancesRegionInstanceGroupsRequest request =
           ListInstancesRegionInstanceGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroup("instanceGroup-1404696854")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupsListInstancesRequestResource(
                   RegionInstanceGroupsListInstancesRequest.newBuilder().build())
               .build();
       while (true) {
         RegionInstanceGroupsListInstances response =
             regionInstanceGroupsClient.listInstancesCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesRegionInstanceGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstancesRegionInstanceGroupsRequest),[RegionInstanceGroupsListInstances](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupsListInstances)>` |   
  
### listInstancesPagedCallable()
    
    
    public final UnaryCallable<ListInstancesRegionInstanceGroupsRequest,RegionInstanceGroupsClient.ListInstancesPagedResponse> listInstancesPagedCallable()

Lists the instances in the specified instance group and displays information about the named ports. Depending on the specified options, this method can list all instances or only the instances that are running. The orderBy query parameter is not supported.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       ListInstancesRegionInstanceGroupsRequest request =
           ListInstancesRegionInstanceGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setInstanceGroup("instanceGroup-1404696854")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupsListInstancesRequestResource(
                   RegionInstanceGroupsListInstancesRequest.newBuilder().build())
               .build();
       ApiFuture<InstanceWithNamedPorts> future =
           regionInstanceGroupsClient.listInstancesPagedCallable().futureCall(request);
       // Do something.
       for (InstanceWithNamedPorts element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListInstancesRegionInstanceGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListInstancesRegionInstanceGroupsRequest),[ListInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupsClient.ListInstancesPagedResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRegionInstanceGroupsRequest,RegionInstanceGroupsClient.ListPagedResponse> listPagedCallable()

Retrieves the list of instance group resources contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       ListRegionInstanceGroupsRequest request =
           ListRegionInstanceGroupsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<InstanceGroup> future =
           regionInstanceGroupsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (InstanceGroup element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionInstanceGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionInstanceGroupsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupsClient.ListPagedResponse)>` |   
  
### setNamedPortsAsync(SetNamedPortsRegionInstanceGroupRequest request)
    
    
    public final OperationFuture<Operation,Operation> setNamedPortsAsync(SetNamedPortsRegionInstanceGroupRequest request)

Sets the named ports for the specified regional instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       SetNamedPortsRegionInstanceGroupRequest request =
           SetNamedPortsRegionInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupsSetNamedPortsRequestResource(
                   RegionInstanceGroupsSetNamedPortsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionInstanceGroupsClient.setNamedPortsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetNamedPortsRegionInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetNamedPortsRegionInstanceGroupRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setNamedPortsAsync(String project, String region, String instanceGroup, RegionInstanceGroupsSetNamedPortsRequest regionInstanceGroupsSetNamedPortsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setNamedPortsAsync(String project, String region, String instanceGroup, RegionInstanceGroupsSetNamedPortsRequest regionInstanceGroupsSetNamedPortsRequestResource)

Sets the named ports for the specified regional instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String instanceGroup = "instanceGroup-1404696854";
       RegionInstanceGroupsSetNamedPortsRequest regionInstanceGroupsSetNamedPortsRequestResource =
           RegionInstanceGroupsSetNamedPortsRequest.newBuilder().build();
       Operation response =
           regionInstanceGroupsClient
               .setNamedPortsAsync(
                   project, region, instanceGroup, regionInstanceGroupsSetNamedPortsRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region scoping this request.  
`instanceGroup` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the regional instance group where the named ports are updated.  
`regionInstanceGroupsSetNamedPortsRequestResource` | `[RegionInstanceGroupsSetNamedPortsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionInstanceGroupsSetNamedPortsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setNamedPortsCallable()
    
    
    public final UnaryCallable<SetNamedPortsRegionInstanceGroupRequest,Operation> setNamedPortsCallable()

Sets the named ports for the specified regional instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       SetNamedPortsRegionInstanceGroupRequest request =
           SetNamedPortsRegionInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupsSetNamedPortsRequestResource(
                   RegionInstanceGroupsSetNamedPortsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionInstanceGroupsClient.setNamedPortsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetNamedPortsRegionInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetNamedPortsRegionInstanceGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setNamedPortsOperationCallable()
    
    
    public final OperationCallable<SetNamedPortsRegionInstanceGroupRequest,Operation,Operation> setNamedPortsOperationCallable()

Sets the named ports for the specified regional instance group.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       SetNamedPortsRegionInstanceGroupRequest request =
           SetNamedPortsRegionInstanceGroupRequest.newBuilder()
               .setInstanceGroup("instanceGroup-1404696854")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionInstanceGroupsSetNamedPortsRequestResource(
                   RegionInstanceGroupsSetNamedPortsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionInstanceGroupsClient.setNamedPortsOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetNamedPortsRegionInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetNamedPortsRegionInstanceGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRegionInstanceGroupRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsRegionInstanceGroupRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       TestIamPermissionsRegionInstanceGroupRequest request =
           TestIamPermissionsRegionInstanceGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = regionInstanceGroupsClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRegionInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionInstanceGroupRequest)`  
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
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           regionInstanceGroupsClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsRegionInstanceGroupRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionInstanceGroupsClient regionInstanceGroupsClient =
         RegionInstanceGroupsClient.create()) {
       TestIamPermissionsRegionInstanceGroupRequest request =
           TestIamPermissionsRegionInstanceGroupRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           regionInstanceGroupsClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsRegionInstanceGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionInstanceGroupRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
