---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpointServiceClient
title: Class IndexEndpointServiceClient (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:54:04.831407+00:00
---

# Class IndexEndpointServiceClient (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpointServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class IndexEndpointServiceClient (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-aiplatform/google-cloud-aiplatform/src/main/java/com/google/cloud/aiplatform/v1/IndexEndpointServiceClient.java)| [Product Reference](https://cloud.google.com/vertex-ai/docs)| [REST Documentation](https://cloud.google.com/vertex-ai/docs/reference/rest)| [RPC Documentation](https://cloud.google.com/vertex-ai/docs/reference/rpc)  
---|---|---|---  
  
Service Description: A service for managing Vertex AI's IndexEndpoints.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       IndexEndpointName name = IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]");
       IndexEndpoint response = indexEndpointServiceClient.getIndexEndpoint(name);
     }
     

Note: close() needs to be called on the IndexEndpointServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateIndexEndpoint |  Creates an IndexEndpoint. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createIndexEndpointAsync(CreateIndexEndpointRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * createIndexEndpointAsync(LocationName parent, IndexEndpoint indexEndpoint) 
  * createIndexEndpointAsync(String parent, IndexEndpoint indexEndpoint) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createIndexEndpointOperationCallable() 
  * createIndexEndpointCallable() 

  
GetIndexEndpoint |  Gets an IndexEndpoint. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getIndexEndpoint(GetIndexEndpointRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getIndexEndpoint(IndexEndpointName name) 
  * getIndexEndpoint(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getIndexEndpointCallable() 

  
ListIndexEndpoints |  Lists IndexEndpoints in a Location. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listIndexEndpoints(ListIndexEndpointsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listIndexEndpoints(LocationName parent) 
  * listIndexEndpoints(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listIndexEndpointsPagedCallable() 
  * listIndexEndpointsCallable() 

  
UpdateIndexEndpoint |  Updates an IndexEndpoint. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateIndexEndpoint(UpdateIndexEndpointRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateIndexEndpoint(IndexEndpoint indexEndpoint, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateIndexEndpointCallable() 

  
DeleteIndexEndpoint |  Deletes an IndexEndpoint. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteIndexEndpointAsync(DeleteIndexEndpointRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deleteIndexEndpointAsync(IndexEndpointName name) 
  * deleteIndexEndpointAsync(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteIndexEndpointOperationCallable() 
  * deleteIndexEndpointCallable() 

  
DeployIndex |  Deploys an Index into this IndexEndpoint, creating a DeployedIndex within it. Only non-empty Indexes can be deployed. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deployIndexAsync(DeployIndexRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * deployIndexAsync(IndexEndpointName indexEndpoint, DeployedIndex deployedIndex) 
  * deployIndexAsync(String indexEndpoint, DeployedIndex deployedIndex) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deployIndexOperationCallable() 
  * deployIndexCallable() 

  
UndeployIndex |  Undeploys an Index from an IndexEndpoint, removing a DeployedIndex from it, and freeing all resources it's using. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * undeployIndexAsync(UndeployIndexRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * undeployIndexAsync(IndexEndpointName indexEndpoint, String deployedIndexId) 
  * undeployIndexAsync(String indexEndpoint, String deployedIndexId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * undeployIndexOperationCallable() 
  * undeployIndexCallable() 

  
MutateDeployedIndex |  Update an existing DeployedIndex under an IndexEndpoint. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * mutateDeployedIndexAsync(MutateDeployedIndexRequest request) 

Methods that return long-running operations have "Async" method variants that return `OperationFuture`, which is used to track polling of the service.

  * mutateDeployedIndexAsync(IndexEndpointName indexEndpoint, DeployedIndex deployedIndex) 
  * mutateDeployedIndexAsync(String indexEndpoint, DeployedIndex deployedIndex) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * mutateDeployedIndexOperationCallable() 
  * mutateDeployedIndexCallable() 

  
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

This class can be customized by passing in a custom instance of IndexEndpointServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     IndexEndpointServiceSettings indexEndpointServiceSettings =
         IndexEndpointServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create(indexEndpointServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     IndexEndpointServiceSettings indexEndpointServiceSettings =
         IndexEndpointServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create(indexEndpointServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > IndexEndpointServiceClient

## Static Methods 

### create()
    
    
    public static final IndexEndpointServiceClient create()

Constructs an instance of IndexEndpointServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[IndexEndpointServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpointServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(IndexEndpointServiceSettings settings)
    
    
    public static final IndexEndpointServiceClient create(IndexEndpointServiceSettings settings)

Constructs an instance of IndexEndpointServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[IndexEndpointServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpointServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IndexEndpointServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpointServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(IndexEndpointServiceStub stub)
    
    
    public static final IndexEndpointServiceClient create(IndexEndpointServiceStub stub)

Constructs an instance of IndexEndpointServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(IndexEndpointServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[IndexEndpointServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.IndexEndpointServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[IndexEndpointServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpointServiceClient)` |   
  
## Constructors 

### IndexEndpointServiceClient(IndexEndpointServiceSettings settings)
    
    
    protected IndexEndpointServiceClient(IndexEndpointServiceSettings settings)

Constructs an instance of IndexEndpointServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[IndexEndpointServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpointServiceSettings)`  
  
  
### IndexEndpointServiceClient(IndexEndpointServiceStub stub)
    
    
    protected IndexEndpointServiceClient(IndexEndpointServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[IndexEndpointServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.IndexEndpointServiceStub)`  
  
  
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

### createIndexEndpointAsync(@Nullable LocationName parent, IndexEndpoint indexEndpoint)
    
    
    public final OperationFuture<IndexEndpoint,CreateIndexEndpointOperationMetadata> createIndexEndpointAsync(@Nullable LocationName parent, IndexEndpoint indexEndpoint)

Creates an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       IndexEndpoint indexEndpoint = IndexEndpoint.newBuilder().build();
       IndexEndpoint response =
           indexEndpointServiceClient.createIndexEndpointAsync(parent, indexEndpoint).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location to create the IndexEndpoint in. Format: `projects/{project}/locations/{location}`  
`indexEndpoint` | `[IndexEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpoint)`  
Required. The IndexEndpoint to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[IndexEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpoint),[CreateIndexEndpointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateIndexEndpointOperationMetadata)>` |   
  
### createIndexEndpointAsync(CreateIndexEndpointRequest request)
    
    
    public final OperationFuture<IndexEndpoint,CreateIndexEndpointOperationMetadata> createIndexEndpointAsync(CreateIndexEndpointRequest request)

Creates an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       CreateIndexEndpointRequest request =
           CreateIndexEndpointRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setIndexEndpoint(IndexEndpoint.newBuilder().build())
               .build();
       IndexEndpoint response = indexEndpointServiceClient.createIndexEndpointAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateIndexEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[IndexEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpoint),[CreateIndexEndpointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateIndexEndpointOperationMetadata)>` |   
  
### createIndexEndpointAsync(String parent, IndexEndpoint indexEndpoint)
    
    
    public final OperationFuture<IndexEndpoint,CreateIndexEndpointOperationMetadata> createIndexEndpointAsync(String parent, IndexEndpoint indexEndpoint)

Creates an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       IndexEndpoint indexEndpoint = IndexEndpoint.newBuilder().build();
       IndexEndpoint response =
           indexEndpointServiceClient.createIndexEndpointAsync(parent, indexEndpoint).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location to create the IndexEndpoint in. Format: `projects/{project}/locations/{location}`  
`indexEndpoint` | `[IndexEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpoint)`  
Required. The IndexEndpoint to create.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[IndexEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpoint),[CreateIndexEndpointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateIndexEndpointOperationMetadata)>` |   
  
### createIndexEndpointCallable()
    
    
    public final UnaryCallable<CreateIndexEndpointRequest,Operation> createIndexEndpointCallable()

Creates an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       CreateIndexEndpointRequest request =
           CreateIndexEndpointRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setIndexEndpoint(IndexEndpoint.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           indexEndpointServiceClient.createIndexEndpointCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateIndexEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateIndexEndpointRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createIndexEndpointOperationCallable()
    
    
    public final OperationCallable<CreateIndexEndpointRequest,IndexEndpoint,CreateIndexEndpointOperationMetadata> createIndexEndpointOperationCallable()

Creates an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       CreateIndexEndpointRequest request =
           CreateIndexEndpointRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setIndexEndpoint(IndexEndpoint.newBuilder().build())
               .build();
       OperationFuture<IndexEndpoint, CreateIndexEndpointOperationMetadata> future =
           indexEndpointServiceClient.createIndexEndpointOperationCallable().futureCall(request);
       // Do something.
       IndexEndpoint response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateIndexEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateIndexEndpointRequest),[IndexEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpoint),[CreateIndexEndpointOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateIndexEndpointOperationMetadata)>` |   
  
### deleteIndexEndpointAsync(@Nullable IndexEndpointName name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteIndexEndpointAsync(@Nullable IndexEndpointName name)

Deletes an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       IndexEndpointName name = IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]");
       indexEndpointServiceClient.deleteIndexEndpointAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.IndexEndpointName`  
Required. The name of the IndexEndpoint resource to be deleted. Format: `projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteIndexEndpointAsync(DeleteIndexEndpointRequest request)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteIndexEndpointAsync(DeleteIndexEndpointRequest request)

Deletes an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       DeleteIndexEndpointRequest request =
           DeleteIndexEndpointRequest.newBuilder()
               .setName(
                   IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString())
               .build();
       indexEndpointServiceClient.deleteIndexEndpointAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteIndexEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteIndexEndpointAsync(String name)
    
    
    public final OperationFuture<Empty,DeleteOperationMetadata> deleteIndexEndpointAsync(String name)

Deletes an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       String name = IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString();
       indexEndpointServiceClient.deleteIndexEndpointAsync(name).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the IndexEndpoint resource to be deleted. Format: `projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}`  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deleteIndexEndpointCallable()
    
    
    public final UnaryCallable<DeleteIndexEndpointRequest,Operation> deleteIndexEndpointCallable()

Deletes an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       DeleteIndexEndpointRequest request =
           DeleteIndexEndpointRequest.newBuilder()
               .setName(
                   IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString())
               .build();
       ApiFuture<Operation> future =
           indexEndpointServiceClient.deleteIndexEndpointCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteIndexEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteIndexEndpointRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteIndexEndpointOperationCallable()
    
    
    public final OperationCallable<DeleteIndexEndpointRequest,Empty,DeleteOperationMetadata> deleteIndexEndpointOperationCallable()

Deletes an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       DeleteIndexEndpointRequest request =
           DeleteIndexEndpointRequest.newBuilder()
               .setName(
                   IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString())
               .build();
       OperationFuture<Empty, DeleteOperationMetadata> future =
           indexEndpointServiceClient.deleteIndexEndpointOperationCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteIndexEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteIndexEndpointRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteOperationMetadata)>` |   
  
### deployIndexAsync(@Nullable IndexEndpointName indexEndpoint, DeployedIndex deployedIndex)
    
    
    public final OperationFuture<DeployIndexResponse,DeployIndexOperationMetadata> deployIndexAsync(@Nullable IndexEndpointName indexEndpoint, DeployedIndex deployedIndex)

Deploys an Index into this IndexEndpoint, creating a DeployedIndex within it. Only non-empty Indexes can be deployed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       IndexEndpointName indexEndpoint =
           IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]");
       DeployedIndex deployedIndex = DeployedIndex.newBuilder().build();
       DeployIndexResponse response =
           indexEndpointServiceClient.deployIndexAsync(indexEndpoint, deployedIndex).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`indexEndpoint` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.IndexEndpointName`  
Required. The name of the IndexEndpoint resource into which to deploy an Index. Format: `projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}`  
`deployedIndex` | `[DeployedIndex](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedIndex)`  
Required. The DeployedIndex to be created within the IndexEndpoint.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeployIndexResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployIndexResponse),[DeployIndexOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployIndexOperationMetadata)>` |   
  
### deployIndexAsync(DeployIndexRequest request)
    
    
    public final OperationFuture<DeployIndexResponse,DeployIndexOperationMetadata> deployIndexAsync(DeployIndexRequest request)

Deploys an Index into this IndexEndpoint, creating a DeployedIndex within it. Only non-empty Indexes can be deployed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       DeployIndexRequest request =
           DeployIndexRequest.newBuilder()
               .setIndexEndpoint(
                   IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString())
               .setDeployedIndex(DeployedIndex.newBuilder().build())
               .build();
       DeployIndexResponse response = indexEndpointServiceClient.deployIndexAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeployIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployIndexRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeployIndexResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployIndexResponse),[DeployIndexOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployIndexOperationMetadata)>` |   
  
### deployIndexAsync(String indexEndpoint, DeployedIndex deployedIndex)
    
    
    public final OperationFuture<DeployIndexResponse,DeployIndexOperationMetadata> deployIndexAsync(String indexEndpoint, DeployedIndex deployedIndex)

Deploys an Index into this IndexEndpoint, creating a DeployedIndex within it. Only non-empty Indexes can be deployed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       String indexEndpoint =
           IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString();
       DeployedIndex deployedIndex = DeployedIndex.newBuilder().build();
       DeployIndexResponse response =
           indexEndpointServiceClient.deployIndexAsync(indexEndpoint, deployedIndex).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`indexEndpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the IndexEndpoint resource into which to deploy an Index. Format: `projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}`  
`deployedIndex` | `[DeployedIndex](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedIndex)`  
Required. The DeployedIndex to be created within the IndexEndpoint.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[DeployIndexResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployIndexResponse),[DeployIndexOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployIndexOperationMetadata)>` |   
  
### deployIndexCallable()
    
    
    public final UnaryCallable<DeployIndexRequest,Operation> deployIndexCallable()

Deploys an Index into this IndexEndpoint, creating a DeployedIndex within it. Only non-empty Indexes can be deployed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       DeployIndexRequest request =
           DeployIndexRequest.newBuilder()
               .setIndexEndpoint(
                   IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString())
               .setDeployedIndex(DeployedIndex.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           indexEndpointServiceClient.deployIndexCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeployIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployIndexRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deployIndexOperationCallable()
    
    
    public final OperationCallable<DeployIndexRequest,DeployIndexResponse,DeployIndexOperationMetadata> deployIndexOperationCallable()

Deploys an Index into this IndexEndpoint, creating a DeployedIndex within it. Only non-empty Indexes can be deployed.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       DeployIndexRequest request =
           DeployIndexRequest.newBuilder()
               .setIndexEndpoint(
                   IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString())
               .setDeployedIndex(DeployedIndex.newBuilder().build())
               .build();
       OperationFuture<DeployIndexResponse, DeployIndexOperationMetadata> future =
           indexEndpointServiceClient.deployIndexOperationCallable().futureCall(request);
       // Do something.
       DeployIndexResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeployIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployIndexRequest),[DeployIndexResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployIndexResponse),[DeployIndexOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployIndexOperationMetadata)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public final Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policyif the resource exists and does not have a policy set.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       Policy response = indexEndpointServiceClient.getIamPolicy(request);
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
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       GetIamPolicyRequest request =
           GetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setOptions(GetPolicyOptions.newBuilder().build())
               .build();
       ApiFuture<Policy> future =
           indexEndpointServiceClient.getIamPolicyCallable().futureCall(request);
       // Do something.
       Policy response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getIndexEndpoint(@Nullable IndexEndpointName name)
    
    
    public final IndexEndpoint getIndexEndpoint(@Nullable IndexEndpointName name)

Gets an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       IndexEndpointName name = IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]");
       IndexEndpoint response = indexEndpointServiceClient.getIndexEndpoint(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.IndexEndpointName`  
Required. The name of the IndexEndpoint resource. Format: `projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}`  
**Returns**  
---  
**Type** | **Description**  
`[IndexEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpoint)` |   
  
### getIndexEndpoint(GetIndexEndpointRequest request)
    
    
    public final IndexEndpoint getIndexEndpoint(GetIndexEndpointRequest request)

Gets an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       GetIndexEndpointRequest request =
           GetIndexEndpointRequest.newBuilder()
               .setName(
                   IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString())
               .build();
       IndexEndpoint response = indexEndpointServiceClient.getIndexEndpoint(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIndexEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IndexEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpoint)` |   
  
### getIndexEndpoint(String name)
    
    
    public final IndexEndpoint getIndexEndpoint(String name)

Gets an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       String name = IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString();
       IndexEndpoint response = indexEndpointServiceClient.getIndexEndpoint(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the IndexEndpoint resource. Format: `projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}`  
**Returns**  
---  
**Type** | **Description**  
`[IndexEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpoint)` |   
  
### getIndexEndpointCallable()
    
    
    public final UnaryCallable<GetIndexEndpointRequest,IndexEndpoint> getIndexEndpointCallable()

Gets an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       GetIndexEndpointRequest request =
           GetIndexEndpointRequest.newBuilder()
               .setName(
                   IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString())
               .build();
       ApiFuture<IndexEndpoint> future =
           indexEndpointServiceClient.getIndexEndpointCallable().futureCall(request);
       // Do something.
       IndexEndpoint response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetIndexEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetIndexEndpointRequest),[IndexEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpoint)>` |   
  
### getLocation(GetLocationRequest request)
    
    
    public final Location getLocation(GetLocationRequest request)

Gets information about a location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       Location response = indexEndpointServiceClient.getLocation(request);
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
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       GetLocationRequest request = GetLocationRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Location> future =
           indexEndpointServiceClient.getLocationCallable().futureCall(request);
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
    
    
    public final @Nullable IndexEndpointServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.IndexEndpointServiceSettings` |   
  
### getStub()
    
    
    public IndexEndpointServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[IndexEndpointServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.stub.IndexEndpointServiceStub)` |   
  
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
  
### listIndexEndpoints(@Nullable LocationName parent)
    
    
    public final IndexEndpointServiceClient.ListIndexEndpointsPagedResponse listIndexEndpoints(@Nullable LocationName parent)

Lists IndexEndpoints in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       LocationName parent = LocationName.of("[PROJECT]", "[LOCATION]");
       for (IndexEndpoint element :
           indexEndpointServiceClient.listIndexEndpoints(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.LocationName`  
Required. The resource name of the Location from which to list the IndexEndpoints. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[IndexEndpointServiceClient.ListIndexEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpointServiceClient.ListIndexEndpointsPagedResponse)` |   
  
### listIndexEndpoints(ListIndexEndpointsRequest request)
    
    
    public final IndexEndpointServiceClient.ListIndexEndpointsPagedResponse listIndexEndpoints(ListIndexEndpointsRequest request)

Lists IndexEndpoints in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       ListIndexEndpointsRequest request =
           ListIndexEndpointsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       for (IndexEndpoint element :
           indexEndpointServiceClient.listIndexEndpoints(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListIndexEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListIndexEndpointsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IndexEndpointServiceClient.ListIndexEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpointServiceClient.ListIndexEndpointsPagedResponse)` |   
  
### listIndexEndpoints(String parent)
    
    
    public final IndexEndpointServiceClient.ListIndexEndpointsPagedResponse listIndexEndpoints(String parent)

Lists IndexEndpoints in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       String parent = LocationName.of("[PROJECT]", "[LOCATION]").toString();
       for (IndexEndpoint element :
           indexEndpointServiceClient.listIndexEndpoints(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the Location from which to list the IndexEndpoints. Format: `projects/{project}/locations/{location}`  
**Returns**  
---  
**Type** | **Description**  
`[IndexEndpointServiceClient.ListIndexEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpointServiceClient.ListIndexEndpointsPagedResponse)` |   
  
### listIndexEndpointsCallable()
    
    
    public final UnaryCallable<ListIndexEndpointsRequest,ListIndexEndpointsResponse> listIndexEndpointsCallable()

Lists IndexEndpoints in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       ListIndexEndpointsRequest request =
           ListIndexEndpointsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       while (true) {
         ListIndexEndpointsResponse response =
             indexEndpointServiceClient.listIndexEndpointsCallable().call(request);
         for (IndexEndpoint element : response.getIndexEndpointsList()) {
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
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListIndexEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListIndexEndpointsRequest),[ListIndexEndpointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListIndexEndpointsResponse)>` |   
  
### listIndexEndpointsPagedCallable()
    
    
    public final UnaryCallable<ListIndexEndpointsRequest,IndexEndpointServiceClient.ListIndexEndpointsPagedResponse> listIndexEndpointsPagedCallable()

Lists IndexEndpoints in a Location.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       ListIndexEndpointsRequest request =
           ListIndexEndpointsRequest.newBuilder()
               .setParent(LocationName.of("[PROJECT]", "[LOCATION]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setReadMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<IndexEndpoint> future =
           indexEndpointServiceClient.listIndexEndpointsPagedCallable().futureCall(request);
       // Do something.
       for (IndexEndpoint element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListIndexEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListIndexEndpointsRequest),[ListIndexEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpointServiceClient.ListIndexEndpointsPagedResponse)>` |   
  
### listLocations(ListLocationsRequest request)
    
    
    public final IndexEndpointServiceClient.ListLocationsPagedResponse listLocations(ListLocationsRequest request)

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Location element : indexEndpointServiceClient.listLocations(request).iterateAll()) {
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
`[IndexEndpointServiceClient.ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpointServiceClient.ListLocationsPagedResponse)` |   
  
### listLocationsCallable()
    
    
    public final UnaryCallable<ListLocationsRequest,ListLocationsResponse> listLocationsCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListLocationsResponse response =
             indexEndpointServiceClient.listLocationsCallable().call(request);
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
    
    
    public final UnaryCallable<ListLocationsRequest,IndexEndpointServiceClient.ListLocationsPagedResponse> listLocationsPagedCallable()

Lists information about the supported locations for this service.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       ListLocationsRequest request =
           ListLocationsRequest.newBuilder()
               .setName("name3373707")
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Location> future =
           indexEndpointServiceClient.listLocationsPagedCallable().futureCall(request);
       // Do something.
       for (Location element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.cloud.location.ListLocationsRequest,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpointServiceClient.ListLocationsPagedResponse)>` |   
  
### mutateDeployedIndexAsync(@Nullable IndexEndpointName indexEndpoint, DeployedIndex deployedIndex)
    
    
    public final OperationFuture<MutateDeployedIndexResponse,MutateDeployedIndexOperationMetadata> mutateDeployedIndexAsync(@Nullable IndexEndpointName indexEndpoint, DeployedIndex deployedIndex)

Update an existing DeployedIndex under an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       IndexEndpointName indexEndpoint =
           IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]");
       DeployedIndex deployedIndex = DeployedIndex.newBuilder().build();
       MutateDeployedIndexResponse response =
           indexEndpointServiceClient.mutateDeployedIndexAsync(indexEndpoint, deployedIndex).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`indexEndpoint` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.IndexEndpointName`  
Required. The name of the IndexEndpoint resource into which to deploy an Index. Format: `projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}`  
`deployedIndex` | `[DeployedIndex](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedIndex)`  
Required. The DeployedIndex to be updated within the IndexEndpoint. Currently, the updatable fields are DeployedIndex.automatic_resources and DeployedIndex.dedicated_resources  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MutateDeployedIndexResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedIndexResponse),[MutateDeployedIndexOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedIndexOperationMetadata)>` |   
  
### mutateDeployedIndexAsync(MutateDeployedIndexRequest request)
    
    
    public final OperationFuture<MutateDeployedIndexResponse,MutateDeployedIndexOperationMetadata> mutateDeployedIndexAsync(MutateDeployedIndexRequest request)

Update an existing DeployedIndex under an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       MutateDeployedIndexRequest request =
           MutateDeployedIndexRequest.newBuilder()
               .setIndexEndpoint(
                   IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString())
               .setDeployedIndex(DeployedIndex.newBuilder().build())
               .build();
       MutateDeployedIndexResponse response =
           indexEndpointServiceClient.mutateDeployedIndexAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MutateDeployedIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedIndexRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MutateDeployedIndexResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedIndexResponse),[MutateDeployedIndexOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedIndexOperationMetadata)>` |   
  
### mutateDeployedIndexAsync(String indexEndpoint, DeployedIndex deployedIndex)
    
    
    public final OperationFuture<MutateDeployedIndexResponse,MutateDeployedIndexOperationMetadata> mutateDeployedIndexAsync(String indexEndpoint, DeployedIndex deployedIndex)

Update an existing DeployedIndex under an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       String indexEndpoint =
           IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString();
       DeployedIndex deployedIndex = DeployedIndex.newBuilder().build();
       MutateDeployedIndexResponse response =
           indexEndpointServiceClient.mutateDeployedIndexAsync(indexEndpoint, deployedIndex).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`indexEndpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the IndexEndpoint resource into which to deploy an Index. Format: `projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}`  
`deployedIndex` | `[DeployedIndex](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeployedIndex)`  
Required. The DeployedIndex to be updated within the IndexEndpoint. Currently, the updatable fields are DeployedIndex.automatic_resources and DeployedIndex.dedicated_resources  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[MutateDeployedIndexResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedIndexResponse),[MutateDeployedIndexOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedIndexOperationMetadata)>` |   
  
### mutateDeployedIndexCallable()
    
    
    public final UnaryCallable<MutateDeployedIndexRequest,Operation> mutateDeployedIndexCallable()

Update an existing DeployedIndex under an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       MutateDeployedIndexRequest request =
           MutateDeployedIndexRequest.newBuilder()
               .setIndexEndpoint(
                   IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString())
               .setDeployedIndex(DeployedIndex.newBuilder().build())
               .build();
       ApiFuture<Operation> future =
           indexEndpointServiceClient.mutateDeployedIndexCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MutateDeployedIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedIndexRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### mutateDeployedIndexOperationCallable()
    
    
    public final OperationCallable<MutateDeployedIndexRequest,MutateDeployedIndexResponse,MutateDeployedIndexOperationMetadata> mutateDeployedIndexOperationCallable()

Update an existing DeployedIndex under an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       MutateDeployedIndexRequest request =
           MutateDeployedIndexRequest.newBuilder()
               .setIndexEndpoint(
                   IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString())
               .setDeployedIndex(DeployedIndex.newBuilder().build())
               .build();
       OperationFuture<MutateDeployedIndexResponse, MutateDeployedIndexOperationMetadata> future =
           indexEndpointServiceClient.mutateDeployedIndexOperationCallable().futureCall(request);
       // Do something.
       MutateDeployedIndexResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[MutateDeployedIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedIndexRequest),[MutateDeployedIndexResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedIndexResponse),[MutateDeployedIndexOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MutateDeployedIndexOperationMetadata)>` |   
  
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
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       SetIamPolicyRequest request =
           SetIamPolicyRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .setPolicy(Policy.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Policy response = indexEndpointServiceClient.setIamPolicy(request);
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
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
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
           indexEndpointServiceClient.setIamPolicyCallable().futureCall(request);
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
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       TestIamPermissionsResponse response = indexEndpointServiceClient.testIamPermissions(request);
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
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       TestIamPermissionsRequest request =
           TestIamPermissionsRequest.newBuilder()
               .setResource(
                   EndpointName.ofProjectLocationEndpointName(
                           "[PROJECT]", "[LOCATION]", "[ENDPOINT]")
                       .toString())
               .addAllPermissions(new ArrayList<String>())
               .build();
       ApiFuture<TestIamPermissionsResponse> future =
           indexEndpointServiceClient.testIamPermissionsCallable().futureCall(request);
       // Do something.
       TestIamPermissionsResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### undeployIndexAsync(@Nullable IndexEndpointName indexEndpoint, String deployedIndexId)
    
    
    public final OperationFuture<UndeployIndexResponse,UndeployIndexOperationMetadata> undeployIndexAsync(@Nullable IndexEndpointName indexEndpoint, String deployedIndexId)

Undeploys an Index from an IndexEndpoint, removing a DeployedIndex from it, and freeing all resources it's using.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       IndexEndpointName indexEndpoint =
           IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]");
       String deployedIndexId = "deployedIndexId-1101212953";
       UndeployIndexResponse response =
           indexEndpointServiceClient.undeployIndexAsync(indexEndpoint, deployedIndexId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`indexEndpoint` | `@org.jspecify.annotations.Nullable com.google.cloud.aiplatform.v1.IndexEndpointName`  
Required. The name of the IndexEndpoint resource from which to undeploy an Index. Format: `projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}`  
`deployedIndexId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the DeployedIndex to be undeployed from the IndexEndpoint.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UndeployIndexResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployIndexResponse),[UndeployIndexOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployIndexOperationMetadata)>` |   
  
### undeployIndexAsync(UndeployIndexRequest request)
    
    
    public final OperationFuture<UndeployIndexResponse,UndeployIndexOperationMetadata> undeployIndexAsync(UndeployIndexRequest request)

Undeploys an Index from an IndexEndpoint, removing a DeployedIndex from it, and freeing all resources it's using.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       UndeployIndexRequest request =
           UndeployIndexRequest.newBuilder()
               .setIndexEndpoint(
                   IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString())
               .setDeployedIndexId("deployedIndexId-1101212953")
               .build();
       UndeployIndexResponse response = indexEndpointServiceClient.undeployIndexAsync(request).get();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UndeployIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployIndexRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UndeployIndexResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployIndexResponse),[UndeployIndexOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployIndexOperationMetadata)>` |   
  
### undeployIndexAsync(String indexEndpoint, String deployedIndexId)
    
    
    public final OperationFuture<UndeployIndexResponse,UndeployIndexOperationMetadata> undeployIndexAsync(String indexEndpoint, String deployedIndexId)

Undeploys an Index from an IndexEndpoint, removing a DeployedIndex from it, and freeing all resources it's using.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       String indexEndpoint =
           IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString();
       String deployedIndexId = "deployedIndexId-1101212953";
       UndeployIndexResponse response =
           indexEndpointServiceClient.undeployIndexAsync(indexEndpoint, deployedIndexId).get();
     }
     

**Parameters**  
---  
**Name** | **Description**  
`indexEndpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the IndexEndpoint resource from which to undeploy an Index. Format: `projects/{project}/locations/{location}/indexEndpoints/{index_endpoint}`  
`deployedIndexId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The ID of the DeployedIndex to be undeployed from the IndexEndpoint.  
**Returns**  
---  
**Type** | **Description**  
`[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html)<[UndeployIndexResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployIndexResponse),[UndeployIndexOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployIndexOperationMetadata)>` |   
  
### undeployIndexCallable()
    
    
    public final UnaryCallable<UndeployIndexRequest,Operation> undeployIndexCallable()

Undeploys an Index from an IndexEndpoint, removing a DeployedIndex from it, and freeing all resources it's using.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       UndeployIndexRequest request =
           UndeployIndexRequest.newBuilder()
               .setIndexEndpoint(
                   IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString())
               .setDeployedIndexId("deployedIndexId-1101212953")
               .build();
       ApiFuture<Operation> future =
           indexEndpointServiceClient.undeployIndexCallable().futureCall(request);
       // Do something.
       Operation response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UndeployIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployIndexRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### undeployIndexOperationCallable()
    
    
    public final OperationCallable<UndeployIndexRequest,UndeployIndexResponse,UndeployIndexOperationMetadata> undeployIndexOperationCallable()

Undeploys an Index from an IndexEndpoint, removing a DeployedIndex from it, and freeing all resources it's using.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       UndeployIndexRequest request =
           UndeployIndexRequest.newBuilder()
               .setIndexEndpoint(
                   IndexEndpointName.of("[PROJECT]", "[LOCATION]", "[INDEX_ENDPOINT]").toString())
               .setDeployedIndexId("deployedIndexId-1101212953")
               .build();
       OperationFuture<UndeployIndexResponse, UndeployIndexOperationMetadata> future =
           indexEndpointServiceClient.undeployIndexOperationCallable().futureCall(request);
       // Do something.
       UndeployIndexResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UndeployIndexRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployIndexRequest),[UndeployIndexResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployIndexResponse),[UndeployIndexOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UndeployIndexOperationMetadata)>` |   
  
### updateIndexEndpoint(IndexEndpoint indexEndpoint, FieldMask updateMask)
    
    
    public final IndexEndpoint updateIndexEndpoint(IndexEndpoint indexEndpoint, FieldMask updateMask)

Updates an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       IndexEndpoint indexEndpoint = IndexEndpoint.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       IndexEndpoint response =
           indexEndpointServiceClient.updateIndexEndpoint(indexEndpoint, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`indexEndpoint` | `[IndexEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpoint)`  
Required. The IndexEndpoint which replaces the resource on the server.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The update mask applies to the resource. See google.protobuf.FieldMask.  
**Returns**  
---  
**Type** | **Description**  
`[IndexEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpoint)` |   
  
### updateIndexEndpoint(UpdateIndexEndpointRequest request)
    
    
    public final IndexEndpoint updateIndexEndpoint(UpdateIndexEndpointRequest request)

Updates an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       UpdateIndexEndpointRequest request =
           UpdateIndexEndpointRequest.newBuilder()
               .setIndexEndpoint(IndexEndpoint.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       IndexEndpoint response = indexEndpointServiceClient.updateIndexEndpoint(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateIndexEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateIndexEndpointRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[IndexEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpoint)` |   
  
### updateIndexEndpointCallable()
    
    
    public final UnaryCallable<UpdateIndexEndpointRequest,IndexEndpoint> updateIndexEndpointCallable()

Updates an IndexEndpoint.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (IndexEndpointServiceClient indexEndpointServiceClient =
         IndexEndpointServiceClient.create()) {
       UpdateIndexEndpointRequest request =
           UpdateIndexEndpointRequest.newBuilder()
               .setIndexEndpoint(IndexEndpoint.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<IndexEndpoint> future =
           indexEndpointServiceClient.updateIndexEndpointCallable().futureCall(request);
       // Do something.
       IndexEndpoint response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateIndexEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateIndexEndpointRequest),[IndexEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.IndexEndpoint)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
