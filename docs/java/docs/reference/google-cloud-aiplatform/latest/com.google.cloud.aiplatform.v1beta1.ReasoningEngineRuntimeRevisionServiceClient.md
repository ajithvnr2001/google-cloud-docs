---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionServiceClient
title: Class ReasoningEngineRuntimeRevisionServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:04.302196+00:00
---

# Class ReasoningEngineRuntimeRevisionServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ReasoningEngineRuntimeRevisionServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1beta1/ReasoningEngineRuntimeRevisionServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: Manages Vertex AI's Reasoning Engine Revisions.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       ReasoningEngineRuntimeRevisionName name =
           ReasoningEngineRuntimeRevisionName.of(
               "[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]", "[RUNTIME_REVISION]");
       ReasoningEngineRuntimeRevision response =
           reasoningEngineRuntimeRevisionServiceClient.getReasoningEngineRuntimeRevision(name);
     }
     

Note: close() needs to be called on the ReasoningEngineRuntimeRevisionServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
GetReasoningEngineRuntimeRevision |  Gets a reasoning engine runtime revision. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getReasoningEngineRuntimeRevision(GetReasoningEngineRuntimeRevisionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getReasoningEngineRuntimeRevision(ReasoningEngineRuntimeRevisionName name) 
  * getReasoningEngineRuntimeRevision(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getReasoningEngineRuntimeRevisionCallable() 

  
ListReasoningEngineRuntimeRevisions |  Lists runtime revisions in a reasoning engine. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listReasoningEngineRuntimeRevisions(ListReasoningEngineRuntimeRevisionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listReasoningEngineRuntimeRevisions(ReasoningEngineName parent) 
  * listReasoningEngineRuntimeRevisions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listReasoningEngineRuntimeRevisionsPagedCallable() 
  * listReasoningEngineRuntimeRevisionsCallable() 

  
DeleteReasoningEngineRuntimeRevision |  Deletes a reasoning engine revision. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteReasoningEngineRuntimeRevisionAsync(DeleteReasoningEngineRuntimeRevisionRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteReasoningEngineRuntimeRevisionAsync(ReasoningEngineRuntimeRevisionName name) 
  * deleteReasoningEngineRuntimeRevisionAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteReasoningEngineRuntimeRevisionOperationCallable() 
  * deleteReasoningEngineRuntimeRevisionCallable() 

  
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

This class can be customized by passing in a custom instance of ReasoningEngineRuntimeRevisionServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ReasoningEngineRuntimeRevisionServiceSettings reasoningEngineRuntimeRevisionServiceSettings =
         ReasoningEngineRuntimeRevisionServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create(
             reasoningEngineRuntimeRevisionServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ReasoningEngineRuntimeRevisionServiceSettings reasoningEngineRuntimeRevisionServiceSettings =
         ReasoningEngineRuntimeRevisionServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create(
             reasoningEngineRuntimeRevisionServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ReasoningEngineRuntimeRevisionServiceClient

## Static Methods 

### create()
    
    
    public static final ReasoningEngineRuntimeRevisionServiceClient create()

Constructs an instance of ReasoningEngineRuntimeRevisionServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineRuntimeRevisionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ReasoningEngineRuntimeRevisionServiceSettings settings)
    
    
    public static final ReasoningEngineRuntimeRevisionServiceClient create(ReasoningEngineRuntimeRevisionServiceSettings settings)

Constructs an instance of ReasoningEngineRuntimeRevisionServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ReasoningEngineRuntimeRevisionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineRuntimeRevisionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ReasoningEngineRuntimeRevisionServiceStub stub)
    
    
    public static final ReasoningEngineRuntimeRevisionServiceClient create(ReasoningEngineRuntimeRevisionServiceStub stub)

Constructs an instance of ReasoningEngineRuntimeRevisionServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ReasoningEngineRuntimeRevisionServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ReasoningEngineRuntimeRevisionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.stub.ReasoningEngineRuntimeRevisionServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineRuntimeRevisionServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionServiceClient)` |   
  
## Constructors 

### ReasoningEngineRuntimeRevisionServiceClient(ReasoningEngineRuntimeRevisionServiceSettings settings)
    
    
    protected ReasoningEngineRuntimeRevisionServiceClient(ReasoningEngineRuntimeRevisionServiceSettings settings)

Constructs an instance of ReasoningEngineRuntimeRevisionServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ReasoningEngineRuntimeRevisionServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionServiceSettings)`  
  
  
### ReasoningEngineRuntimeRevisionServiceClient(ReasoningEngineRuntimeRevisionServiceStub stub)
    
    
    protected ReasoningEngineRuntimeRevisionServiceClient(ReasoningEngineRuntimeRevisionServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ReasoningEngineRuntimeRevisionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.stub.ReasoningEngineRuntimeRevisionServiceStub)`  
  
  
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

### deleteReasoningEngineRuntimeRevisionAsync(@Nullable ReasoningEngineRuntimeRevisionName name)
    
    
    public final OperationFuture<Empty,DeleteReasoningEngineRuntimeRevisionOperationMetadata> deleteReasoningEngineRuntimeRevisionAsync(@Nullable ReasoningEngineRuntimeRevisionName name)

Deletes a reasoning engine revision.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       ReasoningEngineRuntimeRevisionName name =
           ReasoningEngineRuntimeRevisionName.of(
               "[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]", "[RUNTIME_REVISION]");
       reasoningEngineRuntimeRevisionServiceClient
           .deleteReasoningEngineRuntimeRevisionAsync(name)
           .get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionName`  
Required. The name of the ReasoningEngineRuntimeRevision resource to be deleted. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}/runtimeRevisions/{runtime_revision}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteReasoningEngineRuntimeRevisionOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteReasoningEngineRuntimeRevisionOperationMetadata)>` |   
  
### deleteReasoningEngineRuntimeRevisionAsync(DeleteReasoningEngineRuntimeRevisionRequest request)
    
    
    public final OperationFuture<Empty,DeleteReasoningEngineRuntimeRevisionOperationMetadata> deleteReasoningEngineRuntimeRevisionAsync(DeleteReasoningEngineRuntimeRevisionRequest request)

Deletes a reasoning engine revision.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       DeleteReasoningEngineRuntimeRevisionRequest request =
           DeleteReasoningEngineRuntimeRevisionRequest.newBuilder()
               .setName(
                   ReasoningEngineRuntimeRevisionName.of(
                           "[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]", "[RUNTIME_REVISION]")
                       .toString())
               .build();
       reasoningEngineRuntimeRevisionServiceClient
           .deleteReasoningEngineRuntimeRevisionAsync(request)
           .get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteReasoningEngineRuntimeRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteReasoningEngineRuntimeRevisionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteReasoningEngineRuntimeRevisionOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteReasoningEngineRuntimeRevisionOperationMetadata)>` |   
  
### deleteReasoningEngineRuntimeRevisionAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteReasoningEngineRuntimeRevisionOperationMetadata> deleteReasoningEngineRuntimeRevisionAsync(String name)

Deletes a reasoning engine revision.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       String name =
           ReasoningEngineRuntimeRevisionName.of(
                   "[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]", "[RUNTIME_REVISION]")
               .toString();
       reasoningEngineRuntimeRevisionServiceClient
           .deleteReasoningEngineRuntimeRevisionAsync(name)
           .get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ReasoningEngineRuntimeRevision resource to be deleted. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}/runtimeRevisions/{runtime_revision}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteReasoningEngineRuntimeRevisionOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteReasoningEngineRuntimeRevisionOperationMetadata)>` |   
  
### deleteReasoningEngineRuntimeRevisionCallable()
    
    
    public final UnaryCallable<DeleteReasoningEngineRuntimeRevisionRequest,Operation> deleteReasoningEngineRuntimeRevisionCallable()

Deletes a reasoning engine revision.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       DeleteReasoningEngineRuntimeRevisionRequest request =
           DeleteReasoningEngineRuntimeRevisionRequest.newBuilder()
               .setName(
                   ReasoningEngineRuntimeRevisionName.of(
                           "[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]", "[RUNTIME_REVISION]")
                       .toString())
               .build();
       ApiFuture<Operation> future =
           reasoningEngineRuntimeRevisionServiceClient
               .deleteReasoningEngineRuntimeRevisionCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteReasoningEngineRuntimeRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteReasoningEngineRuntimeRevisionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteReasoningEngineRuntimeRevisionOperationCallable()
    
    
    public final OperationCallable<DeleteReasoningEngineRuntimeRevisionRequest,Empty,DeleteReasoningEngineRuntimeRevisionOperationMetadata> deleteReasoningEngineRuntimeRevisionOperationCallable()

Deletes a reasoning engine revision.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       DeleteReasoningEngineRuntimeRevisionRequest request =
           DeleteReasoningEngineRuntimeRevisionRequest.newBuilder()
               .setName(
                   ReasoningEngineRuntimeRevisionName.of(
                           "[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]", "[RUNTIME_REVISION]")
                       .toString())
               .build();
       OperationFuture<Empty, DeleteReasoningEngineRuntimeRevisionOperationMetadata> future =
           reasoningEngineRuntimeRevisionServiceClient
               .deleteReasoningEngineRuntimeRevisionOperationCallable()
               .futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteReasoningEngineRuntimeRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteReasoningEngineRuntimeRevisionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteReasoningEngineRuntimeRevisionOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteReasoningEngineRuntimeRevisionOperationMetadata)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = reasoningEngineRuntimeRevisionServiceClient.getIamPolicy(request);
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
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           reasoningEngineRuntimeRevisionServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = reasoningEngineRuntimeRevisionServiceClient.getLocation(request);
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
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           reasoningEngineRuntimeRevisionServiceClient.getLocationCallable().futureCall(request);
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
  
### getReasoningEngineRuntimeRevision(@Nullable ReasoningEngineRuntimeRevisionName name)
    
    
    public final ReasoningEngineRuntimeRevision getReasoningEngineRuntimeRevision(@Nullable ReasoningEngineRuntimeRevisionName name)

Gets a reasoning engine runtime revision.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       ReasoningEngineRuntimeRevisionName name =
           ReasoningEngineRuntimeRevisionName.of(
               "[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]", "[RUNTIME_REVISION]");
       ReasoningEngineRuntimeRevision response =
           reasoningEngineRuntimeRevisionServiceClient.getReasoningEngineRuntimeRevision(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionName`  
Required. The name of the ReasoningEngineRuntimeRevision resource. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}/runtimeRevisions/{runtimeRevision}`  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineRuntimeRevision](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevision)` |   
  
### getReasoningEngineRuntimeRevision(GetReasoningEngineRuntimeRevisionRequest request)
    
    
    public final ReasoningEngineRuntimeRevision getReasoningEngineRuntimeRevision(GetReasoningEngineRuntimeRevisionRequest request)

Gets a reasoning engine runtime revision.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       GetReasoningEngineRuntimeRevisionRequest request =
           GetReasoningEngineRuntimeRevisionRequest.newBuilder()
               .setName(
                   ReasoningEngineRuntimeRevisionName.of(
                           "[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]", "[RUNTIME_REVISION]")
                       .toString())
               .build();
       ReasoningEngineRuntimeRevision response =
           reasoningEngineRuntimeRevisionServiceClient.getReasoningEngineRuntimeRevision(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetReasoningEngineRuntimeRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetReasoningEngineRuntimeRevisionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineRuntimeRevision](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevision)` |   
  
### getReasoningEngineRuntimeRevision(String name)
    
    
    public final ReasoningEngineRuntimeRevision getReasoningEngineRuntimeRevision(String name)

Gets a reasoning engine runtime revision.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       String name =
           ReasoningEngineRuntimeRevisionName.of(
                   "[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]", "[RUNTIME_REVISION]")
               .toString();
       ReasoningEngineRuntimeRevision response =
           reasoningEngineRuntimeRevisionServiceClient.getReasoningEngineRuntimeRevision(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the ReasoningEngineRuntimeRevision resource. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}/runtimeRevisions/{runtimeRevision}`  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineRuntimeRevision](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevision)` |   
  
### getReasoningEngineRuntimeRevisionCallable()
    
    
    public final UnaryCallable<GetReasoningEngineRuntimeRevisionRequest,ReasoningEngineRuntimeRevision> getReasoningEngineRuntimeRevisionCallable()

Gets a reasoning engine runtime revision.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       GetReasoningEngineRuntimeRevisionRequest request =
           GetReasoningEngineRuntimeRevisionRequest.newBuilder()
               .setName(
                   ReasoningEngineRuntimeRevisionName.of(
                           "[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]", "[RUNTIME_REVISION]")
                       .toString())
               .build();
       ApiFuture<ReasoningEngineRuntimeRevision> future =
           reasoningEngineRuntimeRevisionServiceClient
               .getReasoningEngineRuntimeRevisionCallable()
               .futureCall(request);
       // Do something.
       ReasoningEngineRuntimeRevision response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetReasoningEngineRuntimeRevisionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetReasoningEngineRuntimeRevisionRequest),[ReasoningEngineRuntimeRevision](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevision)>` |   
  
### getSettings()
    
    
    public final @Nullable ReasoningEngineRuntimeRevisionServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionServiceSettings` |   
  
### getStub()
    
    
    public ReasoningEngineRuntimeRevisionServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineRuntimeRevisionServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.stub.ReasoningEngineRuntimeRevisionServiceStub)` |   
  
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
    
    
    public final ReasoningEngineRuntimeRevisionServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element :
           reasoningEngineRuntimeRevisionServiceClient.listLocations(request).iterateAll()) {
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
`[ReasoningEngineRuntimeRevisionServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             reasoningEngineRuntimeRevisionServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,ReasoningEngineRuntimeRevisionServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           reasoningEngineRuntimeRevisionServiceClient
               .listLocationsPagedCallable()
               .futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionServiceClient.ListLocationsPagedResponse)>` |   
  
### listReasoningEngineRuntimeRevisions(@Nullable ReasoningEngineName parent)
    
    
    public final ReasoningEngineRuntimeRevisionServiceClient.ListReasoningEngineRuntimeRevisionsPagedResponse listReasoningEngineRuntimeRevisions(@Nullable ReasoningEngineName parent)

Lists runtime revisions in a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       ReasoningEngineName parent =
           ReasoningEngineName.of("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]");
       for (ReasoningEngineRuntimeRevision element :
           reasoningEngineRuntimeRevisionServiceClient
               .listReasoningEngineRuntimeRevisions(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1beta1.ReasoningEngineName`  
Required. The resource name of the ReasoningEngine to list the ReasoningEngineRuntimeRevisions from. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineRuntimeRevisionServiceClient.ListReasoningEngineRuntimeRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionServiceClient.ListReasoningEngineRuntimeRevisionsPagedResponse)` |   
  
### listReasoningEngineRuntimeRevisions(ListReasoningEngineRuntimeRevisionsRequest request)
    
    
    public final ReasoningEngineRuntimeRevisionServiceClient.ListReasoningEngineRuntimeRevisionsPagedResponse listReasoningEngineRuntimeRevisions(ListReasoningEngineRuntimeRevisionsRequest request)

Lists runtime revisions in a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       ListReasoningEngineRuntimeRevisionsRequest request =
           ListReasoningEngineRuntimeRevisionsRequest.newBuilder()
               .setParent(
                   ReasoningEngineName.of("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (ReasoningEngineRuntimeRevision element :
           reasoningEngineRuntimeRevisionServiceClient
               .listReasoningEngineRuntimeRevisions(request)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReasoningEngineRuntimeRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListReasoningEngineRuntimeRevisionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineRuntimeRevisionServiceClient.ListReasoningEngineRuntimeRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionServiceClient.ListReasoningEngineRuntimeRevisionsPagedResponse)` |   
  
### listReasoningEngineRuntimeRevisions(String parent)
    
    
    public final ReasoningEngineRuntimeRevisionServiceClient.ListReasoningEngineRuntimeRevisionsPagedResponse listReasoningEngineRuntimeRevisions(String parent)

Lists runtime revisions in a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       String parent =
           ReasoningEngineName.of("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]").toString();
       for (ReasoningEngineRuntimeRevision element :
           reasoningEngineRuntimeRevisionServiceClient
               .listReasoningEngineRuntimeRevisions(parent)
               .iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the ReasoningEngine to list the ReasoningEngineRuntimeRevisions from. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}`  
**Returns**  
---  
**Type** | **Description**  
`[ReasoningEngineRuntimeRevisionServiceClient.ListReasoningEngineRuntimeRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionServiceClient.ListReasoningEngineRuntimeRevisionsPagedResponse)` |   
  
### listReasoningEngineRuntimeRevisionsCallable()
    
    
    public final UnaryCallable<ListReasoningEngineRuntimeRevisionsRequest,ListReasoningEngineRuntimeRevisionsResponse> listReasoningEngineRuntimeRevisionsCallable()

Lists runtime revisions in a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       ListReasoningEngineRuntimeRevisionsRequest request =
           ListReasoningEngineRuntimeRevisionsRequest.newBuilder()
               .setParent(
                   ReasoningEngineName.of("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListReasoningEngineRuntimeRevisionsResponse response =
             reasoningEngineRuntimeRevisionServiceClient
                 .listReasoningEngineRuntimeRevisionsCallable()
                 .call(request);
         for (ReasoningEngineRuntimeRevision element :
             response.getReasoningEngineRuntimeRevisionsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReasoningEngineRuntimeRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListReasoningEngineRuntimeRevisionsRequest),[ListReasoningEngineRuntimeRevisionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListReasoningEngineRuntimeRevisionsResponse)>` |   
  
### listReasoningEngineRuntimeRevisionsPagedCallable()
    
    
    public final UnaryCallable<ListReasoningEngineRuntimeRevisionsRequest,ReasoningEngineRuntimeRevisionServiceClient.ListReasoningEngineRuntimeRevisionsPagedResponse> listReasoningEngineRuntimeRevisionsPagedCallable()

Lists runtime revisions in a reasoning engine.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       ListReasoningEngineRuntimeRevisionsRequest request =
           ListReasoningEngineRuntimeRevisionsRequest.newBuilder()
               .setParent(
                   ReasoningEngineName.of("[PROJECT]", "[LOCATION]", "[REASONING_ENGINE]")
                       .toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<ReasoningEngineRuntimeRevision> future =
           reasoningEngineRuntimeRevisionServiceClient
               .listReasoningEngineRuntimeRevisionsPagedCallable()
               .futureCall(request);
       // Do something.
       for (ReasoningEngineRuntimeRevision element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReasoningEngineRuntimeRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListReasoningEngineRuntimeRevisionsRequest),[ListReasoningEngineRuntimeRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ReasoningEngineRuntimeRevisionServiceClient.ListReasoningEngineRuntimeRevisionsPagedResponse)>` |   
  
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
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = reasoningEngineRuntimeRevisionServiceClient.setIamPolicy(request);
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
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
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
           reasoningEngineRuntimeRevisionServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response =
           reasoningEngineRuntimeRevisionServiceClient.testIamPermissions(request);
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
     try (ReasoningEngineRuntimeRevisionServiceClient reasoningEngineRuntimeRevisionServiceClient =
         ReasoningEngineRuntimeRevisionServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           reasoningEngineRuntimeRevisionServiceClient
               .testIamPermissionsCallable()
               .futureCall(request);
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
