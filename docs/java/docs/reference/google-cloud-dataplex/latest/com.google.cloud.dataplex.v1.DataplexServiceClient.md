---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient
title: Class DataplexServiceClient (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:32:15.649663+00:00
---

# Class DataplexServiceClient (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataplexServiceClient (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.1  0.2.2 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-dataplex/google-cloud-dataplex/src/main/java/com/google/cloud/dataplex/v1/DataplexServiceClient.java)| [Product Reference](https://cloud.google.com/dataplex)| [REST Documentation](https://cloud.google.com/dataplex/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/dataplex/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Dataplex service provides data lakes as a service. The primary resources offered by this service are Lakes, Zones and Assets which collectively allow a data administrator to organize, manage, secure and catalog data across their organization located across cloud projects in a variety of storage systems including Cloud Storage and BigQuery.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       LakeName name = LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]");
       Lake response = dataplexServiceClient.getLake(name);
     }
     

Note: close() needs to be called on the DataplexServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateLake |  Creates a lake resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createLakeAsync(CreateLakeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createLakeAsync(LocationName parent, Lake lake, String lakeId) 
  * createLakeAsync(String parent, Lake lake, String lakeId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createLakeOperationCallable() 
  * createLakeCallable() 

  
UpdateLake |  Updates a lake resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateLakeAsync(UpdateLakeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateLakeAsync(Lake lake, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateLakeOperationCallable() 
  * updateLakeCallable() 

  
DeleteLake |  Deletes a lake resource. All zones within the lake must be deleted before the lake can be deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteLakeAsync(DeleteLakeRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteLakeAsync(LakeName name) 
  * deleteLakeAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteLakeOperationCallable() 
  * deleteLakeCallable() 

  
ListLakes |  Lists lake resources in a project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLakes(ListLakesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLakes(LocationName parent) 
  * listLakes(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLakesPagedCallable() 
  * listLakesCallable() 

  
GetLake |  Retrieves a lake resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLake(GetLakeRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getLake(LakeName name) 
  * getLake(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLakeCallable() 

  
ListLakeActions |  Lists action resources in a lake. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLakeActions(ListLakeActionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listLakeActions(LakeName parent) 
  * listLakeActions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLakeActionsPagedCallable() 
  * listLakeActionsCallable() 

  
CreateZone |  Creates a zone resource within a lake. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createZoneAsync(CreateZoneRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createZoneAsync(LakeName parent, Zone zone, String zoneId) 
  * createZoneAsync(String parent, Zone zone, String zoneId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createZoneOperationCallable() 
  * createZoneCallable() 

  
UpdateZone |  Updates a zone resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateZoneAsync(UpdateZoneRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateZoneAsync(Zone zone, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateZoneOperationCallable() 
  * updateZoneCallable() 

  
DeleteZone |  Deletes a zone resource. All assets within a zone must be deleted before the zone can be deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteZoneAsync(DeleteZoneRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteZoneAsync(ZoneName name) 
  * deleteZoneAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteZoneOperationCallable() 
  * deleteZoneCallable() 

  
ListZones |  Lists zone resources in a lake. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listZones(ListZonesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listZones(LakeName parent) 
  * listZones(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listZonesPagedCallable() 
  * listZonesCallable() 

  
GetZone |  Retrieves a zone resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getZone(GetZoneRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getZone(ZoneName name) 
  * getZone(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getZoneCallable() 

  
ListZoneActions |  Lists action resources in a zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listZoneActions(ListZoneActionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listZoneActions(ZoneName parent) 
  * listZoneActions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listZoneActionsPagedCallable() 
  * listZoneActionsCallable() 

  
CreateAsset |  Creates an asset resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createAssetAsync(CreateAssetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createAssetAsync(ZoneName parent, Asset asset, String assetId) 
  * createAssetAsync(String parent, Asset asset, String assetId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createAssetOperationCallable() 
  * createAssetCallable() 

  
UpdateAsset |  Updates an asset resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAssetAsync(UpdateAssetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateAssetAsync(Asset asset, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAssetOperationCallable() 
  * updateAssetCallable() 

  
DeleteAsset |  Deletes an asset resource. The referenced storage resource is detached (default) or deleted based on the associated Lifecycle policy. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAssetAsync(DeleteAssetRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAssetAsync(AssetName name) 
  * deleteAssetAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteAssetOperationCallable() 
  * deleteAssetCallable() 

  
ListAssets |  Lists asset resources in a zone. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAssets(ListAssetsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAssets(ZoneName parent) 
  * listAssets(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAssetsPagedCallable() 
  * listAssetsCallable() 

  
GetAsset |  Retrieves an asset resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAsset(GetAssetRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAsset(AssetName name) 
  * getAsset(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAssetCallable() 

  
ListAssetActions |  Lists action resources in an asset. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listAssetActions(ListAssetActionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listAssetActions(AssetName parent) 
  * listAssetActions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listAssetActionsPagedCallable() 
  * listAssetActionsCallable() 

  
CreateTask |  Creates a task resource within a lake. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTaskAsync(CreateTaskRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createTaskAsync(LakeName parent, Task task, String taskId) 
  * createTaskAsync(String parent, Task task, String taskId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTaskOperationCallable() 
  * createTaskCallable() 

  
UpdateTask |  Update the task resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateTaskAsync(UpdateTaskRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateTaskAsync(Task task, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateTaskOperationCallable() 
  * updateTaskCallable() 

  
DeleteTask |  Delete the task resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTaskAsync(DeleteTaskRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteTaskAsync(TaskName name) 
  * deleteTaskAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTaskOperationCallable() 
  * deleteTaskCallable() 

  
ListTasks |  Lists tasks under the given lake. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTasks(ListTasksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTasks(LakeName parent) 
  * listTasks(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTasksPagedCallable() 
  * listTasksCallable() 

  
GetTask |  Get task resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTask(GetTaskRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTask(TaskName name) 
  * getTask(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTaskCallable() 

  
ListJobs |  Lists Jobs under the given task. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listJobs(ListJobsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listJobs(TaskName parent) 
  * listJobs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listJobsPagedCallable() 
  * listJobsCallable() 

  
RunTask |  Run an on demand execution of a Task. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * runTask(RunTaskRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * runTask(TaskName name) 
  * runTask(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * runTaskCallable() 

  
GetJob |  Get job resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getJob(GetJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getJob(JobName name) 
  * getJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getJobCallable() 

  
CancelJob |  Cancel jobs running for the task resource. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelJob(CancelJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * cancelJob(JobName name) 
  * cancelJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelJobCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
SetIamPolicy |  Sets the access control policy on the specified resource. Replacesany existing policy.  Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setIamPolicy(SetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setIamPolicyCallable() 

  
GetIamPolicy |  Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIamPolicy(GetIamPolicyRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIamPolicyCallable() 

  
TestIamPermissions |  Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.  Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * testIamPermissions(TestIamPermissionsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * testIamPermissionsCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of DataplexServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataplexServiceSettings dataplexServiceSettings =
         DataplexServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     DataplexServiceClient dataplexServiceClient =
         DataplexServiceClient.create(dataplexServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataplexServiceSettings dataplexServiceSettings =
         DataplexServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     DataplexServiceClient dataplexServiceClient =
         DataplexServiceClient.create(dataplexServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     DataplexServiceSettings dataplexServiceSettings =
         DataplexServiceSettings.newHttpJsonBuilder().build();
     DataplexServiceClient dataplexServiceClient =
         DataplexServiceClient.create(dataplexServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataplexServiceClient

## Static Methods 

### create()
    
    
    public static final DataplexServiceClient create()

Constructs an instance of DataplexServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataplexServiceSettings settings)
    
    
    public static final DataplexServiceClient create(DataplexServiceSettings settings)

Constructs an instance of DataplexServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataplexServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(DataplexServiceStub stub)
    
    
    public static final DataplexServiceClient create(DataplexServiceStub stub)

Constructs an instance of DataplexServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(DataplexServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataplexServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.DataplexServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient)` |   
  
## Constructors 

### DataplexServiceClient(DataplexServiceSettings settings)
    
    
    protected DataplexServiceClient(DataplexServiceSettings settings)

Constructs an instance of DataplexServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[DataplexServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceSettings)`  
  
  
### DataplexServiceClient(DataplexServiceStub stub)
    
    
    protected DataplexServiceClient(DataplexServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[DataplexServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.DataplexServiceStub)`  
  
  
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
  
### cancelJob(@Nullable JobName name)
    
    
    public final void cancelJob(@Nullable JobName name)

Cancel jobs running for the task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       JobName name = JobName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]", "[JOB]");
       dataplexServiceClient.cancelJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.JobName`  
Required. The resource name of the job: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/task/{task_id}/job/{job_id}`.  
  
### cancelJob(CancelJobRequest request)
    
    
    public final void cancelJob(CancelJobRequest request)

Cancel jobs running for the task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       CancelJobRequest request =
           CancelJobRequest.newBuilder()
               .setName(
                   JobName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]", "[JOB]").toString())
               .build();
       dataplexServiceClient.cancelJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CancelJobRequest)`  
The request object containing all of the parameters for the API call.  
  
### cancelJob(String name)
    
    
    public final void cancelJob(String name)

Cancel jobs running for the task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String name = JobName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]", "[JOB]").toString();
       dataplexServiceClient.cancelJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the job: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/task/{task_id}/job/{job_id}`.  
  
### cancelJobCallable()
    
    
    public final UnaryCallable<CancelJobRequest,Empty> cancelJobCallable()

Cancel jobs running for the task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       CancelJobRequest request =
           CancelJobRequest.newBuilder()
               .setName(
                   JobName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]", "[JOB]").toString())
               .build();
       ApiFuture<Empty> future = dataplexServiceClient.cancelJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CancelJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### close()
    
    
    public final void close()

### createAssetAsync(@Nullable ZoneName parent, Asset asset, String assetId)
    
    
    public final OperationFuture<Asset,OperationMetadata> createAssetAsync(@Nullable ZoneName parent, Asset asset, String assetId)

Creates an asset resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ZoneName parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]");
       Asset asset = Asset.newBuilder().build();
       String assetId = "assetId-704776149";
       Asset response = dataplexServiceClient.createAssetAsync(parent, asset, assetId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.ZoneName`  
Required. The resource name of the parent zone: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}`.  
`asset` | `[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Asset)`  
Required. Asset resource.  
`assetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Asset identifier. This ID will be used to generate names such as table names when publishing metadata to Hive Metastore and BigQuery. 

  * Must contain only lowercase letters, numbers and hyphens. 
  * Must start with a letter. 
  * Must end with a number or a letter. 
  * Must be between 1-63 characters. 
  * Must be unique within the zone. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Asset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createAssetAsync(CreateAssetRequest request)
    
    
    public final OperationFuture<Asset,OperationMetadata> createAssetAsync(CreateAssetRequest request)

Creates an asset resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       CreateAssetRequest request =
           CreateAssetRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString())
               .setAssetId("assetId-704776149")
               .setAsset(Asset.newBuilder().build())
               .setValidateOnly(true)
               .build();
       Asset response = dataplexServiceClient.createAssetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateAssetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Asset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createAssetAsync(String parent, Asset asset, String assetId)
    
    
    public final OperationFuture<Asset,OperationMetadata> createAssetAsync(String parent, Asset asset, String assetId)

Creates an asset resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString();
       Asset asset = Asset.newBuilder().build();
       String assetId = "assetId-704776149";
       Asset response = dataplexServiceClient.createAssetAsync(parent, asset, assetId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent zone: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}`.  
`asset` | `[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Asset)`  
Required. Asset resource.  
`assetId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Asset identifier. This ID will be used to generate names such as table names when publishing metadata to Hive Metastore and BigQuery. 

  * Must contain only lowercase letters, numbers and hyphens. 
  * Must start with a letter. 
  * Must end with a number or a letter. 
  * Must be between 1-63 characters. 
  * Must be unique within the zone. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Asset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createAssetCallable()
    
    
    public final UnaryCallable<CreateAssetRequest,Operation> createAssetCallable()

Creates an asset resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       CreateAssetRequest request =
           CreateAssetRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString())
               .setAssetId("assetId-704776149")
               .setAsset(Asset.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = dataplexServiceClient.createAssetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateAssetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAssetOperationCallable()
    
    
    public final OperationCallable<CreateAssetRequest,Asset,OperationMetadata> createAssetOperationCallable()

Creates an asset resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       CreateAssetRequest request =
           CreateAssetRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString())
               .setAssetId("assetId-704776149")
               .setAsset(Asset.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<Asset, OperationMetadata> future =
           dataplexServiceClient.createAssetOperationCallable().futureCall(request);
       // Do something.
       Asset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateAssetRequest),[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Asset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createLakeAsync(@Nullable LocationName parent, Lake lake, String lakeId)
    
    
    public final OperationFuture<Lake,OperationMetadata> createLakeAsync(@Nullable LocationName parent, Lake lake, String lakeId)

Creates a lake resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Lake lake = Lake.newBuilder().build();
       String lakeId = "lakeId-1110150390";
       Lake response = dataplexServiceClient.createLakeAsync(parent, lake, lakeId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the lake location, of the form: projects/{project_number}/locations/{location_id} where `location_id` refers to a Google Cloud region.  
`lake` | `[Lake](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Lake)`  
Required. Lake resource  
`lakeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Lake identifier. This ID will be used to generate names such as database and dataset names when publishing metadata to Hive Metastore and BigQuery. 

  * Must contain only lowercase letters, numbers and hyphens. 
  * Must start with a letter. 
  * Must end with a number or a letter. 
  * Must be between 1-63 characters. 
  * Must be unique within the customer project / location. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Lake](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Lake),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createLakeAsync(CreateLakeRequest request)
    
    
    public final OperationFuture<Lake,OperationMetadata> createLakeAsync(CreateLakeRequest request)

Creates a lake resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       CreateLakeRequest request =
           CreateLakeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLakeId("lakeId-1110150390")
               .setLake(Lake.newBuilder().build())
               .setValidateOnly(true)
               .build();
       Lake response = dataplexServiceClient.createLakeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateLakeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateLakeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Lake](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Lake),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createLakeAsync(String parent, Lake lake, String lakeId)
    
    
    public final OperationFuture<Lake,OperationMetadata> createLakeAsync(String parent, Lake lake, String lakeId)

Creates a lake resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Lake lake = Lake.newBuilder().build();
       String lakeId = "lakeId-1110150390";
       Lake response = dataplexServiceClient.createLakeAsync(parent, lake, lakeId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the lake location, of the form: projects/{project_number}/locations/{location_id} where `location_id` refers to a Google Cloud region.  
`lake` | `[Lake](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Lake)`  
Required. Lake resource  
`lakeId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Lake identifier. This ID will be used to generate names such as database and dataset names when publishing metadata to Hive Metastore and BigQuery. 

  * Must contain only lowercase letters, numbers and hyphens. 
  * Must start with a letter. 
  * Must end with a number or a letter. 
  * Must be between 1-63 characters. 
  * Must be unique within the customer project / location. 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Lake](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Lake),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createLakeCallable()
    
    
    public final UnaryCallable<CreateLakeRequest,Operation> createLakeCallable()

Creates a lake resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       CreateLakeRequest request =
           CreateLakeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLakeId("lakeId-1110150390")
               .setLake(Lake.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = dataplexServiceClient.createLakeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateLakeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateLakeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createLakeOperationCallable()
    
    
    public final OperationCallable<CreateLakeRequest,Lake,OperationMetadata> createLakeOperationCallable()

Creates a lake resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       CreateLakeRequest request =
           CreateLakeRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setLakeId("lakeId-1110150390")
               .setLake(Lake.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<Lake, OperationMetadata> future =
           dataplexServiceClient.createLakeOperationCallable().futureCall(request);
       // Do something.
       Lake response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateLakeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateLakeRequest),[Lake](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Lake),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createTaskAsync(@Nullable LakeName parent, Task task, String taskId)
    
    
    public final OperationFuture<Task,OperationMetadata> createTaskAsync(@Nullable LakeName parent, Task task, String taskId)

Creates a task resource within a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       LakeName parent = LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]");
       Task task = Task.newBuilder().build();
       String taskId = "taskId-880873088";
       Task response = dataplexServiceClient.createTaskAsync(parent, task, taskId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LakeName`  
Required. The resource name of the parent lake: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`.  
`task` | `[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task)`  
Required. Task resource.  
`taskId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Task identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createTaskAsync(CreateTaskRequest request)
    
    
    public final OperationFuture<Task,OperationMetadata> createTaskAsync(CreateTaskRequest request)

Creates a task resource within a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       CreateTaskRequest request =
           CreateTaskRequest.newBuilder()
               .setParent(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .setTaskId("taskId-880873088")
               .setTask(Task.newBuilder().build())
               .setValidateOnly(true)
               .build();
       Task response = dataplexServiceClient.createTaskAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateTaskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createTaskAsync(String parent, Task task, String taskId)
    
    
    public final OperationFuture<Task,OperationMetadata> createTaskAsync(String parent, Task task, String taskId)

Creates a task resource within a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String parent = LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString();
       Task task = Task.newBuilder().build();
       String taskId = "taskId-880873088";
       Task response = dataplexServiceClient.createTaskAsync(parent, task, taskId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent lake: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`.  
`task` | `[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task)`  
Required. Task resource.  
`taskId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Task identifier.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createTaskCallable()
    
    
    public final UnaryCallable<CreateTaskRequest,Operation> createTaskCallable()

Creates a task resource within a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       CreateTaskRequest request =
           CreateTaskRequest.newBuilder()
               .setParent(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .setTaskId("taskId-880873088")
               .setTask(Task.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = dataplexServiceClient.createTaskCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateTaskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createTaskOperationCallable()
    
    
    public final OperationCallable<CreateTaskRequest,Task,OperationMetadata> createTaskOperationCallable()

Creates a task resource within a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       CreateTaskRequest request =
           CreateTaskRequest.newBuilder()
               .setParent(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .setTaskId("taskId-880873088")
               .setTask(Task.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<Task, OperationMetadata> future =
           dataplexServiceClient.createTaskOperationCallable().futureCall(request);
       // Do something.
       Task response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateTaskRequest),[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createZoneAsync(@Nullable LakeName parent, Zone zone, String zoneId)
    
    
    public final OperationFuture<Zone,OperationMetadata> createZoneAsync(@Nullable LakeName parent, Zone zone, String zoneId)

Creates a zone resource within a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       LakeName parent = LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]");
       Zone zone = Zone.newBuilder().build();
       String zoneId = "zoneId-696323609";
       Zone response = dataplexServiceClient.createZoneAsync(parent, zone, zoneId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LakeName`  
Required. The resource name of the parent lake: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`.  
`zone` | `[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Zone)`  
Required. Zone resource.  
`zoneId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Zone identifier. This ID will be used to generate names such as database and dataset names when publishing metadata to Hive Metastore and BigQuery. 

  * Must contain only lowercase letters, numbers and hyphens. 
  * Must start with a letter. 
  * Must end with a number or a letter. 
  * Must be between 1-63 characters. 
  * Must be unique across all lakes from all locations in a project. 
  * Must not be one of the reserved IDs (i.e. "default", "global-temp") 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createZoneAsync(CreateZoneRequest request)
    
    
    public final OperationFuture<Zone,OperationMetadata> createZoneAsync(CreateZoneRequest request)

Creates a zone resource within a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       CreateZoneRequest request =
           CreateZoneRequest.newBuilder()
               .setParent(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .setZoneId("zoneId-696323609")
               .setZone(Zone.newBuilder().build())
               .setValidateOnly(true)
               .build();
       Zone response = dataplexServiceClient.createZoneAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateZoneRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createZoneAsync(String parent, Zone zone, String zoneId)
    
    
    public final OperationFuture<Zone,OperationMetadata> createZoneAsync(String parent, Zone zone, String zoneId)

Creates a zone resource within a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String parent = LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString();
       Zone zone = Zone.newBuilder().build();
       String zoneId = "zoneId-696323609";
       Zone response = dataplexServiceClient.createZoneAsync(parent, zone, zoneId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent lake: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`.  
`zone` | `[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Zone)`  
Required. Zone resource.  
`zoneId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Zone identifier. This ID will be used to generate names such as database and dataset names when publishing metadata to Hive Metastore and BigQuery. 

  * Must contain only lowercase letters, numbers and hyphens. 
  * Must start with a letter. 
  * Must end with a number or a letter. 
  * Must be between 1-63 characters. 
  * Must be unique across all lakes from all locations in a project. 
  * Must not be one of the reserved IDs (i.e. "default", "global-temp") 

  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### createZoneCallable()
    
    
    public final UnaryCallable<CreateZoneRequest,Operation> createZoneCallable()

Creates a zone resource within a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       CreateZoneRequest request =
           CreateZoneRequest.newBuilder()
               .setParent(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .setZoneId("zoneId-696323609")
               .setZone(Zone.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = dataplexServiceClient.createZoneCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateZoneRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createZoneOperationCallable()
    
    
    public final OperationCallable<CreateZoneRequest,Zone,OperationMetadata> createZoneOperationCallable()

Creates a zone resource within a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       CreateZoneRequest request =
           CreateZoneRequest.newBuilder()
               .setParent(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .setZoneId("zoneId-696323609")
               .setZone(Zone.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<Zone, OperationMetadata> future =
           dataplexServiceClient.createZoneOperationCallable().futureCall(request);
       // Do something.
       Zone response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateZoneRequest),[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteAssetAsync(@Nullable AssetName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAssetAsync(@Nullable AssetName name)

Deletes an asset resource. The referenced storage resource is detached (default) or deleted based on the associated Lifecycle policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       AssetName name = AssetName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]", "[ASSET]");
       dataplexServiceClient.deleteAssetAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.AssetName`  
Required. The resource name of the asset: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteAssetAsync(DeleteAssetRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAssetAsync(DeleteAssetRequest request)

Deletes an asset resource. The referenced storage resource is detached (default) or deleted based on the associated Lifecycle policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       DeleteAssetRequest request =
           DeleteAssetRequest.newBuilder()
               .setName(
                   AssetName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]", "[ASSET]").toString())
               .build();
       dataplexServiceClient.deleteAssetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteAssetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteAssetAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteAssetAsync(String name)

Deletes an asset resource. The referenced storage resource is detached (default) or deleted based on the associated Lifecycle policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String name =
           AssetName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]", "[ASSET]").toString();
       dataplexServiceClient.deleteAssetAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the asset: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteAssetCallable()
    
    
    public final UnaryCallable<DeleteAssetRequest,Operation> deleteAssetCallable()

Deletes an asset resource. The referenced storage resource is detached (default) or deleted based on the associated Lifecycle policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       DeleteAssetRequest request =
           DeleteAssetRequest.newBuilder()
               .setName(
                   AssetName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]", "[ASSET]").toString())
               .build();
       ApiFuture<Operation> future = dataplexServiceClient.deleteAssetCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteAssetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAssetOperationCallable()
    
    
    public final OperationCallable<DeleteAssetRequest,Empty,OperationMetadata> deleteAssetOperationCallable()

Deletes an asset resource. The referenced storage resource is detached (default) or deleted based on the associated Lifecycle policy.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       DeleteAssetRequest request =
           DeleteAssetRequest.newBuilder()
               .setName(
                   AssetName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]", "[ASSET]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataplexServiceClient.deleteAssetOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteAssetRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteLakeAsync(@Nullable LakeName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLakeAsync(@Nullable LakeName name)

Deletes a lake resource. All zones within the lake must be deleted before the lake can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       LakeName name = LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]");
       dataplexServiceClient.deleteLakeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LakeName`  
Required. The resource name of the lake: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteLakeAsync(DeleteLakeRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLakeAsync(DeleteLakeRequest request)

Deletes a lake resource. All zones within the lake must be deleted before the lake can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       DeleteLakeRequest request =
           DeleteLakeRequest.newBuilder()
               .setName(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .build();
       dataplexServiceClient.deleteLakeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteLakeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteLakeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteLakeAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteLakeAsync(String name)

Deletes a lake resource. All zones within the lake must be deleted before the lake can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String name = LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString();
       dataplexServiceClient.deleteLakeAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the lake: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteLakeCallable()
    
    
    public final UnaryCallable<DeleteLakeRequest,Operation> deleteLakeCallable()

Deletes a lake resource. All zones within the lake must be deleted before the lake can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       DeleteLakeRequest request =
           DeleteLakeRequest.newBuilder()
               .setName(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .build();
       ApiFuture<Operation> future = dataplexServiceClient.deleteLakeCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteLakeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteLakeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteLakeOperationCallable()
    
    
    public final OperationCallable<DeleteLakeRequest,Empty,OperationMetadata> deleteLakeOperationCallable()

Deletes a lake resource. All zones within the lake must be deleted before the lake can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       DeleteLakeRequest request =
           DeleteLakeRequest.newBuilder()
               .setName(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataplexServiceClient.deleteLakeOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteLakeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteLakeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteTaskAsync(@Nullable TaskName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteTaskAsync(@Nullable TaskName name)

Delete the task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       TaskName name = TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]");
       dataplexServiceClient.deleteTaskAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.TaskName`  
Required. The resource name of the task: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/task/{task_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteTaskAsync(DeleteTaskRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteTaskAsync(DeleteTaskRequest request)

Delete the task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       DeleteTaskRequest request =
           DeleteTaskRequest.newBuilder()
               .setName(TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]").toString())
               .build();
       dataplexServiceClient.deleteTaskAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteTaskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteTaskAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteTaskAsync(String name)

Delete the task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String name = TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]").toString();
       dataplexServiceClient.deleteTaskAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the task: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/task/{task_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteTaskCallable()
    
    
    public final UnaryCallable<DeleteTaskRequest,Operation> deleteTaskCallable()

Delete the task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       DeleteTaskRequest request =
           DeleteTaskRequest.newBuilder()
               .setName(TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]").toString())
               .build();
       ApiFuture<Operation> future = dataplexServiceClient.deleteTaskCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteTaskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTaskOperationCallable()
    
    
    public final OperationCallable<DeleteTaskRequest,Empty,OperationMetadata> deleteTaskOperationCallable()

Delete the task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       DeleteTaskRequest request =
           DeleteTaskRequest.newBuilder()
               .setName(TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataplexServiceClient.deleteTaskOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteTaskRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteZoneAsync(@Nullable ZoneName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteZoneAsync(@Nullable ZoneName name)

Deletes a zone resource. All assets within a zone must be deleted before the zone can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ZoneName name = ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]");
       dataplexServiceClient.deleteZoneAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.ZoneName`  
Required. The resource name of the zone: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteZoneAsync(DeleteZoneRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteZoneAsync(DeleteZoneRequest request)

Deletes a zone resource. All assets within a zone must be deleted before the zone can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       DeleteZoneRequest request =
           DeleteZoneRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString())
               .build();
       dataplexServiceClient.deleteZoneAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteZoneRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteZoneAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteZoneAsync(String name)

Deletes a zone resource. All assets within a zone must be deleted before the zone can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String name = ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString();
       dataplexServiceClient.deleteZoneAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the zone: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### deleteZoneCallable()
    
    
    public final UnaryCallable<DeleteZoneRequest,Operation> deleteZoneCallable()

Deletes a zone resource. All assets within a zone must be deleted before the zone can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       DeleteZoneRequest request =
           DeleteZoneRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString())
               .build();
       ApiFuture<Operation> future = dataplexServiceClient.deleteZoneCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteZoneRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteZoneOperationCallable()
    
    
    public final OperationCallable<DeleteZoneRequest,Empty,OperationMetadata> deleteZoneOperationCallable()

Deletes a zone resource. All assets within a zone must be deleted before the zone can be deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       DeleteZoneRequest request =
           DeleteZoneRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString())
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           dataplexServiceClient.deleteZoneOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteZoneRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### getAsset(@Nullable AssetName name)
    
    
    public final Asset getAsset(@Nullable AssetName name)

Retrieves an asset resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       AssetName name = AssetName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]", "[ASSET]");
       Asset response = dataplexServiceClient.getAsset(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.AssetName`  
Required. The resource name of the asset: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Asset)` |   
  
### getAsset(GetAssetRequest request)
    
    
    public final Asset getAsset(GetAssetRequest request)

Retrieves an asset resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       GetAssetRequest request =
           GetAssetRequest.newBuilder()
               .setName(
                   AssetName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]", "[ASSET]").toString())
               .build();
       Asset response = dataplexServiceClient.getAsset(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetAssetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Asset)` |   
  
### getAsset(String name)
    
    
    public final Asset getAsset(String name)

Retrieves an asset resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String name =
           AssetName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]", "[ASSET]").toString();
       Asset response = dataplexServiceClient.getAsset(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the asset: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Asset)` |   
  
### getAssetCallable()
    
    
    public final UnaryCallable<GetAssetRequest,Asset> getAssetCallable()

Retrieves an asset resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       GetAssetRequest request =
           GetAssetRequest.newBuilder()
               .setName(
                   AssetName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]", "[ASSET]").toString())
               .build();
       ApiFuture<Asset> future = dataplexServiceClient.getAssetCallable().futureCall(request);
       // Do something.
       Asset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetAssetRequest),[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Asset)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = dataplexServiceClient.getIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### getIamPolicyCallable()
    
    
    public final UnaryCallable<GetIamPolicyRequest,Policy> getIamPolicyCallable()

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = dataplexServiceClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getJob(@Nullable JobName name)
    
    
    public final Job getJob(@Nullable JobName name)

Get job resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       JobName name = JobName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]", "[JOB]");
       Job response = dataplexServiceClient.getJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.JobName`  
Required. The resource name of the job: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{task_id}/jobs/{job_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Job)` |   
  
### getJob(GetJobRequest request)
    
    
    public final Job getJob(GetJobRequest request)

Get job resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       GetJobRequest request =
           GetJobRequest.newBuilder()
               .setName(
                   JobName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]", "[JOB]").toString())
               .build();
       Job response = dataplexServiceClient.getJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Job)` |   
  
### getJob(String name)
    
    
    public final Job getJob(String name)

Get job resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String name = JobName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]", "[JOB]").toString();
       Job response = dataplexServiceClient.getJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the job: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{task_id}/jobs/{job_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Job)` |   
  
### getJobCallable()
    
    
    public final UnaryCallable<GetJobRequest,Job> getJobCallable()

Get job resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       GetJobRequest request =
           GetJobRequest.newBuilder()
               .setName(
                   JobName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]", "[JOB]").toString())
               .build();
       ApiFuture<Job> future = dataplexServiceClient.getJobCallable().futureCall(request);
       // Do something.
       Job response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetJobRequest),[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Job)>` |   
  
### getLake(@Nullable LakeName name)
    
    
    public final Lake getLake(@Nullable LakeName name)

Retrieves a lake resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       LakeName name = LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]");
       Lake response = dataplexServiceClient.getLake(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LakeName`  
Required. The resource name of the lake: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Lake](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Lake)` |   
  
### getLake(GetLakeRequest request)
    
    
    public final Lake getLake(GetLakeRequest request)

Retrieves a lake resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       GetLakeRequest request =
           GetLakeRequest.newBuilder()
               .setName(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .build();
       Lake response = dataplexServiceClient.getLake(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetLakeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetLakeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Lake](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Lake)` |   
  
### getLake(String name)
    
    
    public final Lake getLake(String name)

Retrieves a lake resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String name = LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString();
       Lake response = dataplexServiceClient.getLake(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the lake: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Lake](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Lake)` |   
  
### getLakeCallable()
    
    
    public final UnaryCallable<GetLakeRequest,Lake> getLakeCallable()

Retrieves a lake resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       GetLakeRequest request =
           GetLakeRequest.newBuilder()
               .setName(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .build();
       ApiFuture<Lake> future = dataplexServiceClient.getLakeCallable().futureCall(request);
       // Do something.
       Lake response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetLakeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetLakeRequest),[Lake](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Lake)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = dataplexServiceClient.getLocation(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.GetLocationRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.location.Location` |   
  
### getLocationCallable()
    
    
    public final UnaryCallable<GetLocationRequest,Location> getLocationCallable()

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = dataplexServiceClient.getLocationCallable().futureCall(request);
       // Do something.
       Location response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable DataplexServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.DataplexServiceSettings` |   
  
### getStub()
    
    
    public DataplexServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.stub.DataplexServiceStub)` |   
  
### getTask(@Nullable TaskName name)
    
    
    public final Task getTask(@Nullable TaskName name)

Get task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       TaskName name = TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]");
       Task response = dataplexServiceClient.getTask(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.TaskName`  
Required. The resource name of the task: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{tasks_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task)` |   
  
### getTask(GetTaskRequest request)
    
    
    public final Task getTask(GetTaskRequest request)

Get task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       GetTaskRequest request =
           GetTaskRequest.newBuilder()
               .setName(TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]").toString())
               .build();
       Task response = dataplexServiceClient.getTask(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetTaskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task)` |   
  
### getTask(String name)
    
    
    public final Task getTask(String name)

Get task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String name = TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]").toString();
       Task response = dataplexServiceClient.getTask(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the task: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{tasks_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task)` |   
  
### getTaskCallable()
    
    
    public final UnaryCallable<GetTaskRequest,Task> getTaskCallable()

Get task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       GetTaskRequest request =
           GetTaskRequest.newBuilder()
               .setName(TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]").toString())
               .build();
       ApiFuture<Task> future = dataplexServiceClient.getTaskCallable().futureCall(request);
       // Do something.
       Task response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetTaskRequest),[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task)>` |   
  
### getZone(@Nullable ZoneName name)
    
    
    public final Zone getZone(@Nullable ZoneName name)

Retrieves a zone resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ZoneName name = ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]");
       Zone response = dataplexServiceClient.getZone(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.ZoneName`  
Required. The resource name of the zone: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Zone)` |   
  
### getZone(GetZoneRequest request)
    
    
    public final Zone getZone(GetZoneRequest request)

Retrieves a zone resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       GetZoneRequest request =
           GetZoneRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString())
               .build();
       Zone response = dataplexServiceClient.getZone(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetZoneRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Zone)` |   
  
### getZone(String name)
    
    
    public final Zone getZone(String name)

Retrieves a zone resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String name = ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString();
       Zone response = dataplexServiceClient.getZone(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the zone: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Zone)` |   
  
### getZoneCallable()
    
    
    public final UnaryCallable<GetZoneRequest,Zone> getZoneCallable()

Retrieves a zone resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       GetZoneRequest request =
           GetZoneRequest.newBuilder()
               .setName(ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString())
               .build();
       ApiFuture<Zone> future = dataplexServiceClient.getZoneCallable().futureCall(request);
       // Do something.
       Zone response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetZoneRequest),[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Zone)>` |   
  
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
  
### listAssetActions(@Nullable AssetName parent)
    
    
    public final DataplexServiceClient.ListAssetActionsPagedResponse listAssetActions(@Nullable AssetName parent)

Lists action resources in an asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       AssetName parent = AssetName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]", "[ASSET]");
       for (Action element : dataplexServiceClient.listAssetActions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.AssetName`  
Required. The resource name of the parent asset: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListAssetActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListAssetActionsPagedResponse)` |   
  
### listAssetActions(ListAssetActionsRequest request)
    
    
    public final DataplexServiceClient.ListAssetActionsPagedResponse listAssetActions(ListAssetActionsRequest request)

Lists action resources in an asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListAssetActionsRequest request =
           ListAssetActionsRequest.newBuilder()
               .setParent(
                   AssetName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]", "[ASSET]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Action element : dataplexServiceClient.listAssetActions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAssetActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListAssetActionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListAssetActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListAssetActionsPagedResponse)` |   
  
### listAssetActions(String parent)
    
    
    public final DataplexServiceClient.ListAssetActionsPagedResponse listAssetActions(String parent)

Lists action resources in an asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String parent =
           AssetName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]", "[ASSET]").toString();
       for (Action element : dataplexServiceClient.listAssetActions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent asset: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListAssetActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListAssetActionsPagedResponse)` |   
  
### listAssetActionsCallable()
    
    
    public final UnaryCallable<ListAssetActionsRequest,ListActionsResponse> listAssetActionsCallable()

Lists action resources in an asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListAssetActionsRequest request =
           ListAssetActionsRequest.newBuilder()
               .setParent(
                   AssetName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]", "[ASSET]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListActionsResponse response =
             dataplexServiceClient.listAssetActionsCallable().call(request);
         for (Action element : response.getActionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAssetActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListAssetActionsRequest),[ListActionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListActionsResponse)>` |   
  
### listAssetActionsPagedCallable()
    
    
    public final UnaryCallable<ListAssetActionsRequest,DataplexServiceClient.ListAssetActionsPagedResponse> listAssetActionsPagedCallable()

Lists action resources in an asset.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListAssetActionsRequest request =
           ListAssetActionsRequest.newBuilder()
               .setParent(
                   AssetName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]", "[ASSET]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Action> future =
           dataplexServiceClient.listAssetActionsPagedCallable().futureCall(request);
       // Do something.
       for (Action element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAssetActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListAssetActionsRequest),[ListAssetActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListAssetActionsPagedResponse)>` |   
  
### listAssets(@Nullable ZoneName parent)
    
    
    public final DataplexServiceClient.ListAssetsPagedResponse listAssets(@Nullable ZoneName parent)

Lists asset resources in a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ZoneName parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]");
       for (Asset element : dataplexServiceClient.listAssets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.ZoneName`  
Required. The resource name of the parent zone: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListAssetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListAssetsPagedResponse)` |   
  
### listAssets(ListAssetsRequest request)
    
    
    public final DataplexServiceClient.ListAssetsPagedResponse listAssets(ListAssetsRequest request)

Lists asset resources in a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListAssetsRequest request =
           ListAssetsRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Asset element : dataplexServiceClient.listAssets(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListAssetsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListAssetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListAssetsPagedResponse)` |   
  
### listAssets(String parent)
    
    
    public final DataplexServiceClient.ListAssetsPagedResponse listAssets(String parent)

Lists asset resources in a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString();
       for (Asset element : dataplexServiceClient.listAssets(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent zone: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListAssetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListAssetsPagedResponse)` |   
  
### listAssetsCallable()
    
    
    public final UnaryCallable<ListAssetsRequest,ListAssetsResponse> listAssetsCallable()

Lists asset resources in a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListAssetsRequest request =
           ListAssetsRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListAssetsResponse response = dataplexServiceClient.listAssetsCallable().call(request);
         for (Asset element : response.getAssetsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListAssetsRequest),[ListAssetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListAssetsResponse)>` |   
  
### listAssetsPagedCallable()
    
    
    public final UnaryCallable<ListAssetsRequest,DataplexServiceClient.ListAssetsPagedResponse> listAssetsPagedCallable()

Lists asset resources in a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListAssetsRequest request =
           ListAssetsRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Asset> future = dataplexServiceClient.listAssetsPagedCallable().futureCall(request);
       // Do something.
       for (Asset element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListAssetsRequest),[ListAssetsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListAssetsPagedResponse)>` |   
  
### listJobs(@Nullable TaskName parent)
    
    
    public final DataplexServiceClient.ListJobsPagedResponse listJobs(@Nullable TaskName parent)

Lists Jobs under the given task.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       TaskName parent = TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]");
       for (Job element : dataplexServiceClient.listJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.TaskName`  
Required. The resource name of the parent environment: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{task_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListJobsPagedResponse)` |   
  
### listJobs(ListJobsRequest request)
    
    
    public final DataplexServiceClient.ListJobsPagedResponse listJobs(ListJobsRequest request)

Lists Jobs under the given task.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListJobsRequest request =
           ListJobsRequest.newBuilder()
               .setParent(TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Job element : dataplexServiceClient.listJobs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListJobsPagedResponse)` |   
  
### listJobs(String parent)
    
    
    public final DataplexServiceClient.ListJobsPagedResponse listJobs(String parent)

Lists Jobs under the given task.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String parent = TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]").toString();
       for (Job element : dataplexServiceClient.listJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent environment: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{task_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListJobsPagedResponse)` |   
  
### listJobsCallable()
    
    
    public final UnaryCallable<ListJobsRequest,ListJobsResponse> listJobsCallable()

Lists Jobs under the given task.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListJobsRequest request =
           ListJobsRequest.newBuilder()
               .setParent(TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListJobsResponse response = dataplexServiceClient.listJobsCallable().call(request);
         for (Job element : response.getJobsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListJobsRequest),[ListJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListJobsResponse)>` |   
  
### listJobsPagedCallable()
    
    
    public final UnaryCallable<ListJobsRequest,DataplexServiceClient.ListJobsPagedResponse> listJobsPagedCallable()

Lists Jobs under the given task.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListJobsRequest request =
           ListJobsRequest.newBuilder()
               .setParent(TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Job> future = dataplexServiceClient.listJobsPagedCallable().futureCall(request);
       // Do something.
       for (Job element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListJobsRequest),[ListJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListJobsPagedResponse)>` |   
  
### listLakeActions(@Nullable LakeName parent)
    
    
    public final DataplexServiceClient.ListLakeActionsPagedResponse listLakeActions(@Nullable LakeName parent)

Lists action resources in a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       LakeName parent = LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]");
       for (Action element : dataplexServiceClient.listLakeActions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LakeName`  
Required. The resource name of the parent lake: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListLakeActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListLakeActionsPagedResponse)` |   
  
### listLakeActions(ListLakeActionsRequest request)
    
    
    public final DataplexServiceClient.ListLakeActionsPagedResponse listLakeActions(ListLakeActionsRequest request)

Lists action resources in a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListLakeActionsRequest request =
           ListLakeActionsRequest.newBuilder()
               .setParent(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Action element : dataplexServiceClient.listLakeActions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLakeActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListLakeActionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListLakeActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListLakeActionsPagedResponse)` |   
  
### listLakeActions(String parent)
    
    
    public final DataplexServiceClient.ListLakeActionsPagedResponse listLakeActions(String parent)

Lists action resources in a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String parent = LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString();
       for (Action element : dataplexServiceClient.listLakeActions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent lake: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListLakeActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListLakeActionsPagedResponse)` |   
  
### listLakeActionsCallable()
    
    
    public final UnaryCallable<ListLakeActionsRequest,ListActionsResponse> listLakeActionsCallable()

Lists action resources in a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListLakeActionsRequest request =
           ListLakeActionsRequest.newBuilder()
               .setParent(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListActionsResponse response =
             dataplexServiceClient.listLakeActionsCallable().call(request);
         for (Action element : response.getActionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLakeActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListLakeActionsRequest),[ListActionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListActionsResponse)>` |   
  
### listLakeActionsPagedCallable()
    
    
    public final UnaryCallable<ListLakeActionsRequest,DataplexServiceClient.ListLakeActionsPagedResponse> listLakeActionsPagedCallable()

Lists action resources in a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListLakeActionsRequest request =
           ListLakeActionsRequest.newBuilder()
               .setParent(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Action> future =
           dataplexServiceClient.listLakeActionsPagedCallable().futureCall(request);
       // Do something.
       for (Action element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLakeActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListLakeActionsRequest),[ListLakeActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListLakeActionsPagedResponse)>` |   
  
### listLakes(@Nullable LocationName parent)
    
    
    public final DataplexServiceClient.ListLakesPagedResponse listLakes(@Nullable LocationName parent)

Lists lake resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (Lake element : dataplexServiceClient.listLakes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LocationName`  
Required. The resource name of the lake location, of the form: `projects/{project_number}/locations/{location_id}` where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListLakesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListLakesPagedResponse)` |   
  
### listLakes(ListLakesRequest request)
    
    
    public final DataplexServiceClient.ListLakesPagedResponse listLakes(ListLakesRequest request)

Lists lake resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListLakesRequest request =
           ListLakesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Lake element : dataplexServiceClient.listLakes(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListLakesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListLakesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListLakesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListLakesPagedResponse)` |   
  
### listLakes(String parent)
    
    
    public final DataplexServiceClient.ListLakesPagedResponse listLakes(String parent)

Lists lake resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (Lake element : dataplexServiceClient.listLakes(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the lake location, of the form: `projects/{project_number}/locations/{location_id}` where `location_id` refers to a Google Cloud region.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListLakesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListLakesPagedResponse)` |   
  
### listLakesCallable()
    
    
    public final UnaryCallable<ListLakesRequest,ListLakesResponse> listLakesCallable()

Lists lake resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListLakesRequest request =
           ListLakesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListLakesResponse response = dataplexServiceClient.listLakesCallable().call(request);
         for (Lake element : response.getLakesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLakesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListLakesRequest),[ListLakesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListLakesResponse)>` |   
  
### listLakesPagedCallable()
    
    
    public final UnaryCallable<ListLakesRequest,DataplexServiceClient.ListLakesPagedResponse> listLakesPagedCallable()

Lists lake resources in a project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListLakesRequest request =
           ListLakesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Lake> future = dataplexServiceClient.listLakesPagedCallable().futureCall(request);
       // Do something.
       for (Lake element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListLakesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListLakesRequest),[ListLakesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListLakesPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final DataplexServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : dataplexServiceClient.listLocations(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.cloud.location.ListLocationsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             dataplexServiceClient.listLocationsCallable().call(request);
         for (Location element : response.getLocationsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse>` |   
  
### listLocationsPagedCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,DataplexServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           dataplexServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListLocationsPagedResponse)>` |   
  
### listTasks(@Nullable LakeName parent)
    
    
    public final DataplexServiceClient.ListTasksPagedResponse listTasks(@Nullable LakeName parent)

Lists tasks under the given lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       LakeName parent = LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]");
       for (Task element : dataplexServiceClient.listTasks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LakeName`  
Required. The resource name of the parent lake: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListTasksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListTasksPagedResponse)` |   
  
### listTasks(ListTasksRequest request)
    
    
    public final DataplexServiceClient.ListTasksPagedResponse listTasks(ListTasksRequest request)

Lists tasks under the given lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListTasksRequest request =
           ListTasksRequest.newBuilder()
               .setParent(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Task element : dataplexServiceClient.listTasks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTasksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListTasksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListTasksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListTasksPagedResponse)` |   
  
### listTasks(String parent)
    
    
    public final DataplexServiceClient.ListTasksPagedResponse listTasks(String parent)

Lists tasks under the given lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String parent = LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString();
       for (Task element : dataplexServiceClient.listTasks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent lake: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListTasksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListTasksPagedResponse)` |   
  
### listTasksCallable()
    
    
    public final UnaryCallable<ListTasksRequest,ListTasksResponse> listTasksCallable()

Lists tasks under the given lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListTasksRequest request =
           ListTasksRequest.newBuilder()
               .setParent(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListTasksResponse response = dataplexServiceClient.listTasksCallable().call(request);
         for (Task element : response.getTasksList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTasksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListTasksRequest),[ListTasksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListTasksResponse)>` |   
  
### listTasksPagedCallable()
    
    
    public final UnaryCallable<ListTasksRequest,DataplexServiceClient.ListTasksPagedResponse> listTasksPagedCallable()

Lists tasks under the given lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListTasksRequest request =
           ListTasksRequest.newBuilder()
               .setParent(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Task> future = dataplexServiceClient.listTasksPagedCallable().futureCall(request);
       // Do something.
       for (Task element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTasksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListTasksRequest),[ListTasksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListTasksPagedResponse)>` |   
  
### listZoneActions(@Nullable ZoneName parent)
    
    
    public final DataplexServiceClient.ListZoneActionsPagedResponse listZoneActions(@Nullable ZoneName parent)

Lists action resources in a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ZoneName parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]");
       for (Action element : dataplexServiceClient.listZoneActions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.ZoneName`  
Required. The resource name of the parent zone: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListZoneActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListZoneActionsPagedResponse)` |   
  
### listZoneActions(ListZoneActionsRequest request)
    
    
    public final DataplexServiceClient.ListZoneActionsPagedResponse listZoneActions(ListZoneActionsRequest request)

Lists action resources in a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListZoneActionsRequest request =
           ListZoneActionsRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Action element : dataplexServiceClient.listZoneActions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListZoneActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListZoneActionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListZoneActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListZoneActionsPagedResponse)` |   
  
### listZoneActions(String parent)
    
    
    public final DataplexServiceClient.ListZoneActionsPagedResponse listZoneActions(String parent)

Lists action resources in a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String parent = ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString();
       for (Action element : dataplexServiceClient.listZoneActions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent zone: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListZoneActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListZoneActionsPagedResponse)` |   
  
### listZoneActionsCallable()
    
    
    public final UnaryCallable<ListZoneActionsRequest,ListActionsResponse> listZoneActionsCallable()

Lists action resources in a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListZoneActionsRequest request =
           ListZoneActionsRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListActionsResponse response =
             dataplexServiceClient.listZoneActionsCallable().call(request);
         for (Action element : response.getActionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListZoneActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListZoneActionsRequest),[ListActionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListActionsResponse)>` |   
  
### listZoneActionsPagedCallable()
    
    
    public final UnaryCallable<ListZoneActionsRequest,DataplexServiceClient.ListZoneActionsPagedResponse> listZoneActionsPagedCallable()

Lists action resources in a zone.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListZoneActionsRequest request =
           ListZoneActionsRequest.newBuilder()
               .setParent(ZoneName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[ZONE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Action> future =
           dataplexServiceClient.listZoneActionsPagedCallable().futureCall(request);
       // Do something.
       for (Action element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListZoneActionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListZoneActionsRequest),[ListZoneActionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListZoneActionsPagedResponse)>` |   
  
### listZones(@Nullable LakeName parent)
    
    
    public final DataplexServiceClient.ListZonesPagedResponse listZones(@Nullable LakeName parent)

Lists zone resources in a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       LakeName parent = LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]");
       for (Zone element : dataplexServiceClient.listZones(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.LakeName`  
Required. The resource name of the parent lake: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListZonesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListZonesPagedResponse)` |   
  
### listZones(ListZonesRequest request)
    
    
    public final DataplexServiceClient.ListZonesPagedResponse listZones(ListZonesRequest request)

Lists zone resources in a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListZonesRequest request =
           ListZonesRequest.newBuilder()
               .setParent(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Zone element : dataplexServiceClient.listZones(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListZonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListZonesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListZonesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListZonesPagedResponse)` |   
  
### listZones(String parent)
    
    
    public final DataplexServiceClient.ListZonesPagedResponse listZones(String parent)

Lists zone resources in a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String parent = LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString();
       for (Zone element : dataplexServiceClient.listZones(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the parent lake: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[DataplexServiceClient.ListZonesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListZonesPagedResponse)` |   
  
### listZonesCallable()
    
    
    public final UnaryCallable<ListZonesRequest,ListZonesResponse> listZonesCallable()

Lists zone resources in a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListZonesRequest request =
           ListZonesRequest.newBuilder()
               .setParent(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         ListZonesResponse response = dataplexServiceClient.listZonesCallable().call(request);
         for (Zone element : response.getZonesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListZonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListZonesRequest),[ListZonesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListZonesResponse)>` |   
  
### listZonesPagedCallable()
    
    
    public final UnaryCallable<ListZonesRequest,DataplexServiceClient.ListZonesPagedResponse> listZonesPagedCallable()

Lists zone resources in a lake.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       ListZonesRequest request =
           ListZonesRequest.newBuilder()
               .setParent(LakeName.of("[PROJECT]", "[LOCATION]", "[LAKE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Zone> future = dataplexServiceClient.listZonesPagedCallable().futureCall(request);
       // Do something.
       for (Zone element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListZonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListZonesRequest),[ListZonesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataplexServiceClient.ListZonesPagedResponse)>` |   
  
### runTask(@Nullable TaskName name)
    
    
    public final RunTaskResponse runTask(@Nullable TaskName name)

Run an on demand execution of a Task.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       TaskName name = TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]");
       RunTaskResponse response = dataplexServiceClient.runTask(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.dataplex.v1.TaskName`  
Required. The resource name of the task: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{task_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[RunTaskResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunTaskResponse)` |   
  
### runTask(RunTaskRequest request)
    
    
    public final RunTaskResponse runTask(RunTaskRequest request)

Run an on demand execution of a Task.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       RunTaskRequest request =
           RunTaskRequest.newBuilder()
               .setName(TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]").toString())
               .putAllLabels(new HashMap<String, String>())
               .putAllArgs(new HashMap<String, String>())
               .build();
       RunTaskResponse response = dataplexServiceClient.runTask(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunTaskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RunTaskResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunTaskResponse)` |   
  
### runTask(String name)
    
    
    public final RunTaskResponse runTask(String name)

Run an on demand execution of a Task.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       String name = TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]").toString();
       RunTaskResponse response = dataplexServiceClient.runTask(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the task: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/tasks/{task_id}`.  
**Returns**  
---  
**Type** | **Description**  
`[RunTaskResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunTaskResponse)` |   
  
### runTaskCallable()
    
    
    public final UnaryCallable<RunTaskRequest,RunTaskResponse> runTaskCallable()

Run an on demand execution of a Task.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       RunTaskRequest request =
           RunTaskRequest.newBuilder()
               .setName(TaskName.of("[PROJECT]", "[LOCATION]", "[LAKE]", "[TASK]").toString())
               .putAllLabels(new HashMap<String, String>())
               .putAllArgs(new HashMap<String, String>())
               .build();
       ApiFuture<RunTaskResponse> future =
           dataplexServiceClient.runTaskCallable().futureCall(request);
       // Do something.
       RunTaskResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RunTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunTaskRequest),[RunTaskResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.RunTaskResponse)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public final Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = dataplexServiceClient.setIamPolicy(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` |   
  
### setIamPolicyCallable()
    
    
    public final UnaryCallable<SetIamPolicyRequest,Policy> setIamPolicyCallable()

Sets the access control policy on the specified resource. Replacesany existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED`errors.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = dataplexServiceClient.setIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public final TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = dataplexServiceClient.testIamPermissions(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.TestIamPermissionsResponse` |   
  
### testIamPermissionsCallable()
    
    
    public final UnaryCallable<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsCallable()

Returns permissions that a caller has on the specified resource. If theresource does not exist, this will return an empty set ofpermissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for buildingpermission-aware UIs and command-line tools, not for authorizationchecking. This operation may "fail open" without warning.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(AspectTypeName.of("[PROJECT]", "[LOCATION]", "[ASPECT_TYPE]").toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           dataplexServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateAssetAsync(Asset asset, FieldMask updateMask)
    
    
    public final OperationFuture<Asset,OperationMetadata> updateAssetAsync(Asset asset, FieldMask updateMask)

Updates an asset resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       Asset asset = Asset.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Asset response = dataplexServiceClient.updateAssetAsync(asset, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`asset` | `[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Asset)`  
Required. Update description. Only fields specified in `update_mask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Mask of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Asset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateAssetAsync(UpdateAssetRequest request)
    
    
    public final OperationFuture<Asset,OperationMetadata> updateAssetAsync(UpdateAssetRequest request)

Updates an asset resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       UpdateAssetRequest request =
           UpdateAssetRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAsset(Asset.newBuilder().build())
               .setValidateOnly(true)
               .build();
       Asset response = dataplexServiceClient.updateAssetAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateAssetRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Asset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateAssetCallable()
    
    
    public final UnaryCallable<UpdateAssetRequest,Operation> updateAssetCallable()

Updates an asset resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       UpdateAssetRequest request =
           UpdateAssetRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAsset(Asset.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = dataplexServiceClient.updateAssetCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateAssetRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateAssetOperationCallable()
    
    
    public final OperationCallable<UpdateAssetRequest,Asset,OperationMetadata> updateAssetOperationCallable()

Updates an asset resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       UpdateAssetRequest request =
           UpdateAssetRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAsset(Asset.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<Asset, OperationMetadata> future =
           dataplexServiceClient.updateAssetOperationCallable().futureCall(request);
       // Do something.
       Asset response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateAssetRequest),[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Asset),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateLakeAsync(Lake lake, FieldMask updateMask)
    
    
    public final OperationFuture<Lake,OperationMetadata> updateLakeAsync(Lake lake, FieldMask updateMask)

Updates a lake resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       Lake lake = Lake.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Lake response = dataplexServiceClient.updateLakeAsync(lake, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`lake` | `[Lake](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Lake)`  
Required. Update description. Only fields specified in `update_mask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Mask of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Lake](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Lake),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateLakeAsync(UpdateLakeRequest request)
    
    
    public final OperationFuture<Lake,OperationMetadata> updateLakeAsync(UpdateLakeRequest request)

Updates a lake resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       UpdateLakeRequest request =
           UpdateLakeRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLake(Lake.newBuilder().build())
               .setValidateOnly(true)
               .build();
       Lake response = dataplexServiceClient.updateLakeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateLakeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateLakeRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Lake](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Lake),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateLakeCallable()
    
    
    public final UnaryCallable<UpdateLakeRequest,Operation> updateLakeCallable()

Updates a lake resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       UpdateLakeRequest request =
           UpdateLakeRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLake(Lake.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = dataplexServiceClient.updateLakeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateLakeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateLakeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateLakeOperationCallable()
    
    
    public final OperationCallable<UpdateLakeRequest,Lake,OperationMetadata> updateLakeOperationCallable()

Updates a lake resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       UpdateLakeRequest request =
           UpdateLakeRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setLake(Lake.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<Lake, OperationMetadata> future =
           dataplexServiceClient.updateLakeOperationCallable().futureCall(request);
       // Do something.
       Lake response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateLakeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateLakeRequest),[Lake](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Lake),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateTaskAsync(Task task, FieldMask updateMask)
    
    
    public final OperationFuture<Task,OperationMetadata> updateTaskAsync(Task task, FieldMask updateMask)

Update the task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       Task task = Task.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Task response = dataplexServiceClient.updateTaskAsync(task, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`task` | `[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task)`  
Required. Update description. Only fields specified in `update_mask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Mask of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateTaskAsync(UpdateTaskRequest request)
    
    
    public final OperationFuture<Task,OperationMetadata> updateTaskAsync(UpdateTaskRequest request)

Update the task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       UpdateTaskRequest request =
           UpdateTaskRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTask(Task.newBuilder().build())
               .setValidateOnly(true)
               .build();
       Task response = dataplexServiceClient.updateTaskAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateTaskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateTaskCallable()
    
    
    public final UnaryCallable<UpdateTaskRequest,Operation> updateTaskCallable()

Update the task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       UpdateTaskRequest request =
           UpdateTaskRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTask(Task.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = dataplexServiceClient.updateTaskCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateTaskRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateTaskOperationCallable()
    
    
    public final OperationCallable<UpdateTaskRequest,Task,OperationMetadata> updateTaskOperationCallable()

Update the task resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       UpdateTaskRequest request =
           UpdateTaskRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setTask(Task.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<Task, OperationMetadata> future =
           dataplexServiceClient.updateTaskOperationCallable().futureCall(request);
       // Do something.
       Task response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateTaskRequest),[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Task),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateZoneAsync(UpdateZoneRequest request)
    
    
    public final OperationFuture<Zone,OperationMetadata> updateZoneAsync(UpdateZoneRequest request)

Updates a zone resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       UpdateZoneRequest request =
           UpdateZoneRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setZone(Zone.newBuilder().build())
               .setValidateOnly(true)
               .build();
       Zone response = dataplexServiceClient.updateZoneAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateZoneRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateZoneAsync(Zone zone, FieldMask updateMask)
    
    
    public final OperationFuture<Zone,OperationMetadata> updateZoneAsync(Zone zone, FieldMask updateMask)

Updates a zone resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       Zone zone = Zone.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Zone response = dataplexServiceClient.updateZoneAsync(zone, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`zone` | `[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Zone)`  
Required. Update description. Only fields specified in `update_mask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Mask of fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
### updateZoneCallable()
    
    
    public final UnaryCallable<UpdateZoneRequest,Operation> updateZoneCallable()

Updates a zone resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       UpdateZoneRequest request =
           UpdateZoneRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setZone(Zone.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = dataplexServiceClient.updateZoneCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateZoneRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateZoneOperationCallable()
    
    
    public final OperationCallable<UpdateZoneRequest,Zone,OperationMetadata> updateZoneOperationCallable()

Updates a zone resource.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (DataplexServiceClient dataplexServiceClient = DataplexServiceClient.create()) {
       UpdateZoneRequest request =
           UpdateZoneRequest.newBuilder()
               .setUpdateMask(FieldMask.newBuilder().build())
               .setZone(Zone.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<Zone, OperationMetadata> future =
           dataplexServiceClient.updateZoneOperationCallable().futureCall(request);
       // Do something.
       Zone response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateZoneRequest),[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
