---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildClient
title: Class CloudBuildClient (3.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:44:00.426915+00:00
---

# Class CloudBuildClient (3.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudBuildClient (3.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.101.0 (latest)  3.97.0  3.96.0  3.95.0  3.93.0  3.90.0  3.89.0  3.87.0  3.85.0  3.84.0  3.83.0  3.82.0  3.80.0  3.78.0  3.77.0  3.76.0  3.75.0  3.74.0  3.72.0  3.70.0  3.69.0  3.66.0  3.65.0  3.64.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.6  3.4.1  3.3.12 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-cloudbuild/google-cloud-build/src/main/java/com/google/cloud/devtools/cloudbuild/v1/CloudBuildClient.java)| [Product Reference](https://cloud.google.com/cloud-build/)  
---|---  
  
Service Description: Creates and manages builds on Google Cloud Platform.

The main concept used by this API is a `Build`, which describes the location of the source to build, how to build the source, and where to store the built artifacts, if any.

A user can list previously-requested builds or get builds by their ID to determine the status of the build.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       BuildName name = BuildName.ofProjectBuildName("[PROJECT]", "[BUILD]");
       Build response = cloudBuildClient.getBuild(name);
     }
     

Note: close() needs to be called on the CloudBuildClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateBuild |  Starts a build with the specified configuration.  This method returns a long-running `Operation`, which includes the build ID. Pass the build ID to `GetBuild` to determine the build status (such as `SUCCESS` or `FAILURE`). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createBuildAsync(CreateBuildRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createBuildAsync(LocationName parent) 
  * createBuildAsync(ProjectName parent) 
  * createBuildAsync(String parent) 
  * createBuildAsync(String projectId, Build build) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createBuildOperationCallable() 
  * createBuildCallable() 

  
GetBuild |  Returns information about a previously requested build.  The `Build` that is returned includes its status (such as `SUCCESS`, `FAILURE`, or `WORKING`), and timing information. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBuild(GetBuildRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBuild(BuildName name) 
  * getBuild(String name) 
  * getBuild(String projectId, String id) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBuildCallable() 

  
ListBuilds |  Lists previously requested builds.  Previously requested builds may still be in-progress, or may have finished successfully or unsuccessfully. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBuilds(ListBuildsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBuilds(String projectId, String filter) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBuildsPagedCallable() 
  * listBuildsCallable() 

  
CancelBuild |  Cancels a build in progress. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelBuild(CancelBuildRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * cancelBuild(BuildName name) 
  * cancelBuild(String name) 
  * cancelBuild(String projectId, String id) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelBuildCallable() 

  
RetryBuild |  Creates a new build based on the specified build.  This method creates a new build using the original build request, which may or may not result in an identical build.  For triggered builds: 

  * Triggered builds resolve to a precise revision; therefore a retry of a triggered build will result in a build that uses the same revision. 

For non-triggered builds that specify `RepoSource`: 

  * If the original build built from the tip of a branch, the retried build will build from the tip of that branch, which may not be the same revision as the original build. 
  * If the original build specified a commit sha or revision ID, the retried build will use the identical source. 

For builds that specify `StorageSource`: 

  * If the original build pulled source from Cloud Storage without specifying the generation of the object, the new build will use the current object, which may be different from the original build source. 
  * If the original build pulled source from Cloud Storage and specified the generation of the object, the new build will attempt to use the same object, which may or may not be available depending on the bucket's lifecycle management settings. 

|  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * retryBuildAsync(RetryBuildRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * retryBuildAsync(BuildName name) 
  * retryBuildAsync(String name) 
  * retryBuildAsync(String projectId, String id) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * retryBuildOperationCallable() 
  * retryBuildCallable() 

  
ApproveBuild |  Approves or rejects a pending build.  If approved, the returned long-running operation (LRO) will be analogous to the LRO returned from a CreateBuild call.  If rejected, the returned LRO will be immediately done. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * approveBuildAsync(ApproveBuildRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * approveBuildAsync(String name, ApprovalResult approvalResult) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * approveBuildOperationCallable() 
  * approveBuildCallable() 

  
CreateBuildTrigger |  Creates a new `BuildTrigger`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createBuildTrigger(CreateBuildTriggerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createBuildTrigger(LocationName parent) 
  * createBuildTrigger(ProjectName parent) 
  * createBuildTrigger(String parent) 
  * createBuildTrigger(String projectId, BuildTrigger trigger) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createBuildTriggerCallable() 

  
GetBuildTrigger |  Returns information about a `BuildTrigger`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getBuildTrigger(GetBuildTriggerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getBuildTrigger(BuildTriggerName name) 
  * getBuildTrigger(String name) 
  * getBuildTrigger(String projectId, String triggerId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getBuildTriggerCallable() 

  
ListBuildTriggers |  Lists existing `BuildTrigger`s. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listBuildTriggers(ListBuildTriggersRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listBuildTriggers(String projectId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listBuildTriggersPagedCallable() 
  * listBuildTriggersCallable() 

  
DeleteBuildTrigger |  Deletes a `BuildTrigger` by its project ID and trigger ID. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteBuildTrigger(DeleteBuildTriggerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteBuildTrigger(BuildTriggerName name) 
  * deleteBuildTrigger(String name) 
  * deleteBuildTrigger(String projectId, String triggerId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteBuildTriggerCallable() 

  
UpdateBuildTrigger |  Updates a `BuildTrigger` by its project ID and trigger ID. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateBuildTrigger(UpdateBuildTriggerRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateBuildTrigger(String projectId, String triggerId, BuildTrigger trigger) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateBuildTriggerCallable() 

  
RunBuildTrigger |  Runs a `BuildTrigger` at a particular source revision.  To run a regional or global trigger, use the POST request that includes the location endpoint in the path (ex. v1/projects/{projectId}/locations/{region}/triggers/{triggerId}:run). The POST request that does not include the location endpoint in the path can only be used when running global triggers. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * runBuildTriggerAsync(RunBuildTriggerRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * runBuildTriggerAsync(String projectId, String triggerId, RepoSource source) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * runBuildTriggerOperationCallable() 
  * runBuildTriggerCallable() 

  
ReceiveTriggerWebhook |  ReceiveTriggerWebhook [Experimental] is called when the API receives a webhook request targeted at a specific trigger. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * receiveTriggerWebhook(ReceiveTriggerWebhookRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * receiveTriggerWebhookCallable() 

  
CreateWorkerPool |  Creates a `WorkerPool`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createWorkerPoolAsync(CreateWorkerPoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createWorkerPoolAsync(LocationName parent, WorkerPool workerPool, String workerPoolId) 
  * createWorkerPoolAsync(String parent, WorkerPool workerPool, String workerPoolId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createWorkerPoolOperationCallable() 
  * createWorkerPoolCallable() 

  
GetWorkerPool |  Returns details of a `WorkerPool`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getWorkerPool(GetWorkerPoolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getWorkerPool(WorkerPoolName name) 
  * getWorkerPool(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getWorkerPoolCallable() 

  
DeleteWorkerPool |  Deletes a `WorkerPool`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteWorkerPoolAsync(DeleteWorkerPoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteWorkerPoolAsync(WorkerPoolName name) 
  * deleteWorkerPoolAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteWorkerPoolOperationCallable() 
  * deleteWorkerPoolCallable() 

  
UpdateWorkerPool |  Updates a `WorkerPool`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateWorkerPoolAsync(UpdateWorkerPoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateWorkerPoolAsync(WorkerPool workerPool, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateWorkerPoolOperationCallable() 
  * updateWorkerPoolCallable() 

  
ListWorkerPools |  Lists `WorkerPool`s. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listWorkerPools(ListWorkerPoolsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listWorkerPools(LocationName parent) 
  * listWorkerPools(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listWorkerPoolsPagedCallable() 
  * listWorkerPoolsCallable() 

  
GetDefaultServiceAccount |  Returns the `DefaultServiceAccount` used by the project. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getDefaultServiceAccount(GetDefaultServiceAccountRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getDefaultServiceAccount(DefaultServiceAccountName name) 
  * getDefaultServiceAccount(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getDefaultServiceAccountCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of CloudBuildSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudBuildSettings cloudBuildSettings =
         CloudBuildSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     CloudBuildClient cloudBuildClient = CloudBuildClient.create(cloudBuildSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudBuildSettings cloudBuildSettings =
         CloudBuildSettings.newBuilder().setEndpoint(myEndpoint).build();
     CloudBuildClient cloudBuildClient = CloudBuildClient.create(cloudBuildSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudBuildSettings cloudBuildSettings = CloudBuildSettings.newHttpJsonBuilder().build();
     CloudBuildClient cloudBuildClient = CloudBuildClient.create(cloudBuildSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > CloudBuildClient

## Static Methods 

### create()
    
    
    public static final CloudBuildClient create()

Constructs an instance of CloudBuildClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[CloudBuildClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CloudBuildSettings settings)
    
    
    public static final CloudBuildClient create(CloudBuildSettings settings)

Constructs an instance of CloudBuildClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CloudBuildSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudBuildClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CloudBuildStub stub)
    
    
    public static final CloudBuildClient create(CloudBuildStub stub)

Constructs an instance of CloudBuildClient, using the given stub for making calls. This is for advanced usage - prefer using create(CloudBuildSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CloudBuildStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.stub.CloudBuildStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudBuildClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildClient)` |   
  
## Constructors 

### CloudBuildClient(CloudBuildSettings settings)
    
    
    protected CloudBuildClient(CloudBuildSettings settings)

Constructs an instance of CloudBuildClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CloudBuildSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildSettings)`  
  
  
### CloudBuildClient(CloudBuildStub stub)
    
    
    protected CloudBuildClient(CloudBuildStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CloudBuildStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.stub.CloudBuildStub)`  
  
  
## Methods 

### approveBuildAsync(ApproveBuildRequest request)
    
    
    public final OperationFuture<Build,BuildOperationMetadata> approveBuildAsync(ApproveBuildRequest request)

Approves or rejects a pending build.

If approved, the returned long-running operation (LRO) will be analogous to the LRO returned from a CreateBuild call.

If rejected, the returned LRO will be immediately done.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       ApproveBuildRequest request =
           ApproveBuildRequest.newBuilder()
               .setName("name3373707")
               .setApprovalResult(ApprovalResult.newBuilder().build())
               .build();
       Build response = cloudBuildClient.approveBuildAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ApproveBuildRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ApproveBuildRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
### approveBuildAsync(String name, ApprovalResult approvalResult)
    
    
    public final OperationFuture<Build,BuildOperationMetadata> approveBuildAsync(String name, ApprovalResult approvalResult)

Approves or rejects a pending build.

If approved, the returned long-running operation (LRO) will be analogous to the LRO returned from a CreateBuild call.

If rejected, the returned LRO will be immediately done.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String name = "name3373707";
       ApprovalResult approvalResult = ApprovalResult.newBuilder().build();
       Build response = cloudBuildClient.approveBuildAsync(name, approvalResult).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the target build. For example: "projects/{$project_id}/builds/{$build_id}"  
`approvalResult` | `[ApprovalResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ApprovalResult)`  
Approval decision and metadata.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
### approveBuildCallable()
    
    
    public final UnaryCallable<ApproveBuildRequest,Operation> approveBuildCallable()

Approves or rejects a pending build.

If approved, the returned long-running operation (LRO) will be analogous to the LRO returned from a CreateBuild call.

If rejected, the returned LRO will be immediately done.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       ApproveBuildRequest request =
           ApproveBuildRequest.newBuilder()
               .setName("name3373707")
               .setApprovalResult(ApprovalResult.newBuilder().build())
               .build();
       ApiFuture<Operation> future = cloudBuildClient.approveBuildCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ApproveBuildRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ApproveBuildRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### approveBuildOperationCallable()
    
    
    public final OperationCallable<ApproveBuildRequest,Build,BuildOperationMetadata> approveBuildOperationCallable()

Approves or rejects a pending build.

If approved, the returned long-running operation (LRO) will be analogous to the LRO returned from a CreateBuild call.

If rejected, the returned LRO will be immediately done.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       ApproveBuildRequest request =
           ApproveBuildRequest.newBuilder()
               .setName("name3373707")
               .setApprovalResult(ApprovalResult.newBuilder().build())
               .build();
       OperationFuture<Build, BuildOperationMetadata> future =
           cloudBuildClient.approveBuildOperationCallable().futureCall(request);
       // Do something.
       Build response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ApproveBuildRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ApproveBuildRequest),[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
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
  
### cancelBuild(@Nullable BuildName name)
    
    
    public final Build cancelBuild(@Nullable BuildName name)

Cancels a build in progress.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       BuildName name = BuildName.ofProjectBuildName("[PROJECT]", "[BUILD]");
       Build response = cloudBuildClient.cancelBuild(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloudbuild.v1.BuildName`  
The name of the `Build` to cancel. Format: `projects/{project}/locations/{location}/builds/{build}`  
**Returns**  
---  
**Type** | **Description**  
`[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build)` |   
  
### cancelBuild(CancelBuildRequest request)
    
    
    public final Build cancelBuild(CancelBuildRequest request)

Cancels a build in progress.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       CancelBuildRequest request =
           CancelBuildRequest.newBuilder()
               .setName(BuildName.ofProjectBuildName("[PROJECT]", "[BUILD]").toString())
               .setProjectId("projectId-894832108")
               .setId("id3355")
               .build();
       Build response = cloudBuildClient.cancelBuild(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelBuildRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.CancelBuildRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build)` |   
  
### cancelBuild(String name)
    
    
    public final Build cancelBuild(String name)

Cancels a build in progress.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String name = BuildName.ofProjectBuildName("[PROJECT]", "[BUILD]").toString();
       Build response = cloudBuildClient.cancelBuild(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the `Build` to cancel. Format: `projects/{project}/locations/{location}/builds/{build}`  
**Returns**  
---  
**Type** | **Description**  
`[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build)` |   
  
### cancelBuild(String projectId, String id)
    
    
    public final Build cancelBuild(String projectId, String id)

Cancels a build in progress.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String projectId = "projectId-894832108";
       String id = "id3355";
       Build response = cloudBuildClient.cancelBuild(projectId, id);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the project.  
`id` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the build.  
**Returns**  
---  
**Type** | **Description**  
`[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build)` |   
  
### cancelBuildCallable()
    
    
    public final UnaryCallable<CancelBuildRequest,Build> cancelBuildCallable()

Cancels a build in progress.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       CancelBuildRequest request =
           CancelBuildRequest.newBuilder()
               .setName(BuildName.ofProjectBuildName("[PROJECT]", "[BUILD]").toString())
               .setProjectId("projectId-894832108")
               .setId("id3355")
               .build();
       ApiFuture<Build> future = cloudBuildClient.cancelBuildCallable().futureCall(request);
       // Do something.
       Build response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelBuildRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.CancelBuildRequest),[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build)>` |   
  
### close()
    
    
    public final void close()

### createBuildAsync(@Nullable LocationName parent)
    
    
    public final OperationFuture<Build,BuildOperationMetadata> createBuildAsync(@Nullable LocationName parent)

Starts a build with the specified configuration.

This method returns a long-running `Operation`, which includes the build ID. Pass the build ID to `GetBuild` to determine the build status (such as `SUCCESS` or `FAILURE`).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Build response = cloudBuildClient.createBuildAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloudbuild.v1.LocationName`  
The parent resource where this build will be created. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
### createBuildAsync(@Nullable ProjectName parent)
    
    
    public final OperationFuture<Build,BuildOperationMetadata> createBuildAsync(@Nullable ProjectName parent)

Starts a build with the specified configuration.

This method returns a long-running `Operation`, which includes the build ID. Pass the build ID to `GetBuild` to determine the build status (such as `SUCCESS` or `FAILURE`).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       Build response = cloudBuildClient.createBuildAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloudbuild.v1.ProjectName`  
The parent resource where this build will be created. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
### createBuildAsync(CreateBuildRequest request)
    
    
    public final OperationFuture<Build,BuildOperationMetadata> createBuildAsync(CreateBuildRequest request)

Starts a build with the specified configuration.

This method returns a long-running `Operation`, which includes the build ID. Pass the build ID to `GetBuild` to determine the build status (such as `SUCCESS` or `FAILURE`).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       CreateBuildRequest request =
           CreateBuildRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setProjectId("projectId-894832108")
               .setBuild(Build.newBuilder().build())
               .build();
       Build response = cloudBuildClient.createBuildAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBuildRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.CreateBuildRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
### createBuildAsync(String parent)
    
    
    public final OperationFuture<Build,BuildOperationMetadata> createBuildAsync(String parent)

Starts a build with the specified configuration.

This method returns a long-running `Operation`, which includes the build ID. Pass the build ID to `GetBuild` to determine the build status (such as `SUCCESS` or `FAILURE`).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       Build response = cloudBuildClient.createBuildAsync(parent).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The parent resource where this build will be created. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
### createBuildAsync(String projectId, Build build)
    
    
    public final OperationFuture<Build,BuildOperationMetadata> createBuildAsync(String projectId, Build build)

Starts a build with the specified configuration.

This method returns a long-running `Operation`, which includes the build ID. Pass the build ID to `GetBuild` to determine the build status (such as `SUCCESS` or `FAILURE`).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String projectId = "projectId-894832108";
       Build build = Build.newBuilder().build();
       Build response = cloudBuildClient.createBuildAsync(projectId, build).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the project.  
`build` | `[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build)`  
Required. Build resource to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
### createBuildCallable()
    
    
    public final UnaryCallable<CreateBuildRequest,Operation> createBuildCallable()

Starts a build with the specified configuration.

This method returns a long-running `Operation`, which includes the build ID. Pass the build ID to `GetBuild` to determine the build status (such as `SUCCESS` or `FAILURE`).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       CreateBuildRequest request =
           CreateBuildRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setProjectId("projectId-894832108")
               .setBuild(Build.newBuilder().build())
               .build();
       ApiFuture<Operation> future = cloudBuildClient.createBuildCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateBuildRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.CreateBuildRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createBuildOperationCallable()
    
    
    public final OperationCallable<CreateBuildRequest,Build,BuildOperationMetadata> createBuildOperationCallable()

Starts a build with the specified configuration.

This method returns a long-running `Operation`, which includes the build ID. Pass the build ID to `GetBuild` to determine the build status (such as `SUCCESS` or `FAILURE`).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       CreateBuildRequest request =
           CreateBuildRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setProjectId("projectId-894832108")
               .setBuild(Build.newBuilder().build())
               .build();
       OperationFuture<Build, BuildOperationMetadata> future =
           cloudBuildClient.createBuildOperationCallable().futureCall(request);
       // Do something.
       Build response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateBuildRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.CreateBuildRequest),[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
### createBuildTrigger(@Nullable LocationName parent)
    
    
    public final BuildTrigger createBuildTrigger(@Nullable LocationName parent)

Creates a new `BuildTrigger`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       BuildTrigger response = cloudBuildClient.createBuildTrigger(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloudbuild.v1.LocationName`  
The parent resource where this trigger will be created. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[BuildTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger)` |   
  
### createBuildTrigger(@Nullable ProjectName parent)
    
    
    public final BuildTrigger createBuildTrigger(@Nullable ProjectName parent)

Creates a new `BuildTrigger`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       ProjectName parent = ProjectName.of("[PROJECT]");
       BuildTrigger response = cloudBuildClient.createBuildTrigger(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloudbuild.v1.ProjectName`  
The parent resource where this trigger will be created. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[BuildTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger)` |   
  
### createBuildTrigger(CreateBuildTriggerRequest request)
    
    
    public final BuildTrigger createBuildTrigger(CreateBuildTriggerRequest request)

Creates a new `BuildTrigger`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       CreateBuildTriggerRequest request =
           CreateBuildTriggerRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setProjectId("projectId-894832108")
               .setTrigger(BuildTrigger.newBuilder().build())
               .build();
       BuildTrigger response = cloudBuildClient.createBuildTrigger(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBuildTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.CreateBuildTriggerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BuildTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger)` |   
  
### createBuildTrigger(String parent)
    
    
    public final BuildTrigger createBuildTrigger(String parent)

Creates a new `BuildTrigger`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String parent = ProjectName.of("[PROJECT]").toString();
       BuildTrigger response = cloudBuildClient.createBuildTrigger(parent);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The parent resource where this trigger will be created. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[BuildTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger)` |   
  
### createBuildTrigger(String projectId, BuildTrigger trigger)
    
    
    public final BuildTrigger createBuildTrigger(String projectId, BuildTrigger trigger)

Creates a new `BuildTrigger`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String projectId = "projectId-894832108";
       BuildTrigger trigger = BuildTrigger.newBuilder().build();
       BuildTrigger response = cloudBuildClient.createBuildTrigger(projectId, trigger);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the project for which to configure automatic builds.  
`trigger` | `[BuildTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger)`  
Required. `BuildTrigger` to create.  
**Returns**  
---  
**Type** | **Description**  
`[BuildTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger)` |   
  
### createBuildTriggerCallable()
    
    
    public final UnaryCallable<CreateBuildTriggerRequest,BuildTrigger> createBuildTriggerCallable()

Creates a new `BuildTrigger`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       CreateBuildTriggerRequest request =
           CreateBuildTriggerRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setProjectId("projectId-894832108")
               .setTrigger(BuildTrigger.newBuilder().build())
               .build();
       ApiFuture<BuildTrigger> future =
           cloudBuildClient.createBuildTriggerCallable().futureCall(request);
       // Do something.
       BuildTrigger response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateBuildTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.CreateBuildTriggerRequest),[BuildTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger)>` |   
  
### createWorkerPoolAsync(@Nullable LocationName parent, WorkerPool workerPool, String workerPoolId)
    
    
    public final OperationFuture<WorkerPool,CreateWorkerPoolOperationMetadata> createWorkerPoolAsync(@Nullable LocationName parent, WorkerPool workerPool, String workerPoolId)

Creates a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       WorkerPool workerPool = WorkerPool.newBuilder().build();
       String workerPoolId = "workerPoolId-46320779";
       WorkerPool response =
           cloudBuildClient.createWorkerPoolAsync(parent, workerPool, workerPoolId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloudbuild.v1.LocationName`  
Required. The parent resource where this worker pool will be created. Format: `projects/{project}/locations/{location}`.  
`workerPool` | `[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.WorkerPool)`  
Required. `WorkerPool` resource to create.  
`workerPoolId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Immutable. The ID to use for the `WorkerPool`, which will become the final component of the resource name. This value should be 1-63 characters, and valid characters are /a-z-/.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.WorkerPool),[CreateWorkerPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.CreateWorkerPoolOperationMetadata)>` |   
  
### createWorkerPoolAsync(CreateWorkerPoolRequest request)
    
    
    public final OperationFuture<WorkerPool,CreateWorkerPoolOperationMetadata> createWorkerPoolAsync(CreateWorkerPoolRequest request)

Creates a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       CreateWorkerPoolRequest request =
           CreateWorkerPoolRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setWorkerPool(WorkerPool.newBuilder().build())
               .setWorkerPoolId("workerPoolId-46320779")
               .setValidateOnly(true)
               .build();
       WorkerPool response = cloudBuildClient.createWorkerPoolAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateWorkerPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.CreateWorkerPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.WorkerPool),[CreateWorkerPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.CreateWorkerPoolOperationMetadata)>` |   
  
### createWorkerPoolAsync(String parent, WorkerPool workerPool, String workerPoolId)
    
    
    public final OperationFuture<WorkerPool,CreateWorkerPoolOperationMetadata> createWorkerPoolAsync(String parent, WorkerPool workerPool, String workerPoolId)

Creates a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       WorkerPool workerPool = WorkerPool.newBuilder().build();
       String workerPoolId = "workerPoolId-46320779";
       WorkerPool response =
           cloudBuildClient.createWorkerPoolAsync(parent, workerPool, workerPoolId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource where this worker pool will be created. Format: `projects/{project}/locations/{location}`.  
`workerPool` | `[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.WorkerPool)`  
Required. `WorkerPool` resource to create.  
`workerPoolId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Immutable. The ID to use for the `WorkerPool`, which will become the final component of the resource name. This value should be 1-63 characters, and valid characters are /a-z-/.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.WorkerPool),[CreateWorkerPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.CreateWorkerPoolOperationMetadata)>` |   
  
### createWorkerPoolCallable()
    
    
    public final UnaryCallable<CreateWorkerPoolRequest,Operation> createWorkerPoolCallable()

Creates a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       CreateWorkerPoolRequest request =
           CreateWorkerPoolRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setWorkerPool(WorkerPool.newBuilder().build())
               .setWorkerPoolId("workerPoolId-46320779")
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = cloudBuildClient.createWorkerPoolCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateWorkerPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.CreateWorkerPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createWorkerPoolOperationCallable()
    
    
    public final OperationCallable<CreateWorkerPoolRequest,WorkerPool,CreateWorkerPoolOperationMetadata> createWorkerPoolOperationCallable()

Creates a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       CreateWorkerPoolRequest request =
           CreateWorkerPoolRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setWorkerPool(WorkerPool.newBuilder().build())
               .setWorkerPoolId("workerPoolId-46320779")
               .setValidateOnly(true)
               .build();
       OperationFuture<WorkerPool, CreateWorkerPoolOperationMetadata> future =
           cloudBuildClient.createWorkerPoolOperationCallable().futureCall(request);
       // Do something.
       WorkerPool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateWorkerPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.CreateWorkerPoolRequest),[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.WorkerPool),[CreateWorkerPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.CreateWorkerPoolOperationMetadata)>` |   
  
### deleteBuildTrigger(@Nullable BuildTriggerName name)
    
    
    public final void deleteBuildTrigger(@Nullable BuildTriggerName name)

Deletes a `BuildTrigger` by its project ID and trigger ID.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       BuildTriggerName name = BuildTriggerName.ofProjectTriggerName("[PROJECT]", "[TRIGGER]");
       cloudBuildClient.deleteBuildTrigger(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloudbuild.v1.BuildTriggerName`  
The name of the `Trigger` to delete. Format: `projects/{project}/locations/{location}/triggers/{trigger}`  
  
### deleteBuildTrigger(DeleteBuildTriggerRequest request)
    
    
    public final void deleteBuildTrigger(DeleteBuildTriggerRequest request)

Deletes a `BuildTrigger` by its project ID and trigger ID.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       DeleteBuildTriggerRequest request =
           DeleteBuildTriggerRequest.newBuilder()
               .setName(BuildTriggerName.ofProjectTriggerName("[PROJECT]", "[TRIGGER]").toString())
               .setProjectId("projectId-894832108")
               .setTriggerId("triggerId-648752909")
               .build();
       cloudBuildClient.deleteBuildTrigger(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBuildTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.DeleteBuildTriggerRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteBuildTrigger(String name)
    
    
    public final void deleteBuildTrigger(String name)

Deletes a `BuildTrigger` by its project ID and trigger ID.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String name = BuildTriggerName.ofProjectTriggerName("[PROJECT]", "[TRIGGER]").toString();
       cloudBuildClient.deleteBuildTrigger(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the `Trigger` to delete. Format: `projects/{project}/locations/{location}/triggers/{trigger}`  
  
### deleteBuildTrigger(String projectId, String triggerId)
    
    
    public final void deleteBuildTrigger(String projectId, String triggerId)

Deletes a `BuildTrigger` by its project ID and trigger ID.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String projectId = "projectId-894832108";
       String triggerId = "triggerId-648752909";
       cloudBuildClient.deleteBuildTrigger(projectId, triggerId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the project that owns the trigger.  
`triggerId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the `BuildTrigger` to delete.  
  
### deleteBuildTriggerCallable()
    
    
    public final UnaryCallable<DeleteBuildTriggerRequest,Empty> deleteBuildTriggerCallable()

Deletes a `BuildTrigger` by its project ID and trigger ID.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       DeleteBuildTriggerRequest request =
           DeleteBuildTriggerRequest.newBuilder()
               .setName(BuildTriggerName.ofProjectTriggerName("[PROJECT]", "[TRIGGER]").toString())
               .setProjectId("projectId-894832108")
               .setTriggerId("triggerId-648752909")
               .build();
       ApiFuture<Empty> future = cloudBuildClient.deleteBuildTriggerCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteBuildTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.DeleteBuildTriggerRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteWorkerPoolAsync(@Nullable WorkerPoolName name)
    
    
    public final OperationFuture<Empty,DeleteWorkerPoolOperationMetadata> deleteWorkerPoolAsync(@Nullable WorkerPoolName name)

Deletes a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       WorkerPoolName name = WorkerPoolName.of("[PROJECT]", "[LOCATION]", "[WORKER_POOL]");
       cloudBuildClient.deleteWorkerPoolAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloudbuild.v1.WorkerPoolName`  
Required. The name of the `WorkerPool` to delete. Format: `projects/{project}/locations/{location}/workerPools/{workerPool}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteWorkerPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.DeleteWorkerPoolOperationMetadata)>` |   
  
### deleteWorkerPoolAsync(DeleteWorkerPoolRequest request)
    
    
    public final OperationFuture<Empty,DeleteWorkerPoolOperationMetadata> deleteWorkerPoolAsync(DeleteWorkerPoolRequest request)

Deletes a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       DeleteWorkerPoolRequest request =
           DeleteWorkerPoolRequest.newBuilder()
               .setName(WorkerPoolName.of("[PROJECT]", "[LOCATION]", "[WORKER_POOL]").toString())
               .setEtag("etag3123477")
               .setAllowMissing(true)
               .setValidateOnly(true)
               .build();
       cloudBuildClient.deleteWorkerPoolAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkerPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.DeleteWorkerPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteWorkerPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.DeleteWorkerPoolOperationMetadata)>` |   
  
### deleteWorkerPoolAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteWorkerPoolOperationMetadata> deleteWorkerPoolAsync(String name)

Deletes a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String name = WorkerPoolName.of("[PROJECT]", "[LOCATION]", "[WORKER_POOL]").toString();
       cloudBuildClient.deleteWorkerPoolAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `WorkerPool` to delete. Format: `projects/{project}/locations/{location}/workerPools/{workerPool}`.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteWorkerPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.DeleteWorkerPoolOperationMetadata)>` |   
  
### deleteWorkerPoolCallable()
    
    
    public final UnaryCallable<DeleteWorkerPoolRequest,Operation> deleteWorkerPoolCallable()

Deletes a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       DeleteWorkerPoolRequest request =
           DeleteWorkerPoolRequest.newBuilder()
               .setName(WorkerPoolName.of("[PROJECT]", "[LOCATION]", "[WORKER_POOL]").toString())
               .setEtag("etag3123477")
               .setAllowMissing(true)
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = cloudBuildClient.deleteWorkerPoolCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteWorkerPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.DeleteWorkerPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteWorkerPoolOperationCallable()
    
    
    public final OperationCallable<DeleteWorkerPoolRequest,Empty,DeleteWorkerPoolOperationMetadata> deleteWorkerPoolOperationCallable()

Deletes a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       DeleteWorkerPoolRequest request =
           DeleteWorkerPoolRequest.newBuilder()
               .setName(WorkerPoolName.of("[PROJECT]", "[LOCATION]", "[WORKER_POOL]").toString())
               .setEtag("etag3123477")
               .setAllowMissing(true)
               .setValidateOnly(true)
               .build();
       OperationFuture<Empty, DeleteWorkerPoolOperationMetadata> future =
           cloudBuildClient.deleteWorkerPoolOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteWorkerPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.DeleteWorkerPoolRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteWorkerPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.DeleteWorkerPoolOperationMetadata)>` |   
  
### getBuild(@Nullable BuildName name)
    
    
    public final Build getBuild(@Nullable BuildName name)

Returns information about a previously requested build.

The `Build` that is returned includes its status (such as `SUCCESS`, `FAILURE`, or `WORKING`), and timing information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       BuildName name = BuildName.ofProjectBuildName("[PROJECT]", "[BUILD]");
       Build response = cloudBuildClient.getBuild(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloudbuild.v1.BuildName`  
The name of the `Build` to retrieve. Format: `projects/{project}/locations/{location}/builds/{build}`  
**Returns**  
---  
**Type** | **Description**  
`[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build)` |   
  
### getBuild(GetBuildRequest request)
    
    
    public final Build getBuild(GetBuildRequest request)

Returns information about a previously requested build.

The `Build` that is returned includes its status (such as `SUCCESS`, `FAILURE`, or `WORKING`), and timing information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       GetBuildRequest request =
           GetBuildRequest.newBuilder()
               .setName(BuildName.ofProjectBuildName("[PROJECT]", "[BUILD]").toString())
               .setProjectId("projectId-894832108")
               .setId("id3355")
               .build();
       Build response = cloudBuildClient.getBuild(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBuildRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.GetBuildRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build)` |   
  
### getBuild(String name)
    
    
    public final Build getBuild(String name)

Returns information about a previously requested build.

The `Build` that is returned includes its status (such as `SUCCESS`, `FAILURE`, or `WORKING`), and timing information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String name = BuildName.ofProjectBuildName("[PROJECT]", "[BUILD]").toString();
       Build response = cloudBuildClient.getBuild(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the `Build` to retrieve. Format: `projects/{project}/locations/{location}/builds/{build}`  
**Returns**  
---  
**Type** | **Description**  
`[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build)` |   
  
### getBuild(String projectId, String id)
    
    
    public final Build getBuild(String projectId, String id)

Returns information about a previously requested build.

The `Build` that is returned includes its status (such as `SUCCESS`, `FAILURE`, or `WORKING`), and timing information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String projectId = "projectId-894832108";
       String id = "id3355";
       Build response = cloudBuildClient.getBuild(projectId, id);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the project.  
`id` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the build.  
**Returns**  
---  
**Type** | **Description**  
`[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build)` |   
  
### getBuildCallable()
    
    
    public final UnaryCallable<GetBuildRequest,Build> getBuildCallable()

Returns information about a previously requested build.

The `Build` that is returned includes its status (such as `SUCCESS`, `FAILURE`, or `WORKING`), and timing information.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       GetBuildRequest request =
           GetBuildRequest.newBuilder()
               .setName(BuildName.ofProjectBuildName("[PROJECT]", "[BUILD]").toString())
               .setProjectId("projectId-894832108")
               .setId("id3355")
               .build();
       ApiFuture<Build> future = cloudBuildClient.getBuildCallable().futureCall(request);
       // Do something.
       Build response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBuildRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.GetBuildRequest),[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build)>` |   
  
### getBuildTrigger(@Nullable BuildTriggerName name)
    
    
    public final BuildTrigger getBuildTrigger(@Nullable BuildTriggerName name)

Returns information about a `BuildTrigger`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       BuildTriggerName name = BuildTriggerName.ofProjectTriggerName("[PROJECT]", "[TRIGGER]");
       BuildTrigger response = cloudBuildClient.getBuildTrigger(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloudbuild.v1.BuildTriggerName`  
The name of the `Trigger` to retrieve. Format: `projects/{project}/locations/{location}/triggers/{trigger}`  
**Returns**  
---  
**Type** | **Description**  
`[BuildTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger)` |   
  
### getBuildTrigger(GetBuildTriggerRequest request)
    
    
    public final BuildTrigger getBuildTrigger(GetBuildTriggerRequest request)

Returns information about a `BuildTrigger`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       GetBuildTriggerRequest request =
           GetBuildTriggerRequest.newBuilder()
               .setName(BuildTriggerName.ofProjectTriggerName("[PROJECT]", "[TRIGGER]").toString())
               .setProjectId("projectId-894832108")
               .setTriggerId("triggerId-648752909")
               .build();
       BuildTrigger response = cloudBuildClient.getBuildTrigger(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBuildTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.GetBuildTriggerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BuildTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger)` |   
  
### getBuildTrigger(String name)
    
    
    public final BuildTrigger getBuildTrigger(String name)

Returns information about a `BuildTrigger`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String name = BuildTriggerName.ofProjectTriggerName("[PROJECT]", "[TRIGGER]").toString();
       BuildTrigger response = cloudBuildClient.getBuildTrigger(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the `Trigger` to retrieve. Format: `projects/{project}/locations/{location}/triggers/{trigger}`  
**Returns**  
---  
**Type** | **Description**  
`[BuildTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger)` |   
  
### getBuildTrigger(String projectId, String triggerId)
    
    
    public final BuildTrigger getBuildTrigger(String projectId, String triggerId)

Returns information about a `BuildTrigger`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String projectId = "projectId-894832108";
       String triggerId = "triggerId-648752909";
       BuildTrigger response = cloudBuildClient.getBuildTrigger(projectId, triggerId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the project that owns the trigger.  
`triggerId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Identifier (`id` or `name`) of the `BuildTrigger` to get.  
**Returns**  
---  
**Type** | **Description**  
`[BuildTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger)` |   
  
### getBuildTriggerCallable()
    
    
    public final UnaryCallable<GetBuildTriggerRequest,BuildTrigger> getBuildTriggerCallable()

Returns information about a `BuildTrigger`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       GetBuildTriggerRequest request =
           GetBuildTriggerRequest.newBuilder()
               .setName(BuildTriggerName.ofProjectTriggerName("[PROJECT]", "[TRIGGER]").toString())
               .setProjectId("projectId-894832108")
               .setTriggerId("triggerId-648752909")
               .build();
       ApiFuture<BuildTrigger> future =
           cloudBuildClient.getBuildTriggerCallable().futureCall(request);
       // Do something.
       BuildTrigger response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetBuildTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.GetBuildTriggerRequest),[BuildTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger)>` |   
  
### getDefaultServiceAccount(@Nullable DefaultServiceAccountName name)
    
    
    public final DefaultServiceAccount getDefaultServiceAccount(@Nullable DefaultServiceAccountName name)

Returns the `DefaultServiceAccount` used by the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       DefaultServiceAccountName name = DefaultServiceAccountName.of("[PROJECT]", "[LOCATION]");
       DefaultServiceAccount response = cloudBuildClient.getDefaultServiceAccount(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloudbuild.v1.DefaultServiceAccountName`  
Required. The name of the `DefaultServiceAccount` to retrieve. Format: `projects/{project}/locations/{location}/defaultServiceAccount`  
**Returns**  
---  
**Type** | **Description**  
`[DefaultServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.DefaultServiceAccount)` |   
  
### getDefaultServiceAccount(GetDefaultServiceAccountRequest request)
    
    
    public final DefaultServiceAccount getDefaultServiceAccount(GetDefaultServiceAccountRequest request)

Returns the `DefaultServiceAccount` used by the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       GetDefaultServiceAccountRequest request =
           GetDefaultServiceAccountRequest.newBuilder()
               .setName(DefaultServiceAccountName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       DefaultServiceAccount response = cloudBuildClient.getDefaultServiceAccount(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDefaultServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.GetDefaultServiceAccountRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[DefaultServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.DefaultServiceAccount)` |   
  
### getDefaultServiceAccount(String name)
    
    
    public final DefaultServiceAccount getDefaultServiceAccount(String name)

Returns the `DefaultServiceAccount` used by the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String name = DefaultServiceAccountName.of("[PROJECT]", "[LOCATION]").toString();
       DefaultServiceAccount response = cloudBuildClient.getDefaultServiceAccount(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `DefaultServiceAccount` to retrieve. Format: `projects/{project}/locations/{location}/defaultServiceAccount`  
**Returns**  
---  
**Type** | **Description**  
`[DefaultServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.DefaultServiceAccount)` |   
  
### getDefaultServiceAccountCallable()
    
    
    public final UnaryCallable<GetDefaultServiceAccountRequest,DefaultServiceAccount> getDefaultServiceAccountCallable()

Returns the `DefaultServiceAccount` used by the project.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       GetDefaultServiceAccountRequest request =
           GetDefaultServiceAccountRequest.newBuilder()
               .setName(DefaultServiceAccountName.of("[PROJECT]", "[LOCATION]").toString())
               .build();
       ApiFuture<DefaultServiceAccount> future =
           cloudBuildClient.getDefaultServiceAccountCallable().futureCall(request);
       // Do something.
       DefaultServiceAccount response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetDefaultServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.GetDefaultServiceAccountRequest),[DefaultServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.DefaultServiceAccount)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getOperationsClient()
    
    
    public final OperationsClient getOperationsClient()

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationsClient.html)` |   
  
### getSettings()
    
    
    public final @Nullable CloudBuildSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.devtools.cloudbuild.v1.CloudBuildSettings` |   
  
### getStub()
    
    
    public CloudBuildStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[CloudBuildStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.stub.CloudBuildStub)` |   
  
### getWorkerPool(@Nullable WorkerPoolName name)
    
    
    public final WorkerPool getWorkerPool(@Nullable WorkerPoolName name)

Returns details of a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       WorkerPoolName name = WorkerPoolName.of("[PROJECT]", "[LOCATION]", "[WORKER_POOL]");
       WorkerPool response = cloudBuildClient.getWorkerPool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloudbuild.v1.WorkerPoolName`  
Required. The name of the `WorkerPool` to retrieve. Format: `projects/{project}/locations/{location}/workerPools/{workerPool}`.  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.WorkerPool)` |   
  
### getWorkerPool(GetWorkerPoolRequest request)
    
    
    public final WorkerPool getWorkerPool(GetWorkerPoolRequest request)

Returns details of a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       GetWorkerPoolRequest request =
           GetWorkerPoolRequest.newBuilder()
               .setName(WorkerPoolName.of("[PROJECT]", "[LOCATION]", "[WORKER_POOL]").toString())
               .build();
       WorkerPool response = cloudBuildClient.getWorkerPool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetWorkerPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.GetWorkerPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.WorkerPool)` |   
  
### getWorkerPool(String name)
    
    
    public final WorkerPool getWorkerPool(String name)

Returns details of a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String name = WorkerPoolName.of("[PROJECT]", "[LOCATION]", "[WORKER_POOL]").toString();
       WorkerPool response = cloudBuildClient.getWorkerPool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the `WorkerPool` to retrieve. Format: `projects/{project}/locations/{location}/workerPools/{workerPool}`.  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.WorkerPool)` |   
  
### getWorkerPoolCallable()
    
    
    public final UnaryCallable<GetWorkerPoolRequest,WorkerPool> getWorkerPoolCallable()

Returns details of a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       GetWorkerPoolRequest request =
           GetWorkerPoolRequest.newBuilder()
               .setName(WorkerPoolName.of("[PROJECT]", "[LOCATION]", "[WORKER_POOL]").toString())
               .build();
       ApiFuture<WorkerPool> future = cloudBuildClient.getWorkerPoolCallable().futureCall(request);
       // Do something.
       WorkerPool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetWorkerPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.GetWorkerPoolRequest),[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.WorkerPool)>` |   
  
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
  
### listBuildTriggers(ListBuildTriggersRequest request)
    
    
    public final CloudBuildClient.ListBuildTriggersPagedResponse listBuildTriggers(ListBuildTriggersRequest request)

Lists existing `BuildTrigger`s.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       ListBuildTriggersRequest request =
           ListBuildTriggersRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setProjectId("projectId-894832108")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (BuildTrigger element : cloudBuildClient.listBuildTriggers(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBuildTriggersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ListBuildTriggersRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudBuildClient.ListBuildTriggersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildClient.ListBuildTriggersPagedResponse)` |   
  
### listBuildTriggers(String projectId)
    
    
    public final CloudBuildClient.ListBuildTriggersPagedResponse listBuildTriggers(String projectId)

Lists existing `BuildTrigger`s.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String projectId = "projectId-894832108";
       for (BuildTrigger element : cloudBuildClient.listBuildTriggers(projectId).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the project for which to list BuildTriggers.  
**Returns**  
---  
**Type** | **Description**  
`[CloudBuildClient.ListBuildTriggersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildClient.ListBuildTriggersPagedResponse)` |   
  
### listBuildTriggersCallable()
    
    
    public final UnaryCallable<ListBuildTriggersRequest,ListBuildTriggersResponse> listBuildTriggersCallable()

Lists existing `BuildTrigger`s.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       ListBuildTriggersRequest request =
           ListBuildTriggersRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setProjectId("projectId-894832108")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListBuildTriggersResponse response =
             cloudBuildClient.listBuildTriggersCallable().call(request);
         for (BuildTrigger element : response.getTriggersList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBuildTriggersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ListBuildTriggersRequest),[ListBuildTriggersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ListBuildTriggersResponse)>` |   
  
### listBuildTriggersPagedCallable()
    
    
    public final UnaryCallable<ListBuildTriggersRequest,CloudBuildClient.ListBuildTriggersPagedResponse> listBuildTriggersPagedCallable()

Lists existing `BuildTrigger`s.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       ListBuildTriggersRequest request =
           ListBuildTriggersRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setProjectId("projectId-894832108")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<BuildTrigger> future =
           cloudBuildClient.listBuildTriggersPagedCallable().futureCall(request);
       // Do something.
       for (BuildTrigger element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBuildTriggersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ListBuildTriggersRequest),[ListBuildTriggersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildClient.ListBuildTriggersPagedResponse)>` |   
  
### listBuilds(ListBuildsRequest request)
    
    
    public final CloudBuildClient.ListBuildsPagedResponse listBuilds(ListBuildsRequest request)

Lists previously requested builds.

Previously requested builds may still be in-progress, or may have finished successfully or unsuccessfully.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       ListBuildsRequest request =
           ListBuildsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setProjectId("projectId-894832108")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Build element : cloudBuildClient.listBuilds(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBuildsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ListBuildsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudBuildClient.ListBuildsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildClient.ListBuildsPagedResponse)` |   
  
### listBuilds(String projectId, String filter)
    
    
    public final CloudBuildClient.ListBuildsPagedResponse listBuilds(String projectId, String filter)

Lists previously requested builds.

Previously requested builds may still be in-progress, or may have finished successfully or unsuccessfully.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String projectId = "projectId-894832108";
       String filter = "filter-1274492040";
       for (Build element : cloudBuildClient.listBuilds(projectId, filter).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the project.  
`filter` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The raw filter text to constrain the results.  
**Returns**  
---  
**Type** | **Description**  
`[CloudBuildClient.ListBuildsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildClient.ListBuildsPagedResponse)` |   
  
### listBuildsCallable()
    
    
    public final UnaryCallable<ListBuildsRequest,ListBuildsResponse> listBuildsCallable()

Lists previously requested builds.

Previously requested builds may still be in-progress, or may have finished successfully or unsuccessfully.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       ListBuildsRequest request =
           ListBuildsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setProjectId("projectId-894832108")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListBuildsResponse response = cloudBuildClient.listBuildsCallable().call(request);
         for (Build element : response.getBuildsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBuildsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ListBuildsRequest),[ListBuildsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ListBuildsResponse)>` |   
  
### listBuildsPagedCallable()
    
    
    public final UnaryCallable<ListBuildsRequest,CloudBuildClient.ListBuildsPagedResponse> listBuildsPagedCallable()

Lists previously requested builds.

Previously requested builds may still be in-progress, or may have finished successfully or unsuccessfully.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       ListBuildsRequest request =
           ListBuildsRequest.newBuilder()
               .setParent(ProjectName.of("[PROJECT]").toString())
               .setProjectId("projectId-894832108")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Build> future = cloudBuildClient.listBuildsPagedCallable().futureCall(request);
       // Do something.
       for (Build element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListBuildsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ListBuildsRequest),[ListBuildsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildClient.ListBuildsPagedResponse)>` |   
  
### listWorkerPools(@Nullable LocationName parent)
    
    
    public final CloudBuildClient.ListWorkerPoolsPagedResponse listWorkerPools(@Nullable LocationName parent)

Lists `WorkerPool`s.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (WorkerPool element : cloudBuildClient.listWorkerPools(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloudbuild.v1.LocationName`  
Required. The parent of the collection of `WorkerPools`. Format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[CloudBuildClient.ListWorkerPoolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildClient.ListWorkerPoolsPagedResponse)` |   
  
### listWorkerPools(ListWorkerPoolsRequest request)
    
    
    public final CloudBuildClient.ListWorkerPoolsPagedResponse listWorkerPools(ListWorkerPoolsRequest request)

Lists `WorkerPool`s.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       ListWorkerPoolsRequest request =
           ListWorkerPoolsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (WorkerPool element : cloudBuildClient.listWorkerPools(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListWorkerPoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ListWorkerPoolsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CloudBuildClient.ListWorkerPoolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildClient.ListWorkerPoolsPagedResponse)` |   
  
### listWorkerPools(String parent)
    
    
    public final CloudBuildClient.ListWorkerPoolsPagedResponse listWorkerPools(String parent)

Lists `WorkerPool`s.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (WorkerPool element : cloudBuildClient.listWorkerPools(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent of the collection of `WorkerPools`. Format: `projects/{project}/locations/{location}`.  
**Returns**  
---  
**Type** | **Description**  
`[CloudBuildClient.ListWorkerPoolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildClient.ListWorkerPoolsPagedResponse)` |   
  
### listWorkerPoolsCallable()
    
    
    public final UnaryCallable<ListWorkerPoolsRequest,ListWorkerPoolsResponse> listWorkerPoolsCallable()

Lists `WorkerPool`s.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       ListWorkerPoolsRequest request =
           ListWorkerPoolsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListWorkerPoolsResponse response = cloudBuildClient.listWorkerPoolsCallable().call(request);
         for (WorkerPool element : response.getWorkerPoolsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWorkerPoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ListWorkerPoolsRequest),[ListWorkerPoolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ListWorkerPoolsResponse)>` |   
  
### listWorkerPoolsPagedCallable()
    
    
    public final UnaryCallable<ListWorkerPoolsRequest,CloudBuildClient.ListWorkerPoolsPagedResponse> listWorkerPoolsPagedCallable()

Lists `WorkerPool`s.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       ListWorkerPoolsRequest request =
           ListWorkerPoolsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<WorkerPool> future =
           cloudBuildClient.listWorkerPoolsPagedCallable().futureCall(request);
       // Do something.
       for (WorkerPool element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListWorkerPoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ListWorkerPoolsRequest),[ListWorkerPoolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloud.devtools.cloudbuild.v1.CloudBuildClient.ListWorkerPoolsPagedResponse)>` |   
  
### receiveTriggerWebhook(ReceiveTriggerWebhookRequest request)
    
    
    public final ReceiveTriggerWebhookResponse receiveTriggerWebhook(ReceiveTriggerWebhookRequest request)

ReceiveTriggerWebhook [Experimental] is called when the API receives a webhook request targeted at a specific trigger.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       ReceiveTriggerWebhookRequest request =
           ReceiveTriggerWebhookRequest.newBuilder()
               .setName("name3373707")
               .setBody(HttpBody.newBuilder().build())
               .setProjectId("projectId-894832108")
               .setTrigger("trigger-1059891784")
               .setSecret("secret-906277200")
               .build();
       ReceiveTriggerWebhookResponse response = cloudBuildClient.receiveTriggerWebhook(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReceiveTriggerWebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ReceiveTriggerWebhookRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReceiveTriggerWebhookResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ReceiveTriggerWebhookResponse)` |   
  
### receiveTriggerWebhookCallable()
    
    
    public final UnaryCallable<ReceiveTriggerWebhookRequest,ReceiveTriggerWebhookResponse> receiveTriggerWebhookCallable()

ReceiveTriggerWebhook [Experimental] is called when the API receives a webhook request targeted at a specific trigger.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       ReceiveTriggerWebhookRequest request =
           ReceiveTriggerWebhookRequest.newBuilder()
               .setName("name3373707")
               .setBody(HttpBody.newBuilder().build())
               .setProjectId("projectId-894832108")
               .setTrigger("trigger-1059891784")
               .setSecret("secret-906277200")
               .build();
       ApiFuture<ReceiveTriggerWebhookResponse> future =
           cloudBuildClient.receiveTriggerWebhookCallable().futureCall(request);
       // Do something.
       ReceiveTriggerWebhookResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ReceiveTriggerWebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ReceiveTriggerWebhookRequest),[ReceiveTriggerWebhookResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ReceiveTriggerWebhookResponse)>` |   
  
### retryBuildAsync(@Nullable BuildName name)
    
    
    public final OperationFuture<Build,BuildOperationMetadata> retryBuildAsync(@Nullable BuildName name)

Creates a new build based on the specified build.

This method creates a new build using the original build request, which may or may not result in an identical build.

For triggered builds:

  * Triggered builds resolve to a precise revision; therefore a retry of a triggered build will result in a build that uses the same revision. 



For non-triggered builds that specify `RepoSource`:

  * If the original build built from the tip of a branch, the retried build will build from the tip of that branch, which may not be the same revision as the original build. 
  * If the original build specified a commit sha or revision ID, the retried build will use the identical source. 



For builds that specify `StorageSource`:

  * If the original build pulled source from Cloud Storage without specifying the generation of the object, the new build will use the current object, which may be different from the original build source. 
  * If the original build pulled source from Cloud Storage and specified the generation of the object, the new build will attempt to use the same object, which may or may not be available depending on the bucket's lifecycle management settings. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       BuildName name = BuildName.ofProjectBuildName("[PROJECT]", "[BUILD]");
       Build response = cloudBuildClient.retryBuildAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloudbuild.v1.BuildName`  
The name of the `Build` to retry. Format: `projects/{project}/locations/{location}/builds/{build}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
### retryBuildAsync(RetryBuildRequest request)
    
    
    public final OperationFuture<Build,BuildOperationMetadata> retryBuildAsync(RetryBuildRequest request)

Creates a new build based on the specified build.

This method creates a new build using the original build request, which may or may not result in an identical build.

For triggered builds:

  * Triggered builds resolve to a precise revision; therefore a retry of a triggered build will result in a build that uses the same revision. 



For non-triggered builds that specify `RepoSource`:

  * If the original build built from the tip of a branch, the retried build will build from the tip of that branch, which may not be the same revision as the original build. 
  * If the original build specified a commit sha or revision ID, the retried build will use the identical source. 



For builds that specify `StorageSource`:

  * If the original build pulled source from Cloud Storage without specifying the generation of the object, the new build will use the current object, which may be different from the original build source. 
  * If the original build pulled source from Cloud Storage and specified the generation of the object, the new build will attempt to use the same object, which may or may not be available depending on the bucket's lifecycle management settings. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       RetryBuildRequest request =
           RetryBuildRequest.newBuilder()
               .setName(BuildName.ofProjectBuildName("[PROJECT]", "[BUILD]").toString())
               .setProjectId("projectId-894832108")
               .setId("id3355")
               .build();
       Build response = cloudBuildClient.retryBuildAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RetryBuildRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.RetryBuildRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
### retryBuildAsync(String name)
    
    
    public final OperationFuture<Build,BuildOperationMetadata> retryBuildAsync(String name)

Creates a new build based on the specified build.

This method creates a new build using the original build request, which may or may not result in an identical build.

For triggered builds:

  * Triggered builds resolve to a precise revision; therefore a retry of a triggered build will result in a build that uses the same revision. 



For non-triggered builds that specify `RepoSource`:

  * If the original build built from the tip of a branch, the retried build will build from the tip of that branch, which may not be the same revision as the original build. 
  * If the original build specified a commit sha or revision ID, the retried build will use the identical source. 



For builds that specify `StorageSource`:

  * If the original build pulled source from Cloud Storage without specifying the generation of the object, the new build will use the current object, which may be different from the original build source. 
  * If the original build pulled source from Cloud Storage and specified the generation of the object, the new build will attempt to use the same object, which may or may not be available depending on the bucket's lifecycle management settings. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String name = BuildName.ofProjectBuildName("[PROJECT]", "[BUILD]").toString();
       Build response = cloudBuildClient.retryBuildAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name of the `Build` to retry. Format: `projects/{project}/locations/{location}/builds/{build}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
### retryBuildAsync(String projectId, String id)
    
    
    public final OperationFuture<Build,BuildOperationMetadata> retryBuildAsync(String projectId, String id)

Creates a new build based on the specified build.

This method creates a new build using the original build request, which may or may not result in an identical build.

For triggered builds:

  * Triggered builds resolve to a precise revision; therefore a retry of a triggered build will result in a build that uses the same revision. 



For non-triggered builds that specify `RepoSource`:

  * If the original build built from the tip of a branch, the retried build will build from the tip of that branch, which may not be the same revision as the original build. 
  * If the original build specified a commit sha or revision ID, the retried build will use the identical source. 



For builds that specify `StorageSource`:

  * If the original build pulled source from Cloud Storage without specifying the generation of the object, the new build will use the current object, which may be different from the original build source. 
  * If the original build pulled source from Cloud Storage and specified the generation of the object, the new build will attempt to use the same object, which may or may not be available depending on the bucket's lifecycle management settings. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String projectId = "projectId-894832108";
       String id = "id3355";
       Build response = cloudBuildClient.retryBuildAsync(projectId, id).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the project.  
`id` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Build ID of the original build.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
### retryBuildCallable()
    
    
    public final UnaryCallable<RetryBuildRequest,Operation> retryBuildCallable()

Creates a new build based on the specified build.

This method creates a new build using the original build request, which may or may not result in an identical build.

For triggered builds:

  * Triggered builds resolve to a precise revision; therefore a retry of a triggered build will result in a build that uses the same revision. 



For non-triggered builds that specify `RepoSource`:

  * If the original build built from the tip of a branch, the retried build will build from the tip of that branch, which may not be the same revision as the original build. 
  * If the original build specified a commit sha or revision ID, the retried build will use the identical source. 



For builds that specify `StorageSource`:

  * If the original build pulled source from Cloud Storage without specifying the generation of the object, the new build will use the current object, which may be different from the original build source. 
  * If the original build pulled source from Cloud Storage and specified the generation of the object, the new build will attempt to use the same object, which may or may not be available depending on the bucket's lifecycle management settings. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       RetryBuildRequest request =
           RetryBuildRequest.newBuilder()
               .setName(BuildName.ofProjectBuildName("[PROJECT]", "[BUILD]").toString())
               .setProjectId("projectId-894832108")
               .setId("id3355")
               .build();
       ApiFuture<Operation> future = cloudBuildClient.retryBuildCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RetryBuildRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.RetryBuildRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### retryBuildOperationCallable()
    
    
    public final OperationCallable<RetryBuildRequest,Build,BuildOperationMetadata> retryBuildOperationCallable()

Creates a new build based on the specified build.

This method creates a new build using the original build request, which may or may not result in an identical build.

For triggered builds:

  * Triggered builds resolve to a precise revision; therefore a retry of a triggered build will result in a build that uses the same revision. 



For non-triggered builds that specify `RepoSource`:

  * If the original build built from the tip of a branch, the retried build will build from the tip of that branch, which may not be the same revision as the original build. 
  * If the original build specified a commit sha or revision ID, the retried build will use the identical source. 



For builds that specify `StorageSource`:

  * If the original build pulled source from Cloud Storage without specifying the generation of the object, the new build will use the current object, which may be different from the original build source. 
  * If the original build pulled source from Cloud Storage and specified the generation of the object, the new build will attempt to use the same object, which may or may not be available depending on the bucket's lifecycle management settings. 



Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       RetryBuildRequest request =
           RetryBuildRequest.newBuilder()
               .setName(BuildName.ofProjectBuildName("[PROJECT]", "[BUILD]").toString())
               .setProjectId("projectId-894832108")
               .setId("id3355")
               .build();
       OperationFuture<Build, BuildOperationMetadata> future =
           cloudBuildClient.retryBuildOperationCallable().futureCall(request);
       // Do something.
       Build response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RetryBuildRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.RetryBuildRequest),[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
### runBuildTriggerAsync(RunBuildTriggerRequest request)
    
    
    public final OperationFuture<Build,BuildOperationMetadata> runBuildTriggerAsync(RunBuildTriggerRequest request)

Runs a `BuildTrigger` at a particular source revision.

To run a regional or global trigger, use the POST request that includes the location endpoint in the path (ex. v1/projects/{projectId}/locations/{region}/triggers/{triggerId}:run). The POST request that does not include the location endpoint in the path can only be used when running global triggers.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       RunBuildTriggerRequest request =
           RunBuildTriggerRequest.newBuilder()
               .setName(BuildTriggerName.ofProjectTriggerName("[PROJECT]", "[TRIGGER]").toString())
               .setProjectId("projectId-894832108")
               .setTriggerId("triggerId-648752909")
               .setSource(RepoSource.newBuilder().build())
               .build();
       Build response = cloudBuildClient.runBuildTriggerAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunBuildTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.RunBuildTriggerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
### runBuildTriggerAsync(String projectId, String triggerId, RepoSource source)
    
    
    public final OperationFuture<Build,BuildOperationMetadata> runBuildTriggerAsync(String projectId, String triggerId, RepoSource source)

Runs a `BuildTrigger` at a particular source revision.

To run a regional or global trigger, use the POST request that includes the location endpoint in the path (ex. v1/projects/{projectId}/locations/{region}/triggers/{triggerId}:run). The POST request that does not include the location endpoint in the path can only be used when running global triggers.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String projectId = "projectId-894832108";
       String triggerId = "triggerId-648752909";
       RepoSource source = RepoSource.newBuilder().build();
       Build response = cloudBuildClient.runBuildTriggerAsync(projectId, triggerId, source).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the project.  
`triggerId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the trigger.  
`source` | `[RepoSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.RepoSource)`  
Source to build against this trigger. Branch and tag names cannot consist of regular expressions.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
### runBuildTriggerCallable()
    
    
    public final UnaryCallable<RunBuildTriggerRequest,Operation> runBuildTriggerCallable()

Runs a `BuildTrigger` at a particular source revision.

To run a regional or global trigger, use the POST request that includes the location endpoint in the path (ex. v1/projects/{projectId}/locations/{region}/triggers/{triggerId}:run). The POST request that does not include the location endpoint in the path can only be used when running global triggers.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       RunBuildTriggerRequest request =
           RunBuildTriggerRequest.newBuilder()
               .setName(BuildTriggerName.ofProjectTriggerName("[PROJECT]", "[TRIGGER]").toString())
               .setProjectId("projectId-894832108")
               .setTriggerId("triggerId-648752909")
               .setSource(RepoSource.newBuilder().build())
               .build();
       ApiFuture<Operation> future = cloudBuildClient.runBuildTriggerCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[RunBuildTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.RunBuildTriggerRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### runBuildTriggerOperationCallable()
    
    
    public final OperationCallable<RunBuildTriggerRequest,Build,BuildOperationMetadata> runBuildTriggerOperationCallable()

Runs a `BuildTrigger` at a particular source revision.

To run a regional or global trigger, use the POST request that includes the location endpoint in the path (ex. v1/projects/{projectId}/locations/{region}/triggers/{triggerId}:run). The POST request that does not include the location endpoint in the path can only be used when running global triggers.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       RunBuildTriggerRequest request =
           RunBuildTriggerRequest.newBuilder()
               .setName(BuildTriggerName.ofProjectTriggerName("[PROJECT]", "[TRIGGER]").toString())
               .setProjectId("projectId-894832108")
               .setTriggerId("triggerId-648752909")
               .setSource(RepoSource.newBuilder().build())
               .build();
       OperationFuture<Build, BuildOperationMetadata> future =
           cloudBuildClient.runBuildTriggerOperationCallable().futureCall(request);
       // Do something.
       Build response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[RunBuildTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.RunBuildTriggerRequest),[Build](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Build),[BuildOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildOperationMetadata)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateBuildTrigger(UpdateBuildTriggerRequest request)
    
    
    public final BuildTrigger updateBuildTrigger(UpdateBuildTriggerRequest request)

Updates a `BuildTrigger` by its project ID and trigger ID.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       UpdateBuildTriggerRequest request =
           UpdateBuildTriggerRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setTriggerId("triggerId-648752909")
               .setTrigger(BuildTrigger.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       BuildTrigger response = cloudBuildClient.updateBuildTrigger(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBuildTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.UpdateBuildTriggerRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BuildTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger)` |   
  
### updateBuildTrigger(String projectId, String triggerId, BuildTrigger trigger)
    
    
    public final BuildTrigger updateBuildTrigger(String projectId, String triggerId, BuildTrigger trigger)

Updates a `BuildTrigger` by its project ID and trigger ID.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       String projectId = "projectId-894832108";
       String triggerId = "triggerId-648752909";
       BuildTrigger trigger = BuildTrigger.newBuilder().build();
       BuildTrigger response = cloudBuildClient.updateBuildTrigger(projectId, triggerId, trigger);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the project that owns the trigger.  
`triggerId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ID of the `BuildTrigger` to update.  
`trigger` | `[BuildTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger)`  
Required. `BuildTrigger` to update.  
**Returns**  
---  
**Type** | **Description**  
`[BuildTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger)` |   
  
### updateBuildTriggerCallable()
    
    
    public final UnaryCallable<UpdateBuildTriggerRequest,BuildTrigger> updateBuildTriggerCallable()

Updates a `BuildTrigger` by its project ID and trigger ID.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       UpdateBuildTriggerRequest request =
           UpdateBuildTriggerRequest.newBuilder()
               .setProjectId("projectId-894832108")
               .setTriggerId("triggerId-648752909")
               .setTrigger(BuildTrigger.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<BuildTrigger> future =
           cloudBuildClient.updateBuildTriggerCallable().futureCall(request);
       // Do something.
       BuildTrigger response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateBuildTriggerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.UpdateBuildTriggerRequest),[BuildTrigger](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.BuildTrigger)>` |   
  
### updateWorkerPoolAsync(UpdateWorkerPoolRequest request)
    
    
    public final OperationFuture<WorkerPool,UpdateWorkerPoolOperationMetadata> updateWorkerPoolAsync(UpdateWorkerPoolRequest request)

Updates a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       UpdateWorkerPoolRequest request =
           UpdateWorkerPoolRequest.newBuilder()
               .setWorkerPool(WorkerPool.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       WorkerPool response = cloudBuildClient.updateWorkerPoolAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkerPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.UpdateWorkerPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.WorkerPool),[UpdateWorkerPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.UpdateWorkerPoolOperationMetadata)>` |   
  
### updateWorkerPoolAsync(WorkerPool workerPool, FieldMask updateMask)
    
    
    public final OperationFuture<WorkerPool,UpdateWorkerPoolOperationMetadata> updateWorkerPoolAsync(WorkerPool workerPool, FieldMask updateMask)

Updates a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       WorkerPool workerPool = WorkerPool.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       WorkerPool response = cloudBuildClient.updateWorkerPoolAsync(workerPool, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`workerPool` | `[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.WorkerPool)`  
Required. The `WorkerPool` to update. The `name` field is used to identify the `WorkerPool` to update. Format: `projects/{project}/locations/{location}/workerPools/{workerPool}`.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. A mask specifying which fields in `worker_pool` to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.WorkerPool),[UpdateWorkerPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.UpdateWorkerPoolOperationMetadata)>` |   
  
### updateWorkerPoolCallable()
    
    
    public final UnaryCallable<UpdateWorkerPoolRequest,Operation> updateWorkerPoolCallable()

Updates a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       UpdateWorkerPoolRequest request =
           UpdateWorkerPoolRequest.newBuilder()
               .setWorkerPool(WorkerPool.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       ApiFuture<Operation> future = cloudBuildClient.updateWorkerPoolCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateWorkerPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.UpdateWorkerPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateWorkerPoolOperationCallable()
    
    
    public final OperationCallable<UpdateWorkerPoolRequest,WorkerPool,UpdateWorkerPoolOperationMetadata> updateWorkerPoolOperationCallable()

Updates a `WorkerPool`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (CloudBuildClient cloudBuildClient = CloudBuildClient.create()) {
       UpdateWorkerPoolRequest request =
           UpdateWorkerPoolRequest.newBuilder()
               .setWorkerPool(WorkerPool.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setValidateOnly(true)
               .build();
       OperationFuture<WorkerPool, UpdateWorkerPoolOperationMetadata> future =
           cloudBuildClient.updateWorkerPoolOperationCallable().futureCall(request);
       // Do something.
       WorkerPool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateWorkerPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.UpdateWorkerPoolRequest),[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.WorkerPool),[UpdateWorkerPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.UpdateWorkerPoolOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
