---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ExecutionsClient
title: Class ExecutionsClient (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:22.620632+00:00
---

# Class ExecutionsClient (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ExecutionsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ExecutionsClient (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.5  0.2.1  0.1.2 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-run/google-cloud-run/src/main/java/com/google/cloud/run/v2/ExecutionsClient.java)| [Product Reference](https://cloud.google.com/run/docs)| [REST Documentation](https://cloud.google.com/run/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/run/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Cloud Run Execution Control Plane API.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       ExecutionName name = ExecutionName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[EXECUTION]");
       Execution response = executionsClient.getExecution(name);
     }
     

Note: close() needs to be called on the ExecutionsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetExecution |  Gets information about an Execution. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getExecution(GetExecutionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getExecution(ExecutionName name) 
  * getExecution(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getExecutionCallable() 

  
ListExecutions |  Lists Executions from a Job. Results are sorted by creation time, descending. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listExecutions(ListExecutionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listExecutions(JobName parent) 
  * listExecutions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listExecutionsPagedCallable() 
  * listExecutionsCallable() 

  
DeleteExecution |  Deletes an Execution. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteExecutionAsync(DeleteExecutionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteExecutionAsync(ExecutionName name) 
  * deleteExecutionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteExecutionOperationCallable() 
  * deleteExecutionCallable() 

  
CancelExecution |  Cancels an Execution. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelExecutionAsync(CancelExecutionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * cancelExecutionAsync(ExecutionName name) 
  * cancelExecutionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelExecutionOperationCallable() 
  * cancelExecutionCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ExecutionsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ExecutionsSettings executionsSettings =
         ExecutionsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ExecutionsClient executionsClient = ExecutionsClient.create(executionsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ExecutionsSettings executionsSettings =
         ExecutionsSettings.newBuilder().setEndpoint(myEndpoint).build();
     ExecutionsClient executionsClient = ExecutionsClient.create(executionsSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ExecutionsSettings executionsSettings = ExecutionsSettings.newHttpJsonBuilder().build();
     ExecutionsClient executionsClient = ExecutionsClient.create(executionsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ExecutionsClient

## Static Methods 

### create()
    
    
    public static final ExecutionsClient create()

Constructs an instance of ExecutionsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ExecutionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ExecutionsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ExecutionsSettings settings)
    
    
    public static final ExecutionsClient create(ExecutionsSettings settings)

Constructs an instance of ExecutionsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ExecutionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ExecutionsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExecutionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ExecutionsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ExecutionsStub stub)
    
    
    public static final ExecutionsClient create(ExecutionsStub stub)

Constructs an instance of ExecutionsClient, using the given stub for making calls. This is for advanced usage - prefer using create(ExecutionsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ExecutionsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.stub.ExecutionsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExecutionsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ExecutionsClient)` |   
  
## Constructors 

### ExecutionsClient(ExecutionsSettings settings)
    
    
    protected ExecutionsClient(ExecutionsSettings settings)

Constructs an instance of ExecutionsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ExecutionsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ExecutionsSettings)`  
  
  
### ExecutionsClient(ExecutionsStub stub)
    
    
    protected ExecutionsClient(ExecutionsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ExecutionsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.stub.ExecutionsStub)`  
  
  
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
  
### cancelExecutionAsync(@Nullable ExecutionName name)
    
    
    public final OperationFuture<Execution,Execution> cancelExecutionAsync(@Nullable ExecutionName name)

Cancels an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       ExecutionName name = ExecutionName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[EXECUTION]");
       Execution response = executionsClient.cancelExecutionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.run.v2.ExecutionName`  
Required. The name of the Execution to cancel. Format: `projects/{project}/locations/{location}/jobs/{job}/executions/{execution}`, where `{project}` can be project id or number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution),[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution)>` |   
  
### cancelExecutionAsync(CancelExecutionRequest request)
    
    
    public final OperationFuture<Execution,Execution> cancelExecutionAsync(CancelExecutionRequest request)

Cancels an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       CancelExecutionRequest request =
           CancelExecutionRequest.newBuilder()
               .setName(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[EXECUTION]").toString())
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       Execution response = executionsClient.cancelExecutionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.CancelExecutionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution),[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution)>` |   
  
### cancelExecutionAsync(String name)
    
    
    public final OperationFuture<Execution,Execution> cancelExecutionAsync(String name)

Cancels an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       String name = ExecutionName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[EXECUTION]").toString();
       Execution response = executionsClient.cancelExecutionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Execution to cancel. Format: `projects/{project}/locations/{location}/jobs/{job}/executions/{execution}`, where `{project}` can be project id or number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution),[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution)>` |   
  
### cancelExecutionCallable()
    
    
    public final UnaryCallable<CancelExecutionRequest,Operation> cancelExecutionCallable()

Cancels an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       CancelExecutionRequest request =
           CancelExecutionRequest.newBuilder()
               .setName(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[EXECUTION]").toString())
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future = executionsClient.cancelExecutionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.CancelExecutionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### cancelExecutionOperationCallable()
    
    
    public final OperationCallable<CancelExecutionRequest,Execution,Execution> cancelExecutionOperationCallable()

Cancels an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       CancelExecutionRequest request =
           CancelExecutionRequest.newBuilder()
               .setName(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[EXECUTION]").toString())
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       OperationFuture<Execution, Execution> future =
           executionsClient.cancelExecutionOperationCallable().futureCall(request);
       // Do something.
       Execution response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CancelExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.CancelExecutionRequest),[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution),[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution)>` |   
  
### close()
    
    
    public final void close()

### deleteExecutionAsync(@Nullable ExecutionName name)
    
    
    public final OperationFuture<Execution,Execution> deleteExecutionAsync(@Nullable ExecutionName name)

Deletes an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       ExecutionName name = ExecutionName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[EXECUTION]");
       Execution response = executionsClient.deleteExecutionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.run.v2.ExecutionName`  
Required. The name of the Execution to delete. Format: `projects/{project}/locations/{location}/jobs/{job}/executions/{execution}`, where `{project}` can be project id or number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution),[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution)>` |   
  
### deleteExecutionAsync(DeleteExecutionRequest request)
    
    
    public final OperationFuture<Execution,Execution> deleteExecutionAsync(DeleteExecutionRequest request)

Deletes an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       DeleteExecutionRequest request =
           DeleteExecutionRequest.newBuilder()
               .setName(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[EXECUTION]").toString())
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       Execution response = executionsClient.deleteExecutionAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.DeleteExecutionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution),[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution)>` |   
  
### deleteExecutionAsync(String name)
    
    
    public final OperationFuture<Execution,Execution> deleteExecutionAsync(String name)

Deletes an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       String name = ExecutionName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[EXECUTION]").toString();
       Execution response = executionsClient.deleteExecutionAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the Execution to delete. Format: `projects/{project}/locations/{location}/jobs/{job}/executions/{execution}`, where `{project}` can be project id or number.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution),[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution)>` |   
  
### deleteExecutionCallable()
    
    
    public final UnaryCallable<DeleteExecutionRequest,Operation> deleteExecutionCallable()

Deletes an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       DeleteExecutionRequest request =
           DeleteExecutionRequest.newBuilder()
               .setName(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[EXECUTION]").toString())
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       ApiFuture<Operation> future = executionsClient.deleteExecutionCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.DeleteExecutionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteExecutionOperationCallable()
    
    
    public final OperationCallable<DeleteExecutionRequest,Execution,Execution> deleteExecutionOperationCallable()

Deletes an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       DeleteExecutionRequest request =
           DeleteExecutionRequest.newBuilder()
               .setName(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[EXECUTION]").toString())
               .setValidateOnly(true)
               .setEtag("etag3123477")
               .build();
       OperationFuture<Execution, Execution> future =
           executionsClient.deleteExecutionOperationCallable().futureCall(request);
       // Do something.
       Execution response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.DeleteExecutionRequest),[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution),[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution)>` |   
  
### getExecution(@Nullable ExecutionName name)
    
    
    public final Execution getExecution(@Nullable ExecutionName name)

Gets information about an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       ExecutionName name = ExecutionName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[EXECUTION]");
       Execution response = executionsClient.getExecution(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.run.v2.ExecutionName`  
Required. The full name of the Execution. Format: `projects/{project}/locations/{location}/jobs/{job}/executions/{execution}`, where `{project}` can be project id or number.  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution)` |   
  
### getExecution(GetExecutionRequest request)
    
    
    public final Execution getExecution(GetExecutionRequest request)

Gets information about an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       GetExecutionRequest request =
           GetExecutionRequest.newBuilder()
               .setName(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[EXECUTION]").toString())
               .build();
       Execution response = executionsClient.getExecution(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.GetExecutionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution)` |   
  
### getExecution(String name)
    
    
    public final Execution getExecution(String name)

Gets information about an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       String name = ExecutionName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[EXECUTION]").toString();
       Execution response = executionsClient.getExecution(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The full name of the Execution. Format: `projects/{project}/locations/{location}/jobs/{job}/executions/{execution}`, where `{project}` can be project id or number.  
**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution)` |   
  
### getExecutionCallable()
    
    
    public final UnaryCallable<GetExecutionRequest,Execution> getExecutionCallable()

Gets information about an Execution.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       GetExecutionRequest request =
           GetExecutionRequest.newBuilder()
               .setName(
                   ExecutionName.of("[PROJECT]", "[LOCATION]", "[JOB]", "[EXECUTION]").toString())
               .build();
       ApiFuture<Execution> future = executionsClient.getExecutionCallable().futureCall(request);
       // Do something.
       Execution response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.GetExecutionRequest),[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution)>` |   
  
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
    
    
    public final @Nullable ExecutionsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.run.v2.ExecutionsSettings` |   
  
### getStub()
    
    
    public ExecutionsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ExecutionsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.stub.ExecutionsStub)` |   
  
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
  
### listExecutions(@Nullable JobName parent)
    
    
    public final ExecutionsClient.ListExecutionsPagedResponse listExecutions(@Nullable JobName parent)

Lists Executions from a Job. Results are sorted by creation time, descending.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       JobName parent = JobName.of("[PROJECT]", "[LOCATION]", "[JOB]");
       for (Execution element : executionsClient.listExecutions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.run.v2.JobName`  
Required. The Execution from which the Executions should be listed. To list all Executions across Jobs, use "-" instead of Job name. Format: `projects/{project}/locations/{location}/jobs/{job}`, where `{project}` can be project id or number.  
**Returns**  
---  
**Type** | **Description**  
`[ExecutionsClient.ListExecutionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ExecutionsClient.ListExecutionsPagedResponse)` |   
  
### listExecutions(ListExecutionsRequest request)
    
    
    public final ExecutionsClient.ListExecutionsPagedResponse listExecutions(ListExecutionsRequest request)

Lists Executions from a Job. Results are sorted by creation time, descending.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       ListExecutionsRequest request =
           ListExecutionsRequest.newBuilder()
               .setParent(JobName.of("[PROJECT]", "[LOCATION]", "[JOB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setShowDeleted(true)
               .build();
       for (Execution element : executionsClient.listExecutions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ListExecutionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ExecutionsClient.ListExecutionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ExecutionsClient.ListExecutionsPagedResponse)` |   
  
### listExecutions(String parent)
    
    
    public final ExecutionsClient.ListExecutionsPagedResponse listExecutions(String parent)

Lists Executions from a Job. Results are sorted by creation time, descending.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       String parent = JobName.of("[PROJECT]", "[LOCATION]", "[JOB]").toString();
       for (Execution element : executionsClient.listExecutions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The Execution from which the Executions should be listed. To list all Executions across Jobs, use "-" instead of Job name. Format: `projects/{project}/locations/{location}/jobs/{job}`, where `{project}` can be project id or number.  
**Returns**  
---  
**Type** | **Description**  
`[ExecutionsClient.ListExecutionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ExecutionsClient.ListExecutionsPagedResponse)` |   
  
### listExecutionsCallable()
    
    
    public final UnaryCallable<ListExecutionsRequest,ListExecutionsResponse> listExecutionsCallable()

Lists Executions from a Job. Results are sorted by creation time, descending.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       ListExecutionsRequest request =
           ListExecutionsRequest.newBuilder()
               .setParent(JobName.of("[PROJECT]", "[LOCATION]", "[JOB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setShowDeleted(true)
               .build();
       while (true) {
         ListExecutionsResponse response = executionsClient.listExecutionsCallable().call(request);
         for (Execution element : response.getExecutionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ListExecutionsRequest),[ListExecutionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ListExecutionsResponse)>` |   
  
### listExecutionsPagedCallable()
    
    
    public final UnaryCallable<ListExecutionsRequest,ExecutionsClient.ListExecutionsPagedResponse> listExecutionsPagedCallable()

Lists Executions from a Job. Results are sorted by creation time, descending.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ExecutionsClient executionsClient = ExecutionsClient.create()) {
       ListExecutionsRequest request =
           ListExecutionsRequest.newBuilder()
               .setParent(JobName.of("[PROJECT]", "[LOCATION]", "[JOB]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setShowDeleted(true)
               .build();
       ApiFuture<Execution> future =
           executionsClient.listExecutionsPagedCallable().futureCall(request);
       // Do something.
       for (Execution element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ListExecutionsRequest),[ListExecutionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ExecutionsClient.ListExecutionsPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
