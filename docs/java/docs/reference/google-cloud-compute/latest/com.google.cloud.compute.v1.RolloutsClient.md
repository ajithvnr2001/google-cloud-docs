---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutsClient
title: Class RolloutsClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:17.674688+00:00
---

# Class RolloutsClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RolloutsClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RolloutsClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The Rollouts API.

This client uses Rollouts version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       String project = "project-309310695";
       String rollout = "rollout1377108401";
       Rollout response = rolloutsClient.get(project, rollout);
     }
     

Note: close() needs to be called on the RolloutsClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Advance |  Advances a Rollout to the next wave, or completes it if no waves remain. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * advanceAsync(AdvanceRolloutRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * advanceAsync(String project, String rollout) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * advanceOperationCallable() 
  * advanceCallable() 

  
Cancel |  Cancels a Rollout. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * cancelAsync(CancelRolloutRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * cancelAsync(String project, String rollout) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * cancelOperationCallable() 
  * cancelCallable() 

  
Delete |  Deletes a Rollout. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRolloutRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String rollout) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Gets details of a single project-scoped Rollout. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRolloutRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String rollout) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
List |  Lists Rollouts in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRolloutsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
Pause |  Pauses a Rollout. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * pauseAsync(PauseRolloutRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * pauseAsync(String project, String rollout) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * pauseOperationCallable() 
  * pauseCallable() 

  
Resume |  Resumes a Rollout. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * resumeAsync(ResumeRolloutRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * resumeAsync(String project, String rollout) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * resumeOperationCallable() 
  * resumeCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RolloutsSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RolloutsSettings rolloutsSettings =
         RolloutsSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RolloutsClient rolloutsClient = RolloutsClient.create(rolloutsSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RolloutsSettings rolloutsSettings =
         RolloutsSettings.newBuilder().setEndpoint(myEndpoint).build();
     RolloutsClient rolloutsClient = RolloutsClient.create(rolloutsSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RolloutsClient

## Static Methods 

### create()
    
    
    public static final RolloutsClient create()

Constructs an instance of RolloutsClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RolloutsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RolloutsSettings settings)
    
    
    public static final RolloutsClient create(RolloutsSettings settings)

Constructs an instance of RolloutsClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RolloutsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutsSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RolloutsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutsClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RolloutsStub stub)
    
    
    public static final RolloutsClient create(RolloutsStub stub)

Constructs an instance of RolloutsClient, using the given stub for making calls. This is for advanced usage - prefer using create(RolloutsSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RolloutsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RolloutsStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RolloutsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutsClient)` |   
  
## Constructors 

### RolloutsClient(RolloutsSettings settings)
    
    
    protected RolloutsClient(RolloutsSettings settings)

Constructs an instance of RolloutsClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RolloutsSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutsSettings)`  
  
  
### RolloutsClient(RolloutsStub stub)
    
    
    protected RolloutsClient(RolloutsStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RolloutsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RolloutsStub)`  
  
  
## Methods 

### advanceAsync(AdvanceRolloutRequest request)
    
    
    public final OperationFuture<Operation,Operation> advanceAsync(AdvanceRolloutRequest request)

Advances a Rollout to the next wave, or completes it if no waves remain.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       AdvanceRolloutRequest request =
           AdvanceRolloutRequest.newBuilder()
               .setCurrentWaveNumber(-1432331895)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRollout("rollout1377108401")
               .build();
       Operation response = rolloutsClient.advanceAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AdvanceRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AdvanceRolloutRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### advanceAsync(String project, String rollout)
    
    
    public final OperationFuture<Operation,Operation> advanceAsync(String project, String rollout)

Advances a Rollout to the next wave, or completes it if no waves remain.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       String project = "project-309310695";
       String rollout = "rollout1377108401";
       Operation response = rolloutsClient.advanceAsync(project, rollout).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Project ID for this request.  
`rollout` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the Rollout resource to advance.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### advanceCallable()
    
    
    public final UnaryCallable<AdvanceRolloutRequest,Operation> advanceCallable()

Advances a Rollout to the next wave, or completes it if no waves remain.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       AdvanceRolloutRequest request =
           AdvanceRolloutRequest.newBuilder()
               .setCurrentWaveNumber(-1432331895)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRollout("rollout1377108401")
               .build();
       ApiFuture<Operation> future = rolloutsClient.advanceCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[AdvanceRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AdvanceRolloutRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### advanceOperationCallable()
    
    
    public final OperationCallable<AdvanceRolloutRequest,Operation,Operation> advanceOperationCallable()

Advances a Rollout to the next wave, or completes it if no waves remain.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       AdvanceRolloutRequest request =
           AdvanceRolloutRequest.newBuilder()
               .setCurrentWaveNumber(-1432331895)
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRollout("rollout1377108401")
               .build();
       OperationFuture<Operation, Operation> future =
           rolloutsClient.advanceOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[AdvanceRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AdvanceRolloutRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### cancelAsync(CancelRolloutRequest request)
    
    
    public final OperationFuture<Operation,Operation> cancelAsync(CancelRolloutRequest request)

Cancels a Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       CancelRolloutRequest request =
           CancelRolloutRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRollback(true)
               .setRollout("rollout1377108401")
               .build();
       Operation response = rolloutsClient.cancelAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CancelRolloutRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cancelAsync(String project, String rollout)
    
    
    public final OperationFuture<Operation,Operation> cancelAsync(String project, String rollout)

Cancels a Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       String project = "project-309310695";
       String rollout = "rollout1377108401";
       Operation response = rolloutsClient.cancelAsync(project, rollout).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`rollout` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Rollout resource to cancel.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cancelCallable()
    
    
    public final UnaryCallable<CancelRolloutRequest,Operation> cancelCallable()

Cancels a Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       CancelRolloutRequest request =
           CancelRolloutRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRollback(true)
               .setRollout("rollout1377108401")
               .build();
       ApiFuture<Operation> future = rolloutsClient.cancelCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CancelRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CancelRolloutRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### cancelOperationCallable()
    
    
    public final OperationCallable<CancelRolloutRequest,Operation,Operation> cancelOperationCallable()

Cancels a Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       CancelRolloutRequest request =
           CancelRolloutRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRollback(true)
               .setRollout("rollout1377108401")
               .build();
       OperationFuture<Operation, Operation> future =
           rolloutsClient.cancelOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CancelRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CancelRolloutRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### close()
    
    
    public final void close()

### deleteAsync(DeleteRolloutRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRolloutRequest request)

Deletes a Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       DeleteRolloutRequest request =
           DeleteRolloutRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRollout("rollout1377108401")
               .build();
       Operation response = rolloutsClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRolloutRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String rollout)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String rollout)

Deletes a Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       String project = "project-309310695";
       String rollout = "rollout1377108401";
       Operation response = rolloutsClient.deleteAsync(project, rollout).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`rollout` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the Rollout resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRolloutRequest,Operation> deleteCallable()

Deletes a Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       DeleteRolloutRequest request =
           DeleteRolloutRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRollout("rollout1377108401")
               .build();
       ApiFuture<Operation> future = rolloutsClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRolloutRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRolloutRequest,Operation,Operation> deleteOperationCallable()

Deletes a Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       DeleteRolloutRequest request =
           DeleteRolloutRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRollout("rollout1377108401")
               .build();
       OperationFuture<Operation, Operation> future =
           rolloutsClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRolloutRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRolloutRequest request)
    
    
    public final Rollout get(GetRolloutRequest request)

Gets details of a single project-scoped Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       GetRolloutRequest request =
           GetRolloutRequest.newBuilder()
               .setProject("project-309310695")
               .setRollout("rollout1377108401")
               .build();
       Rollout response = rolloutsClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRolloutRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Rollout)` |   
  
### get(String project, String rollout)
    
    
    public final Rollout get(String project, String rollout)

Gets details of a single project-scoped Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       String project = "project-309310695";
       String rollout = "rollout1377108401";
       Rollout response = rolloutsClient.get(project, rollout);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`rollout` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the persistent rollout to return.  
**Returns**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Rollout)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRolloutRequest,Rollout> getCallable()

Gets details of a single project-scoped Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       GetRolloutRequest request =
           GetRolloutRequest.newBuilder()
               .setProject("project-309310695")
               .setRollout("rollout1377108401")
               .build();
       ApiFuture<Rollout> future = rolloutsClient.getCallable().futureCall(request);
       // Do something.
       Rollout response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRolloutRequest),[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Rollout)>` |   
  
### getSettings()
    
    
    public final @Nullable RolloutsSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RolloutsSettings` |   
  
### getStub()
    
    
    public RolloutsStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RolloutsStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RolloutsStub)` |   
  
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
  
### list(ListRolloutsRequest request)
    
    
    public final RolloutsClient.ListPagedResponse list(ListRolloutsRequest request)

Lists Rollouts in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       ListRolloutsRequest request =
           ListRolloutsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (Rollout element : rolloutsClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRolloutsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRolloutsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RolloutsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutsClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final RolloutsClient.ListPagedResponse list(String project)

Lists Rollouts in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       String project = "project-309310695";
       for (Rollout element : rolloutsClient.list(project).iterateAll()) {
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
`[RolloutsClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutsClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRolloutsRequest,RolloutsListResponse> listCallable()

Lists Rollouts in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       ListRolloutsRequest request =
           ListRolloutsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         RolloutsListResponse response = rolloutsClient.listCallable().call(request);
         for (Rollout element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRolloutsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRolloutsRequest),[RolloutsListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutsListResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRolloutsRequest,RolloutsClient.ListPagedResponse> listPagedCallable()

Lists Rollouts in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       ListRolloutsRequest request =
           ListRolloutsRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<Rollout> future = rolloutsClient.listPagedCallable().futureCall(request);
       // Do something.
       for (Rollout element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRolloutsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRolloutsRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutsClient.ListPagedResponse)>` |   
  
### pauseAsync(PauseRolloutRequest request)
    
    
    public final OperationFuture<Operation,Operation> pauseAsync(PauseRolloutRequest request)

Pauses a Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       PauseRolloutRequest request =
           PauseRolloutRequest.newBuilder()
               .setEtag("etag3123477")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRollout("rollout1377108401")
               .build();
       Operation response = rolloutsClient.pauseAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PauseRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PauseRolloutRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### pauseAsync(String project, String rollout)
    
    
    public final OperationFuture<Operation,Operation> pauseAsync(String project, String rollout)

Pauses a Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       String project = "project-309310695";
       String rollout = "rollout1377108401";
       Operation response = rolloutsClient.pauseAsync(project, rollout).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Project ID for this request.  
`rollout` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the Rollout resource to pause.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### pauseCallable()
    
    
    public final UnaryCallable<PauseRolloutRequest,Operation> pauseCallable()

Pauses a Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       PauseRolloutRequest request =
           PauseRolloutRequest.newBuilder()
               .setEtag("etag3123477")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRollout("rollout1377108401")
               .build();
       ApiFuture<Operation> future = rolloutsClient.pauseCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PauseRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PauseRolloutRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### pauseOperationCallable()
    
    
    public final OperationCallable<PauseRolloutRequest,Operation,Operation> pauseOperationCallable()

Pauses a Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       PauseRolloutRequest request =
           PauseRolloutRequest.newBuilder()
               .setEtag("etag3123477")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRollout("rollout1377108401")
               .build();
       OperationFuture<Operation, Operation> future =
           rolloutsClient.pauseOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[PauseRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PauseRolloutRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeAsync(ResumeRolloutRequest request)
    
    
    public final OperationFuture<Operation,Operation> resumeAsync(ResumeRolloutRequest request)

Resumes a Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       ResumeRolloutRequest request =
           ResumeRolloutRequest.newBuilder()
               .setEtag("etag3123477")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRollout("rollout1377108401")
               .build();
       Operation response = rolloutsClient.resumeAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResumeRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResumeRolloutRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeAsync(String project, String rollout)
    
    
    public final OperationFuture<Operation,Operation> resumeAsync(String project, String rollout)

Resumes a Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       String project = "project-309310695";
       String rollout = "rollout1377108401";
       Operation response = rolloutsClient.resumeAsync(project, rollout).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Project ID for this request.  
`rollout` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the Rollout resource to resume.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeCallable()
    
    
    public final UnaryCallable<ResumeRolloutRequest,Operation> resumeCallable()

Resumes a Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       ResumeRolloutRequest request =
           ResumeRolloutRequest.newBuilder()
               .setEtag("etag3123477")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRollout("rollout1377108401")
               .build();
       ApiFuture<Operation> future = rolloutsClient.resumeCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ResumeRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResumeRolloutRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### resumeOperationCallable()
    
    
    public final OperationCallable<ResumeRolloutRequest,Operation,Operation> resumeOperationCallable()

Resumes a Rollout.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutsClient rolloutsClient = RolloutsClient.create()) {
       ResumeRolloutRequest request =
           ResumeRolloutRequest.newBuilder()
               .setEtag("etag3123477")
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRollout("rollout1377108401")
               .build();
       OperationFuture<Operation, Operation> future =
           rolloutsClient.resumeOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[ResumeRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResumeRolloutRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
