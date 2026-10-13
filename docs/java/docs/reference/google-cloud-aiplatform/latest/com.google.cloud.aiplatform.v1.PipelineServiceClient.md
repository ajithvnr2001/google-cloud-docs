---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient
title: Class PipelineServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:54:26.491238+00:00
---

# Class PipelineServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PipelineServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/PipelineServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: A service for creating and managing Vertex AI's pipelines. This includes both `TrainingPipeline` resources (used for AutoML and custom training) and `PipelineJob` resources (used for Vertex AI Pipelines).

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       TrainingPipeline trainingPipeline = TrainingPipeline.newBuilder().build();
       TrainingPipeline response =
           pipelineServiceClient.createTrainingPipeline(parent, trainingPipeline);
     }
     

Note: close() needs to be called on the PipelineServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateTrainingPipeline |  Creates a TrainingPipeline. A created TrainingPipeline right away will be attempted to be run. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createTrainingPipeline(CreateTrainingPipelineRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createTrainingPipeline(LocationName parent, TrainingPipeline trainingPipeline) 
  * createTrainingPipeline(String parent, TrainingPipeline trainingPipeline) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createTrainingPipelineCallable() 

  
GetTrainingPipeline |  Gets a TrainingPipeline. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTrainingPipeline(GetTrainingPipelineRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTrainingPipeline(TrainingPipelineName name) 
  * getTrainingPipeline(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTrainingPipelineCallable() 

  
ListTrainingPipelines |  Lists TrainingPipelines in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTrainingPipelines(ListTrainingPipelinesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTrainingPipelines(LocationName parent) 
  * listTrainingPipelines(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTrainingPipelinesPagedCallable() 
  * listTrainingPipelinesCallable() 

  
DeleteTrainingPipeline |  Deletes a TrainingPipeline. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteTrainingPipelineAsync(DeleteTrainingPipelineRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteTrainingPipelineAsync(TrainingPipelineName name) 
  * deleteTrainingPipelineAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteTrainingPipelineOperationCallable() 
  * deleteTrainingPipelineCallable() 

  
CancelTrainingPipeline |  Cancels a TrainingPipeline. Starts asynchronous cancellation on the TrainingPipeline. The server makes a best effort to cancel the pipeline, but success is not guaranteed. Clients can use PipelineService.GetTrainingPipeline or other methods to check whether the cancellation succeeded or whether the pipeline completed despite cancellation. On successful cancellation, the TrainingPipeline is not deleted; instead it becomes a pipeline with a TrainingPipeline.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and TrainingPipeline.state is set to `CANCELLED`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelTrainingPipeline(CancelTrainingPipelineRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * cancelTrainingPipeline(TrainingPipelineName name) 
  * cancelTrainingPipeline(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelTrainingPipelineCallable() 

  
CreatePipelineJob |  Creates a PipelineJob. A PipelineJob will run immediately when created. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createPipelineJob(CreatePipelineJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createPipelineJob(LocationName parent, PipelineJob pipelineJob, String pipelineJobId) 
  * createPipelineJob(String parent, PipelineJob pipelineJob, String pipelineJobId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createPipelineJobCallable() 

  
GetPipelineJob |  Gets a PipelineJob. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getPipelineJob(GetPipelineJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getPipelineJob(PipelineJobName name) 
  * getPipelineJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getPipelineJobCallable() 

  
ListPipelineJobs |  Lists PipelineJobs in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listPipelineJobs(ListPipelineJobsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listPipelineJobs(LocationName parent) 
  * listPipelineJobs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPipelineJobsPagedCallable() 
  * listPipelineJobsCallable() 

  
DeletePipelineJob |  Deletes a PipelineJob. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deletePipelineJobAsync(DeletePipelineJobRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deletePipelineJobAsync(PipelineJobName name) 
  * deletePipelineJobAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deletePipelineJobOperationCallable() 
  * deletePipelineJobCallable() 

  
BatchDeletePipelineJobs |  Batch deletes PipelineJobs The Operation is atomic. If it fails, none of the PipelineJobs are deleted. If it succeeds, all of the PipelineJobs are deleted. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchDeletePipelineJobsAsync(BatchDeletePipelineJobsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * batchDeletePipelineJobsAsync(LocationName parent, List<String> names) 
  * batchDeletePipelineJobsAsync(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchDeletePipelineJobsOperationCallable() 
  * batchDeletePipelineJobsCallable() 

  
CancelPipelineJob |  Cancels a PipelineJob. Starts asynchronous cancellation on the PipelineJob. The server makes a best effort to cancel the pipeline, but success is not guaranteed. Clients can use PipelineService.GetPipelineJob or other methods to check whether the cancellation succeeded or whether the pipeline completed despite cancellation. On successful cancellation, the PipelineJob is not deleted; instead it becomes a pipeline with a PipelineJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and PipelineJob.state is set to `CANCELLED`. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelPipelineJob(CancelPipelineJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * cancelPipelineJob(PipelineJobName name) 
  * cancelPipelineJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelPipelineJobCallable() 

  
BatchCancelPipelineJobs |  Batch cancel PipelineJobs. Firstly the server will check if all the jobs are in non-terminal states, and skip the jobs that are already terminated. If the operation failed, none of the pipeline jobs are cancelled. The server will poll the states of all the pipeline jobs periodically to check the cancellation status. This operation will return an LRO. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * batchCancelPipelineJobsAsync(BatchCancelPipelineJobsRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * batchCancelPipelineJobsAsync(LocationName parent, List<String> names) 
  * batchCancelPipelineJobsAsync(String parent, List<String> names) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * batchCancelPipelineJobsOperationCallable() 
  * batchCancelPipelineJobsCallable() 

  
ListLocations |  Lists information about the supported locations for this service. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

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

This class can be customized by passing in a custom instance of PipelineServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PipelineServiceSettings pipelineServiceSettings =
         PipelineServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     PipelineServiceClient pipelineServiceClient =
         PipelineServiceClient.create(pipelineServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     PipelineServiceSettings pipelineServiceSettings =
         PipelineServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     PipelineServiceClient pipelineServiceClient =
         PipelineServiceClient.create(pipelineServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PipelineServiceClient

## Static Methods 

### create()
    
    
    public static final PipelineServiceClient create()

Constructs an instance of PipelineServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PipelineServiceSettings settings)
    
    
    public static final PipelineServiceClient create(PipelineServiceSettings settings)

Constructs an instance of PipelineServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PipelineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(PipelineServiceStub stub)
    
    
    public static final PipelineServiceClient create(PipelineServiceStub stub)

Constructs an instance of PipelineServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(PipelineServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PipelineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.PipelineServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PipelineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient)` |   
  
## Constructors 

### PipelineServiceClient(PipelineServiceSettings settings)
    
    
    protected PipelineServiceClient(PipelineServiceSettings settings)

Constructs an instance of PipelineServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[PipelineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceSettings)`  
  
  
### PipelineServiceClient(PipelineServiceStub stub)
    
    
    protected PipelineServiceClient(PipelineServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[PipelineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.PipelineServiceStub)`  
  
  
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
  
### batchCancelPipelineJobsAsync(@Nullable LocationName parent, List<String> names)
    
    
    public final OperationFuture<BatchCancelPipelineJobsResponse,BatchCancelPipelineJobsOperationMetadata> batchCancelPipelineJobsAsync(@Nullable LocationName parent, List<String> names)

Batch cancel PipelineJobs. Firstly the server will check if all the jobs are in non-terminal states, and skip the jobs that are already terminated. If the operation failed, none of the pipeline jobs are cancelled. The server will poll the states of all the pipeline jobs periodically to check the cancellation status. This operation will return an LRO.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       List<String> names = new ArrayList<>();
       BatchCancelPipelineJobsResponse response =
           pipelineServiceClient.batchCancelPipelineJobsAsync(parent, names).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The name of the PipelineJobs' parent resource. Format: `projects/{project}/locations/{location}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The names of the PipelineJobs to cancel. A maximum of 32 PipelineJobs can be cancelled in a batch. Format: `projects/{project}/locations/{location}/pipelineJobs/{pipelineJob}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchCancelPipelineJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCancelPipelineJobsResponse),[BatchCancelPipelineJobsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCancelPipelineJobsOperationMetadata)>` |   
  
### batchCancelPipelineJobsAsync(BatchCancelPipelineJobsRequest request)
    
    
    public final OperationFuture<BatchCancelPipelineJobsResponse,BatchCancelPipelineJobsOperationMetadata> batchCancelPipelineJobsAsync(BatchCancelPipelineJobsRequest request)

Batch cancel PipelineJobs. Firstly the server will check if all the jobs are in non-terminal states, and skip the jobs that are already terminated. If the operation failed, none of the pipeline jobs are cancelled. The server will poll the states of all the pipeline jobs periodically to check the cancellation status. This operation will return an LRO.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       BatchCancelPipelineJobsRequest request =
           BatchCancelPipelineJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchCancelPipelineJobsResponse response =
           pipelineServiceClient.batchCancelPipelineJobsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCancelPipelineJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCancelPipelineJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchCancelPipelineJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCancelPipelineJobsResponse),[BatchCancelPipelineJobsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCancelPipelineJobsOperationMetadata)>` |   
  
### batchCancelPipelineJobsAsync(String parent, List<String> names)
    
    
    public final OperationFuture<BatchCancelPipelineJobsResponse,BatchCancelPipelineJobsOperationMetadata> batchCancelPipelineJobsAsync(String parent, List<String> names)

Batch cancel PipelineJobs. Firstly the server will check if all the jobs are in non-terminal states, and skip the jobs that are already terminated. If the operation failed, none of the pipeline jobs are cancelled. The server will poll the states of all the pipeline jobs periodically to check the cancellation status. This operation will return an LRO.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       List<String> names = new ArrayList<>();
       BatchCancelPipelineJobsResponse response =
           pipelineServiceClient.batchCancelPipelineJobsAsync(parent, names).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the PipelineJobs' parent resource. Format: `projects/{project}/locations/{location}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The names of the PipelineJobs to cancel. A maximum of 32 PipelineJobs can be cancelled in a batch. Format: `projects/{project}/locations/{location}/pipelineJobs/{pipelineJob}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchCancelPipelineJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCancelPipelineJobsResponse),[BatchCancelPipelineJobsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCancelPipelineJobsOperationMetadata)>` |   
  
### batchCancelPipelineJobsCallable()
    
    
    public final UnaryCallable<BatchCancelPipelineJobsRequest,Operation> batchCancelPipelineJobsCallable()

Batch cancel PipelineJobs. Firstly the server will check if all the jobs are in non-terminal states, and skip the jobs that are already terminated. If the operation failed, none of the pipeline jobs are cancelled. The server will poll the states of all the pipeline jobs periodically to check the cancellation status. This operation will return an LRO.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       BatchCancelPipelineJobsRequest request =
           BatchCancelPipelineJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<Operation> future =
           pipelineServiceClient.batchCancelPipelineJobsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchCancelPipelineJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCancelPipelineJobsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchCancelPipelineJobsOperationCallable()
    
    
    public final OperationCallable<BatchCancelPipelineJobsRequest,BatchCancelPipelineJobsResponse,BatchCancelPipelineJobsOperationMetadata> batchCancelPipelineJobsOperationCallable()

Batch cancel PipelineJobs. Firstly the server will check if all the jobs are in non-terminal states, and skip the jobs that are already terminated. If the operation failed, none of the pipeline jobs are cancelled. The server will poll the states of all the pipeline jobs periodically to check the cancellation status. This operation will return an LRO.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       BatchCancelPipelineJobsRequest request =
           BatchCancelPipelineJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       OperationFuture<BatchCancelPipelineJobsResponse, BatchCancelPipelineJobsOperationMetadata>
           future =
               pipelineServiceClient.batchCancelPipelineJobsOperationCallable().futureCall(request);
       // Do something.
       BatchCancelPipelineJobsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchCancelPipelineJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCancelPipelineJobsRequest),[BatchCancelPipelineJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCancelPipelineJobsResponse),[BatchCancelPipelineJobsOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchCancelPipelineJobsOperationMetadata)>` |   
  
### batchDeletePipelineJobsAsync(@Nullable LocationName parent, List<String> names)
    
    
    public final OperationFuture<BatchDeletePipelineJobsResponse,DeleteOperationMetadata> batchDeletePipelineJobsAsync(@Nullable LocationName parent, List<String> names)

Batch deletes PipelineJobs The Operation is atomic. If it fails, none of the PipelineJobs are deleted. If it succeeds, all of the PipelineJobs are deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       List<String> names = new ArrayList<>();
       BatchDeletePipelineJobsResponse response =
           pipelineServiceClient.batchDeletePipelineJobsAsync(parent, names).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The name of the PipelineJobs' parent resource. Format: `projects/{project}/locations/{location}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The names of the PipelineJobs to delete. A maximum of 32 PipelineJobs can be deleted in a batch. Format: `projects/{project}/locations/{location}/pipelineJobs/{pipelineJob}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchDeletePipelineJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchDeletePipelineJobsResponse),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### batchDeletePipelineJobsAsync(BatchDeletePipelineJobsRequest request)
    
    
    public final OperationFuture<BatchDeletePipelineJobsResponse,DeleteOperationMetadata> batchDeletePipelineJobsAsync(BatchDeletePipelineJobsRequest request)

Batch deletes PipelineJobs The Operation is atomic. If it fails, none of the PipelineJobs are deleted. If it succeeds, all of the PipelineJobs are deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       BatchDeletePipelineJobsRequest request =
           BatchDeletePipelineJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       BatchDeletePipelineJobsResponse response =
           pipelineServiceClient.batchDeletePipelineJobsAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchDeletePipelineJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchDeletePipelineJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchDeletePipelineJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchDeletePipelineJobsResponse),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### batchDeletePipelineJobsAsync(String parent, List<String> names)
    
    
    public final OperationFuture<BatchDeletePipelineJobsResponse,DeleteOperationMetadata> batchDeletePipelineJobsAsync(String parent, List<String> names)

Batch deletes PipelineJobs The Operation is atomic. If it fails, none of the PipelineJobs are deleted. If it succeeds, all of the PipelineJobs are deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       List<String> names = new ArrayList<>();
       BatchDeletePipelineJobsResponse response =
           pipelineServiceClient.batchDeletePipelineJobsAsync(parent, names).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the PipelineJobs' parent resource. Format: `projects/{project}/locations/{location}`  
`names` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
Required. The names of the PipelineJobs to delete. A maximum of 32 PipelineJobs can be deleted in a batch. Format: `projects/{project}/locations/{location}/pipelineJobs/{pipelineJob}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[BatchDeletePipelineJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchDeletePipelineJobsResponse),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### batchDeletePipelineJobsCallable()
    
    
    public final UnaryCallable<BatchDeletePipelineJobsRequest,Operation> batchDeletePipelineJobsCallable()

Batch deletes PipelineJobs The Operation is atomic. If it fails, none of the PipelineJobs are deleted. If it succeeds, all of the PipelineJobs are deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       BatchDeletePipelineJobsRequest request =
           BatchDeletePipelineJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       ApiFuture<Operation> future =
           pipelineServiceClient.batchDeletePipelineJobsCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[BatchDeletePipelineJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchDeletePipelineJobsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### batchDeletePipelineJobsOperationCallable()
    
    
    public final OperationCallable<BatchDeletePipelineJobsRequest,BatchDeletePipelineJobsResponse,DeleteOperationMetadata> batchDeletePipelineJobsOperationCallable()

Batch deletes PipelineJobs The Operation is atomic. If it fails, none of the PipelineJobs are deleted. If it succeeds, all of the PipelineJobs are deleted.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       BatchDeletePipelineJobsRequest request =
           BatchDeletePipelineJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .addAllNames(new ArrayList<String>())
               .build();
       OperationFuture<BatchDeletePipelineJobsResponse, DeleteOperationMetadata> future =
           pipelineServiceClient.batchDeletePipelineJobsOperationCallable().futureCall(request);
       // Do something.
       BatchDeletePipelineJobsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[BatchDeletePipelineJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchDeletePipelineJobsRequest),[BatchDeletePipelineJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchDeletePipelineJobsResponse),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### cancelPipelineJob(@Nullable PipelineJobName name)
    
    
    public final void cancelPipelineJob(@Nullable PipelineJobName name)

Cancels a PipelineJob. Starts asynchronous cancellation on the PipelineJob. The server makes a best effort to cancel the pipeline, but success is not guaranteed. Clients can use PipelineService.GetPipelineJob or other methods to check whether the cancellation succeeded or whether the pipeline completed despite cancellation. On successful cancellation, the PipelineJob is not deleted; instead it becomes a pipeline with a PipelineJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and PipelineJob.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       PipelineJobName name = PipelineJobName.of("[PROJECT]", "[LOCATION]", "[PIPELINE_JOB]");
       pipelineServiceClient.cancelPipelineJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.PipelineJobName`  
Required. The name of the PipelineJob to cancel. Format: `projects/{project}/locations/{location}/pipelineJobs/{pipeline_job}`  
  
### cancelPipelineJob(CancelPipelineJobRequest request)
    
    
    public final void cancelPipelineJob(CancelPipelineJobRequest request)

Cancels a PipelineJob. Starts asynchronous cancellation on the PipelineJob. The server makes a best effort to cancel the pipeline, but success is not guaranteed. Clients can use PipelineService.GetPipelineJob or other methods to check whether the cancellation succeeded or whether the pipeline completed despite cancellation. On successful cancellation, the PipelineJob is not deleted; instead it becomes a pipeline with a PipelineJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and PipelineJob.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       CancelPipelineJobRequest request =
           CancelPipelineJobRequest.newBuilder()
               .setName(PipelineJobName.of("[PROJECT]", "[LOCATION]", "[PIPELINE_JOB]").toString())
               .build();
       pipelineServiceClient.cancelPipelineJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelPipelineJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CancelPipelineJobRequest)`  
The request object containing all of the parameters for the API call.  
  
### cancelPipelineJob(String name)
    
    
    public final void cancelPipelineJob(String name)

Cancels a PipelineJob. Starts asynchronous cancellation on the PipelineJob. The server makes a best effort to cancel the pipeline, but success is not guaranteed. Clients can use PipelineService.GetPipelineJob or other methods to check whether the cancellation succeeded or whether the pipeline completed despite cancellation. On successful cancellation, the PipelineJob is not deleted; instead it becomes a pipeline with a PipelineJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and PipelineJob.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       String name = PipelineJobName.of("[PROJECT]", "[LOCATION]", "[PIPELINE_JOB]").toString();
       pipelineServiceClient.cancelPipelineJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the PipelineJob to cancel. Format: `projects/{project}/locations/{location}/pipelineJobs/{pipeline_job}`  
  
### cancelPipelineJobCallable()
    
    
    public final UnaryCallable<CancelPipelineJobRequest,Empty> cancelPipelineJobCallable()

Cancels a PipelineJob. Starts asynchronous cancellation on the PipelineJob. The server makes a best effort to cancel the pipeline, but success is not guaranteed. Clients can use PipelineService.GetPipelineJob or other methods to check whether the cancellation succeeded or whether the pipeline completed despite cancellation. On successful cancellation, the PipelineJob is not deleted; instead it becomes a pipeline with a PipelineJob.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and PipelineJob.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       CancelPipelineJobRequest request =
           CancelPipelineJobRequest.newBuilder()
               .setName(PipelineJobName.of("[PROJECT]", "[LOCATION]", "[PIPELINE_JOB]").toString())
               .build();
       ApiFuture<Empty> future =
           pipelineServiceClient.cancelPipelineJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelPipelineJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CancelPipelineJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### cancelTrainingPipeline(@Nullable TrainingPipelineName name)
    
    
    public final void cancelTrainingPipeline(@Nullable TrainingPipelineName name)

Cancels a TrainingPipeline. Starts asynchronous cancellation on the TrainingPipeline. The server makes a best effort to cancel the pipeline, but success is not guaranteed. Clients can use PipelineService.GetTrainingPipeline or other methods to check whether the cancellation succeeded or whether the pipeline completed despite cancellation. On successful cancellation, the TrainingPipeline is not deleted; instead it becomes a pipeline with a TrainingPipeline.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and TrainingPipeline.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       TrainingPipelineName name =
           TrainingPipelineName.of("[PROJECT]", "[LOCATION]", "[TRAINING_PIPELINE]");
       pipelineServiceClient.cancelTrainingPipeline(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TrainingPipelineName`  
Required. The name of the TrainingPipeline to cancel. Format: `projects/{project}/locations/{location}/trainingPipelines/{training_pipeline}`  
  
### cancelTrainingPipeline(CancelTrainingPipelineRequest request)
    
    
    public final void cancelTrainingPipeline(CancelTrainingPipelineRequest request)

Cancels a TrainingPipeline. Starts asynchronous cancellation on the TrainingPipeline. The server makes a best effort to cancel the pipeline, but success is not guaranteed. Clients can use PipelineService.GetTrainingPipeline or other methods to check whether the cancellation succeeded or whether the pipeline completed despite cancellation. On successful cancellation, the TrainingPipeline is not deleted; instead it becomes a pipeline with a TrainingPipeline.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and TrainingPipeline.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       CancelTrainingPipelineRequest request =
           CancelTrainingPipelineRequest.newBuilder()
               .setName(
                   TrainingPipelineName.of("[PROJECT]", "[LOCATION]", "[TRAINING_PIPELINE]")
                       .toString())
               .build();
       pipelineServiceClient.cancelTrainingPipeline(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelTrainingPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CancelTrainingPipelineRequest)`  
The request object containing all of the parameters for the API call.  
  
### cancelTrainingPipeline(String name)
    
    
    public final void cancelTrainingPipeline(String name)

Cancels a TrainingPipeline. Starts asynchronous cancellation on the TrainingPipeline. The server makes a best effort to cancel the pipeline, but success is not guaranteed. Clients can use PipelineService.GetTrainingPipeline or other methods to check whether the cancellation succeeded or whether the pipeline completed despite cancellation. On successful cancellation, the TrainingPipeline is not deleted; instead it becomes a pipeline with a TrainingPipeline.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and TrainingPipeline.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       String name =
           TrainingPipelineName.of("[PROJECT]", "[LOCATION]", "[TRAINING_PIPELINE]").toString();
       pipelineServiceClient.cancelTrainingPipeline(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the TrainingPipeline to cancel. Format: `projects/{project}/locations/{location}/trainingPipelines/{training_pipeline}`  
  
### cancelTrainingPipelineCallable()
    
    
    public final UnaryCallable<CancelTrainingPipelineRequest,Empty> cancelTrainingPipelineCallable()

Cancels a TrainingPipeline. Starts asynchronous cancellation on the TrainingPipeline. The server makes a best effort to cancel the pipeline, but success is not guaranteed. Clients can use PipelineService.GetTrainingPipeline or other methods to check whether the cancellation succeeded or whether the pipeline completed despite cancellation. On successful cancellation, the TrainingPipeline is not deleted; instead it becomes a pipeline with a TrainingPipeline.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`, and TrainingPipeline.state is set to `CANCELLED`.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       CancelTrainingPipelineRequest request =
           CancelTrainingPipelineRequest.newBuilder()
               .setName(
                   TrainingPipelineName.of("[PROJECT]", "[LOCATION]", "[TRAINING_PIPELINE]")
                       .toString())
               .build();
       ApiFuture<Empty> future =
           pipelineServiceClient.cancelTrainingPipelineCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelTrainingPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CancelTrainingPipelineRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### close()
    
    
    public final void close()

### createPipelineJob(@Nullable LocationName parent, PipelineJob pipelineJob, String pipelineJobId)
    
    
    public final PipelineJob createPipelineJob(@Nullable LocationName parent, PipelineJob pipelineJob, String pipelineJobId)

Creates a PipelineJob. A PipelineJob will run immediately when created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       PipelineJob pipelineJob = PipelineJob.newBuilder().build();
       String pipelineJobId = "pipelineJobId-1711315914";
       PipelineJob response =
           pipelineServiceClient.createPipelineJob(parent, pipelineJob, pipelineJobId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create the PipelineJob in. Format: `projects/{project}/locations/{location}`  
`pipelineJob` | `[PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob)`  
Required. The PipelineJob to create.  
`pipelineJobId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The ID to use for the PipelineJob, which will become the final component of the PipelineJob name. If not provided, an ID will be automatically generated. This value should be less than 128 characters, and valid characters are `/a-z-/`.  
**Returns**  
---  
**Type** | **Description**  
`[PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob)` |   
  
### createPipelineJob(CreatePipelineJobRequest request)
    
    
    public final PipelineJob createPipelineJob(CreatePipelineJobRequest request)

Creates a PipelineJob. A PipelineJob will run immediately when created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       CreatePipelineJobRequest request =
           CreatePipelineJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPipelineJob(PipelineJob.newBuilder().build())
               .setPipelineJobId("pipelineJobId-1711315914")
               .build();
       PipelineJob response = pipelineServiceClient.createPipelineJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePipelineJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreatePipelineJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob)` |   
  
### createPipelineJob(String parent, PipelineJob pipelineJob, String pipelineJobId)
    
    
    public final PipelineJob createPipelineJob(String parent, PipelineJob pipelineJob, String pipelineJobId)

Creates a PipelineJob. A PipelineJob will run immediately when created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       PipelineJob pipelineJob = PipelineJob.newBuilder().build();
       String pipelineJobId = "pipelineJobId-1711315914";
       PipelineJob response =
           pipelineServiceClient.createPipelineJob(parent, pipelineJob, pipelineJobId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the PipelineJob in. Format: `projects/{project}/locations/{location}`  
`pipelineJob` | `[PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob)`  
Required. The PipelineJob to create.  
`pipelineJobId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The ID to use for the PipelineJob, which will become the final component of the PipelineJob name. If not provided, an ID will be automatically generated. This value should be less than 128 characters, and valid characters are `/a-z-/`.  
**Returns**  
---  
**Type** | **Description**  
`[PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob)` |   
  
### createPipelineJobCallable()
    
    
    public final UnaryCallable<CreatePipelineJobRequest,PipelineJob> createPipelineJobCallable()

Creates a PipelineJob. A PipelineJob will run immediately when created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       CreatePipelineJobRequest request =
           CreatePipelineJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPipelineJob(PipelineJob.newBuilder().build())
               .setPipelineJobId("pipelineJobId-1711315914")
               .build();
       ApiFuture<PipelineJob> future =
           pipelineServiceClient.createPipelineJobCallable().futureCall(request);
       // Do something.
       PipelineJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePipelineJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreatePipelineJobRequest),[PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob)>` |   
  
### createTrainingPipeline(@Nullable LocationName parent, TrainingPipeline trainingPipeline)
    
    
    public final TrainingPipeline createTrainingPipeline(@Nullable LocationName parent, TrainingPipeline trainingPipeline)

Creates a TrainingPipeline. A created TrainingPipeline right away will be attempted to be run.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       TrainingPipeline trainingPipeline = TrainingPipeline.newBuilder().build();
       TrainingPipeline response =
           pipelineServiceClient.createTrainingPipeline(parent, trainingPipeline);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create the TrainingPipeline in. Format: `projects/{project}/locations/{location}`  
`trainingPipeline` | `[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline)`  
Required. The TrainingPipeline to create.  
**Returns**  
---  
**Type** | **Description**  
`[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline)` |   
  
### createTrainingPipeline(CreateTrainingPipelineRequest request)
    
    
    public final TrainingPipeline createTrainingPipeline(CreateTrainingPipelineRequest request)

Creates a TrainingPipeline. A created TrainingPipeline right away will be attempted to be run.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       CreateTrainingPipelineRequest request =
           CreateTrainingPipelineRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTrainingPipeline(TrainingPipeline.newBuilder().build())
               .build();
       TrainingPipeline response = pipelineServiceClient.createTrainingPipeline(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTrainingPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTrainingPipelineRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline)` |   
  
### createTrainingPipeline(String parent, TrainingPipeline trainingPipeline)
    
    
    public final TrainingPipeline createTrainingPipeline(String parent, TrainingPipeline trainingPipeline)

Creates a TrainingPipeline. A created TrainingPipeline right away will be attempted to be run.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       TrainingPipeline trainingPipeline = TrainingPipeline.newBuilder().build();
       TrainingPipeline response =
           pipelineServiceClient.createTrainingPipeline(parent, trainingPipeline);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the TrainingPipeline in. Format: `projects/{project}/locations/{location}`  
`trainingPipeline` | `[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline)`  
Required. The TrainingPipeline to create.  
**Returns**  
---  
**Type** | **Description**  
`[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline)` |   
  
### createTrainingPipelineCallable()
    
    
    public final UnaryCallable<CreateTrainingPipelineRequest,TrainingPipeline> createTrainingPipelineCallable()

Creates a TrainingPipeline. A created TrainingPipeline right away will be attempted to be run.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       CreateTrainingPipelineRequest request =
           CreateTrainingPipelineRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setTrainingPipeline(TrainingPipeline.newBuilder().build())
               .build();
       ApiFuture<TrainingPipeline> future =
           pipelineServiceClient.createTrainingPipelineCallable().futureCall(request);
       // Do something.
       TrainingPipeline response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateTrainingPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateTrainingPipelineRequest),[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline)>` |   
  
### deletePipelineJobAsync(@Nullable PipelineJobName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deletePipelineJobAsync(@Nullable PipelineJobName name)

Deletes a PipelineJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       PipelineJobName name = PipelineJobName.of("[PROJECT]", "[LOCATION]", "[PIPELINE_JOB]");
       pipelineServiceClient.deletePipelineJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.PipelineJobName`  
Required. The name of the PipelineJob resource to be deleted. Format: `projects/{project}/locations/{location}/pipelineJobs/{pipeline_job}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deletePipelineJobAsync(DeletePipelineJobRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deletePipelineJobAsync(DeletePipelineJobRequest request)

Deletes a PipelineJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       DeletePipelineJobRequest request =
           DeletePipelineJobRequest.newBuilder()
               .setName(PipelineJobName.of("[PROJECT]", "[LOCATION]", "[PIPELINE_JOB]").toString())
               .build();
       pipelineServiceClient.deletePipelineJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePipelineJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeletePipelineJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deletePipelineJobAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deletePipelineJobAsync(String name)

Deletes a PipelineJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       String name = PipelineJobName.of("[PROJECT]", "[LOCATION]", "[PIPELINE_JOB]").toString();
       pipelineServiceClient.deletePipelineJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the PipelineJob resource to be deleted. Format: `projects/{project}/locations/{location}/pipelineJobs/{pipeline_job}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deletePipelineJobCallable()
    
    
    public final UnaryCallable<DeletePipelineJobRequest,Operation> deletePipelineJobCallable()

Deletes a PipelineJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       DeletePipelineJobRequest request =
           DeletePipelineJobRequest.newBuilder()
               .setName(PipelineJobName.of("[PROJECT]", "[LOCATION]", "[PIPELINE_JOB]").toString())
               .build();
       ApiFuture<Operation> future =
           pipelineServiceClient.deletePipelineJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePipelineJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeletePipelineJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePipelineJobOperationCallable()
    
    
    public final OperationCallable<DeletePipelineJobRequest,Empty,DeleteOperationMetadata> deletePipelineJobOperationCallable()

Deletes a PipelineJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       DeletePipelineJobRequest request =
           DeletePipelineJobRequest.newBuilder()
               .setName(PipelineJobName.of("[PROJECT]", "[LOCATION]", "[PIPELINE_JOB]").toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           pipelineServiceClient.deletePipelineJobOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePipelineJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeletePipelineJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTrainingPipelineAsync(@Nullable TrainingPipelineName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteTrainingPipelineAsync(@Nullable TrainingPipelineName name)

Deletes a TrainingPipeline.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       TrainingPipelineName name =
           TrainingPipelineName.of("[PROJECT]", "[LOCATION]", "[TRAINING_PIPELINE]");
       pipelineServiceClient.deleteTrainingPipelineAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TrainingPipelineName`  
Required. The name of the TrainingPipeline resource to be deleted. Format: `projects/{project}/locations/{location}/trainingPipelines/{training_pipeline}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTrainingPipelineAsync(DeleteTrainingPipelineRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteTrainingPipelineAsync(DeleteTrainingPipelineRequest request)

Deletes a TrainingPipeline.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       DeleteTrainingPipelineRequest request =
           DeleteTrainingPipelineRequest.newBuilder()
               .setName(
                   TrainingPipelineName.of("[PROJECT]", "[LOCATION]", "[TRAINING_PIPELINE]")
                       .toString())
               .build();
       pipelineServiceClient.deleteTrainingPipelineAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTrainingPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTrainingPipelineRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTrainingPipelineAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteTrainingPipelineAsync(String name)

Deletes a TrainingPipeline.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       String name =
           TrainingPipelineName.of("[PROJECT]", "[LOCATION]", "[TRAINING_PIPELINE]").toString();
       pipelineServiceClient.deleteTrainingPipelineAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the TrainingPipeline resource to be deleted. Format: `projects/{project}/locations/{location}/trainingPipelines/{training_pipeline}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteTrainingPipelineCallable()
    
    
    public final UnaryCallable<DeleteTrainingPipelineRequest,Operation> deleteTrainingPipelineCallable()

Deletes a TrainingPipeline.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       DeleteTrainingPipelineRequest request =
           DeleteTrainingPipelineRequest.newBuilder()
               .setName(
                   TrainingPipelineName.of("[PROJECT]", "[LOCATION]", "[TRAINING_PIPELINE]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           pipelineServiceClient.deleteTrainingPipelineCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteTrainingPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTrainingPipelineRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTrainingPipelineOperationCallable()
    
    
    public final OperationCallable<DeleteTrainingPipelineRequest,Empty,DeleteOperationMetadata> deleteTrainingPipelineOperationCallable()

Deletes a TrainingPipeline.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       DeleteTrainingPipelineRequest request =
           DeleteTrainingPipelineRequest.newBuilder()
               .setName(
                   TrainingPipelineName.of("[PROJECT]", "[LOCATION]", "[TRAINING_PIPELINE]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           pipelineServiceClient.deleteTrainingPipelineOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteTrainingPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteTrainingPipelineRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = pipelineServiceClient.getIamPolicy(request);
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
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future = pipelineServiceClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = pipelineServiceClient.getLocation(request);
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
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = pipelineServiceClient.getLocationCallable().futureCall(request);
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
  
### getPipelineJob(@Nullable PipelineJobName name)
    
    
    public final PipelineJob getPipelineJob(@Nullable PipelineJobName name)

Gets a PipelineJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       PipelineJobName name = PipelineJobName.of("[PROJECT]", "[LOCATION]", "[PIPELINE_JOB]");
       PipelineJob response = pipelineServiceClient.getPipelineJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.PipelineJobName`  
Required. The name of the PipelineJob resource. Format: `projects/{project}/locations/{location}/pipelineJobs/{pipeline_job}`  
**Returns**  
---  
**Type** | **Description**  
`[PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob)` |   
  
### getPipelineJob(GetPipelineJobRequest request)
    
    
    public final PipelineJob getPipelineJob(GetPipelineJobRequest request)

Gets a PipelineJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       GetPipelineJobRequest request =
           GetPipelineJobRequest.newBuilder()
               .setName(PipelineJobName.of("[PROJECT]", "[LOCATION]", "[PIPELINE_JOB]").toString())
               .build();
       PipelineJob response = pipelineServiceClient.getPipelineJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPipelineJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetPipelineJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob)` |   
  
### getPipelineJob(String name)
    
    
    public final PipelineJob getPipelineJob(String name)

Gets a PipelineJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       String name = PipelineJobName.of("[PROJECT]", "[LOCATION]", "[PIPELINE_JOB]").toString();
       PipelineJob response = pipelineServiceClient.getPipelineJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the PipelineJob resource. Format: `projects/{project}/locations/{location}/pipelineJobs/{pipeline_job}`  
**Returns**  
---  
**Type** | **Description**  
`[PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob)` |   
  
### getPipelineJobCallable()
    
    
    public final UnaryCallable<GetPipelineJobRequest,PipelineJob> getPipelineJobCallable()

Gets a PipelineJob.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       GetPipelineJobRequest request =
           GetPipelineJobRequest.newBuilder()
               .setName(PipelineJobName.of("[PROJECT]", "[LOCATION]", "[PIPELINE_JOB]").toString())
               .build();
       ApiFuture<PipelineJob> future =
           pipelineServiceClient.getPipelineJobCallable().futureCall(request);
       // Do something.
       PipelineJob response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPipelineJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetPipelineJobRequest),[PipelineJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineJob)>` |   
  
### getSettings()
    
    
    public final @Nullable PipelineServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.PipelineServiceSettings` |   
  
### getStub()
    
    
    public PipelineServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[PipelineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.PipelineServiceStub)` |   
  
### getTrainingPipeline(@Nullable TrainingPipelineName name)
    
    
    public final TrainingPipeline getTrainingPipeline(@Nullable TrainingPipelineName name)

Gets a TrainingPipeline.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       TrainingPipelineName name =
           TrainingPipelineName.of("[PROJECT]", "[LOCATION]", "[TRAINING_PIPELINE]");
       TrainingPipeline response = pipelineServiceClient.getTrainingPipeline(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.TrainingPipelineName`  
Required. The name of the TrainingPipeline resource. Format: `projects/{project}/locations/{location}/trainingPipelines/{training_pipeline}`  
**Returns**  
---  
**Type** | **Description**  
`[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline)` |   
  
### getTrainingPipeline(GetTrainingPipelineRequest request)
    
    
    public final TrainingPipeline getTrainingPipeline(GetTrainingPipelineRequest request)

Gets a TrainingPipeline.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       GetTrainingPipelineRequest request =
           GetTrainingPipelineRequest.newBuilder()
               .setName(
                   TrainingPipelineName.of("[PROJECT]", "[LOCATION]", "[TRAINING_PIPELINE]")
                       .toString())
               .build();
       TrainingPipeline response = pipelineServiceClient.getTrainingPipeline(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTrainingPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetTrainingPipelineRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline)` |   
  
### getTrainingPipeline(String name)
    
    
    public final TrainingPipeline getTrainingPipeline(String name)

Gets a TrainingPipeline.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       String name =
           TrainingPipelineName.of("[PROJECT]", "[LOCATION]", "[TRAINING_PIPELINE]").toString();
       TrainingPipeline response = pipelineServiceClient.getTrainingPipeline(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the TrainingPipeline resource. Format: `projects/{project}/locations/{location}/trainingPipelines/{training_pipeline}`  
**Returns**  
---  
**Type** | **Description**  
`[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline)` |   
  
### getTrainingPipelineCallable()
    
    
    public final UnaryCallable<GetTrainingPipelineRequest,TrainingPipeline> getTrainingPipelineCallable()

Gets a TrainingPipeline.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       GetTrainingPipelineRequest request =
           GetTrainingPipelineRequest.newBuilder()
               .setName(
                   TrainingPipelineName.of("[PROJECT]", "[LOCATION]", "[TRAINING_PIPELINE]")
                       .toString())
               .build();
       ApiFuture<TrainingPipeline> future =
           pipelineServiceClient.getTrainingPipelineCallable().futureCall(request);
       // Do something.
       TrainingPipeline response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTrainingPipelineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetTrainingPipelineRequest),[TrainingPipeline](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrainingPipeline)>` |   
  
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
  
### listLocations(ListLocationsRequest request)
    
    
    public final PipelineServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : pipelineServiceClient.listLocations(request).iterateAll()) {
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
`[PipelineServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             pipelineServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,PipelineServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           pipelineServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.ListLocationsPagedResponse)>` |   
  
### listPipelineJobs(@Nullable LocationName parent)
    
    
    public final PipelineServiceClient.ListPipelineJobsPagedResponse listPipelineJobs(@Nullable LocationName parent)

Lists PipelineJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (PipelineJob element : pipelineServiceClient.listPipelineJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to list the PipelineJobs from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[PipelineServiceClient.ListPipelineJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.ListPipelineJobsPagedResponse)` |   
  
### listPipelineJobs(ListPipelineJobsRequest request)
    
    
    public final PipelineServiceClient.ListPipelineJobsPagedResponse listPipelineJobs(ListPipelineJobsRequest request)

Lists PipelineJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       ListPipelineJobsRequest request =
           ListPipelineJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (PipelineJob element : pipelineServiceClient.listPipelineJobs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPipelineJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListPipelineJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PipelineServiceClient.ListPipelineJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.ListPipelineJobsPagedResponse)` |   
  
### listPipelineJobs(String parent)
    
    
    public final PipelineServiceClient.ListPipelineJobsPagedResponse listPipelineJobs(String parent)

Lists PipelineJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (PipelineJob element : pipelineServiceClient.listPipelineJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to list the PipelineJobs from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[PipelineServiceClient.ListPipelineJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.ListPipelineJobsPagedResponse)` |   
  
### listPipelineJobsCallable()
    
    
    public final UnaryCallable<ListPipelineJobsRequest,ListPipelineJobsResponse> listPipelineJobsCallable()

Lists PipelineJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       ListPipelineJobsRequest request =
           ListPipelineJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListPipelineJobsResponse response =
             pipelineServiceClient.listPipelineJobsCallable().call(request);
         for (PipelineJob element : response.getPipelineJobsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPipelineJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListPipelineJobsRequest),[ListPipelineJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListPipelineJobsResponse)>` |   
  
### listPipelineJobsPagedCallable()
    
    
    public final UnaryCallable<ListPipelineJobsRequest,PipelineServiceClient.ListPipelineJobsPagedResponse> listPipelineJobsPagedCallable()

Lists PipelineJobs in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       ListPipelineJobsRequest request =
           ListPipelineJobsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<PipelineJob> future =
           pipelineServiceClient.listPipelineJobsPagedCallable().futureCall(request);
       // Do something.
       for (PipelineJob element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPipelineJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListPipelineJobsRequest),[ListPipelineJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.ListPipelineJobsPagedResponse)>` |   
  
### listTrainingPipelines(@Nullable LocationName parent)
    
    
    public final PipelineServiceClient.ListTrainingPipelinesPagedResponse listTrainingPipelines(@Nullable LocationName parent)

Lists TrainingPipelines in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (TrainingPipeline element :
           pipelineServiceClient.listTrainingPipelines(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to list the TrainingPipelines from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[PipelineServiceClient.ListTrainingPipelinesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.ListTrainingPipelinesPagedResponse)` |   
  
### listTrainingPipelines(ListTrainingPipelinesRequest request)
    
    
    public final PipelineServiceClient.ListTrainingPipelinesPagedResponse listTrainingPipelines(ListTrainingPipelinesRequest request)

Lists TrainingPipelines in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       ListTrainingPipelinesRequest request =
           ListTrainingPipelinesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (TrainingPipeline element :
           pipelineServiceClient.listTrainingPipelines(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTrainingPipelinesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTrainingPipelinesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PipelineServiceClient.ListTrainingPipelinesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.ListTrainingPipelinesPagedResponse)` |   
  
### listTrainingPipelines(String parent)
    
    
    public final PipelineServiceClient.ListTrainingPipelinesPagedResponse listTrainingPipelines(String parent)

Lists TrainingPipelines in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (TrainingPipeline element :
           pipelineServiceClient.listTrainingPipelines(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to list the TrainingPipelines from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[PipelineServiceClient.ListTrainingPipelinesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.ListTrainingPipelinesPagedResponse)` |   
  
### listTrainingPipelinesCallable()
    
    
    public final UnaryCallable<ListTrainingPipelinesRequest,ListTrainingPipelinesResponse> listTrainingPipelinesCallable()

Lists TrainingPipelines in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       ListTrainingPipelinesRequest request =
           ListTrainingPipelinesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListTrainingPipelinesResponse response =
             pipelineServiceClient.listTrainingPipelinesCallable().call(request);
         for (TrainingPipeline element : response.getTrainingPipelinesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTrainingPipelinesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTrainingPipelinesRequest),[ListTrainingPipelinesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTrainingPipelinesResponse)>` |   
  
### listTrainingPipelinesPagedCallable()
    
    
    public final UnaryCallable<ListTrainingPipelinesRequest,PipelineServiceClient.ListTrainingPipelinesPagedResponse> listTrainingPipelinesPagedCallable()

Lists TrainingPipelines in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       ListTrainingPipelinesRequest request =
           ListTrainingPipelinesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<TrainingPipeline> future =
           pipelineServiceClient.listTrainingPipelinesPagedCallable().futureCall(request);
       // Do something.
       for (TrainingPipeline element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTrainingPipelinesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListTrainingPipelinesRequest),[ListTrainingPipelinesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PipelineServiceClient.ListTrainingPipelinesPagedResponse)>` |   
  
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
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = pipelineServiceClient.setIamPolicy(request);
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
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future = pipelineServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = pipelineServiceClient.testIamPermissions(request);
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
     try (PipelineServiceClient pipelineServiceClient = PipelineServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           pipelineServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
