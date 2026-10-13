---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient
title: Class RegionDisksClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:33.491735+00:00
---

# Class RegionDisksClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionDisksClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RegionDisksClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RegionDisks API.

This client uses RegionDisks version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String disk = "disk3083677";
       Disk response = regionDisksClient.get(project, region, disk);
     }
     

Note: close() needs to be called on the RegionDisksClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
AddResourcePolicies |  Adds existing resource policies to a regional disk. You can only add one policy which will be applied to this disk for scheduling snapshot creation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * addResourcePoliciesAsync(AddResourcePoliciesRegionDiskRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * addResourcePoliciesAsync(String project, String region, String disk, RegionDisksAddResourcePoliciesRequest regionDisksAddResourcePoliciesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * addResourcePoliciesOperationCallable() 
  * addResourcePoliciesCallable() 

  
BulkInsert |  Bulk create a set of disks. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * bulkInsertAsync(BulkInsertRegionDiskRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * bulkInsertAsync(String project, String region, BulkInsertDiskResource bulkInsertDiskResourceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * bulkInsertOperationCallable() 
  * bulkInsertCallable() 

  
CreateSnapshot |  Creates a snapshot of a specified persistent disk. For regular snapshot creation, consider using snapshots.insert instead, as that method supports more features, such as creating snapshots in a project different from the source disk project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSnapshotAsync(CreateSnapshotRegionDiskRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createSnapshotAsync(String project, String region, String disk, Snapshot snapshotResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSnapshotOperationCallable() 
  * createSnapshotCallable() 

  
Delete |  Deletes the specified regional persistent disk. Deleting a regional disk removes all the replicas of its data permanently and is irreversible. However, deleting a disk does not delete anysnapshots previously made from the disk. You must separatelydelete snapshots. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRegionDiskRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String disk) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns a specified regional persistent disk. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRegionDiskRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String disk) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRegionDiskRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String region, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
Insert |  Creates a persistent regional disk in the specified project using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRegionDiskRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, Disk diskResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of persistent disks contained within the specified region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRegionDisksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
RemoveResourcePolicies |  Removes resource policies from a regional disk. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * removeResourcePoliciesAsync(RemoveResourcePoliciesRegionDiskRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * removeResourcePoliciesAsync(String project, String region, String disk, RegionDisksRemoveResourcePoliciesRequest regionDisksRemoveResourcePoliciesRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * removeResourcePoliciesOperationCallable() 
  * removeResourcePoliciesCallable() 

  
Resize |  Resizes the specified regional persistent disk. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resizeAsync(ResizeRegionDiskRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * resizeAsync(String project, String region, String disk, RegionDisksResizeRequest regionDisksResizeRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resizeOperationCallable() 
  * resizeCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRegionDiskRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String region, String resource, RegionSetPolicyRequest regionSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
SetLabels |  Sets the labels on the target regional disk. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setLabelsAsync(SetLabelsRegionDiskRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setLabelsAsync(String project, String region, String resource, RegionSetLabelsRequest regionSetLabelsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setLabelsOperationCallable() 
  * setLabelsCallable() 

  
StartAsyncReplication |  Starts asynchronous replication. Must be invoked on the primary disk. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * startAsyncReplicationAsync(StartAsyncReplicationRegionDiskRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * startAsyncReplicationAsync(String project, String region, String disk, RegionDisksStartAsyncReplicationRequest regionDisksStartAsyncReplicationRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * startAsyncReplicationOperationCallable() 
  * startAsyncReplicationCallable() 

  
StopAsyncReplication |  Stops asynchronous replication. Can be invoked either on the primary or on the secondary disk. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * stopAsyncReplicationAsync(StopAsyncReplicationRegionDiskRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * stopAsyncReplicationAsync(String project, String region, String disk) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * stopAsyncReplicationOperationCallable() 
  * stopAsyncReplicationCallable() 

  
StopGroupAsyncReplication |  Stops asynchronous replication for a consistency group of disks. Can be invoked either in the primary or secondary scope. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * stopGroupAsyncReplicationAsync(StopGroupAsyncReplicationRegionDiskRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * stopGroupAsyncReplicationAsync(String project, String region, DisksStopGroupAsyncReplicationResource disksStopGroupAsyncReplicationResourceResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * stopGroupAsyncReplicationOperationCallable() 
  * stopGroupAsyncReplicationCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRegionDiskRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
Update |  Update the specified disk with the data included in the request. Update is performed only on selected fields included as part of update-mask. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAsync(UpdateRegionDiskRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAsync(String project, String region, String disk, Disk diskResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateOperationCallable() 
  * updateCallable() 

  
UpdateKmsKey |  Rotates the customer-managed encryption key to the latest version for the specified persistent disk. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateKmsKeyAsync(UpdateKmsKeyRegionDiskRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateKmsKeyAsync(String project, String region, String disk, RegionDiskUpdateKmsKeyRequest regionDiskUpdateKmsKeyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateKmsKeyOperationCallable() 
  * updateKmsKeyCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionDisksSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionDisksSettings regionDisksSettings =
         RegionDisksSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegionDisksClient regionDisksClient = RegionDisksClient.create(regionDisksSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionDisksSettings regionDisksSettings =
         RegionDisksSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegionDisksClient regionDisksClient = RegionDisksClient.create(regionDisksSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionDisksClient

## Static Methods 

### create()
    
    
    public static final RegionDisksClient create()

Constructs an instance of RegionDisksClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionDisksSettings settings)
    
    
    public static final RegionDisksClient create(RegionDisksSettings settings)

Constructs an instance of RegionDisksClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionDisksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionDisksStub stub)
    
    
    public static final RegionDisksClient create(RegionDisksStub stub)

Constructs an instance of RegionDisksClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionDisksSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionDisksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionDisksStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient)` |   
  
## Constructors 

### RegionDisksClient(RegionDisksSettings settings)
    
    
    protected RegionDisksClient(RegionDisksSettings settings)

Constructs an instance of RegionDisksClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionDisksSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksSettings)`  
  
  
### RegionDisksClient(RegionDisksStub stub)
    
    
    protected RegionDisksClient(RegionDisksStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionDisksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionDisksStub)`  
  
  
## Methods 

### addResourcePoliciesAsync(AddResourcePoliciesRegionDiskRequest request)
    
    
    public final OperationFuture<Operation,Operation> addResourcePoliciesAsync(AddResourcePoliciesRegionDiskRequest request)

Adds existing resource policies to a regional disk. You can only add one policy which will be applied to this disk for scheduling snapshot creation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       AddResourcePoliciesRegionDiskRequest request =
           AddResourcePoliciesRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionDisksAddResourcePoliciesRequestResource(
                   RegionDisksAddResourcePoliciesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionDisksClient.addResourcePoliciesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AddResourcePoliciesRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddResourcePoliciesRegionDiskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addResourcePoliciesAsync(String project, String region, String disk, RegionDisksAddResourcePoliciesRequest regionDisksAddResourcePoliciesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> addResourcePoliciesAsync(String project, String region, String disk, RegionDisksAddResourcePoliciesRequest regionDisksAddResourcePoliciesRequestResource)

Adds existing resource policies to a regional disk. You can only add one policy which will be applied to this disk for scheduling snapshot creation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String disk = "disk3083677";
       RegionDisksAddResourcePoliciesRequest regionDisksAddResourcePoliciesRequestResource =
           RegionDisksAddResourcePoliciesRequest.newBuilder().build();
       Operation response =
           regionDisksClient
               .addResourcePoliciesAsync(
                   project, region, disk, regionDisksAddResourcePoliciesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`disk` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The disk name for this request.  
`regionDisksAddResourcePoliciesRequestResource` | `[RegionDisksAddResourcePoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksAddResourcePoliciesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addResourcePoliciesCallable()
    
    
    public final UnaryCallable<AddResourcePoliciesRegionDiskRequest,Operation> addResourcePoliciesCallable()

Adds existing resource policies to a regional disk. You can only add one policy which will be applied to this disk for scheduling snapshot creation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       AddResourcePoliciesRegionDiskRequest request =
           AddResourcePoliciesRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionDisksAddResourcePoliciesRequestResource(
                   RegionDisksAddResourcePoliciesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionDisksClient.addResourcePoliciesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AddResourcePoliciesRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddResourcePoliciesRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addResourcePoliciesOperationCallable()
    
    
    public final OperationCallable<AddResourcePoliciesRegionDiskRequest,Operation,Operation> addResourcePoliciesOperationCallable()

Adds existing resource policies to a regional disk. You can only add one policy which will be applied to this disk for scheduling snapshot creation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       AddResourcePoliciesRegionDiskRequest request =
           AddResourcePoliciesRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionDisksAddResourcePoliciesRequestResource(
                   RegionDisksAddResourcePoliciesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionDisksClient.addResourcePoliciesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AddResourcePoliciesRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddResourcePoliciesRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### bulkInsertAsync(BulkInsertRegionDiskRequest request)
    
    
    public final OperationFuture<Operation,Operation> bulkInsertAsync(BulkInsertRegionDiskRequest request)

Bulk create a set of disks.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       BulkInsertRegionDiskRequest request =
           BulkInsertRegionDiskRequest.newBuilder()
               .setBulkInsertDiskResourceResource(BulkInsertDiskResource.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionDisksClient.bulkInsertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BulkInsertRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BulkInsertRegionDiskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### bulkInsertAsync(String project, String region, BulkInsertDiskResource bulkInsertDiskResourceResource)
    
    
    public final OperationFuture<Operation,Operation> bulkInsertAsync(String project, String region, BulkInsertDiskResource bulkInsertDiskResourceResource)

Bulk create a set of disks.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       BulkInsertDiskResource bulkInsertDiskResourceResource =
           BulkInsertDiskResource.newBuilder().build();
       Operation response =
           regionDisksClient.bulkInsertAsync(project, region, bulkInsertDiskResourceResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`bulkInsertDiskResourceResource` | `[BulkInsertDiskResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BulkInsertDiskResource)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### bulkInsertCallable()
    
    
    public final UnaryCallable<BulkInsertRegionDiskRequest,Operation> bulkInsertCallable()

Bulk create a set of disks.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       BulkInsertRegionDiskRequest request =
           BulkInsertRegionDiskRequest.newBuilder()
               .setBulkInsertDiskResourceResource(BulkInsertDiskResource.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = regionDisksClient.bulkInsertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BulkInsertRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BulkInsertRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### bulkInsertOperationCallable()
    
    
    public final OperationCallable<BulkInsertRegionDiskRequest,Operation,Operation> bulkInsertOperationCallable()

Bulk create a set of disks.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       BulkInsertRegionDiskRequest request =
           BulkInsertRegionDiskRequest.newBuilder()
               .setBulkInsertDiskResourceResource(BulkInsertDiskResource.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionDisksClient.bulkInsertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BulkInsertRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BulkInsertRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### close()
    
    
    public final void close()

### createSnapshotAsync(CreateSnapshotRegionDiskRequest request)
    
    
    public final OperationFuture<Operation,Operation> createSnapshotAsync(CreateSnapshotRegionDiskRequest request)

Creates a snapshot of a specified persistent disk. For regular snapshot creation, consider using snapshots.insert instead, as that method supports more features, such as creating snapshots in a project different from the source disk project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       CreateSnapshotRegionDiskRequest request =
           CreateSnapshotRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSnapshotResource(Snapshot.newBuilder().build())
               .build();
       Operation response = regionDisksClient.createSnapshotAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSnapshotRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CreateSnapshotRegionDiskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### createSnapshotAsync(String project, String region, String disk, Snapshot snapshotResource)
    
    
    public final OperationFuture<Operation,Operation> createSnapshotAsync(String project, String region, String disk, Snapshot snapshotResource)

Creates a snapshot of a specified persistent disk. For regular snapshot creation, consider using snapshots.insert instead, as that method supports more features, such as creating snapshots in a project different from the source disk project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String disk = "disk3083677";
       Snapshot snapshotResource = Snapshot.newBuilder().build();
       Operation response =
           regionDisksClient.createSnapshotAsync(project, region, disk, snapshotResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`disk` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the regional persistent disk to snapshot.  
`snapshotResource` | `[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### createSnapshotCallable()
    
    
    public final UnaryCallable<CreateSnapshotRegionDiskRequest,Operation> createSnapshotCallable()

Creates a snapshot of a specified persistent disk. For regular snapshot creation, consider using snapshots.insert instead, as that method supports more features, such as creating snapshots in a project different from the source disk project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       CreateSnapshotRegionDiskRequest request =
           CreateSnapshotRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSnapshotResource(Snapshot.newBuilder().build())
               .build();
       ApiFuture<Operation> future = regionDisksClient.createSnapshotCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSnapshotRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CreateSnapshotRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### createSnapshotOperationCallable()
    
    
    public final OperationCallable<CreateSnapshotRegionDiskRequest,Operation,Operation> createSnapshotOperationCallable()

Creates a snapshot of a specified persistent disk. For regular snapshot creation, consider using snapshots.insert instead, as that method supports more features, such as creating snapshots in a project different from the source disk project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       CreateSnapshotRegionDiskRequest request =
           CreateSnapshotRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSnapshotResource(Snapshot.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           regionDisksClient.createSnapshotOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateSnapshotRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CreateSnapshotRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(DeleteRegionDiskRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRegionDiskRequest request)

Deletes the specified regional persistent disk. Deleting a regional disk removes all the replicas of its data permanently and is irreversible. However, deleting a disk does not delete anysnapshots previously made from the disk. You must separatelydelete snapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       DeleteRegionDiskRequest request =
           DeleteRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionDisksClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionDiskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String disk)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String disk)

Deletes the specified regional persistent disk. Deleting a regional disk removes all the replicas of its data permanently and is irreversible. However, deleting a disk does not delete anysnapshots previously made from the disk. You must separatelydelete snapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String disk = "disk3083677";
       Operation response = regionDisksClient.deleteAsync(project, region, disk).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`disk` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the regional persistent disk to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRegionDiskRequest,Operation> deleteCallable()

Deletes the specified regional persistent disk. Deleting a regional disk removes all the replicas of its data permanently and is irreversible. However, deleting a disk does not delete anysnapshots previously made from the disk. You must separatelydelete snapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       DeleteRegionDiskRequest request =
           DeleteRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = regionDisksClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRegionDiskRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified regional persistent disk. Deleting a regional disk removes all the replicas of its data permanently and is irreversible. However, deleting a disk does not delete anysnapshots previously made from the disk. You must separatelydelete snapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       DeleteRegionDiskRequest request =
           DeleteRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionDisksClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRegionDiskRequest request)
    
    
    public final Disk get(GetRegionDiskRequest request)

Returns a specified regional persistent disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       GetRegionDiskRequest request =
           GetRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       Disk response = regionDisksClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionDiskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk)` |   
  
### get(String project, String region, String disk)
    
    
    public final Disk get(String project, String region, String disk)

Returns a specified regional persistent disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String disk = "disk3083677";
       Disk response = regionDisksClient.get(project, region, disk);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`disk` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the regional persistent disk to return.  
**Returns**  
---  
**Type** | **Description**  
`[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRegionDiskRequest,Disk> getCallable()

Returns a specified regional persistent disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       GetRegionDiskRequest request =
           GetRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<Disk> future = regionDisksClient.getCallable().futureCall(request);
       // Do something.
       Disk response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionDiskRequest),[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk)>` |   
  
### getIamPolicy(GetIamPolicyRegionDiskRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRegionDiskRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       GetIamPolicyRegionDiskRequest request =
           GetIamPolicyRegionDiskRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .build();
       Policy response = regionDisksClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyRegionDiskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicy(String project, String region, String resource)
    
    
    public final Policy getIamPolicy(String project, String region, String resource)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       Policy response = regionDisksClient.getIamPolicy(project, region, resource);
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
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRegionDiskRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       GetIamPolicyRegionDiskRequest request =
           GetIamPolicyRegionDiskRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = regionDisksClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyRegionDiskRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionDisksSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RegionDisksSettings` |   
  
### getStub()
    
    
    public RegionDisksStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionDisksStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionDisksStub)` |   
  
### insertAsync(InsertRegionDiskRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRegionDiskRequest request)

Creates a persistent regional disk in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       InsertRegionDiskRequest request =
           InsertRegionDiskRequest.newBuilder()
               .setDiskResource(Disk.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSourceImage("sourceImage-105174528")
               .build();
       Operation response = regionDisksClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionDiskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, Disk diskResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, Disk diskResource)

Creates a persistent regional disk in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       Disk diskResource = Disk.newBuilder().build();
       Operation response = regionDisksClient.insertAsync(project, region, diskResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`diskResource` | `[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRegionDiskRequest,Operation> insertCallable()

Creates a persistent regional disk in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       InsertRegionDiskRequest request =
           InsertRegionDiskRequest.newBuilder()
               .setDiskResource(Disk.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSourceImage("sourceImage-105174528")
               .build();
       ApiFuture<Operation> future = regionDisksClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRegionDiskRequest,Operation,Operation> insertOperationCallable()

Creates a persistent regional disk in the specified project using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       InsertRegionDiskRequest request =
           InsertRegionDiskRequest.newBuilder()
               .setDiskResource(Disk.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSourceImage("sourceImage-105174528")
               .build();
       OperationFuture<Operation, Operation> future =
           regionDisksClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRegionDisksRequest request)
    
    
    public final RegionDisksClient.ListPagedResponse list(ListRegionDisksRequest request)

Retrieves the list of persistent disks contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       ListRegionDisksRequest request =
           ListRegionDisksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (Disk element : regionDisksClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionDisksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionDisksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionDisksClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final RegionDisksClient.ListPagedResponse list(String project, String region)

Retrieves the list of persistent disks contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (Disk element : regionDisksClient.list(project, region).iterateAll()) {
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
`[RegionDisksClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRegionDisksRequest,DiskList> listCallable()

Retrieves the list of persistent disks contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       ListRegionDisksRequest request =
           ListRegionDisksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         DiskList response = regionDisksClient.listCallable().call(request);
         for (Disk element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionDisksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionDisksRequest),[DiskList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRegionDisksRequest,RegionDisksClient.ListPagedResponse> listPagedCallable()

Retrieves the list of persistent disks contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       ListRegionDisksRequest request =
           ListRegionDisksRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<Disk> future = regionDisksClient.listPagedCallable().futureCall(request);
       // Do something.
       for (Disk element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionDisksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionDisksRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.ListPagedResponse)>` |   
  
### removeResourcePoliciesAsync(RemoveResourcePoliciesRegionDiskRequest request)
    
    
    public final OperationFuture<Operation,Operation> removeResourcePoliciesAsync(RemoveResourcePoliciesRegionDiskRequest request)

Removes resource policies from a regional disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       RemoveResourcePoliciesRegionDiskRequest request =
           RemoveResourcePoliciesRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionDisksRemoveResourcePoliciesRequestResource(
                   RegionDisksRemoveResourcePoliciesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionDisksClient.removeResourcePoliciesAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveResourcePoliciesRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveResourcePoliciesRegionDiskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeResourcePoliciesAsync(String project, String region, String disk, RegionDisksRemoveResourcePoliciesRequest regionDisksRemoveResourcePoliciesRequestResource)
    
    
    public final OperationFuture<Operation,Operation> removeResourcePoliciesAsync(String project, String region, String disk, RegionDisksRemoveResourcePoliciesRequest regionDisksRemoveResourcePoliciesRequestResource)

Removes resource policies from a regional disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String disk = "disk3083677";
       RegionDisksRemoveResourcePoliciesRequest regionDisksRemoveResourcePoliciesRequestResource =
           RegionDisksRemoveResourcePoliciesRequest.newBuilder().build();
       Operation response =
           regionDisksClient
               .removeResourcePoliciesAsync(
                   project, region, disk, regionDisksRemoveResourcePoliciesRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`disk` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The disk name for this request.  
`regionDisksRemoveResourcePoliciesRequestResource` | `[RegionDisksRemoveResourcePoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksRemoveResourcePoliciesRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeResourcePoliciesCallable()
    
    
    public final UnaryCallable<RemoveResourcePoliciesRegionDiskRequest,Operation> removeResourcePoliciesCallable()

Removes resource policies from a regional disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       RemoveResourcePoliciesRegionDiskRequest request =
           RemoveResourcePoliciesRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionDisksRemoveResourcePoliciesRequestResource(
                   RegionDisksRemoveResourcePoliciesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionDisksClient.removeResourcePoliciesCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RemoveResourcePoliciesRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveResourcePoliciesRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeResourcePoliciesOperationCallable()
    
    
    public final OperationCallable<RemoveResourcePoliciesRegionDiskRequest,Operation,Operation> removeResourcePoliciesOperationCallable()

Removes resource policies from a regional disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       RemoveResourcePoliciesRegionDiskRequest request =
           RemoveResourcePoliciesRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionDisksRemoveResourcePoliciesRequestResource(
                   RegionDisksRemoveResourcePoliciesRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionDisksClient.removeResourcePoliciesOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RemoveResourcePoliciesRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveResourcePoliciesRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resizeAsync(ResizeRegionDiskRequest request)
    
    
    public final OperationFuture<Operation,Operation> resizeAsync(ResizeRegionDiskRequest request)

Resizes the specified regional persistent disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       ResizeRegionDiskRequest request =
           ResizeRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionDisksResizeRequestResource(RegionDisksResizeRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionDisksClient.resizeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResizeRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResizeRegionDiskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resizeAsync(String project, String region, String disk, RegionDisksResizeRequest regionDisksResizeRequestResource)
    
    
    public final OperationFuture<Operation,Operation> resizeAsync(String project, String region, String disk, RegionDisksResizeRequest regionDisksResizeRequestResource)

Resizes the specified regional persistent disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String disk = "disk3083677";
       RegionDisksResizeRequest regionDisksResizeRequestResource =
           RegionDisksResizeRequest.newBuilder().build();
       Operation response =
           regionDisksClient
               .resizeAsync(project, region, disk, regionDisksResizeRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`disk` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the regional persistent disk.  
`regionDisksResizeRequestResource` | `[RegionDisksResizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksResizeRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resizeCallable()
    
    
    public final UnaryCallable<ResizeRegionDiskRequest,Operation> resizeCallable()

Resizes the specified regional persistent disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       ResizeRegionDiskRequest request =
           ResizeRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionDisksResizeRequestResource(RegionDisksResizeRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = regionDisksClient.resizeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResizeRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResizeRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resizeOperationCallable()
    
    
    public final OperationCallable<ResizeRegionDiskRequest,Operation,Operation> resizeOperationCallable()

Resizes the specified regional persistent disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       ResizeRegionDiskRequest request =
           ResizeRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionDisksResizeRequestResource(RegionDisksResizeRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionDisksClient.resizeOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ResizeRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResizeRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setIamPolicy(SetIamPolicyRegionDiskRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRegionDiskRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       SetIamPolicyRegionDiskRequest request =
           SetIamPolicyRegionDiskRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetPolicyRequestResource(RegionSetPolicyRequest.newBuilder().build())
               .setResource("resource-341064690")
               .build();
       Policy response = regionDisksClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyRegionDiskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicy(String project, String region, String resource, RegionSetPolicyRequest regionSetPolicyRequestResource)
    
    
    public final Policy setIamPolicy(String project, String region, String resource, RegionSetPolicyRequest regionSetPolicyRequestResource)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       RegionSetPolicyRequest regionSetPolicyRequestResource =
           RegionSetPolicyRequest.newBuilder().build();
       Policy response =
           regionDisksClient.setIamPolicy(project, region, resource, regionSetPolicyRequestResource);
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
`regionSetPolicyRequestResource` | `[RegionSetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSetPolicyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRegionDiskRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       SetIamPolicyRegionDiskRequest request =
           SetIamPolicyRegionDiskRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetPolicyRequestResource(RegionSetPolicyRequest.newBuilder().build())
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = regionDisksClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyRegionDiskRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### setLabelsAsync(SetLabelsRegionDiskRequest request)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(SetLabelsRegionDiskRequest request)

Sets the labels on the target regional disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       SetLabelsRegionDiskRequest request =
           SetLabelsRegionDiskRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetLabelsRequestResource(RegionSetLabelsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .build();
       Operation response = regionDisksClient.setLabelsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetLabelsRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsRegionDiskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsAsync(String project, String region, String resource, RegionSetLabelsRequest regionSetLabelsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(String project, String region, String resource, RegionSetLabelsRequest regionSetLabelsRequestResource)

Sets the labels on the target regional disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       RegionSetLabelsRequest regionSetLabelsRequestResource =
           RegionSetLabelsRequest.newBuilder().build();
       Operation response =
           regionDisksClient
               .setLabelsAsync(project, region, resource, regionSetLabelsRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The region for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`regionSetLabelsRequestResource` | `[RegionSetLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSetLabelsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsCallable()
    
    
    public final UnaryCallable<SetLabelsRegionDiskRequest,Operation> setLabelsCallable()

Sets the labels on the target regional disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       SetLabelsRegionDiskRequest request =
           SetLabelsRegionDiskRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetLabelsRequestResource(RegionSetLabelsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Operation> future = regionDisksClient.setLabelsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLabelsRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsOperationCallable()
    
    
    public final OperationCallable<SetLabelsRegionDiskRequest,Operation,Operation> setLabelsOperationCallable()

Sets the labels on the target regional disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       SetLabelsRegionDiskRequest request =
           SetLabelsRegionDiskRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetLabelsRequestResource(RegionSetLabelsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .build();
       OperationFuture<Operation, Operation> future =
           regionDisksClient.setLabelsOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetLabelsRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### startAsyncReplicationAsync(StartAsyncReplicationRegionDiskRequest request)
    
    
    public final OperationFuture<Operation,Operation> startAsyncReplicationAsync(StartAsyncReplicationRegionDiskRequest request)

Starts asynchronous replication. Must be invoked on the primary disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       StartAsyncReplicationRegionDiskRequest request =
           StartAsyncReplicationRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionDisksStartAsyncReplicationRequestResource(
                   RegionDisksStartAsyncReplicationRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionDisksClient.startAsyncReplicationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartAsyncReplicationRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartAsyncReplicationRegionDiskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startAsyncReplicationAsync(String project, String region, String disk, RegionDisksStartAsyncReplicationRequest regionDisksStartAsyncReplicationRequestResource)
    
    
    public final OperationFuture<Operation,Operation> startAsyncReplicationAsync(String project, String region, String disk, RegionDisksStartAsyncReplicationRequest regionDisksStartAsyncReplicationRequestResource)

Starts asynchronous replication. Must be invoked on the primary disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String disk = "disk3083677";
       RegionDisksStartAsyncReplicationRequest regionDisksStartAsyncReplicationRequestResource =
           RegionDisksStartAsyncReplicationRequest.newBuilder().build();
       Operation response =
           regionDisksClient
               .startAsyncReplicationAsync(
                   project, region, disk, regionDisksStartAsyncReplicationRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`disk` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the persistent disk.  
`regionDisksStartAsyncReplicationRequestResource` | `[RegionDisksStartAsyncReplicationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksStartAsyncReplicationRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startAsyncReplicationCallable()
    
    
    public final UnaryCallable<StartAsyncReplicationRegionDiskRequest,Operation> startAsyncReplicationCallable()

Starts asynchronous replication. Must be invoked on the primary disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       StartAsyncReplicationRegionDiskRequest request =
           StartAsyncReplicationRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionDisksStartAsyncReplicationRequestResource(
                   RegionDisksStartAsyncReplicationRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionDisksClient.startAsyncReplicationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StartAsyncReplicationRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartAsyncReplicationRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### startAsyncReplicationOperationCallable()
    
    
    public final OperationCallable<StartAsyncReplicationRegionDiskRequest,Operation,Operation> startAsyncReplicationOperationCallable()

Starts asynchronous replication. Must be invoked on the primary disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       StartAsyncReplicationRegionDiskRequest request =
           StartAsyncReplicationRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionDisksStartAsyncReplicationRequestResource(
                   RegionDisksStartAsyncReplicationRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionDisksClient.startAsyncReplicationOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StartAsyncReplicationRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartAsyncReplicationRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopAsyncReplicationAsync(StopAsyncReplicationRegionDiskRequest request)
    
    
    public final OperationFuture<Operation,Operation> stopAsyncReplicationAsync(StopAsyncReplicationRegionDiskRequest request)

Stops asynchronous replication. Can be invoked either on the primary or on the secondary disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       StopAsyncReplicationRegionDiskRequest request =
           StopAsyncReplicationRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionDisksClient.stopAsyncReplicationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopAsyncReplicationRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopAsyncReplicationRegionDiskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopAsyncReplicationAsync(String project, String region, String disk)
    
    
    public final OperationFuture<Operation,Operation> stopAsyncReplicationAsync(String project, String region, String disk)

Stops asynchronous replication. Can be invoked either on the primary or on the secondary disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String disk = "disk3083677";
       Operation response = regionDisksClient.stopAsyncReplicationAsync(project, region, disk).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`disk` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the persistent disk.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopAsyncReplicationCallable()
    
    
    public final UnaryCallable<StopAsyncReplicationRegionDiskRequest,Operation> stopAsyncReplicationCallable()

Stops asynchronous replication. Can be invoked either on the primary or on the secondary disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       StopAsyncReplicationRegionDiskRequest request =
           StopAsyncReplicationRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionDisksClient.stopAsyncReplicationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StopAsyncReplicationRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopAsyncReplicationRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopAsyncReplicationOperationCallable()
    
    
    public final OperationCallable<StopAsyncReplicationRegionDiskRequest,Operation,Operation> stopAsyncReplicationOperationCallable()

Stops asynchronous replication. Can be invoked either on the primary or on the secondary disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       StopAsyncReplicationRegionDiskRequest request =
           StopAsyncReplicationRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionDisksClient.stopAsyncReplicationOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StopAsyncReplicationRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopAsyncReplicationRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopGroupAsyncReplicationAsync(StopGroupAsyncReplicationRegionDiskRequest request)
    
    
    public final OperationFuture<Operation,Operation> stopGroupAsyncReplicationAsync(StopGroupAsyncReplicationRegionDiskRequest request)

Stops asynchronous replication for a consistency group of disks. Can be invoked either in the primary or secondary scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       StopGroupAsyncReplicationRegionDiskRequest request =
           StopGroupAsyncReplicationRegionDiskRequest.newBuilder()
               .setDisksStopGroupAsyncReplicationResourceResource(
                   DisksStopGroupAsyncReplicationResource.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionDisksClient.stopGroupAsyncReplicationAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopGroupAsyncReplicationRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopGroupAsyncReplicationRegionDiskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopGroupAsyncReplicationAsync(String project, String region, DisksStopGroupAsyncReplicationResource disksStopGroupAsyncReplicationResourceResource)
    
    
    public final OperationFuture<Operation,Operation> stopGroupAsyncReplicationAsync(String project, String region, DisksStopGroupAsyncReplicationResource disksStopGroupAsyncReplicationResourceResource)

Stops asynchronous replication for a consistency group of disks. Can be invoked either in the primary or secondary scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       DisksStopGroupAsyncReplicationResource disksStopGroupAsyncReplicationResourceResource =
           DisksStopGroupAsyncReplicationResource.newBuilder().build();
       Operation response =
           regionDisksClient
               .stopGroupAsyncReplicationAsync(
                   project, region, disksStopGroupAsyncReplicationResourceResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request. This must be the region of the primary or secondary disks in the consistency group.  
`disksStopGroupAsyncReplicationResourceResource` | `[DisksStopGroupAsyncReplicationResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksStopGroupAsyncReplicationResource)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopGroupAsyncReplicationCallable()
    
    
    public final UnaryCallable<StopGroupAsyncReplicationRegionDiskRequest,Operation> stopGroupAsyncReplicationCallable()

Stops asynchronous replication for a consistency group of disks. Can be invoked either in the primary or secondary scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       StopGroupAsyncReplicationRegionDiskRequest request =
           StopGroupAsyncReplicationRegionDiskRequest.newBuilder()
               .setDisksStopGroupAsyncReplicationResourceResource(
                   DisksStopGroupAsyncReplicationResource.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           regionDisksClient.stopGroupAsyncReplicationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[StopGroupAsyncReplicationRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopGroupAsyncReplicationRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### stopGroupAsyncReplicationOperationCallable()
    
    
    public final OperationCallable<StopGroupAsyncReplicationRegionDiskRequest,Operation,Operation> stopGroupAsyncReplicationOperationCallable()

Stops asynchronous replication for a consistency group of disks. Can be invoked either in the primary or secondary scope.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       StopGroupAsyncReplicationRegionDiskRequest request =
           StopGroupAsyncReplicationRegionDiskRequest.newBuilder()
               .setDisksStopGroupAsyncReplicationResourceResource(
                   DisksStopGroupAsyncReplicationResource.newBuilder().build())
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionDisksClient.stopGroupAsyncReplicationOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[StopGroupAsyncReplicationRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopGroupAsyncReplicationRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### testIamPermissions(TestIamPermissionsRegionDiskRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsRegionDiskRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       TestIamPermissionsRegionDiskRequest request =
           TestIamPermissionsRegionDiskRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = regionDisksClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionDiskRequest)`  
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
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           regionDisksClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsRegionDiskRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       TestIamPermissionsRegionDiskRequest request =
           TestIamPermissionsRegionDiskRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           regionDisksClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionDiskRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
### updateAsync(UpdateRegionDiskRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(UpdateRegionDiskRequest request)

Update the specified disk with the data included in the request. Update is performed only on selected fields included as part of update-mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       UpdateRegionDiskRequest request =
           UpdateRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setDiskResource(Disk.newBuilder().build())
               .setPaths("paths106438894")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .build();
       Operation response = regionDisksClient.updateAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateRegionDiskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateAsync(String project, String region, String disk, Disk diskResource)
    
    
    public final OperationFuture<Operation,Operation> updateAsync(String project, String region, String disk, Disk diskResource)

Update the specified disk with the data included in the request. Update is performed only on selected fields included as part of update-mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String disk = "disk3083677";
       Disk diskResource = Disk.newBuilder().build();
       Operation response = regionDisksClient.updateAsync(project, region, disk, diskResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`disk` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The disk name for this request.  
`diskResource` | `[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateCallable()
    
    
    public final UnaryCallable<UpdateRegionDiskRequest,Operation> updateCallable()

Update the specified disk with the data included in the request. Update is performed only on selected fields included as part of update-mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       UpdateRegionDiskRequest request =
           UpdateRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setDiskResource(Disk.newBuilder().build())
               .setPaths("paths106438894")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .build();
       ApiFuture<Operation> future = regionDisksClient.updateCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateKmsKeyAsync(UpdateKmsKeyRegionDiskRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateKmsKeyAsync(UpdateKmsKeyRegionDiskRequest request)

Rotates the customer-managed encryption key to the latest version for the specified persistent disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       UpdateKmsKeyRegionDiskRequest request =
           UpdateKmsKeyRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionDiskUpdateKmsKeyRequestResource(
                   RegionDiskUpdateKmsKeyRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Operation response = regionDisksClient.updateKmsKeyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateKmsKeyRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateKmsKeyRegionDiskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateKmsKeyAsync(String project, String region, String disk, RegionDiskUpdateKmsKeyRequest regionDiskUpdateKmsKeyRequestResource)
    
    
    public final OperationFuture<Operation,Operation> updateKmsKeyAsync(String project, String region, String disk, RegionDiskUpdateKmsKeyRequest regionDiskUpdateKmsKeyRequestResource)

Rotates the customer-managed encryption key to the latest version for the specified persistent disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String disk = "disk3083677";
       RegionDiskUpdateKmsKeyRequest regionDiskUpdateKmsKeyRequestResource =
           RegionDiskUpdateKmsKeyRequest.newBuilder().build();
       Operation response =
           regionDisksClient
               .updateKmsKeyAsync(project, region, disk, regionDiskUpdateKmsKeyRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`disk` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Disk resource, should conform to RFC1035.  
`regionDiskUpdateKmsKeyRequestResource` | `[RegionDiskUpdateKmsKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDiskUpdateKmsKeyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateKmsKeyCallable()
    
    
    public final UnaryCallable<UpdateKmsKeyRegionDiskRequest,Operation> updateKmsKeyCallable()

Rotates the customer-managed encryption key to the latest version for the specified persistent disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       UpdateKmsKeyRegionDiskRequest request =
           UpdateKmsKeyRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionDiskUpdateKmsKeyRequestResource(
                   RegionDiskUpdateKmsKeyRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = regionDisksClient.updateKmsKeyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateKmsKeyRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateKmsKeyRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateKmsKeyOperationCallable()
    
    
    public final OperationCallable<UpdateKmsKeyRegionDiskRequest,Operation,Operation> updateKmsKeyOperationCallable()

Rotates the customer-managed encryption key to the latest version for the specified persistent disk.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       UpdateKmsKeyRegionDiskRequest request =
           UpdateKmsKeyRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionDiskUpdateKmsKeyRequestResource(
                   RegionDiskUpdateKmsKeyRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Operation, Operation> future =
           regionDisksClient.updateKmsKeyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateKmsKeyRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateKmsKeyRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateOperationCallable()
    
    
    public final OperationCallable<UpdateRegionDiskRequest,Operation,Operation> updateOperationCallable()

Update the specified disk with the data included in the request. Update is performed only on selected fields included as part of update-mask.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionDisksClient regionDisksClient = RegionDisksClient.create()) {
       UpdateRegionDiskRequest request =
           UpdateRegionDiskRequest.newBuilder()
               .setDisk("disk3083677")
               .setDiskResource(Disk.newBuilder().build())
               .setPaths("paths106438894")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setUpdateMask("updateMask-296147115")
               .build();
       OperationFuture<Operation, Operation> future =
           regionDisksClient.updateOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateRegionDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateRegionDiskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
