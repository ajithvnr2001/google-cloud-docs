---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient
title: Class ProjectsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:19.433696+00:00
---

# Class ProjectsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ProjectsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/ProjectsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The Projects API.

This client uses Projects version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       String project = "project-309310695";
       Project response = projectsClient.get(project);
     }
     

Note: close() needs to be called on the ProjectsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
DisableXpnHost |  Disable this project as a shared VPC host project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * disableXpnHostAsync(DisableXpnHostProjectRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * disableXpnHostAsync(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * disableXpnHostOperationCallable() 
  * disableXpnHostCallable() 

  
DisableXpnResource |  Disable a service resource (also known as service project) associated with this host project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * disableXpnResourceAsync(DisableXpnResourceProjectRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * disableXpnResourceAsync(String project, ProjectsDisableXpnResourceRequest projectsDisableXpnResourceRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * disableXpnResourceOperationCallable() 
  * disableXpnResourceCallable() 

  
EnableXpnHost |  Enable this project as a shared VPC host project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * enableXpnHostAsync(EnableXpnHostProjectRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * enableXpnHostAsync(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * enableXpnHostOperationCallable() 
  * enableXpnHostCallable() 

  
EnableXpnResource |  Enable service resource (a.k.a service project) for a host project, so that subnets in the host project can be used by instances in the service project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * enableXpnResourceAsync(EnableXpnResourceProjectRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * enableXpnResourceAsync(String project, ProjectsEnableXpnResourceRequest projectsEnableXpnResourceRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * enableXpnResourceOperationCallable() 
  * enableXpnResourceCallable() 

  
Get |  Returns the specified Project resource.  To decrease latency for this method, you can optionally omit any unneeded information from the response by using a field mask. This practice is especially recommended for unused quota information (the `quotas` field). To exclude one or more fields, set your request's `fields` query parameter to only include the fields you need. For example, to only include the `id` and `selfLink` fields, add the query parameter `?fields=id,selfLink` to your request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetProjectRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetXpnHost |  Gets the shared VPC host project that this project links to. May be empty if no link exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getXpnHost(GetXpnHostProjectRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getXpnHost(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getXpnHostCallable() 

  
GetXpnResources |  Gets service resources (a.k.a service project) associated with this host project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getXpnResources(GetXpnResourcesProjectsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getXpnResources(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getXpnResourcesPagedCallable() 
  * getXpnResourcesCallable() 

  
ListXpnHosts |  Lists all shared VPC host projects visible to the user in an organization. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listXpnHosts(ListXpnHostsProjectsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listXpnHosts(String project, ProjectsListXpnHostsRequest projectsListXpnHostsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listXpnHostsPagedCallable() 
  * listXpnHostsCallable() 

  
MoveDisk |  Moves a persistent disk from one zone to another. 

  * Note*: The moveDisk API will be deprecated on September 29, 2026. 

Starting September 29, 2025, you can't use the moveDisk API on new projects. To move a disk to a different region or zone, follow the steps in [Change the location of a disk](https://cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hd).  Projects that already use the moveDisk API can continue usage until September 29, 2026.  Starting November 1, 2025, API responses will include a warning message in the response body about the upcoming deprecation. You can skip the message to continue using the service without interruption. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * moveDiskAsync(MoveDiskProjectRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * moveDiskAsync(String project, DiskMoveRequest diskMoveRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * moveDiskOperationCallable() 
  * moveDiskCallable() 

  
MoveInstance |  Moves an instance and its attached persistent disks from one zone to another. 

  * Note*: Moving VMs or disks by using this method might cause unexpected behavior. For more information, see the [known issue](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#moving_vms_or_disks_using_the_moveinstance_api_or_the_causes_unexpected_behavior). [Deprecated] This method is deprecated. See [moving instance across zones](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones) instead. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * moveInstanceAsync(MoveInstanceProjectRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * moveInstanceAsync(String project, InstanceMoveRequest instanceMoveRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * moveInstanceOperationCallable() 
  * moveInstanceCallable() 

  
SetCloudArmorTier |  Sets the Cloud Armor tier of the project. To set ENTERPRISE or above the billing account of the project must be subscribed to Cloud Armor Enterprise. See Subscribing to Cloud Armor Enterprise for more information. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setCloudArmorTierAsync(SetCloudArmorTierProjectRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setCloudArmorTierAsync(String project, ProjectsSetCloudArmorTierRequest projectsSetCloudArmorTierRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setCloudArmorTierOperationCallable() 
  * setCloudArmorTierCallable() 

  
SetCommonInstanceMetadata |  Sets metadata common to all instances within the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setCommonInstanceMetadataAsync(SetCommonInstanceMetadataProjectRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setCommonInstanceMetadataAsync(String project, Metadata metadataResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setCommonInstanceMetadataOperationCallable() 
  * setCommonInstanceMetadataCallable() 

  
SetDefaultNetworkTier |  Sets the default network tier of the project. The default network tier is used when an address/forwardingRule/instance is created without specifying the network tier field. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setDefaultNetworkTierAsync(SetDefaultNetworkTierProjectRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setDefaultNetworkTierAsync(String project, ProjectsSetDefaultNetworkTierRequest projectsSetDefaultNetworkTierRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setDefaultNetworkTierOperationCallable() 
  * setDefaultNetworkTierCallable() 

  
SetUsageExportBucket |  Enables the usage export feature and sets theusage export bucket where reports are stored. If you provide an empty request body using this method, the usage export feature will be disabled. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setUsageExportBucketAsync(SetUsageExportBucketProjectRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setUsageExportBucketAsync(String project, UsageExportLocation usageExportLocationResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setUsageExportBucketOperationCallable() 
  * setUsageExportBucketCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ProjectsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ProjectsSettings projectsSettings =
         ProjectsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ProjectsClient projectsClient = ProjectsClient.create(projectsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ProjectsSettings projectsSettings =
         ProjectsSettings.newBuilder().setEndpoint(myEndpoint).build();
     ProjectsClient projectsClient = ProjectsClient.create(projectsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ProjectsClient

## Static Methods 

### create()
    
    
    public static final ProjectsClient create()

Constructs an instance of ProjectsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ProjectsSettings settings)
    
    
    public static final ProjectsClient create(ProjectsSettings settings)

Constructs an instance of ProjectsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ProjectsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ProjectsStub stub)
    
    
    public static final ProjectsClient create(ProjectsStub stub)

Constructs an instance of ProjectsClient, using the given stub for making calls. This is for advanced usage - prefer using create(ProjectsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ProjectsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ProjectsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient)` |   
  
## Constructors 

### ProjectsClient(ProjectsSettings settings)
    
    
    protected ProjectsClient(ProjectsSettings settings)

Constructs an instance of ProjectsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ProjectsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsSettings)`  
  
  
### ProjectsClient(ProjectsStub stub)
    
    
    protected ProjectsClient(ProjectsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ProjectsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ProjectsStub)`  
  
  
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

### disableXpnHostAsync(DisableXpnHostProjectRequest request)
    
    
    public final OperationFuture<Operation,Operation> disableXpnHostAsync(DisableXpnHostProjectRequest request)

Disable this project as a shared VPC host project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       DisableXpnHostProjectRequest request =
           DisableXpnHostProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = projectsClient.disableXpnHostAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DisableXpnHostProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisableXpnHostProjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### disableXpnHostAsync(String project)
    
    
    public final OperationFuture<Operation,Operation> disableXpnHostAsync(String project)

Disable this project as a shared VPC host project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       String project = "project-309310695";
       Operation response = projectsClient.disableXpnHostAsync(project).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### disableXpnHostCallable()
    
    
    public final UnaryCallable<DisableXpnHostProjectRequest,Operation> disableXpnHostCallable()

Disable this project as a shared VPC host project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       DisableXpnHostProjectRequest request =
           DisableXpnHostProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = projectsClient.disableXpnHostCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DisableXpnHostProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisableXpnHostProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### disableXpnHostOperationCallable()
    
    
    public final OperationCallable<DisableXpnHostProjectRequest,Operation,Operation> disableXpnHostOperationCallable()

Disable this project as a shared VPC host project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       DisableXpnHostProjectRequest request =
           DisableXpnHostProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           projectsClient.disableXpnHostOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DisableXpnHostProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisableXpnHostProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### disableXpnResourceAsync(DisableXpnResourceProjectRequest request)
    
    
    public final OperationFuture<Operation,Operation> disableXpnResourceAsync(DisableXpnResourceProjectRequest request)

Disable a service resource (also known as service project) associated with this host project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       DisableXpnResourceProjectRequest request =
           DisableXpnResourceProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setProjectsDisableXpnResourceRequestResource(
                   ProjectsDisableXpnResourceRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = projectsClient.disableXpnResourceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DisableXpnResourceProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisableXpnResourceProjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### disableXpnResourceAsync(String project, ProjectsDisableXpnResourceRequest projectsDisableXpnResourceRequestResource)
    
    
    public final OperationFuture<Operation,Operation> disableXpnResourceAsync(String project, ProjectsDisableXpnResourceRequest projectsDisableXpnResourceRequestResource)

Disable a service resource (also known as service project) associated with this host project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       String project = "project-309310695";
       ProjectsDisableXpnResourceRequest projectsDisableXpnResourceRequestResource =
           ProjectsDisableXpnResourceRequest.newBuilder().build();
       Operation response =
           projectsClient
               .disableXpnResourceAsync(project, projectsDisableXpnResourceRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`projectsDisableXpnResourceRequestResource` | `[ProjectsDisableXpnResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsDisableXpnResourceRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### disableXpnResourceCallable()
    
    
    public final UnaryCallable<DisableXpnResourceProjectRequest,Operation> disableXpnResourceCallable()

Disable a service resource (also known as service project) associated with this host project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       DisableXpnResourceProjectRequest request =
           DisableXpnResourceProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setProjectsDisableXpnResourceRequestResource(
                   ProjectsDisableXpnResourceRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = projectsClient.disableXpnResourceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DisableXpnResourceProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisableXpnResourceProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### disableXpnResourceOperationCallable()
    
    
    public final OperationCallable<DisableXpnResourceProjectRequest,Operation,Operation> disableXpnResourceOperationCallable()

Disable a service resource (also known as service project) associated with this host project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       DisableXpnResourceProjectRequest request =
           DisableXpnResourceProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setProjectsDisableXpnResourceRequestResource(
                   ProjectsDisableXpnResourceRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           projectsClient.disableXpnResourceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DisableXpnResourceProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisableXpnResourceProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### enableXpnHostAsync(EnableXpnHostProjectRequest request)
    
    
    public final OperationFuture<Operation,Operation> enableXpnHostAsync(EnableXpnHostProjectRequest request)

Enable this project as a shared VPC host project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       EnableXpnHostProjectRequest request =
           EnableXpnHostProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = projectsClient.enableXpnHostAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EnableXpnHostProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.EnableXpnHostProjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### enableXpnHostAsync(String project)
    
    
    public final OperationFuture<Operation,Operation> enableXpnHostAsync(String project)

Enable this project as a shared VPC host project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       String project = "project-309310695";
       Operation response = projectsClient.enableXpnHostAsync(project).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### enableXpnHostCallable()
    
    
    public final UnaryCallable<EnableXpnHostProjectRequest,Operation> enableXpnHostCallable()

Enable this project as a shared VPC host project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       EnableXpnHostProjectRequest request =
           EnableXpnHostProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = projectsClient.enableXpnHostCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[EnableXpnHostProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.EnableXpnHostProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### enableXpnHostOperationCallable()
    
    
    public final OperationCallable<EnableXpnHostProjectRequest,Operation,Operation> enableXpnHostOperationCallable()

Enable this project as a shared VPC host project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       EnableXpnHostProjectRequest request =
           EnableXpnHostProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           projectsClient.enableXpnHostOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[EnableXpnHostProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.EnableXpnHostProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### enableXpnResourceAsync(EnableXpnResourceProjectRequest request)
    
    
    public final OperationFuture<Operation,Operation> enableXpnResourceAsync(EnableXpnResourceProjectRequest request)

Enable service resource (a.k.a service project) for a host project, so that subnets in the host project can be used by instances in the service project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       EnableXpnResourceProjectRequest request =
           EnableXpnResourceProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setProjectsEnableXpnResourceRequestResource(
                   ProjectsEnableXpnResourceRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = projectsClient.enableXpnResourceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EnableXpnResourceProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.EnableXpnResourceProjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### enableXpnResourceAsync(String project, ProjectsEnableXpnResourceRequest projectsEnableXpnResourceRequestResource)
    
    
    public final OperationFuture<Operation,Operation> enableXpnResourceAsync(String project, ProjectsEnableXpnResourceRequest projectsEnableXpnResourceRequestResource)

Enable service resource (a.k.a service project) for a host project, so that subnets in the host project can be used by instances in the service project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       String project = "project-309310695";
       ProjectsEnableXpnResourceRequest projectsEnableXpnResourceRequestResource =
           ProjectsEnableXpnResourceRequest.newBuilder().build();
       Operation response =
           projectsClient
               .enableXpnResourceAsync(project, projectsEnableXpnResourceRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`projectsEnableXpnResourceRequestResource` | `[ProjectsEnableXpnResourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsEnableXpnResourceRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### enableXpnResourceCallable()
    
    
    public final UnaryCallable<EnableXpnResourceProjectRequest,Operation> enableXpnResourceCallable()

Enable service resource (a.k.a service project) for a host project, so that subnets in the host project can be used by instances in the service project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       EnableXpnResourceProjectRequest request =
           EnableXpnResourceProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setProjectsEnableXpnResourceRequestResource(
                   ProjectsEnableXpnResourceRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = projectsClient.enableXpnResourceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[EnableXpnResourceProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.EnableXpnResourceProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### enableXpnResourceOperationCallable()
    
    
    public final OperationCallable<EnableXpnResourceProjectRequest,Operation,Operation> enableXpnResourceOperationCallable()

Enable service resource (a.k.a service project) for a host project, so that subnets in the host project can be used by instances in the service project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       EnableXpnResourceProjectRequest request =
           EnableXpnResourceProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setProjectsEnableXpnResourceRequestResource(
                   ProjectsEnableXpnResourceRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           projectsClient.enableXpnResourceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[EnableXpnResourceProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.EnableXpnResourceProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetProjectRequest request)
    
    
    public final Project get(GetProjectRequest request)

Returns the specified Project resource.

To decrease latency for this method, you can optionally omit any unneeded information from the response by using a field mask. This practice is especially recommended for unused quota information (the `quotas` field). To exclude one or more fields, set your request's `fields` query parameter to only include the fields you need. For example, to only include the `id` and `selfLink` fields, add the query parameter `?fields=id,selfLink` to your request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       GetProjectRequest request =
           GetProjectRequest.newBuilder().setProject("project-309310695").build();
       Project response = projectsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetProjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Project)` |   
  
### get(String project)
    
    
    public final Project get(String project)

Returns the specified Project resource.

To decrease latency for this method, you can optionally omit any unneeded information from the response by using a field mask. This practice is especially recommended for unused quota information (the `quotas` field). To exclude one or more fields, set your request's `fields` query parameter to only include the fields you need. For example, to only include the `id` and `selfLink` fields, add the query parameter `?fields=id,selfLink` to your request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       String project = "project-309310695";
       Project response = projectsClient.get(project);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
**Returns**  
---  
**Type** | **Description**  
`[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Project)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetProjectRequest,Project> getCallable()

Returns the specified Project resource.

To decrease latency for this method, you can optionally omit any unneeded information from the response by using a field mask. This practice is especially recommended for unused quota information (the `quotas` field). To exclude one or more fields, set your request's `fields` query parameter to only include the fields you need. For example, to only include the `id` and `selfLink` fields, add the query parameter `?fields=id,selfLink` to your request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       GetProjectRequest request =
           GetProjectRequest.newBuilder().setProject("project-309310695").build();
       ApiFuture<Project> future = projectsClient.getCallable().futureCall(request);
       // Do something.
       Project response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetProjectRequest),[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Project)>` |   
  
### getSettings()
    
    
    public final @Nullable ProjectsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.ProjectsSettings` |   
  
### getStub()
    
    
    public ProjectsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ProjectsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.ProjectsStub)` |   
  
### getXpnHost(GetXpnHostProjectRequest request)
    
    
    public final Project getXpnHost(GetXpnHostProjectRequest request)

Gets the shared VPC host project that this project links to. May be empty if no link exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       GetXpnHostProjectRequest request =
           GetXpnHostProjectRequest.newBuilder().setProject("project-309310695").build();
       Project response = projectsClient.getXpnHost(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetXpnHostProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetXpnHostProjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Project)` |   
  
### getXpnHost(String project)
    
    
    public final Project getXpnHost(String project)

Gets the shared VPC host project that this project links to. May be empty if no link exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       String project = "project-309310695";
       Project response = projectsClient.getXpnHost(project);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
**Returns**  
---  
**Type** | **Description**  
`[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Project)` |   
  
### getXpnHostCallable()
    
    
    public final UnaryCallable<GetXpnHostProjectRequest,Project> getXpnHostCallable()

Gets the shared VPC host project that this project links to. May be empty if no link exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       GetXpnHostProjectRequest request =
           GetXpnHostProjectRequest.newBuilder().setProject("project-309310695").build();
       ApiFuture<Project> future = projectsClient.getXpnHostCallable().futureCall(request);
       // Do something.
       Project response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetXpnHostProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetXpnHostProjectRequest),[Project](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Project)>` |   
  
### getXpnResources(GetXpnResourcesProjectsRequest request)
    
    
    public final ProjectsClient.GetXpnResourcesPagedResponse getXpnResources(GetXpnResourcesProjectsRequest request)

Gets service resources (a.k.a service project) associated with this host project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       GetXpnResourcesProjectsRequest request =
           GetXpnResourcesProjectsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (XpnResourceId element : projectsClient.getXpnResources(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetXpnResourcesProjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetXpnResourcesProjectsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProjectsClient.GetXpnResourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient.GetXpnResourcesPagedResponse)` |   
  
### getXpnResources(String project)
    
    
    public final ProjectsClient.GetXpnResourcesPagedResponse getXpnResources(String project)

Gets service resources (a.k.a service project) associated with this host project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       String project = "project-309310695";
       for (XpnResourceId element : projectsClient.getXpnResources(project).iterateAll()) {
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
`[ProjectsClient.GetXpnResourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient.GetXpnResourcesPagedResponse)` |   
  
### getXpnResourcesCallable()
    
    
    public final UnaryCallable<GetXpnResourcesProjectsRequest,ProjectsGetXpnResources> getXpnResourcesCallable()

Gets service resources (a.k.a service project) associated with this host project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       GetXpnResourcesProjectsRequest request =
           GetXpnResourcesProjectsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         ProjectsGetXpnResources response = projectsClient.getXpnResourcesCallable().call(request);
         for (XpnResourceId element : response.getResourcesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetXpnResourcesProjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetXpnResourcesProjectsRequest),[ProjectsGetXpnResources](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsGetXpnResources)>` |   
  
### getXpnResourcesPagedCallable()
    
    
    public final UnaryCallable<GetXpnResourcesProjectsRequest,ProjectsClient.GetXpnResourcesPagedResponse> getXpnResourcesPagedCallable()

Gets service resources (a.k.a service project) associated with this host project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       GetXpnResourcesProjectsRequest request =
           GetXpnResourcesProjectsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<XpnResourceId> future =
           projectsClient.getXpnResourcesPagedCallable().futureCall(request);
       // Do something.
       for (XpnResourceId element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetXpnResourcesProjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetXpnResourcesProjectsRequest),[GetXpnResourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient.GetXpnResourcesPagedResponse)>` |   
  
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
  
### listXpnHosts(ListXpnHostsProjectsRequest request)
    
    
    public final ProjectsClient.ListXpnHostsPagedResponse listXpnHosts(ListXpnHostsProjectsRequest request)

Lists all shared VPC host projects visible to the user in an organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       ListXpnHostsProjectsRequest request =
           ListXpnHostsProjectsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setProjectsListXpnHostsRequestResource(
                   ProjectsListXpnHostsRequest.newBuilder().build())
               .build();
       for (Project element : projectsClient.listXpnHosts(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListXpnHostsProjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListXpnHostsProjectsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ProjectsClient.ListXpnHostsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient.ListXpnHostsPagedResponse)` |   
  
### listXpnHosts(String project, ProjectsListXpnHostsRequest projectsListXpnHostsRequestResource)
    
    
    public final ProjectsClient.ListXpnHostsPagedResponse listXpnHosts(String project, ProjectsListXpnHostsRequest projectsListXpnHostsRequestResource)

Lists all shared VPC host projects visible to the user in an organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       String project = "project-309310695";
       ProjectsListXpnHostsRequest projectsListXpnHostsRequestResource =
           ProjectsListXpnHostsRequest.newBuilder().build();
       for (Project element :
           projectsClient.listXpnHosts(project, projectsListXpnHostsRequestResource).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`projectsListXpnHostsRequestResource` | `[ProjectsListXpnHostsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsListXpnHostsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[ProjectsClient.ListXpnHostsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient.ListXpnHostsPagedResponse)` |   
  
### listXpnHostsCallable()
    
    
    public final UnaryCallable<ListXpnHostsProjectsRequest,XpnHostList> listXpnHostsCallable()

Lists all shared VPC host projects visible to the user in an organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       ListXpnHostsProjectsRequest request =
           ListXpnHostsProjectsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setProjectsListXpnHostsRequestResource(
                   ProjectsListXpnHostsRequest.newBuilder().build())
               .build();
       while (true) {
         XpnHostList response = projectsClient.listXpnHostsCallable().call(request);
         for (Project element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListXpnHostsProjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListXpnHostsProjectsRequest),[XpnHostList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.XpnHostList)>` |   
  
### listXpnHostsPagedCallable()
    
    
    public final UnaryCallable<ListXpnHostsProjectsRequest,ProjectsClient.ListXpnHostsPagedResponse> listXpnHostsPagedCallable()

Lists all shared VPC host projects visible to the user in an organization.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       ListXpnHostsProjectsRequest request =
           ListXpnHostsProjectsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setProjectsListXpnHostsRequestResource(
                   ProjectsListXpnHostsRequest.newBuilder().build())
               .build();
       ApiFuture<Project> future = projectsClient.listXpnHostsPagedCallable().futureCall(request);
       // Do something.
       for (Project element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListXpnHostsProjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListXpnHostsProjectsRequest),[ListXpnHostsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsClient.ListXpnHostsPagedResponse)>` |   
  
### moveDiskAsync(MoveDiskProjectRequest request)
    
    
    public final OperationFuture<Operation,Operation> moveDiskAsync(MoveDiskProjectRequest request)

Moves a persistent disk from one zone to another.

  * Note*: The moveDisk API will be deprecated on September 29, 2026. 



Starting September 29, 2025, you can't use the moveDisk API on new projects. To move a disk to a different region or zone, follow the steps in [Change the location of a disk](https://cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hd).

Projects that already use the moveDisk API can continue usage until September 29, 2026.

Starting November 1, 2025, API responses will include a warning message in the response body about the upcoming deprecation. You can skip the message to continue using the service without interruption.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       MoveDiskProjectRequest request =
           MoveDiskProjectRequest.newBuilder()
               .setDiskMoveRequestResource(DiskMoveRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = projectsClient.moveDiskAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MoveDiskProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MoveDiskProjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### moveDiskAsync(String project, DiskMoveRequest diskMoveRequestResource)
    
    
    public final OperationFuture<Operation,Operation> moveDiskAsync(String project, DiskMoveRequest diskMoveRequestResource)

Moves a persistent disk from one zone to another.

  * Note*: The moveDisk API will be deprecated on September 29, 2026. 



Starting September 29, 2025, you can't use the moveDisk API on new projects. To move a disk to a different region or zone, follow the steps in [Change the location of a disk](https://cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hd).

Projects that already use the moveDisk API can continue usage until September 29, 2026.

Starting November 1, 2025, API responses will include a warning message in the response body about the upcoming deprecation. You can skip the message to continue using the service without interruption.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       String project = "project-309310695";
       DiskMoveRequest diskMoveRequestResource = DiskMoveRequest.newBuilder().build();
       Operation response = projectsClient.moveDiskAsync(project, diskMoveRequestResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`diskMoveRequestResource` | `[DiskMoveRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskMoveRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### moveDiskCallable()
    
    
    public final UnaryCallable<MoveDiskProjectRequest,Operation> moveDiskCallable()

Moves a persistent disk from one zone to another.

  * Note*: The moveDisk API will be deprecated on September 29, 2026. 



Starting September 29, 2025, you can't use the moveDisk API on new projects. To move a disk to a different region or zone, follow the steps in [Change the location of a disk](https://cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hd).

Projects that already use the moveDisk API can continue usage until September 29, 2026.

Starting November 1, 2025, API responses will include a warning message in the response body about the upcoming deprecation. You can skip the message to continue using the service without interruption.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       MoveDiskProjectRequest request =
           MoveDiskProjectRequest.newBuilder()
               .setDiskMoveRequestResource(DiskMoveRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = projectsClient.moveDiskCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MoveDiskProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MoveDiskProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### moveDiskOperationCallable()
    
    
    public final OperationCallable<MoveDiskProjectRequest,Operation,Operation> moveDiskOperationCallable()

Moves a persistent disk from one zone to another.

  * Note*: The moveDisk API will be deprecated on September 29, 2026. 



Starting September 29, 2025, you can't use the moveDisk API on new projects. To move a disk to a different region or zone, follow the steps in [Change the location of a disk](https://cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hd).

Projects that already use the moveDisk API can continue usage until September 29, 2026.

Starting November 1, 2025, API responses will include a warning message in the response body about the upcoming deprecation. You can skip the message to continue using the service without interruption.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       MoveDiskProjectRequest request =
           MoveDiskProjectRequest.newBuilder()
               .setDiskMoveRequestResource(DiskMoveRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           projectsClient.moveDiskOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[MoveDiskProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MoveDiskProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### moveInstanceAsync(MoveInstanceProjectRequest request)
    
    
    public final OperationFuture<Operation,Operation> moveInstanceAsync(MoveInstanceProjectRequest request)

Moves an instance and its attached persistent disks from one zone to another.

  * Note*: Moving VMs or disks by using this method might cause unexpected behavior. For more information, see the [known issue](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#moving_vms_or_disks_using_the_moveinstance_api_or_the_causes_unexpected_behavior). [Deprecated] This method is deprecated. See [moving instance across zones](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones) instead. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       MoveInstanceProjectRequest request =
           MoveInstanceProjectRequest.newBuilder()
               .setInstanceMoveRequestResource(InstanceMoveRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = projectsClient.moveInstanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MoveInstanceProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MoveInstanceProjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### moveInstanceAsync(String project, InstanceMoveRequest instanceMoveRequestResource)
    
    
    public final OperationFuture<Operation,Operation> moveInstanceAsync(String project, InstanceMoveRequest instanceMoveRequestResource)

Moves an instance and its attached persistent disks from one zone to another.

  * Note*: Moving VMs or disks by using this method might cause unexpected behavior. For more information, see the [known issue](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#moving_vms_or_disks_using_the_moveinstance_api_or_the_causes_unexpected_behavior). [Deprecated] This method is deprecated. See [moving instance across zones](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones) instead. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       String project = "project-309310695";
       InstanceMoveRequest instanceMoveRequestResource = InstanceMoveRequest.newBuilder().build();
       Operation response =
           projectsClient.moveInstanceAsync(project, instanceMoveRequestResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`instanceMoveRequestResource` | `[InstanceMoveRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceMoveRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### moveInstanceCallable()
    
    
    public final UnaryCallable<MoveInstanceProjectRequest,Operation> moveInstanceCallable()

Moves an instance and its attached persistent disks from one zone to another.

  * Note*: Moving VMs or disks by using this method might cause unexpected behavior. For more information, see the [known issue](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#moving_vms_or_disks_using_the_moveinstance_api_or_the_causes_unexpected_behavior). [Deprecated] This method is deprecated. See [moving instance across zones](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones) instead. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       MoveInstanceProjectRequest request =
           MoveInstanceProjectRequest.newBuilder()
               .setInstanceMoveRequestResource(InstanceMoveRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = projectsClient.moveInstanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MoveInstanceProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MoveInstanceProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### moveInstanceOperationCallable()
    
    
    public final OperationCallable<MoveInstanceProjectRequest,Operation,Operation> moveInstanceOperationCallable()

Moves an instance and its attached persistent disks from one zone to another.

  * Note*: Moving VMs or disks by using this method might cause unexpected behavior. For more information, see the [known issue](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#moving_vms_or_disks_using_the_moveinstance_api_or_the_causes_unexpected_behavior). [Deprecated] This method is deprecated. See [moving instance across zones](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones) instead. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       MoveInstanceProjectRequest request =
           MoveInstanceProjectRequest.newBuilder()
               .setInstanceMoveRequestResource(InstanceMoveRequest.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           projectsClient.moveInstanceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[MoveInstanceProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MoveInstanceProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setCloudArmorTierAsync(SetCloudArmorTierProjectRequest request)
    
    
    public final OperationFuture<Operation,Operation> setCloudArmorTierAsync(SetCloudArmorTierProjectRequest request)

Sets the Cloud Armor tier of the project. To set ENTERPRISE or above the billing account of the project must be subscribed to Cloud Armor Enterprise. See Subscribing to Cloud Armor Enterprise for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       SetCloudArmorTierProjectRequest request =
           SetCloudArmorTierProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setProjectsSetCloudArmorTierRequestResource(
                   ProjectsSetCloudArmorTierRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = projectsClient.setCloudArmorTierAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetCloudArmorTierProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetCloudArmorTierProjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setCloudArmorTierAsync(String project, ProjectsSetCloudArmorTierRequest projectsSetCloudArmorTierRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setCloudArmorTierAsync(String project, ProjectsSetCloudArmorTierRequest projectsSetCloudArmorTierRequestResource)

Sets the Cloud Armor tier of the project. To set ENTERPRISE or above the billing account of the project must be subscribed to Cloud Armor Enterprise. See Subscribing to Cloud Armor Enterprise for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       String project = "project-309310695";
       ProjectsSetCloudArmorTierRequest projectsSetCloudArmorTierRequestResource =
           ProjectsSetCloudArmorTierRequest.newBuilder().build();
       Operation response =
           projectsClient
               .setCloudArmorTierAsync(project, projectsSetCloudArmorTierRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`projectsSetCloudArmorTierRequestResource` | `[ProjectsSetCloudArmorTierRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsSetCloudArmorTierRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setCloudArmorTierCallable()
    
    
    public final UnaryCallable<SetCloudArmorTierProjectRequest,Operation> setCloudArmorTierCallable()

Sets the Cloud Armor tier of the project. To set ENTERPRISE or above the billing account of the project must be subscribed to Cloud Armor Enterprise. See Subscribing to Cloud Armor Enterprise for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       SetCloudArmorTierProjectRequest request =
           SetCloudArmorTierProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setProjectsSetCloudArmorTierRequestResource(
                   ProjectsSetCloudArmorTierRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = projectsClient.setCloudArmorTierCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetCloudArmorTierProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetCloudArmorTierProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setCloudArmorTierOperationCallable()
    
    
    public final OperationCallable<SetCloudArmorTierProjectRequest,Operation,Operation> setCloudArmorTierOperationCallable()

Sets the Cloud Armor tier of the project. To set ENTERPRISE or above the billing account of the project must be subscribed to Cloud Armor Enterprise. See Subscribing to Cloud Armor Enterprise for more information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       SetCloudArmorTierProjectRequest request =
           SetCloudArmorTierProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setProjectsSetCloudArmorTierRequestResource(
                   ProjectsSetCloudArmorTierRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           projectsClient.setCloudArmorTierOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetCloudArmorTierProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetCloudArmorTierProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setCommonInstanceMetadataAsync(SetCommonInstanceMetadataProjectRequest request)
    
    
    public final OperationFuture<Operation,Operation> setCommonInstanceMetadataAsync(SetCommonInstanceMetadataProjectRequest request)

Sets metadata common to all instances within the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       SetCommonInstanceMetadataProjectRequest request =
           SetCommonInstanceMetadataProjectRequest.newBuilder()
               .setMetadataResource(Metadata.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       Operation response = projectsClient.setCommonInstanceMetadataAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetCommonInstanceMetadataProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetCommonInstanceMetadataProjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setCommonInstanceMetadataAsync(String project, Metadata metadataResource)
    
    
    public final OperationFuture<Operation,Operation> setCommonInstanceMetadataAsync(String project, Metadata metadataResource)

Sets metadata common to all instances within the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       String project = "project-309310695";
       Metadata metadataResource = Metadata.newBuilder().build();
       Operation response =
           projectsClient.setCommonInstanceMetadataAsync(project, metadataResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`metadataResource` | `[Metadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Metadata)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setCommonInstanceMetadataCallable()
    
    
    public final UnaryCallable<SetCommonInstanceMetadataProjectRequest,Operation> setCommonInstanceMetadataCallable()

Sets metadata common to all instances within the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       SetCommonInstanceMetadataProjectRequest request =
           SetCommonInstanceMetadataProjectRequest.newBuilder()
               .setMetadataResource(Metadata.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           projectsClient.setCommonInstanceMetadataCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetCommonInstanceMetadataProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetCommonInstanceMetadataProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setCommonInstanceMetadataOperationCallable()
    
    
    public final OperationCallable<SetCommonInstanceMetadataProjectRequest,Operation,Operation> setCommonInstanceMetadataOperationCallable()

Sets metadata common to all instances within the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       SetCommonInstanceMetadataProjectRequest request =
           SetCommonInstanceMetadataProjectRequest.newBuilder()
               .setMetadataResource(Metadata.newBuilder().build())
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           projectsClient.setCommonInstanceMetadataOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetCommonInstanceMetadataProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetCommonInstanceMetadataProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setDefaultNetworkTierAsync(SetDefaultNetworkTierProjectRequest request)
    
    
    public final OperationFuture<Operation,Operation> setDefaultNetworkTierAsync(SetDefaultNetworkTierProjectRequest request)

Sets the default network tier of the project. The default network tier is used when an address/forwardingRule/instance is created without specifying the network tier field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       SetDefaultNetworkTierProjectRequest request =
           SetDefaultNetworkTierProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setProjectsSetDefaultNetworkTierRequestResource(
                   ProjectsSetDefaultNetworkTierRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = projectsClient.setDefaultNetworkTierAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetDefaultNetworkTierProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDefaultNetworkTierProjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setDefaultNetworkTierAsync(String project, ProjectsSetDefaultNetworkTierRequest projectsSetDefaultNetworkTierRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setDefaultNetworkTierAsync(String project, ProjectsSetDefaultNetworkTierRequest projectsSetDefaultNetworkTierRequestResource)

Sets the default network tier of the project. The default network tier is used when an address/forwardingRule/instance is created without specifying the network tier field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       String project = "project-309310695";
       ProjectsSetDefaultNetworkTierRequest projectsSetDefaultNetworkTierRequestResource =
           ProjectsSetDefaultNetworkTierRequest.newBuilder().build();
       Operation response =
           projectsClient
               .setDefaultNetworkTierAsync(project, projectsSetDefaultNetworkTierRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`projectsSetDefaultNetworkTierRequestResource` | `[ProjectsSetDefaultNetworkTierRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ProjectsSetDefaultNetworkTierRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setDefaultNetworkTierCallable()
    
    
    public final UnaryCallable<SetDefaultNetworkTierProjectRequest,Operation> setDefaultNetworkTierCallable()

Sets the default network tier of the project. The default network tier is used when an address/forwardingRule/instance is created without specifying the network tier field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       SetDefaultNetworkTierProjectRequest request =
           SetDefaultNetworkTierProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setProjectsSetDefaultNetworkTierRequestResource(
                   ProjectsSetDefaultNetworkTierRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           projectsClient.setDefaultNetworkTierCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetDefaultNetworkTierProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDefaultNetworkTierProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setDefaultNetworkTierOperationCallable()
    
    
    public final OperationCallable<SetDefaultNetworkTierProjectRequest,Operation,Operation> setDefaultNetworkTierOperationCallable()

Sets the default network tier of the project. The default network tier is used when an address/forwardingRule/instance is created without specifying the network tier field.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       SetDefaultNetworkTierProjectRequest request =
           SetDefaultNetworkTierProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setProjectsSetDefaultNetworkTierRequestResource(
                   ProjectsSetDefaultNetworkTierRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           projectsClient.setDefaultNetworkTierOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetDefaultNetworkTierProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDefaultNetworkTierProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUsageExportBucketAsync(SetUsageExportBucketProjectRequest request)
    
    
    public final OperationFuture<Operation,Operation> setUsageExportBucketAsync(SetUsageExportBucketProjectRequest request)

Enables the usage export feature and sets theusage export bucket where reports are stored. If you provide an empty request body using this method, the usage export feature will be disabled.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       SetUsageExportBucketProjectRequest request =
           SetUsageExportBucketProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUsageExportLocationResource(UsageExportLocation.newBuilder().build())
               .build();
       Operation response = projectsClient.setUsageExportBucketAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetUsageExportBucketProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUsageExportBucketProjectRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUsageExportBucketAsync(String project, UsageExportLocation usageExportLocationResource)
    
    
    public final OperationFuture<Operation,Operation> setUsageExportBucketAsync(String project, UsageExportLocation usageExportLocationResource)

Enables the usage export feature and sets theusage export bucket where reports are stored. If you provide an empty request body using this method, the usage export feature will be disabled.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       String project = "project-309310695";
       UsageExportLocation usageExportLocationResource = UsageExportLocation.newBuilder().build();
       Operation response =
           projectsClient.setUsageExportBucketAsync(project, usageExportLocationResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`usageExportLocationResource` | `[UsageExportLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UsageExportLocation)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUsageExportBucketCallable()
    
    
    public final UnaryCallable<SetUsageExportBucketProjectRequest,Operation> setUsageExportBucketCallable()

Enables the usage export feature and sets theusage export bucket where reports are stored. If you provide an empty request body using this method, the usage export feature will be disabled.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       SetUsageExportBucketProjectRequest request =
           SetUsageExportBucketProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUsageExportLocationResource(UsageExportLocation.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           projectsClient.setUsageExportBucketCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetUsageExportBucketProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUsageExportBucketProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setUsageExportBucketOperationCallable()
    
    
    public final OperationCallable<SetUsageExportBucketProjectRequest,Operation,Operation> setUsageExportBucketOperationCallable()

Enables the usage export feature and sets theusage export bucket where reports are stored. If you provide an empty request body using this method, the usage export feature will be disabled.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ProjectsClient projectsClient = ProjectsClient.create()) {
       SetUsageExportBucketProjectRequest request =
           SetUsageExportBucketProjectRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setUsageExportLocationResource(UsageExportLocation.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           projectsClient.setUsageExportBucketOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetUsageExportBucketProjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetUsageExportBucketProjectRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
