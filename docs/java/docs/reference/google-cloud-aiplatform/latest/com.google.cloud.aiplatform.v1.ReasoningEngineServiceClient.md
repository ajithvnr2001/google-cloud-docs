---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngineServiceClient
title: Class ReasoningEngineServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:54:29.666851+00:00
---

# Class ReasoningEngineServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngineServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ReasoningEngineServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/ReasoningEngineServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: A service for managing Vertex AI's Reasoning Engines.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       ReasoningEngineName name =
           ReasoningEngineName.of("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]");
       ReasoningEngine response = reasoningEngineServiceClient.getReasoningEngine(name);
     }
     

Note: close() needs to be called on the ReasoningEngineServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateReasoningEngine |  Creates a reasoning engine. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createReasoningEngineAsync(CreateReasoningEngineRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createReasoningEngineAsync(LocationName parent, ReasoningEngine reasoningEngine) 
  * createReasoningEngineAsync(String parent, ReasoningEngine reasoningEngine) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createReasoningEngineOperationCallable() 
  * createReasoningEngineCallable() 

  
GetReasoningEngine |  Gets a reasoning engine. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getReasoningEngine(GetReasoningEngineRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getReasoningEngine(ReasoningEngineName name) 
  * getReasoningEngine(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getReasoningEngineCallable() 

  
ListReasoningEngines |  Lists reasoning engines in a location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listReasoningEngines(ListReasoningEnginesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listReasoningEngines(LocationName parent) 
  * listReasoningEngines(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listReasoningEnginesPagedCallable() 
  * listReasoningEnginesCallable() 

  
UpdateReasoningEngine |  Updates a reasoning engine. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateReasoningEngineAsync(UpdateReasoningEngineRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateReasoningEngineAsync(ReasoningEngine reasoningEngine, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateReasoningEngineOperationCallable() 
  * updateReasoningEngineCallable() 

  
DeleteReasoningEngine |  Deletes a reasoning engine. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteReasoningEngineAsync(DeleteReasoningEngineRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteReasoningEngineAsync(ReasoningEngineName name) 
  * deleteReasoningEngineAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteReasoningEngineOperationCallable() 
  * deleteReasoningEngineCallable() 

  
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

This class can be customized by passing in a custom instance of ReasoningEngineServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ReasoningEngineServiceSettings reasoningEngineServiceSettings =
         ReasoningEngineServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create(reasoningEngineServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ReasoningEngineServiceSettings reasoningEngineServiceSettings =
         ReasoningEngineServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create(reasoningEngineServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ReasoningEngineServiceClient

## Static Methods 

### create()
    
    
    public static final ReasoningEngineServiceClient create()

Constructs an instance of ReasoningEngineServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngineServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ReasoningEngineServiceSettings settings)
    
    
    public static final ReasoningEngineServiceClient create(ReasoningEngineServiceSettings settings)

Constructs an instance of ReasoningEngineServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ReasoningEngineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngineServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngineServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ReasoningEngineServiceStub stub)
    
    
    public static final ReasoningEngineServiceClient create(ReasoningEngineServiceStub stub)

Constructs an instance of ReasoningEngineServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ReasoningEngineServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ReasoningEngineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.ReasoningEngineServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngineServiceClient)` |   
  
## Constructors 

### ReasoningEngineServiceClient(ReasoningEngineServiceSettings settings)
    
    
    protected ReasoningEngineServiceClient(ReasoningEngineServiceSettings settings)

Constructs an instance of ReasoningEngineServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ReasoningEngineServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngineServiceSettings)`  
  
  
### ReasoningEngineServiceClient(ReasoningEngineServiceStub stub)
    
    
    protected ReasoningEngineServiceClient(ReasoningEngineServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ReasoningEngineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.ReasoningEngineServiceStub)`  
  
  
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

### createReasoningEngineAsync(@Nullable LocationName parent, ReasoningEngine reasoningEngine)
    
    
    public final OperationFuture<ReasoningEngine,CreateReasoningEngineOperationMetadata> createReasoningEngineAsync(@Nullable LocationName parent, ReasoningEngine reasoningEngine)

Creates a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       ReasoningEngine reasoningEngine = ReasoningEngine.newBuilder().build();
       ReasoningEngine response =
           reasoningEngineServiceClient.createReasoningEngineAsync(parent, reasoningEngine).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create the ReasoningEngine in. Format: `projects/{project}/locations/{location}`  
`reasoningEngine` | `[ReasoningEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngine)`  
Required. The ReasoningEngine to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ReasoningEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngine),[CreateReasoningEngineOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateReasoningEngineOperationMetadata)>` |   
  
### createReasoningEngineAsync(CreateReasoningEngineRequest request)
    
    
    public final OperationFuture<ReasoningEngine,CreateReasoningEngineOperationMetadata> createReasoningEngineAsync(CreateReasoningEngineRequest request)

Creates a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       CreateReasoningEngineRequest request =
           CreateReasoningEngineRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setReasoningEngine(ReasoningEngine.newBuilder().build())
               .build();
       ReasoningEngine response =
           reasoningEngineServiceClient.createReasoningEngineAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateReasoningEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateReasoningEngineRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ReasoningEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngine),[CreateReasoningEngineOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateReasoningEngineOperationMetadata)>` |   
  
### createReasoningEngineAsync(String parent, ReasoningEngine reasoningEngine)
    
    
    public final OperationFuture<ReasoningEngine,CreateReasoningEngineOperationMetadata> createReasoningEngineAsync(String parent, ReasoningEngine reasoningEngine)

Creates a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       ReasoningEngine reasoningEngine = ReasoningEngine.newBuilder().build();
       ReasoningEngine response =
           reasoningEngineServiceClient.createReasoningEngineAsync(parent, reasoningEngine).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the ReasoningEngine in. Format: `projects/{project}/locations/{location}`  
`reasoningEngine` | `[ReasoningEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngine)`  
Required. The ReasoningEngine to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ReasoningEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngine),[CreateReasoningEngineOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateReasoningEngineOperationMetadata)>` |   
  
### createReasoningEngineCallable()
    
    
    public final UnaryCallable<CreateReasoningEngineRequest,Operation> createReasoningEngineCallable()

Creates a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       CreateReasoningEngineRequest request =
           CreateReasoningEngineRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setReasoningEngine(ReasoningEngine.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           reasoningEngineServiceClient.createReasoningEngineCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateReasoningEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateReasoningEngineRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createReasoningEngineOperationCallable()
    
    
    public final OperationCallable<CreateReasoningEngineRequest,ReasoningEngine,CreateReasoningEngineOperationMetadata> createReasoningEngineOperationCallable()

Creates a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       CreateReasoningEngineRequest request =
           CreateReasoningEngineRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setReasoningEngine(ReasoningEngine.newBuilder().build())
               .build();
       OperationFuture<ReasoningEngine, CreateReasoningEngineOperationMetadata> future =
           reasoningEngineServiceClient.createReasoningEngineOperationCallable().futureCall(request);
       // Do something.
       ReasoningEngine response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateReasoningEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateReasoningEngineRequest),[ReasoningEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngine),[CreateReasoningEngineOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateReasoningEngineOperationMetadata)>` |   
  
### deleteReasoningEngineAsync(@Nullable ReasoningEngineName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteReasoningEngineAsync(@Nullable ReasoningEngineName name)

Deletes a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       ReasoningEngineName name =
           ReasoningEngineName.of("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]");
       reasoningEngineServiceClient.deleteReasoningEngineAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ReasoningEngineName`  
Required. The name of the ReasoningEngine resource to be deleted. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteReasoningEngineAsync(DeleteReasoningEngineRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteReasoningEngineAsync(DeleteReasoningEngineRequest request)

Deletes a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       DeleteReasoningEngineRequest request =
           DeleteReasoningEngineRequest.newBuilder()
               .setName(
                   ReasoningEngineName.of("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]")
                       .toString())
               .setForce(true)
               .build();
       reasoningEngineServiceClient.deleteReasoningEngineAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteReasoningEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteReasoningEngineRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteReasoningEngineAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteReasoningEngineAsync(String name)

Deletes a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       String name =
           ReasoningEngineName.of("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]").toString();
       reasoningEngineServiceClient.deleteReasoningEngineAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ReasoningEngine resource to be deleted. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteReasoningEngineCallable()
    
    
    public final UnaryCallable<DeleteReasoningEngineRequest,Operation> deleteReasoningEngineCallable()

Deletes a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       DeleteReasoningEngineRequest request =
           DeleteReasoningEngineRequest.newBuilder()
               .setName(
                   ReasoningEngineName.of("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]")
                       .toString())
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           reasoningEngineServiceClient.deleteReasoningEngineCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteReasoningEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteReasoningEngineRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteReasoningEngineOperationCallable()
    
    
    public final OperationCallable<DeleteReasoningEngineRequest,Empty,DeleteOperationMetadata> deleteReasoningEngineOperationCallable()

Deletes a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       DeleteReasoningEngineRequest request =
           DeleteReasoningEngineRequest.newBuilder()
               .setName(
                   ReasoningEngineName.of("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]")
                       .toString())
               .setForce(true)
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           reasoningEngineServiceClient.deleteReasoningEngineOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteReasoningEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteReasoningEngineRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = reasoningEngineServiceClient.getIamPolicy(request);
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
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           reasoningEngineServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = reasoningEngineServiceClient.getLocation(request);
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
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           reasoningEngineServiceClient.getLocationCallable().futureCall(request);
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
  
### getReasoningEngine(@Nullable ReasoningEngineName name)
    
    
    public final ReasoningEngine getReasoningEngine(@Nullable ReasoningEngineName name)

Gets a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       ReasoningEngineName name =
           ReasoningEngineName.of("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]");
       ReasoningEngine response = reasoningEngineServiceClient.getReasoningEngine(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ReasoningEngineName`  
Required. The name of the ReasoningEngine resource. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngine)` |   
  
### getReasoningEngine(GetReasoningEngineRequest request)
    
    
    public final ReasoningEngine getReasoningEngine(GetReasoningEngineRequest request)

Gets a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       GetReasoningEngineRequest request =
           GetReasoningEngineRequest.newBuilder()
               .setName(
                   ReasoningEngineName.of("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]")
                       .toString())
               .build();
       ReasoningEngine response = reasoningEngineServiceClient.getReasoningEngine(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetReasoningEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetReasoningEngineRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngine)` |   
  
### getReasoningEngine(String name)
    
    
    public final ReasoningEngine getReasoningEngine(String name)

Gets a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       String name =
           ReasoningEngineName.of("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]").toString();
       ReasoningEngine response = reasoningEngineServiceClient.getReasoningEngine(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ReasoningEngine resource. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngine)` |   
  
### getReasoningEngineCallable()
    
    
    public final UnaryCallable<GetReasoningEngineRequest,ReasoningEngine> getReasoningEngineCallable()

Gets a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       GetReasoningEngineRequest request =
           GetReasoningEngineRequest.newBuilder()
               .setName(
                   ReasoningEngineName.of("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]")
                       .toString())
               .build();
       ApiFuture<ReasoningEngine> future =
           reasoningEngineServiceClient.getReasoningEngineCallable().futureCall(request);
       // Do something.
       ReasoningEngine response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetReasoningEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetReasoningEngineRequest),[ReasoningEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngine)>` |   
  
### getSettings()
    
    
    public final @Nullable ReasoningEngineServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.ReasoningEngineServiceSettings` |   
  
### getStub()
    
    
    public ReasoningEngineServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.ReasoningEngineServiceStub)` |   
  
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
    
    
    public final ReasoningEngineServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : reasoningEngineServiceClient.listLocations(request).iterateAll()) {
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
`[ReasoningEngineServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngineServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             reasoningEngineServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,ReasoningEngineServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           reasoningEngineServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngineServiceClient.ListLocationsPagedResponse)>` |   
  
### listReasoningEngines(@Nullable LocationName parent)
    
    
    public final ReasoningEngineServiceClient.ListReasoningEnginesPagedResponse listReasoningEngines(@Nullable LocationName parent)

Lists reasoning engines in a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (ReasoningEngine element :
           reasoningEngineServiceClient.listReasoningEngines(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to list the ReasoningEngines from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineServiceClient.ListReasoningEnginesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngineServiceClient.ListReasoningEnginesPagedResponse)` |   
  
### listReasoningEngines(ListReasoningEnginesRequest request)
    
    
    public final ReasoningEngineServiceClient.ListReasoningEnginesPagedResponse listReasoningEngines(ListReasoningEnginesRequest request)

Lists reasoning engines in a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       ListReasoningEnginesRequest request =
           ListReasoningEnginesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ReasoningEngine element :
           reasoningEngineServiceClient.listReasoningEngines(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReasoningEnginesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListReasoningEnginesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineServiceClient.ListReasoningEnginesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngineServiceClient.ListReasoningEnginesPagedResponse)` |   
  
### listReasoningEngines(String parent)
    
    
    public final ReasoningEngineServiceClient.ListReasoningEnginesPagedResponse listReasoningEngines(String parent)

Lists reasoning engines in a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (ReasoningEngine element :
           reasoningEngineServiceClient.listReasoningEngines(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to list the ReasoningEngines from. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineServiceClient.ListReasoningEnginesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngineServiceClient.ListReasoningEnginesPagedResponse)` |   
  
### listReasoningEnginesCallable()
    
    
    public final UnaryCallable<ListReasoningEnginesRequest,ListReasoningEnginesResponse> listReasoningEnginesCallable()

Lists reasoning engines in a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       ListReasoningEnginesRequest request =
           ListReasoningEnginesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListReasoningEnginesResponse response =
             reasoningEngineServiceClient.listReasoningEnginesCallable().call(request);
         for (ReasoningEngine element : response.getReasoningEnginesList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReasoningEnginesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListReasoningEnginesRequest),[ListReasoningEnginesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListReasoningEnginesResponse)>` |   
  
### listReasoningEnginesPagedCallable()
    
    
    public final UnaryCallable<ListReasoningEnginesRequest,ReasoningEngineServiceClient.ListReasoningEnginesPagedResponse> listReasoningEnginesPagedCallable()

Lists reasoning engines in a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       ListReasoningEnginesRequest request =
           ListReasoningEnginesRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ReasoningEngine> future =
           reasoningEngineServiceClient.listReasoningEnginesPagedCallable().futureCall(request);
       // Do something.
       for (ReasoningEngine element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReasoningEnginesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListReasoningEnginesRequest),[ListReasoningEnginesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngineServiceClient.ListReasoningEnginesPagedResponse)>` |   
  
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
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = reasoningEngineServiceClient.setIamPolicy(request);
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
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           reasoningEngineServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response =
           reasoningEngineServiceClient.testIamPermissions(request);
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
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           reasoningEngineServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateReasoningEngineAsync(ReasoningEngine reasoningEngine, FieldMask updateMask)
    
    
    public final OperationFuture<ReasoningEngine,UpdateReasoningEngineOperationMetadata> updateReasoningEngineAsync(ReasoningEngine reasoningEngine, FieldMask updateMask)

Updates a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       ReasoningEngine reasoningEngine = ReasoningEngine.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       ReasoningEngine response =
           reasoningEngineServiceClient
               .updateReasoningEngineAsync(reasoningEngine, updateMask)
               .get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`reasoningEngine` | `[ReasoningEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngine)`  
Required. The ReasoningEngine which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Optional. Mask specifying which fields to update.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ReasoningEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngine),[UpdateReasoningEngineOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateReasoningEngineOperationMetadata)>` |   
  
### updateReasoningEngineAsync(UpdateReasoningEngineRequest request)
    
    
    public final OperationFuture<ReasoningEngine,UpdateReasoningEngineOperationMetadata> updateReasoningEngineAsync(UpdateReasoningEngineRequest request)

Updates a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       UpdateReasoningEngineRequest request =
           UpdateReasoningEngineRequest.newBuilder()
               .setReasoningEngine(ReasoningEngine.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ReasoningEngine response =
           reasoningEngineServiceClient.updateReasoningEngineAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateReasoningEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateReasoningEngineRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[ReasoningEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngine),[UpdateReasoningEngineOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateReasoningEngineOperationMetadata)>` |   
  
### updateReasoningEngineCallable()
    
    
    public final UnaryCallable<UpdateReasoningEngineRequest,Operation> updateReasoningEngineCallable()

Updates a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       UpdateReasoningEngineRequest request =
           UpdateReasoningEngineRequest.newBuilder()
               .setReasoningEngine(ReasoningEngine.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           reasoningEngineServiceClient.updateReasoningEngineCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateReasoningEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateReasoningEngineRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateReasoningEngineOperationCallable()
    
    
    public final OperationCallable<UpdateReasoningEngineRequest,ReasoningEngine,UpdateReasoningEngineOperationMetadata> updateReasoningEngineOperationCallable()

Updates a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineServiceClient reasoningEngineServiceClient =
         ReasoningEngineServiceClient.create()) {
       UpdateReasoningEngineRequest request =
           UpdateReasoningEngineRequest.newBuilder()
               .setReasoningEngine(ReasoningEngine.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<ReasoningEngine, UpdateReasoningEngineOperationMetadata> future =
           reasoningEngineServiceClient.updateReasoningEngineOperationCallable().futureCall(request);
       // Do something.
       ReasoningEngine response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateReasoningEngineRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateReasoningEngineRequest),[ReasoningEngine](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ReasoningEngine),[UpdateReasoningEngineOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateReasoningEngineOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
