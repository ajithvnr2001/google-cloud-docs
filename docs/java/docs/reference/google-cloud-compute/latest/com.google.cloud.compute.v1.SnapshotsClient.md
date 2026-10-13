---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient
title: Class SnapshotsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:24.803569+00:00
---

# Class SnapshotsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SnapshotsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/SnapshotsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The Snapshots API.

This client uses Snapshots version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       String project = "project-309310695";
       String snapshot = "snapshot284874180";
       Snapshot response = snapshotsClient.get(project, snapshot);
     }
     

Note: close() needs to be called on the SnapshotsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes the specified Snapshot resource. Keep in mind that deleting a single snapshot might not necessarily delete all the data on that snapshot. If any data on the snapshot that is marked for deletion is needed for subsequent snapshots, the data will be moved to the next corresponding snapshot.  For more information, seeDeleting snapshots. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteSnapshotRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String snapshot) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Returns the specified Snapshot resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetSnapshotRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String snapshot) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. May be empty if no such policy or resource exists. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicySnapshotRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIamPolicy(String project, String resource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
Insert |  Creates a snapshot in the specified project using the data included in the request. For regular snapshot creation, consider using this method instead of disks.createSnapshot, as this method supports more features, such as creating snapshots in a project different from the source disk project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertSnapshotRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, Snapshot snapshotResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Retrieves the list of Snapshot resources contained within the specified project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListSnapshotsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replaces any existing policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicySnapshotRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
SetLabels |  Sets the labels on a snapshot. To learn more about labels, read theLabeling Resources documentation. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setLabelsAsync(SetLabelsSnapshotRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * setLabelsAsync(String project, String resource, GlobalSetLabelsRequest globalSetLabelsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setLabelsOperationCallable() 
  * setLabelsCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsSnapshotRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
UpdateKmsKey |  Rotates the customer-managed encryption key to the latest version for the specified snapshot. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateKmsKeyAsync(UpdateKmsKeySnapshotRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateKmsKeyAsync(String project, String snapshot, SnapshotUpdateKmsKeyRequest snapshotUpdateKmsKeyRequestResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateKmsKeyOperationCallable() 
  * updateKmsKeyCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of SnapshotsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SnapshotsSettings snapshotsSettings =
         SnapshotsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SnapshotsClient snapshotsClient = SnapshotsClient.create(snapshotsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SnapshotsSettings snapshotsSettings =
         SnapshotsSettings.newBuilder().setEndpoint(myEndpoint).build();
     SnapshotsClient snapshotsClient = SnapshotsClient.create(snapshotsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SnapshotsClient

## Static Methods 

### create()
    
    
    public static final SnapshotsClient create()

Constructs an instance of SnapshotsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SnapshotsSettings settings)
    
    
    public static final SnapshotsClient create(SnapshotsSettings settings)

Constructs an instance of SnapshotsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SnapshotsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SnapshotsStub stub)
    
    
    public static final SnapshotsClient create(SnapshotsStub stub)

Constructs an instance of SnapshotsClient, using the given stub for making calls. This is for advanced usage - prefer using create(SnapshotsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SnapshotsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.SnapshotsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient)` |   
  
## Constructors 

### SnapshotsClient(SnapshotsSettings settings)
    
    
    protected SnapshotsClient(SnapshotsSettings settings)

Constructs an instance of SnapshotsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SnapshotsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsSettings)`  
  
  
### SnapshotsClient(SnapshotsStub stub)
    
    
    protected SnapshotsClient(SnapshotsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SnapshotsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.SnapshotsStub)`  
  
  
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

### deleteAsync(DeleteSnapshotRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteSnapshotRequest request)

Deletes the specified Snapshot resource. Keep in mind that deleting a single snapshot might not necessarily delete all the data on that snapshot. If any data on the snapshot that is marked for deletion is needed for subsequent snapshots, the data will be moved to the next corresponding snapshot.

For more information, seeDeleting snapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       DeleteSnapshotRequest request =
           DeleteSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSnapshot("snapshot284874180")
               .build();
       Operation response = snapshotsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String snapshot)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String snapshot)

Deletes the specified Snapshot resource. Keep in mind that deleting a single snapshot might not necessarily delete all the data on that snapshot. If any data on the snapshot that is marked for deletion is needed for subsequent snapshots, the data will be moved to the next corresponding snapshot.

For more information, seeDeleting snapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       String project = "project-309310695";
       String snapshot = "snapshot284874180";
       Operation response = snapshotsClient.deleteAsync(project, snapshot).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`snapshot` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Snapshot resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteSnapshotRequest,Operation> deleteCallable()

Deletes the specified Snapshot resource. Keep in mind that deleting a single snapshot might not necessarily delete all the data on that snapshot. If any data on the snapshot that is marked for deletion is needed for subsequent snapshots, the data will be moved to the next corresponding snapshot.

For more information, seeDeleting snapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       DeleteSnapshotRequest request =
           DeleteSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSnapshot("snapshot284874180")
               .build();
       ApiFuture<Operation> future = snapshotsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteSnapshotRequest,Operation,Operation> deleteOperationCallable()

Deletes the specified Snapshot resource. Keep in mind that deleting a single snapshot might not necessarily delete all the data on that snapshot. If any data on the snapshot that is marked for deletion is needed for subsequent snapshots, the data will be moved to the next corresponding snapshot.

For more information, seeDeleting snapshots.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       DeleteSnapshotRequest request =
           DeleteSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSnapshot("snapshot284874180")
               .build();
       OperationFuture<Operation, Operation> future =
           snapshotsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetSnapshotRequest request)
    
    
    public final Snapshot get(GetSnapshotRequest request)

Returns the specified Snapshot resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       GetSnapshotRequest request =
           GetSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setSnapshot("snapshot284874180")
               .build();
       Snapshot response = snapshotsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot)` |   
  
### get(String project, String snapshot)
    
    
    public final Snapshot get(String project, String snapshot)

Returns the specified Snapshot resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       String project = "project-309310695";
       String snapshot = "snapshot284874180";
       Snapshot response = snapshotsClient.get(project, snapshot);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`snapshot` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Snapshot resource to return.  
**Returns**  
---  
**Type** | **Description**  
`[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetSnapshotRequest,Snapshot> getCallable()

Returns the specified Snapshot resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       GetSnapshotRequest request =
           GetSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setSnapshot("snapshot284874180")
               .build();
       ApiFuture<Snapshot> future = snapshotsClient.getCallable().futureCall(request);
       // Do something.
       Snapshot response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetSnapshotRequest),[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot)>` |   
  
### getIamPolicy(GetIamPolicySnapshotRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicySnapshotRequest request)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       GetIamPolicySnapshotRequest request =
           GetIamPolicySnapshotRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Policy response = snapshotsClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicySnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicySnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicy(String project, String resource)
    
    
    public final Policy getIamPolicy(String project, String resource)

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       Policy response = snapshotsClient.getIamPolicy(project, resource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicySnapshotRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       GetIamPolicySnapshotRequest request =
           GetIamPolicySnapshotRequest.newBuilder()
               .setOptionsRequestedPolicyVersion(-574521795)
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = snapshotsClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIamPolicySnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetIamPolicySnapshotRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### getSettings()
    
    
    public final @Nullable SnapshotsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.SnapshotsSettings` |   
  
### getStub()
    
    
    public SnapshotsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SnapshotsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.SnapshotsStub)` |   
  
### insertAsync(InsertSnapshotRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertSnapshotRequest request)

Creates a snapshot in the specified project using the data included in the request. For regular snapshot creation, consider using this method instead of disks.createSnapshot, as this method supports more features, such as creating snapshots in a project different from the source disk project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       InsertSnapshotRequest request =
           InsertSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSnapshotResource(Snapshot.newBuilder().build())
               .build();
       Operation response = snapshotsClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, Snapshot snapshotResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, Snapshot snapshotResource)

Creates a snapshot in the specified project using the data included in the request. For regular snapshot creation, consider using this method instead of disks.createSnapshot, as this method supports more features, such as creating snapshots in a project different from the source disk project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       String project = "project-309310695";
       Snapshot snapshotResource = Snapshot.newBuilder().build();
       Operation response = snapshotsClient.insertAsync(project, snapshotResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`snapshotResource` | `[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertSnapshotRequest,Operation> insertCallable()

Creates a snapshot in the specified project using the data included in the request. For regular snapshot creation, consider using this method instead of disks.createSnapshot, as this method supports more features, such as creating snapshots in a project different from the source disk project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       InsertSnapshotRequest request =
           InsertSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSnapshotResource(Snapshot.newBuilder().build())
               .build();
       ApiFuture<Operation> future = snapshotsClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertSnapshotRequest,Operation,Operation> insertOperationCallable()

Creates a snapshot in the specified project using the data included in the request. For regular snapshot creation, consider using this method instead of disks.createSnapshot, as this method supports more features, such as creating snapshots in a project different from the source disk project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       InsertSnapshotRequest request =
           InsertSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSnapshotResource(Snapshot.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           snapshotsClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListSnapshotsRequest request)
    
    
    public final SnapshotsClient.ListPagedResponse list(ListSnapshotsRequest request)

Retrieves the list of Snapshot resources contained within the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       ListSnapshotsRequest request =
           ListSnapshotsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (Snapshot element : snapshotsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListSnapshotsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SnapshotsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final SnapshotsClient.ListPagedResponse list(String project)

Retrieves the list of Snapshot resources contained within the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       String project = "project-309310695";
       for (Snapshot element : snapshotsClient.list(project).iterateAll()) {
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
`[SnapshotsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListSnapshotsRequest,SnapshotList> listCallable()

Retrieves the list of Snapshot resources contained within the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       ListSnapshotsRequest request =
           ListSnapshotsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         SnapshotList response = snapshotsClient.listCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListSnapshotsRequest),[SnapshotList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotList)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListSnapshotsRequest,SnapshotsClient.ListPagedResponse> listPagedCallable()

Retrieves the list of Snapshot resources contained within the specified project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       ListSnapshotsRequest request =
           ListSnapshotsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<Snapshot> future = snapshotsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (Snapshot element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSnapshotsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListSnapshotsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.ListPagedResponse)>` |   
  
### setIamPolicy(SetIamPolicySnapshotRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicySnapshotRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       SetIamPolicySnapshotRequest request =
           SetIamPolicySnapshotRequest.newBuilder()
               .setGlobalSetPolicyRequestResource(GlobalSetPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Policy response = snapshotsClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicySnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicySnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource)
    
    
    public final Policy setIamPolicy(String project, String resource, GlobalSetPolicyRequest globalSetPolicyRequestResource)

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       GlobalSetPolicyRequest globalSetPolicyRequestResource =
           GlobalSetPolicyRequest.newBuilder().build();
       Policy response =
           snapshotsClient.setIamPolicy(project, resource, globalSetPolicyRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`globalSetPolicyRequestResource` | `[GlobalSetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalSetPolicyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicySnapshotRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replaces any existing policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       SetIamPolicySnapshotRequest request =
           SetIamPolicySnapshotRequest.newBuilder()
               .setGlobalSetPolicyRequestResource(GlobalSetPolicyRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Policy> future = snapshotsClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetIamPolicySnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetIamPolicySnapshotRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy)>` |   
  
### setLabelsAsync(SetLabelsSnapshotRequest request)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(SetLabelsSnapshotRequest request)

Sets the labels on a snapshot. To learn more about labels, read theLabeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       SetLabelsSnapshotRequest request =
           SetLabelsSnapshotRequest.newBuilder()
               .setGlobalSetLabelsRequestResource(GlobalSetLabelsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       Operation response = snapshotsClient.setLabelsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetLabelsSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsAsync(String project, String resource, GlobalSetLabelsRequest globalSetLabelsRequestResource)
    
    
    public final OperationFuture<Operation,Operation> setLabelsAsync(String project, String resource, GlobalSetLabelsRequest globalSetLabelsRequestResource)

Sets the labels on a snapshot. To learn more about labels, read theLabeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       GlobalSetLabelsRequest globalSetLabelsRequestResource =
           GlobalSetLabelsRequest.newBuilder().build();
       Operation response =
           snapshotsClient.setLabelsAsync(project, resource, globalSetLabelsRequestResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`globalSetLabelsRequestResource` | `[GlobalSetLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GlobalSetLabelsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsCallable()
    
    
    public final UnaryCallable<SetLabelsSnapshotRequest,Operation> setLabelsCallable()

Sets the labels on a snapshot. To learn more about labels, read theLabeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       SetLabelsSnapshotRequest request =
           SetLabelsSnapshotRequest.newBuilder()
               .setGlobalSetLabelsRequestResource(GlobalSetLabelsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       ApiFuture<Operation> future = snapshotsClient.setLabelsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetLabelsSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### setLabelsOperationCallable()
    
    
    public final OperationCallable<SetLabelsSnapshotRequest,Operation,Operation> setLabelsOperationCallable()

Sets the labels on a snapshot. To learn more about labels, read theLabeling Resources documentation.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       SetLabelsSnapshotRequest request =
           SetLabelsSnapshotRequest.newBuilder()
               .setGlobalSetLabelsRequestResource(GlobalSetLabelsRequest.newBuilder().build())
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .build();
       OperationFuture<Operation, Operation> future =
           snapshotsClient.setLabelsOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[SetLabelsSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetLabelsSnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsSnapshotRequest request)
    
    
    public final TestPermissionsResponse testIamPermissions(TestIamPermissionsSnapshotRequest request)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       TestIamPermissionsSnapshotRequest request =
           TestIamPermissionsSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       TestPermissionsResponse response = snapshotsClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsSnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource)
    
    
    public final TestPermissionsResponse testIamPermissions(String project, String resource, TestPermissionsRequest testPermissionsRequestResource)

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       String project = "project-309310695";
       String resource = "resource-341064690";
       TestPermissionsRequest testPermissionsRequestResource =
           TestPermissionsRequest.newBuilder().build();
       TestPermissionsResponse response =
           snapshotsClient.testIamPermissions(project, resource, testPermissionsRequestResource);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`resource` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name or id of the resource for this request.  
`testPermissionsRequestResource` | `[TestPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsSnapshotRequest,TestPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       TestIamPermissionsSnapshotRequest request =
           TestIamPermissionsSnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setResource("resource-341064690")
               .setTestPermissionsRequestResource(TestPermissionsRequest.newBuilder().build())
               .build();
       ApiFuture<TestPermissionsResponse> future =
           snapshotsClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[TestIamPermissionsSnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestIamPermissionsSnapshotRequest),[TestPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.TestPermissionsResponse)>` |   
  
### updateKmsKeyAsync(UpdateKmsKeySnapshotRequest request)
    
    
    public final OperationFuture<Operation,Operation> updateKmsKeyAsync(UpdateKmsKeySnapshotRequest request)

Rotates the customer-managed encryption key to the latest version for the specified snapshot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       UpdateKmsKeySnapshotRequest request =
           UpdateKmsKeySnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSnapshot("snapshot284874180")
               .setSnapshotUpdateKmsKeyRequestResource(
                   SnapshotUpdateKmsKeyRequest.newBuilder().build())
               .build();
       Operation response = snapshotsClient.updateKmsKeyAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateKmsKeySnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateKmsKeySnapshotRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateKmsKeyAsync(String project, String snapshot, SnapshotUpdateKmsKeyRequest snapshotUpdateKmsKeyRequestResource)
    
    
    public final OperationFuture<Operation,Operation> updateKmsKeyAsync(String project, String snapshot, SnapshotUpdateKmsKeyRequest snapshotUpdateKmsKeyRequestResource)

Rotates the customer-managed encryption key to the latest version for the specified snapshot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       String project = "project-309310695";
       String snapshot = "snapshot284874180";
       SnapshotUpdateKmsKeyRequest snapshotUpdateKmsKeyRequestResource =
           SnapshotUpdateKmsKeyRequest.newBuilder().build();
       Operation response =
           snapshotsClient
               .updateKmsKeyAsync(project, snapshot, snapshotUpdateKmsKeyRequestResource)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`snapshot` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the snapshot resource to update. Should conform to RFC1035.  
`snapshotUpdateKmsKeyRequestResource` | `[SnapshotUpdateKmsKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotUpdateKmsKeyRequest)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateKmsKeyCallable()
    
    
    public final UnaryCallable<UpdateKmsKeySnapshotRequest,Operation> updateKmsKeyCallable()

Rotates the customer-managed encryption key to the latest version for the specified snapshot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       UpdateKmsKeySnapshotRequest request =
           UpdateKmsKeySnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSnapshot("snapshot284874180")
               .setSnapshotUpdateKmsKeyRequestResource(
                   SnapshotUpdateKmsKeyRequest.newBuilder().build())
               .build();
       ApiFuture<Operation> future = snapshotsClient.updateKmsKeyCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateKmsKeySnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateKmsKeySnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### updateKmsKeyOperationCallable()
    
    
    public final OperationCallable<UpdateKmsKeySnapshotRequest,Operation,Operation> updateKmsKeyOperationCallable()

Rotates the customer-managed encryption key to the latest version for the specified snapshot.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SnapshotsClient snapshotsClient = SnapshotsClient.create()) {
       UpdateKmsKeySnapshotRequest request =
           UpdateKmsKeySnapshotRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setSnapshot("snapshot284874180")
               .setSnapshotUpdateKmsKeyRequestResource(
                   SnapshotUpdateKmsKeyRequest.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           snapshotsClient.updateKmsKeyOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateKmsKeySnapshotRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpdateKmsKeySnapshotRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
