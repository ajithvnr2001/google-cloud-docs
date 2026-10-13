---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSnapshotsClient
title: Class RegionSnapshotsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:03:57.771091+00:00
---

# Class RegionSnapshotsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSnapshotsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegionSnapshotsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RegionSnapshotsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RegionSnapshots API.

This client uses RegionSnapshots version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String snapshot = "snapshot284874180";
       Snapshot response = regionSnapshotsClient.get(project, region, snapshot);
     }
     

Note: close() needs to be called on the RegionSnapshotsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified Snapshot resource. Keep in mind that deleting a single snapshot might not necessarily delete all the data on that snapshot. If any data on the snapshot that is marked for deletion is needed for subsequent snapshots, the data will be moved to the next corresponding snapshot.  For more information, seeDeleting snapshots. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRegionSnapshotRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String region, String snapshot) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified Snapshot resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRegionSnapshotRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String region, String snapshot) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRegionSnapshotRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String region, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
Insert |  Creates a snapshot in the specified region using the data included in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRegionSnapshotRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, String region, Snapshot snapshotResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of Snapshot resources contained within the specified region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRegionSnapshotsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project, String region) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRegionSnapshotRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String region, String resource, RegionSetPolicyRequest regionSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
SetLabels |  Sets the labels on a regional snapshot. To learn more about labels, read the Labeling Resources documentation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setLabelsAsync(SetLabelsRegionSnapshotRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setLabelsAsync(String project, String region, String resource, RegionSetLabelsRequest regionSetLabelsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setLabelsOperationCallable() 
  * setLabelsCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRegionSnapshotRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String region, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
UpdateKmsKey |  Rotates the customer-managed encryption key to the latest version for the specified snapshot. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateKmsKeyAsync(UpdateKmsKeyRegionSnapshotRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateKmsKeyAsync(String project, String region, String snapshot, RegionSnapshotUpdateKmsKeyRequest regionSnapshotUpdateKmsKeyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateKmsKeyOperationCallable() 
  * updateKmsKeyCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RegionSnapshotsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionSnapshotsSettings regionSnapshotsSettings =
         RegionSnapshotsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RegionSnapshotsClient regionSnapshotsClient =
         RegionSnapshotsClient.create(regionSnapshotsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegionSnapshotsSettings regionSnapshotsSettings =
         RegionSnapshotsSettings.newBuilder().setEndpoint(myEndpoint).build();
     RegionSnapshotsClient regionSnapshotsClient =
         RegionSnapshotsClient.create(regionSnapshotsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RegionSnapshotsClient

## Static Methods 

### create()
    
    
    public static final RegionSnapshotsClient create()

Constructs an instance of RegionSnapshotsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RegionSnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSnapshotsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionSnapshotsSettings settings)
    
    
    public static final RegionSnapshotsClient create(RegionSnapshotsSettings settings)

Constructs an instance of RegionSnapshotsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionSnapshotsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSnapshotsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionSnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSnapshotsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RegionSnapshotsStub stub)
    
    
    public static final RegionSnapshotsClient create(RegionSnapshotsStub stub)

Constructs an instance of RegionSnapshotsClient, using the given stub for making calls. This is for advanced usage - prefer using create(RegionSnapshotsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionSnapshotsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionSnapshotsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegionSnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSnapshotsClient)` |   
  
## Constructors 

### RegionSnapshotsClient(RegionSnapshotsSettings settings)
    
    
    protected RegionSnapshotsClient(RegionSnapshotsSettings settings)

Constructs an instance of RegionSnapshotsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RegionSnapshotsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSnapshotsSettings)`  
  
  
### RegionSnapshotsClient(RegionSnapshotsStub stub)
    
    
    protected RegionSnapshotsClient(RegionSnapshotsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RegionSnapshotsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionSnapshotsStub)`  
  
  
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

### deleteAsync(DeleteRegionSnapshotRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRegionSnapshotRequest request)

Deletes the specified Snapshot resource. Keep in mind that deleting a single snapshot might not necessarily delete all the data on that snapshot. If any data on the snapshot that is marked for deletion is needed for subsequent snapshots, the data will be moved to the next corresponding snapshot.

For more information, seeDeleting snapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       DeleteRegionSnapshotRequest request =
           DeleteRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSnapshot("snapshot284874180")
               .build();
       Operation response = regionSnapshotsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String region, String snapshot)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String region, String snapshot)

Deletes the specified Snapshot resource. Keep in mind that deleting a single snapshot might not necessarily delete all the data on that snapshot. If any data on the snapshot that is marked for deletion is needed for subsequent snapshots, the data will be moved to the next corresponding snapshot.

For more information, seeDeleting snapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String snapshot = "snapshot284874180";
       Operation response = regionSnapshotsClient.deleteAsync(project, region, snapshot).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the region for this request.  
`snapshot` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the snapshot resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRegionSnapshotRequest,Operation> deleteCallable()

Deletes the specified Snapshot resource. Keep in mind that deleting a single snapshot might not necessarily delete all the data on that snapshot. If any data on the snapshot that is marked for deletion is needed for subsequent snapshots, the data will be moved to the next corresponding snapshot.

For more information, seeDeleting snapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       DeleteRegionSnapshotRequest request =
           DeleteRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSnapshot("snapshot284874180")
               .build();
       ApiFuture<Operation> future = regionSnapshotsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRegionSnapshotRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified Snapshot resource. Keep in mind that deleting a single snapshot might not necessarily delete all the data on that snapshot. If any data on the snapshot that is marked for deletion is needed for subsequent snapshots, the data will be moved to the next corresponding snapshot.

For more information, seeDeleting snapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       DeleteRegionSnapshotRequest request =
           DeleteRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSnapshot("snapshot284874180")
               .build();
       OperationFuture<Operation, Operation> future =
           regionSnapshotsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRegionSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRegionSnapshotRequest request)
    
    
    public final Snapshot get(GetRegionSnapshotRequest request)

Returns the specified Snapshot resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       GetRegionSnapshotRequest request =
           GetRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setSnapshot("snapshot284874180")
               .build();
       Snapshot response = regionSnapshotsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot)` |   
  
### get(String project, String region, String snapshot)
    
    
    public final Snapshot get(String project, String region, String snapshot)

Returns the specified Snapshot resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String snapshot = "snapshot284874180";
       Snapshot response = regionSnapshotsClient.get(project, region, snapshot);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`snapshot` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Snapshot resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRegionSnapshotRequest,Snapshot> getCallable()

Returns the specified Snapshot resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       GetRegionSnapshotRequest request =
           GetRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setSnapshot("snapshot284874180")
               .build();
       ApiFuture<Snapshot> future = regionSnapshotsClient.getCallable().futureCall(request);
       // Do something.
       Snapshot response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRegionSnapshotRequest),[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot)>` |   
  
### getIamPolicy(GetIamPolicyRegionSnapshotRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRegionSnapshotRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       GetIamPolicyRegionSnapshotRequest request =
           GetIamPolicyRegionSnapshotRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .build();
       Policy response = regionSnapshotsClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyRegionSnapshotRequest)`  
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
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       Policy response = regionSnapshotsClient.getIamPolicy(project, region, resource);
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
    
    
    public final UnaryCallable<GetIamPolicyRegionSnapshotRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       GetIamPolicyRegionSnapshotRequest request =
           GetIamPolicyRegionSnapshotRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = regionSnapshotsClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicyRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicyRegionSnapshotRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getSettings()
    
    
    public final @Nullable RegionSnapshotsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RegionSnapshotsSettings` |   
  
### getStub()
    
    
    public RegionSnapshotsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RegionSnapshotsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RegionSnapshotsStub)` |   
  
### insertAsync(InsertRegionSnapshotRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRegionSnapshotRequest request)

Creates a snapshot in the specified region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       InsertRegionSnapshotRequest request =
           InsertRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSnapshotResource(Snapshot.newBuilder().build())
               .build();
       Operation response = regionSnapshotsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, String region, Snapshot snapshotResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, String region, Snapshot snapshotResource)

Creates a snapshot in the specified region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       Snapshot snapshotResource = Snapshot.newBuilder().build();
       Operation response =
           regionSnapshotsClient.insertAsync(project, region, snapshotResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`snapshotResource` | `[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRegionSnapshotRequest,Operation> insertCallable()

Creates a snapshot in the specified region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       InsertRegionSnapshotRequest request =
           InsertRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSnapshotResource(Snapshot.newBuilder().build())
               .build();
       ApiFuture<Operation> future = regionSnapshotsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRegionSnapshotRequest,Operation,Operation> insertOperationCallable()

Creates a snapshot in the specified region using the data included in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       InsertRegionSnapshotRequest request =
           InsertRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRequestId("requestId693933066")
               .setSnapshotResource(Snapshot.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           regionSnapshotsClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRegionSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRegionSnapshotsRequest request)
    
    
    public final RegionSnapshotsClient.ListPagedResponse list(ListRegionSnapshotsRequest request)

Retrieves the list of Snapshot resources contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       ListRegionSnapshotsRequest request =
           ListRegionSnapshotsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       for (Snapshot element : regionSnapshotsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRegionSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionSnapshotsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RegionSnapshotsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSnapshotsClient.ListPagedResponse)` |   
  
### list(String project, String region)
    
    
    public final RegionSnapshotsClient.ListPagedResponse list(String project, String region)

Retrieves the list of Snapshot resources contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       for (Snapshot element : regionSnapshotsClient.list(project, region).iterateAll()) {
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
`[RegionSnapshotsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSnapshotsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRegionSnapshotsRequest,SnapshotList> listCallable()

Retrieves the list of Snapshot resources contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       ListRegionSnapshotsRequest request =
           ListRegionSnapshotsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       while (true) {
         SnapshotList response = regionSnapshotsClient.listCallable().call(request);
         for (Snapshot element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionSnapshotsRequest),[SnapshotList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRegionSnapshotsRequest,RegionSnapshotsClient.ListPagedResponse> listPagedCallable()

Retrieves the list of Snapshot resources contained within the specified region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       ListRegionSnapshotsRequest request =
           ListRegionSnapshotsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .build();
       ApiFuture<Snapshot> future = regionSnapshotsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (Snapshot element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRegionSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRegionSnapshotsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSnapshotsClient.ListPagedResponse)>` |   
  
### setIamPolicy(SetIamPolicyRegionSnapshotRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRegionSnapshotRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       SetIamPolicyRegionSnapshotRequest request =
           SetIamPolicyRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetPolicyRequestResource(RegionSetPolicyRequest.newBuilder().build())
               .setResource("resource-341064690")
               .build();
       Policy response = regionSnapshotsClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyRegionSnapshotRequest)`  
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
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       RegionSetPolicyRequest regionSetPolicyRequestResource =
           RegionSetPolicyRequest.newBuilder().build();
       Policy response =
           regionSnapshotsClient.setIamPolicy(
               project, region, resource, regionSetPolicyRequestResource);
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
    
    
    public final UnaryCallable<SetIamPolicyRegionSnapshotRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       SetIamPolicyRegionSnapshotRequest request =
           SetIamPolicyRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetPolicyRequestResource(RegionSetPolicyRequest.newBuilder().build())
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = regionSnapshotsClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicyRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicyRegionSnapshotRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### setLabelsAsync(SetLabelsRegionSnapshotRequest request)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(SetLabelsRegionSnapshotRequest request)

Sets the labels on a regional snapshot. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       SetLabelsRegionSnapshotRequest request =
           SetLabelsRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetLabelsRequestResource(RegionSetLabelsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .build();
       Operation response = regionSnapshotsClient.setLabelsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetLabelsRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsRegionSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsAsync(String project, String region, String resource, RegionSetLabelsRequest regionSetLabelsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(String project, String region, String resource, RegionSetLabelsRequest regionSetLabelsRequestResource)

Sets the labels on a regional snapshot. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       RegionSetLabelsRequest regionSetLabelsRequestResource =
           RegionSetLabelsRequest.newBuilder().build();
       Operation response =
           regionSnapshotsClient
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
    
    
    public final UnaryCallable<SetLabelsRegionSnapshotRequest,Operation> setLabelsCallable()

Sets the labels on a regional snapshot. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       SetLabelsRegionSnapshotRequest request =
           SetLabelsRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetLabelsRequestResource(RegionSetLabelsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Operation> future = regionSnapshotsClient.setLabelsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLabelsRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsRegionSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsOperationCallable()
    
    
    public final OperationCallable<SetLabelsRegionSnapshotRequest,Operation,Operation> setLabelsOperationCallable()

Sets the labels on a regional snapshot. To learn more about labels, read the Labeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       SetLabelsRegionSnapshotRequest request =
           SetLabelsRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSetLabelsRequestResource(RegionSetLabelsRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setResource("resource-341064690")
               .build();
       OperationFuture<Operation, Operation> future =
           regionSnapshotsClient.setLabelsOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetLabelsRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsRegionSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRegionSnapshotRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsRegionSnapshotRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       TestIamPermissionsRegionSnapshotRequest request =
           TestIamPermissionsRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = regionSnapshotsClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionSnapshotRequest)`  
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
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           regionSnapshotsClient.testIamPermissions(
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
    
    
    public final UnaryCallable<TestIamPermissionsRegionSnapshotRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       TestIamPermissionsRegionSnapshotRequest request =
           TestIamPermissionsRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           regionSnapshotsClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsRegionSnapshotRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
### updateKmsKeyAsync(UpdateKmsKeyRegionSnapshotRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateKmsKeyAsync(UpdateKmsKeyRegionSnapshotRequest request)

Rotates the customer-managed encryption key to the latest version for the specified snapshot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       UpdateKmsKeyRegionSnapshotRequest request =
           UpdateKmsKeyRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSnapshotUpdateKmsKeyRequestResource(
                   RegionSnapshotUpdateKmsKeyRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setSnapshot("snapshot284874180")
               .build();
       Operation response = regionSnapshotsClient.updateKmsKeyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateKmsKeyRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateKmsKeyRegionSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateKmsKeyAsync(String project, String region, String snapshot, RegionSnapshotUpdateKmsKeyRequest regionSnapshotUpdateKmsKeyRequestResource)
    
    
    public final OperationFuture<Operation,Operation> updateKmsKeyAsync(String project, String region, String snapshot, RegionSnapshotUpdateKmsKeyRequest regionSnapshotUpdateKmsKeyRequestResource)

Rotates the customer-managed encryption key to the latest version for the specified snapshot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       String project = "project-309310695";
       String region = "region-934795532";
       String snapshot = "snapshot284874180";
       RegionSnapshotUpdateKmsKeyRequest regionSnapshotUpdateKmsKeyRequestResource =
           RegionSnapshotUpdateKmsKeyRequest.newBuilder().build();
       Operation response =
           regionSnapshotsClient
               .updateKmsKeyAsync(
                   project, region, snapshot, regionSnapshotUpdateKmsKeyRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`region` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the region for this request.  
`snapshot` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the snapshot resource to update. Should conform to RFC1035.  
`regionSnapshotUpdateKmsKeyRequestResource` | `[RegionSnapshotUpdateKmsKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionSnapshotUpdateKmsKeyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateKmsKeyCallable()
    
    
    public final UnaryCallable<UpdateKmsKeyRegionSnapshotRequest,Operation> updateKmsKeyCallable()

Rotates the customer-managed encryption key to the latest version for the specified snapshot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       UpdateKmsKeyRegionSnapshotRequest request =
           UpdateKmsKeyRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSnapshotUpdateKmsKeyRequestResource(
                   RegionSnapshotUpdateKmsKeyRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setSnapshot("snapshot284874180")
               .build();
       ApiFuture<Operation> future =
           regionSnapshotsClient.updateKmsKeyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateKmsKeyRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateKmsKeyRegionSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateKmsKeyOperationCallable()
    
    
    public final OperationCallable<UpdateKmsKeyRegionSnapshotRequest,Operation,Operation> updateKmsKeyOperationCallable()

Rotates the customer-managed encryption key to the latest version for the specified snapshot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RegionSnapshotsClient regionSnapshotsClient = RegionSnapshotsClient.create()) {
       UpdateKmsKeyRegionSnapshotRequest request =
           UpdateKmsKeyRegionSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRegion("region-934795532")
               .setRegionSnapshotUpdateKmsKeyRequestResource(
                   RegionSnapshotUpdateKmsKeyRequest.newBuilder().build())
               .setRequestId("requestId693933066")
               .setSnapshot("snapshot284874180")
               .build();
       OperationFuture<Operation, Operation> future =
           regionSnapshotsClient.updateKmsKeyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateKmsKeyRegionSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateKmsKeyRegionSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
