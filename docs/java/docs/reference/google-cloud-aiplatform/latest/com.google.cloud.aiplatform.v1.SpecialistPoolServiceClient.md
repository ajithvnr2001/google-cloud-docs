---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPoolServiceClient
title: Class SpecialistPoolServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:40.253185+00:00
---

# Class SpecialistPoolServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPoolServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SpecialistPoolServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/SpecialistPoolServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: A service for creating and managing Customer SpecialistPools. When customers start Data Labeling jobs, they can reuse/create Specialist Pools to bring their own Specialists to label the data. Customers can add/remove Managers for the Specialist Pool on Cloud console, then Managers will get email notifications to manage Specialists and tasks on CrowdCompute console.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       SpecialistPoolName name =
           SpecialistPoolName.of("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]");
       SpecialistPool response = specialistPoolServiceClient.getSpecialistPool(name);
     }
     

Note: close() needs to be called on the SpecialistPoolServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateSpecialistPool |  Creates a SpecialistPool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSpecialistPoolAsync(CreateSpecialistPoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createSpecialistPoolAsync(LocationName parent, SpecialistPool specialistPool) 
  * createSpecialistPoolAsync(String parent, SpecialistPool specialistPool) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSpecialistPoolOperationCallable() 
  * createSpecialistPoolCallable() 

  
GetSpecialistPool |  Gets a SpecialistPool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSpecialistPool(GetSpecialistPoolRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSpecialistPool(SpecialistPoolName name) 
  * getSpecialistPool(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSpecialistPoolCallable() 

  
ListSpecialistPools |  Lists SpecialistPools in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSpecialistPools(ListSpecialistPoolsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSpecialistPools(LocationName parent) 
  * listSpecialistPools(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSpecialistPoolsPagedCallable() 
  * listSpecialistPoolsCallable() 

  
DeleteSpecialistPool |  Deletes a SpecialistPool as well as all Specialists in the pool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSpecialistPoolAsync(DeleteSpecialistPoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteSpecialistPoolAsync(SpecialistPoolName name) 
  * deleteSpecialistPoolAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSpecialistPoolOperationCallable() 
  * deleteSpecialistPoolCallable() 

  
UpdateSpecialistPool |  Updates a SpecialistPool. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSpecialistPoolAsync(UpdateSpecialistPoolRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * updateSpecialistPoolAsync(SpecialistPool specialistPool, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSpecialistPoolOperationCallable() 
  * updateSpecialistPoolCallable() 

  
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

This class can be customized by passing in a custom instance of SpecialistPoolServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SpecialistPoolServiceSettings specialistPoolServiceSettings =
         SpecialistPoolServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create(specialistPoolServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SpecialistPoolServiceSettings specialistPoolServiceSettings =
         SpecialistPoolServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create(specialistPoolServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SpecialistPoolServiceClient

## Static Methods 

### create()
    
    
    public static final SpecialistPoolServiceClient create()

Constructs an instance of SpecialistPoolServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[SpecialistPoolServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPoolServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SpecialistPoolServiceSettings settings)
    
    
    public static final SpecialistPoolServiceClient create(SpecialistPoolServiceSettings settings)

Constructs an instance of SpecialistPoolServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SpecialistPoolServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPoolServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SpecialistPoolServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPoolServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(SpecialistPoolServiceStub stub)
    
    
    public static final SpecialistPoolServiceClient create(SpecialistPoolServiceStub stub)

Constructs an instance of SpecialistPoolServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(SpecialistPoolServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SpecialistPoolServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.SpecialistPoolServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SpecialistPoolServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPoolServiceClient)` |   
  
## Constructors 

### SpecialistPoolServiceClient(SpecialistPoolServiceSettings settings)
    
    
    protected SpecialistPoolServiceClient(SpecialistPoolServiceSettings settings)

Constructs an instance of SpecialistPoolServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[SpecialistPoolServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPoolServiceSettings)`  
  
  
### SpecialistPoolServiceClient(SpecialistPoolServiceStub stub)
    
    
    protected SpecialistPoolServiceClient(SpecialistPoolServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SpecialistPoolServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.SpecialistPoolServiceStub)`  
  
  
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

### createSpecialistPoolAsync(@Nullable LocationName parent, SpecialistPool specialistPool)
    
    
    public final OperationFuture<SpecialistPool,CreateSpecialistPoolOperationMetadata> createSpecialistPoolAsync(@Nullable LocationName parent, SpecialistPool specialistPool)

Creates a SpecialistPool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       SpecialistPool specialistPool = SpecialistPool.newBuilder().build();
       SpecialistPool response =
           specialistPoolServiceClient.createSpecialistPoolAsync(parent, specialistPool).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The parent Project name for the new SpecialistPool. The form is `projects/{project}/locations/{location}`.  
`specialistPool` | `[SpecialistPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPool)`  
Required. The SpecialistPool to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[SpecialistPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPool),[CreateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateSpecialistPoolOperationMetadata)>` |   
  
### createSpecialistPoolAsync(CreateSpecialistPoolRequest request)
    
    
    public final OperationFuture<SpecialistPool,CreateSpecialistPoolOperationMetadata> createSpecialistPoolAsync(CreateSpecialistPoolRequest request)

Creates a SpecialistPool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       CreateSpecialistPoolRequest request =
           CreateSpecialistPoolRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSpecialistPool(SpecialistPool.newBuilder().build())
               .build();
       SpecialistPool response =
           specialistPoolServiceClient.createSpecialistPoolAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSpecialistPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateSpecialistPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[SpecialistPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPool),[CreateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateSpecialistPoolOperationMetadata)>` |   
  
### createSpecialistPoolAsync(String parent, SpecialistPool specialistPool)
    
    
    public final OperationFuture<SpecialistPool,CreateSpecialistPoolOperationMetadata> createSpecialistPoolAsync(String parent, SpecialistPool specialistPool)

Creates a SpecialistPool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       SpecialistPool specialistPool = SpecialistPool.newBuilder().build();
       SpecialistPool response =
           specialistPoolServiceClient.createSpecialistPoolAsync(parent, specialistPool).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent Project name for the new SpecialistPool. The form is `projects/{project}/locations/{location}`.  
`specialistPool` | `[SpecialistPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPool)`  
Required. The SpecialistPool to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[SpecialistPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPool),[CreateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateSpecialistPoolOperationMetadata)>` |   
  
### createSpecialistPoolCallable()
    
    
    public final UnaryCallable<CreateSpecialistPoolRequest,Operation> createSpecialistPoolCallable()

Creates a SpecialistPool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       CreateSpecialistPoolRequest request =
           CreateSpecialistPoolRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSpecialistPool(SpecialistPool.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           specialistPoolServiceClient.createSpecialistPoolCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSpecialistPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateSpecialistPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSpecialistPoolOperationCallable()
    
    
    public final OperationCallable<CreateSpecialistPoolRequest,SpecialistPool,CreateSpecialistPoolOperationMetadata> createSpecialistPoolOperationCallable()

Creates a SpecialistPool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       CreateSpecialistPoolRequest request =
           CreateSpecialistPoolRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setSpecialistPool(SpecialistPool.newBuilder().build())
               .build();
       OperationFuture<SpecialistPool, CreateSpecialistPoolOperationMetadata> future =
           specialistPoolServiceClient.createSpecialistPoolOperationCallable().futureCall(request);
       // Do something.
       SpecialistPool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateSpecialistPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateSpecialistPoolRequest),[SpecialistPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPool),[CreateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateSpecialistPoolOperationMetadata)>` |   
  
### deleteSpecialistPoolAsync(@Nullable SpecialistPoolName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteSpecialistPoolAsync(@Nullable SpecialistPoolName name)

Deletes a SpecialistPool as well as all Specialists in the pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       SpecialistPoolName name =
           SpecialistPoolName.of("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]");
       specialistPoolServiceClient.deleteSpecialistPoolAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.SpecialistPoolName`  
Required. The resource name of the SpecialistPool to delete. Format: `projects/{project}/locations/{location}/specialistPools/{specialist_pool}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteSpecialistPoolAsync(DeleteSpecialistPoolRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteSpecialistPoolAsync(DeleteSpecialistPoolRequest request)

Deletes a SpecialistPool as well as all Specialists in the pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       DeleteSpecialistPoolRequest request =
           DeleteSpecialistPoolRequest.newBuilder()
               .setName(
                   SpecialistPoolName.of("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]").toString())
               .setForce(true)
               .build();
       specialistPoolServiceClient.deleteSpecialistPoolAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSpecialistPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteSpecialistPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteSpecialistPoolAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteSpecialistPoolAsync(String name)

Deletes a SpecialistPool as well as all Specialists in the pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       String name =
           SpecialistPoolName.of("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]").toString();
       specialistPoolServiceClient.deleteSpecialistPoolAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the SpecialistPool to delete. Format: `projects/{project}/locations/{location}/specialistPools/{specialist_pool}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteSpecialistPoolCallable()
    
    
    public final UnaryCallable<DeleteSpecialistPoolRequest,Operation> deleteSpecialistPoolCallable()

Deletes a SpecialistPool as well as all Specialists in the pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       DeleteSpecialistPoolRequest request =
           DeleteSpecialistPoolRequest.newBuilder()
               .setName(
                   SpecialistPoolName.of("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]").toString())
               .setForce(true)
               .build();
       ApiFuture<Operation> future =
           specialistPoolServiceClient.deleteSpecialistPoolCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSpecialistPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteSpecialistPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSpecialistPoolOperationCallable()
    
    
    public final OperationCallable<DeleteSpecialistPoolRequest,Empty,DeleteOperationMetadata> deleteSpecialistPoolOperationCallable()

Deletes a SpecialistPool as well as all Specialists in the pool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       DeleteSpecialistPoolRequest request =
           DeleteSpecialistPoolRequest.newBuilder()
               .setName(
                   SpecialistPoolName.of("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]").toString())
               .setForce(true)
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           specialistPoolServiceClient.deleteSpecialistPoolOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSpecialistPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteSpecialistPoolRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = specialistPoolServiceClient.getIamPolicy(request);
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
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           specialistPoolServiceClient.getIamPolicyCallable().futureCall(request);
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
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = specialistPoolServiceClient.getLocation(request);
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
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           specialistPoolServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable SpecialistPoolServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.SpecialistPoolServiceSettings` |   
  
### getSpecialistPool(@Nullable SpecialistPoolName name)
    
    
    public final SpecialistPool getSpecialistPool(@Nullable SpecialistPoolName name)

Gets a SpecialistPool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       SpecialistPoolName name =
           SpecialistPoolName.of("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]");
       SpecialistPool response = specialistPoolServiceClient.getSpecialistPool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.SpecialistPoolName`  
Required. The name of the SpecialistPool resource. The form is `projects/{project}/locations/{location}/specialistPools/{specialist_pool}`.  
**Returns**  
---  
**Type** | **Description**  
`[SpecialistPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPool)` |   
  
### getSpecialistPool(GetSpecialistPoolRequest request)
    
    
    public final SpecialistPool getSpecialistPool(GetSpecialistPoolRequest request)

Gets a SpecialistPool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       GetSpecialistPoolRequest request =
           GetSpecialistPoolRequest.newBuilder()
               .setName(
                   SpecialistPoolName.of("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]").toString())
               .build();
       SpecialistPool response = specialistPoolServiceClient.getSpecialistPool(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSpecialistPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetSpecialistPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SpecialistPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPool)` |   
  
### getSpecialistPool(String name)
    
    
    public final SpecialistPool getSpecialistPool(String name)

Gets a SpecialistPool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       String name =
           SpecialistPoolName.of("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]").toString();
       SpecialistPool response = specialistPoolServiceClient.getSpecialistPool(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the SpecialistPool resource. The form is `projects/{project}/locations/{location}/specialistPools/{specialist_pool}`.  
**Returns**  
---  
**Type** | **Description**  
`[SpecialistPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPool)` |   
  
### getSpecialistPoolCallable()
    
    
    public final UnaryCallable<GetSpecialistPoolRequest,SpecialistPool> getSpecialistPoolCallable()

Gets a SpecialistPool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       GetSpecialistPoolRequest request =
           GetSpecialistPoolRequest.newBuilder()
               .setName(
                   SpecialistPoolName.of("[PROJECT]", "[LOCATION]", "[SPECIALIST_POOL]").toString())
               .build();
       ApiFuture<SpecialistPool> future =
           specialistPoolServiceClient.getSpecialistPoolCallable().futureCall(request);
       // Do something.
       SpecialistPool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSpecialistPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetSpecialistPoolRequest),[SpecialistPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPool)>` |   
  
### getStub()
    
    
    public SpecialistPoolServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[SpecialistPoolServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.SpecialistPoolServiceStub)` |   
  
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
    
    
    public final SpecialistPoolServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : specialistPoolServiceClient.listLocations(request).iterateAll()) {
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
`[SpecialistPoolServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPoolServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             specialistPoolServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,SpecialistPoolServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           specialistPoolServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPoolServiceClient.ListLocationsPagedResponse)>` |   
  
### listSpecialistPools(@Nullable LocationName parent)
    
    
    public final SpecialistPoolServiceClient.ListSpecialistPoolsPagedResponse listSpecialistPools(@Nullable LocationName parent)

Lists SpecialistPools in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (SpecialistPool element :
           specialistPoolServiceClient.listSpecialistPools(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The name of the SpecialistPool's parent resource. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[SpecialistPoolServiceClient.ListSpecialistPoolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPoolServiceClient.ListSpecialistPoolsPagedResponse)` |   
  
### listSpecialistPools(ListSpecialistPoolsRequest request)
    
    
    public final SpecialistPoolServiceClient.ListSpecialistPoolsPagedResponse listSpecialistPools(ListSpecialistPoolsRequest request)

Lists SpecialistPools in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       ListSpecialistPoolsRequest request =
           ListSpecialistPoolsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (SpecialistPool element :
           specialistPoolServiceClient.listSpecialistPools(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSpecialistPoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListSpecialistPoolsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SpecialistPoolServiceClient.ListSpecialistPoolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPoolServiceClient.ListSpecialistPoolsPagedResponse)` |   
  
### listSpecialistPools(String parent)
    
    
    public final SpecialistPoolServiceClient.ListSpecialistPoolsPagedResponse listSpecialistPools(String parent)

Lists SpecialistPools in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (SpecialistPool element :
           specialistPoolServiceClient.listSpecialistPools(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the SpecialistPool's parent resource. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[SpecialistPoolServiceClient.ListSpecialistPoolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPoolServiceClient.ListSpecialistPoolsPagedResponse)` |   
  
### listSpecialistPoolsCallable()
    
    
    public final UnaryCallable<ListSpecialistPoolsRequest,ListSpecialistPoolsResponse> listSpecialistPoolsCallable()

Lists SpecialistPools in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       ListSpecialistPoolsRequest request =
           ListSpecialistPoolsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListSpecialistPoolsResponse response =
             specialistPoolServiceClient.listSpecialistPoolsCallable().call(request);
         for (SpecialistPool element : response.getSpecialistPoolsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSpecialistPoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListSpecialistPoolsRequest),[ListSpecialistPoolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListSpecialistPoolsResponse)>` |   
  
### listSpecialistPoolsPagedCallable()
    
    
    public final UnaryCallable<ListSpecialistPoolsRequest,SpecialistPoolServiceClient.ListSpecialistPoolsPagedResponse> listSpecialistPoolsPagedCallable()

Lists SpecialistPools in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       ListSpecialistPoolsRequest request =
           ListSpecialistPoolsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<SpecialistPool> future =
           specialistPoolServiceClient.listSpecialistPoolsPagedCallable().futureCall(request);
       // Do something.
       for (SpecialistPool element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSpecialistPoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListSpecialistPoolsRequest),[ListSpecialistPoolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPoolServiceClient.ListSpecialistPoolsPagedResponse)>` |   
  
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
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = specialistPoolServiceClient.setIamPolicy(request);
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
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
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
           specialistPoolServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = specialistPoolServiceClient.testIamPermissions(request);
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
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           specialistPoolServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateSpecialistPoolAsync(SpecialistPool specialistPool, FieldMask updateMask)
    
    
    public final OperationFuture<SpecialistPool,UpdateSpecialistPoolOperationMetadata> updateSpecialistPoolAsync(SpecialistPool specialistPool, FieldMask updateMask)

Updates a SpecialistPool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       SpecialistPool specialistPool = SpecialistPool.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       SpecialistPool response =
           specialistPoolServiceClient.updateSpecialistPoolAsync(specialistPool, updateMask).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`specialistPool` | `[SpecialistPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPool)`  
Required. The SpecialistPool which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The update mask applies to the resource.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[SpecialistPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPool),[UpdateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateSpecialistPoolOperationMetadata)>` |   
  
### updateSpecialistPoolAsync(UpdateSpecialistPoolRequest request)
    
    
    public final OperationFuture<SpecialistPool,UpdateSpecialistPoolOperationMetadata> updateSpecialistPoolAsync(UpdateSpecialistPoolRequest request)

Updates a SpecialistPool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       UpdateSpecialistPoolRequest request =
           UpdateSpecialistPoolRequest.newBuilder()
               .setSpecialistPool(SpecialistPool.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       SpecialistPool response =
           specialistPoolServiceClient.updateSpecialistPoolAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSpecialistPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateSpecialistPoolRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[SpecialistPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPool),[UpdateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateSpecialistPoolOperationMetadata)>` |   
  
### updateSpecialistPoolCallable()
    
    
    public final UnaryCallable<UpdateSpecialistPoolRequest,Operation> updateSpecialistPoolCallable()

Updates a SpecialistPool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       UpdateSpecialistPoolRequest request =
           UpdateSpecialistPoolRequest.newBuilder()
               .setSpecialistPool(SpecialistPool.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           specialistPoolServiceClient.updateSpecialistPoolCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSpecialistPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateSpecialistPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSpecialistPoolOperationCallable()
    
    
    public final OperationCallable<UpdateSpecialistPoolRequest,SpecialistPool,UpdateSpecialistPoolOperationMetadata> updateSpecialistPoolOperationCallable()

Updates a SpecialistPool.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (SpecialistPoolServiceClient specialistPoolServiceClient =
         SpecialistPoolServiceClient.create()) {
       UpdateSpecialistPoolRequest request =
           UpdateSpecialistPoolRequest.newBuilder()
               .setSpecialistPool(SpecialistPool.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       OperationFuture<SpecialistPool, UpdateSpecialistPoolOperationMetadata> future =
           specialistPoolServiceClient.updateSpecialistPoolOperationCallable().futureCall(request);
       // Do something.
       SpecialistPool response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateSpecialistPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateSpecialistPoolRequest),[SpecialistPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SpecialistPool),[UpdateSpecialistPoolOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateSpecialistPoolOperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
