---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutPlansClient
title: Class RolloutPlansClient (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:04:16.111551+00:00
---

# Class RolloutPlansClient (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutPlansClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RolloutPlansClient (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-compute/google-cloud-compute/src/main/java/com/google/cloud/compute/v1/RolloutPlansClient.java)| [Product Reference](https://cloud.google.com/compute/)  
---|---  
  
Service Description: The RolloutPlans API.

This client uses RolloutPlans version 2026-09-01.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create()) {
       String project = "project-309310695";
       String rolloutPlan = "rolloutPlan1469104250";
       RolloutPlan response = rolloutPlansClient.get(project, rolloutPlan);
     }
     

Note: close() needs to be called on the RolloutPlansClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
Delete |  Deletes a RolloutPlan. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteAsync(DeleteRolloutPlanRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteAsync(String project, String rolloutPlan) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteOperationCallable() 
  * deleteCallable() 

  
Get |  Gets details of a single project-scoped RolloutPlan. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * get(GetRolloutPlanRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * get(String project, String rolloutPlan) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCallable() 

  
Insert |  Creates a new RolloutPlan in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * insertAsync(InsertRolloutPlanRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * insertAsync(String project, RolloutPlan rolloutPlanResource) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * insertOperationCallable() 
  * insertCallable() 

  
List |  Lists RolloutPlans in a given project and location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * list(ListRolloutPlansRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * list(String project) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listPagedCallable() 
  * listCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of RolloutPlansSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RolloutPlansSettings rolloutPlansSettings =
         RolloutPlansSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create(rolloutPlansSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RolloutPlansSettings rolloutPlansSettings =
         RolloutPlansSettings.newBuilder().setEndpoint(myEndpoint).build();
     RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create(rolloutPlansSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RolloutPlansClient

## Static Methods 

### create()
    
    
    public static final RolloutPlansClient create()

Constructs an instance of RolloutPlansClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[RolloutPlansClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutPlansClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RolloutPlansSettings settings)
    
    
    public static final RolloutPlansClient create(RolloutPlansSettings settings)

Constructs an instance of RolloutPlansClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RolloutPlansSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutPlansSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RolloutPlansClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutPlansClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(RolloutPlansStub stub)
    
    
    public static final RolloutPlansClient create(RolloutPlansStub stub)

Constructs an instance of RolloutPlansClient, using the given stub for making calls. This is for advanced usage - prefer using create(RolloutPlansSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RolloutPlansStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RolloutPlansStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RolloutPlansClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutPlansClient)` |   
  
## Constructors 

### RolloutPlansClient(RolloutPlansSettings settings)
    
    
    protected RolloutPlansClient(RolloutPlansSettings settings)

Constructs an instance of RolloutPlansClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[RolloutPlansSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutPlansSettings)`  
  
  
### RolloutPlansClient(RolloutPlansStub stub)
    
    
    protected RolloutPlansClient(RolloutPlansStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[RolloutPlansStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RolloutPlansStub)`  
  
  
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

### deleteAsync(DeleteRolloutPlanRequest request)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(DeleteRolloutPlanRequest request)

Deletes a RolloutPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create()) {
       DeleteRolloutPlanRequest request =
           DeleteRolloutPlanRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRolloutPlan("rolloutPlan1469104250")
               .build();
       Operation response = rolloutPlansClient.deleteAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRolloutPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRolloutPlanRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteAsync(String project, String rolloutPlan)
    
    
    public final OperationFuture<Operation,Operation> deleteAsync(String project, String rolloutPlan)

Deletes a RolloutPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create()) {
       String project = "project-309310695";
       String rolloutPlan = "rolloutPlan1469104250";
       Operation response = rolloutPlansClient.deleteAsync(project, rolloutPlan).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`rolloutPlan` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the RolloutPlan resource to delete.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteCallable()
    
    
    public final UnaryCallable<DeleteRolloutPlanRequest,Operation> deleteCallable()

Deletes a RolloutPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create()) {
       DeleteRolloutPlanRequest request =
           DeleteRolloutPlanRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRolloutPlan("rolloutPlan1469104250")
               .build();
       ApiFuture<Operation> future = rolloutPlansClient.deleteCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteRolloutPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRolloutPlanRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationCallable()
    
    
    public final OperationCallable<DeleteRolloutPlanRequest,Operation,Operation> deleteOperationCallable()

Deletes a RolloutPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create()) {
       DeleteRolloutPlanRequest request =
           DeleteRolloutPlanRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRolloutPlan("rolloutPlan1469104250")
               .build();
       OperationFuture<Operation, Operation> future =
           rolloutPlansClient.deleteOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteRolloutPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteRolloutPlanRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### get(GetRolloutPlanRequest request)
    
    
    public final RolloutPlan get(GetRolloutPlanRequest request)

Gets details of a single project-scoped RolloutPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create()) {
       GetRolloutPlanRequest request =
           GetRolloutPlanRequest.newBuilder()
               .setProject("project-309310695")
               .setRolloutPlan("rolloutPlan1469104250")
               .build();
       RolloutPlan response = rolloutPlansClient.get(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRolloutPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRolloutPlanRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RolloutPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutPlan)` |   
  
### get(String project, String rolloutPlan)
    
    
    public final RolloutPlan get(String project, String rolloutPlan)

Gets details of a single project-scoped RolloutPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create()) {
       String project = "project-309310695";
       String rolloutPlan = "rolloutPlan1469104250";
       RolloutPlan response = rolloutPlansClient.get(project, rolloutPlan);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`rolloutPlan` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the persistent rollout plan to return.  
**Returns**  
---  
**Type** | **Description**  
`[RolloutPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutPlan)` |   
  
### getCallable()
    
    
    public final UnaryCallable<GetRolloutPlanRequest,RolloutPlan> getCallable()

Gets details of a single project-scoped RolloutPlan.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create()) {
       GetRolloutPlanRequest request =
           GetRolloutPlanRequest.newBuilder()
               .setProject("project-309310695")
               .setRolloutPlan("rolloutPlan1469104250")
               .build();
       ApiFuture<RolloutPlan> future = rolloutPlansClient.getCallable().futureCall(request);
       // Do something.
       RolloutPlan response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetRolloutPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRolloutPlanRequest),[RolloutPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutPlan)>` |   
  
### getSettings()
    
    
    public final @Nullable RolloutPlansSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.compute.v1.RolloutPlansSettings` |   
  
### getStub()
    
    
    public RolloutPlansStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[RolloutPlansStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.RolloutPlansStub)` |   
  
### insertAsync(InsertRolloutPlanRequest request)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(InsertRolloutPlanRequest request)

Creates a new RolloutPlan in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create()) {
       InsertRolloutPlanRequest request =
           InsertRolloutPlanRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRolloutPlanResource(RolloutPlan.newBuilder().build())
               .build();
       Operation response = rolloutPlansClient.insertAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[InsertRolloutPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRolloutPlanRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertAsync(String project, RolloutPlan rolloutPlanResource)
    
    
    public final OperationFuture<Operation,Operation> insertAsync(String project, RolloutPlan rolloutPlanResource)

Creates a new RolloutPlan in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create()) {
       String project = "project-309310695";
       RolloutPlan rolloutPlanResource = RolloutPlan.newBuilder().build();
       Operation response = rolloutPlansClient.insertAsync(project, rolloutPlanResource).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`project` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Project ID for this request.  
`rolloutPlanResource` | `[RolloutPlan](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutPlan)`  
The body resource for this request  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertCallable()
    
    
    public final UnaryCallable<InsertRolloutPlanRequest,Operation> insertCallable()

Creates a new RolloutPlan in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create()) {
       InsertRolloutPlanRequest request =
           InsertRolloutPlanRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRolloutPlanResource(RolloutPlan.newBuilder().build())
               .build();
       ApiFuture<Operation> future = rolloutPlansClient.insertCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[InsertRolloutPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRolloutPlanRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertOperationCallable()
    
    
    public final OperationCallable<InsertRolloutPlanRequest,Operation,Operation> insertOperationCallable()

Creates a new RolloutPlan in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create()) {
       InsertRolloutPlanRequest request =
           InsertRolloutPlanRequest.newBuilder()
               .setProject("project-309310695")
               .setRequestId("requestId693933066")
               .setRolloutPlanResource(RolloutPlan.newBuilder().build())
               .build();
       OperationFuture<Operation, Operation> future =
           rolloutPlansClient.insertOperationCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[InsertRolloutPlanRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertRolloutPlanRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
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
  
### list(ListRolloutPlansRequest request)
    
    
    public final RolloutPlansClient.ListPagedResponse list(ListRolloutPlansRequest request)

Lists RolloutPlans in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create()) {
       ListRolloutPlansRequest request =
           ListRolloutPlansRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       for (RolloutPlan element : rolloutPlansClient.list(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRolloutPlansRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRolloutPlansRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[RolloutPlansClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutPlansClient.ListPagedResponse)` |   
  
### list(String project)
    
    
    public final RolloutPlansClient.ListPagedResponse list(String project)

Lists RolloutPlans in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create()) {
       String project = "project-309310695";
       for (RolloutPlan element : rolloutPlansClient.list(project).iterateAll()) {
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
`[RolloutPlansClient.ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutPlansClient.ListPagedResponse)` |   
  
### listCallable()
    
    
    public final UnaryCallable<ListRolloutPlansRequest,RolloutPlansListResponse> listCallable()

Lists RolloutPlans in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create()) {
       ListRolloutPlansRequest request =
           ListRolloutPlansRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       while (true) {
         RolloutPlansListResponse response = rolloutPlansClient.listCallable().call(request);
         for (RolloutPlan element : response.getItemsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRolloutPlansRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRolloutPlansRequest),[RolloutPlansListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutPlansListResponse)>` |   
  
### listPagedCallable()
    
    
    public final UnaryCallable<ListRolloutPlansRequest,RolloutPlansClient.ListPagedResponse> listPagedCallable()

Lists RolloutPlans in a given project and location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (RolloutPlansClient rolloutPlansClient = RolloutPlansClient.create()) {
       ListRolloutPlansRequest request =
           ListRolloutPlansRequest.newBuilder()
               .setFilter("filter-1274492040")
               .setMaxResults(1128457243)
               .setOrderBy("orderBy-1207110587")
               .setPageToken("pageToken873572522")
               .setProject("project-309310695")
               .build();
       ApiFuture<RolloutPlan> future = rolloutPlansClient.listPagedCallable().futureCall(request);
       // Do something.
       for (RolloutPlan element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListRolloutPlansRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListRolloutPlansRequest),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RolloutPlansClient.ListPagedResponse)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
