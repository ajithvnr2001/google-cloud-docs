---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient
title: Class BatchServiceClient (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:39:21.248015+00:00
---

# Class BatchServiceClient (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BatchServiceClient (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.2  0.2.2  0.1.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-batch/google-cloud-batch/src/main/java/com/google/cloud/batch/v1alpha/BatchServiceClient.java)| [Product Reference](https://cloud.google.com/)  
---|---  
  
Service Description: Google Batch Service. The service manages user submitted batch jobs and allocates Google Compute Engine VM instances to run the jobs.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Job job = Job.newBuilder().build();
       String jobId = "jobId101296568";
       Job response = batchServiceClient.createJob(parent, job, jobId);
     }
     

Note: close() needs to be called on the BatchServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateJob |  Create a Job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createJob(CreateJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createJob(LocationName parent, Job job, String jobId) 
  * createJob(String parent, Job job, String jobId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createJobCallable() 

  
GetJob |  Get a Job specified by its resource name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getJob(GetJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getJob(JobName name) 
  * getJob(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getJobCallable() 

  
DeleteJob |  Delete a Job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteJobAsync(DeleteJobRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteJobAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteJobOperationCallable() 
  * deleteJobCallable() 

  
CancelJob |  Cancel a Job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelJobAsync(CancelJobRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * cancelJobAsync(JobName name) 
  * cancelJobAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelJobOperationCallable() 
  * cancelJobCallable() 

  
UpdateJob |  Update a Job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateJob(UpdateJobRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateJob(Job job, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateJobCallable() 

  
ListJobs |  List all Jobs for a project within a region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listJobs(ListJobsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listJobs(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listJobsPagedCallable() 
  * listJobsCallable() 

  
GetTask |  Return a single Task. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getTask(GetTaskRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getTask(TaskName name) 
  * getTask(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getTaskCallable() 

  
ListTasks |  List Tasks associated with a job. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listTasks(ListTasksRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listTasks(TaskGroupName parent) 
  * listTasks(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listTasksPagedCallable() 
  * listTasksCallable() 

  
CreateResourceAllowance |  Create a Resource Allowance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createResourceAllowance(CreateResourceAllowanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createResourceAllowance(LocationName parent, ResourceAllowance resourceAllowance, String resourceAllowanceId) 
  * createResourceAllowance(String parent, ResourceAllowance resourceAllowance, String resourceAllowanceId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createResourceAllowanceCallable() 

  
GetResourceAllowance |  Get a ResourceAllowance specified by its resource name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getResourceAllowance(GetResourceAllowanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getResourceAllowance(ResourceAllowanceName name) 
  * getResourceAllowance(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getResourceAllowanceCallable() 

  
DeleteResourceAllowance |  Delete a ResourceAllowance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteResourceAllowanceAsync(DeleteResourceAllowanceRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteResourceAllowanceAsync(ResourceAllowanceName name) 
  * deleteResourceAllowanceAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteResourceAllowanceOperationCallable() 
  * deleteResourceAllowanceCallable() 

  
ListResourceAllowances |  List all ResourceAllowances for a project within a region. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listResourceAllowances(ListResourceAllowancesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listResourceAllowances(LocationName parent) 
  * listResourceAllowances(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listResourceAllowancesPagedCallable() 
  * listResourceAllowancesCallable() 

  
UpdateResourceAllowance |  Update a Resource Allowance. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateResourceAllowance(UpdateResourceAllowanceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateResourceAllowance(ResourceAllowance resourceAllowance, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateResourceAllowanceCallable() 

  
ListLocations |  Lists information about the supported locations for this service.  This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.  For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listLocations(ListLocationsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listLocationsPagedCallable() 
  * listLocationsCallable() 

  
GetLocation |  Gets information about a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getLocation(GetLocationRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getLocationCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of BatchServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BatchServiceSettings batchServiceSettings =
         BatchServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     BatchServiceClient batchServiceClient = BatchServiceClient.create(batchServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BatchServiceSettings batchServiceSettings =
         BatchServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     BatchServiceClient batchServiceClient = BatchServiceClient.create(batchServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     BatchServiceSettings batchServiceSettings = BatchServiceSettings.newHttpJsonBuilder().build();
     BatchServiceClient batchServiceClient = BatchServiceClient.create(batchServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BatchServiceClient

## Static Methods 

### create()
    
    
    public static final BatchServiceClient create()

Constructs an instance of BatchServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BatchServiceSettings settings)
    
    
    public static final BatchServiceClient create(BatchServiceSettings settings)

Constructs an instance of BatchServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BatchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(BatchServiceStub stub)
    
    
    public static final BatchServiceClient create(BatchServiceStub stub)

Constructs an instance of BatchServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(BatchServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BatchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.stub.BatchServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BatchServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient)` |   
  
## Constructors 

### BatchServiceClient(BatchServiceSettings settings)
    
    
    protected BatchServiceClient(BatchServiceSettings settings)

Constructs an instance of BatchServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[BatchServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceSettings)`  
  
  
### BatchServiceClient(BatchServiceStub stub)
    
    
    protected BatchServiceClient(BatchServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[BatchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.stub.BatchServiceStub)`  
  
  
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
  
### cancelJobAsync(@Nullable JobName name)
    
    
    public final OperationFuture<CancelJobResponse,OperationMetadata> cancelJobAsync(@Nullable JobName name)

Cancel a Job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       JobName name = JobName.of("[PROJECT]", "[LOCATION]", "[JOB]");
       CancelJobResponse response = batchServiceClient.cancelJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.batch.v1alpha.JobName`  
Required. Job name.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CancelJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CancelJobResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadata)>` |   
  
### cancelJobAsync(CancelJobRequest request)
    
    
    public final OperationFuture<CancelJobResponse,OperationMetadata> cancelJobAsync(CancelJobRequest request)

Cancel a Job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       CancelJobRequest request =
           CancelJobRequest.newBuilder()
               .setName(JobName.of("[PROJECT]", "[LOCATION]", "[JOB]").toString())
               .setRequestId("requestId693933066")
               .build();
       CancelJobResponse response = batchServiceClient.cancelJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CancelJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CancelJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CancelJobResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadata)>` |   
  
### cancelJobAsync(String name)
    
    
    public final OperationFuture<CancelJobResponse,OperationMetadata> cancelJobAsync(String name)

Cancel a Job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       String name = JobName.of("[PROJECT]", "[LOCATION]", "[JOB]").toString();
       CancelJobResponse response = batchServiceClient.cancelJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Job name.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[CancelJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CancelJobResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadata)>` |   
  
### cancelJobCallable()
    
    
    public final UnaryCallable<CancelJobRequest,Operation> cancelJobCallable()

Cancel a Job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       CancelJobRequest request =
           CancelJobRequest.newBuilder()
               .setName(JobName.of("[PROJECT]", "[LOCATION]", "[JOB]").toString())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = batchServiceClient.cancelJobCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CancelJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### cancelJobOperationCallable()
    
    
    public final OperationCallable<CancelJobRequest,CancelJobResponse,OperationMetadata> cancelJobOperationCallable()

Cancel a Job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       CancelJobRequest request =
           CancelJobRequest.newBuilder()
               .setName(JobName.of("[PROJECT]", "[LOCATION]", "[JOB]").toString())
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<CancelJobResponse, OperationMetadata> future =
           batchServiceClient.cancelJobOperationCallable().futureCall(request);
       // Do something.
       CancelJobResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CancelJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CancelJobRequest),[CancelJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CancelJobResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadata)>` |   
  
### close()
    
    
    public final void close()

### createJob(@Nullable LocationName parent, Job job, String jobId)
    
    
    public final Job createJob(@Nullable LocationName parent, Job job, String jobId)

Create a Job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       Job job = Job.newBuilder().build();
       String jobId = "jobId101296568";
       Job response = batchServiceClient.createJob(parent, job, jobId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.batch.v1alpha.LocationName`  
Required. The parent resource name where the Job will be created. Pattern: "projects/{project}/locations/{location}"  
`job` | `[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)`  
Required. The Job to create.  
`jobId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
ID used to uniquely identify the Job within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and '-' are accepted. The '-' character cannot be the first or the last one. A system generated ID will be used if the field is not set. The job.name field in the request will be ignored and the created resource name of the Job will be "{parent}/jobs/{job_id}".  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)` |   
  
### createJob(CreateJobRequest request)
    
    
    public final Job createJob(CreateJobRequest request)

Create a Job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       CreateJobRequest request =
           CreateJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setJobId("jobId101296568")
               .setJob(Job.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Job response = batchServiceClient.createJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CreateJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)` |   
  
### createJob(String parent, Job job, String jobId)
    
    
    public final Job createJob(String parent, Job job, String jobId)

Create a Job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       Job job = Job.newBuilder().build();
       String jobId = "jobId101296568";
       Job response = batchServiceClient.createJob(parent, job, jobId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name where the Job will be created. Pattern: "projects/{project}/locations/{location}"  
`job` | `[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)`  
Required. The Job to create.  
`jobId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
ID used to uniquely identify the Job within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and '-' are accepted. The '-' character cannot be the first or the last one. A system generated ID will be used if the field is not set. The job.name field in the request will be ignored and the created resource name of the Job will be "{parent}/jobs/{job_id}".  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)` |   
  
### createJobCallable()
    
    
    public final UnaryCallable<CreateJobRequest,Job> createJobCallable()

Create a Job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       CreateJobRequest request =
           CreateJobRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setJobId("jobId101296568")
               .setJob(Job.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Job> future = batchServiceClient.createJobCallable().futureCall(request);
       // Do something.
       Job response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CreateJobRequest),[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)>` |   
  
### createResourceAllowance(@Nullable LocationName parent, ResourceAllowance resourceAllowance, String resourceAllowanceId)
    
    
    public final ResourceAllowance createResourceAllowance(@Nullable LocationName parent, ResourceAllowance resourceAllowance, String resourceAllowanceId)

Create a Resource Allowance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ResourceAllowance resourceAllowance = ResourceAllowance.newBuilder().build();
       String resourceAllowanceId = "resourceAllowanceId-786470299";
       ResourceAllowance response =
           batchServiceClient.createResourceAllowance(
               parent, resourceAllowance, resourceAllowanceId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.batch.v1alpha.LocationName`  
Required. The parent resource name where the ResourceAllowance will be created. Pattern: "projects/{project}/locations/{location}"  
`resourceAllowance` | `[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)`  
Required. The ResourceAllowance to create.  
`resourceAllowanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
ID used to uniquely identify the ResourceAllowance within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and '-' are accepted. The '-' character cannot be the first or the last one. A system generated ID will be used if the field is not set. The resource_allowance.name field in the request will be ignored and the created resource name of the ResourceAllowance will be "{parent}/resourceAllowances/{resource_allowance_id}".  
**Returns**  
---  
**Type** | **Description**  
`[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)` |   
  
### createResourceAllowance(CreateResourceAllowanceRequest request)
    
    
    public final ResourceAllowance createResourceAllowance(CreateResourceAllowanceRequest request)

Create a Resource Allowance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       CreateResourceAllowanceRequest request =
           CreateResourceAllowanceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setResourceAllowanceId("resourceAllowanceId-786470299")
               .setResourceAllowance(ResourceAllowance.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ResourceAllowance response = batchServiceClient.createResourceAllowance(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateResourceAllowanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CreateResourceAllowanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)` |   
  
### createResourceAllowance(String parent, ResourceAllowance resourceAllowance, String resourceAllowanceId)
    
    
    public final ResourceAllowance createResourceAllowance(String parent, ResourceAllowance resourceAllowance, String resourceAllowanceId)

Create a Resource Allowance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ResourceAllowance resourceAllowance = ResourceAllowance.newBuilder().build();
       String resourceAllowanceId = "resourceAllowanceId-786470299";
       ResourceAllowance response =
           batchServiceClient.createResourceAllowance(
               parent, resourceAllowance, resourceAllowanceId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name where the ResourceAllowance will be created. Pattern: "projects/{project}/locations/{location}"  
`resourceAllowance` | `[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)`  
Required. The ResourceAllowance to create.  
`resourceAllowanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
ID used to uniquely identify the ResourceAllowance within its parent scope. This field should contain at most 63 characters and must start with lowercase characters. Only lowercase characters, numbers and '-' are accepted. The '-' character cannot be the first or the last one. A system generated ID will be used if the field is not set. The resource_allowance.name field in the request will be ignored and the created resource name of the ResourceAllowance will be "{parent}/resourceAllowances/{resource_allowance_id}".  
**Returns**  
---  
**Type** | **Description**  
`[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)` |   
  
### createResourceAllowanceCallable()
    
    
    public final UnaryCallable<CreateResourceAllowanceRequest,ResourceAllowance> createResourceAllowanceCallable()

Create a Resource Allowance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       CreateResourceAllowanceRequest request =
           CreateResourceAllowanceRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setResourceAllowanceId("resourceAllowanceId-786470299")
               .setResourceAllowance(ResourceAllowance.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<ResourceAllowance> future =
           batchServiceClient.createResourceAllowanceCallable().futureCall(request);
       // Do something.
       ResourceAllowance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateResourceAllowanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.CreateResourceAllowanceRequest),[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)>` |   
  
### deleteJobAsync(DeleteJobRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteJobAsync(DeleteJobRequest request)

Delete a Job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       DeleteJobRequest request =
           DeleteJobRequest.newBuilder()
               .setName("name3373707")
               .setReason("reason-934964668")
               .setRequestId("requestId693933066")
               .build();
       batchServiceClient.deleteJobAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.DeleteJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadata)>` |   
  
### deleteJobAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteJobAsync(String name)

Delete a Job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       String name = "name3373707";
       batchServiceClient.deleteJobAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Job name.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadata)>` |   
  
### deleteJobCallable()
    
    
    public final UnaryCallable<DeleteJobRequest,Operation> deleteJobCallable()

Delete a Job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       DeleteJobRequest request =
           DeleteJobRequest.newBuilder()
               .setName("name3373707")
               .setReason("reason-934964668")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future = batchServiceClient.deleteJobCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.DeleteJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteJobOperationCallable()
    
    
    public final OperationCallable<DeleteJobRequest,Empty,OperationMetadata> deleteJobOperationCallable()

Delete a Job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       DeleteJobRequest request =
           DeleteJobRequest.newBuilder()
               .setName("name3373707")
               .setReason("reason-934964668")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           batchServiceClient.deleteJobOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.DeleteJobRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadata)>` |   
  
### deleteResourceAllowanceAsync(@Nullable ResourceAllowanceName name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteResourceAllowanceAsync(@Nullable ResourceAllowanceName name)

Delete a ResourceAllowance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       ResourceAllowanceName name =
           ResourceAllowanceName.of("[PROJECT]", "[LOCATION]", "[RESOURCE_ALLOWANCE]");
       batchServiceClient.deleteResourceAllowanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.batch.v1alpha.ResourceAllowanceName`  
Required. ResourceAllowance name.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadata)>` |   
  
### deleteResourceAllowanceAsync(DeleteResourceAllowanceRequest request)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteResourceAllowanceAsync(DeleteResourceAllowanceRequest request)

Delete a ResourceAllowance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       DeleteResourceAllowanceRequest request =
           DeleteResourceAllowanceRequest.newBuilder()
               .setName(
                   ResourceAllowanceName.of("[PROJECT]", "[LOCATION]", "[RESOURCE_ALLOWANCE]")
                       .toString())
               .setReason("reason-934964668")
               .setRequestId("requestId693933066")
               .build();
       batchServiceClient.deleteResourceAllowanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteResourceAllowanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.DeleteResourceAllowanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadata)>` |   
  
### deleteResourceAllowanceAsync(String name)
    
    
    public final OperationFuture<Empty,OperationMetadata> deleteResourceAllowanceAsync(String name)

Delete a ResourceAllowance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       String name =
           ResourceAllowanceName.of("[PROJECT]", "[LOCATION]", "[RESOURCE_ALLOWANCE]").toString();
       batchServiceClient.deleteResourceAllowanceAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ResourceAllowance name.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadata)>` |   
  
### deleteResourceAllowanceCallable()
    
    
    public final UnaryCallable<DeleteResourceAllowanceRequest,Operation> deleteResourceAllowanceCallable()

Delete a ResourceAllowance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       DeleteResourceAllowanceRequest request =
           DeleteResourceAllowanceRequest.newBuilder()
               .setName(
                   ResourceAllowanceName.of("[PROJECT]", "[LOCATION]", "[RESOURCE_ALLOWANCE]")
                       .toString())
               .setReason("reason-934964668")
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Operation> future =
           batchServiceClient.deleteResourceAllowanceCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteResourceAllowanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.DeleteResourceAllowanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteResourceAllowanceOperationCallable()
    
    
    public final OperationCallable<DeleteResourceAllowanceRequest,Empty,OperationMetadata> deleteResourceAllowanceOperationCallable()

Delete a ResourceAllowance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       DeleteResourceAllowanceRequest request =
           DeleteResourceAllowanceRequest.newBuilder()
               .setName(
                   ResourceAllowanceName.of("[PROJECT]", "[LOCATION]", "[RESOURCE_ALLOWANCE]")
                       .toString())
               .setReason("reason-934964668")
               .setRequestId("requestId693933066")
               .build();
       OperationFuture<Empty, OperationMetadata> future =
           batchServiceClient.deleteResourceAllowanceOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteResourceAllowanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.DeleteResourceAllowanceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.OperationMetadata)>` |   
  
### getHttpJsonOperationsClient()
    
    
    public final OperationsClient getHttpJsonOperationsClient()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns the OperationsClient that can be used to query the status of a long-running operation returned by another API method call.

**Returns**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.longrunning.OperationsClient.html)` |   
  
### getJob(@Nullable JobName name)
    
    
    public final Job getJob(@Nullable JobName name)

Get a Job specified by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       JobName name = JobName.of("[PROJECT]", "[LOCATION]", "[JOB]");
       Job response = batchServiceClient.getJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.batch.v1alpha.JobName`  
Required. Job name.  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)` |   
  
### getJob(GetJobRequest request)
    
    
    public final Job getJob(GetJobRequest request)

Get a Job specified by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       GetJobRequest request =
           GetJobRequest.newBuilder()
               .setName(JobName.of("[PROJECT]", "[LOCATION]", "[JOB]").toString())
               .build();
       Job response = batchServiceClient.getJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)` |   
  
### getJob(String name)
    
    
    public final Job getJob(String name)

Get a Job specified by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       String name = JobName.of("[PROJECT]", "[LOCATION]", "[JOB]").toString();
       Job response = batchServiceClient.getJob(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Job name.  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)` |   
  
### getJobCallable()
    
    
    public final UnaryCallable<GetJobRequest,Job> getJobCallable()

Get a Job specified by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       GetJobRequest request =
           GetJobRequest.newBuilder()
               .setName(JobName.of("[PROJECT]", "[LOCATION]", "[JOB]").toString())
               .build();
       ApiFuture<Job> future = batchServiceClient.getJobCallable().futureCall(request);
       // Do something.
       Job response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetJobRequest),[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = batchServiceClient.getLocation(request);
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
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future = batchServiceClient.getLocationCallable().futureCall(request);
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
  
### getResourceAllowance(@Nullable ResourceAllowanceName name)
    
    
    public final ResourceAllowance getResourceAllowance(@Nullable ResourceAllowanceName name)

Get a ResourceAllowance specified by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       ResourceAllowanceName name =
           ResourceAllowanceName.of("[PROJECT]", "[LOCATION]", "[RESOURCE_ALLOWANCE]");
       ResourceAllowance response = batchServiceClient.getResourceAllowance(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.batch.v1alpha.ResourceAllowanceName`  
Required. ResourceAllowance name.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)` |   
  
### getResourceAllowance(GetResourceAllowanceRequest request)
    
    
    public final ResourceAllowance getResourceAllowance(GetResourceAllowanceRequest request)

Get a ResourceAllowance specified by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       GetResourceAllowanceRequest request =
           GetResourceAllowanceRequest.newBuilder()
               .setName(
                   ResourceAllowanceName.of("[PROJECT]", "[LOCATION]", "[RESOURCE_ALLOWANCE]")
                       .toString())
               .build();
       ResourceAllowance response = batchServiceClient.getResourceAllowance(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetResourceAllowanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetResourceAllowanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)` |   
  
### getResourceAllowance(String name)
    
    
    public final ResourceAllowance getResourceAllowance(String name)

Get a ResourceAllowance specified by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       String name =
           ResourceAllowanceName.of("[PROJECT]", "[LOCATION]", "[RESOURCE_ALLOWANCE]").toString();
       ResourceAllowance response = batchServiceClient.getResourceAllowance(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. ResourceAllowance name.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)` |   
  
### getResourceAllowanceCallable()
    
    
    public final UnaryCallable<GetResourceAllowanceRequest,ResourceAllowance> getResourceAllowanceCallable()

Get a ResourceAllowance specified by its resource name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       GetResourceAllowanceRequest request =
           GetResourceAllowanceRequest.newBuilder()
               .setName(
                   ResourceAllowanceName.of("[PROJECT]", "[LOCATION]", "[RESOURCE_ALLOWANCE]")
                       .toString())
               .build();
       ApiFuture<ResourceAllowance> future =
           batchServiceClient.getResourceAllowanceCallable().futureCall(request);
       // Do something.
       ResourceAllowance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetResourceAllowanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetResourceAllowanceRequest),[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)>` |   
  
### getSettings()
    
    
    public final @Nullable BatchServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.batch.v1alpha.BatchServiceSettings` |   
  
### getStub()
    
    
    public BatchServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[BatchServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.stub.BatchServiceStub)` |   
  
### getTask(@Nullable TaskName name)
    
    
    public final Task getTask(@Nullable TaskName name)

Return a single Task.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       TaskName name = TaskName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[TASK_GROUP]", "[TASK]");
       Task response = batchServiceClient.getTask(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.batch.v1alpha.TaskName`  
Required. Task name.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Task)` |   
  
### getTask(GetTaskRequest request)
    
    
    public final Task getTask(GetTaskRequest request)

Return a single Task.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       GetTaskRequest request =
           GetTaskRequest.newBuilder()
               .setName(
                   TaskName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[TASK_GROUP]", "[TASK]")
                       .toString())
               .build();
       Task response = batchServiceClient.getTask(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetTaskRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Task)` |   
  
### getTask(String name)
    
    
    public final Task getTask(String name)

Return a single Task.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       String name =
           TaskName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[TASK_GROUP]", "[TASK]").toString();
       Task response = batchServiceClient.getTask(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Task name.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Task)` |   
  
### getTaskCallable()
    
    
    public final UnaryCallable<GetTaskRequest,Task> getTaskCallable()

Return a single Task.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       GetTaskRequest request =
           GetTaskRequest.newBuilder()
               .setName(
                   TaskName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[TASK_GROUP]", "[TASK]")
                       .toString())
               .build();
       ApiFuture<Task> future = batchServiceClient.getTaskCallable().futureCall(request);
       // Do something.
       Task response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetTaskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.GetTaskRequest),[Task](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Task)>` |   
  
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
  
### listJobs(ListJobsRequest request)
    
    
    public final BatchServiceClient.ListJobsPagedResponse listJobs(ListJobsRequest request)

List all Jobs for a project within a region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       ListJobsRequest request =
           ListJobsRequest.newBuilder()
               .setParent("parent-995424086")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Job element : batchServiceClient.listJobs(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListJobsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchServiceClient.ListJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListJobsPagedResponse)` |   
  
### listJobs(String parent)
    
    
    public final BatchServiceClient.ListJobsPagedResponse listJobs(String parent)

List all Jobs for a project within a region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       String parent = "parent-995424086";
       for (Job element : batchServiceClient.listJobs(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Parent path.  
**Returns**  
---  
**Type** | **Description**  
`[BatchServiceClient.ListJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListJobsPagedResponse)` |   
  
### listJobsCallable()
    
    
    public final UnaryCallable<ListJobsRequest,ListJobsResponse> listJobsCallable()

List all Jobs for a project within a region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       ListJobsRequest request =
           ListJobsRequest.newBuilder()
               .setParent("parent-995424086")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListJobsResponse response = batchServiceClient.listJobsCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListJobsRequest),[ListJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListJobsResponse)>` |   
  
### listJobsPagedCallable()
    
    
    public final UnaryCallable<ListJobsRequest,BatchServiceClient.ListJobsPagedResponse> listJobsPagedCallable()

List all Jobs for a project within a region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       ListJobsRequest request =
           ListJobsRequest.newBuilder()
               .setParent("parent-995424086")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Job> future = batchServiceClient.listJobsPagedCallable().futureCall(request);
       // Do something.
       for (Job element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListJobsRequest),[ListJobsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListJobsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final BatchServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : batchServiceClient.listLocations(request).iterateAll()) {
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
`[BatchServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListLocationsPagedResponse)` |   
  
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
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response = batchServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,BatchServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

This method lists locations based on the resource scope provided inthe ListLocationsRequest.name field: ***Global locations**: If `name` is empty, the method lists thepublic locations available to all projects. * **Project-specificlocations**: If `name` follows the format`projects/{project}`, the method lists locations visible to thatspecific project. This includes public, private, or otherproject-specific locations enabled for the project.

For gRPC and client library implementations, the resource name ispassed as the `name` field. For direct service calls, the resourcename isincorporated into the request path based on the specific serviceimplementation and version.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           batchServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListLocationsPagedResponse)>` |   
  
### listResourceAllowances(@Nullable LocationName parent)
    
    
    public final BatchServiceClient.ListResourceAllowancesPagedResponse listResourceAllowances(@Nullable LocationName parent)

List all ResourceAllowances for a project within a region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ResourceAllowance element :
           batchServiceClient.listResourceAllowances(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.batch.v1alpha.LocationName`  
Required. Parent path.  
**Returns**  
---  
**Type** | **Description**  
`[BatchServiceClient.ListResourceAllowancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListResourceAllowancesPagedResponse)` |   
  
### listResourceAllowances(ListResourceAllowancesRequest request)
    
    
    public final BatchServiceClient.ListResourceAllowancesPagedResponse listResourceAllowances(ListResourceAllowancesRequest request)

List all ResourceAllowances for a project within a region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       ListResourceAllowancesRequest request =
           ListResourceAllowancesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ResourceAllowance element :
           batchServiceClient.listResourceAllowances(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListResourceAllowancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListResourceAllowancesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchServiceClient.ListResourceAllowancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListResourceAllowancesPagedResponse)` |   
  
### listResourceAllowances(String parent)
    
    
    public final BatchServiceClient.ListResourceAllowancesPagedResponse listResourceAllowances(String parent)

List all ResourceAllowances for a project within a region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ResourceAllowance element :
           batchServiceClient.listResourceAllowances(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Parent path.  
**Returns**  
---  
**Type** | **Description**  
`[BatchServiceClient.ListResourceAllowancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListResourceAllowancesPagedResponse)` |   
  
### listResourceAllowancesCallable()
    
    
    public final UnaryCallable<ListResourceAllowancesRequest,ListResourceAllowancesResponse> listResourceAllowancesCallable()

List all ResourceAllowances for a project within a region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       ListResourceAllowancesRequest request =
           ListResourceAllowancesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListResourceAllowancesResponse response =
             batchServiceClient.listResourceAllowancesCallable().call(request);
         for (ResourceAllowance element : response.getResourceAllowancesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListResourceAllowancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListResourceAllowancesRequest),[ListResourceAllowancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListResourceAllowancesResponse)>` |   
  
### listResourceAllowancesPagedCallable()
    
    
    public final UnaryCallable<ListResourceAllowancesRequest,BatchServiceClient.ListResourceAllowancesPagedResponse> listResourceAllowancesPagedCallable()

List all ResourceAllowances for a project within a region.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       ListResourceAllowancesRequest request =
           ListResourceAllowancesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ResourceAllowance> future =
           batchServiceClient.listResourceAllowancesPagedCallable().futureCall(request);
       // Do something.
       for (ResourceAllowance element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListResourceAllowancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListResourceAllowancesRequest),[ListResourceAllowancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListResourceAllowancesPagedResponse)>` |   
  
### listTasks(@Nullable TaskGroupName parent)
    
    
    public final BatchServiceClient.ListTasksPagedResponse listTasks(@Nullable TaskGroupName parent)

List Tasks associated with a job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       TaskGroupName parent = TaskGroupName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[TASK_GROUP]");
       for (Task element : batchServiceClient.listTasks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.batch.v1alpha.TaskGroupName`  
Required. Name of a TaskGroup from which Tasks are being requested. Pattern: "projects/{project}/locations/{location}/jobs/{job}/taskGroups/{task_group}"  
**Returns**  
---  
**Type** | **Description**  
`[BatchServiceClient.ListTasksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListTasksPagedResponse)` |   
  
### listTasks(ListTasksRequest request)
    
    
    public final BatchServiceClient.ListTasksPagedResponse listTasks(ListTasksRequest request)

List Tasks associated with a job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       ListTasksRequest request =
           ListTasksRequest.newBuilder()
               .setParent(
                   TaskGroupName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[TASK_GROUP]").toString())
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Task element : batchServiceClient.listTasks(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTasksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListTasksRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchServiceClient.ListTasksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListTasksPagedResponse)` |   
  
### listTasks(String parent)
    
    
    public final BatchServiceClient.ListTasksPagedResponse listTasks(String parent)

List Tasks associated with a job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       String parent =
           TaskGroupName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[TASK_GROUP]").toString();
       for (Task element : batchServiceClient.listTasks(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of a TaskGroup from which Tasks are being requested. Pattern: "projects/{project}/locations/{location}/jobs/{job}/taskGroups/{task_group}"  
**Returns**  
---  
**Type** | **Description**  
`[BatchServiceClient.ListTasksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListTasksPagedResponse)` |   
  
### listTasksCallable()
    
    
    public final UnaryCallable<ListTasksRequest,ListTasksResponse> listTasksCallable()

List Tasks associated with a job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       ListTasksRequest request =
           ListTasksRequest.newBuilder()
               .setParent(
                   TaskGroupName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[TASK_GROUP]").toString())
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListTasksResponse response = batchServiceClient.listTasksCallable().call(request);
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTasksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListTasksRequest),[ListTasksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListTasksResponse)>` |   
  
### listTasksPagedCallable()
    
    
    public final UnaryCallable<ListTasksRequest,BatchServiceClient.ListTasksPagedResponse> listTasksPagedCallable()

List Tasks associated with a job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       ListTasksRequest request =
           ListTasksRequest.newBuilder()
               .setParent(
                   TaskGroupName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[TASK_GROUP]").toString())
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Task> future = batchServiceClient.listTasksPagedCallable().futureCall(request);
       // Do something.
       for (Task element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListTasksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ListTasksRequest),[ListTasksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.BatchServiceClient.ListTasksPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateJob(Job job, FieldMask updateMask)
    
    
    public final Job updateJob(Job job, FieldMask updateMask)

Update a Job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       Job job = Job.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Job response = batchServiceClient.updateJob(job, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`job` | `[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)`  
Required. The Job to update. Only fields specified in `updateMask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Mask of fields to update. The `jobs.patch` method can only be used while a job is in the `QUEUED`, `SCHEDULED`, or `RUNNING` state and currently only supports increasing the value of the first `taskCount` field in the job's `taskGroups` field. Therefore, you must set the value of `updateMask` to `taskGroups`. Any other job fields in the update request will be ignored. For example, to update a job's `taskCount` to `2`, set `updateMask` to `taskGroups` and use the following request body: `<code> { "taskGroups":[{ "taskCount": 2 }] } </code>`  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)` |   
  
### updateJob(UpdateJobRequest request)
    
    
    public final Job updateJob(UpdateJobRequest request)

Update a Job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       UpdateJobRequest request =
           UpdateJobRequest.newBuilder()
               .setJob(Job.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Job response = batchServiceClient.updateJob(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UpdateJobRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)` |   
  
### updateJobCallable()
    
    
    public final UnaryCallable<UpdateJobRequest,Job> updateJobCallable()

Update a Job.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       UpdateJobRequest request =
           UpdateJobRequest.newBuilder()
               .setJob(Job.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Job> future = batchServiceClient.updateJobCallable().futureCall(request);
       // Do something.
       Job response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UpdateJobRequest),[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.Job)>` |   
  
### updateResourceAllowance(ResourceAllowance resourceAllowance, FieldMask updateMask)
    
    
    public final ResourceAllowance updateResourceAllowance(ResourceAllowance resourceAllowance, FieldMask updateMask)

Update a Resource Allowance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       ResourceAllowance resourceAllowance = ResourceAllowance.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ResourceAllowance response =
           batchServiceClient.updateResourceAllowance(resourceAllowance, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`resourceAllowance` | `[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)`  
Required. The ResourceAllowance to update. Update description. Only fields specified in `update_mask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Mask of fields to update. Field mask is used to specify the fields to be overwritten in the ResourceAllowance resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. UpdateResourceAllowance request now only supports update on `limit` field.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)` |   
  
### updateResourceAllowance(UpdateResourceAllowanceRequest request)
    
    
    public final ResourceAllowance updateResourceAllowance(UpdateResourceAllowanceRequest request)

Update a Resource Allowance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       UpdateResourceAllowanceRequest request =
           UpdateResourceAllowanceRequest.newBuilder()
               .setResourceAllowance(ResourceAllowance.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ResourceAllowance response = batchServiceClient.updateResourceAllowance(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateResourceAllowanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UpdateResourceAllowanceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)` |   
  
### updateResourceAllowanceCallable()
    
    
    public final UnaryCallable<UpdateResourceAllowanceRequest,ResourceAllowance> updateResourceAllowanceCallable()

Update a Resource Allowance.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (BatchServiceClient batchServiceClient = BatchServiceClient.create()) {
       UpdateResourceAllowanceRequest request =
           UpdateResourceAllowanceRequest.newBuilder()
               .setResourceAllowance(ResourceAllowance.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<ResourceAllowance> future =
           batchServiceClient.updateResourceAllowanceCallable().futureCall(request);
       // Do something.
       ResourceAllowance response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateResourceAllowanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.UpdateResourceAllowanceRequest),[ResourceAllowance](https://docs.cloud.google.com/java/docs/reference/google-cloud-batch/latest/com.google.cloud.batch.v1alpha.ResourceAllowance)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
